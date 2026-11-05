"""Rubric v1.2 §7.3: re-score a random 10% of answers without seeing the first scores; report agreement.

make:  picks 18 random answers (seed 7) and writes results/scores/<tag>/rescore_sheet.md with every label blank (**?**).
       The key facts and claims to judge are listed (same items as the first scoring) so labels can be compared one to one.
score: reads the filled-in sheet and compares each label with final_judgments.jsonl → agreement rate.

Fill in each **?** with one of:
  key facts:  Correct | Partial | Incorrect | Missing
  claims:     Supported | Unsupported   and   Supports | Doesn't support | Invalid | None
  abstention: 1 | 0 | n/a        false abstention: yes | no

Usage:  .venv/bin/python src/consistency_check.py make  [--tag full]
        .venv/bin/python src/consistency_check.py score [--tag full]
Writes: results/scores/<tag>/consistency.json
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ROOT  # noqa: E402

SEED, SHARE = 7, 0.10
SHORT = {"Ontario": "ON", "British Columbia": "BC", "VERDICT": "VERDICT"}


def make(tag: str):
    d = ROOT / "results/scores" / tag
    items = {i["blind_id"]: i for i in map(json.loads, open(d / "items.jsonl", encoding="utf-8"))}
    judg = {j["blind_id"]: j for j in map(json.loads, open(d / "final_judgments.jsonl", encoding="utf-8"))}
    pick = sorted(random.Random(SEED).sample(sorted(items), round(SHARE * len(items))))
    out = ["# Consistency re-score (rubric v1.2 §7)", "",
           "Score these answers **from scratch**, using only the rubric and the gold answer. Don't look at "
           "`scoring_review.md` or your earlier scores. Replace every **?** (labels are listed at the top of "
           "`src/consistency_check.py`).", ""]
    for bid in pick:
        it, j = items[bid], judg[bid]
        out += [f"## {bid} · {it['qid']}", "", f"**Question:** {it['question']}", "",
                "**Answer:**", "```text", it["answer"], "```", "", "**Gold:**"]
        out += [f"- {jur} (s. {', '.join(g['sections'])}): {g['answer']}" for jur, g in it["gold"].items()]
        if it["comparison"]:
            out.append(f"- Comparison: {it['comparison']}")
        out += [f"- Abstain ({jur}): {n}" for jur, n in it["abstain"].items()]
        out += ["", "**Key facts:**"] + [f"- [{SHORT[k['jurisdiction']]}] {k['fact']} → **?**" for k in j["key_facts"]]
        out += ["", "**Claims:**"] + ([f'- "{c["claim"]}" → **?** | **?**' for c in j["claims"]] or ["- (no claims)"])
        out += ["", "**Abstention:** **?**   **False abstention:** **?**", "", "---", ""]
    (d / "rescore_sheet.md").write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {d/'rescore_sheet.md'}: {len(pick)} answers ({pick[0]} … {pick[-1]})")


def score(tag: str):
    d = ROOT / "results/scores" / tag
    judg = {j["blind_id"]: j for j in map(json.loads, open(d / "final_judgments.jsonl", encoding="utf-8"))}
    text = (d / "rescore_sheet.md").read_text(encoding="utf-8")
    blocks = re.split(r"^## (S\d{3}) · ", text, flags=re.M)[1:]
    agree = total = 0
    per_type = {"key_fact": [0, 0], "supported": [0, 0], "citation": [0, 0], "abstention": [0, 0]}
    disagreements, unfilled = [], 0
    for bid, body in zip(blocks[::2], blocks[1::2]):
        j = judg[bid]
        kfs = re.findall(r"^- \[(?:ON|BC|VERDICT)\] .+? → \*\*(.+?)\*\*", body, flags=re.M)
        cls = re.findall(r'^- ".+?" → \*\*(.+?)\*\* \| \*\*(.+?)\*\*', body, flags=re.M)
        ab = re.search(r"\*\*Abstention:\*\* \*\*(.+?)\*\*\s+\*\*False abstention:\*\* \*\*(.+?)\*\*", body)
        pairs = [("key_fact", k["fact"], new, k["label"]) for k, new in zip(j["key_facts"], kfs)]
        for c, (s, ci) in zip(j["claims"], cls):
            pairs += [("supported", c["claim"], s, c["supported"]), ("citation", c["claim"], ci, c["citation"])]
        if ab:
            old_ab = "n/a" if j["abstention"] is None else str(j["abstention"])
            pairs += [("abstention", "abstention", ab[1], old_ab),
                      ("abstention", "false abstention", ab[2], "yes" if j["false_abstention"] else "no")]
        for kind, what, new, old in pairs:
            if new.strip() == "?":
                unfilled += 1
                continue
            ok = new.strip().lower() == old.strip().lower()
            per_type[kind][0] += ok
            per_type[kind][1] += 1
            agree += ok
            total += 1
            if not ok:
                disagreements.append({"blind_id": bid, "type": kind, "item": what, "first": old, "rescore": new})
    report = {"answers": len(blocks) // 2, "labels_compared": total, "unfilled": unfilled,
              "agreement": round(agree / total, 3) if total else None,
              "by_type": {k: f"{a}/{n}" for k, (a, n) in per_type.items()}, "disagreements": disagreements}
    (d / "consistency.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(json.dumps({k: v for k, v in report.items() if k != "disagreements"}, indent=2))
    for x in disagreements:
        print(f"  {x['blind_id']} {x['type']}: first {x['first']!r} vs re-score {x['rescore']!r} — {x['item'][:70]}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["make", "score"])
    ap.add_argument("--tag", default="full")
    a = ap.parse_args()
    make(a.tag) if a.mode == "make" else score(a.tag)
