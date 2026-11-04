"""Build a section -> Part map from the official ON / BC sources saved by verify_sections.py.

Why: hand-typed Part ranges were wrong in several places (e.g. BC Part 6 starts at s.49.01,
ON Part XI.1 is s.41.1.1). Reading Part membership from the official structure avoids that.

Output: data/processed/part_map.json
    {"Ontario": {"33": {"part": "XI", "part_title": "Vacation With Pay"}, ...},
     "British Columbia": {...}}

Usage (from project root):  .venv/bin/python src/part_map.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = ROOT / "data" / "raw" / "official"
OUT = ROOT / "data" / "processed" / "part_map.json"


def clean(fragment: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
    return re.sub(r"\s+", " ", text).strip()


def ontario() -> dict[str, dict[str, str]]:
    content = json.loads((OFFICIAL / "on_esa_api.json").read_text(encoding="utf-8"))["content"]
    mapping, part, title = {}, None, None
    for cls, inner in re.findall(r'<p class="([^"]+)"[^>]*>(.*?)</p>', content, flags=re.S):
        cls = cls.strip()
        if cls == "partnum":                       # e.g. "PART xi VACATION WITH PAY"
            m = re.match(r"(?i)part\s+([ivxl]+(?:\.[\d.]+)?)\s+(.*)", clean(inner))
            part, title = (m.group(1).upper(), m.group(2).title()) if m else (clean(inner), "")
        elif cls == "section" and part:
            m = re.search(r"<b>\s*(\d+(?:\.\d+)*)", inner)
            if m:
                mapping[m.group(1)] = {"part": part, "part_title": title}
    return mapping


def british_columbia() -> dict[str, dict[str, str]]:
    raw = (OFFICIAL / "bc_esa.html").read_text(encoding="utf-8")
    events = [(m.start(), "part", clean(m.group(1)))
              for m in re.finditer(r'<p class="part"[^>]*>(.*?)</p>', raw, flags=re.S)]
    events += [(m.start(), "section", m.group(1))
               for m in re.finditer(r'<div class="section"><a name="section([\d.]+)"', raw)]
    mapping, part, title = {}, None, None
    for _, kind, value in sorted(events):
        if kind == "part":                         # e.g. "Part 7 — Annual Vacation"
            m = re.match(r"Part\s+(\d+)\s*[—-]\s*(.*)", value)
            part, title = (m.group(1), m.group(2)) if m else (value, "")
        elif part:
            mapping[value] = {"part": part, "part_title": title}
    return mapping


def main() -> None:
    result = {"Ontario": ontario(), "British Columbia": british_columbia()}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    for jur, m in result.items():
        parts = {}
        for sec, info in m.items():
            parts.setdefault((info["part"], info["part_title"]), []).append(sec)
        print(f"\n{jur}: {len(m)} sections in {len(parts)} Parts")
        for (p, t), secs in parts.items():
            print(f"  Part {p:10} {t[:45]:45} s.{secs[0]}–s.{secs[-1]} ({len(secs)})")
    print(f"\nSaved {OUT}")


if __name__ == "__main__":
    main()
