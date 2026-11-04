"""Step 2.1: split knowledge-base sections into retrieval chunks.

Rules
- Definition sections (s. 1 of each Act): one chunk per defined term, so a question like Q24 can
  retrieve "standard vacation entitlement year" on its own instead of a 13,860-character block.
- Short sections (<= max_chars): kept whole.
- Long sections: split at subsection markers "(1)", "(2)" ...; a subsection that is still too long is
  split further at line breaks, packed up to max_chars, and marked "(continued)".
- Every chunk keeps its base section number, so Recall@k can match it to the test set's gold sections.
- Each chunk gets an `embed_text` with a short label prefix ("[Ontario ESA s. 33(1), Vacation With Pay]"),
  which helps a small embedding model on short legal text.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import load_config  # noqa: E402

DEF_LINE = re.compile(r"^(“[^”]+”|\*[^*]+\*)")          # ON “term” …  /  BC *term* …
SUBSEC = re.compile(r"^\((\d+(?:\.\d+)?)\)\s")           # (1) …  (2.1) …
SHORT_ACT = {"Ontario": "Ontario ESA", "British Columbia": "BC ESA"}


def _pack(lines: list[str], max_chars: int) -> list[str]:
    """Greedily pack lines into pieces no longer than max_chars (a single long line stays whole)."""
    pieces, cur = [], ""
    for ln in lines:
        if cur and len(cur) + 1 + len(ln) > max_chars:
            pieces.append(cur)
            cur = ln
        else:
            cur = f"{cur}\n{ln}" if cur else ln
    if cur:
        pieces.append(cur)
    return pieces


def _split_subsections(text: str) -> list[tuple[str | None, str]]:
    """Return [(subsection_number or None, text)] by splitting at lines that start with (n)."""
    out, num, buf = [], None, []
    for ln in text.split("\n"):
        m = SUBSEC.match(ln)
        if m and buf:
            out.append((num, "\n".join(buf)))
            buf = []
        if m:
            num = m.group(1)
        buf.append(ln)
    if buf:
        out.append((num, "\n".join(buf)))
    return out


def _split_definitions(text: str) -> list[tuple[str, str]]:
    """Return [(label, text)]: one entry per defined term; non-definition subsections kept as their own pieces."""
    out, label, buf, sub = [], None, [], "1"
    for ln in text.split("\n"):
        d, s = DEF_LINE.match(ln), SUBSEC.match(ln)
        if (d or (s and s.group(1) != "1")) and buf:
            out.append((label, "\n".join(buf)))
            buf = []
        if s:
            sub = s.group(1)
            label = f"({sub})"
        if d:
            label = f"({sub}) {d.group(1)}"
        buf.append(ln)
    if buf:
        out.append((label, "\n".join(buf)))
    return out


def build_chunks(cfg: dict | None = None, save: bool = True) -> pd.DataFrame:
    cfg = cfg or load_config()
    max_chars = cfg["chunking"]["max_chars"]
    kb = pd.read_json(cfg["paths"]["kb_sections"], lines=True, dtype={"section": str})

    rows = []
    for r in kb.itertuples():
        text = r.text.strip()
        if cfg["chunking"]["drop_repealed"] and text.lower().lstrip("[").startswith("repealed"):
            continue

        if r.section == "1":                                   # definitions: one chunk per term
            pieces = [(lbl, t) for lbl, t in _split_definitions(text)]
            pieces = [(lbl, p) for lbl, t in pieces for p in _pack(t.split("\n"), max_chars)]
        elif len(text) <= max_chars:
            pieces = [(None, text)]
        else:
            pieces = []
            for num, t in _split_subsections(text):
                lbl = f"({num})" if num else None
                parts = _pack(t.split("\n"), max_chars)
                pieces += [(lbl, p if i == 0 else f"(continued) {p}") for i, p in enumerate(parts)]

        for i, (lbl, piece) in enumerate(pieces, 1):
            label = f"{r.section}{lbl}" if lbl and not lbl.startswith("(1) “") and not lbl.startswith("(1) *") \
                else (f"{r.section}{lbl.split(' ', 1)[0]} {lbl.split(' ', 1)[1]}" if lbl else r.section)
            rows.append({
                "chunk_id": f"{r.chunk_id}-{i}" if len(pieces) > 1 else r.chunk_id,
                "jurisdiction": r.jurisdiction,
                "section": r.section,                 # base section, used to match gold sections
                "label": label,                       # e.g. "33(1)" or "1(1) “standard vacation entitlement year”"
                "part": r.part,
                "part_title": r.part_title,
                "split_role": r.split_role,
                "text": piece,
                "embed_text": f"[{SHORT_ACT[r.jurisdiction]} s. {label}, {r.part_title}] {piece}",
                "char_count": len(piece),
                "source_url": r.source_url,
            })

    chunks = pd.DataFrame(rows)
    assert chunks["chunk_id"].is_unique
    if save:
        chunks.to_json(cfg["paths"]["kb_chunks"], orient="records", lines=True, force_ascii=False)
    return chunks


if __name__ == "__main__":
    c = build_chunks()
    print(f"{len(c)} chunks from {c[['jurisdiction', 'section']].drop_duplicates().shape[0]} sections; "
          f"longest {c.char_count.max()} chars")
