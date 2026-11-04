"""Convert the reviewed SFT examples (docs/training_examples.md) into data/train.jsonl and data/val.jsonl.

docs/training_examples.md is the source of truth. Edit examples there, then run:
    .venv/bin/python src/convert_training_data.py           # requires every example Reviewed: yes
    .venv/bin/python src/convert_training_data.py --draft   # allow unreviewed examples (for testing only)

Each output line is one chat-formatted training example:
    {"id": "T001", "messages": [{"role": "system", ...}, {"role": "user", ...}, {"role": "assistant", "content": "<JSON>"}],
     "sections": [...], "type": "..."}

Nothing is written if any check fails.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompts import NS, SYSTEM_PROMPT, build_user_prompt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "training_examples.md"
KB = ROOT / "data" / "processed" / "kb_sections.jsonl"
OUT = {"train": ROOT / "data" / "train.jsonl", "val": ROOT / "data" / "val.jsonl"}
KEYS = ["jurisdiction", "topic", "section", "eligibility", "entitlement_or_requirement",
        "threshold", "exceptions", "mandatory", "supporting_quote"]
CODES = {"ON": "Ontario", "BC": "British Columbia"}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def field(block: str, name: str) -> str:
    m = re.search(rf"^- \*\*{name}:\*\*\s*(.+)$", block, flags=re.M)
    if not m:
        raise ValueError(f"missing '{name}'")
    return m.group(1).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", action="store_true", help="allow unreviewed examples")
    args = ap.parse_args()

    kb = pd.read_json(KB, lines=True, dtype={"section": str})
    kb_text = {(r.jurisdiction, r.section): norm(r.text) for r in kb.itertuples()}
    kb_role = {(r.jurisdiction, r.section): r.split_role for r in kb.itertuples()}

    blocks = re.findall(r"(?ms)^## ([TV]\d{3})\n(.*?)(?=^## [TV]\d{3}|\Z)", SRC.read_text(encoding="utf-8"))
    problems, rows, unreviewed = [], {"train": [], "val": []}, []
    sections_by_split = {"train": set(), "val": set()}

    for eid, b in blocks:
        try:
            split, jur, question = field(b, "Split"), field(b, "Jurisdiction"), field(b, "Question")
            etype, reviewed = field(b, "Type"), field(b, "Reviewed").lower()
            excerpts = re.findall(r"^  - \[(ON|BC) s\. ([^\]]+)\] (.+)$", b, flags=re.M)
            out = json.loads(re.search(r"```json\n(.*?)\n```", b, flags=re.S).group(1))
        except (ValueError, AttributeError, json.JSONDecodeError) as e:
            problems.append(f"{eid}: cannot parse ({e})")
            continue
        if reviewed != "yes":
            unreviewed.append(eid)
        if split not in rows:
            problems.append(f"{eid}: split must be train or val")
            continue

        # --- excerpts: real KB text, correct province, never test/excluded sections
        ex_pairs = []
        for code, sub, text in excerpts:
            if CODES[code] != jur:
                problems.append(f"{eid}: excerpt {code} s.{sub} is from the other province")
            base = sub.split("(")[0]
            key = (CODES[code], base)
            if key not in kb_text:
                problems.append(f"{eid}: s.{base} not in knowledge base")
                continue
            if kb_role[key] != "train_pool":
                problems.append(f"{eid}: s.{base} is {kb_role[key]} (only train_pool sections may be used)")
            text = text.replace(" / ", "\n")
            if norm(text) not in kb_text[key]:
                problems.append(f"{eid}: excerpt text for s.{sub} does not match the knowledge base")
            sections_by_split[split].add(key)
            ex_pairs.append((sub, text))
        if not ex_pairs:
            problems.append(f"{eid}: no excerpts")

        # --- expected JSON
        if list(out) != KEYS:
            problems.append(f"{eid}: JSON keys must be exactly {KEYS}")
        if out.get("jurisdiction") != jur:
            problems.append(f"{eid}: JSON jurisdiction doesn't match")
        if not isinstance(out.get("exceptions"), list):
            problems.append(f"{eid}: exceptions must be a list")
        if out.get("mandatory") not in {"mandatory", "optional", NS}:
            problems.append(f"{eid}: mandatory must be mandatory / optional / '{NS}'")
        quote = out.get("supporting_quote", "")
        if quote and not any(norm(quote) in norm(t) for _, t in ex_pairs):
            problems.append(f"{eid}: supporting_quote is not word-for-word in an excerpt")
        if not quote and out.get("section") != NS:
            problems.append(f"{eid}: empty supporting_quote but section is set")

        rows[split].append({
            "id": eid,
            "type": etype,
            "sections": sorted(f"{CODES[c]} s.{s}" for c, s, _ in excerpts),
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": build_user_prompt(jur, question, ex_pairs)},
                {"role": "assistant", "content": json.dumps(out, ensure_ascii=False)},
            ],
        })

    overlap = sections_by_split["train"] & sections_by_split["val"]
    if overlap:
        problems.append(f"sections used in BOTH train and val: {sorted(overlap)}")
    if unreviewed and not args.draft:
        problems.append(f"{len(unreviewed)} examples not reviewed yet (e.g. {unreviewed[:5]}); "
                        "set 'Reviewed: yes' or run with --draft")

    if problems:
        print("NOT WRITTEN, fix these in docs/training_examples.md first:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)

    for split, items in rows.items():
        with OUT[split].open("w", encoding="utf-8") as f:
            for it in items:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")
    for split, items in rows.items():
        types = Counter(t.strip() for it in items for t in it["type"].split(","))
        missing = sum("missing" in it["type"] for it in items)
        print(f"{split}: {len(items)} examples · {len(sections_by_split[split])} sections · "
              f"'missing' examples {missing} ({missing / len(items):.0%}) · types {dict(types)}")
    print(f"reviewed: {len(blocks) - len(unreviewed)}/{len(blocks)}" + ("  (DRAFT MODE)" if args.draft else ""))
    print("Wrote", OUT["train"], "and", OUT["val"])


if __name__ == "__main__":
    main()
