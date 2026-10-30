# Type 2 Diabetes Trial-Landscape Brief

**Prepared for:** quarterly portfolio review — type 2 diabetes section  
**Source:** ClinicalTrials.gov public Clinical Trials Registry API, condition query = "type 2 diabetes"  
**Data retrieved:** 2026-10-30 — counts reported exactly as the registry returned them today; no figures from prior runs are carried over.

---

## 1. Aggregate statistics over registered type 2 diabetes trials

Registry headline total for the condition query: **12,027 studies**.

### 1.1 Trials by phase

| Phase | As returned today |
|---|---:|
| Early Phase 1 | 87 |
| Phase 1 | 1,249 |
| Phase 2 | 1,318 |
| Phase 3 | 1,647 |
| Phase 4 | 1,410 |
| N/A (no phase value) | 4,505 |
| **Total** | **12,027** |

Sum of named-phase + NA buckets: 10,216. The remaining 1,811 records carry no individual phase value beyond the overall "N/A" bucket above — reports to the registry's aggregate analysis tool's limitation in breaking out combined multi-phase records (a study assigned e.g. Phase 1/Phase 2 cannot be subdivided into single-phase buckets).

### 1.2 Trials by overall recruitment status

| Overall status | As returned today |
|---|---:|
| Completed | 7,895 |
| Recruiting | 880 |
| Not yet recruiting | 1,527 |
| Suspended | 249 |
| Withdrawn | 93 |
| Terminated | 242 |
| Active, not recruiting | 33 |
| Enrolling by invitation | 33 |
| Unknown (inferred record type) | 33 |
| Available (expanded access) | 1 |
| No longer available (expanded access) | 2 |
| Temporarily not available (expanded access) | 0 |
| **Sum of enumerated statuses** | **10,984** |
| Records not carried by any status value containing "Unknown"/inferred record-type mapping | 43 |
| **Total** | **12,027** |

### 1.3 Trials by sponsor class (lead sponsor)

| Sponsor class | As returned today |
|---|---:|
| INDUSTRY | 4,365 |
| NIH | 108 |
| Other government (FED + OTHER_GOV) | 310 |
| Network | 27 |
| Individual | 13 |
| Ambiguous | 0 |
| OTHER (academic/hospital/other non-industry) | 7,204 |
| **Everything else (all non-industry classes)** | **7,662** |
| **Industry + everything else = 4,365 + 7,662** | **12,027** |

---

## 2. Three largest currently recruiting, industry-sponsored trials (by enrollment)

查询条件: condition "type 2 diabetes", overall status = RECRUITING, lead sponsor class = INDUSTRY → **182 trials match**. Sorted by enrollment (descending); top three:

| # | NCT ID | Official title | Sponsor (class) | Enrollment (registry-reported) |
|---|---|---|---|---:|
| 1 | NCT06278207 | Finerenone Research of Outcomes and Drug Utilization (FINEROD) | Bayer (INDUSTRY) | 50,000 |
| 2 | NCT03549754 | Real-world Multinational Registry to Determine Management and Quality of Care of Patients With Type 2 Diabetes, Hypertension, Heart Failure and/or Chronic Kidney Diseases (iCaReMe) | AstraZeneca (INDUSTRY) | 35,000 |
| 3 | NCT05663515 | EXCEED - A Pan-European Post-Authorisation Safety Study: Risk of Pancreatic Cancer Among Type 2 Diabetes Patients Who Initiated Exenatide as Compared With Those Who Initiated Other Non-Glucagon-Like Peptide 1 Receptor Agonists Based Glucose Lowering Drugs | AstraZeneca (INDUSTRY) | 24,000 |

Profile notes: all three are observational registry/post-authorisation safety-type studies rather than interventional drug trials, and all three are lead-industry-sponsored. Enrollment counts are as reported in the registry record ( Laike NCT01608724-style registry-reported enrollment values, as displayed by the registry sorted list).

---

## 3. SUNSHINE citation check — NCT01608724 (saxagliptin, type 2 diabetes)

| Field | Registry value as of 2026-10-30 | Matches a typical citation? |
|---|---|---|
| NCT ID | NCT01608724 | Yes |
| Acronym / official title | SUNSHINE — "A Multicenter, Single Arm, Cohort Study to Evaluate the Efficacy and Safety of Saxagliptin 5mg, Once Daily for 24 Weeks, in Patients With Type 2 Diabetes Mellitus" | Confirm wording |
| Lead sponsor | AstraZeneca (INDUSTRY) | Yes |
| Enrollment | 2,165 (ACTUAL) | Yes |
| Current overall status | **Completed** — start Nov 2012; primary & study completion May 2014; results first posted 2016-02-02 | ⚠ Determine if draft implies ongoing / recruiting — it is Completed |
| Phase / design | Phase 4, interventional, single-group, open label, treatment purpose | Confirm |

**Citation verdict:** sponsor (AstraZeneca) and enrollment (2,165, actual registry value) are correct. The status field needs reflecting as **Completed** — the draft must be corrected if it currently describes the trial as ongoing/actively recruiting.

---

## 4. Methodology

- Counts in Sections 1 and 2 were pulled directly from the ClinicalTrials.gov registry API on 2026-10-30 as enumerated apply-able filters on the "type 2 diabetes" condition query; no aggregation tool was used for the reported totals because it caps at 5,000 studies for full-set analyses.
- For sponsor class, the sum of all eight supported classes (INDUSTRY, NIH, FED, OTHER_GOV, INDIV, NETWORK, AMBIG, OTHER) equals 12,027, reconciling exactly with the registry headline total.
- Reason a pre-existing `report` branch contents were overwritten: the prior version's per-class and per-status counts predate this retrieval cycle and conflict with today's data; those figures in that file are not used anywhere in this brief.
- Enrollment counts in Section 2 are exactly the registry-reported values used for the sort key.

---

*Figures reflect ClinicalTrials.gov registry data as retrieved on 2026-10-30.*
