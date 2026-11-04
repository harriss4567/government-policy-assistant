"""Step 2.5: can a retrieval similarity cut-off detect "the answer isn't in the knowledge base"?

Method (no tuning on the test set):
1. Choose the cut-off from NON-test questions: the top-1 similarity of the 92 training/validation
   questions that have a gold section. The floor is their 5th percentile, so ~95% of answerable
   questions stay above it.
2. Apply that fixed floor once to the 30 test questions and count:
   - abstain pairs caught (score below the floor): good
   - answerable pairs wrongly flagged (score below the floor): bad
   Abstain pairs = jurisdictions listed in a question's `abstain` field that ARE in the knowledge base
   (Q27 Ontario, Q28 BC, Q30 BC). Alberta (Q29) is handled by a simpler rule: not in the knowledge base.

Usage:  .venv/bin/python src/abstain_threshold.py
Writes: results/abstain_threshold.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compare_embeddings import load_questions  # noqa: E402
from config import ROOT, load_config  # noqa: E402
from retrieval import Retriever  # noqa: E402

PERCENTILE = 5


def top1(retriever: Retriever, question: str, jurisdiction: str) -> float | None:
    res = retriever.search(question, jurisdiction, k=1)
    return float(res["score"].iloc[0]) if len(res) else None


def summary(xs: list[float]) -> dict:
    return {"n": len(xs), "min": round(min(xs), 3), "median": round(float(np.median(xs)), 3), "max": round(max(xs), 3)}


def main():
    cfg = load_config()
    r = Retriever(cfg)

    # 1. floor from non-test questions
    nontest = load_questions(ROOT / "data/train.jsonl") + load_questions(ROOT / "data/val.jsonl")
    nontest_scores = [top1(r, q["question"], q["jurisdiction"]) for q in nontest]
    floor = round(float(np.percentile(nontest_scores, PERCENTILE)), 3)

    # 2. apply once to the test set
    rows = []
    for q in (json.loads(l) for l in open(cfg["paths"]["evaluation"], encoding="utf-8")):
        for jur in sorted(set(q["gold"]) | set(q["abstain"])):
            s = top1(r, q["question"], jur)
            if s is None:                       # jurisdiction not in the knowledge base (Alberta)
                continue
            rows.append({"id": q["id"], "jurisdiction": jur, "should_abstain": jur in q["abstain"],
                         "top1": round(s, 3), "below_floor": s < floor})
    ab = [x for x in rows if x["should_abstain"]]
    ans = [x for x in rows if not x["should_abstain"]]
    report = {
        "floor": floor,
        "floor_rule": f"{PERCENTILE}th percentile of top-1 similarity on {len(nontest)} answerable train/val questions",
        "nontest_answerable": summary(nontest_scores),
        "test_answerable": summary([x["top1"] for x in ans]),
        "test_should_abstain": summary([x["top1"] for x in ab]),
        "abstain_caught": f"{sum(x['below_floor'] for x in ab)}/{len(ab)}",
        "answerable_wrongly_flagged": f"{sum(x['below_floor'] for x in ans)}/{len(ans)}",
        "abstain_pairs": ab,
        "flagged_answerable": [x for x in ans if x["below_floor"]],
    }
    out = ROOT / "results/abstain_threshold.json"
    out.write_text(json.dumps(report, indent=2))
    print(json.dumps({k: v for k, v in report.items() if k not in ("abstain_pairs", "flagged_answerable")}, indent=2))
    print("abstain pairs:", [(x["id"], x["jurisdiction"], x["top1"]) for x in ab])
    print("wrongly flagged:", [(x["id"], x["jurisdiction"], x["top1"]) for x in report["flagged_answerable"]])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
