# Verification log: dataset text vs. official sources

- **Dataset:** A2AJ `a2aj/canadian-laws`, revision `7aeeba3`, scraped 2026-10-31
- **Official sources** (fetched 2026-11-02; copies and fetch timestamps in `data/raw/official/`):
  - Ontario e-Laws: https://www.ontario.ca/laws/statute/00e41. The public page is built by JavaScript from the ontario.ca legislation API, so the script fetches the API response directly.
  - BC Laws: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01
- **Method:** automated, `src/verify_sections.py`. Both texts are normalized and then compared word by word (Python `difflib`), for **every** section of both Acts, not only the targets. Flagged sections were reviewed by hand. Full output: `results/verification_report.json`.
- **What counts as a difference:** different words, numbers, percentages, time periods, conditions, or a missing or extra subsection or clause.
- **Ignored (normalized away):** whitespace, curly vs. straight quotes, dashes, markdown italics (`*term*`), quote marks around defined terms, headings, amendment citations and history notes.

## Target sections: 13 / 13 match

| Jurisdiction | Section | Topic | Matches official? | Differences | Mentions regulations? | Keep as target? |
|---|---|---|---|---|---|---|
| Ontario | 33 | vacation_entitlement | Yes | none | No | Yes |
| Ontario | 34 | vacation_entitlement | Yes | none | No | Yes |
| Ontario | 35 | vacation_entitlement | Yes | none | No | Yes |
| Ontario | 35.2 | vacation_pay | Yes | none | No | Yes |
| Ontario | 36 | vacation_pay | Yes | none | No | Yes |
| Ontario | 22 | overtime | Yes | none (repealed-subsection citations only) | **Yes**: "if another threshold is prescribed" (22(1)); exemptions by regulation (22(9)); 22(2.2) para. 3 | Yes |
| British Columbia | 57 | vacation_entitlement | Yes | none | No | Yes |
| British Columbia | 59 | vacation_entitlement | Yes | none | No | Yes |
| British Columbia | 58 | vacation_pay | Yes | none | No | Yes |
| British Columbia | 60 | vacation_pay | Yes | none | No | Yes |
| British Columbia | 40 | overtime | Yes | none | No | Yes |
| British Columbia | 37 | overtime | Yes | none | No | Yes |
| British Columbia | 42 | overtime | Yes | none | No | Yes |

"Mentions regulations?" comes from reading the printed text. "Keep as target?" is filled in during Step 1.8 reading.

## All sections

| | Ontario (259) | British Columbia (160) |
|---|---|---|
| Exact match after normalization | 249 | 143 |
| Flagged | 10 | 17 (11 differ + 6 missing from the official parse) |

### Flagged sections, reviewed by hand

| Category | Sections | Verdict |
|---|---|---|
| **Repealed-subsection placeholders.** The official page lists e.g. "(4) Repealed" at the end of a section; the dataset leaves it out | ON 49.1, 49.4, 49.5, 49.7, 81, 97, 103, 118, 142 | Cosmetic, no legal text missing |
| Blank form line (`______`) | ON 146 | Cosmetic |
| Spacing | BC 76.1 | Cosmetic |
| **Fully repealed sections.** The dataset has `[Repealed …]` placeholders; the official page formats them outside the normal section markup | BC 69, 70, 107, 108, 128, 129 | Not legal text |
| Official page adds bracketed section titles in cross-reference lists | BC 3, 103 | Cosmetic (official annotation) |
| **Tables and formulas.** The dataset turns them into markdown tables (`\| --- \|`); the script doesn't read tables on the official page | BC 3, 16.2, 45, 49.1, 52.13 | **Not verified automatically.** The dataset content exists but is noisy for embeddings and the LLM. Exclude from training data or clean up |
| **Missing clause labels in definitions.** The dataset drops `(a)`, `(b)`, `(c)` in definition lists, even though the text refers to "paragraph (a), (b) or (c)" | BC 1, 49.2, 52.5, 96 | **Real dataset parsing defect.** Wording is otherwise identical. BC s.1 holds the Act's definitions (e.g. "regular wage", used by overtime s.40), so watch for it in retrieval |

## Summary
- Target sections: **13 / 13 match** the official text (ignoring formatting)
- All sections: **392 / 419 exact matches**. 0 substantive wording differences found; 4 BC sections have a real structural defect (missing clause labels); 5 BC sections contain tables/formulas that couldn't be verified automatically
