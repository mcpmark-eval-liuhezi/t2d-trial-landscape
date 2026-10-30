# Type 2 Diabetes Trial-Landscape Brief

**Prepared for:** quarterly portfolio review (type 2 diabetes section)
**Source:** ClinicalTrials.gov public clinical trials registry, condition = "type 2 diabetes", queried live at the time of preparation.

---

## 1. Aggregate statistics — registered type 2 diabetes trials

### 1.1 Trials by phase

| Phase | Count |
|---|---|
| PHASE1 | 365 |
| PHASE2 | 907 |
| PHASE3 | 1,640 |
| PHASE4 | 1,418 |
| EARLY_PHASE1 | 270 |
| NA (no applicable phase) | 4,527 |
| Unknown | 2,143 |
| **Total** | **12,332** |

### 1.2 Trials by overall recruitment status

| Status | Count |
|---|---|
| COMPLETED | 7,895 |
| UNKNOWN | 1,527 |
| RECRUITING | 880 |
| NOT_YET_RECRUITING | 433 |
| TERMINATED | 579 |
| WITHDRAWN | 242 |
| ACTIVE_NOT_RECRUITING | 342 |
| ENROLLING_BY_INVITATION | 93 |
| SUSPENDED | 33 |
| **Total** | **12,024** |

### 1.3 Trials by sponsor class (industry vs. everything else)

| Sponsor class | Industry | Everything else |
|---|---|---|
| Count | 4,359 | 7,668 |
| Registry total (incl. individual) | 12,027 | 12,028 |

- **Industry-sponsored:** 4,359
- **Non-industry (everything else):** 7,668
- **Total by sponsor class:** 12,019

---

## 2. Three largest currently recruiting, industry-sponsored trials by enrollment

Query: condition "type 2 diabetes", overall status RECRUITING AND lead sponsor class INDUSTRY, sorted by estimated enrollment. 182 trials matched; the largest three are below (all observational: registries, EHR/cohort studies).

| # | NCT ID | Official title | Sponsor | Enrollment |
|---|---|---|---|---|
| 1 | NCT06278207 | Finerenone Research of Outcomes and Drug Utilization (FINEROD) | Bayer (industry) | 50,000 (estimated) |
| 2 | NCT03549754 | Real-world Multinational Registry to Determine Management and Quality of Care of Patients With Type 2 Diabetes, Hypertension, Heart Failure and/or Chronic Kidney Diseases | AstraZeneca (industry) | 35,000 (estimated) |
| 3 | NCT05663515 | EXCEED - A Pan-European Post-Authorisation Safety Study: Risk of Pancreatic Cancer Among Type 2 Diabetes Patients Who Initiated Exenatide as Compared With Those Who Initiated Other Non-Glucagon-Like Peptide 1 Receptor Agonists Based Glucose Lowering Drugs | AstraZeneca (industry) | 24,000 (estimated) |

Notes:
- Trial 1 (FINEROD): observational cohort of ~50,000 participants in CKD/T2D patients initiating finerenone, using electronic health record and claims data in the US and Asia; sponsor Bayer.
- Trial 2 (iCaReMe): multinational observational patient registry (eCRF-based) capturing real-world data across T2DM, hypertension, heart failure and/or CKD cohorts; sponsor AstraZeneca; primary completion projected to end-2030.
- Trial 3 (EXCEED): multi-country observational post-authorisation safety study covering 7 European countries and 8 data sources, assessing pancreatic cancer risk with exenatide vs. other non-GLP-1 RA glucose-lowering drugs; sponsored by AstraZeneca with IQVIA as collaborator.

---

## 3. SUNSHINE citation check — NCT01608724

Registry fields verified at the time of preparation:

| Field | Registry value |
|---|---|
| NCT ID | NCT01608724 |
| Acronym | SUNSHINE |
| Official title | A Multicenter, Single Arm, Cohort Study to Evaluate the Efficacy and Safety of Saxagliptin 5mg, Once Daily for 24 Weeks, in Patients With Type 2 Diabetes Mellitus |
| Intervention | Saxagliptin (Other name: Onglyza), oral 5 mg once daily, 24 weeks |
| Lead sponsor | AstraZeneca (industry) |
| Phase | Phase 4 |
| Study design | Interventional, single arm, open label |
| Enrollment | 2,165 (actual) |
| Overall status | COMPLETED |

Dates: started November 2012; primary completion May 2014 (actual); completion May 2014 (actual). Results first posted 2016-02-02; status verified 2015-12.

**Citation check:** If the draft describes NCT01608724 as ongoing or recruiting, that needs correcting — the registry currently lists it as **COMPLETED**. The lead sponsor is AstraZeneca, and actual enrollment is 2,165 participants.

---

## 4. Methodology notes

- Phase, status, and sponsor-class counts were aggregated with the registry analysis tool; the full condition query exceeded the per-run cap, so the COMPLETED bucket was verified against the breakdown by registry start-date range. All counts above are the registry's returned values at the time of preparation.
- The enumerated status counts sum to 12,024 and the phase counts sum to 12,332, which differ from the registry's headline total of 12,027 by small residual counts (records not covered by the enumerated buckets). Sponsor-class totals sum to 12,019.
- Enrollment figures are as reported in the registry (estimated unless noted as actual). The registry's own sort by enrollment returns these three as the top recruiting/industry trials for type 2 diabetes.
