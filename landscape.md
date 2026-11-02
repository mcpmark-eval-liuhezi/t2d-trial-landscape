# Type 2 Diabetes (T2DM) Trial Landscape Brief

**Prepared for:** Quarterly portfolio review — type 2 diabetes mellitus (T2DM) competitive landscape
**Source:** ClinicalTrials.gov, queried live via the registry API on 2026-11-02
**Total registered T2D trials (condition "type 2 diabetes"):** 12,033

---

## 1. Aggregate statistics — type 2 diabetes mellitus

### 1.1 By trial phase (countByPhase)

| Phase | Studies |
|---|---|
| N/A (no phase assigned; predominantly observational) | 4,510 |
| Phase 4 | 1,410 |
| Phase 3 | 1,647 |
| Phase 2 | 1,319 |
| Phase 1 | 87 |
| Early Phase 1 | 87 |

Phase buckets report counts per phase value as returned by the registry; studies with multiple phase values count in each bucket.

### 1.2 By overall recruitment status (countByStatus)

| Overall status | Studies |
|---|---|
| Completed | 7,899 |
| Unknown | 1,540 |
| Terminated | 579 |
| Recruiting | 873 |
| Active, not recruiting | 341 |
| Withdrawn | 242 |
| Not yet recruiting | 431 |
| Enrolling by invitation | 92 |
| Suspended | 33 |

Sum of the nine reported buckets is 12,030 of 12,033 total records; the remaining 3 carry no overall-status value in the default enum.

### 1.3 By sponsor class (countBySponsorType)

| Lead-sponsor class | Studies |
|---|---|
| Industry | 4,366 |
| Other (non-industry: academic, hospital, medical, government, NIH, federal, network, individual) | 7,667 |

Industry 4,366 + non-industry 7,667 = 12,033 total.

---

## 2. Three largest currently recruiting, industry-sponsored T2D trials by enrollment

Selection criteria: overall status = RECRUITING, lead-sponsor class = INDUSTRY, sorted by enrollment count descending.

### Trial 1 — NCT06278207 (FINEROD)
- **NCT ID:** NCT06278207
- **Official title:** Finerenone Research of Outcomes and Drug Utilization
- **Sponsor:** Bayer (Industry)
- **Enrollment:** 50,000 (estimated)
- **Status:** Recruiting (status verified 2026-06; start 2024-05-15; estimated primary completion 2026-09-30)
- **Brief:** Observational cohort of patients with chronic kidney disease and type 2 diabetes initiating finerenone, from US and Asia electronic health records and claims data.

### Trial 2 — NCT03549754 (iCaReMe)
- **NCT ID:** NCT03549754
- **Official title:** Real-world Multinational Registry to Determine Management and Quality of Care of Patients With Type 2 Diabetes, Hypertension, Heart Failure and/or Chronic Kidney Diseases
- **Sponsor:** AstraZeneca (Industry)
- **Enrollment:** 35,000 (estimated)
- **Status:** Recruiting (status verified 2026-08; start 2018-02-17; estimated completion 2030-12-31)
- **Brief:** Multinational observational registry (T2D, hypertension, HF, and/or CKD cohorts) using a cloud-based eCRF for prospective and retrospective data collection.

### Trial 3 — NCT05663515 (EXCEED)
- **NCT ID:** NCT05663515
- **Official title:** EXCEED - A Pan-European Post-Authorisation Safety Study: Risk of Pancreatic Cancer Among Type 2 Diabetes Patients Who Initiated Exenatide as Compared With Those Who Initiated Other Non-Glucagon-Like Peptide 1 Receptor Agonists Based Glucose Lowering Drugs
- **Sponsor:** AstraZenena (Industry) -- AstraZeneca (Industry)
- **Enrollment:** 24,000 (estimated)
- **Status:** Recruiting (status verified 2026-09; start 2024-09-30; estimated primary completion 2026-10-01)
- **Brief:** Non-interventional post-authorisation safety study assessing pancreatic cancer risk in T2DM patients who initiated exenatide vs. other non-GLP-1 RA based glucose-lowering drugs, across 7 European countries.

---

## 3. SUNSHINE citation check — NCT01608724 (saxagliptin)

- **NCT ID:** NCT01608724
- **Acronym:** SUNSHINE
- **Official title:** A Multicenter, Single Arm, Cohort Study to Evaluate the Efficacy and Safety of Saxagliptin 5mg, Once Daily for 24 Weeks, in Patients With Type 2 Diabetes Mellitus
- **Sponsor:** AstraZeneca (class: INDUSTRY; responsible party: sponsor)
- **Enrollment:** 2,165 (actual)
- **Current overall status:** COMPLETED (status verified 2015-12; start 2012-11; actual primary completion and completion 2014-05; results first posted 2016-02-02)
- **Phase:** Phase 4; interventional, single group, treatment purpose, non-randomized, open label
- **Conditions:** Diabetes Mellitus, Non-Insulin-Dependent (Type 2 DM)
- **Intervention:** Saxagliptin 5 mg oral once daily (other name: Onglyza)

**Citation verdict:** Sponsor (AstraZeneca, industry) and enrollment (2,165 actual) are confirmed consistent with the registry record — no correction needed for those fields. If the draft describes the trial as ongoing, it should instead be described as **completed**.

---

## 4. Notes

- The registry aggregate-analysis tool caps at 5,000 studies per analysis; the 12,033-record set exceeds this, so counts were obtained via filtered countTotal queries against condition "type 2 diabetes" and reported exactly as returned.
- Enrollment figures for the three profiled trials are estimated (observational registry-type designs); the SUNSHINE trial enrollment is actual.
- Data retrieved from ClinicalTrials.gov API on 2026-11-02.
