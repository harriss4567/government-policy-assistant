"""Command-line app for the live demo.

Examples:
    .venv/bin/python app.py "How much vacation do I get after 6 years in Toronto vs Vancouver?"
    .venv/bin/python app.py --experiment B "..."          # base model + RAG (compare with D)
    .venv/bin/python app.py --exclude BC:40 "..."         # failure demo: hide BC s.40 from retrieval
    .venv/bin/python app.py --trace "..."                 # also show retrieved chunks, checks, tokens, time
    .venv/bin/python app.py                               # interactive: type questions, blank line to quit

Experiments (configs/config.yaml): A base · B base+RAG · C fine-tuned · D fine-tuned+RAG (default)
· E SmolLM2+RAG · F SmolLM2
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from pipeline import Pipeline  # noqa: E402

JUR = {"ON": "Ontario", "BC": "British Columbia"}


def parse_exclude(items: list[str]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for item in items:
        for part in item.split(","):
            prov, sec = part.split(":")
            out.setdefault(JUR[prov.strip().upper()], set()).add(sec.strip())
    return out


def show(result: dict, trace: bool):
    print(result["answer"])
    if trace:
        print("\n--- trace ---")
        for r in result["results"]:
            print(f"[{r['jurisdiction']}] status={r['status']} checks={json.dumps(r['checks'])}")
            for h in r["retrieved"]:
                print(f"   retrieved #{h['rank']} s.{h['label']} (score {h['score']:.2f})")
            for c in r["calls"]:
                print(f"   {c['step']}: {c.get('prompt_tokens')} prompt tokens, "
                      f"{c.get('output_tokens', 0)} output tokens, {c['seconds']}s")
    t = result["totals"]
    print(f"\n[experiment {result['experiment']['name']} · {t['seconds']:.1f}s · "
          f"{t['prompt_tokens']} prompt + {t['output_tokens']} output tokens]")


def main():
    ap = argparse.ArgumentParser(description="Ontario vs. BC employment standards assistant")
    ap.add_argument("question", nargs="?", help="leave out for interactive mode")
    ap.add_argument("--experiment", "-e", default="D", choices=list("ABCDEF"))
    ap.add_argument("--exclude", action="append", default=[], help="hide sections, e.g. BC:40 or ON:22,BC:35")
    ap.add_argument("--trace", action="store_true", help="show retrieved chunks, checks, tokens and time")
    a = ap.parse_args()

    pipe = Pipeline(a.experiment)
    exclude = parse_exclude(a.exclude)
    if a.question:
        show(pipe.run(a.question, exclude), a.trace)
        return
    print(f"Experiment {a.experiment}. Ask a question about Ontario or BC employment standards (blank line to quit).")
    while (q := input("\n> ").strip()):
        show(pipe.run(q, exclude), a.trace)


if __name__ == "__main__":
    main()
