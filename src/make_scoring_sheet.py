"""Day 4: build the BLIND scoring sheet from the full run (rubric v1.2 §7).

All answers from all experiments are shuffled (fixed seed) and given blind ids S001…S180. The experiment
label goes into a separate key file that is not opened until scoring is finished.

To keep the sheet blind, each answer is shown as the user sees it MINUS lines that would reveal the
experiment: the licence notices (identical everywhere) and the "no-RAG experiment" warning. Remaining limit
(rubric §7): answers without quotes can still hint at a no-RAG experiment.

Usage:  .venv/bin/python src/make_scoring_sheet.py [--tag full]
Writes: results/scores/<tag>/items.jsonl   one blind item per answer (question, answer, gold)
        results/scores/<tag>/_key.json     blind id → experiment (DO NOT OPEN until scoring is done)
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ROOT, load_config  # noqa: E402
from pipeline import NOTICES  # noqa: E402

SEED = 2026
REVEALING = ("Answered without retrieving the law (no-RAG experiment)",)


def blind_text(answer: str) -> str:
    keep = []
    for line in answer.split("\n"):
        if line.strip() in NOTICES.values() or any(r in line for r in REVEALING):
            continue
        keep.append(line)
    return "\n".join(keep).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="full")
    a = ap.parse_args()
    cfg = load_config()
    gold = {q["id"]: q for q in map(json.loads, open(cfg["paths"]["evaluation"], encoding="utf-8"))}
    run_dir, out_dir = ROOT / "results/runs" / a.tag, ROOT / "results/scores" / a.tag
    out_dir.mkdir(parents=True, exist_ok=True)

    items = []
    for f in sorted(run_dir.glob("[A-F].jsonl")):
        for r in map(json.loads, open(f, encoding="utf-8")):
            q = gold[r["id"]]
            items.append({"experiment": f.stem, "qid": r["id"], "category": q["category"], "question": q["question"],
                          "answer": blind_text(r["answer"]) if "answer" in r else f"[pipeline error: {r.get('error')}]",
                          "gold": {j: {"answer": g["answer"], "key_facts": g["key_facts"], "sections": g["sections"]}
                                   for j, g in q["gold"].items()},
                          "comparison": q["comparison"], "abstain": q["abstain"],
                          "expected_abstain": q["expected_abstain"], "gold_chunks": q["gold_chunks"]})
    random.Random(SEED).shuffle(items)
    key = {}
    with open(out_dir / "items.jsonl", "w", encoding="utf-8") as fh:
        for i, it in enumerate(items, 1):
            bid = f"S{i:03d}"
            key[bid] = {"experiment": it.pop("experiment"), "qid": it["qid"]}
            fh.write(json.dumps({"blind_id": bid, **it}, ensure_ascii=False) + "\n")
    (out_dir / "_key.json").write_text(json.dumps(key, indent=1))
    print(f"{len(items)} blind items → {out_dir/'items.jsonl'} (key in _key.json, keep closed)")


if __name__ == "__main__":
    main()
