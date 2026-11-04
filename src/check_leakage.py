"""Step 2.8: prove the training data can't leak test answers. One report, five checks.

1. Split roles: every excerpt in train/val comes from a `train_pool` section.
2. Test evidence: no train/val excerpt uses a section that a test question relies on (gold sections),
   in either jurisdiction.
3. Train vs. validation: no section appears in both (exact section and base section).
4. Text overlap: no 13-word sequence from a test_only/exclude section, or from a test gold section,
   appears anywhere in the training/validation conversations (catches copied or quoted law).
5. Question similarity: each train/val question vs. each test question (MiniLM cosine);
   flags near-duplicates >= 0.85 and lists the 5 closest pairs.

Usage:  .venv/bin/python src/check_leakage.py
Writes: results/leakage_report.json   (exit code 1 if any check fails)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pandas as pd
from sentence_transformers import SentenceTransformer

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ROOT, load_config  # noqa: E402

NGRAM = 13
SIM_FLAG = 0.85
JUR = {"Ontario": "Ontario", "British Columbia": "British Columbia"}


def base(section: str) -> str:
    return re.sub(r"\(.*", "", section.strip())


def ngrams(text: str, n: int = NGRAM) -> set[tuple[str, ...]]:
    w = re.findall(r"[a-z0-9]+", text.lower())
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def load_sft(path: Path) -> list[dict]:
    out = []
    for line in open(path, encoding="utf-8"):
        ex = json.loads(line)
        secs = []
        for s in ex["sections"]:                      # e.g. "Ontario s.8.5(1)", "British Columbia s.52"
            jur, sec = s.rsplit(" s.", 1)
            secs.append((jur, sec))
        user = ex["messages"][1]["content"]
        out.append({"id": ex["id"], "sections": secs,
                    "question": re.search(r"Question: (.+)", user).group(1),
                    "text": " ".join(m["content"] for m in ex["messages"][1:])})
    return out


def main():
    cfg = load_config()
    kb = pd.read_json(cfg["paths"]["kb_sections"], lines=True, dtype={"section": str})
    role = {(r.jurisdiction, r.section): r.split_role for r in kb.itertuples()}
    test = [json.loads(l) for l in open(cfg["paths"]["evaluation"], encoding="utf-8")]
    train, val = load_sft(ROOT / "data/train.jsonl"), load_sft(ROOT / "data/val.jsonl")
    sft = train + val
    checks = {}

    # 1. split roles
    bad = [(e["id"], j, s, role.get((j, base(s)))) for e in sft for j, s in e["sections"]
           if role.get((j, base(s))) != "train_pool"]
    checks["1_all_excerpts_from_train_pool"] = {"pass": not bad, "violations": bad}

    # 2. test gold sections never used in training
    gold = {(j, s) for q in test for j, g in q["gold"].items() for s in g["sections"]}
    bad = [(e["id"], j, s) for e in sft for j, s in e["sections"] if (j, base(s)) in gold]
    checks["2_no_test_gold_sections_in_training"] = {"pass": not bad, "test_gold_sections": len(gold),
                                                     "violations": bad}

    # 3. train vs val sections
    tr = {(j, s) for e in train for j, s in e["sections"]}
    va = {(j, s) for e in val for j, s in e["sections"]}
    exact = sorted(tr & va)
    base_overlap = sorted({(j, base(s)) for j, s in tr} & {(j, base(s)) for j, s in va})
    checks["3_train_val_section_overlap"] = {"pass": not exact, "exact_overlap": exact,
                                             "base_section_overlap_info": base_overlap}

    # 4. 13-word overlap with held-out law
    held = kb[kb["split_role"].isin(["test_only", "exclude"]) |
              kb.apply(lambda r: (r.jurisdiction, r.section) in gold, axis=1)]
    held_ngrams = {}
    for r in held.itertuples():
        for g in ngrams(r.text):
            held_ngrams.setdefault(g, f"{r.jurisdiction} s.{r.section}")
    hits = []
    for e in sft:
        shared = ngrams(e["text"]) & held_ngrams.keys()
        if shared:
            g = next(iter(shared))
            hits.append({"id": e["id"], "shared_ngrams": len(shared), "example": " ".join(g),
                         "from": held_ngrams[g]})
    checks["4_no_13gram_overlap_with_held_out_law"] = {"pass": not hits, "held_out_sections": len(held),
                                                       "hits": hits}

    # 5. question similarity
    model = SentenceTransformer(cfg["embedding_model"])
    a = model.encode([e["question"] for e in sft], normalize_embeddings=True)
    b = model.encode([q["question"] for q in test], normalize_embeddings=True)
    sim = a @ b.T
    pairs = sorted(((float(sim[i, j]), sft[i]["id"], test[j]["id"], sft[i]["question"], test[j]["question"])
                    for i in range(len(sft)) for j in range(len(test))), reverse=True)
    flagged = [p for p in pairs if p[0] >= SIM_FLAG]
    checks["5_no_near_duplicate_questions"] = {
        "pass": not flagged, "threshold": SIM_FLAG, "flagged": flagged,
        "closest_5": [{"cosine": round(s, 3), "train_val": i, "test": t, "train_val_q": qi, "test_q": qt}
                      for s, i, t, qi, qt in pairs[:5]]}

    report = {"all_pass": all(c["pass"] for c in checks.values()),
              "examples_checked": {"train": len(train), "val": len(val), "test_questions": len(test)},
              "checks": checks}
    out = ROOT / "results/leakage_report.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    for name, c in checks.items():
        print(f"{'PASS' if c['pass'] else 'FAIL'}  {name}")
    print("closest question pairs:")
    for p in checks["5_no_near_duplicate_questions"]["closest_5"]:
        print(f"  {p['cosine']:.3f}  {p['train_val']} ↔ {p['test']}: {p['train_val_q']!r} / {p['test_q']!r}")
    print(f"Wrote {out}")
    sys.exit(0 if report["all_pass"] else 1)


if __name__ == "__main__":
    main()
