# Blind scoring review (rubric v1.2)

Experiment labels are hidden. For each answer, check the AI pre-scores against the gold answer and the rubric; change any **bold** label you disagree with, then set **Reviewed:** yes. Format help is at the top of `src/review_sheet.py`.

## S001 · Q15 · cross_jurisdiction_comparison

**Question:** If someone works 45 hours in a week, would they get overtime in Toronto and Vancouver, or does it depend on where they work?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 22(1), 22(1.1)
  Answer: Overtime pay of at least one and one-half times the regular rate for each hour worked over 44 hours in a work week
  Who it applies to: Employee performs work of a particular kind or character, which is exempted by regulations or has an overtime threshold other than 44 hours
  Amount / threshold: At least 44 hours in a work week
  Mandatory?: mandatory
  Exceptions: The overtime pay is subject to the overtime threshold set out in the regulations
  Quote: "an employer shall pay an employee overtime pay of at least one and one-half times his or her regular rate"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 35
  Answer: Overtime wages must be paid at 1.5 times the regular wage for hours over 8, and 1.5 times the regular wage for hours over 40
  Who it applies to: Employer requires or allows the employee to work more than 8 hours per day or 40 hours per week
  Amount / threshold: More than 8 hours a day or 40 hours a week
  Mandatory?: mandatory
  Exceptions: Does not apply for employees working under an averaging agreement
  Quote: "An employer must pay an employee overtime wages in accordance with section 40"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 22): Ontario's general weekly overtime threshold is 44 hours, so hours beyond 44 qualify for overtime at a minimum of 1.5 times the regular rate.
- British Columbia (s. 40): BC's weekly overtime threshold is 40 hours, with hours beyond 40 paid at 1.5 times the regular wage. Daily overtime also applies to any day over 8 hours.
- Comparison: Different: Ontario pays overtime only for the hour over 44. In BC overtime is owed, but whether it comes from the weekly rule (over 40) or the daily rule (over 8 a day) depends on how the hours fall across the days.

**Key facts:**
- [ON] 44-hour weekly threshold → **Correct**
- [ON] At least 1.5 times the regular rate → **Correct**
- [BC] 40-hour weekly threshold → **Correct**
- [BC] 1.5 times the regular wage → **Correct**
- [BC] Daily overtime may also apply for any day over 8 hours → **Correct**
- [VERDICT] Different: Ontario pays overtime only for the hour over 44; in BC overtime is owed (weekly over 40 or daily over 8) → **Correct** — different, with 44 vs. 40/8 thresholds shown

**Claims:**
- "Ontario: at least 1.5 times the regular rate for each hour over 44 in a work week" → **Supported** | **Supports**
- "Ontario: Applies to employees whose work is exempted by regulation or has a different threshold" → **Unsupported** | **Doesn't support** — garbles s.22(2): those employees are the exception, not who it applies to
- "BC: overtime is owed for hours over 8 a day or 40 a week" → **Supported** | **Supports**
- "BC: paid at 1.5 times the regular wage" → **Supported** | **Doesn't support** — rate is in s.40, cited s.35
- "BC: doesn't apply to employees under an averaging agreement" → **Supported** | **Doesn't support** — s.37

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S002 · Q22 · exceptions

**Question:** What conditions must be met for a valid averaging agreement under BC's Employment Standards Act?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: The employer and employee must agree on the terms of the averaging agreement.
  Who it applies to: Valid averaging agreements require specific conditions to be met.
  Amount / threshold: There is no explicit mention of a minimum wage threshold for averaging agreements.
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 37): The agreement must be written, signed by both parties before its start date, specify the averaging period and daily work schedule, and meet the other statutory requirements.

**Key facts:**
- [BC] Must be in writing → **Missing**
- [BC] Must be signed before the start date → **Missing**
- [BC] Must specify a 1-, 2-, 3-, or 4-week period → **Missing**
- [BC] Must specify the daily work schedule → **Missing**
- [BC] Employee must receive a copy before the averaging period begins → **Missing**

**Claims:**
- "The employer and employee must agree on the terms of the averaging agreement" → **Supported** | **Invalid** — 'section' is the Act name

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S003 · Q18 · cross_jurisdiction_comparison

**Question:** Compare the vacation pay payment-timing requirements in Ontario and BC.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Payment Timing
  Who it applies to: Employee
  Amount / threshold: Pay Periods
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 58
  Answer: payment of vacation pay upon termination
  Who it applies to: any employee
  Amount / threshold: at least 5 calendar days of employment
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: different wording (check details)
```

**Gold:**
- Ontario (s. 36): Ontario requires vacation pay to be paid in a lump sum before the employee begins vacation by default. It may instead be paid each pay period if the employee agrees and the vacation pay is shown separately (other alternatives also exist, such as an agreed time).
- British Columbia (s. 58): BC requires vacation pay at least seven days before vacation begins, unless scheduled-payday payment is agreed to in writing or provided by a collective agreement.
- Comparison: Different: Ontario's default is a lump sum before vacation (with alternatives: payday, each pay period by agreement, or an agreed time); BC's default is at least 7 days before vacation, or on scheduled paydays if agreed in writing or by collective agreement.

**Key facts:**
- [ON] General rule is lump-sum payment before vacation → **Missing**
- [ON] Payment during each pay period requires an agreement and separate identification of vacation pay → **Missing**
- [BC] Payment at least 7 days before vacation → **Missing**
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**
- [VERDICT] Different: Ontario default lump sum before vacation; BC at least 7 days before, or scheduled paydays by written/collective agreement → **Partial** — 'different' for the wrong reason

**Claims:**
- "BC: vacation pay is paid on termination" → **Supported** | **Supports** — s.58(3)
- "BC: vacation pay applies after 5 calendar days of employment" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S004 · Q17 · cross_jurisdiction_comparison

**Question:** I want to split my vacation into single days instead of whole weeks. Can I do that in Ontario? What about in BC?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 35.1(2)
  Answer: Vacation must be completed no later than 10 months after the start of the first alternative vacation entitlement year, and if the entitlement is greater than five days, at least five consecutive days plus any remaining days in another period of consecutive days
  Amount / threshold: No later than 10 months after the first alternative vacation entitlement year, and at least five consecutive days plus any remaining days in another period of consecutive days if the entitlement is greater than five days
  Mandatory?: mandatory
  Quote: "the vacation shall be taken in a period of consecutive days"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 60
  Answer: Annual vacation of at least 2 weeks after 12 consecutive months of employment, or at least 3 weeks after 5 consecutive years of employment
  Who it applies to: Employer uses a common date for calculating annual vacation entitlements without reducing employees' rights under sections 57 and 58
  Amount / threshold: At least 2 weeks after 12 consecutive months, or at least 3 weeks after 5 consecutive years
  Mandatory?: optional
  Exceptions: Provisions of a collective agreement respecting statutory holidays only apply to other holidays, not the National Day for Truth and Reconciliation
  Quote: "so long as this does not result in a reduction of any employee's rights under those sections"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: unknown
```

**Gold:**
- Ontario (s. 35): By default, Ontario vacation is taken in whole weeks (a two-week period or two one-week periods; for 5+ years, combinations of one-, two-, or three-week periods). Shorter periods are allowed only if the employee requests them in writing and the employer agrees.
- British Columbia (s. 57): BC requires the employer to allow an employee to take annual vacation in periods of one or more weeks. Section 57 does not address periods shorter than a week.
- Comparison: Similar: both are built around whole weeks. Ontario allows shorter periods by written request plus employer agreement; BC requires the employer to allow periods of one week or more.

**Key facts:**
- [ON] Default is whole-week periods → **Missing** — answers the stub-period rules for an alternative vacation year
- [ON] Shorter periods only if the employee requests in writing and the employer agrees → **Missing**
- [BC] Employer must allow vacation in periods of one or more weeks → **Missing**
- [BC] Periods shorter than a week are not addressed in s. 57 → **Missing**
- [VERDICT] Similar: both built around whole weeks; Ontario allows shorter periods by written request plus employer agreement → **Incorrect** — says different, no valid reason

**Claims:**
- "Ontario (alternative vacation year stub period): vacation completed within 10 months; over five days, at least five consecutive days" → **Supported** | **Supports** — s.35.1(2); not the general rule asked about
- "BC: at least 2 weeks after 12 months, 3 weeks after 5 years" → **Supported** | **Doesn't support** — s.57, cited s.60
- "BC: an employer may use a common date if no employee's rights are reduced" → **Supported** | **Supports**
- "BC: collective agreement statutory-holiday provisions don't extend to the National Day for Truth and Reconciliation" → **Supported** | **Doesn't support** — s.3 territory, cited s.60; irrelevant

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S005 · Q24 · dates_thresholds

**Question:** I started my job in Toronto on March 15, 2025. My manager says I have to use my vacation within 10 months of my vacation year ending. Can I save it and take it over the Christmas holidays this year (2026)?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 33
  Answer: Clause (1) (b)
  Who it applies to: at least two weeks after each vacation entitlement year that the employee completes
  Amount / threshold: five years or more
  Mandatory?: mandatory
  Quote: "An employer shall give an employee a vacation of, at least two weeks after each vacation entitlement year that the employee completes, if the employee’s period of employment is less than five years; or at least three weeks after each vacation entitlement year that the employee completes, if the employee’s period of employment is five years or more."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 35, 1): Likely yes, timing-wise. Under the standard vacation entitlement year (which starts on the employee's first day of work), the first year ran March 15, 2025 to March 14, 2026. Vacation for that year must be completed within 10 months after it ends, so by about January 14, 2027, and December 2026 falls inside that window. However, the employer decides when vacation is taken, so the employee can request December but cannot insist. If the employer uses an alternative vacation entitlement year, the dates would be different.

**Key facts:**
- [ON] Deadline is 10 months after the end of the vacation entitlement year → **Missing**
- [ON] Standard vacation entitlement year starts on the employee's first day of employment → **Missing**
- [ON] First year ended March 14, 2026, so the deadline is about January 14, 2027 → **Missing**
- [ON] December 2026 is within the deadline → **Missing**
- [ON] The employer determines when vacation is taken → **Missing**
- [ON] Dates differ if the employer uses an alternative vacation entitlement year → **Missing**

**Claims:**
- "Ontario: at least two weeks after each vacation entitlement year (under 5 years), three weeks (5+ years)" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S006 · Q03 · direct_extraction

**Question:** I work in Ontario and have only been here for two years. How much vacation pay am I owed?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 35.2
  Answer: Vacation pay
  Who it applies to: Employee
  Amount / threshold: 4% or 6% of wages
  Mandatory?: mandatory
  Quote: "An employer shall pay vacation pay to an employee who is entitled to vacation under section 33 or 34, equal to at least, (a) 4 per cent of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given, if the employee’s period of employment is less than five years; or (b) 6 per cent of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given, if the employee’s period of employment is five years or more."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 35.2): The employee is entitled to vacation pay of at least 4% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Correct** — 4% or 6%; the quote ties 4% to under 5 years
- [ON] Vacation pay is excluded from the wage calculation → **Correct** — in the quote

**Claims:**
- "Vacation pay is at least 4% of wages if employed under 5 years, 6% if 5 years or more" → **Supported** | **Supports**
- "Wages exclude vacation pay" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S007 · Q29 · insufficient_evidence

**Question:** My sister works in Calgary and I work in Toronto. We've both been at our jobs for 2 years. Do we get the same vacation pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 20.1(1)(a)
  Answer: Vacation pay
  Who it applies to: Employees
  Amount / threshold: 2 years
  Mandatory?: mandatory

ALBERTA: not covered. This tool only includes the Ontario and British Columbia Employment Standards Acts, so it cannot answer for this province.
```

**Gold:**
- Ontario (s. 35.2): An Ontario employee with less than five years of employment is entitled to vacation pay of at least 4% of wages, excluding vacation pay, earned during the relevant period.
- Abstain (Alberta): Alberta legislation is not in the knowledge base. The system should answer for Ontario and say it cannot speak to Alberta.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing**

**Claims:**
- (no claims)

**Abstention:** **1**   **False abstention:** **no**

**Reviewed:** yes

---

## S008 · Q04 · direct_extraction

**Question:** What is the minimum vacation pay percentage for an Ontario employee with at least five years of employment?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 35.2
  Answer: pay vacation pay
  Who it applies to: An employer shall pay vacation pay to an employee who is entitled to vacation under section 33 or 34
  Amount / threshold: at least 4% of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given
  Mandatory?: mandatory
  Quote: "An employer shall pay vacation pay to an employee who is entitled to vacation under section 33 or 34, equal to at least, (a) 4 per cent of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given, if the employee’s period of employment is less than five years; or (b) 6 per cent of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given, if the employee’s period of employment is five years or more."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 35.2): The employee must receive vacation pay equal to at least 6% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 6% vacation pay → **Incorrect** — threshold line says 'at least 4%'; 6% only inside the quote
- [ON] Vacation pay is excluded from the wage calculation → **Correct**

**Claims:**
- "Vacation pay is at least 4% of wages, given as the answer for 5+ years" → **Unsupported** | **Doesn't support** — 4% is the under-5-years rate
- "6% of wages if employed five years or more (in the quote)" → **Supported** | **Supports**
- "Wages exclude vacation pay" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S009 · Q24 · dates_thresholds

**Question:** I started my job in Toronto on March 15, 2025. My manager says I have to use my vacation within 10 months of my vacation year ending. Can I save it and take it over the Christmas holidays this year (2026)?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 108(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 10 months
  Mandatory?: mandatory
  Quote: "It is mandatory for an employer to ensure that an employee has a reasonable opportunity to take a vacation within a reasonable period of time after the end of the employee's vacation year."
```

**Gold:**
- Ontario (s. 35, 1): Likely yes, timing-wise. Under the standard vacation entitlement year (which starts on the employee's first day of work), the first year ran March 15, 2025 to March 14, 2026. Vacation for that year must be completed within 10 months after it ends, so by about January 14, 2027, and December 2026 falls inside that window. However, the employer decides when vacation is taken, so the employee can request December but cannot insist. If the employer uses an alternative vacation entitlement year, the dates would be different.

**Key facts:**
- [ON] Deadline is 10 months after the end of the vacation entitlement year → **Partial** — "10 months" shown as the threshold, but beside an invented quote and without "after the end of the vacation entitlement year" (human review)
- [ON] Standard vacation entitlement year starts on the employee's first day of employment → **Missing**
- [ON] First year ended March 14, 2026, so the deadline is about January 14, 2027 → **Missing**
- [ON] December 2026 is within the deadline → **Missing**
- [ON] The employer determines when vacation is taken → **Missing**
- [ON] Dates differ if the employer uses an alternative vacation entitlement year → **Missing**

**Claims:**
- "The employer must ensure a reasonable opportunity to take vacation within a reasonable period after the vacation year" → **Unsupported** | **Doesn't support** — invented quote; s.108 is unrelated

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S010 · Q02 · direct_extraction

**Question:** I've been at my job in Vancouver for six years now. Do I get any more vacation time than when I started?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 127(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 6 years
  Mandatory?: mandatory
  Quote: "Section 127(1)(a) of the Employment Standards Act (British Columbia) states that an employee is entitled to a minimum of 10 days of vacation time for every 12 months of service."
```

**Gold:**
- British Columbia (s. 57): Yes. After five consecutive years of employment, the entitlement increases from at least two weeks to at least three weeks of annual vacation.

**Key facts:**
- [BC] At least 3 weeks of annual vacation → **Missing**
- [BC] Up from at least 2 weeks before reaching 5 years → **Missing**
- [BC] 5 consecutive years of employment → **Missing**

**Claims:**
- "An employee is entitled to a minimum of 10 days of vacation for every 12 months of service" → **Unsupported** | **Doesn't support** — invented quote attributed to s.127(1)(a), which is a regulation-making power

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S011 · Q09 · direct_extraction

**Question:** Can a BC employer use a single common date to calculate annual vacation entitlement for all of its employees?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 60): Yes. An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58, as long as this does not reduce any employee's rights under those sections.

**Key facts:**
- [BC] A common date for all employees is permitted → **Missing**
- [BC] Must not reduce any employee's rights under those sections → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S012 · Q11 · cross_jurisdiction_comparison

**Question:** I've worked at my job in Ottawa for 6 years. Would someone who's worked 6 years at a job in Vancouver get the same amount of vacation as me?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: Vacation pay
  Who it applies to: All employees
  Amount / threshold: 6 years of continuous service
  Mandatory?: Yes

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment standards
  Answer: Vacation pay
  Who it applies to: Yes
  Amount / threshold: 6 years of continuous service
  Mandatory?: mandatory

COMPARISON: UNCLEAR
  entitlement or requirement: same
  threshold: same
  eligibility: different wording (check details)
```

**Gold:**
- Ontario (s. 33): With five or more years of employment, an Ontario employee is entitled to at least three weeks of vacation.
- British Columbia (s. 57): After five consecutive years of employment, a BC employee is entitled to at least three weeks of annual vacation.
- Comparison: Same: both at least 3 weeks after 5 years. Ontario ties it to completed vacation entitlement years; BC to consecutive years of employment.

**Key facts:**
- [ON] At least 3 weeks at 5 years or more → **Missing**
- [BC] At least 3 weeks after 5 consecutive years → **Missing**
- [VERDICT] Same: both at least 3 weeks after 5 years → **Missing** — verdict 'unclear'

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S013 · Q06 · direct_extraction

**Question:** I just finished my first year working in BC. Am I supposed to get two weeks off now?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment standards
  Answer: Two weeks paid vacation after one year of continuous employment
  Who it applies to: All employees
  Amount / threshold: One year of continuous employment
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 57): Yes. After 12 consecutive months of employment, an employee is entitled to at least two weeks of annual vacation.

**Key facts:**
- [BC] At least 2 weeks of annual vacation → **Correct**

**Claims:**
- "Two weeks of paid vacation after one year of continuous employment" → **Supported** | **Invalid** — 'Employment standards' is not a section

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S014 · Q12 · cross_jurisdiction_comparison

**Question:** Compare the deadline for an employee to take earned vacation in Ontario and British Columbia.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Deadline for taking earned vacation
  Who it applies to: All employees
  Amount / threshold: 10 months after the end of the vacation entitlement year
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 57
  Answer: annual vacation entitlement
  Who it applies to: all employees
  Amount / threshold: at least 2 weeks after 12 consecutive months of employment, or at least 3 weeks after 5 consecutive years of employment
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: same
```

**Gold:**
- Ontario (s. 35): Vacation must be completed no later than 10 months after the end of the vacation entitlement year for which it is given.
- British Columbia (s. 57): Annual vacation must be taken within 12 months after completing the year of employment that entitles the employee to it.
- Comparison: Different: 10 months in Ontario vs. 12 months in BC.

**Key facts:**
- [ON] No later than 10 months after the end of the vacation entitlement year → **Correct**
- [BC] Within 12 months after completing the entitling year of employment → **Missing** — gives amounts, not the deadline
- [VERDICT] Different: 10 months in Ontario vs. 12 months in BC → **Partial** — 'different', but not because of 10 vs. 12 months

**Claims:**
- "Ontario: vacation must be taken within 10 months after the end of the vacation entitlement year" → **Supported** | **Invalid** — 'section' is the Act name
- "BC: at least 2 weeks after 12 months, 3 weeks after 5 years" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S015 · Q22 · exceptions

**Question:** What conditions must be met for a valid averaging agreement under BC's Employment Standards Act?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 37
  Answer: a valid averaging agreement under this section as terms of the agreement
  Who it applies to: An averaging agreement under subsection (1) is not valid unless
  Amount / threshold: the agreement
  Mandatory?: is not valid unless
  Exceptions: i; s;  ; n; o; t;  ; v; a; l; i; d;  ; u; n; l; e; s; s
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 37): The agreement must be written, signed by both parties before its start date, specify the averaging period and daily work schedule, and meet the other statutory requirements.

**Key facts:**
- [BC] Must be in writing → **Missing**
- [BC] Must be signed before the start date → **Missing**
- [BC] Must specify a 1-, 2-, 3-, or 4-week period → **Missing**
- [BC] Must specify the daily work schedule → **Missing**
- [BC] Employee must receive a copy before the averaging period begins → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S016 · Q06 · direct_extraction

**Question:** I just finished my first year working in BC. Am I supposed to get two weeks off now?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 52.1(4)
  Answer: An employee may start a leave no earlier than that day
  Who it applies to: The period under subsection (2) begins on the first day of the week
  Mandatory?: optional
  Quote: "an employee who, due to serious personal illness or injury"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 57): Yes. After 12 consecutive months of employment, an employee is entitled to at least two weeks of annual vacation.

**Key facts:**
- [BC] At least 2 weeks of annual vacation → **Missing** — answers compassionate care leave start date

**Claims:**
- "An employee may start the leave no earlier than the first day of the week in which the period begins" → **Supported** | **Supports** — s.52.1(4); irrelevant

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S017 · Q09 · direct_extraction

**Question:** Can a BC employer use a single common date to calculate annual vacation entitlement for all of its employees?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Vacation entitlement calculation
  Answer: Use of a single common date
  Who it applies to: All employers
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 60): Yes. An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58, as long as this does not reduce any employee's rights under those sections.

**Key facts:**
- [BC] A common date for all employees is permitted → **Partial** — 'Use of a single common date' presented as mandatory
- [BC] Must not reduce any employee's rights under those sections → **Missing**

**Claims:**
- "Employers must use a single common date" → **Unsupported** | **Invalid** — s.60 is a permission; 'Vacation entitlement calculation' is not a section

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S018 · Q25 · dates_thresholds

**Question:** I started a new job in BC last week. How long do I have to work before I'm entitled to vacation pay?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: Entitled to vacation pay after working at least 120 hours
  Who it applies to: New employees
  Amount / threshold: 120 hours
  Mandatory?: Yes
```

**Gold:**
- British Columbia (s. 58): An employee qualifies for at least 4% vacation pay after five calendar days of employment.

**Key facts:**
- [BC] 5 calendar days of employment → **Incorrect** — says 120 hours
- [BC] Minimum 4% vacation pay → **Missing**
- [BC] Based on total wages during the relevant year → **Missing**

**Claims:**
- "Vacation pay after at least 120 hours of work" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S019 · Q01 · direct_extraction

**Question:** I've been working in Toronto for about 3 years. How much paid time off am I supposed to get each year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: entitlement to be paid a fixed amount for each pay period
  Who it applies to: An employee is considered to be paid a salary for the purposes of subsection (3) if, (a) the employee is entitled to be paid a fixed amount for each pay period; and (b) the amount actually paid for each pay period does not vary according to the number of hours worked by the employee, unless he or she works more than 44 hours in a week.
  Amount / threshold: the amount actually paid for each pay period does not vary according to the number of hours worked by the employee, unless he or she works more than 44 hours in a week.
  Mandatory?: mandatory
  Exceptions: N; o; n; e
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.
```

**Gold:**
- Ontario (s. 33): At least two weeks of vacation each year (the two-week level applies to employees with less than five years of employment).

**Key facts:**
- [ON] At least 2 weeks of vacation → **Missing** — answers the salaried-employee definition instead

**Claims:**
- "An employee is considered paid a salary if paid a fixed amount per pay period that doesn't vary with hours unless they work over 44 hours a week" → **Supported** | **Invalid** — true (ON s.15) but irrelevant; 'section' is the Act name

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S020 · Q20 · exceptions

**Question:** How must an employer calculate vacation entitlement for an Ontario employee during a stub period created by an alternative vacation entitlement year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 510.1(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 34): The employer must calculate the ratio of the stub period to 12 months and apply it to the employee's applicable two-week or three-week vacation entitlement, using a separate calculation for employees without a regular work week.

**Key facts:**
- [ON] Calculate stub-period-to-12-month ratio → **Missing**
- [ON] Less than 5 years: use 2 weeks as the base → **Missing**
- [ON] 5 years or more: use 3 weeks as the base → **Missing**
- [ON] Employees without a regular work week use average weekly working days → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S021 · Q08 · direct_extraction

**Question:** I'm working a 10-hour shift in BC today. Should the last couple of hours be paid at a higher rate?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: Employees must be compensated at one and one-half times their regular wage for all hours worked over the standard eight-hour period or forty-hour workweek.
  Who it applies to: All employees who work more than eight hours per day or forty hours per week must receive overtime pay.
  Amount / threshold: Eight hours per day or forty hours per week
  Mandatory?: Yes
```

**Gold:**
- British Columbia (s. 40): If the employee is not working under an averaging agreement, hours beyond eight in a day must be paid at 1.5 times the regular wage.

**Key facts:**
- [BC] Hours over 8 a day are paid at 1.5 times the regular wage → **Correct**
- [BC] No averaging agreement applies → **Missing**

**Claims:**
- "1.5 times the regular wage for hours over 8 a day or 40 a week" → **Supported** | **Invalid** — s.40; 'Employment Standards Act' is not a section

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S022 · Q02 · direct_extraction

**Question:** I've been at my job in Vancouver for six years now. Do I get any more vacation time than when I started?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 57
  Answer: at least 2 weeks
  Who it applies to: after 12 consecutive months of employment
  Amount / threshold: 2 weeks
  Mandatory?: mandatory
  Quote: "An employer must give an employee an annual vacation of at least 2 weeks, after 12 consecutive months of employment, or at least 3 weeks, after 5 consecutive years of employment."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 57): Yes. After five consecutive years of employment, the entitlement increases from at least two weeks to at least three weeks of annual vacation.

**Key facts:**
- [BC] At least 3 weeks of annual vacation → **Incorrect** — headline answer for a 6-year employee is 'at least 2 weeks'; the 3-week rule appears only inside the quote
- [BC] Up from at least 2 weeks before reaching 5 years → **Correct**
- [BC] 5 consecutive years of employment → **Correct** — in the quote

**Claims:**
- "At least 2 weeks of vacation after 12 consecutive months" → **Supported** | **Supports**
- "At least 3 weeks after 5 consecutive years (in the quote)" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S023 · Q30 · insufficient_evidence

**Question:** I'm a software developer in Vancouver. Do tech workers get overtime in BC?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 35
  Answer: Overtime wages
  Who it applies to: Employee
  Amount / threshold: 8 hours a day or 40 hours a week
  Mandatory?: mandatory
  Quote: "An employer must pay an employee overtime wages in accordance with section 40 if the employer requires, or directly or indirectly allows, the employee to work more than 8 hours a day or 40 hours a week."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): Cannot be determined from the Acts in the knowledge base. Section 40 sets the general overtime rules, but the BC Act's text does not address whether tech workers are excluded.
- Abstain (British Columbia): whether tech workers are excluded from overtime is not addressed in the BC Act; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Section 40 sets general overtime rules (1.5x over 8 hours a day or 40 a week; double over 12 hours a day) → **Partial** — 8/40 thresholds without the rates
- [BC] The BC Act does not mention technology workers; any occupation-specific exclusion would be in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- "Overtime is owed under s.40 for over 8 hours a day or 40 a week" → **Supported** | **Supports**

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S024 · Q18 · cross_jurisdiction_comparison

**Question:** Compare the vacation pay payment-timing requirements in Ontario and BC.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 28(1)(a)
  Answer: Employers must pay vacation pay within 30 days after the end of the employee's last day of work
  Who it applies to: Employers with 50 or more employees
  Amount / threshold: Employers must pay vacation pay within 30 days after the end of the employee's last day of work
  Mandatory?: mandatory

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 28(1)(a)
  Answer: Employers must pay vacation pay within 30 days after the end of the employee's last day of work
  Who it applies to: Employers
  Amount / threshold: Employers must pay vacation pay within 30 days after the end of the employee's last day of work
  Mandatory?: mandatory

COMPARISON: DIFFERENT
  entitlement or requirement: same
  threshold: same
  eligibility: different
```

**Gold:**
- Ontario (s. 36): Ontario requires vacation pay to be paid in a lump sum before the employee begins vacation by default. It may instead be paid each pay period if the employee agrees and the vacation pay is shown separately (other alternatives also exist, such as an agreed time).
- British Columbia (s. 58): BC requires vacation pay at least seven days before vacation begins, unless scheduled-payday payment is agreed to in writing or provided by a collective agreement.
- Comparison: Different: Ontario's default is a lump sum before vacation (with alternatives: payday, each pay period by agreement, or an agreed time); BC's default is at least 7 days before vacation, or on scheduled paydays if agreed in writing or by collective agreement.

**Key facts:**
- [ON] General rule is lump-sum payment before vacation → **Incorrect** — says within 30 days after the last day of work
- [ON] Payment during each pay period requires an agreement and separate identification of vacation pay → **Missing**
- [BC] Payment at least 7 days before vacation → **Incorrect** — says within 30 days after the last day of work
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**
- [VERDICT] Different: Ontario default lump sum before vacation; BC at least 7 days before, or scheduled paydays by written/collective agreement → **Partial** — 'different' only on eligibility

**Claims:**
- "Ontario: employers with 50+ employees must pay vacation pay within 30 days after the employee's last day" → **Unsupported** | **Doesn't support**
- "BC: employers must pay vacation pay within 30 days after the employee's last day" → **Unsupported** | **Doesn't support** — s.28 is payroll records

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S025 · Q09 · direct_extraction

**Question:** Can a BC employer use a single common date to calculate annual vacation entitlement for all of its employees?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 60
  Answer: use a common date for calculating annual vacation entitlement
  Who it applies to: BC employers
  Amount / threshold: not specified
  Mandatory?: mandatory
  Quote: "An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58, so long as this does not result in a reduction of any employee's rights under those sections."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 60): Yes. An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58, as long as this does not reduce any employee's rights under those sections.

**Key facts:**
- [BC] A common date for all employees is permitted → **Correct**
- [BC] Must not reduce any employee's rights under those sections → **Correct** — in the quote

**Claims:**
- "An employer may use a common date for all employees if no employee's rights under ss.57–58 are reduced" → **Supported** | **Supports**
- "The rule is mandatory" → **Unsupported** | **Doesn't support** — wrong 'Mandatory?' label on a question about what is allowed

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S026 · Q30 · insufficient_evidence

**Question:** I'm a software developer in Vancouver. Do tech workers get overtime in BC?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 35
  Answer: overtime wages
  Who it applies to: software developers in Vancouver
  Amount / threshold: more than 8 hours a day or 40 hours a week
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): Cannot be determined from the Acts in the knowledge base. Section 40 sets the general overtime rules, but the BC Act's text does not address whether tech workers are excluded.
- Abstain (British Columbia): whether tech workers are excluded from overtime is not addressed in the BC Act; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Section 40 sets general overtime rules (1.5x over 8 hours a day or 40 a week; double over 12 hours a day) → **Partial** — 8/40 thresholds without the rates
- [BC] The BC Act does not mention technology workers; any occupation-specific exclusion would be in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- "Software developers in Vancouver get overtime for more than 8 hours a day or 40 a week" → **Unsupported** | **Supports** — definitive answer on an abstain question; the general rule is in s.35

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S027 · Q15 · cross_jurisdiction_comparison

**Question:** If someone works 45 hours in a week, would they get overtime in Toronto and Vancouver, or does it depend on where they work?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: Employees must be paid time-and-a-half for all hours worked over 40 hours in a workweek.
  Who it applies to: All employees who have worked at least one hour during the pay period.
  Amount / threshold: 40 hours per workweek
  Mandatory?: mandatory

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: Employees must be paid overtime when working more than 40 hours per week.
  Who it applies to: All employees who have worked at least one hour during the pay period.
  Amount / threshold: 40 hours per week
  Mandatory?: mandatory

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: same
  eligibility: same
```

**Gold:**
- Ontario (s. 22): Ontario's general weekly overtime threshold is 44 hours, so hours beyond 44 qualify for overtime at a minimum of 1.5 times the regular rate.
- British Columbia (s. 40): BC's weekly overtime threshold is 40 hours, with hours beyond 40 paid at 1.5 times the regular wage. Daily overtime also applies to any day over 8 hours.
- Comparison: Different: Ontario pays overtime only for the hour over 44. In BC overtime is owed, but whether it comes from the weekly rule (over 40) or the daily rule (over 8 a day) depends on how the hours fall across the days.

**Key facts:**
- [ON] 44-hour weekly threshold → **Incorrect** — says 40 hours
- [ON] At least 1.5 times the regular rate → **Correct**
- [BC] 40-hour weekly threshold → **Correct**
- [BC] 1.5 times the regular wage → **Missing**
- [BC] Daily overtime may also apply for any day over 8 hours → **Missing**
- [VERDICT] Different: Ontario pays overtime only for the hour over 44; in BC overtime is owed (weekly over 40 or daily over 8) → **Partial** — 'different' for the wrong reason (both shown as 40)

**Claims:**
- "Ontario: time and a half for hours over 40 in a workweek" → **Unsupported** | **Invalid**
- "BC: overtime after 40 hours a week" → **Supported** | **Invalid**
- "Applies to employees who worked at least one hour in the pay period" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S028 · Q11 · cross_jurisdiction_comparison

**Question:** I've worked at my job in Ottawa for 6 years. Would someone who's worked 6 years at a job in Vancouver get the same amount of vacation as me?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Provide employees with a period of employment of at least five years or more with at least three weeks of vacation after each vacation entitlement year that ends on or after December 31, 2017.
  Who it applies to: An employee's period of employment is at least five years.
  Amount / threshold: Five years of continuous employment.
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 57
  Answer: annual vacation
  Who it applies to: any employee
  Amount / threshold: at least 5 years of employment
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: same
  eligibility: different
```

**Gold:**
- Ontario (s. 33): With five or more years of employment, an Ontario employee is entitled to at least three weeks of vacation.
- British Columbia (s. 57): After five consecutive years of employment, a BC employee is entitled to at least three weeks of annual vacation.
- Comparison: Same: both at least 3 weeks after 5 years. Ontario ties it to completed vacation entitlement years; BC to consecutive years of employment.

**Key facts:**
- [ON] At least 3 weeks at 5 years or more → **Correct**
- [BC] At least 3 weeks after 5 consecutive years → **Missing** — no amount given
- [VERDICT] Same: both at least 3 weeks after 5 years → **Incorrect** — says different

**Claims:**
- "Ontario: at least three weeks after each vacation entitlement year once employed 5 years or more" → **Supported** | **Invalid** — 'section' is the Act name
- "Ontario and BC give different amounts of vacation at 6 years" → **Unsupported** | **None** — comparison verdict; both are 3 weeks

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S029 · Q24 · dates_thresholds

**Question:** I started my job in Toronto on March 15, 2025. My manager says I have to use my vacation within 10 months of my vacation year ending. Can I save it and take it over the Christmas holidays this year (2026)?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 33(1), 33(4), 34(5)
  Answer: At least three weeks of vacation after each vacation entitlement year that ends on or after December 31, 2017
  Who it applies to: Employee's period of employment is at least five years or more
  Amount / threshold: Three weeks of vacation after each vacation entitlement year that ends on or after December 31, 2017
  Mandatory?: mandatory
  Exceptions: Employers are required to provide at least five years of employment with at least three weeks of vacation after each vacation entitlement year that ends on or after December 31, 2017
  Quote: "if the employee’s period of employment is five years or more"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 35, 1): Likely yes, timing-wise. Under the standard vacation entitlement year (which starts on the employee's first day of work), the first year ran March 15, 2025 to March 14, 2026. Vacation for that year must be completed within 10 months after it ends, so by about January 14, 2027, and December 2026 falls inside that window. However, the employer decides when vacation is taken, so the employee can request December but cannot insist. If the employer uses an alternative vacation entitlement year, the dates would be different.

**Key facts:**
- [ON] Deadline is 10 months after the end of the vacation entitlement year → **Missing**
- [ON] Standard vacation entitlement year starts on the employee's first day of employment → **Missing**
- [ON] First year ended March 14, 2026, so the deadline is about January 14, 2027 → **Missing**
- [ON] December 2026 is within the deadline → **Missing**
- [ON] The employer determines when vacation is taken → **Missing**
- [ON] Dates differ if the employer uses an alternative vacation entitlement year → **Missing**

**Claims:**
- "Ontario: at least three weeks after each vacation entitlement year once employed 5+ years" → **Supported** | **Supports** — not relevant to a 1.5-year employee

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S030 · Q13 · cross_jurisdiction_comparison

**Question:** We have staff in Toronto and Vancouver who'd rather bank their overtime and take time off later. Can we do that in both provinces, and do the rules differ?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 29(1) and 29(2)
  Answer: Entitlement
  Who it applies to: Employees
  Amount / threshold: 160 hours
  Mandatory?: mandatory
  Quote: "The Ontario Employment Standards Act, 2000 (Ontario) does not allow employees to bank their overtime and take time off later. All employees are entitled to the minimum wage for all hours worked, including overtime, and must be paid for all hours worked."

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 203(1)(a)
  Answer: Entitlement
  Who it applies to: Employees
  Amount / threshold: 40 hours
  Mandatory?: mandatory
  Quote: "The Employment Standards Act, 2000, as amended, sets out the minimum standards for employment conditions in British Columbia."

COMPARISON: DIFFERENT
  entitlement or requirement: same
  threshold: different
  eligibility: same
```

**Gold:**
- Ontario (s. 22): Yes, if the employer and employee agree. The employee receives 1.5 hours of paid time off for each overtime hour, taken within 3 months of the work week in which it was earned (or within 12 months with the employee's agreement). If employment ends before the time off is taken, overtime pay is owed.
- British Columbia (s. 42): Yes. At the employee's written request, the employer may set up a time bank and credit overtime wages to it at overtime rates. The employee can ask at any time to be paid out, to use the credit for paid time off at an agreed time, or to close the bank. The employer may close it with one month's written notice and must settle it within 6 months. The balance must be paid on termination or when the employee asks to close it.
- Comparison: Different: both allow banking overtime, but Ontario uses an agreement with a 3- or 12-month deadline to take the time off, while BC uses a time bank set up at the employee's written request, with no use-by deadline stated while it is open.

**Key facts:**
- [ON] Requires agreement between employer and employee → **Incorrect** — says banking isn't allowed
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Taken within 3 months, or within 12 months with the employee's agreement → **Missing**
- [ON] Paid out as overtime pay if employment ends first → **Missing**
- [BC] Set up at the employee's written request → **Missing**
- [BC] Overtime credited at overtime rates → **Missing**
- [BC] Employee may request payout, time off, or closing at any time → **Missing**
- [BC] Employer may close with 1 month's written notice and settle within 6 months → **Missing**
- [BC] Balance paid on termination or on the employee's request to close → **Missing**
- [VERDICT] Different: both allow banking overtime; Ontario by agreement with a 3- or 12-month deadline, BC by a time bank at the employee's written request → **Partial** — 'different' for an invalid reason

**Claims:**
- "Ontario does not allow employees to bank overtime and take time off later" → **Unsupported** | **Doesn't support** — invented quote; s.22(7) allows it by agreement

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S031 · Q13 · cross_jurisdiction_comparison

**Question:** We have staff in Toronto and Vancouver who'd rather bank their overtime and take time off later. Can we do that in both provinces, and do the rules differ?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 22
  Answer: overtime pay
  Who it applies to: paid time off
  Amount / threshold: 44 hours
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 42
  Answer: credit the employee's overtime wages to the time bank
  Who it applies to: At the written request of an employee
  Amount / threshold: within the time required under section 17
  Mandatory?: mandatory
  Exceptions: N; o; t;  ; s; p; e; c; i; f; i; e; d;  ; i; n;  ; t; h; e;  ; e; x; c; e; r; p; t
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: different wording (check details)
```

**Gold:**
- Ontario (s. 22): Yes, if the employer and employee agree. The employee receives 1.5 hours of paid time off for each overtime hour, taken within 3 months of the work week in which it was earned (or within 12 months with the employee's agreement). If employment ends before the time off is taken, overtime pay is owed.
- British Columbia (s. 42): Yes. At the employee's written request, the employer may set up a time bank and credit overtime wages to it at overtime rates. The employee can ask at any time to be paid out, to use the credit for paid time off at an agreed time, or to close the bank. The employer may close it with one month's written notice and must settle it within 6 months. The balance must be paid on termination or when the employee asks to close it.
- Comparison: Different: both allow banking overtime, but Ontario uses an agreement with a 3- or 12-month deadline to take the time off, while BC uses a time bank set up at the employee's written request, with no use-by deadline stated while it is open.

**Key facts:**
- [ON] Requires agreement between employer and employee → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Taken within 3 months, or within 12 months with the employee's agreement → **Missing**
- [ON] Paid out as overtime pay if employment ends first → **Missing**
- [BC] Set up at the employee's written request → **Correct**
- [BC] Overtime credited at overtime rates → **Missing**
- [BC] Employee may request payout, time off, or closing at any time → **Missing**
- [BC] Employer may close with 1 month's written notice and settle within 6 months → **Missing**
- [BC] Balance paid on termination or on the employee's request to close → **Missing**
- [VERDICT] Different: both allow banking overtime; Ontario by agreement with a 3- or 12-month deadline, BC by a time bank at the employee's written request → **Partial** — no valid reason given

**Claims:**
- "Ontario: overtime after 44 hours" → **Supported** | **Supports**
- "BC: at the employee's written request, overtime wages can be credited to a time bank instead of paid" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S032 · Q14 · cross_jurisdiction_comparison

**Question:** We've got employees in Toronto and Vancouver who've both been here for six years. Do they get the same vacation pay percentage?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Equal to at least 4% of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given, if the employee's period of employment is less than five years; or 6% if the employee's period of employment is five years or more.
  Who it applies to: Employees in Toronto and Vancouver who have worked for six years.
  Amount / threshold: Five years or more
  Mandatory?: mandatory
  Exceptions: If the employee is represented by a trade union; If the employer makes contributions for vacation pay to the trustees of a multi-employer vacation benefit plan
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 58
  Answer: Vacation pay
  Who it applies to: After 5 calendar days of employment, after 5 consecutive years of employment
  Amount / threshold: At least 4% of the employee's total wages during the year of employment entitling the employee to the vacation pay
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 35.2): At least 6% of wages, excluding vacation pay, for employees with five or more years of employment.
- British Columbia (s. 58): At least 6% of total wages during the relevant year after five consecutive years of employment.
- Comparison: Same: both at least 6% after five years. The wage base is worded differently (Ontario: wages excluding vacation pay earned in the period; BC: total wages in the entitling year).

**Key facts:**
- [ON] Minimum 6% → **Correct**
- [ON] Excludes vacation pay from wages → **Correct**
- [BC] Minimum 6% → **Incorrect** — gives 4% for a 6-year employee
- [BC] Based on total wages during the relevant year → **Correct**
- [VERDICT] Same: both at least 6% after five years → **Incorrect** — says different

**Claims:**
- "Ontario: at least 4% of wages excluding vacation pay under five years; 6% at five years or more" → **Supported** | **Invalid** — 'section' is the Act name
- "Ontario: exceptions if the employee has a union, or if the employer contributes to a multi-employer vacation plan" → **Unsupported** | **Invalid** — s.39 requires both conditions together, and only affects ss.36–38
- "BC: at least 4% of total wages during the entitling year" → **Supported** | **Supports** — true rule, wrong tier for 6 years (scored in key facts)
- "Ontario and BC vacation pay percentages differ at six years" → **Unsupported** | **None** — comparison verdict; both are 6%

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S033 · Q10 · direct_extraction

**Question:** What is the statutory deadline for paying vacation pay to a BC employee before their annual vacation begins?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: Entitlement to vacation pay
  Who it applies to: All employees who have worked at least one full month and completed at least two weeks of service.
  Amount / threshold: The employer must pay the vacation pay within 28 days after the end of the employee's first day of work during the year that the employee has completed at least two weeks of service.
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 58): Vacation pay must be paid at least seven days before the beginning of the employee's annual vacation, unless it is paid on scheduled paydays under a written agreement or collective agreement.

**Key facts:**
- [BC] Payment at least 7 days before vacation → **Incorrect** — says within 28 days
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**

**Claims:**
- "Vacation pay is due within 28 days after the first day of work in the year" → **Unsupported** | **Invalid**
- "Applies to employees with at least one month and two weeks of service" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S034 · Q25 · dates_thresholds

**Question:** I started a new job in BC last week. How long do I have to work before I'm entitled to vacation pay?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 22(1)(a)
  Answer: entitlement
  Who it applies to: You are entitled to vacation pay if you have worked for the employer for at least 12 weeks.
  Amount / threshold: 12 weeks
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 58): An employee qualifies for at least 4% vacation pay after five calendar days of employment.

**Key facts:**
- [BC] 5 calendar days of employment → **Incorrect** — says 12 weeks
- [BC] Minimum 4% vacation pay → **Missing**
- [BC] Based on total wages during the relevant year → **Missing**

**Claims:**
- "Vacation pay after at least 12 weeks with the employer" → **Unsupported** | **Doesn't support** — s.22 is wage assignments

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S035 · Q13 · cross_jurisdiction_comparison

**Question:** We have staff in Toronto and Vancouver who'd rather bank their overtime and take time off later. Can we do that in both provinces, and do the rules differ?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: Overtime pay
  Who it applies to: Staff members
  Mandatory?: Yes

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Overtime Pay
  Answer: The ability to bank overtime hours and use them later
  Who it applies to: Staff working in both Toronto and Vancouver
  Mandatory?: mandatory

COMPARISON: UNCLEAR
  entitlement or requirement: different wording (check details)
  threshold: unknown
  eligibility: different wording (check details)
```

**Gold:**
- Ontario (s. 22): Yes, if the employer and employee agree. The employee receives 1.5 hours of paid time off for each overtime hour, taken within 3 months of the work week in which it was earned (or within 12 months with the employee's agreement). If employment ends before the time off is taken, overtime pay is owed.
- British Columbia (s. 42): Yes. At the employee's written request, the employer may set up a time bank and credit overtime wages to it at overtime rates. The employee can ask at any time to be paid out, to use the credit for paid time off at an agreed time, or to close the bank. The employer may close it with one month's written notice and must settle it within 6 months. The balance must be paid on termination or when the employee asks to close it.
- Comparison: Different: both allow banking overtime, but Ontario uses an agreement with a 3- or 12-month deadline to take the time off, while BC uses a time bank set up at the employee's written request, with no use-by deadline stated while it is open.

**Key facts:**
- [ON] Requires agreement between employer and employee → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Taken within 3 months, or within 12 months with the employee's agreement → **Missing**
- [ON] Paid out as overtime pay if employment ends first → **Missing**
- [BC] Set up at the employee's written request → **Missing**
- [BC] Overtime credited at overtime rates → **Missing**
- [BC] Employee may request payout, time off, or closing at any time → **Missing**
- [BC] Employer may close with 1 month's written notice and settle within 6 months → **Missing**
- [BC] Balance paid on termination or on the employee's request to close → **Missing**
- [VERDICT] Different: both allow banking overtime; Ontario by agreement with a 3- or 12-month deadline, BC by a time bank at the employee's written request → **Missing** — verdict 'unclear'

**Claims:**
- "BC allows banking overtime hours to use later" → **Supported** | **Invalid** — 'Overtime Pay' is not a section

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S036 · Q25 · dates_thresholds

**Question:** I started a new job in BC last week. How long do I have to work before I'm entitled to vacation pay?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 58
  Answer: vacation pay
  Who it applies to: after 5 calendar days of employment
  Amount / threshold: 4% of the employee's total wages during the year of employment
  Mandatory?: mandatory
  Exceptions: N; o; t;  ; s; p; e; c; i; f; i; e; d;  ; i; n;  ; t; h; e;  ; e; x; c; e; r; p; t
  Quote: "An employer must pay an employee the following amount of vacation pay: after 5 calendar days of employment, at least 4% of the employee's total wages during the year of employment entitling the employee to the vacation pay; after 5 consecutive years of employment, at least 6% of the employee's total wages during the year of employment entitling the employee to the vacation pay."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 58): An employee qualifies for at least 4% vacation pay after five calendar days of employment.

**Key facts:**
- [BC] 5 calendar days of employment → **Correct**
- [BC] Minimum 4% vacation pay → **Correct**
- [BC] Based on total wages during the relevant year → **Correct**

**Claims:**
- "After 5 calendar days of employment, at least 4% of total wages during the year" → **Supported** | **Supports**
- "6% after 5 consecutive years (quote)" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S037 · Q11 · cross_jurisdiction_comparison

**Question:** I've worked at my job in Ottawa for 6 years. Would someone who's worked 6 years at a job in Vancouver get the same amount of vacation as me?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 33
  Answer: at least three weeks of vacation after each vacation entitlement year that ends on or after December 31, 2017
  Who it applies to: at least five years or more with at least three weeks of vacation after each vacation entitlement year that ends on or after December 31, 2017
  Amount / threshold: five years or more
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 57
  Answer: at least 2 weeks
  Who it applies to: after 12 consecutive months of employment
  Amount / threshold: 2 weeks
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 33): With five or more years of employment, an Ontario employee is entitled to at least three weeks of vacation.
- British Columbia (s. 57): After five consecutive years of employment, a BC employee is entitled to at least three weeks of annual vacation.
- Comparison: Same: both at least 3 weeks after 5 years. Ontario ties it to completed vacation entitlement years; BC to consecutive years of employment.

**Key facts:**
- [ON] At least 3 weeks at 5 years or more → **Correct**
- [BC] At least 3 weeks after 5 consecutive years → **Incorrect** — gives 2 weeks for a 6-year employee
- [VERDICT] Same: both at least 3 weeks after 5 years → **Incorrect** — says different

**Claims:**
- "Ontario: at least three weeks after five years or more" → **Supported** | **Supports**
- "BC: at least 2 weeks after 12 consecutive months" → **Supported** | **Supports** — true rule, wrong tier for 6 years (scored in key facts)
- "Ontario and BC give different amounts of vacation at 6 years" → **Unsupported** | **None** — comparison verdict; both are 3 weeks

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S038 · Q10 · direct_extraction

**Question:** What is the statutory deadline for paying vacation pay to a BC employee before their annual vacation begins?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 58
  Answer: At least 4% of the employee's total wages during the first 5 calendar days of employment, or at least 6% during the next 5 consecutive years
  Who it applies to: After 5 calendar days of employment, or after 5 consecutive years of employment
  Amount / threshold: At least 4% of total wages for the first 5 calendar days, or at least 6% during the next 5 consecutive years
  Mandatory?: mandatory
  Exceptions: Vacation pay must be paid at least 7 days before the beginning of the annual vacation, or on the employee's scheduled payday(s)
  Quote: "at least 4% of the employee's total wages during the year of employment entitling the employee to the vacation pay"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 58): Vacation pay must be paid at least seven days before the beginning of the employee's annual vacation, unless it is paid on scheduled paydays under a written agreement or collective agreement.

**Key facts:**
- [BC] Payment at least 7 days before vacation → **Correct** — in the exceptions line
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Partial** — scheduled paydays mentioned without the written-agreement / collective-agreement condition

**Claims:**
- "4% of total wages during the first 5 calendar days, 6% during the next 5 consecutive years" → **Unsupported** | **Doesn't support** — garbles s.58(1)
- "Vacation pay is paid at least 7 days before the vacation or on scheduled paydays" → **Supported** | **Supports** — condition dropped (scored in key facts)
- "At least 4% of total wages during the year of employment (quote)" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S039 · Q18 · cross_jurisdiction_comparison

**Question:** Compare the vacation pay payment-timing requirements in Ontario and BC.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. payment timing
  Answer: requirement
  Who it applies to: all employees
  Amount / threshold: not specified
  Mandatory?: mandatory

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. payment timing
  Answer: requirement
  Who it applies to: all employees
  Amount / threshold: not specified
  Mandatory?: mandatory

COMPARISON: SAME
  entitlement or requirement: same
  threshold: same
  eligibility: same
```

**Gold:**
- Ontario (s. 36): Ontario requires vacation pay to be paid in a lump sum before the employee begins vacation by default. It may instead be paid each pay period if the employee agrees and the vacation pay is shown separately (other alternatives also exist, such as an agreed time).
- British Columbia (s. 58): BC requires vacation pay at least seven days before vacation begins, unless scheduled-payday payment is agreed to in writing or provided by a collective agreement.
- Comparison: Different: Ontario's default is a lump sum before vacation (with alternatives: payday, each pay period by agreement, or an agreed time); BC's default is at least 7 days before vacation, or on scheduled paydays if agreed in writing or by collective agreement.

**Key facts:**
- [ON] General rule is lump-sum payment before vacation → **Missing**
- [ON] Payment during each pay period requires an agreement and separate identification of vacation pay → **Missing**
- [BC] Payment at least 7 days before vacation → **Missing**
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**
- [VERDICT] Different: Ontario default lump sum before vacation; BC at least 7 days before, or scheduled paydays by written/collective agreement → **Incorrect** — says same

**Claims:**
- "Ontario and BC vacation pay timing rules are the same" → **Unsupported** | **None** — comparison verdict

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S040 · Q24 · dates_thresholds

**Question:** I started my job in Toronto on March 15, 2025. My manager says I have to use my vacation within 10 months of my vacation year ending. Can I save it and take it over the Christmas holidays this year (2026)?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 43(1)(a)
  Answer: The vacation must be taken within 10 months after the end of that year
  Who it applies to: Vacations must be taken during the same calendar year as the employee's birthday
  Amount / threshold: Within 10 months after the end of the vacation year
  Mandatory?: mandatory
  Quote: "the vacation must be taken during the same calendar year as the employee's birthday"
```

**Gold:**
- Ontario (s. 35, 1): Likely yes, timing-wise. Under the standard vacation entitlement year (which starts on the employee's first day of work), the first year ran March 15, 2025 to March 14, 2026. Vacation for that year must be completed within 10 months after it ends, so by about January 14, 2027, and December 2026 falls inside that window. However, the employer decides when vacation is taken, so the employee can request December but cannot insist. If the employer uses an alternative vacation entitlement year, the dates would be different.

**Key facts:**
- [ON] Deadline is 10 months after the end of the vacation entitlement year → **Correct**
- [ON] Standard vacation entitlement year starts on the employee's first day of employment → **Missing**
- [ON] First year ended March 14, 2026, so the deadline is about January 14, 2027 → **Missing**
- [ON] December 2026 is within the deadline → **Missing**
- [ON] The employer determines when vacation is taken → **Missing**
- [ON] Dates differ if the employer uses an alternative vacation entitlement year → **Missing**

**Claims:**
- "Vacation must be taken within 10 months after the end of the vacation year" → **Supported** | **Doesn't support** — s.35, cited s.43
- "Vacations must be taken in the same calendar year as the employee's birthday" → **Unsupported** | **Doesn't support** — invented quote

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S041 · Q30 · insufficient_evidence

**Question:** I'm a software developer in Vancouver. Do tech workers get overtime in BC?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The retrieved law does not state this; it may be set out in regulations, which this tool does not include.
```

**Gold:**
- British Columbia (s. 40): Cannot be determined from the Acts in the knowledge base. Section 40 sets the general overtime rules, but the BC Act's text does not address whether tech workers are excluded.
- Abstain (British Columbia): whether tech workers are excluded from overtime is not addressed in the BC Act; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Section 40 sets general overtime rules (1.5x over 8 hours a day or 40 a week; double over 12 hours a day) → **Missing**
- [BC] The BC Act does not mention technology workers; any occupation-specific exclusion would be in the regulations, which are not in the knowledge base → **Correct**

**Claims:**
- (no claims)

**Abstention:** **1**   **False abstention:** **no**

**Reviewed:** yes

---

## S042 · Q27 · insufficient_evidence

**Question:** I work on a farm in Ontario. My employer says farm workers don't get overtime. Is that true?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 22(8)
  Answer: overtime pay for the overtime hours that were worked in accordance with subsection 11 (5)
  Who it applies to: Employee's employment ends before the paid time off is taken under subsection (7)
  Amount / threshold: not specified
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Cannot be determined from the Acts in the knowledge base.
- Abstain (Ontario): s. 22 allows exemptions by regulation, but the regulations that list exempt occupations are not in the knowledge base.

**Key facts:**
- [ON] Explains that overtime exemptions are set by regulation, which is not in the knowledge base, so whether farm workers are exempt can't be determined → **Missing**

**Claims:**
- "If employment ends before banked time off is taken, overtime pay is owed" → **Supported** | **Supports** — s.22(8); doesn't address farm workers

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S043 · Q12 · cross_jurisdiction_comparison

**Question:** Compare the deadline for an employee to take earned vacation in Ontario and British Columbia.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment standards
  Answer: Entitlement to paid vacation
  Who it applies to: All employees
  Amount / threshold: 12 months continuous service
  Mandatory?: Yes

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employer's obligations
  Answer: Employees must be entitled to paid vacation leave.
  Who it applies to: All employees
  Amount / threshold: The amount of vacation leave that can be taken varies by employer.

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: same
```

**Gold:**
- Ontario (s. 35): Vacation must be completed no later than 10 months after the end of the vacation entitlement year for which it is given.
- British Columbia (s. 57): Annual vacation must be taken within 12 months after completing the year of employment that entitles the employee to it.
- Comparison: Different: 10 months in Ontario vs. 12 months in BC.

**Key facts:**
- [ON] No later than 10 months after the end of the vacation entitlement year → **Missing**
- [BC] Within 12 months after completing the entitling year of employment → **Missing**
- [VERDICT] Different: 10 months in Ontario vs. 12 months in BC → **Partial** — 'different' with no valid reason

**Claims:**
- "Ontario: entitlement to paid vacation after 12 months of continuous service" → **Supported** | **Invalid** — roughly the vacation entitlement year; not a section
- "BC: the amount of vacation leave varies by employer" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S044 · Q19 · exceptions

**Question:** Instead of getting my vacation pay all at once, can my employer in Ontario just add it to every paycheque?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 36(4)
  Answer: vacation pay payment method
  Who it applies to: employee
  Amount / threshold: agreement between employer and employee
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 36): Only if the employee has agreed to it and the vacation pay is shown separately, either on the wage statement for each pay period or on a separate statement given at the same time. Otherwise the default is a lump sum before the vacation starts.

**Key facts:**
- [ON] Requires an agreement between the employee and employer → **Correct**
- [ON] Vacation pay shown separately on the wage statement, or on a separate statement provided at the same time → **Missing**
- [ON] Default is a lump sum before vacation (s. 36(1)) → **Missing**

**Claims:**
- "The vacation pay payment method can be set by agreement between employer and employee" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S045 · Q25 · dates_thresholds

**Question:** I started a new job in BC last week. How long do I have to work before I'm entitled to vacation pay?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 58
  Answer: At least 4% of the employee's total wages during the year of employment, or 6% if employed for 5 consecutive years
  Who it applies to: After 5 calendar days of employment, or after 5 consecutive years of employment
  Amount / threshold: At least 4% of total wages, or 6% if employed for 5 consecutive years
  Mandatory?: mandatory
  Exceptions: Vacation pay must be paid at least 7 days before the start of the annual vacation, or on the employee's scheduled payday(s)
  Quote: "at least 4% of the employee's total wages during the year of employment entitling the employee to the vacation pay"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 58): An employee qualifies for at least 4% vacation pay after five calendar days of employment.

**Key facts:**
- [BC] 5 calendar days of employment → **Correct**
- [BC] Minimum 4% vacation pay → **Correct**
- [BC] Based on total wages during the relevant year → **Correct**

**Claims:**
- "After 5 calendar days, at least 4% of total wages; 6% after 5 consecutive years" → **Supported** | **Supports**
- "Vacation pay is paid at least 7 days before the vacation or on scheduled paydays" → **Supported** | **Supports** — condition omitted

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S046 · Q19 · exceptions

**Question:** Instead of getting my vacation pay all at once, can my employer in Ontario just add it to every paycheque?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)
  Answer: Employer must give vacation pay as a lump sum instead of adding it to each pay cheque
  Mandatory?: mandatory
  Quote: "The vacation pay shall be paid in one lump sum"
```

**Gold:**
- Ontario (s. 36): Only if the employee has agreed to it and the vacation pay is shown separately, either on the wage statement for each pay period or on a separate statement given at the same time. Otherwise the default is a lump sum before the vacation starts.

**Key facts:**
- [ON] Requires an agreement between the employee and employer → **Incorrect** — says it must always be a lump sum
- [ON] Vacation pay shown separately on the wage statement, or on a separate statement provided at the same time → **Missing**
- [ON] Default is a lump sum before vacation (s. 36(1)) → **Partial** — lump sum stated as absolute, not as the default before vacation

**Claims:**
- "The employer must pay vacation pay as a lump sum, not added to each paycheque" → **Unsupported** | **Doesn't support** — invented quote; s.36(3) allows each-pay-period payment by agreement

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S047 · Q16 · cross_jurisdiction_comparison

**Question:** Compare the daily overtime rules in Ontario and BC for employees who work more than eight hours in a day.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Daily overtime rules
  Who it applies to: Employees who work more than eight hours in a day
  Amount / threshold: 44 hours per week
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 35
  Answer: overtime wages
  Who it applies to: employees who work more than eight hours in a day
  Amount / threshold: more than 8 hours a day or 40 hours a week
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: same
```

**Gold:**
- Ontario (s. 22): Ontario's overtime section (s. 22) sets overtime on a weekly basis only: hours over 44 in a work week (or a prescribed threshold). It does not provide for daily overtime.
- British Columbia (s. 40): BC requires 1.5 times regular wages for hours over eight in a day and double wages for hours over 12, unless an averaging agreement applies.
- Comparison: Different: BC has daily overtime (1.5x over 8 hours, double over 12); Ontario has none, only a weekly threshold.

**Key facts:**
- [ON] No daily overtime threshold in s. 22 → **Incorrect** — presents 'daily overtime rules' for Ontario
- [BC] Daily overtime after 8 hours → **Correct**
- [BC] Double time after 12 hours → **Missing**
- [BC] Averaging agreement may affect the calculation → **Missing**
- [VERDICT] Different: BC has daily overtime (1.5x over 8, double over 12); Ontario has none, only weekly → **Partial** — 'different' for the wrong reason

**Claims:**
- "Ontario has daily overtime rules for employees who work more than eight hours" → **Unsupported** | **Invalid**
- "BC: overtime for more than 8 hours a day or 40 a week" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S048 · Q15 · cross_jurisdiction_comparison

**Question:** If someone works 45 hours in a week, would they get overtime in Toronto and Vancouver, or does it depend on where they work?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 22(9)
  Answer: overtime pay
  Who it applies to: If an employee performs work of a particular kind or character and is exempted from the application of this section by the regulations or prescribes an overtime threshold of other than 44 hours for an employee who performs such work.
  Amount / threshold: 44 hours
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act (British Columbia)
  Answer: Entitled to overtime wages at 1.5 times the regular wage for hours over 40.
  Who it applies to: An employee who works more than 40 hours a week without an averaging agreement under section 37.
  Amount / threshold: 40 hours a week
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act (British Columbia) was not among the retrieved sections.

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 22): Ontario's general weekly overtime threshold is 44 hours, so hours beyond 44 qualify for overtime at a minimum of 1.5 times the regular rate.
- British Columbia (s. 40): BC's weekly overtime threshold is 40 hours, with hours beyond 40 paid at 1.5 times the regular wage. Daily overtime also applies to any day over 8 hours.
- Comparison: Different: Ontario pays overtime only for the hour over 44. In BC overtime is owed, but whether it comes from the weekly rule (over 40) or the daily rule (over 8 a day) depends on how the hours fall across the days.

**Key facts:**
- [ON] 44-hour weekly threshold → **Correct**
- [ON] At least 1.5 times the regular rate → **Missing**
- [BC] 40-hour weekly threshold → **Correct**
- [BC] 1.5 times the regular wage → **Correct**
- [BC] Daily overtime may also apply for any day over 8 hours → **Missing**
- [VERDICT] Different: Ontario pays overtime only for the hour over 44; in BC overtime is owed (weekly over 40 or daily over 8) → **Correct** — 44 vs. 40

**Claims:**
- "Ontario: overtime threshold 44 hours" → **Supported** | **Supports**
- "Ontario: Applies to employees whose work is exempted by regulation or has a different threshold" → **Unsupported** | **Doesn't support** — garbles s.22(2)
- "BC: 1.5 times the regular wage for hours over 40 a week without an averaging agreement" → **Supported** | **Invalid** — 'section' is the Act name

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S049 · Q16 · cross_jurisdiction_comparison

**Question:** Compare the daily overtime rules in Ontario and BC for employees who work more than eight hours in a day.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 17(1)
  Answer: Employer must pay overtime pay of at least one and one-half times the regular rate for each hour worked over 44 hours in a work week
  Who it applies to: No employer shall require or permit an employee to work more than eight hours in a day or, if the employer establishes a regular work day of more than eight hours for the employee, the number of hours in their regular work day
  Amount / threshold: At least 44 hours per work week
  Mandatory?: mandatory
  Exceptions: If the employee is exempted by regulation or has an overtime threshold other than 44 hours
  Quote: "Subject to subsections (2) and (3), no employer shall require or permit an employee to work more than"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 35
  Answer: Overtime wages must be paid at 1.5 times the regular wage for hours over 8, and double the regular wage for hours over 12
  Who it applies to: Employer requires or indirectly allows the employee to work more than 8 hours a day or 40 hours a week
  Amount / threshold: More than 8 hours a day or 40 hours a week
  Mandatory?: mandatory
  Exceptions: Does not apply for an employee working under an averaging agreement
  Quote: "An employer must pay an employee overtime wages in accordance with section 40"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 22): Ontario's overtime section (s. 22) sets overtime on a weekly basis only: hours over 44 in a work week (or a prescribed threshold). It does not provide for daily overtime.
- British Columbia (s. 40): BC requires 1.5 times regular wages for hours over eight in a day and double wages for hours over 12, unless an averaging agreement applies.
- Comparison: Different: BC has daily overtime (1.5x over 8 hours, double over 12); Ontario has none, only a weekly threshold.

**Key facts:**
- [ON] No daily overtime threshold in s. 22 → **Partial** — gives only the weekly 44-hour rule, but doesn't say there is no daily overtime
- [BC] Daily overtime after 8 hours → **Correct**
- [BC] Double time after 12 hours → **Correct**
- [BC] Averaging agreement may affect the calculation → **Correct**
- [VERDICT] Different: BC has daily overtime (1.5x over 8, double over 12); Ontario has none, only weekly → **Correct** — BC daily vs. Ontario weekly shown

**Claims:**
- "Ontario: at least 1.5 times the regular rate for hours over 44 a week" → **Supported** | **Doesn't support** — s.22, cited s.17(1)
- "Ontario: no employer may require more than eight hours of work a day (or the regular work day)" → **Supported** | **Supports** — s.17 hours limit, not overtime
- "BC: overtime for more than 8 hours a day or 40 a week" → **Supported** | **Supports**
- "BC: 1.5 times over 8 hours, double over 12" → **Supported** | **Doesn't support** — s.40, cited s.35
- "BC: doesn't apply under an averaging agreement" → **Supported** | **Doesn't support** — s.37

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S050 · Q05 · direct_extraction

**Question:** I work in Toronto and sometimes end up doing 48 hours a week. When should I start getting extra pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 11(5)
  Answer: Wages
  Who it applies to: Employee's employment ends
  Amount / threshold: 7 days after the employment ends
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Overtime pay is required for hours worked beyond 44 in a work week (unless a different threshold is prescribed by regulation), at a minimum of 1.5 times the employee's regular rate.

**Key facts:**
- [ON] Weekly overtime threshold is 44 hours → **Missing** — answers final pay timing
- [ON] Overtime rate is at least 1.5 times the regular rate → **Missing**

**Claims:**
- "Wages are due within 7 days after employment ends" → **Supported** | **Supports** — s.11(5); irrelevant to the question

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S051 · Q04 · direct_extraction

**Question:** What is the minimum vacation pay percentage for an Ontario employee with at least five years of employment?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario)
  Not specified in the retrieved sections. The retrieved law does not state this; it may be set out in regulations, which this tool does not include.
```

**Gold:**
- Ontario (s. 35.2): The employee must receive vacation pay equal to at least 6% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 6% vacation pay → **Missing**
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S052 · Q11 · cross_jurisdiction_comparison

**Question:** I've worked at my job in Ottawa for 6 years. Would someone who's worked 6 years at a job in Vancouver get the same amount of vacation as me?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 20.1(1)(a)
  Answer: Vacation pay
  Who it applies to: Employee
  Amount / threshold: 6 years
  Mandatory?: mandatory

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 110(1)(a)
  Answer: entitlement
  Who it applies to: 6 years of continuous employment
  Amount / threshold: 6 years
  Mandatory?: mandatory
  Quote: "The Employment Standards Act, 2000, Section 110(1)(a) states that an employee is entitled to a minimum of 10 days of vacation pay for every 100 hours worked."

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: same
  eligibility: different
```

**Gold:**
- Ontario (s. 33): With five or more years of employment, an Ontario employee is entitled to at least three weeks of vacation.
- British Columbia (s. 57): After five consecutive years of employment, a BC employee is entitled to at least three weeks of annual vacation.
- Comparison: Same: both at least 3 weeks after 5 years. Ontario ties it to completed vacation entitlement years; BC to consecutive years of employment.

**Key facts:**
- [ON] At least 3 weeks at 5 years or more → **Missing**
- [BC] At least 3 weeks after 5 consecutive years → **Missing**
- [VERDICT] Same: both at least 3 weeks after 5 years → **Incorrect** — says different

**Claims:**
- "BC: an employee is entitled to 10 days of vacation pay for every 100 hours worked" → **Unsupported** | **Doesn't support** — invented quote
- "Ontario and BC give different amounts of vacation at 6 years" → **Unsupported** | **None** — comparison verdict; both are 3 weeks

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S053 · Q14 · cross_jurisdiction_comparison

**Question:** We've got employees in Toronto and Vancouver who've both been here for six years. Do they get the same vacation pay percentage?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 35.2
  Answer: Paid
  Who it applies to: Employee
  Amount / threshold: 4% or 6%
  Mandatory?: mandatory
  Quote: "An employer shall pay vacation pay to an employee who is entitled to vacation under section 33 or 34, equal to at least, (a) 4 per cent of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given, if the employee’s period of employment is less than five years; or (b) 6 per cent of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given, if the employee’s period of employment is five years or more."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 58
  Answer: at least 6% of the employee's total wages during the year of employment entitling the employee to the vacation pay
  Who it applies to: after 5 years of employment
  Amount / threshold: 5 years
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 35.2): At least 6% of wages, excluding vacation pay, for employees with five or more years of employment.
- British Columbia (s. 58): At least 6% of total wages during the relevant year after five consecutive years of employment.
- Comparison: Same: both at least 6% after five years. The wage base is worded differently (Ontario: wages excluding vacation pay earned in the period; BC: total wages in the entitling year).

**Key facts:**
- [ON] Minimum 6% → **Correct** — '4% or 6%'; quote ties 6% to 5+ years
- [ON] Excludes vacation pay from wages → **Correct**
- [BC] Minimum 6% → **Correct**
- [BC] Based on total wages during the relevant year → **Correct**
- [VERDICT] Same: both at least 6% after five years → **Incorrect** — says different

**Claims:**
- "Ontario: 4% under five years, 6% at five years or more, of wages excluding vacation pay" → **Supported** | **Supports**
- "BC: at least 6% of total wages during the entitling year after 5 years" → **Supported** | **Supports**
- "Ontario and BC vacation pay percentages differ at six years" → **Unsupported** | **None** — comparison verdict; both are 6%

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S054 · Q06 · direct_extraction

**Question:** I just finished my first year working in BC. Am I supposed to get two weeks off now?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 22(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 1 year
  Mandatory?: mandatory
  Quote: "Section 22(1)(a) of the Employment Standards Act (British Columbia) states that an employee is entitled to two weeks of vacation pay for each year of service."
```

**Gold:**
- British Columbia (s. 57): Yes. After 12 consecutive months of employment, an employee is entitled to at least two weeks of annual vacation.

**Key facts:**
- [BC] At least 2 weeks of annual vacation → **Partial** — 'two weeks of vacation pay' instead of two weeks of vacation

**Claims:**
- "An employee is entitled to two weeks of vacation pay for each year of service" → **Unsupported** | **Doesn't support** — invented quote; s.22 is wage assignments

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S055 · Q13 · cross_jurisdiction_comparison

**Question:** We have staff in Toronto and Vancouver who'd rather bank their overtime and take time off later. Can we do that in both provinces, and do the rules differ?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 22(8)
  Answer: Overtime pay for overtime hours worked
  Who it applies to: Staff in Toronto and Vancouver
  Amount / threshold: Subsection (8) specifies that overtime pay applies when the employment ends before the paid time off is taken.
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 42(1)-(3.2)
  Answer: Allowing employees to bank overtime and take time off later
  Who it applies to: At the written request of an employee
  Amount / threshold: Written request
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: different wording (check details)
```

**Gold:**
- Ontario (s. 22): Yes, if the employer and employee agree. The employee receives 1.5 hours of paid time off for each overtime hour, taken within 3 months of the work week in which it was earned (or within 12 months with the employee's agreement). If employment ends before the time off is taken, overtime pay is owed.
- British Columbia (s. 42): Yes. At the employee's written request, the employer may set up a time bank and credit overtime wages to it at overtime rates. The employee can ask at any time to be paid out, to use the credit for paid time off at an agreed time, or to close the bank. The employer may close it with one month's written notice and must settle it within 6 months. The balance must be paid on termination or when the employee asks to close it.
- Comparison: Different: both allow banking overtime, but Ontario uses an agreement with a 3- or 12-month deadline to take the time off, while BC uses a time bank set up at the employee's written request, with no use-by deadline stated while it is open.

**Key facts:**
- [ON] Requires agreement between employer and employee → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Taken within 3 months, or within 12 months with the employee's agreement → **Missing**
- [ON] Paid out as overtime pay if employment ends first → **Correct**
- [BC] Set up at the employee's written request → **Correct**
- [BC] Overtime credited at overtime rates → **Missing**
- [BC] Employee may request payout, time off, or closing at any time → **Missing**
- [BC] Employer may close with 1 month's written notice and settle within 6 months → **Missing**
- [BC] Balance paid on termination or on the employee's request to close → **Missing**
- [VERDICT] Different: both allow banking overtime; Ontario by agreement with a 3- or 12-month deadline, BC by a time bank at the employee's written request → **Partial** — no valid reason given

**Claims:**
- "Ontario: overtime pay is owed if employment ends before the paid time off is taken" → **Supported** | **Supports**
- "BC: overtime can be banked at the employee's written request" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S056 · Q06 · direct_extraction

**Question:** I just finished my first year working in BC. Am I supposed to get two weeks off now?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 49.01(2)
  Answer: Entitled to up to 27 weeks of unpaid leave in any period of 52 weeks.
  Who it applies to: An employee who has been employed for a certain number of consecutive days and is unable to work for at least one week due to serious personal illness or injury.
  Amount / threshold: After the prescribed number of consecutive days of employment with an employer.
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 57): Yes. After 12 consecutive months of employment, an employee is entitled to at least two weeks of annual vacation.

**Key facts:**
- [BC] At least 2 weeks of annual vacation → **Missing** — answers illness leave

**Claims:**
- "Up to 27 weeks of unpaid leave in any 52 weeks for serious illness or injury" → **Supported** | **Supports** — s.49.01(2); irrelevant

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S057 · Q28 · insufficient_evidence

**Question:** Are employees in managerial positions exempt from the daily and weekly overtime requirements in British Columbia?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Overtime pay
  Answer: Daily and weekly overtime requirements
  Who it applies to: Managers
```

**Gold:**
- British Columbia (s. 37, 40): Cannot be determined from the Acts in the knowledge base.
- Abstain (British Columbia): the BC Act does not address a manager exclusion; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Sections 37 and 40 set out averaging agreements and general overtime rules → **Missing**
- [BC] The BC Act does not establish a managerial exemption; occupation-specific exclusions are in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- "Managers are subject to the daily and weekly overtime requirements" → **Unsupported** | **Invalid** — definitive answer on an abstain question

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S058 · Q18 · cross_jurisdiction_comparison

**Question:** Compare the vacation pay payment-timing requirements in Ontario and BC.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)(a), 14(3)(b)
  Answer: Vacation pay must be paid within 28 days after the end of the vacation period
  Who it applies to: Employer must have at least one employee who has worked at least 56 hours during the preceding week
  Amount / threshold: At least 56 hours worked in the preceding week
  Mandatory?: mandatory
  Quote: "The employer must pay the vacation pay within 28 days after the end of the vacation period"

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 36): Ontario requires vacation pay to be paid in a lump sum before the employee begins vacation by default. It may instead be paid each pay period if the employee agrees and the vacation pay is shown separately (other alternatives also exist, such as an agreed time).
- British Columbia (s. 58): BC requires vacation pay at least seven days before vacation begins, unless scheduled-payday payment is agreed to in writing or provided by a collective agreement.
- Comparison: Different: Ontario's default is a lump sum before vacation (with alternatives: payday, each pay period by agreement, or an agreed time); BC's default is at least 7 days before vacation, or on scheduled paydays if agreed in writing or by collective agreement.

**Key facts:**
- [ON] General rule is lump-sum payment before vacation → **Incorrect** — says within 28 days after the vacation
- [ON] Payment during each pay period requires an agreement and separate identification of vacation pay → **Missing**
- [BC] Payment at least 7 days before vacation → **Missing**
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**
- [VERDICT] Different: Ontario default lump sum before vacation; BC at least 7 days before, or scheduled paydays by written/collective agreement → **Missing** — verdict unknown

**Claims:**
- "Ontario: vacation pay is due within 28 days after the end of the vacation" → **Unsupported** | **Doesn't support** — invented quote
- "Ontario: applies if an employee worked at least 56 hours the preceding week" → **Unsupported** | **Doesn't support**

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S059 · Q02 · direct_extraction

**Question:** I've been at my job in Vancouver for six years now. Do I get any more vacation time than when I started?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 57
  Answer: Entitlement
  Who it applies to: Yes
  Amount / threshold: 5 consecutive years of employment
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 57): Yes. After five consecutive years of employment, the entitlement increases from at least two weeks to at least three weeks of annual vacation.

**Key facts:**
- [BC] At least 3 weeks of annual vacation → **Missing**
- [BC] Up from at least 2 weeks before reaching 5 years → **Missing**
- [BC] 5 consecutive years of employment → **Correct** — 'Yes … 5 consecutive years of employment'

**Claims:**
- "Yes, the entitlement changes after 5 consecutive years of employment" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S060 · Q23 · exceptions

**Question:** I work in Ontario and would rather take time off than get overtime pay. Can my employer let me do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 22(7)
  Answer: Compensation for overtime hours
  Who it applies to: Employee
  Amount / threshold: One and one-half hours of paid time off work for each hour of overtime worked
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Yes. The employer and employee may agree to paid time off at one and a half hours for each overtime hour worked. The time off must generally be taken within three months, or within 12 months if the employee agrees.

**Key facts:**
- [ON] Employer and employee must agree → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Correct**
- [ON] Normally taken within 3 months → **Missing**
- [ON] May be taken within 12 months with employee agreement → **Missing**

**Claims:**
- "One and a half hours of paid time off for each hour of overtime" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S061 · Q20 · exceptions

**Question:** How must an employer calculate vacation entitlement for an Ontario employee during a stub period created by an alternative vacation entitlement year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 15.1(3)
  Answer: Vacation entitlement calculation
  Who it applies to: Employee
  Amount / threshold: Alternative vacation entitlement year
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 34): The employer must calculate the ratio of the stub period to 12 months and apply it to the employee's applicable two-week or three-week vacation entitlement, using a separate calculation for employees without a regular work week.

**Key facts:**
- [ON] Calculate stub-period-to-12-month ratio → **Missing**
- [ON] Less than 5 years: use 2 weeks as the base → **Missing**
- [ON] 5 years or more: use 3 weeks as the base → **Missing**
- [ON] Employees without a regular work week use average weekly working days → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S062 · Q25 · dates_thresholds

**Question:** I started a new job in BC last week. How long do I have to work before I'm entitled to vacation pay?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 58): An employee qualifies for at least 4% vacation pay after five calendar days of employment.

**Key facts:**
- [BC] 5 calendar days of employment → **Missing**
- [BC] Minimum 4% vacation pay → **Missing**
- [BC] Based on total wages during the relevant year → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S063 · Q08 · direct_extraction

**Question:** I'm working a 10-hour shift in BC today. Should the last couple of hours be paid at a higher rate?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 37(4)
  Answer: Double the employee's regular wage for the time over 12 hours
  Who it applies to: Employer requires or allows an employee to work more than 12 hours a day, at any time during the period specified in the agreement
  Amount / threshold: More than 12 hours a day
  Mandatory?: mandatory
  Quote: "must pay the employee double the employee's regular wage for the time over 12 hours"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): If the employee is not working under an averaging agreement, hours beyond eight in a day must be paid at 1.5 times the regular wage.

**Key facts:**
- [BC] Hours over 8 a day are paid at 1.5 times the regular wage → **Missing** — answers the averaging-agreement 12-hour rule
- [BC] No averaging agreement applies → **Missing**

**Claims:**
- "Under an averaging agreement, double the regular wage for time over 12 hours a day" → **Supported** | **Supports** — s.37(4)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S064 · Q27 · insufficient_evidence

**Question:** I work on a farm in Ontario. My employer says farm workers don't get overtime. Is that true?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 31
  Answer: Hours worked on a public holiday are not considered when calculating overtime pay
  Who it applies to: Employee receives premium pay for working on a public holiday
  Mandatory?: optional
  Exceptions: The exemption applies only if the employee is exempted by regulation or has an overtime threshold of more than 44 hours
  Quote: "the hours worked shall not be taken into consideration in calculating overtime pay to which the employee may be entitled"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Cannot be determined from the Acts in the knowledge base.
- Abstain (Ontario): s. 22 allows exemptions by regulation, but the regulations that list exempt occupations are not in the knowledge base.

**Key facts:**
- [ON] Explains that overtime exemptions are set by regulation, which is not in the knowledge base, so whether farm workers are exempt can't be determined → **Missing** — mentions regulation exemptions only as a condition of s.31, never concludes

**Claims:**
- "Hours worked on a public holiday with premium pay don't count toward overtime" → **Supported** | **Supports**
- "This applies only to employees exempted by regulation or with a threshold over 44 hours" → **Unsupported** | **Doesn't support** — garbled

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S065 · Q07 · direct_extraction

**Question:** My boss in BC says my vacation pay will be lower this year because I got a bonus. Is that allowed?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 22(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: No threshold specified
  Mandatory?: mandatory
  Quote: "The Employment Standards Act (British Columbia) does not specify a minimum amount of vacation pay that must be paid to employees who receive a bonus."
```

**Gold:**
- British Columbia (s. 59): No. A BC employer must not reduce an employee's annual vacation or vacation pay because the employee was paid a bonus.

**Key facts:**
- [BC] Cannot reduce vacation or vacation pay because of a bonus → **Missing**

**Claims:**
- "The Act does not specify a minimum vacation pay for employees who receive a bonus" → **Unsupported** | **Doesn't support** — invented quote; s.22 is wage assignments

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S066 · Q16 · cross_jurisdiction_comparison

**Question:** Compare the daily overtime rules in Ontario and BC for employees who work more than eight hours in a day.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3), 14(5)
  Answer: Overtime pay at least one and a half times the regular rate of pay
  Who it applies to: Worked more than eight hours in a day
  Amount / threshold: At least one and a half times the regular rate of pay
  Mandatory?: mandatory
  Quote: "The employer must compensate each employee for all overtime worked"

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 22): Ontario's overtime section (s. 22) sets overtime on a weekly basis only: hours over 44 in a work week (or a prescribed threshold). It does not provide for daily overtime.
- British Columbia (s. 40): BC requires 1.5 times regular wages for hours over eight in a day and double wages for hours over 12, unless an averaging agreement applies.
- Comparison: Different: BC has daily overtime (1.5x over 8 hours, double over 12); Ontario has none, only a weekly threshold.

**Key facts:**
- [ON] No daily overtime threshold in s. 22 → **Incorrect** — says overtime after 8 hours a day
- [BC] Daily overtime after 8 hours → **Missing**
- [BC] Double time after 12 hours → **Missing**
- [BC] Averaging agreement may affect the calculation → **Missing**
- [VERDICT] Different: BC has daily overtime (1.5x over 8, double over 12); Ontario has none, only weekly → **Missing** — verdict unknown

**Claims:**
- "Ontario: 1.5 times the regular rate for working more than eight hours in a day" → **Unsupported** | **Doesn't support**
- "The employer must compensate each employee for all overtime worked" → **Unsupported** | **Doesn't support** — invented quote; s.14 is wage priority

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S067 · Q17 · cross_jurisdiction_comparison

**Question:** I want to split my vacation into single days instead of whole weeks. Can I do that in Ontario? What about in BC?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Entitlement to vacation days
  Who it applies to: Any employee
  Amount / threshold: Two or more days for vacation entitlement
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act (BC)
  Answer: Entitlement to annual vacation
  Who it applies to: Any employee
  Amount / threshold: At least 2 weeks after 12 consecutive months of employment or at least 3 weeks after 5 consecutive years of employment
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act (BC) was not among the retrieved sections.

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: same
```

**Gold:**
- Ontario (s. 35): By default, Ontario vacation is taken in whole weeks (a two-week period or two one-week periods; for 5+ years, combinations of one-, two-, or three-week periods). Shorter periods are allowed only if the employee requests them in writing and the employer agrees.
- British Columbia (s. 57): BC requires the employer to allow an employee to take annual vacation in periods of one or more weeks. Section 57 does not address periods shorter than a week.
- Comparison: Similar: both are built around whole weeks. Ontario allows shorter periods by written request plus employer agreement; BC requires the employer to allow periods of one week or more.

**Key facts:**
- [ON] Default is whole-week periods → **Missing**
- [ON] Shorter periods only if the employee requests in writing and the employer agrees → **Missing**
- [BC] Employer must allow vacation in periods of one or more weeks → **Missing**
- [BC] Periods shorter than a week are not addressed in s. 57 → **Missing**
- [VERDICT] Similar: both built around whole weeks; Ontario allows shorter periods by written request plus employer agreement → **Incorrect** — says different, no valid reason

**Claims:**
- "Ontario: vacation entitlement of two or more days" → **Unsupported** | **Invalid** — not a rule in the Act
- "BC: at least 2 weeks after 12 months, 3 weeks after 5 years" → **Supported** | **Invalid** — 'section' is the Act name

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S068 · Q30 · insufficient_evidence

**Question:** I'm a software developer in Vancouver. Do tech workers get overtime in BC?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 35
  Answer: Overtime wages must be paid according to section 40
  Who it applies to: Employer requires or allows the employee to work more than 8 hours per day or 40 hours per week
  Amount / threshold: More than 8 hours a day or 40 hours a week
  Mandatory?: mandatory
  Exceptions: Does not apply for employees working under an averaging agreement under section 37
  Quote: "*overtime wages* means the wages an employee is entitled to receive under section 37 (4), (5) or (6) or 40"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): Cannot be determined from the Acts in the knowledge base. Section 40 sets the general overtime rules, but the BC Act's text does not address whether tech workers are excluded.
- Abstain (British Columbia): whether tech workers are excluded from overtime is not addressed in the BC Act; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Section 40 sets general overtime rules (1.5x over 8 hours a day or 40 a week; double over 12 hours a day) → **Partial** — 8/40 thresholds without the rates
- [BC] The BC Act does not mention technology workers; any occupation-specific exclusion would be in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- "Overtime is owed under s.40 for over 8 hours a day or 40 a week" → **Supported** | **Supports**
- "Doesn't apply under an averaging agreement" → **Supported** | **Doesn't support** — s.37
- "Overtime wages means wages under s.37(4)–(6) or s.40" → **Supported** | **Doesn't support** — s.1 definition

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S069 · Q11 · cross_jurisdiction_comparison

**Question:** I've worked at my job in Ottawa for 6 years. Would someone who's worked 6 years at a job in Vancouver get the same amount of vacation as me?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 33(1)
  Answer: At least two weeks after each vacation entitlement year completed, and at least three weeks after each vacation entitlement year completed if the employee's period of employment is five years or more
  Who it applies to: Employee's period of employment is less than five years or five years or more
  Amount / threshold: Less than five years: at least two weeks; Five years or more: at least three weeks
  Mandatory?: mandatory
  Quote: "(a) at least two weeks after each vacation entitlement year that the employee completes"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 57
  Answer: Annual vacation of at least 2 weeks after 12 consecutive months, or at least 3 weeks after 5 consecutive years
  Who it applies to: At least 12 consecutive months of employment, or at least 5 consecutive years of employment
  Amount / threshold: At least 2 weeks after 12 consecutive months, or at least 3 weeks after 5 consecutive years
  Mandatory?: mandatory
  Quote: "after 12 consecutive months of employment"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 33): With five or more years of employment, an Ontario employee is entitled to at least three weeks of vacation.
- British Columbia (s. 57): After five consecutive years of employment, a BC employee is entitled to at least three weeks of annual vacation.
- Comparison: Same: both at least 3 weeks after 5 years. Ontario ties it to completed vacation entitlement years; BC to consecutive years of employment.

**Key facts:**
- [ON] At least 3 weeks at 5 years or more → **Correct**
- [BC] At least 3 weeks after 5 consecutive years → **Correct**
- [VERDICT] Same: both at least 3 weeks after 5 years → **Incorrect** — code compared whole fields and said different although both give 3 weeks at 6 years

**Claims:**
- "Ontario: at least two weeks under five years" → **Supported** | **Supports**
- "Ontario: at least three weeks at five years or more" → **Supported** | **Supports**
- "BC: at least 2 weeks after 12 consecutive months" → **Supported** | **Supports**
- "BC: at least 3 weeks after 5 consecutive years" → **Supported** | **Supports**
- "Ontario and BC give different amounts of vacation at 6 years" → **Unsupported** | **None** — comparison verdict; both are 3 weeks

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S070 · Q29 · insufficient_evidence

**Question:** My sister works in Calgary and I work in Toronto. We've both been at our jobs for 2 years. Do we get the same vacation pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)(a)
  Answer: Vacation pay must be paid to employees who have worked continuously for at least two consecutive years
  Amount / threshold: At least two consecutive years of continuous employment
  Mandatory?: mandatory
  Quote: "Vacation pay must be paid to employees who have worked continuously for at least two consecutive years"

ALBERTA: not covered. This tool only includes the Ontario and British Columbia Employment Standards Acts, so it cannot answer for this province.
```

**Gold:**
- Ontario (s. 35.2): An Ontario employee with less than five years of employment is entitled to vacation pay of at least 4% of wages, excluding vacation pay, earned during the relevant period.
- Abstain (Alberta): Alberta legislation is not in the knowledge base. The system should answer for Ontario and say it cannot speak to Alberta.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing**

**Claims:**
- "Ontario: vacation pay is owed only after two consecutive years of continuous work" → **Unsupported** | **Doesn't support** — invented quote

**Abstention:** **1**   **False abstention:** **no**

**Reviewed:** yes

---

## S071 · Q26 · dates_thresholds

**Question:** What are the daily and weekly overtime thresholds in BC for an employee who is not working under an averaging agreement?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 40
  Answer: 1 1/2 times the employee's regular wage for the time over 8 hours
  Who it applies to: Employee who works over 8 hours a day, and is not working under an averaging agreement under section 37
  Amount / threshold: 8 hours
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): Daily overtime begins after eight hours, with double time after 12 hours. Weekly overtime begins after 40 hours, with only the first eight hours worked each day counted toward the weekly calculation.

**Key facts:**
- [BC] Daily threshold: 8 hours → **Correct**
- [BC] Double-time threshold: 12 hours → **Missing**
- [BC] Weekly threshold: 40 hours → **Missing**
- [BC] Only first 8 hours per day count toward weekly overtime → **Missing**

**Claims:**
- "1.5 times the regular wage over 8 hours a day without an averaging agreement" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S072 · Q05 · direct_extraction

**Question:** I work in Toronto and sometimes end up doing 48 hours a week. When should I start getting extra pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Hours of Work
  Answer: Extra pay for overtime
  Who it applies to: All employees
  Amount / threshold: 48 hours per week
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 22): Overtime pay is required for hours worked beyond 44 in a work week (unless a different threshold is prescribed by regulation), at a minimum of 1.5 times the employee's regular rate.

**Key facts:**
- [ON] Weekly overtime threshold is 44 hours → **Incorrect** — says 48 hours
- [ON] Overtime rate is at least 1.5 times the regular rate → **Missing**

**Claims:**
- "Overtime pay starts at 48 hours per week" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S073 · Q02 · direct_extraction

**Question:** I've been at my job in Vancouver for six years now. Do I get any more vacation time than when I started?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment standards
  Answer: Vacation pay increases as service length increases
  Who it applies to: All employees
  Amount / threshold: 6 years
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 57): Yes. After five consecutive years of employment, the entitlement increases from at least two weeks to at least three weeks of annual vacation.

**Key facts:**
- [BC] At least 3 weeks of annual vacation → **Missing** — talks about vacation pay, not time
- [BC] Up from at least 2 weeks before reaching 5 years → **Missing**
- [BC] 5 consecutive years of employment → **Missing**

**Claims:**
- "Vacation pay increases as length of service increases" → **Supported** | **Invalid** — broadly true (s.58: 4% → 6%); 'Employment standards' is not a section

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S074 · Q05 · direct_extraction

**Question:** I work in Toronto and sometimes end up doing 48 hours a week. When should I start getting extra pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 18
  Answer: Minimum rest periods
  Who it applies to: All employees
  Amount / threshold: At least 11 consecutive hours free from work
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Overtime pay is required for hours worked beyond 44 in a work week (unless a different threshold is prescribed by regulation), at a minimum of 1.5 times the employee's regular rate.

**Key facts:**
- [ON] Weekly overtime threshold is 44 hours → **Missing** — answers rest periods
- [ON] Overtime rate is at least 1.5 times the regular rate → **Missing**

**Claims:**
- "Employees must get at least 11 consecutive hours free from work" → **Supported** | **Supports** — s.18(1); irrelevant

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S075 · Q08 · direct_extraction

**Question:** I'm working a 10-hour shift in BC today. Should the last couple of hours be paid at a higher rate?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 37(5)
  Answer: must pay the employee 1 1/2 times the employee's regular wage for the time over 40 hours
  Who it applies to: An employer under this section who requires, or directly or indirectly allows, an employee to work more than an average of 40 hours a week within the period specified in the agreement
  Amount / threshold: an average of 40 hours a week
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): If the employee is not working under an averaging agreement, hours beyond eight in a day must be paid at 1.5 times the regular wage.

**Key facts:**
- [BC] Hours over 8 a day are paid at 1.5 times the regular wage → **Missing** — answers the averaging-agreement weekly rule
- [BC] No averaging agreement applies → **Missing**

**Claims:**
- "Under an averaging agreement, 1.5 times the regular wage for time over an average of 40 hours a week" → **Supported** | **Supports** — s.37(5)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S076 · Q12 · cross_jurisdiction_comparison

**Question:** Compare the deadline for an employee to take earned vacation in Ontario and British Columbia.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 28(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 12 weeks
  Mandatory?: mandatory
  Quote: "The Employment Standards Act, 2000 (Ontario) requires employers to provide employees with a minimum of 12 weeks of earned vacation time per year."

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 150(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 12 months
  Mandatory?: mandatory
  Quote: "The Employment Standards Act, 2000, sets out the minimum standards for employment in British Columbia. Section 150(1)(a) of the Act requires employers to provide employees with a minimum of 12 months of earned vacation time."

COMPARISON: SAME
  entitlement or requirement: same
  threshold: same
  eligibility: same
```

**Gold:**
- Ontario (s. 35): Vacation must be completed no later than 10 months after the end of the vacation entitlement year for which it is given.
- British Columbia (s. 57): Annual vacation must be taken within 12 months after completing the year of employment that entitles the employee to it.
- Comparison: Different: 10 months in Ontario vs. 12 months in BC.

**Key facts:**
- [ON] No later than 10 months after the end of the vacation entitlement year → **Missing**
- [BC] Within 12 months after completing the entitling year of employment → **Missing**
- [VERDICT] Different: 10 months in Ontario vs. 12 months in BC → **Incorrect** — says same

**Claims:**
- "Ontario: a minimum of 12 weeks of vacation per year" → **Unsupported** | **Doesn't support** — invented quote; s.28 is public holidays
- "BC: a minimum of 12 months of earned vacation time" → **Unsupported** | **Invalid** — BC has no s.150
- "The two provinces' deadlines are the same" → **Unsupported** | **None** — comparison verdict

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S077 · Q26 · dates_thresholds

**Question:** What are the daily and weekly overtime thresholds in BC for an employee who is not working under an averaging agreement?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 40
  Answer: daily and weekly overtime payment
  Who it applies to: employee who works over 8 hours a day, and is not working under an averaging agreement under section 37
  Amount / threshold: over 8 hours a day, over 40 hours a week
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): Daily overtime begins after eight hours, with double time after 12 hours. Weekly overtime begins after 40 hours, with only the first eight hours worked each day counted toward the weekly calculation.

**Key facts:**
- [BC] Daily threshold: 8 hours → **Correct**
- [BC] Double-time threshold: 12 hours → **Missing**
- [BC] Weekly threshold: 40 hours → **Correct**
- [BC] Only first 8 hours per day count toward weekly overtime → **Missing**

**Claims:**
- "Overtime over 8 hours a day and over 40 hours a week without an averaging agreement" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S078 · Q23 · exceptions

**Question:** I work in Ontario and would rather take time off than get overtime pay. Can my employer let me do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)
  Answer: Employer must give at least one week's notice before taking time off to avoid overtime
  Amount / threshold: At least one week's notice
  Mandatory?: mandatory
  Quote: "The employer must give at least one week's notice before taking time off"
```

**Gold:**
- Ontario (s. 22): Yes. The employer and employee may agree to paid time off at one and a half hours for each overtime hour worked. The time off must generally be taken within three months, or within 12 months if the employee agrees.

**Key facts:**
- [ON] Employer and employee must agree → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Normally taken within 3 months → **Missing**
- [ON] May be taken within 12 months with employee agreement → **Missing**

**Claims:**
- "The employer must give at least one week's notice before time off is taken instead of overtime" → **Unsupported** | **Doesn't support** — invented quote

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S079 · Q03 · direct_extraction

**Question:** I work in Ontario and have only been here for two years. How much vacation pay am I owed?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 35.2
  Answer: Vacation pay is at least 4% of the wages earned during the vacation period, unless the period of employment is five years or more, when it's 6%
  Who it applies to: Employee earns vacation pay under sections 33 or 34 and has a period of employment of less than five years, or five years or more
  Amount / threshold: At least 4% of the wages earned during the vacation period, unless the period of employment is five years or more, when it's 6%
  Mandatory?: mandatory
  Quote: "equal to at least, (a) 4 per cent of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 35.2): The employee is entitled to vacation pay of at least 4% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Correct**
- [ON] Vacation pay is excluded from the wage calculation → **Correct** — in the quote

**Claims:**
- "Vacation pay is at least 4% of wages, or 6% after five years of employment" → **Supported** | **Supports**
- "Wages exclude vacation pay" → **Supported** | **Supports**
- "Applies to employees entitled to vacation under s.33 or 34" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S080 · Q05 · direct_extraction

**Question:** I work in Toronto and sometimes end up doing 48 hours a week. When should I start getting extra pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 20.1(1)(a)
  Answer: Extra pay
  Who it applies to: Employee
  Amount / threshold: 48 hours
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 22): Overtime pay is required for hours worked beyond 44 in a work week (unless a different threshold is prescribed by regulation), at a minimum of 1.5 times the employee's regular rate.

**Key facts:**
- [ON] Weekly overtime threshold is 44 hours → **Incorrect** — says 48 hours
- [ON] Overtime rate is at least 1.5 times the regular rate → **Missing**

**Claims:**
- "Extra pay starts at 48 hours" → **Unsupported** | **Invalid** — ON has no s.20.1

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S081 · Q11 · cross_jurisdiction_comparison

**Question:** I've worked at my job in Ottawa for 6 years. Would someone who's worked 6 years at a job in Vancouver get the same amount of vacation as me?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)
  Answer: Vacation pay must be paid to employees who have been employed continuously for six months and at least one year
  Amount / threshold: At least six months and at least one year continuous employment
  Mandatory?: mandatory
  Quote: "Vacation pay must be paid to employees who have been employed continuously for six months and at least one year"

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The retrieved law does not state this; it may be set out in regulations, which this tool does not include.

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 33): With five or more years of employment, an Ontario employee is entitled to at least three weeks of vacation.
- British Columbia (s. 57): After five consecutive years of employment, a BC employee is entitled to at least three weeks of annual vacation.
- Comparison: Same: both at least 3 weeks after 5 years. Ontario ties it to completed vacation entitlement years; BC to consecutive years of employment.

**Key facts:**
- [ON] At least 3 weeks at 5 years or more → **Missing**
- [BC] At least 3 weeks after 5 consecutive years → **Missing**
- [VERDICT] Same: both at least 3 weeks after 5 years → **Missing** — verdict unknown

**Claims:**
- "Ontario: vacation pay must be paid to employees employed continuously for six months and at least one year" → **Unsupported** | **Doesn't support** — invented quote; s.14 is wage priority

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S082 · Q10 · direct_extraction

**Question:** What is the statutory deadline for paying vacation pay to a BC employee before their annual vacation begins?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 58
  Answer: Must pay vacation pay
  Who it applies to: After 5 consecutive years of employment
  Amount / threshold: At least 6% of total wages
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 58): Vacation pay must be paid at least seven days before the beginning of the employee's annual vacation, unless it is paid on scheduled paydays under a written agreement or collective agreement.

**Key facts:**
- [BC] Payment at least 7 days before vacation → **Missing** — answers the 6% rate
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**

**Claims:**
- "At least 6% of total wages after 5 consecutive years" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S083 · Q22 · exceptions

**Question:** What conditions must be met for a valid averaging agreement under BC's Employment Standards Act?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 37(12)
  Answer: not valid unless certain conditions are met
  Who it applies to: valid averaging agreement
  Amount / threshold: (a)(i) is in writing,
(ii) is signed by the employer and employee before the start date provided in the agreement,
(iii) specifies the number of weeks over which the agreement applies,
(iv) specifies the work schedule for each day covered by the agreement,
(v) specifies the number of times, if any, that the agreement may be repeated, and
(vi) provides for a start date and an expiry date for the period specified under subparagraph (iii)
(b) the schedule in the agreement under paragraph (a) (iv) is in compliance with subsection (3)
(c) the employee receives a copy of the agreement before the date on which the period specified in the agreement begins
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 37): The agreement must be written, signed by both parties before its start date, specify the averaging period and daily work schedule, and meet the other statutory requirements.

**Key facts:**
- [BC] Must be in writing → **Correct**
- [BC] Must be signed before the start date → **Correct**
- [BC] Must specify a 1-, 2-, 3-, or 4-week period → **Partial** — 'number of weeks' without the 1–4 week limit
- [BC] Must specify the daily work schedule → **Correct**
- [BC] Employee must receive a copy before the averaging period begins → **Correct**

**Claims:**
- "The agreement must be in writing and signed by both before its start date" → **Supported** | **Supports**
- "It must specify the number of weeks, the daily schedule, any repeats, and start and expiry dates" → **Supported** | **Supports**
- "The employee must receive a copy before the averaging period begins" → **Supported** | **Supports**
- "The schedule must comply with subsection (3)" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S084 · Q12 · cross_jurisdiction_comparison

**Question:** Compare the deadline for an employee to take earned vacation in Ontario and British Columbia.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)(a)
  Answer: Employees must be entitled to at least one week's paid vacation per year
  Amount / threshold: At least one week's paid vacation per year
  Mandatory?: mandatory
  Quote: "An employer must provide employees with at least one week’s paid vacation per year"

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 35): Vacation must be completed no later than 10 months after the end of the vacation entitlement year for which it is given.
- British Columbia (s. 57): Annual vacation must be taken within 12 months after completing the year of employment that entitles the employee to it.
- Comparison: Different: 10 months in Ontario vs. 12 months in BC.

**Key facts:**
- [ON] No later than 10 months after the end of the vacation entitlement year → **Missing**
- [BC] Within 12 months after completing the entitling year of employment → **Missing**
- [VERDICT] Different: 10 months in Ontario vs. 12 months in BC → **Missing** — verdict unknown

**Claims:**
- "Ontario: at least one week of paid vacation per year" → **Unsupported** | **Doesn't support** — invented quote

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S085 · Q03 · direct_extraction

**Question:** I work in Ontario and have only been here for two years. How much vacation pay am I owed?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Vacation pay
  Who it applies to: Employee
  Amount / threshold: Period of employment
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.
```

**Gold:**
- Ontario (s. 35.2): The employee is entitled to vacation pay of at least 4% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing**
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S086 · Q10 · direct_extraction

**Question:** What is the statutory deadline for paying vacation pay to a BC employee before their annual vacation begins?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 58): Vacation pay must be paid at least seven days before the beginning of the employee's annual vacation, unless it is paid on scheduled paydays under a written agreement or collective agreement.

**Key facts:**
- [BC] Payment at least 7 days before vacation → **Missing**
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S087 · Q15 · cross_jurisdiction_comparison

**Question:** If someone works 45 hours in a week, would they get overtime in Toronto and Vancouver, or does it depend on where they work?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 22
  Answer: entitlement
  Who it applies to: If an employee who performs work of a particular kind or character is exempted from the application of this section by the regulations or the regulations prescribe an overtime threshold of other than 44 hours for an employee who performs such work, and the duties of an employee's position require him or her to perform both that work and work of another kind or character, this Part shall apply to the employee in respect of all work performed by him or her in a work week unless the time spent by the employee performing that other work constitutes less than half the time that the employee spent fulfilling the duties of his or her position in that work week.
  Amount / threshold: 44 hours
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 35
  Answer: Overtime wages
  Who it applies to: Employee
  Amount / threshold: 40 hours
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 22): Ontario's general weekly overtime threshold is 44 hours, so hours beyond 44 qualify for overtime at a minimum of 1.5 times the regular rate.
- British Columbia (s. 40): BC's weekly overtime threshold is 40 hours, with hours beyond 40 paid at 1.5 times the regular wage. Daily overtime also applies to any day over 8 hours.
- Comparison: Different: Ontario pays overtime only for the hour over 44. In BC overtime is owed, but whether it comes from the weekly rule (over 40) or the daily rule (over 8 a day) depends on how the hours fall across the days.

**Key facts:**
- [ON] 44-hour weekly threshold → **Correct**
- [ON] At least 1.5 times the regular rate → **Missing**
- [BC] 40-hour weekly threshold → **Correct**
- [BC] 1.5 times the regular wage → **Missing**
- [BC] Daily overtime may also apply for any day over 8 hours → **Missing**
- [VERDICT] Different: Ontario pays overtime only for the hour over 44; in BC overtime is owed (weekly over 40 or daily over 8) → **Correct** — 44 vs. 40

**Claims:**
- "Ontario: overtime threshold 44 hours" → **Supported** | **Supports**
- "Ontario: an employee doing both exempted and other work is covered unless the other work is under half their time" → **Supported** | **Supports** — s.22(9); not relevant
- "BC: overtime after 40 hours" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S088 · Q27 · insufficient_evidence

**Question:** I work on a farm in Ontario. My employer says farm workers don't get overtime. Is that true?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)(a)
  Answer: Farm workers must be paid at least one and a half times their regular rate of pay for all hours worked over 8 per day and 40 per week
  Amount / threshold: At least one and a half times the regular rate of pay
  Mandatory?: mandatory
  Quote: "The minimum wage shall be at least one and a half times the regular rate of pay"
```

**Gold:**
- Ontario (s. 22): Cannot be determined from the Acts in the knowledge base.
- Abstain (Ontario): s. 22 allows exemptions by regulation, but the regulations that list exempt occupations are not in the knowledge base.

**Key facts:**
- [ON] Explains that overtime exemptions are set by regulation, which is not in the knowledge base, so whether farm workers are exempt can't be determined → **Missing**

**Claims:**
- "Farm workers must be paid 1.5 times for hours over 8 a day and 40 a week" → **Unsupported** | **Doesn't support** — definitive answer on an abstain question; invented quote

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S089 · Q29 · insufficient_evidence

**Question:** My sister works in Calgary and I work in Toronto. We've both been at our jobs for 2 years. Do we get the same vacation pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 36(2)
  Answer: pay the employee his or her vacation pay on or before the pay day for the period in which the vacation falls
  Who it applies to: employee and his or her employer
  Amount / threshold: not specified
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

ALBERTA: not covered. This tool only includes the Ontario and British Columbia Employment Standards Acts, so it cannot answer for this province.
```

**Gold:**
- Ontario (s. 35.2): An Ontario employee with less than five years of employment is entitled to vacation pay of at least 4% of wages, excluding vacation pay, earned during the relevant period.
- Abstain (Alberta): Alberta legislation is not in the knowledge base. The system should answer for Ontario and say it cannot speak to Alberta.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing**

**Claims:**
- "Ontario: vacation pay paid on or before the pay day for the period in which the vacation falls" → **Supported** | **Supports** — s.36(2); its conditions are omitted

**Abstention:** **1**   **False abstention:** **no**

**Reviewed:** yes

---

## S090 · Q23 · exceptions

**Question:** I work in Ontario and would rather take time off than get overtime pay. Can my employer let me do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 27(1)(a)
  Answer: Mandatory
  Who it applies to: Employee
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 22): Yes. The employer and employee may agree to paid time off at one and a half hours for each overtime hour worked. The time off must generally be taken within three months, or within 12 months if the employee agrees.

**Key facts:**
- [ON] Employer and employee must agree → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Normally taken within 3 months → **Missing**
- [ON] May be taken within 12 months with employee agreement → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S091 · Q16 · cross_jurisdiction_comparison

**Question:** Compare the daily overtime rules in Ontario and BC for employees who work more than eight hours in a day.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Daily Overtime Rules
  Answer: Entitlement to overtime pay at one-and-a-half times the regular rate of pay
  Who it applies to: Employees who work more than eight hours in a day
  Amount / threshold: Eight hours worked in a day
  Mandatory?: mandatory

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Daily Overtime Rules
  Answer: Entitlement to overtime pay at one-and-one-half times the regular rate of pay
  Who it applies to: Employees who work more than eight hours in a day
  Amount / threshold: Eight hours worked in a day
  Mandatory?: mandatory

COMPARISON: SAME
  entitlement or requirement: same
  threshold: same
  eligibility: same
```

**Gold:**
- Ontario (s. 22): Ontario's overtime section (s. 22) sets overtime on a weekly basis only: hours over 44 in a work week (or a prescribed threshold). It does not provide for daily overtime.
- British Columbia (s. 40): BC requires 1.5 times regular wages for hours over eight in a day and double wages for hours over 12, unless an averaging agreement applies.
- Comparison: Different: BC has daily overtime (1.5x over 8 hours, double over 12); Ontario has none, only a weekly threshold.

**Key facts:**
- [ON] No daily overtime threshold in s. 22 → **Incorrect** — says daily overtime after 8 hours
- [BC] Daily overtime after 8 hours → **Correct**
- [BC] Double time after 12 hours → **Missing**
- [BC] Averaging agreement may affect the calculation → **Missing**
- [VERDICT] Different: BC has daily overtime (1.5x over 8, double over 12); Ontario has none, only weekly → **Incorrect** — says same

**Claims:**
- "Ontario: overtime at 1.5 times for over eight hours a day" → **Unsupported** | **Invalid**
- "BC: overtime at 1.5 times for over eight hours a day" → **Supported** | **Invalid** — 'Daily Overtime Rules' is not a section
- "Ontario and BC daily overtime rules are the same" → **Unsupported** | **None** — comparison verdict

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S092 · Q28 · insufficient_evidence

**Question:** Are employees in managerial positions exempt from the daily and weekly overtime requirements in British Columbia?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The retrieved law does not state this; it may be set out in regulations, which this tool does not include.
```

**Gold:**
- British Columbia (s. 37, 40): Cannot be determined from the Acts in the knowledge base.
- Abstain (British Columbia): the BC Act does not address a manager exclusion; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Sections 37 and 40 set out averaging agreements and general overtime rules → **Missing**
- [BC] The BC Act does not establish a managerial exemption; occupation-specific exclusions are in the regulations, which are not in the knowledge base → **Correct** — 'may be set out in regulations, which this tool does not include'

**Claims:**
- (no claims)

**Abstention:** **1**   **False abstention:** **no**

**Reviewed:** yes

---

## S093 · Q22 · exceptions

**Question:** What conditions must be met for a valid averaging agreement under BC's Employment Standards Act?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 37(2)
  Answer: The agreement must comply with subsection (3) regarding the work schedule
  Who it applies to: The agreement must be in writing, signed by both parties before the start date, specify the number of weeks, work schedules, repeatable times, start and end dates, and the employee must receive a copy before the agreement starts
  Amount / threshold: Written, signed by both parties before the start date, specifying the number of weeks, work schedules, repeatable times, start and end dates, and the employee receiving a copy before the agreement starts
  Mandatory?: mandatory
  Exceptions: Waiver of the averaging agreement is not permitted
  Quote: "(a) the agreement (i) is in writing, (ii) is signed by the employer and employee before the start date provided in the agreement, etc."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 37): The agreement must be written, signed by both parties before its start date, specify the averaging period and daily work schedule, and meet the other statutory requirements.

**Key facts:**
- [BC] Must be in writing → **Correct**
- [BC] Must be signed before the start date → **Correct**
- [BC] Must specify a 1-, 2-, 3-, or 4-week period → **Partial** — 'number of weeks' without the 1–4 week limit
- [BC] Must specify the daily work schedule → **Correct**
- [BC] Employee must receive a copy before the averaging period begins → **Correct**

**Claims:**
- "The agreement must be in writing and signed by both before its start date" → **Supported** | **Supports**
- "It must specify the number of weeks, the daily schedule, any repeats, and start and expiry dates" → **Supported** | **Supports**
- "The employee must receive a copy before the averaging period begins" → **Supported** | **Supports**
- "Waiver of the averaging agreement is not permitted" → **Unsupported** | **Doesn't support** — s.37(14) says the agreement is not a waiver of the Act, a different rule

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S094 · Q19 · exceptions

**Question:** Instead of getting my vacation pay all at once, can my employer in Ontario just add it to every paycheque?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: Entitlement to vacation pay must be established by contract between employee and employer.
  Who it applies to: All employees who have worked for their employer for more than one year and earned at least $15 per hour.
  Amount / threshold: The amount of vacation pay that may be added to each paycheque depends on the terms of the contract between the employee and employer.
```

**Gold:**
- Ontario (s. 36): Only if the employee has agreed to it and the vacation pay is shown separately, either on the wage statement for each pay period or on a separate statement given at the same time. Otherwise the default is a lump sum before the vacation starts.

**Key facts:**
- [ON] Requires an agreement between the employee and employer → **Missing**
- [ON] Vacation pay shown separately on the wage statement, or on a separate statement provided at the same time → **Missing**
- [ON] Default is a lump sum before vacation (s. 36(1)) → **Missing**

**Claims:**
- "Entitlement to vacation pay must be set by contract" → **Unsupported** | **Invalid**
- "Applies to employees with over one year of service earning at least $15 an hour" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S095 · Q01 · direct_extraction

**Question:** I've been working in Toronto for about 3 years. How much paid time off am I supposed to get each year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 41(1)(a)
  Answer: At least one week of annual leave per full-time employee
  Amount / threshold: One week per full-time employee
  Mandatory?: mandatory
  Quote: "Annual leave shall be at least one week per full-time employee"
```

**Gold:**
- Ontario (s. 33): At least two weeks of vacation each year (the two-week level applies to employees with less than five years of employment).

**Key facts:**
- [ON] At least 2 weeks of vacation → **Incorrect** — says at least one week

**Claims:**
- "Annual leave is at least one week per full-time employee" → **Unsupported** | **Doesn't support** — invented rule and invented quote; s.41 says nothing of this

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S096 · Q07 · direct_extraction

**Question:** My boss in BC says my vacation pay will be lower this year because I got a bonus. Is that allowed?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 59
  Answer: must not reduce an employee's annual vacation or vacation pay
  Who it applies to: An employee
  Amount / threshold: because the employee was paid a bonus or sick pay, or was previously given a longer annual vacation than the minimum required under section 57
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 59): No. A BC employer must not reduce an employee's annual vacation or vacation pay because the employee was paid a bonus.

**Key facts:**
- [BC] Cannot reduce vacation or vacation pay because of a bonus → **Correct**

**Claims:**
- "An employer must not reduce annual vacation or vacation pay because the employee was paid a bonus or sick pay" → **Supported** | **Supports**
- "Or because the employee previously got a longer vacation than the s.57 minimum" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S097 · Q17 · cross_jurisdiction_comparison

**Question:** I want to split my vacation into single days instead of whole weeks. Can I do that in Ontario? What about in BC?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 60
  Answer: An annual vacation
  Who it applies to: An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58, so long as this does not result in a reduction of any employee's rights under those sections.
  Amount / threshold: at least 2 weeks, after 12 consecutive months of employment, or at least 3 weeks, after 5 consecutive years of employment.
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 35): By default, Ontario vacation is taken in whole weeks (a two-week period or two one-week periods; for 5+ years, combinations of one-, two-, or three-week periods). Shorter periods are allowed only if the employee requests them in writing and the employer agrees.
- British Columbia (s. 57): BC requires the employer to allow an employee to take annual vacation in periods of one or more weeks. Section 57 does not address periods shorter than a week.
- Comparison: Similar: both are built around whole weeks. Ontario allows shorter periods by written request plus employer agreement; BC requires the employer to allow periods of one week or more.

**Key facts:**
- [ON] Default is whole-week periods → **Missing**
- [ON] Shorter periods only if the employee requests in writing and the employer agrees → **Missing**
- [BC] Employer must allow vacation in periods of one or more weeks → **Missing**
- [BC] Periods shorter than a week are not addressed in s. 57 → **Missing**
- [VERDICT] Similar: both built around whole weeks; Ontario allows shorter periods by written request plus employer agreement → **Missing** — verdict unknown

**Claims:**
- "BC: an employer may use a common date if no employee's rights are reduced" → **Supported** | **Supports**
- "BC: at least 2 weeks after 12 months, 3 weeks after 5 years" → **Supported** | **Doesn't support** — s.57, cited s.60

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S098 · Q29 · insufficient_evidence

**Question:** My sister works in Calgary and I work in Toronto. We've both been at our jobs for 2 years. Do we get the same vacation pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 36
  Answer: not specified in the excerpt
  Who it applies to: not specified in the excerpt
  Amount / threshold: not specified in the excerpt
  Mandatory?: not specified in the excerpt
  Exceptions: n; o; t;  ; s; p; e; c; i; f; i; e; d;  ; i; n;  ; t; h; e;  ; e; x; c; e; r; p; t
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

ALBERTA: not covered. This tool only includes the Ontario and British Columbia Employment Standards Acts, so it cannot answer for this province.
```

**Gold:**
- Ontario (s. 35.2): An Ontario employee with less than five years of employment is entitled to vacation pay of at least 4% of wages, excluding vacation pay, earned during the relevant period.
- Abstain (Alberta): Alberta legislation is not in the knowledge base. The system should answer for Ontario and say it cannot speak to Alberta.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing** — every Ontario field says 'not specified in the excerpt'

**Claims:**
- (no claims)

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S099 · Q14 · cross_jurisdiction_comparison

**Question:** We've got employees in Toronto and Vancouver who've both been here for six years. Do they get the same vacation pay percentage?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: Vacation pay percentage
  Who it applies to: Employees working in Toronto and Vancouver
  Amount / threshold: Six years of service
  Mandatory?: Yes

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: Vacation pay percentage
  Who it applies to: Employees working in Toronto and Vancouver
  Amount / threshold: Six years of service
  Mandatory?: Yes

COMPARISON: SAME
  entitlement or requirement: same
  threshold: same
  eligibility: same
```

**Gold:**
- Ontario (s. 35.2): At least 6% of wages, excluding vacation pay, for employees with five or more years of employment.
- British Columbia (s. 58): At least 6% of total wages during the relevant year after five consecutive years of employment.
- Comparison: Same: both at least 6% after five years. The wage base is worded differently (Ontario: wages excluding vacation pay earned in the period; BC: total wages in the entitling year).

**Key facts:**
- [ON] Minimum 6% → **Missing**
- [ON] Excludes vacation pay from wages → **Missing**
- [BC] Minimum 6% → **Missing**
- [BC] Based on total wages during the relevant year → **Missing**
- [VERDICT] Same: both at least 6% after five years → **Partial** — 'same' with no percentage given

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S100 · Q26 · dates_thresholds

**Question:** What are the daily and weekly overtime thresholds in BC for an employee who is not working under an averaging agreement?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 40): Daily overtime begins after eight hours, with double time after 12 hours. Weekly overtime begins after 40 hours, with only the first eight hours worked each day counted toward the weekly calculation.

**Key facts:**
- [BC] Daily threshold: 8 hours → **Missing**
- [BC] Double-time threshold: 12 hours → **Missing**
- [BC] Weekly threshold: 40 hours → **Missing**
- [BC] Only first 8 hours per day count toward weekly overtime → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S101 · Q20 · exceptions

**Question:** How must an employer calculate vacation entitlement for an Ontario employee during a stub period created by an alternative vacation entitlement year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 15.1(3)
  Answer: The employer records the amounts of vacation time earned, taken, and unearned during the stub period, as well as the vacation pay earned and paid during that period
  Who it applies to: Employer establishes an alternative vacation entitlement year for an employee
  Mandatory?: mandatory
  Quote: "the employer shall record the following information for the stub period"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 34): The employer must calculate the ratio of the stub period to 12 months and apply it to the employee's applicable two-week or three-week vacation entitlement, using a separate calculation for employees without a regular work week.

**Key facts:**
- [ON] Calculate stub-period-to-12-month ratio → **Missing** — answers record-keeping, not the calculation
- [ON] Less than 5 years: use 2 weeks as the base → **Missing**
- [ON] 5 years or more: use 3 weeks as the base → **Missing**
- [ON] Employees without a regular work week use average weekly working days → **Missing**

**Claims:**
- "The employer must record vacation time earned, taken and not taken, and vacation pay earned and paid, for the stub period" → **Supported** | **Supports** — s.15.1(3); not the calculation

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S102 · Q01 · direct_extraction

**Question:** I've been working in Toronto for about 3 years. How much paid time off am I supposed to get each year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 50.1(1.3)
  Answer: An employee is entitled to take a total of three paid days of leave under subsection (1.2)
  Who it applies to: Subject to subsection (1.4), which is not included in this excerpt
  Amount / threshold: Three paid days per year
  Mandatory?: optional
  Exceptions: Subject to subsection (1.4), which is not included in this excerpt
  Quote: "an employee is entitled to take a total of three paid days of leave"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 33): At least two weeks of vacation each year (the two-week level applies to employees with less than five years of employment).

**Key facts:**
- [ON] At least 2 weeks of vacation → **Missing** — answers 3 paid days of leave (s.50.1), not vacation

**Claims:**
- "An employee is entitled to a total of three paid days of leave under s.50.1(1.2)" → **Supported** | **Supports** — true but about infectious disease emergency leave, not vacation

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S103 · Q16 · cross_jurisdiction_comparison

**Question:** Compare the daily overtime rules in Ontario and BC for employees who work more than eight hours in a day.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 17(1) and 22(9) and 22(1)
  Answer: no employer shall require or permit an employee to work more than, (a) eight hours in a day or, if the employer establishes a regular work day of more than eight hours for the employee, the number of hours in his or her regular work day; and (b) 48 hours in a work week.
  Who it applies to: employees who work more than eight hours in a day
  Amount / threshold: 8 hours in a day or 48 hours in a work week
  Mandatory?: mandatory
  Exceptions: N; o; t;  ; s; p; e; c; i; f; i; e; d;  ; i; n;  ; t; h; e;  ; e; x; c; e; r; p; t
  Quote: "Subject to subsections (2) and (3), no employer shall require or permit an employee to work more than, (a) eight hours in a day or, if the employer establishes a regular work day of more than eight hours for the employee, the number of hours in his or her regular work day; and (b) 48 hours in a work week."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 35
  Answer: must pay overtime wages
  Who it applies to: employees who work more than 8 hours in a day
  Amount / threshold: 8 hours
  Mandatory?: mandatory
  Exceptions: N; o; t;  ; s; p; e; c; i; f; i; e; d;  ; i; n;  ; t; h; e;  ; e; x; c; e; r; p; t
  Quote: "An employer must pay an employee overtime wages in accordance with section 40 if the employer requires, or directly or indirectly allows, the employee to work more than 8 hours a day or 40 hours a week."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: same
```

**Gold:**
- Ontario (s. 22): Ontario's overtime section (s. 22) sets overtime on a weekly basis only: hours over 44 in a work week (or a prescribed threshold). It does not provide for daily overtime.
- British Columbia (s. 40): BC requires 1.5 times regular wages for hours over eight in a day and double wages for hours over 12, unless an averaging agreement applies.
- Comparison: Different: BC has daily overtime (1.5x over 8 hours, double over 12); Ontario has none, only a weekly threshold.

**Key facts:**
- [ON] No daily overtime threshold in s. 22 → **Missing** — gives the hours-of-work limit, not overtime
- [BC] Daily overtime after 8 hours → **Correct**
- [BC] Double time after 12 hours → **Missing**
- [BC] Averaging agreement may affect the calculation → **Missing**
- [VERDICT] Different: BC has daily overtime (1.5x over 8, double over 12); Ontario has none, only weekly → **Partial** — 'different' for the wrong reason

**Claims:**
- "Ontario: no employer may require more than 8 hours a day or 48 hours a week" → **Supported** | **Supports** — s.17
- "BC: overtime for more than 8 hours a day or 40 a week" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S104 · Q17 · cross_jurisdiction_comparison

**Question:** I want to split my vacation into single days instead of whole weeks. Can I do that in Ontario? What about in BC?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment standards
  Answer: Entitlement to take vacation days as requested by the employee
  Who it applies to: All employees
  Mandatory?: Not applicable

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment standards
  Answer: Entitlement to take vacation days as requested by the employee
  Who it applies to: All employees

COMPARISON: SAME
  entitlement or requirement: same
  threshold: unknown
  eligibility: same
```

**Gold:**
- Ontario (s. 35): By default, Ontario vacation is taken in whole weeks (a two-week period or two one-week periods; for 5+ years, combinations of one-, two-, or three-week periods). Shorter periods are allowed only if the employee requests them in writing and the employer agrees.
- British Columbia (s. 57): BC requires the employer to allow an employee to take annual vacation in periods of one or more weeks. Section 57 does not address periods shorter than a week.
- Comparison: Similar: both are built around whole weeks. Ontario allows shorter periods by written request plus employer agreement; BC requires the employer to allow periods of one week or more.

**Key facts:**
- [ON] Default is whole-week periods → **Incorrect** — says vacation days can be taken as the employee requests
- [ON] Shorter periods only if the employee requests in writing and the employer agrees → **Partial** — employee request mentioned; written form and employer agreement missing
- [BC] Employer must allow vacation in periods of one or more weeks → **Missing**
- [BC] Periods shorter than a week are not addressed in s. 57 → **Missing**
- [VERDICT] Similar: both built around whole weeks; Ontario allows shorter periods by written request plus employer agreement → **Partial** — 'same' with no difference noted

**Claims:**
- "Ontario: employees are entitled to take vacation days as they request" → **Unsupported** | **Invalid** — needs written request and employer agreement
- "BC: employees are entitled to take vacation days as they request" → **Unsupported** | **Invalid** — s.57 only requires periods of one week or more

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S105 · Q09 · direct_extraction

**Question:** Can a BC employer use a single common date to calculate annual vacation entitlement for all of its employees?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 60
  Answer: Annual vacation calculated based on a common date, which cannot reduce the rights of any employee under sections 57 and 58
  Who it applies to: Employer uses a common date for calculating annual vacation entitlements without reducing any employee's rights under sections 57 and 58
  Amount / threshold: At least 2 weeks after 12 consecutive months of employment, or at least 3 weeks after 5 consecutive years of employment
  Mandatory?: mandatory
  Quote: "so long as this does not result in a reduction of any employee's rights under those sections"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 60): Yes. An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58, as long as this does not reduce any employee's rights under those sections.

**Key facts:**
- [BC] A common date for all employees is permitted → **Correct**
- [BC] Must not reduce any employee's rights under those sections → **Correct**

**Claims:**
- "A common date may be used if it doesn't reduce any employee's rights under ss.57 and 58" → **Supported** | **Supports**
- "At least 2 weeks after 12 months, 3 weeks after 5 years" → **Supported** | **Doesn't support** — s.57, cited as s.60
- "The rule is mandatory" → **Unsupported** | **Doesn't support** — wrong 'Mandatory?' label on a question about what is allowed

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S106 · Q22 · exceptions

**Question:** What conditions must be met for a valid averaging agreement under BC's Employment Standards Act?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 22(1)(a)
  Answer: Entitlement
  Who it applies to: Employers with 50 or more employees
  Amount / threshold: 1000 hours
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 37): The agreement must be written, signed by both parties before its start date, specify the averaging period and daily work schedule, and meet the other statutory requirements.

**Key facts:**
- [BC] Must be in writing → **Missing**
- [BC] Must be signed before the start date → **Missing**
- [BC] Must specify a 1-, 2-, 3-, or 4-week period → **Missing**
- [BC] Must specify the daily work schedule → **Missing**
- [BC] Employee must receive a copy before the averaging period begins → **Missing**

**Claims:**
- "Applies to employers with 50 or more employees; 1000 hours" → **Unsupported** | **Doesn't support**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S107 · Q20 · exceptions

**Question:** How must an employer calculate vacation entitlement for an Ontario employee during a stub period created by an alternative vacation entitlement year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 15.1(3)
  Answer: Vacation entitlement
  Who it applies to: Employee
  Amount / threshold: Stub period
  Mandatory?: mandatory
  Quote: "The employer shall record the following information for the stub period: 1. The amount of vacation time that the employee earned during the stub period. 2. The amount of vacation time, if any, that the employee took during the stub period. 3. The amount of vacation time, if any, earned but not taken by the employee during the stub period. 3.1 The amount of vacation pay that the employee earned during the stub period and how that amount was calculated. 4. The amount of vacation pay paid to the employee during the stub period. 5. The amount of wages on which the vacation pay referred to in paragraph 4 was calculated and the period of time to which those wages relate."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 34): The employer must calculate the ratio of the stub period to 12 months and apply it to the employee's applicable two-week or three-week vacation entitlement, using a separate calculation for employees without a regular work week.

**Key facts:**
- [ON] Calculate stub-period-to-12-month ratio → **Missing** — answers record-keeping, not the calculation
- [ON] Less than 5 years: use 2 weeks as the base → **Missing**
- [ON] 5 years or more: use 3 weeks as the base → **Missing**
- [ON] Employees without a regular work week use average weekly working days → **Missing**

**Claims:**
- "The employer must record vacation time earned, taken and not taken, and vacation pay earned and paid, for the stub period" → **Supported** | **Supports** — s.15.1(3); not the calculation

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S108 · Q04 · direct_extraction

**Question:** What is the minimum vacation pay percentage for an Ontario employee with at least five years of employment?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: Minimum vacation pay
  Who it applies to: At least five years of employment
  Amount / threshold: 5%
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 35.2): The employee must receive vacation pay equal to at least 6% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 6% vacation pay → **Incorrect** — says 5%
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- "Minimum vacation pay after five years is 5%" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S109 · Q14 · cross_jurisdiction_comparison

**Question:** We've got employees in Toronto and Vancouver who've both been here for six years. Do they get the same vacation pay percentage?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 35.2
  Answer: Vacation pay is at least 4% of the wages excluding vacation pay, or 6%, depending on the length of employment
  Who it applies to: Employee's period of employment is less than five years or five years or more
  Amount / threshold: At least 4% of wages excluding vacation pay, or 6% if the period of employment is five years or more
  Mandatory?: mandatory
  Exceptions: Sections 36, 37 and 38 do not apply if the employee is represented by a trade union and the employer makes contributions to a multi-employer vacation benefit plan
  Quote: "equal to at least, (a) 4 per cent of the wages, excluding vacation pay, that the employee earned during the period for which the vacation is given, if the employee’s period of employment is less than five years; or"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 58
  Answer: At least 4% of the employee's total wages during the year of employment, then at least 6%
  Who it applies to: After 5 calendar days of employment, after 5 consecutive years of employment
  Amount / threshold: At least 4%, then at least 6% of the employee's total wages during the year of employment
  Mandatory?: mandatory
  Exceptions: Vacation pay must be paid at least 7 days before the beginning of the employee's annual vacation, or on their scheduled payday
  Quote: "at least 4% of the employee's total wages during the year of employment entitling the employee to the vacation pay"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: same
  threshold: different
  eligibility: same
```

**Gold:**
- Ontario (s. 35.2): At least 6% of wages, excluding vacation pay, for employees with five or more years of employment.
- British Columbia (s. 58): At least 6% of total wages during the relevant year after five consecutive years of employment.
- Comparison: Same: both at least 6% after five years. The wage base is worded differently (Ontario: wages excluding vacation pay earned in the period; BC: total wages in the entitling year).

**Key facts:**
- [ON] Minimum 6% → **Correct**
- [ON] Excludes vacation pay from wages → **Correct**
- [BC] Minimum 6% → **Correct**
- [BC] Based on total wages during the relevant year → **Correct**
- [VERDICT] Same: both at least 6% after five years → **Incorrect** — says different

**Claims:**
- "Ontario: at least 4% of wages excluding vacation pay, or 6% at five years or more" → **Supported** | **Supports**
- "Ontario: ss.36–38 don't apply if the employee has a union and the employer contributes to a multi-employer vacation plan" → **Supported** | **Doesn't support** — s.39, cited as s.35.2
- "BC: at least 4%, then at least 6% after 5 consecutive years, of total wages" → **Supported** | **Supports**
- "BC: vacation pay is paid at least 7 days before the vacation or on scheduled paydays" → **Supported** | **Supports** — condition omitted
- "Ontario and BC vacation pay percentages differ at six years" → **Unsupported** | **None** — comparison verdict; both are 6%

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S110 · Q07 · direct_extraction

**Question:** My boss in BC says my vacation pay will be lower this year because I got a bonus. Is that allowed?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 59): No. A BC employer must not reduce an employee's annual vacation or vacation pay because the employee was paid a bonus.

**Key facts:**
- [BC] Cannot reduce vacation or vacation pay because of a bonus → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S111 · Q06 · direct_extraction

**Question:** I just finished my first year working in BC. Am I supposed to get two weeks off now?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 57): Yes. After 12 consecutive months of employment, an employee is entitled to at least two weeks of annual vacation.

**Key facts:**
- [BC] At least 2 weeks of annual vacation → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S112 · Q14 · cross_jurisdiction_comparison

**Question:** We've got employees in Toronto and Vancouver who've both been here for six years. Do they get the same vacation pay percentage?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 28(1)(a)
  Answer: Entitlement to vacation pay
  Who it applies to: Employees who have worked for the employer for at least 12 months
  Amount / threshold: 12 months
  Mandatory?: mandatory

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 22(1)(a)
  Answer: Entitlement to vacation pay
  Who it applies to: Employees who have worked for the employer for at least 60 days
  Amount / threshold: 60 days
  Mandatory?: mandatory

COMPARISON: DIFFERENT
  entitlement or requirement: same
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 35.2): At least 6% of wages, excluding vacation pay, for employees with five or more years of employment.
- British Columbia (s. 58): At least 6% of total wages during the relevant year after five consecutive years of employment.
- Comparison: Same: both at least 6% after five years. The wage base is worded differently (Ontario: wages excluding vacation pay earned in the period; BC: total wages in the entitling year).

**Key facts:**
- [ON] Minimum 6% → **Missing**
- [ON] Excludes vacation pay from wages → **Missing**
- [BC] Minimum 6% → **Missing**
- [BC] Based on total wages during the relevant year → **Missing**
- [VERDICT] Same: both at least 6% after five years → **Incorrect** — says different

**Claims:**
- "Ontario: vacation pay after at least 12 months with the employer" → **Unsupported** | **Doesn't support**
- "BC: vacation pay after at least 60 days with the employer" → **Unsupported** | **Doesn't support**
- "Ontario and BC vacation pay percentages differ at six years" → **Unsupported** | **None** — comparison verdict; both are 6%

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S113 · Q13 · cross_jurisdiction_comparison

**Question:** We have staff in Toronto and Vancouver who'd rather bank their overtime and take time off later. Can we do that in both provinces, and do the rules differ?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 22): Yes, if the employer and employee agree. The employee receives 1.5 hours of paid time off for each overtime hour, taken within 3 months of the work week in which it was earned (or within 12 months with the employee's agreement). If employment ends before the time off is taken, overtime pay is owed.
- British Columbia (s. 42): Yes. At the employee's written request, the employer may set up a time bank and credit overtime wages to it at overtime rates. The employee can ask at any time to be paid out, to use the credit for paid time off at an agreed time, or to close the bank. The employer may close it with one month's written notice and must settle it within 6 months. The balance must be paid on termination or when the employee asks to close it.
- Comparison: Different: both allow banking overtime, but Ontario uses an agreement with a 3- or 12-month deadline to take the time off, while BC uses a time bank set up at the employee's written request, with no use-by deadline stated while it is open.

**Key facts:**
- [ON] Requires agreement between employer and employee → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Taken within 3 months, or within 12 months with the employee's agreement → **Missing**
- [ON] Paid out as overtime pay if employment ends first → **Missing**
- [BC] Set up at the employee's written request → **Missing**
- [BC] Overtime credited at overtime rates → **Missing**
- [BC] Employee may request payout, time off, or closing at any time → **Missing**
- [BC] Employer may close with 1 month's written notice and settle within 6 months → **Missing**
- [BC] Balance paid on termination or on the employee's request to close → **Missing**
- [VERDICT] Different: both allow banking overtime; Ontario by agreement with a 3- or 12-month deadline, BC by a time bank at the employee's written request → **Missing** — verdict unknown

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S114 · Q03 · direct_extraction

**Question:** I work in Ontario and have only been here for two years. How much vacation pay am I owed?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 28
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 240 hours
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 35.2): The employee is entitled to vacation pay of at least 4% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing**
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- "The entitlement is 240 hours" → **Unsupported** | **Doesn't support** — invented; s.28 is about public holidays

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S115 · Q19 · exceptions

**Question:** Instead of getting my vacation pay all at once, can my employer in Ontario just add it to every paycheque?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 24(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 36): Only if the employee has agreed to it and the vacation pay is shown separately, either on the wage statement for each pay period or on a separate statement given at the same time. Otherwise the default is a lump sum before the vacation starts.

**Key facts:**
- [ON] Requires an agreement between the employee and employer → **Missing**
- [ON] Vacation pay shown separately on the wage statement, or on a separate statement provided at the same time → **Missing**
- [ON] Default is a lump sum before vacation (s. 36(1)) → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S116 · Q04 · direct_extraction

**Question:** What is the minimum vacation pay percentage for an Ontario employee with at least five years of employment?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Minimum vacation pay percentage
  Who it applies to: Employee with at least five years of employment
  Amount / threshold: At least five years of employment
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.
```

**Gold:**
- Ontario (s. 35.2): The employee must receive vacation pay equal to at least 6% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 6% vacation pay → **Missing**
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S117 · Q08 · direct_extraction

**Question:** I'm working a 10-hour shift in BC today. Should the last couple of hours be paid at a higher rate?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 28(3)(a)
  Answer: The first 10 hours after the 48th hour must be paid at time and a half
  Who it applies to: Worked more than 48 consecutive hours in one week
  Amount / threshold: First 10 hours after the 48th hour must be paid at time and a half
  Mandatory?: mandatory
  Quote: "Hours worked beyond the first 48 hours in one week shall be paid at time and a half"
```

**Gold:**
- British Columbia (s. 40): If the employee is not working under an averaging agreement, hours beyond eight in a day must be paid at 1.5 times the regular wage.

**Key facts:**
- [BC] Hours over 8 a day are paid at 1.5 times the regular wage → **Incorrect** — says time and a half only after 48 hours a week
- [BC] No averaging agreement applies → **Missing**

**Claims:**
- "Hours beyond the first 48 in a week are paid at time and a half" → **Unsupported** | **Doesn't support** — invented quote; s.28 is payroll records

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S118 · Q19 · exceptions

**Question:** Instead of getting my vacation pay all at once, can my employer in Ontario just add it to every paycheque?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 36
  Answer: Paid
  Who it applies to: Employee
  Amount / threshold: Accrues during a pay period
  Mandatory?: mandatory
  Quote: "The employer may pay the employee vacation pay at a time set out in an agreement that the employee has made with the employer."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 36): Only if the employee has agreed to it and the vacation pay is shown separately, either on the wage statement for each pay period or on a separate statement given at the same time. Otherwise the default is a lump sum before the vacation starts.

**Key facts:**
- [ON] Requires an agreement between the employee and employer → **Correct**
- [ON] Vacation pay shown separately on the wage statement, or on a separate statement provided at the same time → **Missing**
- [ON] Default is a lump sum before vacation (s. 36(1)) → **Missing**

**Claims:**
- "The employer may pay vacation pay at a time set out in an agreement with the employee" → **Supported** | **Supports** — s.36(4)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S119 · Q21 · exceptions

**Question:** My employer in Ontario wants to average my hours over a few weeks instead of paying overtime every time I go over 44 hours. Are they allowed to do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Overtime pay
  Who it applies to: Employee's hours of work may be averaged over periods of a specified number of weeks
  Amount / threshold: Four weeks or the number of weeks specified in the agreement, whichever is lower
  Mandatory?: mandatory
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.
```

**Gold:**
- Ontario (s. 22): Yes, the employer and employee may agree to average hours over separate, non-overlapping, contiguous periods of two or more consecutive weeks, subject to the statutory requirements and a maximum of four weeks or the shorter period specified in the agreement.

**Key facts:**
- [ON] Employer and employee must agree → **Partial** — agreement only implied
- [ON] Periods must be separate, non-overlapping, and contiguous → **Missing**
- [ON] Averaged over 2 to 4 weeks (or the shorter period specified in the agreement) → **Partial** — 4-week maximum given; 2-week minimum missing
- [ON] Agreement must have start and expiry dates → **Missing**
- [ON] For non-union employees, the agreement expires no more than 2 years after the start date → **Missing**

**Claims:**
- "Hours may be averaged over up to four weeks or the number in the agreement, whichever is lower" → **Supported** | **Invalid** — 'section' is the Act name

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S120 · Q03 · direct_extraction

**Question:** I work in Ontario and have only been here for two years. How much vacation pay am I owed?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)(a)
  Answer: Vacation pay is calculated as three times the employee's regular weekly wage
  Who it applies to: Employer must provide at least one week's vacation pay to employees who have worked for at least six months but less than one year
  Amount / threshold: At least one week's vacation pay
  Mandatory?: mandatory
  Quote: "The employer shall provide vacation pay equal to three times the employee's regular weekly wage"
```

**Gold:**
- Ontario (s. 35.2): The employee is entitled to vacation pay of at least 4% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Incorrect** — says three times the weekly wage
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- "Vacation pay is three times the employee's regular weekly wage" → **Unsupported** | **Doesn't support** — invented rule and quote; s.14 is about wage priority
- "At least one week's vacation pay for employees with six months to one year of service" → **Unsupported** | **Doesn't support**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S121 · Q15 · cross_jurisdiction_comparison

**Question:** If someone works 45 hours in a week, would they get overtime in Toronto and Vancouver, or does it depend on where they work?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 29(1)(a)
  Answer: Overtime is optional for employees who work less than 40 hours in a week.
  Who it applies to: Overtime is not mandatory for employees who work less than 40 hours in a week.
  Amount / threshold: 40 hours

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 140(1)(a)
  Answer: overtime
  Who it applies to: 45 hours in a week
  Amount / threshold: 45 hours
  Mandatory?: mandatory

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 22): Ontario's general weekly overtime threshold is 44 hours, so hours beyond 44 qualify for overtime at a minimum of 1.5 times the regular rate.
- British Columbia (s. 40): BC's weekly overtime threshold is 40 hours, with hours beyond 40 paid at 1.5 times the regular wage. Daily overtime also applies to any day over 8 hours.
- Comparison: Different: Ontario pays overtime only for the hour over 44. In BC overtime is owed, but whether it comes from the weekly rule (over 40) or the daily rule (over 8 a day) depends on how the hours fall across the days.

**Key facts:**
- [ON] 44-hour weekly threshold → **Incorrect** — implies a 40-hour rule
- [ON] At least 1.5 times the regular rate → **Missing**
- [BC] 40-hour weekly threshold → **Missing**
- [BC] 1.5 times the regular wage → **Missing**
- [BC] Daily overtime may also apply for any day over 8 hours → **Missing**
- [VERDICT] Different: Ontario pays overtime only for the hour over 44; in BC overtime is owed (weekly over 40 or daily over 8) → **Partial** — no valid reason

**Claims:**
- "Ontario: overtime is optional for employees who work less than 40 hours a week" → **Unsupported** | **Doesn't support** — s.29 is public holidays
- "BC: overtime at 45 hours" → **Unsupported** | **Invalid** — BC has no s.140

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S122 · Q17 · cross_jurisdiction_comparison

**Question:** I want to split my vacation into single days instead of whole weeks. Can I do that in Ontario? What about in BC?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario)
  Not specified in the retrieved sections. The retrieved law does not state this; it may be set out in regulations, which this tool does not include.

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 35): By default, Ontario vacation is taken in whole weeks (a two-week period or two one-week periods; for 5+ years, combinations of one-, two-, or three-week periods). Shorter periods are allowed only if the employee requests them in writing and the employer agrees.
- British Columbia (s. 57): BC requires the employer to allow an employee to take annual vacation in periods of one or more weeks. Section 57 does not address periods shorter than a week.
- Comparison: Similar: both are built around whole weeks. Ontario allows shorter periods by written request plus employer agreement; BC requires the employer to allow periods of one week or more.

**Key facts:**
- [ON] Default is whole-week periods → **Missing**
- [ON] Shorter periods only if the employee requests in writing and the employer agrees → **Missing**
- [BC] Employer must allow vacation in periods of one or more weeks → **Missing**
- [BC] Periods shorter than a week are not addressed in s. 57 → **Missing**
- [VERDICT] Similar: both built around whole weeks; Ontario allows shorter periods by written request plus employer agreement → **Missing** — verdict unknown

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S123 · Q21 · exceptions

**Question:** My employer in Ontario wants to average my hours over a few weeks instead of paying overtime every time I go over 44 hours. Are they allowed to do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 22(1), 22(2), 22(3)
  Answer: Employer pays overtime pay of at least one and one-half times the regular rate for each hour worked above 44 hours in each workweek, or the agreed-upon threshold, whichever is lower
  Who it applies to: Employee makes an agreement with the employer that their hours can be averaged over a specified number of weeks
  Amount / threshold: At least one and one-half times the regular rate for each hour worked above 44 hours in each workweek, or the agreed-upon threshold, whichever is lower
  Mandatory?: mandatory
  Exceptions: The averaging period cannot exceed four weeks or the lower of the two
  Quote: "an employer shall pay an employee overtime pay of at least one and one-half times his or her regular rate for each hour of work in excess of 44 hours in each work week"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Yes, the employer and employee may agree to average hours over separate, non-overlapping, contiguous periods of two or more consecutive weeks, subject to the statutory requirements and a maximum of four weeks or the shorter period specified in the agreement.

**Key facts:**
- [ON] Employer and employee must agree → **Correct**
- [ON] Periods must be separate, non-overlapping, and contiguous → **Missing**
- [ON] Averaged over 2 to 4 weeks (or the shorter period specified in the agreement) → **Partial** — 4-week maximum given; 2-week minimum missing
- [ON] Agreement must have start and expiry dates → **Missing**
- [ON] For non-union employees, the agreement expires no more than 2 years after the start date → **Missing**

**Claims:**
- "Overtime at least 1.5 times the regular rate for each hour over 44 a week" → **Supported** | **Supports**
- "Or over an agreed-upon threshold, whichever is lower" → **Unsupported** | **Doesn't support** — invented
- "Hours can be averaged by agreement between employee and employer" → **Supported** | **Supports**
- "The averaging period can't exceed four weeks" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S124 · Q28 · insufficient_evidence

**Question:** Are employees in managerial positions exempt from the daily and weekly overtime requirements in British Columbia?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 39
  Answer: mandatory
  Who it applies to: Employees in managerial positions
  Amount / threshold: 12 hours
  Mandatory?: mandatory
  Quote: "Despite any provision of this Part, an employer must not require or directly or indirectly allow an employee to work excessive hours or hours detrimental to the employee's health or safety."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 37, 40): Cannot be determined from the Acts in the knowledge base.
- Abstain (British Columbia): the BC Act does not address a manager exclusion; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Sections 37 and 40 set out averaging agreements and general overtime rules → **Missing**
- [BC] The BC Act does not establish a managerial exemption; occupation-specific exclusions are in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- "An employer must not require excessive hours or hours detrimental to health or safety" → **Supported** | **Supports** — s.39
- "Employees in managerial positions are covered by a 12-hour rule" → **Unsupported** | **Doesn't support** — definitive answer on an abstain question

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S125 · Q10 · direct_extraction

**Question:** What is the statutory deadline for paying vacation pay to a BC employee before their annual vacation begins?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 58
  Answer: entitling the employee to the vacation pay
  Who it applies to: after 5 years of employment
  Amount / threshold: 6% of the employee's total wages during the year of employment
  Mandatory?: mandatory
  Quote: "An employer must pay an employee the following amount of vacation pay: after 5 calendar days of employment, at least 4% of the employee's total wages during the year of employment entitling the employee to the vacation pay; after 5 consecutive years of employment, at least 6% of the employee's total wages during the year of employment entitling the employee to the vacation pay."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 58): Vacation pay must be paid at least seven days before the beginning of the employee's annual vacation, unless it is paid on scheduled paydays under a written agreement or collective agreement.

**Key facts:**
- [BC] Payment at least 7 days before vacation → **Missing** — answers the rates
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**

**Claims:**
- "6% of total wages after 5 years; 4% after 5 calendar days" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S126 · Q26 · dates_thresholds

**Question:** What are the daily and weekly overtime thresholds in BC for an employee who is not working under an averaging agreement?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 207(1) and 207(2)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 8 hours
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 40): Daily overtime begins after eight hours, with double time after 12 hours. Weekly overtime begins after 40 hours, with only the first eight hours worked each day counted toward the weekly calculation.

**Key facts:**
- [BC] Daily threshold: 8 hours → **Missing**
- [BC] Double-time threshold: 12 hours → **Missing**
- [BC] Weekly threshold: 40 hours → **Missing**
- [BC] Only first 8 hours per day count toward weekly overtime → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S127 · Q25 · dates_thresholds

**Question:** I started a new job in BC last week. How long do I have to work before I'm entitled to vacation pay?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 58
  Answer: Entitled to vacation pay
  Who it applies to: After 5 consecutive years of employment
  Amount / threshold: At least 6%
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 58): An employee qualifies for at least 4% vacation pay after five calendar days of employment.

**Key facts:**
- [BC] 5 calendar days of employment → **Incorrect** — says after 5 consecutive years
- [BC] Minimum 4% vacation pay → **Incorrect** — says 6%
- [BC] Based on total wages during the relevant year → **Missing**

**Claims:**
- "At least 6% vacation pay after 5 consecutive years" → **Supported** | **Supports** — true rule, wrong tier for a new employee (scored in key facts)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S128 · Q30 · insufficient_evidence

**Question:** I'm a software developer in Vancouver. Do tech workers get overtime in BC?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: Overtime pay
  Who it applies to: Tech workers
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 40): Cannot be determined from the Acts in the knowledge base. Section 40 sets the general overtime rules, but the BC Act's text does not address whether tech workers are excluded.
- Abstain (British Columbia): whether tech workers are excluded from overtime is not addressed in the BC Act; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Section 40 sets general overtime rules (1.5x over 8 hours a day or 40 a week; double over 12 hours a day) → **Missing**
- [BC] The BC Act does not mention technology workers; any occupation-specific exclusion would be in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- "Tech workers are entitled to overtime pay" → **Unsupported** | **Invalid** — definitive answer on an abstain question

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S129 · Q08 · direct_extraction

**Question:** I'm working a 10-hour shift in BC today. Should the last couple of hours be paid at a higher rate?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 37
  Answer: 1 1/2 times the employee's regular wage
  Who it applies to: Employee
  Amount / threshold: more than 40 hours
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): If the employee is not working under an averaging agreement, hours beyond eight in a day must be paid at 1.5 times the regular wage.

**Key facts:**
- [BC] Hours over 8 a day are paid at 1.5 times the regular wage → **Missing** — only the 40-hour weekly rule
- [BC] No averaging agreement applies → **Missing**

**Claims:**
- "1.5 times the regular wage for more than 40 hours" → **Supported** | **Supports** — s.37(5) (averaging) / s.40

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S130 · Q13 · cross_jurisdiction_comparison

**Question:** We have staff in Toronto and Vancouver who'd rather bank their overtime and take time off later. Can we do that in both provinces, and do the rules differ?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 22(8)
  Answer: The employer must pay overtime pay for the overtime hours worked in accordance with subsection 11(5) after the end of the employment period
  Who it applies to: Employment ends before the paid time off is taken under subsection (7)
  Mandatory?: mandatory
  Exceptions: Subject to subsections (3.1) and (3.2)
  Quote: "the employer shall pay the employee overtime pay for the overtime hours that were worked in accordance with subsection 11 (5)"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 42(1), 42(3), 42(3.2)
  Answer: Employer may establish a time bank for overtime wages instead of payment
  Who it applies to: Written request from the employee
  Mandatory?: mandatory
  Exceptions: The time bank can be used to take time off with pay at a time agreed upon by the employer and the employee
  Quote: "At the written request of an employee"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: unknown
  eligibility: different
```

**Gold:**
- Ontario (s. 22): Yes, if the employer and employee agree. The employee receives 1.5 hours of paid time off for each overtime hour, taken within 3 months of the work week in which it was earned (or within 12 months with the employee's agreement). If employment ends before the time off is taken, overtime pay is owed.
- British Columbia (s. 42): Yes. At the employee's written request, the employer may set up a time bank and credit overtime wages to it at overtime rates. The employee can ask at any time to be paid out, to use the credit for paid time off at an agreed time, or to close the bank. The employer may close it with one month's written notice and must settle it within 6 months. The balance must be paid on termination or when the employee asks to close it.
- Comparison: Different: both allow banking overtime, but Ontario uses an agreement with a 3- or 12-month deadline to take the time off, while BC uses a time bank set up at the employee's written request, with no use-by deadline stated while it is open.

**Key facts:**
- [ON] Requires agreement between employer and employee → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Taken within 3 months, or within 12 months with the employee's agreement → **Missing**
- [ON] Paid out as overtime pay if employment ends first → **Correct**
- [BC] Set up at the employee's written request → **Correct**
- [BC] Overtime credited at overtime rates → **Missing**
- [BC] Employee may request payout, time off, or closing at any time → **Partial** — only time off mentioned, not payout or closing
- [BC] Employer may close with 1 month's written notice and settle within 6 months → **Missing**
- [BC] Balance paid on termination or on the employee's request to close → **Missing**
- [VERDICT] Different: both allow banking overtime; Ontario by agreement with a 3- or 12-month deadline, BC by a time bank at the employee's written request → **Partial** — no valid reason given

**Claims:**
- "Ontario: if employment ends before the time off is taken, the employer must pay overtime pay" → **Supported** | **Supports**
- "BC: the employer may set up a time bank for overtime wages at the employee's written request" → **Supported** | **Supports**
- "BC: banked overtime can be taken as paid time off at an agreed time" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S131 · Q24 · dates_thresholds

**Question:** I started my job in Toronto on March 15, 2025. My manager says I have to use my vacation within 10 months of my vacation year ending. Can I save it and take it over the Christmas holidays this year (2026)?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment standards - Vacation leave
  Answer: The employer must allow employees to take their vacation leave during the period between their last day of work and the end of their vacation year.
  Who it applies to: Employees who have worked at least one month but less than six months before their vacation date.
  Amount / threshold: At least one month but less than six months prior to the end of the vacation year.
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 35, 1): Likely yes, timing-wise. Under the standard vacation entitlement year (which starts on the employee's first day of work), the first year ran March 15, 2025 to March 14, 2026. Vacation for that year must be completed within 10 months after it ends, so by about January 14, 2027, and December 2026 falls inside that window. However, the employer decides when vacation is taken, so the employee can request December but cannot insist. If the employer uses an alternative vacation entitlement year, the dates would be different.

**Key facts:**
- [ON] Deadline is 10 months after the end of the vacation entitlement year → **Missing**
- [ON] Standard vacation entitlement year starts on the employee's first day of employment → **Missing**
- [ON] First year ended March 14, 2026, so the deadline is about January 14, 2027 → **Missing**
- [ON] December 2026 is within the deadline → **Missing**
- [ON] The employer determines when vacation is taken → **Missing**
- [ON] Dates differ if the employer uses an alternative vacation entitlement year → **Missing**

**Claims:**
- "The employer must allow vacation between the last day of work and the end of the vacation year" → **Unsupported** | **Invalid**
- "Applies to employees with one to six months of service before the vacation" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S132 · Q19 · exceptions

**Question:** Instead of getting my vacation pay all at once, can my employer in Ontario just add it to every paycheque?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 36(4)
  Answer: The employer may pay vacation pay at a time agreed upon by both parties
  Who it applies to: Employer and employee agree to payment at a specific time
  Mandatory?: optional
  Quote: "the employer may pay the employee vacation pay at a time set out in an agreement that the employee has made with the employer"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 36): Only if the employee has agreed to it and the vacation pay is shown separately, either on the wage statement for each pay period or on a separate statement given at the same time. Otherwise the default is a lump sum before the vacation starts.

**Key facts:**
- [ON] Requires an agreement between the employee and employer → **Correct**
- [ON] Vacation pay shown separately on the wage statement, or on a separate statement provided at the same time → **Missing**
- [ON] Default is a lump sum before vacation (s. 36(1)) → **Missing**

**Claims:**
- "The employer may pay vacation pay at a time agreed with the employee" → **Supported** | **Supports** — s.36(4)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S133 · Q29 · insufficient_evidence

**Question:** My sister works in Calgary and I work in Toronto. We've both been at our jobs for 2 years. Do we get the same vacation pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 36(2), 36(4)
  Answer: The employer may pay the vacation pay on or before the pay day for the period when the vacation falls
  Who it applies to: Employer pays wages according to subsection 11 (4) or the employee doesn't take their vacation in complete weeks
  Mandatory?: optional
  Exceptions: If the employee is represented by a trade union and the employer contributes to a multi-employer vacation benefit plan
  Quote: "the employer may pay the employee his or her vacation pay on or before the pay day for the period in which the vacation falls"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

ALBERTA: not covered. This tool only includes the Ontario and British Columbia Employment Standards Acts, so it cannot answer for this province.
```

**Gold:**
- Ontario (s. 35.2): An Ontario employee with less than five years of employment is entitled to vacation pay of at least 4% of wages, excluding vacation pay, earned during the relevant period.
- Abstain (Alberta): Alberta legislation is not in the knowledge base. The system should answer for Ontario and say it cannot speak to Alberta.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing**

**Claims:**
- "Ontario: vacation pay may be paid on or before the pay day for the period in which the vacation falls, if wages are paid under s.11(4) or vacation isn't taken in complete weeks" → **Supported** | **Supports**
- "Exception if the employee has a union and the employer contributes to a multi-employer vacation plan" → **Supported** | **Doesn't support** — s.39, cited s.36

**Abstention:** **1**   **False abstention:** **no**

**Reviewed:** yes

---

## S134 · Q04 · direct_extraction

**Question:** What is the minimum vacation pay percentage for an Ontario employee with at least five years of employment?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 35.2
  Answer: Vacation pay is at least 4% of wages for periods less than five years, or 6% for those five or more years
  Who it applies to: Employee earns vacation pay and has at least five years of employment
  Amount / threshold: At least 4% of wages for periods less than five years, or 6% for those five or more years
  Mandatory?: mandatory
  Exceptions: Employers are required to provide at least three weeks of vacation after each vacation entitlement year that ends on or after December 31, 2017
  Quote: "if the employee’s period of employment is five years or more"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 35.2): The employee must receive vacation pay equal to at least 6% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 6% vacation pay → **Correct**
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- "Vacation pay is at least 4% under five years, 6% at five years or more" → **Supported** | **Supports**
- "At least three weeks of vacation after each vacation entitlement year (5+ years)" → **Supported** | **Doesn't support** — true (s.33) but cited to s.35.2; listed as an 'exception'

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S135 · Q05 · direct_extraction

**Question:** I work in Toronto and sometimes end up doing 48 hours a week. When should I start getting extra pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 18
  Answer: At least 24 consecutive hours free from work per work week or at least 48 consecutive hours per two consecutive work weeks
  Who it applies to: Employer gives employees a minimum of 11 consecutive hours free from work each day
  Amount / threshold: At least 24 consecutive hours in every work week or at least 48 consecutive hours in every two consecutive work weeks
  Mandatory?: mandatory
  Exceptions: Does not apply to an employee on call and called in
  Quote: "An employer shall give an employee a period of at least 11 consecutive hours free from performing work in each day"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Overtime pay is required for hours worked beyond 44 in a work week (unless a different threshold is prescribed by regulation), at a minimum of 1.5 times the employee's regular rate.

**Key facts:**
- [ON] Weekly overtime threshold is 44 hours → **Missing** — answers rest periods
- [ON] Overtime rate is at least 1.5 times the regular rate → **Missing**

**Claims:**
- "At least 24 consecutive hours off each work week, or 48 in every two consecutive work weeks" → **Supported** | **Supports**
- "At least 11 consecutive hours free from work each day" → **Supported** | **Supports**
- "The daily rest rule does not apply to an employee on call and called in" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S136 · Q07 · direct_extraction

**Question:** My boss in BC says my vacation pay will be lower this year because I got a bonus. Is that allowed?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: Entitled to vacation pay based on hours worked and applicable rates
  Who it applies to: Employees who receive bonuses
  Amount / threshold: Higher than usual due to bonus
```

**Gold:**
- British Columbia (s. 59): No. A BC employer must not reduce an employee's annual vacation or vacation pay because the employee was paid a bonus.

**Key facts:**
- [BC] Cannot reduce vacation or vacation pay because of a bonus → **Missing**

**Claims:**
- "Vacation pay is higher than usual because of the bonus" → **Unsupported** | **Invalid** — the Act says nothing like this; implies the opposite of s.59

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S137 · Q20 · exceptions

**Question:** How must an employer calculate vacation entitlement for an Ontario employee during a stub period created by an alternative vacation entitlement year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)(a)
  Answer: Employer must calculate the vacation entitlement as if it were a full year
  Who it applies to: The stub period is created by an alternative vacation entitlement year
  Mandatory?: mandatory
  Quote: "the stub period is calculated as if it were a full year"
```

**Gold:**
- Ontario (s. 34): The employer must calculate the ratio of the stub period to 12 months and apply it to the employee's applicable two-week or three-week vacation entitlement, using a separate calculation for employees without a regular work week.

**Key facts:**
- [ON] Calculate stub-period-to-12-month ratio → **Incorrect** — says calculate as if it were a full year
- [ON] Less than 5 years: use 2 weeks as the base → **Missing**
- [ON] 5 years or more: use 3 weeks as the base → **Missing**
- [ON] Employees without a regular work week use average weekly working days → **Missing**

**Claims:**
- "Vacation for a stub period is calculated as if it were a full year" → **Unsupported** | **Doesn't support** — invented quote; s.34 uses a pro-rated ratio

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S138 · Q07 · direct_extraction

**Question:** My boss in BC says my vacation pay will be lower this year because I got a bonus. Is that allowed?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 59
  Answer: Entitled to vacation pay
  Who it applies to: Yes
  Amount / threshold: No specific percentage mentioned
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 59): No. A BC employer must not reduce an employee's annual vacation or vacation pay because the employee was paid a bonus.

**Key facts:**
- [BC] Cannot reduce vacation or vacation pay because of a bonus → **Missing** — only 'Entitled to vacation pay … Yes'

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S139 · Q28 · insufficient_evidence

**Question:** Are employees in managerial positions exempt from the daily and weekly overtime requirements in British Columbia?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 37(7)
  Answer: Only the first 12 hours of the day are counted towards the total weekly hours, regardless of the number of days worked
  Amount / threshold: First 12 hours of the day count towards the total weekly hours
  Mandatory?: optional
  Quote: "(a) only the first 12 hours worked by the employee in each day are counted"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 37, 40): Cannot be determined from the Acts in the knowledge base.
- Abstain (British Columbia): the BC Act does not address a manager exclusion; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Sections 37 and 40 set out averaging agreements and general overtime rules → **Partial** — only the s.37 averaging rule
- [BC] The BC Act does not establish a managerial exemption; occupation-specific exclusions are in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- "Under an averaging agreement, only the first 12 hours worked each day count toward weekly hours" → **Supported** | **Supports** — s.37(7); doesn't address managers

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S140 · Q09 · direct_extraction

**Question:** Can a BC employer use a single common date to calculate annual vacation entitlement for all of its employees?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 22(1)(a)
  Answer: Annual vacation entitlement
  Who it applies to: Employees
  Amount / threshold: 100 hours
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 60): Yes. An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58, as long as this does not reduce any employee's rights under those sections.

**Key facts:**
- [BC] A common date for all employees is permitted → **Missing**
- [BC] Must not reduce any employee's rights under those sections → **Missing**

**Claims:**
- "Annual vacation entitlement is 100 hours" → **Unsupported** | **Doesn't support**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S141 · Q15 · cross_jurisdiction_comparison

**Question:** If someone works 45 hours in a week, would they get overtime in Toronto and Vancouver, or does it depend on where they work?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Overtime - Overtime pay
  Answer: At least one hour of overtime must be worked within each seven-day period
  Who it applies to: Work more than 48 hours per week
  Amount / threshold: More than 48 hours in a week
  Exceptions: The employer may choose to apply different rules for overtime in different locations

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The retrieved law does not state this; it may be set out in regulations, which this tool does not include.

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 22): Ontario's general weekly overtime threshold is 44 hours, so hours beyond 44 qualify for overtime at a minimum of 1.5 times the regular rate.
- British Columbia (s. 40): BC's weekly overtime threshold is 40 hours, with hours beyond 40 paid at 1.5 times the regular wage. Daily overtime also applies to any day over 8 hours.
- Comparison: Different: Ontario pays overtime only for the hour over 44. In BC overtime is owed, but whether it comes from the weekly rule (over 40) or the daily rule (over 8 a day) depends on how the hours fall across the days.

**Key facts:**
- [ON] 44-hour weekly threshold → **Incorrect** — says over 48 hours
- [ON] At least 1.5 times the regular rate → **Missing**
- [BC] 40-hour weekly threshold → **Missing**
- [BC] 1.5 times the regular wage → **Missing**
- [BC] Daily overtime may also apply for any day over 8 hours → **Missing**
- [VERDICT] Different: Ontario pays overtime only for the hour over 44; in BC overtime is owed (weekly over 40 or daily over 8) → **Missing** — verdict unknown

**Claims:**
- "Ontario: overtime for work over 48 hours a week" → **Unsupported** | **Invalid**
- "The employer may apply different overtime rules in different locations" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S142 · Q18 · cross_jurisdiction_comparison

**Question:** Compare the vacation pay payment-timing requirements in Ontario and BC.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: Paid
  Who it applies to: Employee
  Amount / threshold: Pay day for that period
  Mandatory?: mandatory
  Quote: "The employer may pay the employee vacation pay that accrues during a pay period on the pay day for that period if the employee has made an agreement with the employer that it may be paid in that manner and, (a) the statement of wages provided for that period under subsection 12 (1) sets out, in addition to the information required by that subsection, the amount of vacation pay that is being paid separately from the amount of other wages that is being paid; or (b) a separate statement setting out the amount of vacation pay that is being paid is provided to the employee at the same time that the statement of wages is provided under subsection 12 (1)."
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 58
  Answer: entitling the employee to the vacation pay
  Who it applies to: after 5 years of employment
  Amount / threshold: 6% of the employee's total wages during the year of employment
  Mandatory?: mandatory
  Exceptions: N; o; t;  ; s; p; e; c; i; f; i; e; d;  ; i; n;  ; t; h; e;  ; e; x; c; e; r; p; t
  Quote: "An employer must pay an employee the following amount of vacation pay: after 5 years of employment, at least 6% of the employee's total wages during the year of employment entitling the employee to the vacation pay."
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 36): Ontario requires vacation pay to be paid in a lump sum before the employee begins vacation by default. It may instead be paid each pay period if the employee agrees and the vacation pay is shown separately (other alternatives also exist, such as an agreed time).
- British Columbia (s. 58): BC requires vacation pay at least seven days before vacation begins, unless scheduled-payday payment is agreed to in writing or provided by a collective agreement.
- Comparison: Different: Ontario's default is a lump sum before vacation (with alternatives: payday, each pay period by agreement, or an agreed time); BC's default is at least 7 days before vacation, or on scheduled paydays if agreed in writing or by collective agreement.

**Key facts:**
- [ON] General rule is lump-sum payment before vacation → **Missing**
- [ON] Payment during each pay period requires an agreement and separate identification of vacation pay → **Correct** — in the quote (s.36(3))
- [BC] Payment at least 7 days before vacation → **Missing**
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**
- [VERDICT] Different: Ontario default lump sum before vacation; BC at least 7 days before, or scheduled paydays by written/collective agreement → **Partial** — 'different' for the wrong reason

**Claims:**
- "Ontario: vacation pay may be paid on each pay day if the employee agrees and it is shown separately" → **Supported** | **Invalid** — 'section' is the Act name
- "BC: at least 6% of total wages after 5 years" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S143 · Q21 · exceptions

**Question:** My employer in Ontario wants to average my hours over a few weeks instead of paying overtime every time I go over 44 hours. Are they allowed to do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 29(1)(a)
  Answer: Entitlement to overtime pay
  Who it applies to: Employers
  Amount / threshold: 44 hours
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 22): Yes, the employer and employee may agree to average hours over separate, non-overlapping, contiguous periods of two or more consecutive weeks, subject to the statutory requirements and a maximum of four weeks or the shorter period specified in the agreement.

**Key facts:**
- [ON] Employer and employee must agree → **Missing**
- [ON] Periods must be separate, non-overlapping, and contiguous → **Missing**
- [ON] Averaged over 2 to 4 weeks (or the shorter period specified in the agreement) → **Missing**
- [ON] Agreement must have start and expiry dates → **Missing**
- [ON] For non-union employees, the agreement expires no more than 2 years after the start date → **Missing**

**Claims:**
- "Overtime after 44 hours" → **Supported** | **Doesn't support** — s.22, cited s.29

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S144 · Q23 · exceptions

**Question:** I work in Ontario and would rather take time off than get overtime pay. Can my employer let me do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employer's obligations to employees
  Answer: Entitlement to overtime pay
  Who it applies to: All employees
  Amount / threshold: Overtime hours worked
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 22): Yes. The employer and employee may agree to paid time off at one and a half hours for each overtime hour worked. The time off must generally be taken within three months, or within 12 months if the employee agrees.

**Key facts:**
- [ON] Employer and employee must agree → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Normally taken within 3 months → **Missing**
- [ON] May be taken within 12 months with employee agreement → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S145 · Q28 · insufficient_evidence

**Question:** Are employees in managerial positions exempt from the daily and weekly overtime requirements in British Columbia?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 37, 40): Cannot be determined from the Acts in the knowledge base.
- Abstain (British Columbia): the BC Act does not address a manager exclusion; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Sections 37 and 40 set out averaging agreements and general overtime rules → **Missing** — abstained only because extraction failed (invalid JSON), not by judgment
- [BC] The BC Act does not establish a managerial exemption; occupation-specific exclusions are in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- (no claims)

**Abstention:** **1**   **False abstention:** **no**

**Reviewed:** yes

---

## S146 · Q20 · exceptions

**Question:** How must an employer calculate vacation entitlement for an Ontario employee during a stub period created by an alternative vacation entitlement year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Alternative Vacation Entitlement Year
  Answer: Calculation of vacation entitlement
  Who it applies to: All employees
  Amount / threshold: During a stub period
  Mandatory?: Yes
```

**Gold:**
- Ontario (s. 34): The employer must calculate the ratio of the stub period to 12 months and apply it to the employee's applicable two-week or three-week vacation entitlement, using a separate calculation for employees without a regular work week.

**Key facts:**
- [ON] Calculate stub-period-to-12-month ratio → **Missing**
- [ON] Less than 5 years: use 2 weeks as the base → **Missing**
- [ON] 5 years or more: use 3 weeks as the base → **Missing**
- [ON] Employees without a regular work week use average weekly working days → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S147 · Q27 · insufficient_evidence

**Question:** I work on a farm in Ontario. My employer says farm workers don't get overtime. Is that true?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 27(1)(a)
  Answer: Entitlement to overtime pay
  Who it applies to: Farm workers
```

**Gold:**
- Ontario (s. 22): Cannot be determined from the Acts in the knowledge base.
- Abstain (Ontario): s. 22 allows exemptions by regulation, but the regulations that list exempt occupations are not in the knowledge base.

**Key facts:**
- [ON] Explains that overtime exemptions are set by regulation, which is not in the knowledge base, so whether farm workers are exempt can't be determined → **Missing**

**Claims:**
- "Farm workers are entitled to overtime pay" → **Unsupported** | **Doesn't support** — definitive answer on an abstain question

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S148 · Q07 · direct_extraction

**Question:** My boss in BC says my vacation pay will be lower this year because I got a bonus. Is that allowed?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 59
  Answer: Employer must not reduce annual vacation or vacation pay due to bonuses or previous long vacations unless the employee requests an early vacation
  Who it applies to: Employee received a bonus or sick pay, or was previously given a longer annual vacation than the minimum required under section 57
  Mandatory?: optional
  Exceptions: Subsection (1) (b) allows reduction due to the written request of the employee allowing the employee to take an annual vacation in advance
  Quote: "an employer must not reduce an employee's annual vacation or vacation pay because the employee was paid a bonus or sick pay"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 59): No. A BC employer must not reduce an employee's annual vacation or vacation pay because the employee was paid a bonus.

**Key facts:**
- [BC] Cannot reduce vacation or vacation pay because of a bonus → **Partial** — right rule, but the answer line attaches 'unless the employee requests an early vacation' to bonuses too; s.59(2) applies only to (1)(b)

**Claims:**
- "An employer must not reduce annual vacation or vacation pay because of a bonus or sick pay" → **Supported** | **Supports**
- "Or because of a previously longer vacation" → **Supported** | **Supports**
- "Reduction allowed for (1)(b) if the employee asked in writing to take vacation in advance" → **Supported** | **Supports**
- "The rule is optional" → **Unsupported** | **Doesn't support** — wrong 'Mandatory?' label on a question about what is allowed

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S149 · Q02 · direct_extraction

**Question:** I've been at my job in Vancouver for six years now. Do I get any more vacation time than when I started?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 57
  Answer: Annual vacation of at least 2 weeks after 12 consecutive months or 3 weeks after 5 consecutive years
  Who it applies to: Employer has employed the employee for at least 12 consecutive months (subsection 1(1)(a)) or 5 consecutive years (subsection 1(1)(b))
  Amount / threshold: At least 2 weeks after 12 consecutive months or 3 weeks after 5 consecutive years
  Mandatory?: mandatory
  Exceptions: The vacation must be taken within 12 months after the end of the year of employment that entitles the employee
  Quote: "an employer must give an employee an annual vacation of"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 57): Yes. After five consecutive years of employment, the entitlement increases from at least two weeks to at least three weeks of annual vacation.

**Key facts:**
- [BC] At least 3 weeks of annual vacation → **Correct**
- [BC] Up from at least 2 weeks before reaching 5 years → **Correct**
- [BC] 5 consecutive years of employment → **Correct**

**Claims:**
- "At least 2 weeks after 12 consecutive months" → **Supported** | **Supports**
- "At least 3 weeks after 5 consecutive years" → **Supported** | **Supports**
- "The vacation must be taken within 12 months after the year of employment that entitles the employee" → **Supported** | **Supports** — s.57(2); listed as an 'exception'

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S150 · Q30 · insufficient_evidence

**Question:** I'm a software developer in Vancouver. Do tech workers get overtime in BC?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 40): Cannot be determined from the Acts in the knowledge base. Section 40 sets the general overtime rules, but the BC Act's text does not address whether tech workers are excluded.
- Abstain (British Columbia): whether tech workers are excluded from overtime is not addressed in the BC Act; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Section 40 sets general overtime rules (1.5x over 8 hours a day or 40 a week; double over 12 hours a day) → **Missing** — abstained only because extraction failed (invalid JSON), not by judgment
- [BC] The BC Act does not mention technology workers; any occupation-specific exclusion would be in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- (no claims)

**Abstention:** **1**   **False abstention:** **no**

**Reviewed:** yes

---

## S151 · Q05 · direct_extraction

**Question:** I work in Toronto and sometimes end up doing 48 hours a week. When should I start getting extra pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 13(1)(a), 13(1)(b)
  Answer: Extra pay for each hour worked over 40
  Who it applies to: Worked more than 40 hours per week
  Amount / threshold: More than 40 hours per week
  Mandatory?: mandatory
  Quote: "The employer must give the employee notice that it will be paying overtime"
```

**Gold:**
- Ontario (s. 22): Overtime pay is required for hours worked beyond 44 in a work week (unless a different threshold is prescribed by regulation), at a minimum of 1.5 times the employee's regular rate.

**Key facts:**
- [ON] Weekly overtime threshold is 44 hours → **Incorrect** — says over 40 hours
- [ON] Overtime rate is at least 1.5 times the regular rate → **Missing**

**Claims:**
- "Extra pay for each hour worked over 40 hours a week" → **Unsupported** | **Doesn't support** — s.13 is about deductions
- "The employer must give the employee notice that it will be paying overtime" → **Unsupported** | **Doesn't support** — invented quote

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S152 · Q12 · cross_jurisdiction_comparison

**Question:** Compare the deadline for an employee to take earned vacation in Ontario and British Columbia.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 33(1)
  Answer: Vacation of at least two weeks after each vacation entitlement year, or at least three weeks after each vacation entitlement year
  Who it applies to: Employee's period of employment is less than five years or five years or more
  Amount / threshold: At least two weeks after each vacation entitlement year, or at least three weeks after each vacation entitlement year
  Mandatory?: mandatory
  Exceptions: If the employee’s period of employment is less than five years, the vacation must be a two-week period or two periods of one week each, unless the employee requests in writing that the vacation be taken in shorter periods and the employer agrees to that request
  Quote: "An employer shall give an employee a vacation of"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 57
  Answer: At least 2 weeks, after 12 consecutive months; at least 3 weeks, after 5 consecutive years
  Who it applies to: After 12 consecutive months of employment, or after 5 consecutive years of employment
  Amount / threshold: At least 2 weeks after 12 consecutive months; at least 3 weeks after 5 consecutive years
  Mandatory?: mandatory
  Quote: "after 12 consecutive months of employment"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 35): Vacation must be completed no later than 10 months after the end of the vacation entitlement year for which it is given.
- British Columbia (s. 57): Annual vacation must be taken within 12 months after completing the year of employment that entitles the employee to it.
- Comparison: Different: 10 months in Ontario vs. 12 months in BC.

**Key facts:**
- [ON] No later than 10 months after the end of the vacation entitlement year → **Missing** — gives amounts, not the deadline
- [BC] Within 12 months after completing the entitling year of employment → **Missing** — gives amounts
- [VERDICT] Different: 10 months in Ontario vs. 12 months in BC → **Partial** — 'different' for the wrong reason

**Claims:**
- "Ontario: at least two weeks (under 5 years) or three weeks (5+ years) after each vacation entitlement year" → **Supported** | **Supports**
- "Ontario: under 5 years, vacation is taken as one two-week or two one-week periods unless the employee asks in writing and the employer agrees" → **Supported** | **Doesn't support** — s.35, cited as s.33(1)
- "BC: at least 2 weeks after 12 months, 3 weeks after 5 years" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S153 · Q24 · dates_thresholds

**Question:** I started my job in Toronto on March 15, 2025. My manager says I have to use my vacation within 10 months of my vacation year ending. Can I save it and take it over the Christmas holidays this year (2026)?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 33(1)
  Answer: Vacation entitlement
  Who it applies to: Employee
  Amount / threshold: Five years or more
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 35, 1): Likely yes, timing-wise. Under the standard vacation entitlement year (which starts on the employee's first day of work), the first year ran March 15, 2025 to March 14, 2026. Vacation for that year must be completed within 10 months after it ends, so by about January 14, 2027, and December 2026 falls inside that window. However, the employer decides when vacation is taken, so the employee can request December but cannot insist. If the employer uses an alternative vacation entitlement year, the dates would be different.

**Key facts:**
- [ON] Deadline is 10 months after the end of the vacation entitlement year → **Missing**
- [ON] Standard vacation entitlement year starts on the employee's first day of employment → **Missing**
- [ON] First year ended March 14, 2026, so the deadline is about January 14, 2027 → **Missing**
- [ON] December 2026 is within the deadline → **Missing**
- [ON] The employer determines when vacation is taken → **Missing**
- [ON] Dates differ if the employer uses an alternative vacation entitlement year → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S154 · Q21 · exceptions

**Question:** My employer in Ontario wants to average my hours over a few weeks instead of paying overtime every time I go over 44 hours. Are they allowed to do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 13(1)(a)
  Answer: The employer must pay overtime only when the total number of hours worked during the averaging period exceeds 48 hours
  Who it applies to: Employer and employee agree on averaging hours over a period of at least two consecutive weeks
  Amount / threshold: Total hours exceed 48 hours
  Mandatory?: mandatory
  Quote: "the employer and the employee agree on averaging hours over a period of at least two consecutive weeks"
```

**Gold:**
- Ontario (s. 22): Yes, the employer and employee may agree to average hours over separate, non-overlapping, contiguous periods of two or more consecutive weeks, subject to the statutory requirements and a maximum of four weeks or the shorter period specified in the agreement.

**Key facts:**
- [ON] Employer and employee must agree → **Correct**
- [ON] Periods must be separate, non-overlapping, and contiguous → **Missing**
- [ON] Averaged over 2 to 4 weeks (or the shorter period specified in the agreement) → **Partial** — 2-week minimum given; 4-week maximum missing
- [ON] Agreement must have start and expiry dates → **Missing**
- [ON] For non-union employees, the agreement expires no more than 2 years after the start date → **Missing**

**Claims:**
- "Overtime is owed only when total hours in the averaging period exceed 48" → **Unsupported** | **Doesn't support**
- "Employer and employee agree to average hours over at least two consecutive weeks" → **Supported** | **Doesn't support** — s.22(2), cited s.13

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S155 · Q17 · cross_jurisdiction_comparison

**Question:** I want to split my vacation into single days instead of whole weeks. Can I do that in Ontario? What about in BC?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 100.1(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 10 hours
  Mandatory?: mandatory
  Quote: "Section 100.1(1)(a) of the Employment Standards Act, 2000 provides that an employee is entitled to a minimum of 10 hours of paid sick leave for each 24 hours of continuous employment."

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 35): By default, Ontario vacation is taken in whole weeks (a two-week period or two one-week periods; for 5+ years, combinations of one-, two-, or three-week periods). Shorter periods are allowed only if the employee requests them in writing and the employer agrees.
- British Columbia (s. 57): BC requires the employer to allow an employee to take annual vacation in periods of one or more weeks. Section 57 does not address periods shorter than a week.
- Comparison: Similar: both are built around whole weeks. Ontario allows shorter periods by written request plus employer agreement; BC requires the employer to allow periods of one week or more.

**Key facts:**
- [ON] Default is whole-week periods → **Missing**
- [ON] Shorter periods only if the employee requests in writing and the employer agrees → **Missing**
- [BC] Employer must allow vacation in periods of one or more weeks → **Missing**
- [BC] Periods shorter than a week are not addressed in s. 57 → **Missing**
- [VERDICT] Similar: both built around whole weeks; Ontario allows shorter periods by written request plus employer agreement → **Missing** — verdict unknown

**Claims:**
- "BC: a minimum of 10 hours of paid sick leave for each 24 hours of continuous employment" → **Unsupported** | **Invalid** — invented quote; no s.100.1

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S156 · Q03 · direct_extraction

**Question:** I work in Ontario and have only been here for two years. How much vacation pay am I owed?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: The employer must provide vacation pay to eligible employees upon termination of employment.
  Who it applies to: All employees who have worked at least one full month within the previous year.
  Amount / threshold: Two months' notice period before termination.
  Mandatory?: Entitlement
```

**Gold:**
- Ontario (s. 35.2): The employee is entitled to vacation pay of at least 4% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing**
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- "The employer must pay vacation pay when employment ends" → **Supported** | **Invalid** — consistent with ON s.38; the 'section' is the Act name
- "Applies to employees who worked at least one full month in the previous year" → **Unsupported** | **Invalid**
- "A two-month notice period before termination" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S157 · Q26 · dates_thresholds

**Question:** What are the daily and weekly overtime thresholds in BC for an employee who is not working under an averaging agreement?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 40
  Answer: Employer must pay 1 1/2 times the regular wage for the time over 8 hours, and double the regular wage for any time over 12 hours
  Who it applies to: Employee works over 8 hours a day but not under an averaging agreement
  Amount / threshold: Over 8 hours a day, and over 12 hours if not under an averaging agreement
  Mandatory?: mandatory
  Quote: "An employer must pay an employee who works over 8 hours a day, and is not working under an averaging agreement"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 40): Daily overtime begins after eight hours, with double time after 12 hours. Weekly overtime begins after 40 hours, with only the first eight hours worked each day counted toward the weekly calculation.

**Key facts:**
- [BC] Daily threshold: 8 hours → **Correct**
- [BC] Double-time threshold: 12 hours → **Correct**
- [BC] Weekly threshold: 40 hours → **Missing**
- [BC] Only first 8 hours per day count toward weekly overtime → **Missing**

**Claims:**
- "1.5 times the regular wage for time over 8 hours a day" → **Supported** | **Supports**
- "Double the regular wage for time over 12 hours" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S158 · Q26 · dates_thresholds

**Question:** What are the daily and weekly overtime thresholds in BC for an employee who is not working under an averaging agreement?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act
  Answer: Daily and weekly overtime pay
  Who it applies to: All employees
  Amount / threshold: {'daily': 8, 'weekly': 40}
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 40): Daily overtime begins after eight hours, with double time after 12 hours. Weekly overtime begins after 40 hours, with only the first eight hours worked each day counted toward the weekly calculation.

**Key facts:**
- [BC] Daily threshold: 8 hours → **Correct**
- [BC] Double-time threshold: 12 hours → **Missing**
- [BC] Weekly threshold: 40 hours → **Correct**
- [BC] Only first 8 hours per day count toward weekly overtime → **Missing**

**Claims:**
- "Daily overtime after 8 hours, weekly after 40" → **Supported** | **Invalid** — 'section' is the Act name

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S159 · Q14 · cross_jurisdiction_comparison

**Question:** We've got employees in Toronto and Vancouver who've both been here for six years. Do they get the same vacation pay percentage?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 14(3)(a)
  Answer: Vacation pay is calculated as 5% of their annual earnings
  Who it applies to: Employees have worked at least one year each in two different locations within the province
  Amount / threshold: At least one year each in two different locations within the province
  Mandatory?: mandatory
  Quote: "Vacation pay is calculated as five percent of the employee's annual earnings"

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 35.2): At least 6% of wages, excluding vacation pay, for employees with five or more years of employment.
- British Columbia (s. 58): At least 6% of total wages during the relevant year after five consecutive years of employment.
- Comparison: Same: both at least 6% after five years. The wage base is worded differently (Ontario: wages excluding vacation pay earned in the period; BC: total wages in the entitling year).

**Key facts:**
- [ON] Minimum 6% → **Incorrect** — says 5%
- [ON] Excludes vacation pay from wages → **Missing**
- [BC] Minimum 6% → **Missing**
- [BC] Based on total wages during the relevant year → **Missing**
- [VERDICT] Same: both at least 6% after five years → **Missing** — verdict unknown

**Claims:**
- "Ontario: vacation pay is 5% of annual earnings" → **Unsupported** | **Doesn't support** — invented quote
- "Ontario: applies to employees with a year in each of two locations" → **Unsupported** | **Doesn't support**

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S160 · Q29 · insufficient_evidence

**Question:** My sister works in Calgary and I work in Toronto. We've both been at our jobs for 2 years. Do we get the same vacation pay?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: They should receive the same vacation pay as their coworkers who have also worked for 2 years.
  Who it applies to: Both employees have worked for 2 years.
  Amount / threshold: The exact amount of vacation pay may vary based on individual circumstances such as length of service and company policies.
  Mandatory?: mandatory

ALBERTA: not covered. This tool only includes the Ontario and British Columbia Employment Standards Acts, so it cannot answer for this province.
```

**Gold:**
- Ontario (s. 35.2): An Ontario employee with less than five years of employment is entitled to vacation pay of at least 4% of wages, excluding vacation pay, earned during the relevant period.
- Abstain (Alberta): Alberta legislation is not in the knowledge base. The system should answer for Ontario and say it cannot speak to Alberta.

**Key facts:**
- [ON] Minimum 4% vacation pay → **Missing**

**Claims:**
- "Both employees (Toronto and Calgary) should receive the same vacation pay" → **Unsupported** | **Invalid** — claim about a jurisdiction outside the knowledge base
- "The amount may vary with company policies" → **Unsupported** | **Invalid**

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S161 · Q21 · exceptions

**Question:** My employer in Ontario wants to average my hours over a few weeks instead of paying overtime every time I go over 44 hours. Are they allowed to do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Overtime and work hours
  Answer: Allowing employees to be paid at least $16 per hour for all hours worked over 44 hours in a week
  Who it applies to: Employees who have worked more than 44 hours in one week
  Amount / threshold: $16 per hour
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 22): Yes, the employer and employee may agree to average hours over separate, non-overlapping, contiguous periods of two or more consecutive weeks, subject to the statutory requirements and a maximum of four weeks or the shorter period specified in the agreement.

**Key facts:**
- [ON] Employer and employee must agree → **Missing**
- [ON] Periods must be separate, non-overlapping, and contiguous → **Missing**
- [ON] Averaged over 2 to 4 weeks (or the shorter period specified in the agreement) → **Missing**
- [ON] Agreement must have start and expiry dates → **Missing**
- [ON] For non-union employees, the agreement expires no more than 2 years after the start date → **Missing**

**Claims:**
- "At least $16 an hour for hours over 44 in a week" → **Unsupported** | **Invalid**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S162 · Q08 · direct_extraction

**Question:** I'm working a 10-hour shift in BC today. Should the last couple of hours be paid at a higher rate?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 20(1)(a)
  Answer: Minimum wage
  Who it applies to: Employee
  Amount / threshold: 10 hours
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 40): If the employee is not working under an averaging agreement, hours beyond eight in a day must be paid at 1.5 times the regular wage.

**Key facts:**
- [BC] Hours over 8 a day are paid at 1.5 times the regular wage → **Missing**
- [BC] No averaging agreement applies → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S163 · Q01 · direct_extraction

**Question:** I've been working in Toronto for about 3 years. How much paid time off am I supposed to get each year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employer's Obligations
  Answer: Paid vacation leave
  Who it applies to: All employees
  Amount / threshold: 3 years of continuous service
  Mandatory?: Yes
```

**Gold:**
- Ontario (s. 33): At least two weeks of vacation each year (the two-week level applies to employees with less than five years of employment).

**Key facts:**
- [ON] At least 2 weeks of vacation → **Missing**

**Claims:**
- "Paid vacation applies once an employee has 3 years of continuous service" → **Unsupported** | **Invalid** — invented threshold; 'Employer's Obligations' is not a section

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S164 · Q02 · direct_extraction

**Question:** I've been at my job in Vancouver for six years now. Do I get any more vacation time than when I started?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 57): Yes. After five consecutive years of employment, the entitlement increases from at least two weeks to at least three weeks of annual vacation.

**Key facts:**
- [BC] At least 3 weeks of annual vacation → **Missing**
- [BC] Up from at least 2 weeks before reaching 5 years → **Missing**
- [BC] 5 consecutive years of employment → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S165 · Q23 · exceptions

**Question:** I work in Ontario and would rather take time off than get overtime pay. Can my employer let me do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 22(7)
  Answer: Paid time off work for each hour of overtime worked
  Who it applies to: Employee and employer agree to compensate by paid time off instead of overtime pay
  Amount / threshold: One and one-half hours of paid time off per hour of overtime worked
  Mandatory?: mandatory
  Exceptions: The paid time off must be taken within three months of the work week in which the overtime was earned or, with the employee's agreement, within 12 months
  Quote: "the paid time off is taken within three months of the work week in which the overtime was earned"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Yes. The employer and employee may agree to paid time off at one and a half hours for each overtime hour worked. The time off must generally be taken within three months, or within 12 months if the employee agrees.

**Key facts:**
- [ON] Employer and employee must agree → **Correct**
- [ON] 1.5 hours of paid time off per overtime hour → **Correct**
- [ON] Normally taken within 3 months → **Correct**
- [ON] May be taken within 12 months with employee agreement → **Correct**

**Claims:**
- "Employer and employee may agree to paid time off instead of overtime pay" → **Supported** | **Supports**
- "One and a half hours of paid time off for each overtime hour" → **Supported** | **Supports**
- "Taken within three months of the work week, or within 12 months with the employee's agreement" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S166 · Q01 · direct_extraction

**Question:** I've been working in Toronto for about 3 years. How much paid time off am I supposed to get each year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 28
  Answer: Entitlement
  Who it applies to: Employees
  Amount / threshold: 100 hours
  Mandatory?: mandatory
  Quote: "The Employment Standards Act, 2000 (Ontario) requires employers to provide employees with a minimum of 100 hours of paid sick leave per year."
```

**Gold:**
- Ontario (s. 33): At least two weeks of vacation each year (the two-week level applies to employees with less than five years of employment).

**Key facts:**
- [ON] At least 2 weeks of vacation → **Missing** — answers sick leave

**Claims:**
- "Employers must provide a minimum of 100 hours of paid sick leave per year" → **Unsupported** | **Doesn't support** — invented rule and quote; s.28 is about public holidays

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S167 · Q06 · direct_extraction

**Question:** I just finished my first year working in BC. Am I supposed to get two weeks off now?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. Employment Standards Act (British Columbia)
  Answer: mandatory
  Who it applies to: two weeks off
  Amount / threshold: up to 16 consecutive days of employment
  Mandatory?: mandatory
  Quote: "An employee may begin a leave under this section no earlier than the first day of the week in which the period under subsection (2) begins."
  ⚠ Cited section Employment Standards Act (British Columbia) was not among the retrieved sections.
```

**Gold:**
- British Columbia (s. 57): Yes. After 12 consecutive months of employment, an employee is entitled to at least two weeks of annual vacation.

**Key facts:**
- [BC] At least 2 weeks of annual vacation → **Missing** — 'two weeks off' appears only as a garbled field value

**Claims:**
- "The threshold is up to 16 consecutive days of employment" → **Unsupported** | **Invalid**
- "An employee may begin the leave no earlier than the first day of the week in which the period begins" → **Supported** | **Invalid** — s.52.1(4) text, but the 'section' is the Act name

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S168 · Q21 · exceptions

**Question:** My employer in Ontario wants to average my hours over a few weeks instead of paying overtime every time I go over 44 hours. Are they allowed to do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 22
  Answer: Overtime pay
  Who it applies to: Employee
  Amount / threshold: 44 hours
  Mandatory?: mandatory
  Quote: "Subject to subsections (3.1) and (3.2), an averaging agreement is not valid unless it provides for a start date and an expiry date."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Yes, the employer and employee may agree to average hours over separate, non-overlapping, contiguous periods of two or more consecutive weeks, subject to the statutory requirements and a maximum of four weeks or the shorter period specified in the agreement.

**Key facts:**
- [ON] Employer and employee must agree → **Missing**
- [ON] Periods must be separate, non-overlapping, and contiguous → **Missing**
- [ON] Averaged over 2 to 4 weeks (or the shorter period specified in the agreement) → **Missing**
- [ON] Agreement must have start and expiry dates → **Correct** — in the quote
- [ON] For non-union employees, the agreement expires no more than 2 years after the start date → **Missing**

**Claims:**
- "Overtime threshold 44 hours" → **Supported** | **Supports**
- "An averaging agreement is not valid unless it has a start date and an expiry date" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S169 · Q27 · insufficient_evidence

**Question:** I work on a farm in Ontario. My employer says farm workers don't get overtime. Is that true?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000 (Ontario)
  Answer: mandatory
  Who it applies to: farm workers
  Amount / threshold: 44 hours
  Mandatory?: mandatory
  Quote: "If an employee receives premium pay for working on a public holiday, the hours worked shall not be taken into consideration in calculating overtime pay to which the employee may be entitled."
  ⚠ Cited section Employment Standards Act, 2000 (Ontario) was not among the retrieved sections.
```

**Gold:**
- Ontario (s. 22): Cannot be determined from the Acts in the knowledge base.
- Abstain (Ontario): s. 22 allows exemptions by regulation, but the regulations that list exempt occupations are not in the knowledge base.

**Key facts:**
- [ON] Explains that overtime exemptions are set by regulation, which is not in the knowledge base, so whether farm workers are exempt can't be determined → **Missing**

**Claims:**
- "Farm workers are entitled to overtime pay" → **Unsupported** | **Invalid** — implies farm workers get overtime after 44 hours
- "Hours worked on a public holiday with premium pay don't count toward overtime" → **Supported** | **Invalid** — true (s.31), but cited as the Act name

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S170 · Q18 · cross_jurisdiction_comparison

**Question:** Compare the vacation pay payment-timing requirements in Ontario and BC.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 36(3)
  Answer: Employer may pay vacation pay on the pay day for that period, either through a separate statement or a combined statement including the vacation pay
  Who it applies to: Employee has agreed with the employer that vacation pay can be paid in that manner
  Mandatory?: mandatory
  Quote: "the statement of wages provided for that period under subsection 12 (1) sets out, in addition to the information required by that subsection, the amount of vacation pay that is being paid separately from the amount of other wages that is being paid"
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 58
  Answer: At least 4% of total wages for the first 5 calendar days, or 6% for 5 consecutive years
  Who it applies to: Employer must pay vacation pay after 5 calendar days of employment, or after 5 consecutive years of employment
  Amount / threshold: At least 4% of total wages for the first 5 calendar days, or 6% for 5 consecutive years
  Mandatory?: mandatory
  Quote: "at least 4% of the employee's total wages during the year of employment entitling the employee to the vacation pay"
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different
  threshold: unknown
  eligibility: different
```

**Gold:**
- Ontario (s. 36): Ontario requires vacation pay to be paid in a lump sum before the employee begins vacation by default. It may instead be paid each pay period if the employee agrees and the vacation pay is shown separately (other alternatives also exist, such as an agreed time).
- British Columbia (s. 58): BC requires vacation pay at least seven days before vacation begins, unless scheduled-payday payment is agreed to in writing or provided by a collective agreement.
- Comparison: Different: Ontario's default is a lump sum before vacation (with alternatives: payday, each pay period by agreement, or an agreed time); BC's default is at least 7 days before vacation, or on scheduled paydays if agreed in writing or by collective agreement.

**Key facts:**
- [ON] General rule is lump-sum payment before vacation → **Missing**
- [ON] Payment during each pay period requires an agreement and separate identification of vacation pay → **Correct**
- [BC] Payment at least 7 days before vacation → **Missing**
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**
- [VERDICT] Different: Ontario default lump sum before vacation; BC at least 7 days before, or scheduled paydays by written/collective agreement → **Partial** — 'different' for the wrong reason

**Claims:**
- "Ontario: vacation pay may be paid on each pay day if the employee agrees and it is shown separately" → **Supported** | **Supports**
- "BC: at least 4% of total wages for the first 5 calendar days, or 6% for 5 consecutive years" → **Unsupported** | **Doesn't support** — garbles s.58(1)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S171 · Q23 · exceptions

**Question:** I work in Ontario and would rather take time off than get overtime pay. Can my employer let me do that?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 22
  Answer: Overtime pay
  Who it applies to: Employee
  Amount / threshold: 44 hours
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 22): Yes. The employer and employee may agree to paid time off at one and a half hours for each overtime hour worked. The time off must generally be taken within three months, or within 12 months if the employee agrees.

**Key facts:**
- [ON] Employer and employee must agree → **Missing**
- [ON] 1.5 hours of paid time off per overtime hour → **Missing**
- [ON] Normally taken within 3 months → **Missing**
- [ON] May be taken within 12 months with employee agreement → **Missing**

**Claims:**
- "Overtime threshold 44 hours" → **Supported** | **Supports**

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S172 · Q10 · direct_extraction

**Question:** What is the statutory deadline for paying vacation pay to a BC employee before their annual vacation begins?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 22(1)(a)
  Answer: Entitlement
  Who it applies to: Employee
  Amount / threshold: 12 months
  Mandatory?: mandatory
```

**Gold:**
- British Columbia (s. 58): Vacation pay must be paid at least seven days before the beginning of the employee's annual vacation, unless it is paid on scheduled paydays under a written agreement or collective agreement.

**Key facts:**
- [BC] Payment at least 7 days before vacation → **Missing**
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S173 · Q04 · direct_extraction

**Question:** What is the minimum vacation pay percentage for an Ontario employee with at least five years of employment?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 27(1)(a)
  Answer: Minimum vacation pay
  Who it applies to: Employee
  Amount / threshold: 5 years
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 35.2): The employee must receive vacation pay equal to at least 6% of wages earned during the relevant period, excluding vacation pay.

**Key facts:**
- [ON] Minimum 6% vacation pay → **Missing**
- [ON] Vacation pay is excluded from the wage calculation → **Missing**

**Claims:**
- (no claims)

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S174 · Q28 · insufficient_evidence

**Question:** Are employees in managerial positions exempt from the daily and weekly overtime requirements in British Columbia?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. s. 39
  Answer: daily and weekly overtime requirements
  Who it applies to: employees in managerial positions
  Amount / threshold: excessive hours or hours detrimental to the employee's health or safety
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 37, 40): Cannot be determined from the Acts in the knowledge base.
- Abstain (British Columbia): the BC Act does not address a manager exclusion; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Sections 37 and 40 set out averaging agreements and general overtime rules → **Missing**
- [BC] The BC Act does not establish a managerial exemption; occupation-specific exclusions are in the regulations, which are not in the knowledge base → **Missing**

**Claims:**
- "Employees in managerial positions are subject to daily and weekly overtime requirements" → **Unsupported** | **Doesn't support** — definitive answer on an abstain question
- "Employers must not require excessive hours or hours detrimental to health or safety" → **Supported** | **Supports** — s.39

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S175 · Q27 · insufficient_evidence

**Question:** I work on a farm in Ontario. My employer says farm workers don't get overtime. Is that true?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: Overtime pay
  Who it applies to: Farm workers
  Mandatory?: mandatory
```

**Gold:**
- Ontario (s. 22): Cannot be determined from the Acts in the knowledge base.
- Abstain (Ontario): s. 22 allows exemptions by regulation, but the regulations that list exempt occupations are not in the knowledge base.

**Key facts:**
- [ON] Explains that overtime exemptions are set by regulation, which is not in the knowledge base, so whether farm workers are exempt can't be determined → **Missing**

**Claims:**
- "Farm workers are entitled to overtime pay" → **Unsupported** | **Invalid** — definitive answer on an abstain question

**Abstention:** **0**   **False abstention:** **no**

**Reviewed:** yes

---

## S176 · Q16 · cross_jurisdiction_comparison

**Question:** Compare the daily overtime rules in Ontario and BC for employees who work more than eight hours in a day.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 290(1)(a)
  Answer: Entitlement to overtime pay
  Who it applies to: Employees who work more than eight hours in a day
  Amount / threshold: Eight hours
  Mandatory?: mandatory

BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).

COMPARISON: UNKNOWN
  At least one province's answer is not specified in the retrieved law.
```

**Gold:**
- Ontario (s. 22): Ontario's overtime section (s. 22) sets overtime on a weekly basis only: hours over 44 in a work week (or a prescribed threshold). It does not provide for daily overtime.
- British Columbia (s. 40): BC requires 1.5 times regular wages for hours over eight in a day and double wages for hours over 12, unless an averaging agreement applies.
- Comparison: Different: BC has daily overtime (1.5x over 8 hours, double over 12); Ontario has none, only a weekly threshold.

**Key facts:**
- [ON] No daily overtime threshold in s. 22 → **Incorrect** — says overtime after eight hours a day
- [BC] Daily overtime after 8 hours → **Missing**
- [BC] Double time after 12 hours → **Missing**
- [BC] Averaging agreement may affect the calculation → **Missing**
- [VERDICT] Different: BC has daily overtime (1.5x over 8, double over 12); Ontario has none, only weekly → **Missing** — verdict unknown

**Claims:**
- "Ontario: overtime pay for more than eight hours a day" → **Unsupported** | **Invalid** — ON has no s.290

**Abstention:** **n/a**   **False abstention:** **yes**

**Reviewed:** yes

---

## S177 · Q12 · cross_jurisdiction_comparison

**Question:** Compare the deadline for an employee to take earned vacation in Ontario and British Columbia.

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. 33(1) and 35
  Answer: Gives
  Who it applies to: Employee
  Amount / threshold: At least two weeks after each vacation entitlement year that the employee completes
  Mandatory?: mandatory
  Quote: "An employer shall give an employee a vacation of, at least two weeks after each vacation entitlement year that the employee completes, if the employee’s period of employment is less than five years; or at least three weeks after each vacation entitlement year that the employee completes, if the employee’s period of employment is five years or more."
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41

BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 60
  Answer: An annual vacation
  Who it applies to: An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58
  Amount / threshold: at least 2 weeks, after 12 consecutive months of employment, or at least 3 weeks, after 5 consecutive years of employment
  Mandatory?: mandatory
  Exceptions: N; o; t;  ; s; p; e; c; i; f; i; e; d;  ; i; n;  ; t; h; e;  ; e; x; c; e; r; p; t
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml

COMPARISON: DIFFERENT
  entitlement or requirement: different wording (check details)
  threshold: different
  eligibility: different
```

**Gold:**
- Ontario (s. 35): Vacation must be completed no later than 10 months after the end of the vacation entitlement year for which it is given.
- British Columbia (s. 57): Annual vacation must be taken within 12 months after completing the year of employment that entitles the employee to it.
- Comparison: Different: 10 months in Ontario vs. 12 months in BC.

**Key facts:**
- [ON] No later than 10 months after the end of the vacation entitlement year → **Missing** — cites s.35 but states only amounts
- [BC] Within 12 months after completing the entitling year of employment → **Missing**
- [VERDICT] Different: 10 months in Ontario vs. 12 months in BC → **Partial** — 'different' for the wrong reason

**Claims:**
- "Ontario: at least two weeks (under 5 years) or three weeks (5+ years) after each vacation entitlement year" → **Supported** | **Supports**
- "BC: an employer may use a common date for calculating annual vacation entitlement" → **Supported** | **Supports**
- "BC: at least 2 weeks after 12 months, 3 weeks after 5 years" → **Supported** | **Doesn't support** — s.57, cited as s.60

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S178 · Q09 · direct_extraction

**Question:** Can a BC employer use a single common date to calculate annual vacation entitlement for all of its employees?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 60
  Answer: entitlement
  Who it applies to: An employer may use a common date for calculating the annual vacation entitlement of all employees
  Amount / threshold: at least 2 weeks
  Mandatory?: mandatory
  Source: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96113_01/xml
```

**Gold:**
- British Columbia (s. 60): Yes. An employer may use a common date for calculating the annual vacation entitlement of all employees under sections 57 and 58, as long as this does not reduce any employee's rights under those sections.

**Key facts:**
- [BC] A common date for all employees is permitted → **Correct**
- [BC] Must not reduce any employee's rights under those sections → **Missing**

**Claims:**
- "An employer may use a common date for calculating all employees' annual vacation" → **Supported** | **Supports**
- "At least 2 weeks" → **Supported** | **Doesn't support** — s.57, cited as s.60
- "The rule is mandatory" → **Unsupported** | **Doesn't support** — wrong 'Mandatory?' label on a question about what is allowed

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S179 · Q22 · exceptions

**Question:** What conditions must be met for a valid averaging agreement under BC's Employment Standards Act?

**Answer (as the user sees it, notices removed):**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia), s. 10.2(3)
  Answer: The parties must agree on how many hours will be averaged and what those hours represent
  Who it applies to: The employer and employee agree to average the hours worked by each party
  Mandatory?: mandatory
  Quote: "the employer and employee agree to average the hours worked"
```

**Gold:**
- British Columbia (s. 37): The agreement must be written, signed by both parties before its start date, specify the averaging period and daily work schedule, and meet the other statutory requirements.

**Key facts:**
- [BC] Must be in writing → **Missing**
- [BC] Must be signed before the start date → **Missing**
- [BC] Must specify a 1-, 2-, 3-, or 4-week period → **Missing**
- [BC] Must specify the daily work schedule → **Missing**
- [BC] Employee must receive a copy before the averaging period begins → **Missing**

**Claims:**
- "The parties must agree how many hours will be averaged and what those hours represent" → **Unsupported** | **Invalid** — no s.10.2; invented quote

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---

## S180 · Q01 · direct_extraction

**Question:** I've been working in Toronto for about 3 years. How much paid time off am I supposed to get each year?

**Answer (as the user sees it, notices removed):**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. s. 50.1(1.3)
  Answer: paid time off
  Who it applies to: An employee
  Amount / threshold: three paid days
  Mandatory?: mandatory
  Source: https://www.ontario.ca/laws/api/v2/legislation/en/doc-search/statute/00e41
```

**Gold:**
- Ontario (s. 33): At least two weeks of vacation each year (the two-week level applies to employees with less than five years of employment).

**Key facts:**
- [ON] At least 2 weeks of vacation → **Missing** — answers 3 paid days of leave (s.50.1), not vacation

**Claims:**
- "An employee gets three paid days off" → **Supported** | **Supports** — s.50.1 grants 3 paid days of leave; misleading as an answer about annual vacation

**Abstention:** **n/a**   **False abstention:** **no**

**Reviewed:** yes

---
