# Type 2 Diabetes Clinical Trial Landscape

**Data source:** ClinicalTrials.gov public registry (API v2), live counts retrieved 2026-10-21.
**Query:** condition search "type 2 diabetes" — 12,002 registered studies in total.
**Case-study anchor:** SUNSHINE (saxagliptin), NCT01608724.

**Headline numbers.** Type 2 diabetes is one of the largest single-condition portfolios in the registry: 12,002 studies, of which only **872 (7.3%) are currently recruiting** — 65.7% have already completed, and a further 14.6% sit in an inactive/terminated status. **Academic/hospital ("other") sponsors lead with 7,189 studies (59.9%) vs. 4,355 industry (36.3%)**, and among phased trials Phase 3 (1,645) is the most common phase. The registry's country counts are location-sites, not studies: the United States (48,300 sites) and China (4,759) host the most activity.

---

## Landscape

### 1. Type 2 diabetes trials by overall status (12,002 studies)

| Overall status | Count | % of studies |
|---|---:|---:|
| Completed | 7,885 | 65.7% |
| Unknown | 1,535 | 12.8% |
| Terminated | 578 | 4.8% |
| Recruiting | 872 | 7.3% |
| Active, not recruiting | 339 | 2.8% |
| Not yet recruiting | 423 | 3.5% |
| Withdrawn | 242 | 2.0% |
| Enrolling by invitation | 92 | 0.8% |
| Suspended | 33 | 0.3% |
| No longer available | 2 | 0.0% |
| Available | 1 | 0.0% |
| **Total** | **12,002** | **100%** |

*Currently active (recruiting, not yet recruiting, active-not-recruiting, enrolling by invitation): 1,726 studies (14.4%).*

### 2. Type 2 diabetes trials by phase

| Phase | Count | % of studies |
|---|---:|---:|
| Phase 3 | 1,645 | 13.7% |
| Phase 4 | 1,408 | 11.7% |
| Phase 2 | 1,313 | 10.9% |
| Phase 1 | 1,247 | 10.4% |
| Early Phase 1 | 86 | 0.7% |
| N/A (no phase recorded) | 4,497 | 37.5% |
| Phase not specified in record | 1,806 | 15.0% |
| **Total (phase-bucket sum)** | **12,002** | **100%** |

*Phase assignments are mutually exclusive here (each study in exactly one bucket; 1,806 records carry no phase in the registry). Among the 5,699 phased trials, Phase 3 (28.9% of phased) and Phase 4 (24.7%) dominate — the pipeline skews late-stage.*

### 3. Type 2 diabetes trials by sponsor class

| Sponsor class | Count | % of studies |
|---|---:|---:|
| Other (academic, hospitals, non-profit) | 7,189 | 59.9% |
| Industry | 4,355 | 36.3% |
| Other government | 244 | 2.0% |
| NIH | 108 | 0.9% |
| U.S. federal agency (FED) | 66 | 0.5% |
| Research network | 27 | 0.2% |
| Individual | 13 | 0.1% |
| **Total** | **12,002** | **100%** |

### 4. Type 2 diabetes trials by country (top 20; location-sites, not studies)

| Country | Registry count | | Country | Registry count |
|---|---:|---|---|---:|
| United States | 48,300 | | Romania | 1,066 |
| China | 4,759 | | Canada | 1,065 |
| Germany | 2,956 | | Sweden | 899 |
| India | 2,632 | | Japan | 845 |
| United Kingdom | 2,033 | | Spain | 821 |
| France | 2,024 | | India... *(see below)* | — |
| Poland | 1,828 | | Argentina | 792 |
| Mexico | 1,613 | | South Africa | 770 |
| Russia | 612 | | Italy | 717 |
| South Korea | 1,710 | | Netherlands | 698 |

A multi-country trial is counted once per country it runs in, so country counts exceed the 12,002-study total. **United States (48,300) hosts roughly 5.3× the sites of the runner-up, China (4,759)**. Rounding out the top ten: Germany 2,956, India 2,632, United Kingdom 2,033, France 2,024, Poland 1,828, Mexico 1,613, South Korea 1,710, Russia 612.

> **Counting caveat (important for review):** the registry reports *study-location entries*, not distinct studies — one global trial contributes a count to every country it operates in, so the country table sums to far more than 12,002. The status, phase, and sponsor-class tables above are study-level counts and each sums exactly to 12,002.

### 5. Contrast: type 1 diabetes (4,668 studies) vs. type 2 diabetes (12,002 studies)

**Type 1 diabetes by overall status (4,668 studies):**

| Overall status | Type 1 count | Type 1 % | T2D count | T2D % |
|---|---:|---:|---:|---:|
| Completed | 2,997 | 64.2% | 7,885 | 65.7% |
| Recruiting | 423 | 9.1% | 872 | 7.3% |
| Unknown | 478 | 10.2% | 1,535 | 12.8% |
| Terminated | 260 | 5.6% | 578 | 4.8% |
| Active, not recruiting | 159 | 3.4% | 339 | 2.8% |
| Not yet recruiting | 158 | 3.4% | 423 | 3.5% |
| Withdrawn | 138 | 3.0% | 242 | 2.0% |
| Enrolling by invitation | 34 | 0.7% | 92 | 0.8% |
| Suspended | 14 | 0.3% | 33 | 0.3% |
| **Total** | **4,668** | | **12,002** | |

**Type 1 diabetes by phase (4,668 studies):**

| Phase | Type 1 count | Type 1 % | T2D count | T2D % |
|---|---:|---:|---:|---:|
| Phase 3 | 418 | 9.0% | 1,645 | 13.7% |
| Phase 4 | 265 | 5.7% | 1,408 | 11.7% |
| Phase 2 | 687 | 14.7% | 1,313 | 10.9% |
| Phase 1 | 727 | 15.6% | 1,247 | 10.4% |
| Early Phase 1 | 62 | 1.3% | 86 | 0.7% |
| N/A (no phase recorded) | 1,784 | 38.2% | 4,497 | 37.5% |
| Phase not specified in record | 968 | 20.7% | 1,806 | 15.0% |
| **Total** | **4,668** | | **12,002** | |

**How lopsided is it?** The T2D portfolio is **2.6× the size of the T1D portfolio (12,002 vs. 4,668 studies)**. In absolute terms, T2D outnumbers T1D in every phase — most starkly in late-stage work: 1,645 Phase 3 T2D studies vs. 418 for type 1 (**3.9× more**), and 1,408 Phase 4 vs. 265 (**5.3× more**). Type 1 research skews relatively earlier (Phase 1 + Phase 2 = 1,414 studies, 30.3% of its portfolio vs. 21.3% for T2D), while T2D carries proportionally more Phase 3/4 registrational and post-marketing work (25.5% vs. 14.7%). Type 1 also runs slightly "greener" on current activity: 423 recruiting studies (9.1% of portfolio) vs. 872 for T2D (7.3%), though absolute active T2D studies (1,726) still outnumber T1D's ~754.

---

## Case study: SUNSHINE

**The AstraZeneca saxagliptin study (SUNSHINE) — registry profile**

| Field | Registry value |
|---|---|
| **NCT number** | NCT01608724 |
| **Acronym** | SUNSHINE (org study ID D1680L00008) |
| **Official title** | A Multicenter, Single Arm, Cohort Study to Evaluate the Efficacy and Safety of Saxagliptin 5mg, Once Daily for 24 Weeks, in Patients With Type 2 Diabetes Mellitus |
| **Lead sponsor** | AstraZeneca — **Industry** (sponsor class) |
| **Study design** | Interventional, Phase 4 — multicenter, single-arm, open-label (non-randomized, single-group, no masking), treatment purpose; drug: saxagliptin (Onglyza), oral 5 mg once daily for 24 weeks |
| **Enrollment** | 2,165 participants (actual) |
| **Start date** | November 2012 |
| **Primary completion date** | May 2014 (actual) |
| **Current status** | **Completed** |
| **Registry record** | https://clinicaltrials.gov/study/NCT01608724 |

Additional registry detail: conducted at research sites across China; primary outcome = absolute change from baseline in HbA1c at weeks 6/12/24; status last verified December 2015; study completion May 2014 (actual); responsible party = sponsor.

---

## Sources

- **Clinical study record:** NCT01608724 (SUNSHINE, saxagliptin 5 mg, AstraZeneca) — full registry record retrieved from ClinicalTrials.gov via the study-record API.
- **Registry analyses relied on** (ClinicalTrials.gov analysis tools, condition query "type 2 diabetes", retrieved 2026-10-21):
  - Count by overall recruitment status
  - Count by phase
  - Count by sponsor class
  - Count by country (location-sites)
  - Type 1 diabetes contrast: count by overall status and count by phase (condition query "type 1 diabetes", 4,668 studies)
- **Methodology note:** the registry's analysis tool caps each analysis at 5,000 studies, and the T2D population (12,002) exceeds that cap. The full population was therefore partitioned into five disjoint slices (4,117 / 2,773 / 2,043 / 1,822 / 1,247 studies), each analyzed separately, with counts summed. The slice totals reconcile exactly to the unscoped condition-query total (12,002), confirming complete, non-overlapping coverage. Type 1 diabetes (4,668 studies) was analyzed directly in a single pass. All counts are reported exactly as the registry returned them; no estimates from prior materials were used.
