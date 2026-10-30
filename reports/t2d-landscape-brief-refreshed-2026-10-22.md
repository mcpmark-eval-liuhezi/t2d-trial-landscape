# Type 2 Diabetes Trial Landscape — Quarterly Brief (Refreshed)

**Data source:** ClinicalTrials.gov registry, queried via API v2 on **2026-10-22**
**Prepared by:** HeziLiu (Hezi Liu) for the group's quarterly therapy-landscape review
**Companion draft PR:** `mcpmark-eval-liuhezi/t2d-trial-landscape#13`

> **Publication note:** This brief was intended for a GitHub gist, but the active personal access token lacks gist scope (403 on gist creation), so it is published here as a single markdown file instead.

---

## 0. GitHub pull request status

**Most recent PR authored by HeziLiu anywhere on GitHub** (of 970 total): **"Add greeting module draft" — mcpmark-eval-liuhezi/code-review-drill-3#1**, created 2026-10-22T03:17:19Z.
- **State:** OPEN
- **Mergeable:** Yes (`mergeable: true`, `mergeable_state: clean`; 1 commit, 2 files, +13/−0)
- **Status checks:** None configured — the head commit has zero check runs (`total_count: 0`), so there is nothing failing (and nothing passing either).

**The landscape brief draft itself** — "T2D trial landscape one-pager: registry status/phase/sponsor/country cuts, T1D contrast, SUNSHINE case study" (`t2d-trial-landscape#13`, created 2026-10-21T20:19:24Z):
- **State:** OPEN
- **Mergeable:** Yes (`mergeable: true`, `mergeable_state: clean`; 2 commits, 1 file, +158/−0)
- **Status checks:** None configured — the repo has no GitHub Actions workflows, so the head commit reports zero check runs.

---

## 1. Five largest currently recruiting Phase 3 T2D trials (by target enrollment)

Registry query: condition "type 2 diabetes", `AREA[Phase]PHASE3`, status = RECRUITING, sorted by enrollment descending. The registry returns **74** recruiting Phase 3 T2D trials; the five largest:

| # | NCT ID | Short title | Lead sponsor | Enrollment |
|---|---|---|---|---:|
| 1 | NCT07064473 | EASi-PROTKT™ — Vicadrostat (BI 690517) + Empagliflozin in T2D, Hypertension & CVD | Boehringer Ingelheim | 11,800 |
| 2 | NCT05633810 | COLchicine and Non-enteric Coated Aspirin CVOT in Type 2 Diabetes (CONCORD) | Montreal Heart Institute | 10,000 |
| 3 | NCT07667803 | Master Protocol: Elecoglipron in Obesity/Overweight With or Without T2DM | AstraZeneca | 4,500 |
| 4 | NCT07481747 | Tirzepatide Once Weekly vs Placebo in Obese/Overweight (SURMOUNT-1) | Hudson Biotech | 2,539 |
| 5 | NCT07784725 | AZD6234 in Obesity/Overweight With Weight-related Comorbidity Without T2DM | AstraZeneca | 2,500 |

**Arithmetic (shown in full):**
- Combined enrollment: `11800 + 10000 + 4500 + 2539 + 2500 = 31,339`
- Average per trial: `31339 / 5 = 6,267.8`
- Largest trial's share of the five-trial total: `11800 / 31339 * 100 = 37.65%` (37.6527649254922%)

---

## 2. Five largest completed semaglutide T2D trials (by enrollment)

Registry query: condition "type 2 diabetes" + intervention "semaglutide", status = COMPLETED, sorted by enrollment descending. The registry returns **198** completed matches; the five largest:

| # | NCT ID | Short title | Lead sponsor | Enrollment |
|---|---|---|---|---:|
| 1 | NCT07096063 | Comparative Effectiveness of Tirzepatide and Semaglutide at CV Risk (TIRZSEMA-CVOT) | Brigham and Women's Hospital | 887,132 |
| 2 | NCT04572165 | Semaglutide & Pancreatic Cancer Risk — Nordic Registry Cohort Study | Novo Nordisk A/S | 194,928 |
| 3 | NCT06659744 | Emulation of the SUSTAIN6 Diabetes Trial Using Healthcare Claims | Brigham and Women's Hospital | 158,310 |
| 4 | NCT07619495 | Injectable Semaglutide vs Dulaglutide at Cardiovascular Risk | Brigham and Women's Hospital | 120,000 |
| 5 | NCT06779929 | Tirzepatide vs Dulaglutide (SURPASS CVOT) or Semaglutide on MACE in T2D | Brigham and Women's Hospital | 70,000 |

> **Caveat:** all five top matches are observational / claims- or registry-based cohort studies (real-world-data trial emulations and drug-safety cohorts), not randomized interventional trials — hence six-figure enrollments.

**Arithmetic (shown in full):**
- Combined enrollment: `887132 + 194928 + 158310 + 120000 + 70000 = 1,430,370`
- Average per trial: `1430370 / 5 = 286,074.0`
- Comparison to item 1's recruiting Phase 3 average (6,267.8):
  - Percentage difference: `(286074/5 − 31339/5) / (31339/5) * 100 = (286074 − 6267.8) / 6267.8 * 100 = 279806.2 / 6267.8 * 100 = +4,464.19%` (4,464.185200548836%)
  - Ratio: `286074 / 6267.8 = 45.64×`
  - Absolute gap: `286074 − 6267.8 = 279,806.2` participants
  - In other words, the completed semaglutide top-5 average is ~45.6× (≈ +4,464%) the size of the recruiting Phase 3 top-5 average; equivalently, the Phase 3 average is ~97.8% smaller.

---

## 3. Recruiting T2D trials with sites in China

Registry query: condition "type 2 diabetes", `AREA[LocationCountry]China`, status = RECRUITING.

- **Count:** **118** currently recruiting T2D trials have study sites in China
- Total currently recruiting T2D trials (all countries): **872**
- **Share:** `118 / 872 * 100 = 13.53%` (13.53211009174312%)

**Two examples:**
| NCT ID | Title | China site(s) |
|---|---|---|
| NCT07481747 | Efficacy and Safety of Tirzepatide Once Weekly Versus Placebo in Participants Who Are Either Obese or Overweight With Weight-Related Comorbidities (SURMOUNT-1) | Shenzhen |
| NCT07121504 | Hybrid Closed-Loop for Perioperative Glycemic Control in T2DM With Parenteral Nutrition | Changsha |

---

## 4. Aggregated breakdown of T2D trials — by phase and by sponsor type

**Population: 12,002 type 2 diabetes studies** currently in the registry (query: condition "type 2 diabetes"). The registry's trend-analysis tool caps analyses at 5,000 studies, so the population was partitioned into three disjoint, individually analyzed slices: **non-completed studies (4,117)** + **completed & industry-sponsored (3,410)** + **completed & non-industry (4,475)**. Reconciliation: `4117 + 3410 + 4475 = 12,002` (and `4117 + 7885 = 12,002`).

### By phase (summed across the three slices)

| Phase | Non-completed | Completed, industry | Completed, non-industry | Total |
|---|---:|---:|---:|---:|
| Phase 1 | 261 | 849 | 137 | 1,247 |
| Early Phase 1 | 41 | 3 | 42 | 86 |
| Phase 2 | 408 | 593 | 312 | 1,313 |
| Phase 3 | 423 | 977 | 245 | 1,645 |
| Phase 4 | 479 | 379 | 550 | 1,408 |
| N/A (no phase recorded) | 1,781 | 238 | 2,478 | 4,497 |
| Unknown | 841 | 443 | 832 | 2,116 |

**Cross-checks (shown in full):**
- Phase 1: `261 + 849 + 137 = 1,247`
- Early Phase 1: `41 + 3 + 42 = 86`
- Phase 2: `408 + 593 + 312 = 1,313`
- Phase 3: `423 + 977 + 245 = 1,645`
- Phase 4: `479 + 379 + 550 = 1,408`
- N/A: `1781 + 238 + 2478 = 4,497`
- Unknown: `841 + 443 + 832 = 2,116`
- Phase assignments total: `1247 + 86 + 1313 + 1645 + 1408 = 5,699` (+ 4,497 N/A + 2,116 Unknown = 12,312 assignments across 12,002 studies — combined-phase trials, e.g. Phase 1/2, are counted in each listed phase)

### By sponsor type (industry vs. everything else)

| Sponsor class | Count | Share of 12,002 |
|---|---:|---:|
| Industry (`AREA[LeadSponsorClass]INDUSTRY`) | 4,355 | 36.29% |
| Non-industry (academic/hospital "other", government, NIH, networks, individuals) | 7,647 | 63.71% |
| **Total** | **12,002** | **100%** |

**Arithmetic (shown in full):**
- Industry share: `4355 / 12002 * 100 = 36.29%` (36.28561906348941%)
- Non-industry share: `7647 / 12002 * 100 = 63.71%` (63.71438093651059%)
- Partition check: `4355 + 7647 = 12,002`
- Sub-splits used for the phase partitioning: completed & industry = 3,410; completed & non-industry = 4,475; check: `3410 + 4475 = 7,885` = all completed T2D studies

---

## Methodology notes

- All figures are live ClinicalTrials.gov counts retrieved **2026-10-22** — not carried over from prior decks.
- "Type 2 diabetes" population = registry condition search `query.cond="type 2 diabetes"` (12,002 studies).
- Recruiting pool = `overallStatus=RECRUITING` (872 studies); recruiting Phase 3 pool = 74; recruiting with-China-sites pool = 118 (country filter applied on study locations).
- Top-5 lists are the registry's own enrollment-descending sort of the respective result sets; enrollment figures for recruiting trials are target/estimated enrollment, while completed trials report actual enrollment.
- The phase and sponsor-type aggregations use the registry's `analyze_trends` aggregation tool, which caps a single analysis at 5,000 studies; the 12,002-study population was therefore partitioned into three disjoint slices (non-completed / completed-industry / completed-non-industry), analyzed separately, and summed. Slice totals and all cross-totals reconcile exactly to 12,002, and the resulting phase and sponsor figures match the prior landscape one-pager (Phase 3: 1,645; Phase 4: 1,408; Phase 2: 1,313; Phase 1: 1,247; no-phase: 4,497; industry: 4,355 vs. non-industry: 7,647).
- Status of the draft PR: open and cleanly mergeable, with no CI checks configured on the repository.

## Sources
- ClinicalTrials.gov API v2 (studies search + trends aggregation), accessed 2026-10-22.
- GitHub REST API (pull request, combined status, workflows) for repositories `mcpmark-eval-liuhezi/code-review-drill-3` and `mcpmark-eval-liuhezi/t2d-trial-landscape`, accessed 2026-10-22.