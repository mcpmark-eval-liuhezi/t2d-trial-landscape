# Type 2 Diabetes Clinical Trial Landscape Brief

**Prepared for:** Quarterly portfolio review — Type 2 diabetes section
**Registry source:** ClinicalTrials.gov (public registry), data retrieved 2026-10-21
**Scope:** All studies returned by the registry's condition query for "Type 2 Diabetes" — **12,002 studies** total.

---

## Methodology note (aggregate statistics)

The registry's analysis tool caps a single analysis at 5,000 studies, and the full T2D set (12,002) exceeds that cap. To cover the complete set, the population was partitioned into five disjoint, exhaustive slices by study start date, each analyzed separately, with the returned counts summed:

| Slice | Start date range | Studies |
|---|---|---|
| 1 | ≤ 2012-12-31 | 4,162 |
| 2 | 2013-01-01 – 2017-12-31 | 2,553 |
| 3 | 2018-01-01 – 2022-12-31 | 2,714 |
| 4 | 2023-01-01 or later | 2,521 |
| 5 | No start date recorded | 52 |
| **Total** | | **12,002** |

The slice sizes sum exactly to the unscoped condition-query total (12,002), confirming complete coverage with no overlap or omission. All counts below are reported exactly as the registry returned them, summed across the five slices.

---

## 1. Trials by phase

| Phase | Count |
|---|---|
| Phase 3 | 1,645 |
| Phase 4 | 1,408 |
| Phase 2 | 1,313 |
| Phase 1 | 1,247 |
| Early Phase 1 | 86 |
| N/A (no phase recorded) | 4,497 |
| Unknown | 2,116 |

> **Note:** phase bucket counts sum to 12,312, not 12,002 — trials registered with combined phases (e.g., Phase 1/2, Phase 2/3) are counted once in each phase the registry lists for them. The status and sponsor-class cuts below each sum exactly to 12,002.

## 2. Trials by overall recruitment status

| Overall status | Count |
|---|---|
| Completed | 7,885 |
| Unknown | 1,535 |
| Recruiting | 872 |
| Active, not recruiting | 339 |
| Not yet recruiting | 423 |
| Terminated | 578 |
| Withdrawn | 242 |
| Enrolling by invitation | 92 |
| Suspended | 33 |
| No longer available | 2 |
| Available | 1 |
| **Total** | **12,002** |

## 3. Trials by sponsor class

| Sponsor class | Count |
|---|---|
| Industry | 4,355 |
| Other (academic, hospitals, non-profit, etc.) | 7,189 |
| Other government | 244 |
| NIH | 108 |
| U.S. federal agency (FED) | 66 |
| Research network | 27 |
| Individual | 13 |
| **Total** | **12,002** |

Industry sponsors account for 4,355 of 12,002 studies (≈36.3%); the remaining 7,647 are non-industry.

---

## 4. Three largest recruiting, industry-sponsored T2D trials

There are 180 currently recruiting, industry-sponsored T2D trials in the registry. The three largest by enrollment:

### 1. NCT06278207 — FINEROD
- **Official title:** Finerenone Research of Outcomes and Drug Utilization
- **Sponsor:** Bayer (Industry)
- **Enrollment:** 50,000 (estimated)
- **Status:** Recruiting
- Observational cohort study of finerenone (Kerendia) use in chronic kidney disease with T2D under real-world conditions, using US and Asia EHR/claims data.

### 2. NCT03549754 — iCaReMe Global Registry
- **Official title:** Real-world Multinational Registry to Determine Management and Quality of Care of Patients With Type 2 Diabetes, Hypertension, Heart Failure and/or Chronic Kidney Diseases
- **Sponsor:** AstraZeneca (Industry)
- **Enrollment:** 35,000 (estimated)
- **Status:** Recruiting
- Multinational real-world evidence registry across T2D, hypertension, heart failure, and CKD cohorts.

### 3. NCT05663515 — EXCEED
- **Official title:** EXCEED - A Pan-European Post-Authorisation Safety Study: Risk of Pancreatic Cancer Among Type 2 Diabetes Patients Who Initiated Exenatide as Compared With Those Who Initiated Other Non-Glucagon-Like Peptide 1 Receptor Agonists Based Glucose Lowering Drugs
- **Sponsor:** AstraZeneca (Industry)
- **Enrollment:** 24,000 (estimated)
- **Status:** Recruiting
- Pan-European retrospective database study of pancreatic cancer risk with exenatide vs. non-GLP-1 RA glucose-lowering drugs, across 7 European countries.

---

## 5. Citation check: SUNSHINE saxagliptin trial

| Field | Registry value |
|---|---|
| NCT ID | NCT01608724 |
| Acronym | SUNSHINE |
| Official title | A Multicenter, Single Arm, Cohort Study to Evaluate the Efficacy and Safety of Saxagliptin 5mg, Once Daily for 24 Weeks, in Patients With Type 2 Diabetes Mellitus |
| Sponsor (lead) | AstraZeneca — Industry |
| Enrollment | 2,165 (actual) |
| Current status | **Completed** |
| Phase | Phase 4 (non-randomized, single-group, open label) |
| Conducted | China; started Nov 2012, completed May 2014; registry record last verified Dec 2015 |

**Citation guidance:** the registry confirms lead sponsor **AstraZeneca** (industry class), actual enrollment of **2,165** participants, and overall status **Completed**. If the draft cites the trial as ongoing/recruiting or lists a different enrollment figure, update it to these values.

---

*Generated from live ClinicalTrials.gov registry data on 2026-10-21 via the public registry API. Note: `report.md` in this repository is an earlier, date-scoped draft (start date ≥ 2021-01-01) with a smaller universe; the figures in this file supersede it and cover the full 12,002-study population.*
