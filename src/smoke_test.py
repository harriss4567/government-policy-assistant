"""Step 2.9: run the BASE (not fine-tuned) Qwen model on 3 validation examples on the local machine.

Purpose: confirm the model loads and runs locally (MPS on the M1), measure speed and memory, and record
the "before fine-tuning" behaviour: does it return valid JSON with the right keys, a word-for-word quote,
the right section and the right `mandatory` label?

Examples: V003 (threshold), V008 (optional + exception), V019 (missing: should answer "Not specified").
Uses the exact training prompt (system + user messages from data/val.jsonl).

Usage:  .venv/bin/python src/smoke_test.py [model_id] [--adapter models/lora-adapter]
Writes: results/smoke_test_<model>[_lora].json

Quote check ignores capitalization (a quote starting "the period…" for "The period…" still counts).
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

os.environ.setdefault("HF_HUB_OFFLINE", "1")          # models are already in the local cache

import torch  # noqa: E402
from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ROOT  # noqa: E402

ARGS = sys.argv[1:]
ADAPTER = ARGS[ARGS.index("--adapter") + 1] if "--adapter" in ARGS else None
POS = [a for i, a in enumerate(ARGS) if a != "--adapter" and (i == 0 or ARGS[i - 1] != "--adapter")]
MODEL = POS[0] if POS else "Qwen/Qwen2.5-1.5B-Instruct"
IDS = ["V003", "V008", "V019"]
KEYS = ["jurisdiction", "topic", "section", "eligibility", "entitlement_or_requirement", "threshold",
        "exceptions", "mandatory", "supporting_quote"]


def parse_json(text: str) -> dict | None:
    m = re.search(r"\{.*\}", text, flags=re.S)          # tolerate ```json fences or extra words
    try:
        return json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        return None


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    t0 = time.perf_counter()
    tok = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.float16).to(device)
    if ADAPTER:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, str(ROOT / ADAPTER)).to(device)
    model = model.eval()
    load_s = time.perf_counter() - t0

    examples = {e["id"]: e for e in map(json.loads, open(ROOT / "data/val.jsonl", encoding="utf-8"))}
    results = []
    for eid in IDS:
        msgs = examples[eid]["messages"]
        expected = json.loads(msgs[2]["content"])
        inputs = tok.apply_chat_template(msgs[:2], add_generation_prompt=True, return_tensors="pt",
                                         return_dict=True).to(device)
        t = time.perf_counter()
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=400, do_sample=False)
        secs = time.perf_counter() - t
        new = out[0, inputs["input_ids"].shape[1]:]
        text = tok.decode(new, skip_special_tokens=True)
        got = parse_json(text)
        checks = {"valid_json": got is not None}
        if got:
            checks |= {
                "exact_keys": list(got) == KEYS or set(got) == set(KEYS),
                "section_match": str(got.get("section")).strip() == expected["section"],
                "mandatory_match": got.get("mandatory") == expected["mandatory"],
                "quote_word_for_word": (not got.get("supporting_quote") and not expected["supporting_quote"])
                or (bool(got.get("supporting_quote")) and norm(str(got["supporting_quote"])) in norm(msgs[1]["content"])),
                "says_not_specified_when_expected": (expected["section"].startswith("Not specified")
                                                     == str(got.get("section", "")).startswith("Not specified")),
            }
        results.append({"id": eid, "prompt_tokens": int(inputs["input_ids"].shape[1]), "output_tokens": len(new),
                        "seconds": round(secs, 1), "tokens_per_second": round(len(new) / secs, 1),
                        "checks": checks, "output": text, "expected": expected})
        print(f"\n=== {eid} ({len(new)} tokens, {secs:.1f}s) ===\n{text}\nchecks: {checks}")

    peak = torch.mps.driver_allocated_memory() / 1e9 if device == "mps" else None
    report = {"model": MODEL, "adapter": ADAPTER, "device": device, "dtype": "float16", "load_seconds": round(load_s, 1),
              "peak_memory_gb": round(peak, 2) if peak else None, "decoding": "greedy, max_new_tokens=400",
              "results": results}
    out = ROOT / f"results/smoke_test_{MODEL.split('/')[-1]}{'_lora' if ADAPTER else ''}.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\nloaded in {load_s:.1f}s on {device}; peak memory {report['peak_memory_gb']} GB\nWrote {out}")


if __name__ == "__main__":
    main()
