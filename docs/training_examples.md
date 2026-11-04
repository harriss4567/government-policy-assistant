# Training examples (SFT): DRAFT, human review required

AI-drafted from `train_pool` sections only; **every example must be checked by a human** against the excerpt before training.
To approve an example change `Reviewed: no` to `Reviewed: yes`. Edit any field directly. Then run `.venv/bin/python src/convert_training_data.py`, which validates everything and writes `data/train.jsonl` and `data/val.jsonl`.

**Field rules:** `Not specified in the excerpt` when the excerpts don't state it (never guess). `exceptions` = list, `[]` if none stated. `mandatory` = `mandatory` when the excerpt binds someone (shall, must, must not, shall not, may not, is entitled to, is liable); `optional` when it only permits something (may); `Not specified in the excerpt` for definitions, scope statements ("This Part does not apply…", "is laid off if…") or when nothing answers. If an excerpt mixes "may" and "may not", label by what the question asks about. `supporting_quote` = copied word for word from an excerpt (`""` if nothing answers the question). When nothing in the excerpts answers the question, every field is `Not specified in the excerpt`.

## T001
- **Split:** train
- **Type:** eligibility
- **Jurisdiction:** Ontario
- **Question:** Does a job ad in Ontario have to say how much the job pays?
- **Excerpts:**
  - [ON s. 8.2(1)] (1) Every employer who advertises a publicly advertised job posting shall include in the posting information about the expected compensation for the position or the range of expected compensation for the position.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "job_postings",
  "section": "8.2(1)",
  "eligibility": "Employer advertises a publicly advertised job posting",
  "entitlement_or_requirement": "The posting must include the expected compensation or a range of expected compensation for the position",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "shall include in the posting information about the expected compensation for the position or the range of expected compensation for the position"
}
```
- **Reviewed:** yes

## T002
- **Split:** train
- **Type:** prohibition
- **Jurisdiction:** Ontario
- **Question:** Can an employer in Ontario ask for Canadian work experience in a job posting?
- **Excerpts:**
  - [ON s. 8.3(1)] (1) No employer who advertises a publicly advertised job posting shall include in the posting or in any associated application form any requirements related to Canadian experience.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "job_postings",
  "section": "8.3(1)",
  "eligibility": "Employer advertises a publicly advertised job posting",
  "entitlement_or_requirement": "The posting and any associated application form must not include requirements related to Canadian experience",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "No employer who advertises a publicly advertised job posting shall include in the posting or in any associated application form any requirements related to Canadian experience"
}
```
- **Reviewed:** yes

## T003
- **Split:** train
- **Type:** eligibility, distractor
- **Jurisdiction:** Ontario
- **Question:** If a company in Ontario uses AI to screen job applicants, does it have to tell them?
- **Excerpts:**
  - [ON s. 8.4(1)] (1) Every employer who advertises a publicly advertised job posting and who uses artificial intelligence to screen, assess or select applicants for the position shall include in the posting a statement disclosing the use of the artificial intelligence.
  - [ON s. 12(3)] (3) The statement may be provided to the employee by electronic mail rather than in writing if the employee has access to a means of making a paper copy of the statement.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "job_postings",
  "section": "8.4(1)",
  "eligibility": "Employer advertises a publicly advertised job posting and uses artificial intelligence to screen, assess or select applicants",
  "entitlement_or_requirement": "The posting must include a statement disclosing the use of artificial intelligence",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "shall include in the posting a statement disclosing the use of the artificial intelligence"
}
```
- **Reviewed:** yes

## T004
- **Split:** train
- **Type:** missing
- **Jurisdiction:** Ontario
- **Question:** How many days after an interview does an Ontario employer have to get back to the applicant?
- **Excerpts:**
  - [ON s. 8.6] If an employer interviews an applicant for a publicly advertised job posting, the employer shall, within the prescribed time period, provide the applicant with the prescribed information.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "job_postings",
  "section": "8.6",
  "eligibility": "Employer interviews an applicant for a publicly advertised job posting",
  "entitlement_or_requirement": "Employer must provide the applicant with the prescribed information",
  "threshold": "Not specified in the excerpt (the time period is prescribed by regulation)",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employer shall, within the prescribed time period, provide the applicant with the prescribed information"
}
```
- **Reviewed:** yes

## T005
- **Split:** train
- **Type:** exception, threshold
- **Jurisdiction:** Ontario
- **Question:** My employer sold the business and the new owner hired me. Does my length of employment start over in Ontario?
- **Excerpts:**
  - [ON s. 9(1)] (1) If an employer sells a business or a part of a business and the purchaser employs an employee of the seller, the employment of the employee shall be deemed not to have been terminated or severed for the purposes of this Act and his or her employment with the seller shall be deemed to have been employment with the purchaser for the purpose of any subsequent calculation of the employee’s length or period of employment.
  - [ON s. 9(2)] (2) Subsection (1) does not apply if the day on which the purchaser hires the employee is more than 13 weeks after the earlier of his or her last day of employment with the seller and the day of the sale.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "continuity_of_employment",
  "section": "9(1), 9(2)",
  "eligibility": "Employer sells all or part of a business and the purchaser employs an employee of the seller",
  "entitlement_or_requirement": "Employment is deemed not terminated, and employment with the seller counts as employment with the purchaser for calculating length or period of employment",
  "threshold": "Purchaser hires the employee within 13 weeks of the earlier of the last day of employment with the seller and the day of the sale",
  "exceptions": [
    "Does not apply if the purchaser hires the employee more than 13 weeks after the earlier of the employee's last day with the seller and the day of the sale (s. 9(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "shall be deemed not to have been terminated or severed for the purposes of this Act"
}
```
- **Reviewed:** yes

## T006
- **Split:** train
- **Type:** exception
- **Jurisdiction:** Ontario
- **Question:** Does my employer in Ontario have to pay me on a regular schedule?
- **Excerpts:**
  - [ON s. 11(1)] (1) An employer shall establish a recurring pay period and a recurring pay day and shall pay all wages earned during each pay period, other than accruing vacation pay, no later than the pay day for that period.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "payment_of_wages",
  "section": "11(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must establish a recurring pay period and recurring pay day, and pay all wages earned in each pay period no later than that pay day",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Accruing vacation pay is excluded"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "shall pay all wages earned during each pay period, other than accruing vacation pay, no later than the pay day for that period"
}
```
- **Reviewed:** yes

## T007
- **Split:** train
- **Type:** optional, eligibility
- **Jurisdiction:** Ontario
- **Question:** Can my pay stub be emailed to me instead of printed in Ontario?
- **Excerpts:**
  - [ON s. 12(3)] (3) The statement may be provided to the employee by electronic mail rather than in writing if the employee has access to a means of making a paper copy of the statement.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "payment_of_wages",
  "section": "12(3)",
  "eligibility": "The employee has access to a means of making a paper copy of the statement",
  "entitlement_or_requirement": "The wage statement may be provided by electronic mail rather than in writing",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "optional",
  "supporting_quote": "The statement may be provided to the employee by electronic mail rather than in writing if the employee has access to a means of making a paper copy of the statement."
}
```
- **Reviewed:** yes

## T008
- **Split:** train
- **Type:** exception
- **Jurisdiction:** Ontario
- **Question:** Is my employer in Ontario allowed to take money off my paycheque?
- **Excerpts:**
  - [ON s. 13(1)] (1) An employer shall not withhold wages payable to an employee, make a deduction from an employee’s wages or cause the employee to return his or her wages to the employer unless authorized to do so under this section.
  - [ON s. 13(2)] (2) An employer may withhold or make a deduction from an employee’s wages or cause the employee to return them if a statute of Ontario or Canada or a court order authorizes it.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "payment_of_wages",
  "section": "13(1), 13(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must not withhold wages, make deductions, or cause the employee to return wages unless authorized under this section",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Allowed if a statute of Ontario or Canada or a court order authorizes it (s. 13(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "An employer shall not withhold wages payable to an employee, make a deduction from an employee’s wages or cause the employee to return his or her wages to the employer unless authorized to do so under this section."
}
```
- **Reviewed:** yes

## T009
- **Split:** train
- **Type:** threshold, exception
- **Jurisdiction:** Ontario
- **Question:** If my Ontario employer runs out of money, do unpaid wages get paid before other creditors?
- **Excerpts:**
  - [ON s. 14(1)] (1) Despite any other Act, wages shall have priority over and be paid before the claims and rights of all other unsecured creditors of an employer, to the extent of $10,000 per employee.
  - [ON s. 14(2)] (2) Subsection (1) does not apply with respect to a distribution made under the Bankruptcy and Insolvency Act (Canada) or other legislation enacted by the Parliament of Canada respecting bankruptcy or insolvency.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "payment_of_wages",
  "section": "14(1), 14(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Wages have priority over and are paid before the claims of all other unsecured creditors of the employer",
  "threshold": "Up to $10,000 per employee",
  "exceptions": [
    "Does not apply to a distribution under the Bankruptcy and Insolvency Act (Canada) or other federal bankruptcy or insolvency legislation (s. 14(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "to the extent of $10,000 per employee"
}
```
- **Reviewed:** yes

## T010
- **Split:** train
- **Type:** eligibility
- **Jurisdiction:** Ontario
- **Question:** If my tips are paid in cash in Ontario, where does my employer have to give them to me?
- **Excerpts:**
  - [ON s. 14.1(2)] (2) If payment is made by cash or cheque, the employer shall ensure that the cash or cheque is given to the employee at his or her workplace or at some other place agreeable to the employee.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "tips_and_gratuities",
  "section": "14.1(2)",
  "eligibility": "Tips or other gratuities are paid by cash or cheque",
  "entitlement_or_requirement": "The cash or cheque must be given to the employee at the workplace or at another place agreeable to the employee",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employer shall ensure that the cash or cheque is given to the employee at his or her workplace or at some other place agreeable to the employee"
}
```
- **Reviewed:** yes

## T011
- **Split:** train
- **Type:** optional, exception
- **Jurisdiction:** Ontario
- **Question:** Can my Ontario employer take a share of the tip pool?
- **Excerpts:**
  - [ON s. 14.4(1)] (1) An employer may withhold or make a deduction from an employee’s tips or other gratuities or cause the employee to return or give them to the employer if the employer collects and redistributes tips or other gratuities among some or all of the employer’s employees.
  - [ON s. 14.4(3)] (3) Subject to subsections (4) and (5), an employer or a director or shareholder of an employer may not share in tips or other gratuities redistributed under subsection (1).
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "tips_and_gratuities",
  "section": "14.4(1), 14.4(3)",
  "eligibility": "Employer collects and redistributes tips or other gratuities among some or all of its employees",
  "entitlement_or_requirement": "The employer may pool and redistribute tips, but the employer, or a director or shareholder of the employer, may not share in the redistributed tips",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Subject to subsections (4) and (5), which are not included in the excerpt"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "an employer or a director or shareholder of an employer may not share in tips or other gratuities redistributed under subsection (1)"
}
```
- **Reviewed:** yes

## T012
- **Split:** train
- **Type:** missing
- **Jurisdiction:** Ontario
- **Question:** How long does an Ontario employer have to keep employee records?
- **Excerpts:**
  - [ON s. 16] An employer shall ensure that all of the records and documents required to be retained under sections 15 and 15.1 are readily available for inspection as required by an employment standards officer, even if the employer has arranged for another person to retain them.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "records",
  "section": "Not specified in the excerpt",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Not specified in the excerpt",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": ""
}
```
- **Reviewed:** yes

## T013
- **Split:** train
- **Type:** threshold, eligibility
- **Jurisdiction:** Ontario
- **Question:** We have 10 employees in Ontario. Do we need a written policy on disconnecting from work?
- **Excerpts:**
  - [ON s. 21.1.2(1)] (1) An employer that, on January 1 of any year, employs 25 or more employees shall, before March 1 of that year, ensure it has a written policy in place for all employees with respect to disconnecting from work that includes the date the policy was prepared and the date any changes were made to the policy.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "disconnecting_from_work",
  "section": "21.1.2(1)",
  "eligibility": "Employer employs 25 or more employees on January 1 of the year",
  "entitlement_or_requirement": "Employer must have a written policy on disconnecting from work for all employees, including the date it was prepared and the dates of any changes",
  "threshold": "25 or more employees on January 1; policy in place before March 1 of that year",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employer that, on January 1 of any year, employs 25 or more employees shall, before March 1 of that year, ensure it has a written policy in place"
}
```
- **Reviewed:** yes

## T014
- **Split:** train
- **Type:** exception, threshold
- **Jurisdiction:** Ontario
- **Question:** I got sent home after an hour at work in Ontario. Do I get paid for more than the hour?
- **Excerpts:**
  - [ON s. 21.2(1)] (1) If an employee who regularly works more than three hours a day is required to present himself or herself for work but works less than three hours, despite being available to work longer, the employer shall pay the employee wages for three hours, equal to the greater of the following: / 1. The sum of, / i. the amount the employee earned for the time worked, and / ii. wages equal to the employee’s regular rate for the remainder of the time. / 2. Wages equal to the employee’s regular rate for three hours of work.
  - [ON s. 21.2(2)] (2) Subsection (1) does not apply if the employer is unable to provide work for the employee because of fire, lightning, power failure, storms or similar causes beyond the employer’s control that result in the stopping of work.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "three_hour_rule",
  "section": "21.2(1), 21.2(2)",
  "eligibility": "Employee regularly works more than three hours a day, is required to present for work, and works less than three hours despite being available to work longer",
  "entitlement_or_requirement": "Employer must pay wages for three hours: the greater of (earnings for time worked plus the regular rate for the rest of the three hours) or the regular rate for three hours",
  "threshold": "Three hours",
  "exceptions": [
    "Does not apply if the employer cannot provide work because of fire, lightning, power failure, storms or similar causes beyond the employer's control that stop work (s. 21.2(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "the employer shall pay the employee wages for three hours"
}
```
- **Reviewed:** yes

## T015
- **Split:** train
- **Type:** eligibility
- **Jurisdiction:** Ontario
- **Question:** In Ontario, can the room and board my employer provides count as part of my wages?
- **Excerpts:**
  - [ON s. 23(2)] (2) If an employer provides room or board to an employee, the prescribed amount with respect to room or board shall be deemed to have been paid by the employer to the employee as wages.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "minimum_wage",
  "section": "23(2)",
  "eligibility": "Employer provides room or board to the employee",
  "entitlement_or_requirement": "The prescribed amount for room or board is deemed to have been paid to the employee as wages",
  "threshold": "Not specified in the excerpt (the amount is prescribed by regulation)",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the prescribed amount with respect to room or board shall be deemed to have been paid by the employer to the employee as wages"
}
```
- **Reviewed:** yes

## T016
- **Split:** train
- **Type:** missing, distractor
- **Jurisdiction:** Ontario
- **Question:** What is the general minimum wage per hour in Ontario?
- **Excerpts:**
  - [ON s. 23(2)] (2) If an employer provides room or board to an employee, the prescribed amount with respect to room or board shall be deemed to have been paid by the employer to the employee as wages.
  - [ON s. 23.0.1] If the minimum wage rate applicable to an employee changes during a pay period, the calculations required by subsection 23 (4) shall be performed as if the pay period were two separate pay periods, the first consisting of the part falling before the day on which the change takes effect and the second consisting of the part falling on and after the day on which the change takes effect.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "minimum_wage",
  "section": "Not specified in the excerpt",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Not specified in the excerpt",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": ""
}
```
- **Reviewed:** yes

## T017
- **Split:** train
- **Type:** threshold
- **Jurisdiction:** Ontario
- **Question:** What does premium pay mean for working a public holiday in Ontario?
- **Excerpts:**
  - [ON s. 24(2)] (2) An employer who is required under this Part to pay premium pay to an employee shall pay the employee at least one and one half times his or her regular rate.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "public_holidays",
  "section": "24(2)",
  "eligibility": "Employer is required under this Part to pay premium pay",
  "entitlement_or_requirement": "Premium pay of at least one and one half times the employee's regular rate",
  "threshold": "At least 1.5 times the regular rate",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "shall pay the employee at least one and one half times his or her regular rate"
}
```
- **Reviewed:** yes

## T018
- **Split:** train
- **Type:** exception
- **Jurisdiction:** Ontario
- **Question:** A public holiday falls on a normal workday for me in Ontario. Do I get the day off with pay?
- **Excerpts:**
  - [ON s. 26(1)] (1) If a public holiday falls on a day that would ordinarily be a working day for an employee and the employee is not on vacation that day, the employer shall give the employee the day off work and pay him or her public holiday pay for that day.
  - [ON s. 26(2)] (2) The employee has no entitlement under subsection (1) if he or she fails, without reasonable cause, to work all of his or her last regularly scheduled day of work before the public holiday or all of his or her first regularly scheduled day of work after the public holiday.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "public_holidays",
  "section": "26(1), 26(2)",
  "eligibility": "Public holiday falls on a day that would ordinarily be a working day, and the employee is not on vacation that day",
  "entitlement_or_requirement": "Employer must give the day off work and pay public holiday pay for that day",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "No entitlement if the employee fails, without reasonable cause, to work all of the last regularly scheduled day before or the first regularly scheduled day after the public holiday (s. 26(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "the employer shall give the employee the day off work and pay him or her public holiday pay for that day"
}
```
- **Reviewed:** yes

## T019
- **Split:** train
- **Type:** options, exception
- **Jurisdiction:** Ontario
- **Question:** If I agree to work on a public holiday in Ontario, what am I paid?
- **Excerpts:**
  - [ON s. 27(1)] (1) An employee and employer may agree that the employee will work on a public holiday that would ordinarily be a working day for that employee, and if they do, section 26 does not apply to the employee.
  - [ON s. 27(2)] (2) Subject to subsections (3) and (4), if an employer and an employee make an agreement under subsection (1), / (a) the employer shall pay to the employee wages at his or her regular rate for the hours worked on the public holiday and substitute another day that would ordinarily be a working day for the employee to take off work and for which he or she shall be paid public holiday pay as if the substitute day were a public holiday; or / (b) if the employee and the employer agree, the employer shall pay to the employee public holiday pay for the day plus premium pay for each hour worked on that day.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "public_holidays",
  "section": "27(1), 27(2)",
  "eligibility": "Employee and employer agree that the employee will work on a public holiday that would ordinarily be a working day",
  "entitlement_or_requirement": "Either regular wages for hours worked plus a substitute day off with public holiday pay, or, if both agree, public holiday pay plus premium pay for each hour worked",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Subject to subsections (3) and (4), which are not included in the excerpt"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "if the employee and the employer agree, the employer shall pay to the employee public holiday pay for the day plus premium pay for each hour worked on that day"
}
```
- **Reviewed:** yes

## T020
- **Split:** train
- **Type:** optional, eligibility
- **Jurisdiction:** Ontario
- **Question:** I work at a restaurant in Ontario. Can my boss make me work on a public holiday?
- **Excerpts:**
  - [ON s. 28(1)] (1) If an employee is employed in a hospital, a continuous operation, or a hotel, motel, tourist resort, restaurant or tavern, the employer may require the employee to work on a public holiday that is ordinarily a working day for the employee and that is not a day on which the employee is on vacation, and if the employer does so, sections 26 and 27 do not apply to the employee.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "public_holidays",
  "section": "28(1)",
  "eligibility": "Employee is employed in a hospital, a continuous operation, or a hotel, motel, tourist resort, restaurant or tavern; the holiday is ordinarily a working day and not a vacation day",
  "entitlement_or_requirement": "The employer may require the employee to work on the public holiday, and sections 26 and 27 then do not apply",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "optional",
  "supporting_quote": "the employer may require the employee to work on a public holiday that is ordinarily a working day for the employee"
}
```
- **Reviewed:** yes

## T021
- **Split:** train
- **Type:** requirement
- **Jurisdiction:** Ontario
- **Question:** A public holiday lands on my day off in Ontario. What happens?
- **Excerpts:**
  - [ON s. 29(1)] (1) If a public holiday falls on a day that would not ordinarily be a working day for an employee or a day on which the employee is on vacation, the employer shall substitute another day that would ordinarily be a working day for the employee to take off work and for which he or she shall be paid public holiday pay as if the substitute day were a public holiday.
  - [ON s. 29(1.1)] (1.1) If a day is substituted for a public holiday under subsection (1), the employer shall provide the employee with a written statement, before the public holiday, that sets out, / (a) the public holiday that is being substituted; / (b) the date of the day that is substituted for a public holiday under subsection (1); and / (c) the date on which the statement is provided to the employee.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "public_holidays",
  "section": "29(1), 29(1.1)",
  "eligibility": "Public holiday falls on a day that is not ordinarily a working day, or on a vacation day",
  "entitlement_or_requirement": "Employer must substitute another working day off with public holiday pay, and give a written statement before the holiday naming the holiday, the substitute date, and the date of the statement",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employer shall substitute another day that would ordinarily be a working day for the employee to take off work"
}
```
- **Reviewed:** yes

## T022
- **Split:** train
- **Type:** exception, list
- **Jurisdiction:** Ontario
- **Question:** Can a man and a woman doing the same job in Ontario be paid different rates?
- **Excerpts:**
  - [ON s. 42(1)] (1) No employer shall pay an employee of one sex at a rate of pay less than the rate paid to an employee of the other sex when, / (a) they perform substantially the same kind of work in the same establishment; / (b) their performance requires substantially the same skill, effort and responsibility; and / (c) their work is performed under similar working conditions.
  - [ON s. 42(2)] (2) Subsection (1) does not apply when the difference in the rate of pay is made on the basis of, / (a) a seniority system; / (b) a merit system; / (c) a system that measures earnings by quantity or quality of production; or / (d) any other factor other than sex.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "equal_pay",
  "section": "42(1), 42(2)",
  "eligibility": "Employees of different sexes do substantially the same kind of work in the same establishment, requiring substantially the same skill, effort and responsibility, under similar working conditions",
  "entitlement_or_requirement": "Employer must not pay one sex a lower rate than the other",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "A seniority system",
    "A merit system",
    "A system measuring earnings by quantity or quality of production",
    "Any other factor other than sex"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "No employer shall pay an employee of one sex at a rate of pay less than the rate paid to an employee of the other sex"
}
```
- **Reviewed:** yes

## T023
- **Split:** train
- **Type:** exception
- **Jurisdiction:** Ontario
- **Question:** Can an Ontario benefit plan treat employees differently based on age?
- **Excerpts:**
  - [ON s. 44(1)] (1) Except as prescribed, no employer or person acting directly on behalf of an employer shall provide, offer or arrange for a benefit plan that treats any of the following persons differently because of the age, sex or marital status of employees: / 1. Employees. / 2. Beneficiaries. / 3. Survivors. / 4. Dependants.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "benefit_plans",
  "section": "44(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must not provide, offer or arrange a benefit plan that treats employees, beneficiaries, survivors or dependants differently because of age, sex or marital status",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Except as prescribed by regulation"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "Except as prescribed, no employer or person acting directly on behalf of an employer shall provide, offer or arrange for a benefit plan"
}
```
- **Reviewed:** yes

## T024
- **Split:** train
- **Type:** threshold
- **Jurisdiction:** Ontario
- **Question:** How early can I start pregnancy leave in Ontario, and how much notice do I have to give?
- **Excerpts:**
  - [ON s. 46(2)] (2) An employee may begin her pregnancy leave no earlier than the earlier of, / (a) the day that is 17 weeks before her due date; and / (b) the day on which she gives birth.
  - [ON s. 46(4)] (4) An employee wishing to take pregnancy leave shall give the employer, / (a) written notice at least two weeks before the day the leave is to begin; and / (b) if the employer requests it, a certificate from a legally qualified medical practitioner stating the due date.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "46(2), 46(4)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Leave may begin no earlier than the earlier of 17 weeks before the due date or the day of birth; written notice must be given, plus a medical certificate of the due date if the employer requests it",
  "threshold": "Earliest start: 17 weeks before the due date; written notice at least two weeks before the leave begins",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "written notice at least two weeks before the day the leave is to begin"
}
```
- **Reviewed:** yes

## T025
- **Split:** train
- **Type:** eligibility, threshold
- **Jurisdiction:** Ontario
- **Question:** I've only been at my job in Ontario for two months. Can I take parental leave?
- **Excerpts:**
  - [ON s. 48(1)] (1) An employee who has been employed by his or her employer for at least 13 weeks and who is the parent of a child is entitled to a leave of absence without pay following the birth of the child or the coming of the child into the employee’s custody, care and control for the first time.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "48(1)",
  "eligibility": "Employee has been employed by the employer for at least 13 weeks and is the parent of a child",
  "entitlement_or_requirement": "Leave of absence without pay following the birth of the child or the child first coming into the employee's custody, care and control",
  "threshold": "At least 13 weeks of employment",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employee who has been employed by his or her employer for at least 13 weeks and who is the parent of a child is entitled to a leave of absence without pay"
}
```
- **Reviewed:** yes

## T026
- **Split:** train
- **Type:** threshold, eligibility
- **Jurisdiction:** Ontario
- **Question:** How long can I take off in Ontario to care for a family member who is dying?
- **Excerpts:**
  - [ON s. 49.1(2)] (2) An employee is entitled to a leave of absence without pay of up to 28 weeks to provide care or support to an individual described in subsection (3) if a qualified health practitioner issues a certificate stating that the individual has a serious medical condition with a significant risk of death occurring within a period of 26 weeks or such shorter period as may be prescribed.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "49.1(2)",
  "eligibility": "A qualified health practitioner certifies that the individual has a serious medical condition with a significant risk of death within 26 weeks (or a shorter prescribed period)",
  "entitlement_or_requirement": "Leave of absence without pay to provide care or support",
  "threshold": "Up to 28 weeks",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employee is entitled to a leave of absence without pay of up to 28 weeks"
}
```
- **Reviewed:** yes

## T027
- **Split:** train
- **Type:** eligibility, optional
- **Jurisdiction:** Ontario
- **Question:** I'm donating a kidney. Can I get time off work in Ontario?
- **Excerpts:**
  - [ON s. 49.2(3)] (3) An employee who has been employed by his or her employer for at least 13 weeks and undergoes surgery for the purpose of organ donation is entitled to a leave of absence without pay.
  - [ON s. 49.2(4)] (4) The employer may require an employee who takes leave under this section to provide a certificate issued by a legally qualified medical practitioner confirming that the employee has undergone or will undergo surgery for the purpose of organ donation.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "49.2(3), 49.2(4)",
  "eligibility": "Employee has been employed for at least 13 weeks and undergoes surgery for organ donation",
  "entitlement_or_requirement": "Leave of absence without pay; the employer may require a medical certificate confirming the surgery",
  "threshold": "At least 13 weeks of employment",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "undergoes surgery for the purpose of organ donation is entitled to a leave of absence without pay"
}
```
- **Reviewed:** yes

## T028
- **Split:** train
- **Type:** threshold, eligibility
- **Jurisdiction:** Ontario
- **Question:** My child is critically ill. How much leave can I take in Ontario?
- **Excerpts:**
  - [ON s. 49.4(2)] (2) An employee who has been employed by his or her employer for at least six consecutive months is entitled to a leave of absence without pay to provide care or support to a critically ill minor child who is a family member of the employee if a qualified health practitioner issues a certificate that, / (a) states that the minor child is a critically ill minor child who requires the care or support of one or more family members; and / (b) sets out the period during which the minor child requires the care or support.
  - [ON s. 49.4(3)] (3) Subject to subsection (4), an employee is entitled to take up to 37 weeks of leave under this section to provide care or support to a critically ill minor child.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "49.4(2), 49.4(3)",
  "eligibility": "Employee employed for at least six consecutive months; a qualified health practitioner certifies the minor child is critically ill and requires care or support, and sets out the period",
  "entitlement_or_requirement": "Leave of absence without pay to care for or support a critically ill minor child who is a family member",
  "threshold": "Up to 37 weeks; at least six consecutive months of employment",
  "exceptions": [
    "Subject to subsection (4), which is not included in the excerpt"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "an employee is entitled to take up to 37 weeks of leave under this section"
}
```
- **Reviewed:** yes

## T029
- **Split:** train
- **Type:** threshold
- **Jurisdiction:** Ontario
- **Question:** How much domestic or sexual violence leave can I take in a year in Ontario?
- **Excerpts:**
  - [ON s. 49.7(4)] (4) An employee is entitled to take, in each calendar year, / (a) up to 10 days of leave under this section; and / (b) up to 15 weeks of leave under this section.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "49.7(4)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Leave in each calendar year of up to 10 days and up to 15 weeks",
  "threshold": "Up to 10 days and up to 15 weeks per calendar year",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "(a) up to 10 days of leave under this section; and"
}
```
- **Reviewed:** yes

## T030
- **Split:** train
- **Type:** eligibility, threshold
- **Jurisdiction:** Ontario
- **Question:** I have a serious illness and can't work for months. Is there job-protected leave in Ontario?
- **Excerpts:**
  - [ON s. 49.8(2)] (2) An employee who has been employed by an employer for at least 13 consecutive weeks is entitled to a leave of absence without pay i f, / (a) the employee will not be performing the duties of the employee’s position because of a serious medical condition; and / (b) a qualified health practitioner issues a certificate that, / (i) states that the employee has a serious medical condition, and / (ii) sets out the period during which the employee will not be performing the duties of the employee’s position because of the serious medical condition.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "49.8(2)",
  "eligibility": "Employee employed for at least 13 consecutive weeks; cannot perform their duties because of a serious medical condition; a qualified health practitioner issues a certificate stating the condition and the period",
  "entitlement_or_requirement": "Leave of absence without pay",
  "threshold": "At least 13 consecutive weeks of employment",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employee who has been employed by an employer for at least 13 consecutive weeks is entitled to a leave of absence without pay"
}
```
- **Reviewed:** yes

## T031
- **Split:** train
- **Type:** missing
- **Jurisdiction:** Ontario
- **Question:** How many sick days do I get each year in Ontario?
- **Excerpts:**
  - [ON s. 50(1)] (1) An employee who has been employed by an employer for at least two consecutive weeks is entitled to a leave of absence without pay because of a personal illness, injury or medical emergency.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "50(1)",
  "eligibility": "Employee has been employed by the employer for at least two consecutive weeks",
  "entitlement_or_requirement": "Leave of absence without pay because of a personal illness, injury or medical emergency",
  "threshold": "Not specified in the excerpt (the number of days is not stated)",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employee who has been employed by an employer for at least two consecutive weeks is entitled to a leave of absence without pay because of a personal illness, injury or medical emergency."
}
```
- **Reviewed:** yes

## T032
- **Split:** train
- **Type:** list, eligibility
- **Jurisdiction:** Ontario
- **Question:** Can I take leave in Ontario to look after my sick grandmother?
- **Excerpts:**
  - [ON s. 50.0.1(1)] (1) An employee who has been employed by an employer for at least two consecutive weeks is entitled to a leave of absence without pay because of any of the following: / 1. The illness, injury or medical emergency of an individual described in subsection (3). / 2. An urgent matter that concerns an individual described in subsection (3).
  - [ON s. 50.0.1(3)] (3) Subsection (1) applies with respect to the following individuals: / 1. The employee’s spouse. / 2. A parent, step-parent or foster parent of the employee or the employee’s spouse. / 3. A child, step-child or foster child of the employee or the employee’s spouse. / 4. A grandparent, step-grandparent, grandchild or step-grandchild of the employee or of the employee’s spouse. / 5. The spouse of a child of the employee. / 6. The employee’s brother or sister. / 7. A relative of the employee who is dependent on the employee for care or assistance.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "50.0.1(1), 50.0.1(3)",
  "eligibility": "Employee employed for at least two consecutive weeks; the illness, injury, medical emergency or urgent matter concerns a listed individual, which includes a grandparent of the employee or the employee's spouse",
  "entitlement_or_requirement": "Leave of absence without pay",
  "threshold": "At least two consecutive weeks of employment",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "4. A grandparent, step-grandparent, grandchild or step-grandchild of the employee or of the employee’s spouse."
}
```
- **Reviewed:** yes

## T033
- **Split:** train
- **Type:** missing
- **Jurisdiction:** Ontario
- **Question:** Do I get bereavement leave in Ontario if my cousin dies?
- **Excerpts:**
  - [ON s. 50.0.2(1)] (1) An employee who has been employed by an employer for at least two consecutive weeks is entitled to a leave of absence without pay because of the death of an individual described in subsection (3).
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "50.0.2(1)",
  "eligibility": "Employee employed for at least two consecutive weeks; whether a cousin is covered is not specified (the individuals are listed in subsection (3), which is not included)",
  "entitlement_or_requirement": "Leave of absence without pay because of the death of an individual described in subsection (3)",
  "threshold": "At least two consecutive weeks of employment",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "is entitled to a leave of absence without pay because of the death of an individual described in subsection (3)"
}
```
- **Reviewed:** yes

## T034
- **Split:** train
- **Type:** eligibility, threshold
- **Jurisdiction:** Ontario
- **Question:** I've been given notice in a mass layoff in Ontario. Can I take time off to look for a new job?
- **Excerpts:**
  - [ON s. 50.3(1)] (1) Subject to subsection (10), an employee to whom notice has been given under section 58 of the Act is entitled to a leave of absence without pay to engage in activities related to obtaining employment, including job searches, interviews and training.
  - [ON s. 50.3(4)] (4) An employee who wishes to take a leave under this section shall advise the employer that the employee will be doing so at least three days before beginning the leave, if possible.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "50.3(1), 50.3(4)",
  "eligibility": "Employee has been given notice under section 58 of the Act",
  "entitlement_or_requirement": "Leave of absence without pay for activities related to obtaining employment, including job searches, interviews and training; the employee must advise the employer at least three days before beginning the leave, if possible",
  "threshold": "Advise the employer at least three days before beginning the leave, if possible",
  "exceptions": [
    "Subject to subsection (10), which is not included in the excerpt"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "to engage in activities related to obtaining employment, including job searches, interviews and training"
}
```
- **Reviewed:** yes

## T035
- **Split:** train
- **Type:** exception
- **Jurisdiction:** Ontario
- **Question:** Do my health and dental benefits continue while I'm on leave in Ontario?
- **Excerpts:**
  - [ON s. 51(1)] (1) During any leave under this Part, an employee continues to participate in each type of benefit plan described in subsection (2) that is related to his or her employment unless he or she elects in writing not to do so.
  - [ON s. 51(2)] (2) Subsection (1) applies with respect to pension plans, life insurance plans, accidental death plans, extended health plans, dental plans and any prescribed type of benefit plan.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "51(1), 51(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employee continues to participate in pension, life insurance, accidental death, extended health, dental and other prescribed benefit plans during the leave",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Unless the employee elects in writing not to participate"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "an employee continues to participate in each type of benefit plan described in subsection (2) that is related to his or her employment unless he or she elects in writing not to do so"
}
```
- **Reviewed:** yes

## T036
- **Split:** train
- **Type:** requirement
- **Jurisdiction:** Ontario
- **Question:** When my leave ends in Ontario, do I get my old job back?
- **Excerpts:**
  - [ON s. 53(1)] (1) Upon the conclusion of an employee’s leave under this Part, the employer shall reinstate the employee to the position the employee most recently held with the employer, if it still exists, or to a comparable position, if it does not.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "53(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must reinstate the employee to the position most recently held, if it still exists, or to a comparable position if it does not",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employer shall reinstate the employee to the position the employee most recently held with the employer, if it still exists, or to a comparable position, if it does not"
}
```
- **Reviewed:** yes

## T037
- **Split:** train
- **Type:** eligibility, threshold
- **Jurisdiction:** Ontario
- **Question:** I've worked in Ontario for six months. Can I be fired without any notice?
- **Excerpts:**
  - [ON s. 54] No employer shall terminate the employment of an employee who has been continuously employed for three months or more unless the employer, / (a) has given to the employee written notice of termination in accordance with section 57 or 58 and the notice has expired; or / (b) has complied with section 61.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "54",
  "eligibility": "Employee has been continuously employed for three months or more",
  "entitlement_or_requirement": "Employer must give written notice of termination under section 57 or 58 that has expired, or comply with section 61",
  "threshold": "Three months or more of continuous employment",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "No employer shall terminate the employment of an employee who has been continuously employed for three months or more unless the employer"
}
```
- **Reviewed:** yes

## T038
- **Split:** train
- **Type:** missing, distractor
- **Jurisdiction:** Ontario
- **Question:** How many weeks of notice is an Ontario employer required to give someone with four years of service?
- **Excerpts:**
  - [ON s. 54] No employer shall terminate the employment of an employee who has been continuously employed for three months or more unless the employer, / (a) has given to the employee written notice of termination in accordance with section 57 or 58 and the notice has expired; or / (b) has complied with section 61.
  - [ON s. 60(1)] (1) During a notice period under section 57 or 58, the employer, / (a) shall not reduce the employee’s wage rate or alter any other term or condition of employment; / (b) shall in each week pay the employee the wages the employee is entitled to receive, which in no case shall be less than his or her regular wages for a regular work week; and / (c) shall continue to make whatever benefit plan contributions would be required to be made in order to maintain the employee’s benefits under the plan until the end of the notice period.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "54",
  "eligibility": "Employee has been continuously employed for three months or more",
  "entitlement_or_requirement": "Written notice of termination in accordance with section 57 or 58, or compliance with section 61",
  "threshold": "Not specified in the excerpt (the notice periods are in section 57, which is not included)",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "has given to the employee written notice of termination in accordance with section 57 or 58 and the notice has expired"
}
```
- **Reviewed:** yes

## T039
- **Split:** train
- **Type:** list
- **Jurisdiction:** Ontario
- **Question:** During my notice period in Ontario, can my employer cut my pay?
- **Excerpts:**
  - [ON s. 60(1)] (1) During a notice period under section 57 or 58, the employer, / (a) shall not reduce the employee’s wage rate or alter any other term or condition of employment; / (b) shall in each week pay the employee the wages the employee is entitled to receive, which in no case shall be less than his or her regular wages for a regular work week; and / (c) shall continue to make whatever benefit plan contributions would be required to be made in order to maintain the employee’s benefits under the plan until the end of the notice period.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "60(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "During the notice period the employer must not reduce the wage rate or alter other terms, must pay at least regular wages for a regular work week, and must keep making benefit plan contributions",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "shall not reduce the employee’s wage rate or alter any other term or condition of employment"
}
```
- **Reviewed:** yes

## T040
- **Split:** train
- **Type:** optional, requirement
- **Jurisdiction:** Ontario
- **Question:** Can my Ontario employer let me go right away instead of giving me notice?
- **Excerpts:**
  - [ON s. 61(1)] (1) An employer may terminate the employment of an employee without notice or with less notice than is required under section 57 or 58 if the employer, / (a) pays to the employee termination pay in a lump sum equal to the amount the employee would have been entitled to receive under section 60 had notice been given in accordance with that section; and / (b) continues to make whatever benefit plan contributions would be required to be made in order to maintain the benefits to which the employee would have been entitled had he or she continued to be employed during the period of notice that he or she would otherwise have been entitled to receive.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "61(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer may terminate without notice or with less notice if it pays lump-sum termination pay equal to what the employee would have received during the notice period and continues benefit plan contributions for that period",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "optional",
  "supporting_quote": "pays to the employee termination pay in a lump sum equal to the amount the employee would have been entitled to receive under section 60"
}
```
- **Reviewed:** yes

## T041
- **Split:** train
- **Type:** eligibility, threshold
- **Jurisdiction:** Ontario
- **Question:** Am I owed severance pay in Ontario after 6 years at a large company?
- **Excerpts:**
  - [ON s. 64(1)] (1) An employer who severs an employment relationship with an employee shall pay severance pay to the employee if the employee was employed by the employer for five years or more and, / (a) the severance occurred because of a permanent discontinuance of all or part of the employer’s business at an establishment and the employee is one of 50 or more employees who have their employment relationship severed within a six-month period as a result; or / (b) the employer has a payroll of $2.5 million or more.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "64(1)",
  "eligibility": "Employee employed for five years or more, and either the severance results from a permanent discontinuance affecting 50 or more employees within six months, or the employer has a payroll of $2.5 million or more",
  "entitlement_or_requirement": "Employer must pay severance pay",
  "threshold": "Five years or more of employment; 50 or more employees severed within six months, or payroll of $2.5 million or more",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "shall pay severance pay to the employee if the employee was employed by the employer for five years or more"
}
```
- **Reviewed:** yes

## T042
- **Split:** train
- **Type:** calculation
- **Jurisdiction:** Ontario
- **Question:** How is severance pay calculated in Ontario?
- **Excerpts:**
  - [ON s. 65(1)] (1) Severance pay under this section shall be calculated by multiplying the employee’s regular wages for a regular work week by the sum of, / (a) the number of years of employment the employee has completed; and / (b) the number of months of employment not included in clause (a) that the employee has completed, divided by 12.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "65(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Regular wages for a regular work week multiplied by the number of completed years of employment plus completed extra months divided by 12",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "Severance pay under this section shall be calculated by multiplying the employee’s regular wages for a regular work week by the sum of"
}
```
- **Reviewed:** yes

## T043
- **Split:** train
- **Type:** list, distractor
- **Jurisdiction:** Ontario
- **Question:** Can my employer in Ontario make me take a lie detector test?
- **Excerpts:**
  - [ON s. 69] Subject to section 71, an employee has a right not to, / (a) take a lie detector test; / (b) be asked to take a lie detector test; or / (c) be required to take a lie detector test.
  - [ON s. 14.1(2)] (2) If payment is made by cash or cheque, the employer shall ensure that the cash or cheque is given to the employee at his or her workplace or at some other place agreeable to the employee.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "lie_detectors",
  "section": "69",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "An employee has a right not to take, be asked to take, or be required to take a lie detector test",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Subject to section 71, which is not included in the excerpt"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "an employee has a right not to"
}
```
- **Reviewed:** yes

## T044
- **Split:** train
- **Type:** threshold, optional
- **Jurisdiction:** Ontario
- **Question:** I work at a store in Ontario. Can I refuse to work on a public holiday, and can I change my mind after agreeing?
- **Excerpts:**
  - [ON s. 73(1)] (1) An employee may refuse to work on a public holiday or a day declared by proclamation of the Lieutenant Governor to be a holiday for the purposes of the Retail Business Holidays Act.
  - [ON s. 73(3)] (3) An employee who agrees to work on a day referred to in subsection (1) or (2) may then decline to work on that day, but only if he or she gives the employer notice that he or she declines at least 48 hours before he or she was to commence work on that day.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "retail_business_establishments",
  "section": "73(1), 73(3)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "An employee may refuse to work on a public holiday; an employee who agreed may later decline by giving notice",
  "threshold": "Notice at least 48 hours before the employee was to start work that day",
  "exceptions": [],
  "mandatory": "optional",
  "supporting_quote": "at least 48 hours before he or she was to commence work on that day"
}
```
- **Reviewed:** yes

## T045
- **Split:** train
- **Type:** missing, distractor
- **Jurisdiction:** Ontario
- **Question:** Is there a limit on how many hours a 16-year-old can work in a day in Ontario?
- **Excerpts:**
  - [ON s. 21.2(1)] (1) If an employee who regularly works more than three hours a day is required to present himself or herself for work but works less than three hours, despite being available to work longer, the employer shall pay the employee wages for three hours, equal to the greater of the following: / 1. The sum of, / i. the amount the employee earned for the time worked, and / ii. wages equal to the employee’s regular rate for the remainder of the time. / 2. Wages equal to the employee’s regular rate for three hours of work.
  - [ON s. 21.1.2(1)] (1) An employer that, on January 1 of any year, employs 25 or more employees shall, before March 1 of that year, ensure it has a written policy in place for all employees with respect to disconnecting from work that includes the date the policy was prepared and the date any changes were made to the policy.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "hours_for_young_workers",
  "section": "Not specified in the excerpt",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Not specified in the excerpt",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": ""
}
```
- **Reviewed:** yes

## T046
- **Split:** train
- **Type:** missing
- **Jurisdiction:** Ontario
- **Question:** How much notice must an Ontario employer give when laying off 60 employees at once?
- **Excerpts:**
  - [ON s. 58(1)] (1) Despite section 57, the employer shall give notice of termination in the prescribed manner and for the prescribed period if the employer terminates the employment of 50 or more employees at the employer’s establishment in the same four-week period.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "58(1)",
  "eligibility": "Employer terminates the employment of 50 or more employees at an establishment in the same four-week period",
  "entitlement_or_requirement": "Notice of termination must be given in the prescribed manner and for the prescribed period",
  "threshold": "Not specified in the excerpt (the notice period is prescribed by regulation)",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employer shall give notice of termination in the prescribed manner and for the prescribed period"
}
```
- **Reviewed:** yes

## T047
- **Split:** train
- **Type:** list
- **Jurisdiction:** Ontario
- **Question:** What has to be on my pay statement in Ontario?
- **Excerpts:**
  - [ON s. 12(1)] (1) On or before an employee’s pay day, the employer shall give to the employee a written statement setting out, / (a) the pay period for which the wages are being paid; / (b) the wage rate, if there is one; / (c) the gross amount of wages and, unless the information is provided to the employee in some other manner, how that amount was calculated; / (d) Repealed: 2002, c. 18, Sched. J, s. 3 (3). / (e) the amount and purpose of each deduction from wages; / (f) any amount with respect to room or board that is deemed to have been paid to the employee under subsection 23 (2); and / (g) the net amount of wages being paid to the employee.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "payment_of_wages",
  "section": "12(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must give a written statement on or before pay day setting out the pay period, the wage rate (if any), the gross wages and (unless provided in some other manner) how they were calculated, each deduction and its purpose, any room or board amount deemed paid, and the net wages",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "On or before an employee’s pay day, the employer shall give to the employee a written statement setting out"
}
```
- **Reviewed:** yes

## T048
- **Split:** train
- **Type:** list
- **Jurisdiction:** British Columbia
- **Question:** Can a BC employer lie about the pay to get me to take a job?
- **Excerpts:**
  - [BC s. 8] An employer must not induce, influence or persuade a person to become an employee, or to work or to be available for work, by misrepresenting any of the following: / (a) the availability of a position; / (b) the type of work; / (c) the wages; / (d) the conditions of employment.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "hiring",
  "section": "8",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "An employer must not induce or persuade a person to become an employee or work by misrepresenting the availability of a position, the type of work, the wages, or the conditions of employment",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employer must not induce, influence or persuade a person to become an employee"
}
```
- **Reviewed:** yes

## T049
- **Split:** train
- **Type:** eligibility, threshold
- **Jurisdiction:** British Columbia
- **Question:** Can my 14-year-old work a part-time job in BC?
- **Excerpts:**
  - [BC s. 9(2)] (2) A person must not employ a child / (a) who is under 14 years of age without the director's permission, or / (b) who is 14 or 15 years of age / (i) to perform light work without the written consent of the child's parent or guardian, or / (ii) to perform any other work without the director's permission.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "hiring",
  "section": "9(2)",
  "eligibility": "Child who is 14 or 15 years of age",
  "entitlement_or_requirement": "A 14- or 15-year-old may do light work only with the written consent of a parent or guardian, and any other work only with the director's permission; a child under 14 needs the director's permission",
  "threshold": "Under 14: director's permission; 14 or 15: parent or guardian's written consent for light work",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "to perform light work without the written consent of the child's parent or guardian"
}
```
- **Reviewed:** yes

## T050
- **Split:** train
- **Type:** threshold, exception
- **Jurisdiction:** British Columbia
- **Question:** Can a 17-year-old work in a hazardous industry in BC?
- **Excerpts:**
  - [BC s. 9.1(2)] (2) A person must not employ a child / (a) who is under 16 years of age in a hazardous industry or in hazardous work, or / (b) who is at least 16 years of age but under 19 years of age in a hazardous industry or in hazardous work unless the child has attained the prescribed age in respect of the hazardous industry or hazardous work.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "hiring",
  "section": "9.1(2)",
  "eligibility": "Child who is at least 16 but under 19 years of age",
  "entitlement_or_requirement": "Must not be employed in a hazardous industry or hazardous work unless the child has reached the prescribed age for that industry or work; under 16 is not allowed at all",
  "threshold": "Not specified in the excerpt (the age is prescribed by regulation)",
  "exceptions": [
    "Allowed if the child has attained the prescribed age for that hazardous industry or work"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "unless the child has attained the prescribed age in respect of the hazardous industry or hazardous work"
}
```
- **Reviewed:** yes

## T051
- **Split:** train
- **Type:** exception
- **Jurisdiction:** British Columbia
- **Question:** Can a recruiter in BC charge me a fee to find me a job?
- **Excerpts:**
  - [BC s. 10(1)] (1) A person must not request, charge or receive, directly or indirectly, from a person seeking employment a payment for / (a) employing or obtaining employment for the person seeking employment, or / (b) providing information about employers seeking employees.
  - [BC s. 10(2)] (2) A person does not contravene this section by requesting, charging or receiving payment for any form of advertisement from the person who placed the advertisement.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "hiring",
  "section": "10(1), 10(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "No one may request, charge or receive a payment from a job seeker for employing or obtaining employment for them, or for providing information about employers seeking employees",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Charging for an advertisement to the person who placed the advertisement is allowed (s. 10(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "A person must not request, charge or receive, directly or indirectly, from a person seeking employment a payment"
}
```
- **Reviewed:** yes

## T052
- **Split:** train
- **Type:** threshold
- **Jurisdiction:** British Columbia
- **Question:** How often does a BC employer have to pay wages?
- **Excerpts:**
  - [BC s. 17(1)] (1) At least semimonthly and within 8 days after the end of the pay period, an employer must pay to an employee all wages earned by the employee in a pay period.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "17(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must pay all wages earned in a pay period at least semimonthly and within 8 days after the end of the pay period",
  "threshold": "At least semimonthly; within 8 days after the end of the pay period",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "At least semimonthly and within 8 days after the end of the pay period"
}
```
- **Reviewed:** yes

## T053
- **Split:** train
- **Type:** threshold, eligibility
- **Jurisdiction:** British Columbia
- **Question:** What happens to my last paycheque in BC if my old employer can't find me?
- **Excerpts:**
  - [BC s. 19(1.1)] (1.1) If an employer cannot locate an employee to pay the employee's wages, the employer must pay the wages to the director within 60 days after the wages became payable.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "19(1.1)",
  "eligibility": "Employer cannot locate an employee to pay wages",
  "entitlement_or_requirement": "Employer must pay the wages to the director",
  "threshold": "Within 60 days after the wages became payable",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employer must pay the wages to the director within 60 days after the wages became payable"
}
```
- **Reviewed:** yes

## T054
- **Split:** train
- **Type:** list, eligibility
- **Jurisdiction:** British Columbia
- **Question:** Can my BC employer pay me by direct deposit?
- **Excerpts:**
  - [BC s. 20] An employer must pay all wages / (a) in Canadian currency, / (b) by cheque, draft or money order, payable on demand, drawn on a savings institution, or / (c) by deposit to the credit of an employee's account in a savings institution, if authorized by the employee in writing or by a collective agreement.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "20",
  "eligibility": "Direct deposit must be authorized by the employee in writing or by a collective agreement",
  "entitlement_or_requirement": "Wages must be paid in Canadian currency, by cheque, draft or money order payable on demand, or by deposit to the employee's account",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "by deposit to the credit of an employee's account in a savings institution, if authorized by the employee in writing or by a collective agreement"
}
```
- **Reviewed:** yes

## T055
- **Split:** train
- **Type:** exception
- **Jurisdiction:** British Columbia
- **Question:** Can my BC employer deduct the cost of a broken dish from my wages?
- **Excerpts:**
  - [BC s. 21(1)] (1) Except as permitted or required by this Act or any other enactment of British Columbia or Canada, an employer must not, directly or indirectly, withhold, deduct or require payment of all or part of an employee's wages for any purpose.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "21(1)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must not withhold, deduct or require payment of wages for any purpose",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Unless permitted or required by the Act or another enactment of British Columbia or Canada"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "an employer must not, directly or indirectly, withhold, deduct or require payment of all or part of an employee's wages for any purpose"
}
```
- **Reviewed:** yes

## T056
- **Split:** train
- **Type:** exception, requirement
- **Jurisdiction:** British Columbia
- **Question:** My BC employer requires a uniform. Who pays for it and for cleaning it?
- **Excerpts:**
  - [BC s. 25(1)] (1) An employer who requires an employee to wear special clothing must, without charge to the employee, / (a) provide the special clothing, and / (b) clean and maintain it in a good state of repair, unless the employee is bound by an agreement made under subsection (2).
  - [BC s. 25(2)] (2) If an employer and the majority of the affected employees at a workplace agree that the employees will clean their own special clothing and maintain it in a good state of repair, / (a) the agreement binds all employees at that workplace who are required to wear special clothing, / (b) the employer must reimburse, in accordance with the agreement, each employee bound by the agreement for the cost of cleaning and maintaining the special clothing, and / (c) the employer must retain for 4 years records of the agreement and the amounts reimbursed.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "special_clothing",
  "section": "25(1), 25(2)",
  "eligibility": "Employer requires the employee to wear special clothing",
  "entitlement_or_requirement": "Employer must provide the special clothing and clean and maintain it without charge",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "If the employer and a majority of affected employees agree that employees clean and maintain it, the employer must reimburse them under the agreement and keep records for 4 years (s. 25(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "An employer who requires an employee to wear special clothing must, without charge to the employee,"
}
```
- **Reviewed:** yes

## T057
- **Split:** train
- **Type:** optional, eligibility
- **Jurisdiction:** British Columbia
- **Question:** Can my BC employer give me my pay stub online only?
- **Excerpts:**
  - [BC s. 27(2)] (2) An employer may provide a wage statement to an employee electronically if the employer provides to the employee, through the workplace, / (a) confidential access to the electronic wage statement, and / (b) a means of making a paper copy of that wage statement.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "27(2)",
  "eligibility": "Employer provides, through the workplace, confidential access to the electronic statement and a means of making a paper copy",
  "entitlement_or_requirement": "Employer may provide the wage statement electronically",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "optional",
  "supporting_quote": "An employer may provide a wage statement to an employee electronically"
}
```
- **Reviewed:** yes

## T058
- **Split:** train
- **Type:** list, threshold
- **Jurisdiction:** British Columbia
- **Question:** How long does a BC employer have to keep payroll records?
- **Excerpts:**
  - [BC s. 28(2)] (2) Payroll records must / (a) be in English, / (b) be kept at the employer's principal place of business in British Columbia, and / (c) be retained by the employer for 4 years after the date on which the payroll records were created.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "records",
  "section": "28(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Payroll records must be in English, kept at the employer's principal place of business in British Columbia, and retained",
  "threshold": "4 years after the date the records were created",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "be retained by the employer for 4 years after the date on which the payroll records were created"
}
```
- **Reviewed:** yes

## T059
- **Split:** train
- **Type:** exception
- **Jurisdiction:** British Columbia
- **Question:** Can my BC employer keep part of my tips?
- **Excerpts:**
  - [BC s. 30.3(1)] (1) An employer must not / (a) withhold gratuities from an employee, / (b) make a deduction from an employee's gratuities, or / (c) require an employee to return or give the employee's gratuities to the employer.
  - [BC s. 30.3(2)] (2) Subsection (1) does not apply if an employer is authorized or required under a law of British Columbia or Canada or by a court to withhold gratuities from an employee, make a deduction from an employee's gratuities or require an employee to return or give the employee's gratuities to the employer.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "tips_and_gratuities",
  "section": "30.3(1), 30.3(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must not withhold, deduct from, or require employees to return or give their gratuities",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Does not apply if a law of British Columbia or Canada or a court authorizes or requires it (s. 30.3(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "An employer must not"
}
```
- **Reviewed:** yes

## T060
- **Split:** train
- **Type:** optional, exception
- **Jurisdiction:** British Columbia
- **Question:** Is a tip pool allowed in BC, and can the owner take a cut?
- **Excerpts:**
  - [BC s. 30.4(1)] (1) Despite section 30.3 (1), an employer may withhold gratuities from an employee, make a deduction from an employee's gratuities or require the employee to return or give the employee's gratuities to the employer if the employer collects and redistributes gratuities among some or all of the employer's employees.
  - [BC s. 30.4(3)] (3) Subject to subsections (4) and (5), an employer or a director or shareholder of an employer may not share in gratuities redistributed under subsection (1).
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "tips_and_gratuities",
  "section": "30.4(1), 30.4(3)",
  "eligibility": "Employer collects and redistributes gratuities among some or all employees",
  "entitlement_or_requirement": "Employer may pool and redistribute gratuities, but the employer, or a director or shareholder, may not share in them",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Subject to subsections (4) and (5), which are not included in the excerpt"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "an employer or a director or shareholder of an employer may not share in gratuities redistributed under subsection (1)"
}
```
- **Reviewed:** yes

## T061
- **Split:** train
- **Type:** eligibility, threshold
- **Jurisdiction:** British Columbia
- **Question:** I started a new job in BC three weeks ago. Do I get paid for the upcoming statutory holiday?
- **Excerpts:**
  - [BC s. 44] An employer must comply with section 45 or 46 in respect of an employee who has been employed by the employer for at least 30 calendar days before the statutory holiday and has / (a) worked or earned wages for 15 of the 30 calendar days preceding the statutory holiday, or / (b) worked under an averaging agreement under section 37 at any time within that 30 calendar day period.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "statutory_holidays",
  "section": "44",
  "eligibility": "Employed for at least 30 calendar days before the statutory holiday and worked or earned wages on 15 of the 30 days before it (or worked under an averaging agreement in that period)",
  "entitlement_or_requirement": "Employer must comply with section 45 or 46 (sections 45 and 46 are not included in the excerpt, so the holiday pay amount is not stated)",
  "threshold": "At least 30 calendar days of employment; worked or earned wages on 15 of the preceding 30 days",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "employed by the employer for at least 30 calendar days before the statutory holiday"
}
```
- **Reviewed:** yes

## T062
- **Split:** train
- **Type:** threshold, distractor
- **Jurisdiction:** British Columbia
- **Question:** I just quit my job in BC. How soon does my employer have to pay my final wages?
- **Excerpts:**
  - [BC s. 18(1)] (1) An employer must pay all wages owing to an employee within 48 hours after the employer terminates the employment.
  - [BC s. 18(2)] (2) An employer must pay all wages owing to an employee within 6 days after the employee terminates the employment.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "18(2)",
  "eligibility": "The employee terminates the employment",
  "entitlement_or_requirement": "Employer must pay all wages owing to the employee",
  "threshold": "Within 6 days after the employee terminates the employment",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employer must pay all wages owing to an employee within 6 days after the employee terminates the employment."
}
```
- **Reviewed:** yes

## T063
- **Split:** train
- **Type:** optional, eligibility
- **Jurisdiction:** British Columbia
- **Question:** Can my BC workplace move a statutory holiday to a different day?
- **Excerpts:**
  - [BC s. 48(1)] (1) An employer may for one or more employees at a workplace substitute another day off for a statutory holiday if the employer and the employee or a majority of those employees, as the case may be, agree to the substitution.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "statutory_holidays",
  "section": "48(1)",
  "eligibility": "The employer and the employee, or a majority of the affected employees, agree",
  "entitlement_or_requirement": "Employer may substitute another day off for a statutory holiday",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "optional",
  "supporting_quote": "if the employer and the employee or a majority of those employees, as the case may be, agree to the substitution"
}
```
- **Reviewed:** yes

## T064
- **Split:** train
- **Type:** threshold, missing
- **Jurisdiction:** British Columbia
- **Question:** I'm too sick to work for a few weeks. How much unpaid leave can I take in BC?
- **Excerpts:**
  - [BC s. 49.01(2)] (2) After the prescribed number of consecutive days, if any, of employment with an employer, an employee who, due to serious personal illness or injury, is unable to work for at least one week is entitled to up to 27 weeks of unpaid leave in any period of 52 weeks.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "49.01(2)",
  "eligibility": "Employee is unable to work for at least one week due to serious personal illness or injury, after the prescribed number of consecutive days of employment (if any)",
  "entitlement_or_requirement": "Unpaid leave",
  "threshold": "Up to 27 weeks in any period of 52 weeks; minimum employment period not specified in the excerpt (prescribed)",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "is entitled to up to 27 weeks of unpaid leave in any period of 52 weeks"
}
```
- **Reviewed:** yes

## T065
- **Split:** train
- **Type:** threshold
- **Jurisdiction:** British Columbia
- **Question:** When can I start pregnancy leave in BC, and how long is it?
- **Excerpts:**
  - [BC s. 50(1)] (1) A pregnant employee who requests leave under this subsection is entitled to up to 17 consecutive weeks of unpaid leave, which must be taken during the period that begins / (a) no earlier than 13 weeks before the expected birth date, and / (b) no later than the actual birth date / and ends no later than 17 weeks after the leave begins.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "50(1)",
  "eligibility": "Pregnant employee who requests the leave",
  "entitlement_or_requirement": "Up to 17 consecutive weeks of unpaid leave",
  "threshold": "Starts no earlier than 13 weeks before the expected birth date and no later than the actual birth date; ends no later than 17 weeks after it begins",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "is entitled to up to 17 consecutive weeks of unpaid leave"
}
```
- **Reviewed:** yes

## T066
- **Split:** train
- **Type:** eligibility, threshold
- **Jurisdiction:** British Columbia
- **Question:** My baby needs extra care. Can I extend parental leave in BC, and how do I ask?
- **Excerpts:**
  - [BC s. 51(2)] (2) If the child has a physical, psychological or emotional condition requiring an additional period of parental care, an employee who requests leave under this subsection is entitled to up to an additional 5 consecutive weeks of unpaid leave, beginning immediately after the end of the leave taken under subsection (1).
  - [BC s. 51(3)] (3) A request for leave must / (a) be given in writing to the employer, / (b) if the request is for leave under subsection (1) (a) or (b), be given to the employer at least 4 weeks before the employee proposes to begin leave, and / (c) if required by the employer, be accompanied by a medical practitioner's or nurse practitioner's certificate or other evidence of the employee's entitlement to leave.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "51(2), 51(3)",
  "eligibility": "The child has a physical, psychological or emotional condition requiring an additional period of parental care",
  "entitlement_or_requirement": "Up to 5 additional consecutive weeks of unpaid leave, immediately after the parental leave; the request must be in writing and, if the employer requires, supported by a certificate or other evidence",
  "threshold": "Up to 5 additional weeks",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "is entitled to up to an additional 5 consecutive weeks of unpaid leave"
}
```
- **Reviewed:** yes

## T067
- **Split:** train
- **Type:** threshold
- **Jurisdiction:** British Columbia
- **Question:** How many days off do I get in BC to deal with my kid's school or health stuff?
- **Excerpts:**
  - [BC s. 52] An employee is entitled to up to 5 days of unpaid leave during each employment year to meet responsibilities related to / (a) the care, health or education of a child in the employee's care, or / (b) the care or health of any other member of the employee's immediate family.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "52",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Unpaid leave to meet responsibilities for the care, health or education of a child in the employee's care, or the care or health of another immediate family member",
  "threshold": "Up to 5 days per employment year",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employee is entitled to up to 5 days of unpaid leave during each employment year"
}
```
- **Reviewed:** yes

## T068
- **Split:** train
- **Type:** missing
- **Jurisdiction:** British Columbia
- **Question:** Can my BC employer ask for a doctor's note when I take family responsibility leave?
- **Excerpts:**
  - [BC s. 52] An employee is entitled to up to 5 days of unpaid leave during each employment year to meet responsibilities related to / (a) the care, health or education of a child in the employee's care, or / (b) the care or health of any other member of the employee's immediate family.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "Not specified in the excerpt",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Not specified in the excerpt",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": ""
}
```
- **Reviewed:** yes

## T069
- **Split:** train
- **Type:** threshold, eligibility
- **Jurisdiction:** British Columbia
- **Question:** How long can I take off in BC to care for a family member who may be dying?
- **Excerpts:**
  - [BC s. 52.1(2)] (2) An employee who requests leave under this section is entitled to up to 27 weeks of unpaid leave to provide care or support to a family member if a medical practitioner or nurse practitioner issues a certificate stating that the family member has a serious medical condition with a significant risk of death within 26 weeks, or such other period as may be prescribed, after / (a) the date the certificate is issued, or / (b) if the leave began before the date the certificate is issued, the date the leave began.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "52.1(2)",
  "eligibility": "A medical practitioner or nurse practitioner certifies that the family member has a serious medical condition with a significant risk of death within 26 weeks (or another prescribed period)",
  "entitlement_or_requirement": "Unpaid leave to provide care or support to a family member",
  "threshold": "Up to 27 weeks",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "is entitled to up to 27 weeks of unpaid leave to provide care or support to a family member"
}
```
- **Reviewed:** yes

## T070
- **Split:** train
- **Type:** threshold, exception
- **Jurisdiction:** British Columbia
- **Question:** How much leave do I get in BC if my child dies?
- **Excerpts:**
  - [BC s. 52.4(1)] (1) If a child of an employee dies and the employee requests leave under this section, the employee is entitled to unpaid leave for a period of up to 104 weeks.
  - [BC s. 52.4(2)] (2) If an employee is charged with a crime that resulted in the death of the employee's child, the employee is not entitled, or, if already on leave, is no longer entitled, to leave under this section.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "52.4(1), 52.4(2)",
  "eligibility": "A child of the employee dies and the employee requests the leave",
  "entitlement_or_requirement": "Unpaid leave",
  "threshold": "Up to 104 weeks",
  "exceptions": [
    "Not entitled, or no longer entitled, if the employee is charged with a crime that resulted in the child's death (s. 52.4(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "the employee is entitled to unpaid leave for a period of up to 104 weeks"
}
```
- **Reviewed:** yes

## T071
- **Split:** train
- **Type:** threshold
- **Jurisdiction:** British Columbia
- **Question:** Is domestic violence leave paid in BC?
- **Excerpts:**
  - [BC s. 52.5(4)] (4) If an employee requests leave under subsection (3), the employee is entitled during each calendar year to / (a) up to 5 days of paid leave, / (b) up to 5 days of unpaid leave, and / (c) up to 15 weeks of additional unpaid leave.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "52.5(4)",
  "eligibility": "Employee requests leave under subsection (3)",
  "entitlement_or_requirement": "Each calendar year: up to 5 days of paid leave, up to 5 days of unpaid leave, and up to 15 weeks of additional unpaid leave",
  "threshold": "5 days paid; 5 days unpaid; 15 weeks additional unpaid, per calendar year",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "(a) up to 5 days of paid leave,"
}
```
- **Reviewed:** yes

## T072
- **Split:** train
- **Type:** threshold, eligibility
- **Jurisdiction:** British Columbia
- **Question:** My teenage daughter is critically ill. How much leave can I take in BC?
- **Excerpts:**
  - [BC s. 52.11(2)] (2) An employee who requests leave under this section is entitled to the following unpaid leave to provide care or support to a family member if a medical practitioner or nurse practitioner issues a certificate in accordance with subsection (4): / (a) up to 36 weeks of unpaid leave to provide care or support to a family member who is under 19 years of age at the start of the leave; / (b) up to 16 weeks of unpaid leave to provide care or support to a family member who is 19 years of age or older.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "52.11(2)",
  "eligibility": "A medical practitioner or nurse practitioner issues a certificate in accordance with subsection (4)",
  "entitlement_or_requirement": "Unpaid leave to provide care or support to a family member",
  "threshold": "Up to 36 weeks for a family member under 19 at the start of the leave; up to 16 weeks for a family member 19 or older",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "up to 36 weeks of unpaid leave to provide care or support to a family member who is under 19 years of age at the start of the leave"
}
```
- **Reviewed:** yes

## T073
- **Split:** train
- **Type:** requirement
- **Jurisdiction:** British Columbia
- **Question:** Can my BC employer fire me for going on maternity leave, and do I get my job back after?
- **Excerpts:**
  - [BC s. 54(2)] (2) An employer must not, because of an employee's pregnancy or a leave allowed by this Part, / (a) terminate employment, or / (b) change a condition of employment without the employee's written consent.
  - [BC s. 54(3)] (3) As soon as the leave ends, the employer must place the employee / (a) in the position the employee held before taking leave under this Part, or / (b) in a comparable position.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "54(2), 54(3)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Employer must not terminate employment or change a condition of employment without written consent because of pregnancy or leave, and must return the employee to the same or a comparable position when the leave ends",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employer must not, because of an employee's pregnancy or a leave allowed by this Part"
}
```
- **Reviewed:** yes

## T074
- **Split:** train
- **Type:** threshold
- **Jurisdiction:** British Columbia
- **Question:** How much severance am I owed in BC after 5 years at my job?
- **Excerpts:**
  - [BC s. 63(1)] (1) After 3 consecutive months of employment, the employer becomes liable to pay an employee an amount equal to one week's wages as compensation for length of service.
  - [BC s. 63(2)] (2) The employer's liability for compensation for length of service increases as follows: / (a) after 12 consecutive months of employment, to an amount equal to 2 weeks' wages; / (b) after 3 consecutive years of employment, to an amount equal to 3 weeks' wages plus one additional week's wages for each additional year of employment, to a maximum of 8 weeks' wages.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "termination",
  "section": "63(1), 63(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Compensation for length of service: one week's wages after 3 consecutive months, 2 weeks after 12 consecutive months, and 3 weeks after 3 consecutive years plus one week for each additional year, to a maximum of 8 weeks",
  "threshold": "5 weeks' wages after 5 consecutive years (3 weeks plus 1 week for each of the 2 additional years; maximum 8 weeks)",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "after 3 consecutive years of employment, to an amount equal to 3 weeks' wages plus one additional week's wages for each additional year of employment, to a maximum of 8 weeks' wages"
}
```
- **Reviewed:** yes

## T075
- **Split:** train
- **Type:** list, threshold
- **Jurisdiction:** British Columbia
- **Question:** What does a BC employer have to do before laying off 60 people at one site?
- **Excerpts:**
  - [BC s. 64(1)] (1) If the employment of 50 or more employees at a single location is to be terminated within any 2 month period, the employer must give written notice of group termination to all of the following: / (a) each employee who will be affected; / (b) a trade union certified to represent, or recognized by the employer as the bargaining agent of, any affected employees; / (c) the minister.
  - [BC s. 64(2)] (2) The notice of group termination must specify all of the following: / (a) the number of employees who will be affected; / (b) the effective date or dates of the termination; / (c) the reasons for the termination.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "termination",
  "section": "64(1), 64(2)",
  "eligibility": "Employment of 50 or more employees at a single location is to be terminated within any 2-month period",
  "entitlement_or_requirement": "Written notice of group termination to each affected employee, any union representing them, and the minister, stating the number affected, the effective date(s), and the reasons",
  "threshold": "50 or more employees within any 2-month period",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "If the employment of 50 or more employees at a single location is to be terminated within any 2 month period"
}
```
- **Reviewed:** yes

## T076
- **Split:** train
- **Type:** rule, threshold
- **Jurisdiction:** British Columbia
- **Question:** My fixed-term contract in BC ended but I kept working. Am I still on a fixed term?
- **Excerpts:**
  - [BC s. 65(2)] (2) If an employee who is employed for a definite term or specific work continues to be employed for at least 3 months after completing the definite term or specific work, the employment is / (a) deemed not to be for a definite term or specific work, and / (b) deemed to have started at the beginning of the definite term or specific work.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "termination",
  "section": "65(2)",
  "eligibility": "Employee hired for a definite term or specific work continues to be employed for at least 3 months after it ends",
  "entitlement_or_requirement": "Employment is deemed not to be for a definite term or specific work, and deemed to have started at the beginning of the term",
  "threshold": "At least 3 months after completing the term or work",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "continues to be employed for at least 3 months after completing the definite term or specific work"
}
```
- **Reviewed:** yes

## T077
- **Split:** train
- **Type:** definition, threshold
- **Jurisdiction:** British Columbia
- **Question:** What counts as a week of layoff in BC?
- **Excerpts:**
  - [BC s. 62] In this Part, *week of layoff* means a week in which an employee earns less than 50% of the employee's weekly wages, at the regular wage, averaged over the previous 8 weeks.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "termination",
  "section": "62",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "A week in which the employee earns less than 50% of their weekly wages at the regular wage, averaged over the previous 8 weeks",
  "threshold": "Less than 50% of average weekly wages over the previous 8 weeks",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": "a week in which an employee earns less than 50% of the employee's weekly wages, at the regular wage, averaged over the previous 8 weeks"
}
```
- **Reviewed:** yes

## T078
- **Split:** train
- **Type:** eligibility
- **Jurisdiction:** British Columbia
- **Question:** I'm a reservist in BC and being deployed. Can I take leave from my job?
- **Excerpts:**
  - [BC s. 52.2(2)] (2) Subject to the regulations, an employee who is a reservist and who requests leave under this section is entitled to unpaid leave, for the period described in subsection (3), if / (a) the employee is deployed to a Canadian Forces operation outside Canada or is engaged, either inside or outside Canada, in a pre-deployment or post-deployment activity required by the Canadian Forces in connection with such an operation, / (b) the employee is deployed to a Canadian Forces operation inside Canada that is or will be providing assistance in dealing with an emergency or with its aftermath, or / (c) the prescribed circumstances apply.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "52.2(2)",
  "eligibility": "Employee is a reservist who requests leave and is deployed to a Canadian Forces operation outside Canada (or a related pre- or post-deployment activity), deployed to an operation inside Canada assisting with an emergency, or in prescribed circumstances",
  "entitlement_or_requirement": "Unpaid leave for the period described in subsection (3)",
  "threshold": "Not specified in the excerpt (the leave period is in subsection (3), which is not included)",
  "exceptions": [
    "Subject to the regulations"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "an employee who is a reservist and who requests leave under this section is entitled to unpaid leave"
}
```
- **Reviewed:** yes

## T079
- **Split:** train
- **Type:** missing, distractor
- **Jurisdiction:** British Columbia
- **Question:** Does a BC employer have to give a reference letter when someone leaves?
- **Excerpts:**
  - [BC s. 63(1)] (1) After 3 consecutive months of employment, the employer becomes liable to pay an employee an amount equal to one week's wages as compensation for length of service.
  - [BC s. 28(2)] (2) Payroll records must / (a) be in English, / (b) be kept at the employer's principal place of business in British Columbia, and / (c) be retained by the employer for 4 years after the date on which the payroll records were created.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "termination",
  "section": "Not specified in the excerpt",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Not specified in the excerpt",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": ""
}
```
- **Reviewed:** yes

## T080
- **Split:** train
- **Type:** missing, distractor
- **Jurisdiction:** British Columbia
- **Question:** If I'm given termination notice in BC, can my employer lower my wage during the notice period?
- **Excerpts:**
  - [BC s. 17(1)] (1) At least semimonthly and within 8 days after the end of the pay period, an employer must pay to an employee all wages earned by the employee in a pay period.
  - [BC s. 19(3)] (3) The director's receipt for wages is proof that the employer's liability for payment of the wages is discharged to the extent of the amount stated in the receipt.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "termination",
  "section": "Not specified in the excerpt",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Not specified in the excerpt",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": ""
}
```
- **Reviewed:** yes

## V001
- **Split:** val
- **Type:** requirement
- **Jurisdiction:** Ontario
- **Question:** Does an Ontario job posting have to say whether the job actually exists?
- **Excerpts:**
  - [ON s. 8.5(1)] (1) Every employer who advertises a publicly advertised job posting shall include in the posting, / (a) a statement disclosing whether the posting is for an existing vacancy or not; and / (b) such other information as may be prescribed.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "job_postings",
  "section": "8.5(1)",
  "eligibility": "Employer advertises a publicly advertised job posting",
  "entitlement_or_requirement": "The posting must include a statement disclosing whether it is for an existing vacancy, and any other prescribed information",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "a statement disclosing whether the posting is for an existing vacancy or not"
}
```
- **Reviewed:** yes

## V002
- **Split:** val
- **Type:** rule
- **Jurisdiction:** Ontario
- **Question:** I was laid off and then let go in Ontario. Does the lay-off time count toward my period of employment?
- **Excerpts:**
  - [ON s. 59(2)] (2) Despite subsection (1), if an employee’s employment was terminated as a result of a lay-off, no part of the lay-off period after the deemed termination date shall be included in determining his or her period of employment.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "59(2)",
  "eligibility": "Employment was terminated as a result of a lay-off",
  "entitlement_or_requirement": "No part of the lay-off period after the deemed termination date is included in determining the period of employment",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "no part of the lay-off period after the deemed termination date shall be included in determining his or her period of employment"
}
```
- **Reviewed:** yes

## V003
- **Split:** val
- **Type:** threshold, eligibility
- **Jurisdiction:** Ontario
- **Question:** How much leave can I take in Ontario if my child goes missing because of a crime?
- **Excerpts:**
  - [ON s. 49.6(2)] (2) An employee who has been employed by an employer for at least six consecutive months is entitled to a leave of absence without pay of up to 104 weeks if a child of the employee disappears and it is probable, considering the circumstances, that the child disappeared as a result of a crime.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "49.6(2)",
  "eligibility": "Employee employed for at least six consecutive months; a child of the employee disappears and it is probable the disappearance resulted from a crime",
  "entitlement_or_requirement": "Leave of absence without pay",
  "threshold": "Up to 104 weeks; at least six consecutive months of employment",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "is entitled to a leave of absence without pay of up to 104 weeks if a child of the employee disappears"
}
```
- **Reviewed:** yes

## V004
- **Split:** val
- **Type:** threshold, eligibility
- **Jurisdiction:** Ontario
- **Question:** When does pregnancy leave end in Ontario if I'm also taking parental leave?
- **Excerpts:**
  - [ON s. 47(1)] (1) An employee’s pregnancy leave ends, / (a) if she is entitled to parental leave, 17 weeks after the pregnancy leave began; / (b) if she is not entitled to parental leave, on the day that is the later of, / (i) 17 weeks after the pregnancy leave began, and / (ii) 12 weeks after the birth, still-birth or miscarriage.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "47(1)",
  "eligibility": "Employee is entitled to parental leave",
  "entitlement_or_requirement": "Pregnancy leave ends 17 weeks after it began",
  "threshold": "17 weeks after the pregnancy leave began",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "if she is entitled to parental leave, 17 weeks after the pregnancy leave began"
}
```
- **Reviewed:** yes

## V005
- **Split:** val
- **Type:** exception
- **Jurisdiction:** Ontario
- **Question:** Does time on leave in Ontario count toward my seniority and probation?
- **Excerpts:**
  - [ON s. 52(1)] (1) The period of an employee’s leave under this Part shall be included in calculating any of the following for the purpose of determining his or her rights under an employment contract: / 1. The length of his or her employment, whether or not it is active employment. / 2. The length of the employee’s service whether or not that service is active. / 3. The employee’s seniority.
  - [ON s. 52(2)] (2) The period of an employee’s leave shall not be included in determining whether he or she has completed a probationary period under an employment contract.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "52(1), 52(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "The leave period counts toward length of employment, length of service and seniority under the employment contract",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "The leave period does not count toward completing a probationary period (s. 52(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "The period of an employee’s leave shall not be included in determining whether he or she has completed a probationary period under an employment contract."
}
```
- **Reviewed:** yes

## V006
- **Split:** val
- **Type:** threshold
- **Jurisdiction:** Ontario
- **Question:** How long can an agreed layoff last in Ontario?
- **Excerpts:**
  - [ON s. 66.1(1)] (1) An employer and an employee may agree to a lay-off that is 35 or more weeks in any period of 52 consecutive weeks, but may not agree to a lay-off of 52 or more weeks in any period of 78 consecutive weeks.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "66.1(1)",
  "eligibility": "Employer and employee agree to the lay-off",
  "entitlement_or_requirement": "May agree to a lay-off of 35 or more weeks in any 52 consecutive weeks, but not 52 or more weeks in any 78 consecutive weeks",
  "threshold": "35 or more weeks in 52 is allowed by agreement; 52 or more weeks in 78 is not",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "may not agree to a lay-off of 52 or more weeks in any period of 78 consecutive weeks"
}
```
- **Reviewed:** yes

## V007
- **Split:** val
- **Type:** list, exception
- **Jurisdiction:** Ontario
- **Question:** Does the right to refuse work on public holidays in retail apply to restaurants in Ontario?
- **Excerpts:**
  - [ON s. 72(2)] (2) This Part does not apply with respect to retail business establishments in which the primary retail business is one that, / (a) sells prepared meals; / (b) rents living accommodations; / (c) is open to the public for educational, recreational or amusement purposes; or / (d) sells goods or services incidental to a business described in clause (a), (b) or (c) and is located in the same premises as that business.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "retail_business_establishments",
  "section": "72(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "The retail Part does not apply to establishments whose primary retail business sells prepared meals, rents living accommodations, is open for educational, recreational or amusement purposes, or sells incidental goods or services in the same premises",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": "This Part does not apply with respect to retail business establishments in which the primary retail business is one that,"
}
```
- **Reviewed:** yes

## V008
- **Split:** val
- **Type:** exception
- **Jurisdiction:** Ontario
- **Question:** Can my Ontario employer deduct money from my tips if a court orders it?
- **Excerpts:**
  - [ON s. 14.3(1)] (1) An employer may withhold or make a deduction from an employee’s tips or other gratuities or cause the employee to return or give them to the employer if a statute of Ontario or Canada or a court order authorizes it.
  - [ON s. 14.3(2)] (2) Subsection (1) does not apply if the statute or order requires the employer to remit the withheld, deducted, returned or given tips or other gratuities to a third person and the employer fails to do so.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "tips_and_gratuities",
  "section": "14.3(1), 14.3(2)",
  "eligibility": "A statute of Ontario or Canada or a court order authorizes it",
  "entitlement_or_requirement": "Employer may withhold or deduct from tips or other gratuities",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Does not apply if the statute or order requires remitting the amount to a third person and the employer fails to do so (s. 14.3(2))"
  ],
  "mandatory": "optional",
  "supporting_quote": "if a statute of Ontario or Canada or a court order authorizes it"
}
```
- **Reviewed:** yes

## V009
- **Split:** val
- **Type:** missing
- **Jurisdiction:** Ontario
- **Question:** How many weeks of family caregiver leave can I take in Ontario?
- **Excerpts:**
  - [ON s. 49.3(2)] (2) An employee is entitled to a leave of absence without pay to provide care or support to an individual described in subsection (5) if a qualified health practitioner issues a certificate stating that the individual has a serious medical condition.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "leaves_of_absence",
  "section": "49.3(2)",
  "eligibility": "A qualified health practitioner issues a certificate stating that the individual has a serious medical condition",
  "entitlement_or_requirement": "Leave of absence without pay to provide care or support to an individual described in subsection (5)",
  "threshold": "Not specified in the excerpt (the number of weeks is not stated)",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employee is entitled to a leave of absence without pay to provide care or support to an individual described in subsection (5)"
}
```
- **Reviewed:** yes

## V010
- **Split:** val
- **Type:** missing
- **Jurisdiction:** Ontario
- **Question:** Can my employer in Ontario make me sign a non-compete agreement?
- **Excerpts:**
  - [ON s. 67.2(5)] (5) In this section, / “executive” means any person who holds the office of chief executive officer, president, chief administrative officer, chief operating officer, chief financial officer, chief information officer, chief legal officer, chief human resources officer or chief corporate development officer, or holds any other chief executive position; (“cadre supérieur”) / “sale” includes a lease. (“vente”)
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "non_compete_agreements",
  "section": "Not specified in the excerpt",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Not specified in the excerpt",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": ""
}
```
- **Reviewed:** yes

## V011
- **Split:** val
- **Type:** threshold, eligibility
- **Jurisdiction:** Ontario
- **Question:** In Ontario, when is someone with a regular work week considered laid off for a week?
- **Excerpts:**
  - [ON s. 63(2.1)] (2.1) For the purpose of clause (1) (c), an employee who has a regular work week is laid off for a week if, / (a) in that week, the employee earns less than one-quarter the amount he or she would earn at his or her regular rate in a regular work week; and / (b) the week is not an excluded week.
- **Expected JSON:**
```json
{
  "jurisdiction": "Ontario",
  "topic": "termination_and_severance",
  "section": "63(2.1)",
  "eligibility": "Employee has a regular work week, and the week is not an excluded week",
  "entitlement_or_requirement": "Laid off for a week if the employee earns less than one-quarter of what they would earn at their regular rate in a regular work week",
  "threshold": "Less than one-quarter of regular weekly earnings",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": "the employee earns less than one-quarter the amount he or she would earn at his or her regular rate in a regular work week"
}
```
- **Reviewed:** yes

## V012
- **Split:** val
- **Type:** list
- **Jurisdiction:** British Columbia
- **Question:** Which wage assignments does a BC employer have to honour?
- **Excerpts:**
  - [BC s. 22(1)] (1) An employer must honour an employee's written assignment of wages / (a) to a trade union in accordance with the Labour Relations Code, / (b) to a charitable or other organization, or a pension or superannuation or other plan, if the amounts assigned are deductible for income tax purposes under the Income Tax Act (Canada), / (c) to a person to whom the employee is required under a maintenance order, as defined in the Family Maintenance Enforcement Act, to pay maintenance, and / (d) to an insurance company for insurance or medical or dental coverage. / (e) [Repealed 2003-65-5.]
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "22(1)",
  "eligibility": "The employee makes a written assignment of wages",
  "entitlement_or_requirement": "Employer must honour written assignments to a trade union, to tax-deductible charitable organizations or pension plans, to a person under a maintenance order, and to an insurer for insurance or medical or dental coverage",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "An employer must honour an employee's written assignment of wages"
}
```
- **Reviewed:** yes

## V013
- **Split:** val
- **Type:** exception
- **Jurisdiction:** British Columbia
- **Question:** If a farm labour contractor in BC doesn't pay workers, is the farm responsible?
- **Excerpts:**
  - [BC s. 30(1)] (1) A producer and a farm labour contractor are jointly and separately liable for wages earned by an employee of the farm labour contractor for work done on behalf of the producer.
  - [BC s. 30(2)] (2) Subsection (1) does not apply in respect of a producer if / (a) the farm labour contractor is licensed under this Act at the time the producer engages the services of the farm labour contractor, and / (b) the producer satisfies the director that the producer paid the farm labour contractor for wages earned by each employee of the farm labour contractor for work done on behalf of the producer.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "30(1), 30(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "The producer and the farm labour contractor are jointly and separately liable for wages earned by the contractor's employee for work done for the producer",
  "threshold": "Not specified in the excerpt",
  "exceptions": [
    "Not the producer, if the contractor was licensed when engaged and the producer shows it paid the contractor for the employees' wages (s. 30(2))"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "A producer and a farm labour contractor are jointly and separately liable for wages"
}
```
- **Reviewed:** yes

## V014
- **Split:** val
- **Type:** rule
- **Jurisdiction:** British Columbia
- **Question:** I've been called for jury duty in BC. Is my job protected?
- **Excerpts:**
  - [BC s. 55] If an employee is required to attend court as a juror, the employer has the same duties under section 54 (2) to (4) in relation to the employee as if that employee were on leave under this Part.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "55",
  "eligibility": "Employee is required to attend court as a juror",
  "entitlement_or_requirement": "The employer has the same duties under section 54 (2) to (4) as if the employee were on leave",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employer has the same duties under section 54 (2) to (4) in relation to the employee as if that employee were on leave under this Part"
}
```
- **Reviewed:** yes

## V015
- **Split:** val
- **Type:** eligibility
- **Jurisdiction:** British Columbia
- **Question:** Does my BC employer keep paying into my pension plan while I'm on leave?
- **Excerpts:**
  - [BC s. 56(2)] (2) In the following circumstances, the employer must continue to make payments to a pension, medical or other plan beneficial to an employee as though the employee were not on leave or attending court as a juror: / (a) if the employer pays the total cost of the plan; / (b) if both the employer and the employee pay the cost of the plan and the employee chooses to continue to pay the employee's share of the cost.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "56(2)",
  "eligibility": "The employer pays the total cost of the plan, or the employer and employee share the cost and the employee chooses to keep paying their share",
  "entitlement_or_requirement": "Employer must continue payments to a pension, medical or other plan as though the employee were not on leave",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employer must continue to make payments to a pension, medical or other plan beneficial to an employee as though the employee were not on leave"
}
```
- **Reviewed:** yes

## V016
- **Split:** val
- **Type:** requirement
- **Jurisdiction:** British Columbia
- **Question:** My BC employer agreed to pay into my RRSP. Do they have to?
- **Excerpts:**
  - [BC s. 26] An employer who agrees under an employment contract to pay an amount on behalf of an employee to a fund, insurer or other person must pay the amount in accordance with the contract.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "26",
  "eligibility": "Employer agrees under an employment contract to pay an amount on the employee's behalf to a fund, insurer or other person",
  "entitlement_or_requirement": "The employer must pay the amount in accordance with the contract",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "must pay the amount in accordance with the contract"
}
```
- **Reviewed:** yes

## V017
- **Split:** val
- **Type:** rule
- **Jurisdiction:** British Columbia
- **Question:** If I find a new job during my notice period in BC, do I still get termination pay?
- **Excerpts:**
  - [BC s. 68(2)] (2) The termination pay requirements of section 64 apply whether or not the employee has obtained other employment or has in any other way realized or recovered any money for the notice period.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "termination",
  "section": "68(2)",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "The termination pay requirements of section 64 apply whether or not the employee has found other employment or recovered money for the notice period",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "apply whether or not the employee has obtained other employment"
}
```
- **Reviewed:** yes

## V018
- **Split:** val
- **Type:** threshold, eligibility
- **Jurisdiction:** British Columbia
- **Question:** How much leave can I take in BC if my child disappears?
- **Excerpts:**
  - [BC s. 52.3(2)] (2) If a child of an employee disappears and it is probable, in the circumstances, that the child's disappearance is a result of a crime, and the employee requests leave under this section, the employee is entitled to unpaid leave for a period of up to 52 weeks.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "leaves",
  "section": "52.3(2)",
  "eligibility": "A child of the employee disappears, it is probable the disappearance is the result of a crime, and the employee requests leave",
  "entitlement_or_requirement": "Unpaid leave",
  "threshold": "Up to 52 weeks",
  "exceptions": [],
  "mandatory": "mandatory",
  "supporting_quote": "the employee is entitled to unpaid leave for a period of up to 52 weeks"
}
```
- **Reviewed:** yes

## V019
- **Split:** val
- **Type:** missing
- **Jurisdiction:** British Columbia
- **Question:** How much notice must a BC employee give before quitting?
- **Excerpts:**
  - [BC s. 67(2)] (2) Once notice is given to an employee under this Part, the employee's wage rate, or any other condition of employment, must not be altered without the written consent of / (a) the employee, or / (b) a trade union representing the employee.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "termination",
  "section": "Not specified in the excerpt",
  "eligibility": "Not specified in the excerpt",
  "entitlement_or_requirement": "Not specified in the excerpt",
  "threshold": "Not specified in the excerpt",
  "exceptions": [],
  "mandatory": "Not specified in the excerpt",
  "supporting_quote": ""
}
```
- **Reviewed:** yes

## V020
- **Split:** val
- **Type:** missing
- **Jurisdiction:** British Columbia
- **Question:** What is the minimum wage for liquor servers in BC?
- **Excerpts:**
  - [BC s. 16.1(2)] (2) Subject to section 16.2, the minimum wage for a prescribed class of employees is the amount specified in, or calculated in accordance with, the regulations.
- **Expected JSON:**
```json
{
  "jurisdiction": "British Columbia",
  "topic": "wages",
  "section": "16.1(2)",
  "eligibility": "Employee belongs to a prescribed class of employees",
  "entitlement_or_requirement": "The minimum wage for the class is the amount specified in, or calculated under, the regulations",
  "threshold": "Not specified in the excerpt (the amount is set by regulation)",
  "exceptions": [
    "Subject to section 16.2, which is not included in the excerpt"
  ],
  "mandatory": "mandatory",
  "supporting_quote": "the minimum wage for a prescribed class of employees is the amount specified in, or calculated in accordance with, the regulations"
}
```
- **Reviewed:** yes
