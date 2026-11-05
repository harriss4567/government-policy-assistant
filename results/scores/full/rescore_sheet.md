# Consistency re-score (rubric v1.2 §7)

Score these answers **from scratch**, using only the rubric and the gold answer. Don't look at `scoring_review.md` or your earlier scores. Replace every **?** (labels are listed at the top of `src/consistency_check.py`).

## S010 · Q02

**Question:** I've been at my job in Vancouver for six years now. Do I get any more vacation time than when I started?

**Answer:**
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
- [BC] At least 3 weeks of annual vacation → **?**
- [BC] Up from at least 2 weeks before reaching 5 years → **?**
- [BC] 5 consecutive years of employment → **?**

**Claims:**
- "An employee is entitled to a minimum of 10 days of vacation for every 12 months of service" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S013 · Q06

**Question:** I just finished my first year working in BC. Am I supposed to get two weeks off now?

**Answer:**
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
- [BC] At least 2 weeks of annual vacation → **?**

**Claims:**
- "Two weeks of paid vacation after one year of continuous employment" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S015 · Q22

**Question:** What conditions must be met for a valid averaging agreement under BC's Employment Standards Act?

**Answer:**
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
- [BC] Must be in writing → **?**
- [BC] Must be signed before the start date → **?**
- [BC] Must specify a 1-, 2-, 3-, or 4-week period → **?**
- [BC] Must specify the daily work schedule → **?**
- [BC] Employee must receive a copy before the averaging period begins → **?**

**Claims:**
- (no claims)

**Abstention:** **?**   **False abstention:** **?**

---

## S018 · Q25

**Question:** I started a new job in BC last week. How long do I have to work before I'm entitled to vacation pay?

**Answer:**
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
- [BC] 5 calendar days of employment → **?**
- [BC] Minimum 4% vacation pay → **?**
- [BC] Based on total wages during the relevant year → **?**

**Claims:**
- "Vacation pay after at least 120 hours of work" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S019 · Q01

**Question:** I've been working in Toronto for about 3 years. How much paid time off am I supposed to get each year?

**Answer:**
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
- [ON] At least 2 weeks of vacation → **?**

**Claims:**
- "An employee is considered paid a salary if paid a fixed amount per pay period that doesn't vary with hours unless they work over 44 hours a week" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S023 · Q30

**Question:** I'm a software developer in Vancouver. Do tech workers get overtime in BC?

**Answer:**
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
- [BC] Section 40 sets general overtime rules (1.5x over 8 hours a day or 40 a week; double over 12 hours a day) → **?**
- [BC] The BC Act does not mention technology workers; any occupation-specific exclusion would be in the regulations, which are not in the knowledge base → **?**

**Claims:**
- "Overtime is owed under s.40 for over 8 hours a day or 40 a week" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S025 · Q09

**Question:** Can a BC employer use a single common date to calculate annual vacation entitlement for all of its employees?

**Answer:**
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
- [BC] A common date for all employees is permitted → **?**
- [BC] Must not reduce any employee's rights under those sections → **?**

**Claims:**
- "An employer may use a common date for all employees if no employee's rights under ss.57–58 are reduced" → **?** | **?**
- "The rule is mandatory" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S039 · Q18

**Question:** Compare the vacation pay payment-timing requirements in Ontario and BC.

**Answer:**
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
- [ON] General rule is lump-sum payment before vacation → **?**
- [ON] Payment during each pay period requires an agreement and separate identification of vacation pay → **?**
- [BC] Payment at least 7 days before vacation → **?**
- [BC] Or on scheduled paydays, if agreed in writing or provided by a collective agreement → **?**
- [VERDICT] Different: Ontario default lump sum before vacation; BC at least 7 days before, or scheduled paydays by written/collective agreement → **?**

**Claims:**
- "Ontario and BC vacation pay timing rules are the same" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S055 · Q13

**Question:** We have staff in Toronto and Vancouver who'd rather bank their overtime and take time off later. Can we do that in both provinces, and do the rules differ?

**Answer:**
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
- [ON] Requires agreement between employer and employee → **?**
- [ON] 1.5 hours of paid time off per overtime hour → **?**
- [ON] Taken within 3 months, or within 12 months with the employee's agreement → **?**
- [ON] Paid out as overtime pay if employment ends first → **?**
- [BC] Set up at the employee's written request → **?**
- [BC] Overtime credited at overtime rates → **?**
- [BC] Employee may request payout, time off, or closing at any time → **?**
- [BC] Employer may close with 1 month's written notice and settle within 6 months → **?**
- [BC] Balance paid on termination or on the employee's request to close → **?**
- [VERDICT] Different: both allow banking overtime; Ontario by agreement with a 3- or 12-month deadline, BC by a time bank at the employee's written request → **?**

**Claims:**
- "Ontario: overtime pay is owed if employment ends before the paid time off is taken" → **?** | **?**
- "BC: overtime can be banked at the employee's written request" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S083 · Q22

**Question:** What conditions must be met for a valid averaging agreement under BC's Employment Standards Act?

**Answer:**
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
- [BC] Must be in writing → **?**
- [BC] Must be signed before the start date → **?**
- [BC] Must specify a 1-, 2-, 3-, or 4-week period → **?**
- [BC] Must specify the daily work schedule → **?**
- [BC] Employee must receive a copy before the averaging period begins → **?**

**Claims:**
- "The agreement must be in writing and signed by both before its start date" → **?** | **?**
- "It must specify the number of weeks, the daily schedule, any repeats, and start and expiry dates" → **?** | **?**
- "The employee must receive a copy before the averaging period begins" → **?** | **?**
- "The schedule must comply with subsection (3)" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S094 · Q19

**Question:** Instead of getting my vacation pay all at once, can my employer in Ontario just add it to every paycheque?

**Answer:**
```text
ONTARIO: Employment Standards Act, 2000 (Ontario), s. Employment Standards Act, 2000
  Answer: Entitlement to vacation pay must be established by contract between employee and employer.
  Who it applies to: All employees who have worked for their employer for more than one year and earned at least $15 per hour.
  Amount / threshold: The amount of vacation pay that may be added to each paycheque depends on the terms of the contract between the employee and employer.
```

**Gold:**
- Ontario (s. 36): Only if the employee has agreed to it and the vacation pay is shown separately, either on the wage statement for each pay period or on a separate statement given at the same time. Otherwise the default is a lump sum before the vacation starts.

**Key facts:**
- [ON] Requires an agreement between the employee and employer → **?**
- [ON] Vacation pay shown separately on the wage statement, or on a separate statement provided at the same time → **?**
- [ON] Default is a lump sum before vacation (s. 36(1)) → **?**

**Claims:**
- "Entitlement to vacation pay must be set by contract" → **?** | **?**
- "Applies to employees with over one year of service earning at least $15 an hour" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S102 · Q01

**Question:** I've been working in Toronto for about 3 years. How much paid time off am I supposed to get each year?

**Answer:**
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
- [ON] At least 2 weeks of vacation → **?**

**Claims:**
- "An employee is entitled to a total of three paid days of leave under s.50.1(1.2)" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S108 · Q04

**Question:** What is the minimum vacation pay percentage for an Ontario employee with at least five years of employment?

**Answer:**
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
- [ON] Minimum 6% vacation pay → **?**
- [ON] Vacation pay is excluded from the wage calculation → **?**

**Claims:**
- "Minimum vacation pay after five years is 5%" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S112 · Q14

**Question:** We've got employees in Toronto and Vancouver who've both been here for six years. Do they get the same vacation pay percentage?

**Answer:**
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
- [ON] Minimum 6% → **?**
- [ON] Excludes vacation pay from wages → **?**
- [BC] Minimum 6% → **?**
- [BC] Based on total wages during the relevant year → **?**
- [VERDICT] Same: both at least 6% after five years → **?**

**Claims:**
- "Ontario: vacation pay after at least 12 months with the employer" → **?** | **?**
- "BC: vacation pay after at least 60 days with the employer" → **?** | **?**
- "Ontario and BC vacation pay percentages differ at six years" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S130 · Q13

**Question:** We have staff in Toronto and Vancouver who'd rather bank their overtime and take time off later. Can we do that in both provinces, and do the rules differ?

**Answer:**
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
- [ON] Requires agreement between employer and employee → **?**
- [ON] 1.5 hours of paid time off per overtime hour → **?**
- [ON] Taken within 3 months, or within 12 months with the employee's agreement → **?**
- [ON] Paid out as overtime pay if employment ends first → **?**
- [BC] Set up at the employee's written request → **?**
- [BC] Overtime credited at overtime rates → **?**
- [BC] Employee may request payout, time off, or closing at any time → **?**
- [BC] Employer may close with 1 month's written notice and settle within 6 months → **?**
- [BC] Balance paid on termination or on the employee's request to close → **?**
- [VERDICT] Different: both allow banking overtime; Ontario by agreement with a 3- or 12-month deadline, BC by a time bank at the employee's written request → **?**

**Claims:**
- "Ontario: if employment ends before the time off is taken, the employer must pay overtime pay" → **?** | **?**
- "BC: the employer may set up a time bank for overtime wages at the employee's written request" → **?** | **?**
- "BC: banked overtime can be taken as paid time off at an agreed time" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---

## S138 · Q07

**Question:** My boss in BC says my vacation pay will be lower this year because I got a bonus. Is that allowed?

**Answer:**
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
- [BC] Cannot reduce vacation or vacation pay because of a bonus → **?**

**Claims:**
- (no claims)

**Abstention:** **?**   **False abstention:** **?**

---

## S150 · Q30

**Question:** I'm a software developer in Vancouver. Do tech workers get overtime in BC?

**Answer:**
```text
BRITISH COLUMBIA: Employment Standards Act (British Columbia)
  Not specified in the retrieved sections. The model did not return a usable answer (invalid JSON after a retry).
```

**Gold:**
- British Columbia (s. 40): Cannot be determined from the Acts in the knowledge base. Section 40 sets the general overtime rules, but the BC Act's text does not address whether tech workers are excluded.
- Abstain (British Columbia): whether tech workers are excluded from overtime is not addressed in the BC Act; exclusions are set out in the regulations, which are not in the knowledge base.

**Key facts:**
- [BC] Section 40 sets general overtime rules (1.5x over 8 hours a day or 40 a week; double over 12 hours a day) → **?**
- [BC] The BC Act does not mention technology workers; any occupation-specific exclusion would be in the regulations, which are not in the knowledge base → **?**

**Claims:**
- (no claims)

**Abstention:** **?**   **False abstention:** **?**

---

## S167 · Q06

**Question:** I just finished my first year working in BC. Am I supposed to get two weeks off now?

**Answer:**
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
- [BC] At least 2 weeks of annual vacation → **?**

**Claims:**
- "The threshold is up to 16 consecutive days of employment" → **?** | **?**
- "An employee may begin the leave no earlier than the first day of the week in which the period begins" → **?** | **?**

**Abstention:** **?**   **False abstention:** **?**

---
