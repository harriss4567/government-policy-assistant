"""Compare A2AJ dataset section text against the official government sources.

Official sources:
  Ontario: e-Laws. The public page (ontario.ca/laws/statute/00e41) is rendered by JavaScript
           from the ontario.ca legislation API, so we fetch the API response directly.
  BC:      BC Laws HTML page for RSBC 1996, c 113.

What counts as a difference: words or numbers differ, or a subsection/clause is missing or extra.
Ignored: formatting (whitespace, curly vs straight quotes, dashes), headings, and amendment
citations/history notes, which are not part of the legal text itself.

Usage (from project root):
    .venv/bin/python src/verify_sections.py            # uses cached official copies if present
    .venv/bin/python src/verify_sections.py --refresh  # re-download official copies
"""
from __future__ import annotations

import argparse
import difflib
import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
RAW_ROWS = ROOT / "data" / "raw" / "esa_raw_rows.parquet"
OFFICIAL_DIR = ROOT / "data" / "raw" / "official"
RESULTS = ROOT / "results"

SOURCES = {
    "Ontario": {
        "dataset_name": "Employment Standards Act, 2000",
        "fetch_url": "https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41",
        "public_url": "https://www.ontario.ca/laws/statute/00e41",
        "file": "on_esa_api.json",
    },
    "British Columbia": {
        "dataset_name": "Employment Standards Act",
        "fetch_url": "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01",
        "public_url": "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01",
        "file": "bc_esa.html",
    },
}

TARGETS = {
    "Ontario": ["33", "34", "35", "35.2", "36", "22"],
    "British Columbia": ["57", "59", "58", "60", "40", "37", "42"],
}


# ---------------------------------------------------------------- text normalization
def normalize(text: str) -> str:
    text = html.unescape(text)
    text = text.replace(" ", " ")
    text = re.sub(r"[‘’′`]", "'", text)
    text = re.sub(r"[“”″]", '"', text)
    text = re.sub(r"[–—‑]", "-", text)
    text = text.replace("*", "")                                   # dataset markdown italics
    text = re.sub(r"\s+([,.;:)])", r"\1", text)                    # tag-stripping spacing artifacts
    text = re.sub(r"\(\s+", "(", text)
    text = text.replace('"', "")                                   # dataset drops quotes on defined terms
    text = re.sub(                                                 # "Repealed: 2019, c. 4, Sched. 9, s. 8 (1)."
        r"(?i)\brepealed\s*:\s*(?:\d{4},\s*c\.\s*\d+(?:,\s*sched\.\s*[\w.]+)?,\s*ss?\.\s*[\d.]+"
        r"(?:\s*\([\d.\-]+\))*(?:\s*\([a-z]\))?(?:\s*;\s*)?)*\.?(?:\s*\(\d+\)\s*-\s*\(\d+\))?",
        "repealed ", text)
    text = re.sub(r"repealed\s*-?\s*\(\d+(?:\.\d+)?\)\s*$", "repealed", text)  # trailing cite fragment
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def strip_tags(fragment: str) -> str:
    return re.sub(r"<[^>]+>", " ", fragment)


# ---------------------------------------------------------------- fetching
def fetch(jurisdiction: str, refresh: bool) -> str:
    src = SOURCES[jurisdiction]
    path = OFFICIAL_DIR / src["file"]
    meta_path = OFFICIAL_DIR / (src["file"] + ".meta.json")
    if path.exists() and not refresh:
        return path.read_text(encoding="utf-8")
    OFFICIAL_DIR.mkdir(parents=True, exist_ok=True)
    resp = requests.get(src["fetch_url"], headers={"User-Agent": "Mozilla/5.0 (research verification)"}, timeout=60)
    resp.raise_for_status()
    path.write_text(resp.text, encoding="utf-8")
    meta_path.write_text(json.dumps({
        "fetch_url": src["fetch_url"],
        "public_url": src["public_url"],
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bytes": len(resp.content),
    }, indent=2))
    return resp.text


# ---------------------------------------------------------------- official parsers
ON_BODY_CLASSES = {"subsection", "paragraph", "subpara", "subsubpara", "clause", "subclause",
                   "definition", "equation", "line", "table"}


def parse_ontario(raw: str) -> dict[str, str]:
    content = json.loads(raw)["content"]
    sections: dict[str, list[str]] = {}
    current = None
    for cls, inner in re.findall(r'<p class="([^"]+)"[^>]*>(.*?)</p>', content, flags=re.S):
        cls = cls.strip()
        inner = re.split(r'<span class="citation">', inner, maxsplit=1)[0]  # drop amendment citations
        if cls == "section":
            m = re.search(r"<b>\s*(\d+(?:\.\d+)*)\b\s*", inner)  # number may share <b> with text
            if not m:
                current = None
                continue
            current = m.group(1).rstrip(".")
            inner = inner.replace(m.group(0), " ", 1)
            sections[current] = [strip_tags(inner)]
        elif cls in ON_BODY_CLASSES and current is not None:
            sections[current].append(strip_tags(inner))
        elif cls in {"partnum", "heading1"}:
            current = None
        # headnote / footnote / TOC / 'Y*' classes are not section body text: skipped
    return {k: " ".join(v) for k, v in sections.items()}


def parse_bc(raw: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    blocks = re.split(r'<div class="section">', raw)[1:]
    for block in blocks:
        m = re.search(r'<a name="section([\d.]+)"', block)
        if not m:
            continue
        num = m.group(1)
        block = re.split(r'<p class="part"|<div class="(?:division|part)"', block, maxsplit=1)[0]
        block = re.sub(r"<h4>.*?</h4>", " ", block, flags=re.S)               # heading
        block = re.sub(r'<span class="secnumholder"><b>[\d.]+</b>', " ", block)  # section number
        paras = re.findall(r"<p[^>]*>(.*?)</p>", block, flags=re.S)
        sections[num] = " ".join(strip_tags(p) for p in paras)
    return sections


def strip_leading_number(text: str, num: str) -> str:
    return re.sub(rf"^\s*{re.escape(num)}\s+", "", text)


# ---------------------------------------------------------------- comparison
def compare(a: str, b: str) -> tuple[float, list[str]]:
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(a=ta, b=tb, autojunk=False)
    diffs = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            diffs.append(f"{op}: dataset='{' '.join(ta[i1:i2])}' | official='{' '.join(tb[j1:j2])}'")
    return sm.ratio(), diffs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true", help="re-download official sources")
    args = ap.parse_args()

    rows = pd.read_parquet(RAW_ROWS)
    parsers = {"Ontario": parse_ontario, "British Columbia": parse_bc}
    records = []

    for jur, src in SOURCES.items():
        row = rows[rows["name_en"] == src["dataset_name"]].iloc[0]
        dataset = json.loads(row["unofficial_sections_en"])
        official = parsers[jur](fetch(jur, args.refresh))

        for num in sorted(set(dataset) | set(official), key=lambda s: [int(p) for p in s.split(".")]):
            d_txt = normalize(dataset.get(num, ""))
            o_txt = normalize(strip_leading_number(official.get(num, ""), num))
            if num not in official:
                status, ratio, diffs = "missing_in_official", 0.0, []
            elif num not in dataset:
                status, ratio, diffs = "missing_in_dataset", 0.0, []
            else:
                ratio, diffs = compare(d_txt, o_txt)
                status = "match" if not diffs else "differs"
            records.append({
                "jurisdiction": jur, "section": num,
                "is_target": num in TARGETS[jur],
                "status": status, "similarity": round(ratio, 4),
                "n_diffs": len(diffs), "diffs": diffs[:20],
            })

    df = pd.DataFrame(records)
    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "verification_report.json"
    df.to_json(out, orient="records", indent=2, force_ascii=False)

    print("=== All sections ===")
    print(df.groupby(["jurisdiction", "status"]).size().to_string())
    print("\n=== Target sections ===")
    tgt = df[df.is_target]
    print(tgt[["jurisdiction", "section", "status", "similarity", "n_diffs"]].to_string(index=False))
    for _, r in tgt[tgt.status != "match"].iterrows():
        print(f"\n--- {r.jurisdiction} s.{r.section} ({r.status}) ---")
        for d in r.diffs:
            print("  ", d)
    print(f"\nFull report: {out}")


if __name__ == "__main__":
    main()
