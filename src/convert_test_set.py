"""Convert the hand-written test set (docs/test_set.md) into data/evaluation.jsonl.

docs/test_set.md is the source of truth. Edit questions there, then re-run:
    .venv/bin/python src/convert_test_set.py

Each output line is one question:
{
  "id": "Q11",
  "category": "cross_jurisdiction_comparison",
  "topic": "vacation_entitlement",
  "phrasing": "casual",
  "question": "...",
  "jurisdictions": ["Ontario", "British Columbia"],      # everything the question asks about
  "gold": {"Ontario": {"sections": ["33"], "answer": "...", "key_facts": ["...", ...]}, ...},
  "gold_chunks": ["ON-ESA-33", "BC-ESA-57"],              # what retrieval should find (Recall@k)
  "comparison": "Same: ..." | null,                      # same/different verdict (comparison questions)
  "abstain": {"Alberta": "reason"} | {},                 # where "insufficient evidence" is the right answer
  "expected_abstain": true | false
}
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "test_set.md"
OUT = ROOT / "data" / "evaluation.jsonl"
KB = ROOT / "data" / "processed" / "kb_sections.jsonl"

CATEGORY_ALIASES = {"jurisdiction_comparison": "cross_jurisdiction_comparison"}
VALID_CATEGORIES = {"direct_extraction", "cross_jurisdiction_comparison", "exceptions",
                    "dates_thresholds", "insufficient_evidence"}
VALID_TOPICS = {"vacation_entitlement", "vacation_pay", "overtime"}
CODES = {"Ontario": "ON", "British Columbia": "BC"}
EXPECTED_COUNTS = {"direct_extraction": 10, "cross_jurisdiction_comparison": 8, "exceptions": 5,
                   "dates_thresholds": 3, "insufficient_evidence": 4}


def field(block: str, name: str) -> str:
    m = re.search(rf"^- \*\*{name}:\*\*\s*(.+)$", block, flags=re.M)
    if not m:
        raise ValueError(f"missing '{name}'")
    return m.group(1).strip()


def parse_jurisdictions(block: str) -> dict:
    gold = {}
    pattern = r"^\*\*(Ontario|British Columbia)\*\* \(([^)]*)\)\n(.*?)(?=^\*\*|\Z)"
    for jur, secs, body in re.findall(pattern, block, flags=re.M | re.S):
        answer = re.search(r"^- Answer:\s*(.+)$", body, flags=re.M)
        facts_part = body.split("- Key facts:", 1)[1] if "- Key facts:" in body else ""
        gold[jur] = {
            "sections": re.findall(r"\d+(?:\.\d+)?", secs),
            "answer": answer.group(1).strip() if answer else "",
            "key_facts": [f.strip() for f in re.findall(r"^\s+- (.+)$", facts_part, flags=re.M)],
        }
    return gold


def parse_abstain(block: str) -> dict:
    m = re.search(r"^\*\*Abstain:\*\*\s*(.+)$", block, flags=re.M)
    text = m.group(1).strip() if m else "none"
    if text.lower() == "none":
        return {}
    jur, _, reason = re.split(r"\s*(:|—|-)\s*", text, maxsplit=1)
    return {jur.strip(): reason.strip()}


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    blocks = re.findall(r"(?ms)^## (Q\d{2})\n(.*?)(?=^## Q\d{2}|\Z)", text)
    kb = pd.read_json(KB, lines=True, dtype={"section": str}).set_index("chunk_id")

    items, problems = [], []
    for qid, block in blocks:
        try:
            category = CATEGORY_ALIASES.get(field(block, "Category"), field(block, "Category"))
            gold = parse_jurisdictions(block)
            abstain = parse_abstain(block)
            comp = re.search(r"^\*\*Comparison:\*\*\s*(.+)$", block, flags=re.M)
            item = {
                "id": qid,
                "category": category,
                "topic": field(block, "Topic"),
                "phrasing": field(block, "Phrasing"),
                "question": field(block, "Question"),
                "jurisdictions": list(gold) + [j for j in abstain if j not in gold],
                "gold": gold,
                "gold_chunks": [f"{CODES[j]}-ESA-{s}" for j, g in gold.items() for s in g["sections"]],
                "comparison": comp.group(1).strip() if comp else None,
                "abstain": abstain,
                "expected_abstain": bool(abstain),
            }
        except ValueError as e:
            problems.append(f"{qid}: {e}")
            continue

        # ---- validation
        if item["category"] not in VALID_CATEGORIES:
            problems.append(f"{qid}: unknown category {item['category']!r}")
        if item["topic"] not in VALID_TOPICS:
            problems.append(f"{qid}: unknown topic {item['topic']!r}")
        if item["phrasing"] not in {"casual", "precise"}:
            problems.append(f"{qid}: phrasing must be casual/precise")
        if not gold:
            problems.append(f"{qid}: no jurisdiction blocks found")
        for j, g in gold.items():
            if not g["answer"] or not g["key_facts"]:
                problems.append(f"{qid}: {j} missing answer or key facts")
        if item["category"] == "cross_jurisdiction_comparison" and not item["comparison"]:
            problems.append(f"{qid}: comparison question without a **Comparison:** line")
        if (item["category"] == "insufficient_evidence") != item["expected_abstain"]:
            problems.append(f"{qid}: abstain field doesn't match category")
        for c in item["gold_chunks"]:
            if c not in kb.index:
                problems.append(f"{qid}: {c} not in knowledge base")
            elif kb.loc[c, "split_role"] == "train_pool":
                problems.append(f"{qid}: {c} is in the TRAINING pool (leakage risk)")
        items.append(item)

    ids = [i["id"] for i in items]
    if len(set(ids)) != len(ids):
        problems.append("duplicate question IDs")
    counts = Counter(i["category"] for i in items)
    if dict(counts) != EXPECTED_COUNTS:
        problems.append(f"category counts {dict(counts)} != expected {EXPECTED_COUNTS}")

    if problems:
        print("NOT WRITTEN, fix these in docs/test_set.md first:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)

    with OUT.open("w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(f"Wrote {len(items)} questions to {OUT}")
    print("Categories:", dict(counts))
    print("Phrasing:", dict(Counter(i["phrasing"] for i in items)))
    print("Abstain questions:", [i["id"] for i in items if i["expected_abstain"]])
    roles = Counter(kb.loc[c, "split_role"] for i in items for c in i["gold_chunks"])
    print("Gold chunk split roles:", dict(roles))


if __name__ == "__main__":
    main()
