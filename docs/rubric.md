# Scoring rubric

**Version:** 1.2 · **Frozen:** 2026-11-03, before any experiment was run. Changes after that are logged in the changelog with a reason.

**Applies to:** the 30 questions in `data/evaluation.jsonl` (source: `docs/test_set.md`), scored the same way for every experiment (A–E).

---

## 1. Overview

| Measure | Unit | Scored by | Points |
|---|---|---|---|
| Key facts (incl. comparison verdicts) | each key fact | Script (numbers, dates) + human (wording) | 1 / 0 |
| Claims: supported? cited? | each claim | Human (script handles gold citations and a proxy) | Counted, not points |
| Abstention | each question (30) | Script + human for borderline wording | 1 / 0 |
| Output format | each JSON extraction | Script | Valid / invalid |
| Retrieval | each gold section | Script | Found / not found |
| Latency and tokens | each question | Script | Measured (seconds, tokens) |

Each measure is reported **separately**. None is deducted from another. They come together only in the **fully correct** check (§6).

**What is scored: the final answer, not the JSON.** The system works in two steps:
1. The model fills in a **JSON extraction** for each province: structured fields such as eligibility, entitlement, threshold, exceptions, section, and a supporting quote.
2. The pipeline turns those fields into the **final answer** the user sees: comparison table, text, and citations.

All content measures (key facts, claims, citations, abstention) are scored on the **final answer**. The JSON is checked automatically for only two things:
- **Is it valid?** (§5) Producing correct structured output is exactly what fine-tuning is meant to teach, so this is the most direct measure of whether SFT worked.
- **Do its supporting quotes appear in the retrieved text?** (grounding proxy, §3)

The final answer is built from the JSON, so the two shouldn't disagree. If they ever do, the final answer is what's scored.

---

## 2. Key facts (main accuracy measure)

| Label | Points | Meaning |
|---|---|---|
| **Correct** | 1 | Same meaning, number, and unit as the key fact |
| **Partial** | 0 | Fact present, but a condition or qualifier is missing or wrong. In legal text the conditions are often the point |
| **Incorrect** | 0 | Contradicts the key fact |
| **Missing** | 0 | Not mentioned |

| Question | Key fact | Model says | Label |
|---|---|---|---|
| Q05 | "Weekly overtime threshold is 44 hours" | "after 44 hours a week" | Correct |
| Q05 | same | "after 40 hours a week" | Incorrect |
| Q23 | "May be taken within 12 months with employee agreement" | "within 12 months" | Partial (without the agreement it reads as the employer's choice) |
| Q01 | "At least 2 weeks of vacation" | "2 weeks" | Correct (rule c) |

**Matching rules**
- **a. Numbers:** written and numeric forms are equal ("two weeks" = "2 weeks", "six per cent" = "6%"). Units must match.
- **b. Rates:** "1.5x" = "one and one-half times" = "time and a half"; "double" = "2x".
- **c. Minimums:** leaving out "at least" is not penalized; turning a minimum into a maximum ("no more than 2 weeks") is Incorrect.
- **d. Paraphrase:** Correct if a reasonable reader takes the same legal meaning ("your boss has to say yes" = "requires the employer's agreement").
- **e. Dates (Q24):** within ±1 day of the gold date is Correct.
- **f. Abstain questions:** their key facts describe what a correct abstention explains (e.g. "the regulations listing exemptions are not in the knowledge base") and are scored the same way. Q29's Alberta part has no key facts.
- **g. Hedging:** a hedged statement ("probably 2 weeks") is scored like a plain statement.

**Comparison verdict (Q11–Q18).** Each comparison question has one extra key fact: the verdict from its gold **Comparison** line (e.g. "Different: 10 months vs. 12 months"). It's labelled like any key fact. Correct requires the right verdict **and** the right reason; the per-province details are already covered by the other key facts.
- **"Same" (Q11, Q14):** the required reason is the shared value (3 weeks; 6%). Noting the wording difference is not required.
- **"Similar" (Q17):** any wording conveying "mostly the same, with a difference" counts, if the difference matches the gold.

**Scores (per experiment)**
- **Key-fact accuracy** (headline) = Correct key facts ÷ all key facts, across the 30 questions
- **Lenient key-fact accuracy** (secondary) = the same, with Partial counted as 0.5, to show near-misses
- **Per-category accuracy** = key-fact accuracy within each of the 5 categories; **macro-average** = mean of the 5, so the 10 direct-extraction questions don't dominate
- **Verdict accuracy** = Correct verdicts ÷ 8. Reported on its own because "does it say correctly whether the rules differ?" is the core product question
- **Exact-match accuracy** = share of numeric/date key facts whose gold value appears in the answer (script only; an automated cross-check of the human labels)
- **Condition omissions** = number of Partial labels (how often the number was right but the condition was dropped)

---

## 3. Claims: supported and cited

Every claim in an answer gets **two labels** in one pass. They answer different questions: *is it true?* and *does it point to the right source?* The research question asks about both (factual accuracy and source grounding), and they can disagree: a true claim can be cited wrongly, or not cited at all.

**A claim** = one distinct statement of a legal rule, number, or condition. The same claim repeated counts once. "4 weeks after 10 years, and 8% vacation pay" = 2 claims.

Not claims: general advice ("check with the Ministry of Labour"), stated uncertainty ("the Act doesn't say"), restating the question.

### Label 1: Supported?
| Label | Meaning |
|---|---|
| **Supported** | Supported by the text of the Ontario or BC Act (any section, not only the gold sections), including correct calculations from it (e.g. Q24's deadline date) |
| **Unsupported** | Not supported by either Act: invented rules or wrong numbers; a definitive answer on an abstain question ("farm workers are exempt"); one province's rule attributed to the other; any claim about a jurisdiction outside the knowledge base ("Alberta gives 4%") |

The same standard (the Act text) applies with and without RAG.

### Label 2: Citation
A **citation** is a section number attached to the claim, in the JSON `section` field or inline ("s. 33"). Section level is enough: "s. 22" counts for a rule in s. 22(7).

| Label | Meaning |
|---|---|
| **Supports** | The cited section contains this claim |
| **Doesn't support** | The section exists but doesn't contain this claim (e.g. s. 35.2 cited for vacation *weeks*, which are in s. 33; s. 35 cited for the *definition* of vacation year, which is in s. 1) |
| **Invalid** | The section doesn't exist, or belongs to the other province |
| **None** | The claim has no citation |

The script labels a citation **Supports** only when it's in the question's `gold_chunks` **and** attached to a claim about that jurisdiction. A human labels the rest.

### Example
| Claim | Supported? | Citation |
|---|---|---|
| "2 weeks after 12 consecutive months" | Supported | Supports (s. 57) |
| "4 weeks after 10 years" | Unsupported | Doesn't support (s. 33) |
| "time and a half after 8 hours a day" | Supported | None |

### Scores (per experiment)
These are **separate measures**; nothing is deducted from key-fact points. A wrong key fact is also an unsupported claim, and it counts in both: key facts measure whether the required facts are right, this measures whether *anything* stated is false.
- **Unsupported-claim rate** (headline) = % of answers with ≥ 1 unsupported claim
- **Unsupported claims per answer** = total unsupported claims ÷ 30
- **Citation accuracy** = citations labelled Supports ÷ all citations (None excluded)
- **Citation coverage** = % of answerable responses with ≥ 1 citation labelled Supports (responses that only abstain are excluded)
- **Grounding proxy (RAG experiments only, automated)** = % of JSON `supporting_quote`s that match the retrieved text (fuzzy match ≥ 0.9). Reported next to the human labels, never instead of them.

---

## 4. Abstention

**Abstain questions (Q27–Q30):** 1 point if the answer clearly says the abstain part can't be determined **and** gives no answer on it (a hedged answer like "probably yes" still counts as answering, rule g). Otherwise 0.
- **Q29:** 1 point only if it answers Ontario **and** abstains on Alberta.

**Answerable questions (Q01–Q26):** saying "can't determine" for a jurisdiction with a gold answer is a **false abstention**. That jurisdiction's key facts are scored Missing.

**Scores (reported together; a model that always abstains passes the first and fails the second)**
- **Abstention accuracy** = points ÷ 4
- **False-abstention rate** = % of the 26 answerable questions with ≥ 1 false abstention

---

## 5. Output format and retrieval (automated)

**JSON validity** = % of JSON extractions (one per jurisdiction per question) that parse **and** match the schema. One automatic retry is allowed; report "valid first time" and "valid after retry".

**Latency and tokens** = seconds per question, prompt tokens, and output tokens; mean and 95th percentile per experiment.

**Recall@k** (k = 1, 3, 5): for each question × jurisdiction, the share of its gold sections found in that jurisdiction's top-k results, averaged over all pairs. Q24 Ontario has 2 gold sections (s. 35, s. 1), so finding one scores 0.5. Alberta (Q29) has no gold sections and is skipped.

---

## 6. Fully correct (strictest headline)

A question is **fully correct** only if all of these hold:
1. Every key fact is Correct (including the verdict on Q11–Q18)
2. No unsupported claims
3. At least one citation labelled Supports, and none labelled Doesn't support or Invalid (not required for Q27, Q28, Q30, which are pure abstentions)
4. Abstention = 1 (Q27–Q30), or no false abstention (Q01–Q26)

**Fully correct rate** = fully correct questions ÷ 30, reported next to key-fact accuracy.

---

## 7. Scoring procedure

1. **Blind:** answers from all experiments are shuffled and their labels hidden while scoring. (Not perfectly blind: answers without retrieved quotes may reveal a no-RAG experiment.)
2. Score using only this rubric and the gold answers in `data/evaluation.jsonl`.
3. **Consistency check:** re-score a random 10% at the end without looking at the first scores; report the agreement rate (% of labels identical to the first scoring).
4. Record every judgment in a scoring sheet (one row per answer × key fact, and per answer × claim), so every reported number is traceable.

---

## Changelog

| Date | Version | Change | Reason |
|---|---|---|---|
| 2026-11-03 | 0.1 | Draft created | |
| 2026-11-03 | 0.2 | Partial scores 0 (lenient 0.5 kept as secondary) | Missing legal conditions change the meaning (Q23) |
| 2026-11-03 | 0.3 | Comparison verdict made binary | A right verdict with a wrong reason is misleading |
| 2026-11-03 | 1.0 | Defined claims and citations; separate measures with no point deductions; Q29 abstention binary; citations required for "fully correct"; blind scoring adopted; "Macro-F1" renamed to macro-averaged accuracy; frozen | Remove ambiguity before any experiment runs |
| 2026-11-03 | 1.1 | Unsupported claims and citations merged into one **Claims** section (two labels per claim, one scoring pass); comparison verdict folded into key facts as an extra key fact, still reported as verdict accuracy | Same claims were scored twice; the verdict used a separate mechanism and double-penalized per-province facts. Both research measures are kept. Made before any experiment ran |
| 2026-11-03 | 1.2 | Stated that content is scored on the final answer and the JSON only for validity and the grounding proxy; correct calculations count as supported; hedged statements scored as plain statements; defined fuzzy-match threshold, latency/token measures (added to the overview), and agreement rate; noted limits of blinding; removed the duplicate automated-vs-human section | Clarifications before any experiment ran; no change to strictness |
