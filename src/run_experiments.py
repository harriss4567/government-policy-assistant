"""Run experiments A–F on the test questions and save every answer with its full trace.

Step 3.8 (smoke test): a few questions, checks that every experiment RUNS end to end.
Day 4 (full run): all 30 questions, the saved answers are then scored blind with the rubric.

Usage:
    .venv/bin/python src/run_experiments.py --ids Q08,Q16,Q27 --tag smoke       # smoke test, all experiments
    .venv/bin/python src/run_experiments.py --experiments A,B,C,D,E --tag full  # Day 4
Writes: results/runs/<tag>/<experiment>.jsonl  (one line per question) and results/runs/<tag>/health.json

The printout shows only run health (did it run, valid JSON, retries, answered/abstained, time, tokens),
not the answers themselves: test answers are read only when scoring, after the pipeline is frozen.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ROOT, load_config  # noqa: E402
from pipeline import Pipeline  # noqa: E402


def slim(result: dict) -> dict:
    """Keep what scoring and error analysis need; drop the long chunk texts (kept as chunk ids + scores)."""
    out = {k: result[k] for k in ("question", "route", "comparison", "answer", "experiment", "totals")}
    out["results"] = []
    for r in result["results"]:
        out["results"].append({
            "jurisdiction": r["jurisdiction"], "status": r["status"], "reason": r.get("reason"),
            "answer_json": r.get("answer"), "checks": r["checks"], "warnings": r["warnings"],
            "retrieved": [{k: h[k] for k in ("rank", "score", "chunk_id", "section", "label")} for h in r["retrieved"]],
            "calls": r["calls"]})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--experiments", default="A,B,C,D,E,F")
    ap.add_argument("--ids", default=None, help="comma-separated question ids (default: all 30)")
    ap.add_argument("--tag", default="run")
    a = ap.parse_args()

    cfg = load_config()
    questions = [json.loads(l) for l in open(cfg["paths"]["evaluation"], encoding="utf-8")]
    if a.ids:
        keep = a.ids.split(",")
        questions = [q for q in questions if q["id"] in keep]
    out_dir = ROOT / "results/runs" / a.tag
    out_dir.mkdir(parents=True, exist_ok=True)

    health = {}
    for exp in a.experiments.split(","):
        pipe = Pipeline(exp, cfg)
        rows, t0 = [], time.perf_counter()
        for q in questions:
            try:
                res = slim(pipe.run(q["question"]))
                res["id"] = q["id"]
            except Exception as e:                       # a crash is recorded, not fatal, so one bad case can't stop the run
                res = {"id": q["id"], "error": f"{type(e).__name__}: {e}"}
            rows.append(res)
        with open(out_dir / f"{exp}.jsonl", "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        ok = [r for r in rows if "error" not in r]
        per = [x for r in ok for x in r["results"]]
        health[exp] = {
            "experiment": {k: v for k, v in pipe.exp.items()}, "model_id": pipe.model["id"],
            "questions": len(rows), "crashed": len(rows) - len(ok),
            "province_answers": len(per),
            "valid_json": sum(x["checks"].get("valid_json", False) for x in per),
            "retries": sum(x["checks"].get("retries", 0) for x in per),
            "status": {s: sum(x["status"] == s for x in per) for s in ("answered", "abstained", "failed")},
            "quote_verified": sum(x["checks"].get("quote") == "verified" for x in per),
            "avg_seconds_per_question": round(sum(r["totals"]["seconds"] for r in ok) / max(1, len(ok)), 1),
            "avg_tokens_per_question": round(sum(r["totals"]["prompt_tokens"] + r["totals"]["output_tokens"]
                                                 for r in ok) / max(1, len(ok))),
            "wall_minutes": round((time.perf_counter() - t0) / 60, 1),
        }
        h = health[exp]
        print(f"{exp} ({'+'.join([h['model_id'].split('/')[-1], 'LoRA' if pipe.exp['adapter'] else 'base', 'RAG' if pipe.exp['rag'] else 'no RAG'])}): "
              f"{h['questions']} questions, crashed {h['crashed']}, valid JSON {h['valid_json']}/{h['province_answers']}, "
              f"retries {h['retries']}, {h['status']}, quotes verified {h['quote_verified']}, "
              f"{h['avg_seconds_per_question']}s and {h['avg_tokens_per_question']} tokens per question", flush=True)
    (out_dir / "health.json").write_text(json.dumps(health, indent=2))
    print(f"Wrote {out_dir}")


if __name__ == "__main__":
    main()
