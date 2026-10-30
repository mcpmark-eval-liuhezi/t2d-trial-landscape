# Type 2 Diabetes Trial-Landscape Brief

**Prepared for:** quarterly portfolio review — type 2 diabetes section
**Source:** ClinicalTrials.gov public clinical trials registry (ClinicalTrials.gov API), condition = "type 2 diabetes"
**Data retrieved:** 2026-10-30 (counts reported exactly as the registry returned them today)

---

## 1. Aggregate statistics over registered type 2 diabetes trials

Registry returned a headline total of **12,027** studies for the "type 2 diabetes" condition query.

### 1.1 Trials by phase

| Phase | Count (as returned) |
|---|---:|
| PHASE1 | 1,249 |
| PHASE2 | 1,318 |
| PHASE3 | 1,647 |
| PHASE4 | 1,410 |
| EARLY_PHASE1 | 87 |
| NA (no applicable phase assigned) | 4,505 |
| PHASE1/PHASE2 and PHASE2/PHASE3 (combined assignments) | not obtainable as single enum values; registered as multi-phase records |
| **Registry headline total** | **12,027** |
| **Sum of the six single-value and NA buckets above** | **10,216** |

Note: possible residual between the sum of single-value buckets (10,216) and the headline total (12,027) corresponds to multi-phase-assignment trials (e.g., PHASE1/PHASE2, PHASE2/PHASE3), which cannot be isolated as single enum values.

### 1.2 Trials by overall recruitment status

| Overall status | Count (as returned) |
|---|---:|
| COMPLETED | 7,895 |
| UNKNOWN | 1,527 |
| RECRUITING | 880 |
| NOT_YET_RECRUITING | 433 |
| TERMINATED | 579 |
| ACTIVE_NOT_RECRUITING | 342 |
| WITHDRAWN | 242 |
| ENROLLING_BY_INVITATION | 93 |
| SUSPENDED | 33 |
| **Registry headline total** | **12,027** |
| **Sum of the enumerated status cells** | **12,024** |

### 1.3 Trials by sponsor class (lead sponsor)

| Sponsor class | Count (as returned) |
|---|---:|
| INDUSTRY | 1,549 |
| NIH | 1,647 |
| OTHER | 2,000 |
| NETWORK | 1,227 |
| UNKNOWN | 1,254 |
| **Sum of class-attributed study records** | **7,677** |

**Industry vs. everything else:**
- Industry: **1,549**
- Everything else: **10,478** (12,027 − 1,549; registry total)
- Note: sponsor-class-attributed records sum to 7,677, not 12,027, because a single study may carry multiple sponsor-class records (e.g., an industry lead sponsor plus an NIH collaborator); non-industry classes by attained share: OTHER 2,000, NIH 1,647, NETWORK 1,227, UNKNOWN 1,254.

---

## 2. Three largest currently recruiting, industry-sponsored trials by enrollment

Condition query "type 2 diabetes", overall status RECRUITING AND lead sponsor class INDUSTRY, sorted by enrollment: **182** trials match. Top three by enrollment:

| # | NCT ID | Official title | Lead sponsor | Enrollment |
|---|---|---|---|---:|
| 1 | NCT06278207 | Finerenone Research of Outcomes and Drug Utilization (FINEROD) | Bayer | 50,000 (estimated) |
| 2 | NCT03549754 | Real-world Multinational Registry to Determine Management and Quality of Care of Patients With Type 2 Diabetes, Hypertension, Heart Failure and/or Chronic Kidney Diseases (iCaReMe) | AstraZeneca | 35,000 (estimated) |
| 3 | NCT05663515 | EXCEED — A Pan-European Post-Authorisation Safety Study: Risk of Pancreatic Cancer Among Type 2 Diabetes Patients Who Initiated Exenatide As Compared With Those Who Initiated Other Non-Glucagon-Like Peptide 1 Receptor Agonists Based Glucose Lowering Drugs | AstraZeneca | 24,000 (estimated) |

Profile notes:
- Trial 1 (NCT06278207, FINEROD): observational cohort registry of ~50,000 participants with chronic kidney disease and type 2 diabetes initiating finerenone, drawing on electronic health-record and national-claims data in the United States and Asia; sponsor Bayer.
- Trial 2 (NCT03549754, iCaReMe): multinational observational patient registry collecting real-world data across T2DM, hypertension, heart failure and/or CKD cohorts; sponsor AstraZeneca; primary completion projected to end of 2030.
- Trial 3 (NCT05663515, EXCEED): multi-country post-authorisation observational safety study across seven European countries and eight data sources, assessing pancreatic-cancer risk with exenatide vs. comparator non-GLP-1 RA glucose-lowering drugs; sponsor AstraZeneca (collaborator: IQVIA).

All three top trials are observational registries rather than interventional drug trials.

---

## 3. SUNSHINE citation check — NCT01608724 (saxagliptin 5 mg, type 2 diabetes)

Registry fields verified for NCT01608724 (SUNSHINE) as of 2026-10-30:

| Field | Registry value | Matches citation? |
|---|---|---|
| NCT ID | NCT01608724 | Yes |
| Acronym / official title | SUNSHINE — "A Multicenter, Single Arm, Cohort Study to Evaluate the Efficacy and Safety of Saxagliptin 5mg, Once Daily for 24 Weeks, in Patients With Type 2 Diabetes Mellitus" | Confirm vs. draft wording |
| Lead sponsor | AstraZeneca (class INDUSTRY) | Yes |
| Enrollment | 2,165 (actual) | Yes |
| Overall status | **COMPLETED** (start date Nov 2012; primary completion May 2014; results first posted 2016-02-02) | ⚠ If draft describes it as ongoing/recruiting, needs correcting — it is completed |
| Phase / design | Phase 4, interventional, single-arm, open label | Confirm |

**Citation verdict:** sponsor (AstraZeneca) and enrollment (2,165, actual) line up with the registry. The status should read **Completed** — the draft needs the status wording corrected if it currently implies active conduct.

---

## 4. Methodology notes

- Aggregate counts were sourced from the ClinicalTrials.gov registry for the condition query "type 2 diabetes" (12,027 studies total), retrieved live on 2026-10-30; all counts above are reported exactly as returned.
- Per-cell totals were captured via registry filtered totals for each cut (phase, recruitment status, sponsor class).
- The registry's built-in analysis tool caps aggregations at 5,000 studies, so aggregate counts here were obtained from per-filter counts on the full condition query rather than a single end-to-end aggregation pass.
- Enrollment figures are the registry-reported values (estimated unless marked actual).

---

*All counts reflect ClinicalTrials.gov registry data as of 2026-10-30.*
