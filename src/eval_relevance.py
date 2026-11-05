"""Test the relevance check BEFORE switching it on, using non-test data only.

The check asks the model "Do these excerpts contain the information needed to answer the question? YES/NO".
Labelled data: the 100 training/validation examples. Each has a question, its excerpts, and an expected answer.
  - answerable   = expected section is set (92)
  - unanswerable = expected section is "Not specified in the excerpt" (8)
Run with the base model (adapter off) and the fine-tuned model (adapter on); report how often each is right.

Plain YES/NO (P(YES) >= 0.5) rejects ~1 in 5 answerable examples, which is too many. So a stricter cut-off is
chosen here, on this non-test data: the cut-off that catches the most unanswerable examples while wrongly
rejecting at most 5% of answerable ones (base model, since it was never trained on these examples).

Usage:  .venv/bin/python src/eval_relevance.py
Writes: results/relevance_check.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import llm  # noqa: E402
from config import ROOT, load_config  # noqa: E402
from prompts import RELEVANCE_SYSTEM, build_relevance_prompt  # noqa: E402


def main():
    cfg = load_config()
    m = cfg["models"]["qwen"]
    rows = [json.loads(l) for f in ("train", "val") for l in open(ROOT / f"data/{f}.jsonl", encoding="utf-8")]
    report = {}
    for label, use_adapter in (("base", False), ("fine_tuned", True)):
        res = []
        for r in rows:
            expected = json.loads(r["messages"][2]["content"])
            answerable = not expected["section"].startswith("Not specified")
            msgs = [{"role": "system", "content": RELEVANCE_SYSTEM},
                    {"role": "user", "content": build_relevance_prompt(r["messages"][1]["content"],
                                                                          expected["jurisdiction"])}]
            out = llm.yes_probability(m["id"], msgs, adapter=m["adapter"], use_adapter=use_adapter)
            res.append({"id": r["id"], "answerable": answerable, **out})
        ans = [x for x in res if x["answerable"]]
        un = [x for x in res if not x["answerable"]]
        report[label] = {
            "answerable_kept (YES)": f"{sum(x['answer'] == 'YES' for x in ans)}/{len(ans)}",
            "unanswerable_caught (NO)": f"{sum(x['answer'] == 'NO' for x in un)}/{len(un)}",
            "unanswerable": [(x["id"], x["answer"], x["p_yes"]) for x in un],
            "answerable_wrongly_rejected": [(x["id"], x["p_yes"]) for x in ans if x["answer"] == "NO"],
            "seconds_per_check": round(sum(x["seconds"] for x in res) / len(res), 2),
        }
        sweep = []
        for th in (0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.2, 0.3, 0.5):
            sweep.append({"min_p_yes": th, "unanswerable_caught": sum(x["p_yes"] < th for x in un),
                          "answerable_wrongly_rejected": sum(x["p_yes"] < th for x in ans)})
        ok = [s for s in sweep if s["answerable_wrongly_rejected"] <= 0.05 * len(ans)]
        best = max(ok, key=lambda s: (s["unanswerable_caught"], -s["answerable_wrongly_rejected"]))
        report[label] |= {"sweep": sweep, "chosen": best}
        print(f"{label}: plain YES/NO → kept {report[label]['answerable_kept (YES)']}, caught "
              f"{report[label]['unanswerable_caught (NO)']}; chosen cut-off P(YES) < {best['min_p_yes']} → caught "
              f"{best['unanswerable_caught']}/{len(un)}, wrongly rejected {best['answerable_wrongly_rejected']}/{len(ans)}")
    out = ROOT / "results/relevance_check.json"
    out.write_text(json.dumps(report, indent=2))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
