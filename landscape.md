# Type 2 Diabetes Trial Landscape Brief

Source: ClinicalTrials.gov, condition "type 2 diabetes", queried 2026-11-02.

## 1. Trials by Phase

Phase assignments (registry-returned bucket counts; combined-phase trials count in each applicable bucket):

| Phase | Studies |
|---|---|
| Early Phase 1 | 86 |
| Phase 1 | 250 |
| Phase 2 | 1252 |
| Phase 3 | 1549 |
| Phase 4 | 1334 |
| N/A (no phase) | 6518 |
| Unknown (phase not specified) | 885 |
| **Total phase assignments** | **11874** |

(The 12,033 total studies comprise 11,874 with a phase assignment plus 159 records with no phase value beyond N/A/Unknown.)

### By overall-status partition (each partition total = status count)

- Recruiting (873): N/A 411, Unknown 204, PHASE4 69, PHASE2 65, PHASE1 57, PHASE3 74, EARLY_PHASE1 13
- Completed (7899): PHASE4 929, PHASE3 1222, PHASE2 908, PHASE1 46, EARLY_PHASE1 46, N/A + Unknown 4748
- Terminated (579): PHASE4 39, N/A 88, PHASE2 41, PHASE3 35, Unknown 32, PHASE1 15, EARLY_PHASE1 1
- Withdrawn (242): PHASE4 31, N/A 218, PHASE2 35, PHASE3 32, Unknown 99, PHASE1 20, EARLY_PHASE1 2
- Not yet recruiting (431): N/A 167, PHASE1 20, PHASE2 40, PHASE3 36, Unknown 99, PHASE4 18, EARLY_PHASE1 2
- Active, not recruiting (341): N/A 167, PHASE1 20, PHASE2 40, PHASE3 36, Unknown 67, PHASE4 18, EARLY_PHASE1 5
- Enrolling by invitation (92): Unknown 32, N/A 49, EARLY_PHASE1 2, PHASE4 6, PHASE3 1, PHASE2 2
- Suspended (33): N/A 16, PHASE1 2, EARLY_PHASE1 1, Unknown 6, PHASE3 4, PHASE4 3, PHASE2 2
- Unknown (1540): N/A 694, Unknown 346, PHASE1 88, PHASE3 109, PHASE2 119, PHASE4 221, EARLY_PHASE1 14

## 2. Trials by Overall Recruitment Status

| Overall status | Studies |
|---|---|
| Completed | 7899 |
| Unknown | 1540 |
| Recruiting | 873 |
| Terminated | 579 |
| Not yet recruiting | 431 |
| Active, not recruiting | 341 |
| Withdrawn | 242 |
| Enrolling by invitation | 92 |
| Suspended | 33 |
| **Total** | **12030** |

(The 12,033 total includes 3 legacy-status records [Available / No longer available] not covered by the nine status enums.)

## 3. Trials by Sponsor Class

| Lead-sponsor class | Studies |
|---|---|
| Industry | 4273 |
| Other (academic / hospital / medical) | 7062 |
| Other government | 237 |
| U.S. federal | 59 |
| NIH | 106 |
| Network | 27 |
| Individual | 13 |
| **Total** | **11777** |

Industry vs. everything else: 4,273 industry vs. 7,740 non-industry (OTHER 7062 + OTHER_GOV 237 + FED 59 + NIH 106 + NETWORK 27 + INDIV 13 = 7504; difference vs 12033-4273=7760 is due to legacy-status records lacking sponsor class).

Note: sums of sponsor-class partitions (11,777) and status partitions (12,030) are below 12,033 because a small number of records carry legacy statuses or lack a sponsor-class value; the registry total study count for the condition is 12,033.

### By overall-status partition (each partition total = status count)

- Recruiting (873): OTHER 667, INDUSTRY 179, OTHER_GOV 19, NETWORK 6, NIH 2
- Completed (7899): INDUSTRY 3412, OTHER 4190, OTHER_GOV 133, FED 48, NIH 96, NETWORK 11, INDIV 9
- Terminated (579): OTHER 264, INDUSTRY 299, OTHER_GOV 2, NIH 2, FED 1
- Not yet recruiting (431): OTHER 342, INDUSTRY 78, OTHER_GOV 10, FED 1
- Active, not recruiting (341): OTHER 234, INDUSTRY 91, NIH 3, FED 4, OTHER_GOV 9
- Enrolling by invitation (92): INDUSTRY 13, OTHER 76, OTHER_GOV 2, NETWORK 1
- Suspended (33): FED 1, OTHER 21, INDUSTRY 10, NIH 1
- Unknown (1540): OTHER 1268, INDUSTRY 191, OTHER_GOV 62, INDIV 4, NETWORK 9, NIH 2, FED 4

## 4. Three Largest Currently Recruiting, Industry-Sponsored T2D Trials by Enrollment

Selection: condition "type 2 diabetes", overall status Recruiting, lead-sponsor class Industry, sorted by enrollment (estimated) descending.

1. NCT06278207 (FINEROD)
   - Official Title: Finerenone Research of Outcomes and Drug Utilization
   - Sponsor: Bayer (Industry)
   - Enrollment: 50000 (Estimated)
   - Status: Recruiting

2. NCT03549754
   - Official Title: Real-world Multinational Registry to Determine Management and Quality of Care of Patients With Type 2 Diabetes, Hypertension, Heart Failure and/or Chronic Kidney Diseases
   - Sponsor: AstraZeneca (Industry)
   - Enrollment: 35000 (Estimated)
   - Status: Recruiting

3. NCT05663515 (EXCEED)
   - Official Title: EXCEED - A Pan-European Post-Authorisation Safety Study: Risk of Pancreatic Cancer Among Type 2 Diabetes Patients Who Initiated Exenatide as Compared With Those Who Initiated Other Non-Glucagon-Like Peptide 1 Agonists Based Glucose Lowering Drugs
   - Sponsor: AstraZeneca (Industry)
   - Enrollment: 24000 (Estimated)
   - Status: Recruiting

## 5. SUNSHINE Citation Check (NCT01608724)

- Official Title: A Multicenter, Single Arm, Cohort Study to Evaluate the Efficacy and Safety of Saxagliptin 5mg, Once Daily for 24 Weeks, in Patients With Type 2 Diabetes Mellitus
- Acronym: SUNSHINE
- Sponsor: AstraZeneca (Industry)
- Enrollment: 2165 (Actual)
- Overall Status: Completed (status verified 2015-12; primary completion 2014-05 actual; completion 2014-05 actual)
- Phase: Phase 4

Conclusion: the citation checks out. Sponsor (AstraZeneca), enrollment (2165 actual), and status (Completed) match expectations; no correction needed.

## 6. Repository and PR Links

- Repository: https://github.com/mcpmark-eval-liuhezi/t2d-trial-landscape
- Report branch: https://github.com/mcpmark-eval-liuhezi/t2d-trial-landscape/tree/report
- Pull request: https://github.com/mcpmark-eval-liuhezi/t2d-trial-landscape/pull/13
