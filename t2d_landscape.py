#!/usr/bin/env python3
"""
t2d_landscape.py
================

Type 2 diabetes trial landscape brief - summary statistics.

Computes landscape statistics from the first 20 interventional, Phase 3,
currently RECRUITING type 2 diabetes trials recorded from the
ClinicalTrials.gov registry (search condition: "type 2 diabetes").

Each trial record captured: NCT ID, brief title, lead sponsor,
lead-sponsor class (INDUSTRY / OTHER / ...), and enrollment target.

Statistics printed (one per line, key=value):
    trials              - total number of trials analyzed
    mean_enrollment     - mean enrollment target across the trials
    median_enrollment   - median enrollment target across the trials
    industry_sponsored  - number of trials with an INDUSTRY lead sponsor
"""

from statistics import mean, median

# The 20 trials recorded from the ClinicalTrials.gov registry.
# Registry search: condition "type 2 diabetes", interventional, Phase 3,
# current overall status RECRUITING. These are the first 20 results
# (registry default ranking) returned on the date the brief was compiled.
# Fields per trial: (NCT ID, brief title, lead sponsor, sponsor class,
#                    enrollment target)
TRIALS = [
    ("NCT07653477", "Phase III Study of UBT251 Injection in Patients With Type 2 Diabetes With Inadequate Glycemic Control on Metformin ± Sulfonylurea/SGLT2 Inhibitor Therapy (UNIGUIDE-2)", "The United Bio-Technology (Hengqin) Co., Ltd.", "INDUSTRY", 956),
    ("NCT07675499", "Exercise and Intranasal Insulin in Type 2 Diabetes", "Rutgers, The State University of New Jersey", "OTHER", 60),
    ("NCT07664553", "A Phase III Study to Investigate the Efficacy and Safety of Elecoglipron Compared With Placebo in Adults With Type 2 Diabetes Mellitus on Background Insulin", "AstraZeneca", "INDUSTRY", 600),
    ("NCT07784270", "A Study to Evaluate Effect of AZD6234 in Adult Participants With Type 2 Diabetes Mellitus and Obesity or Overweight", "AstraZeneca", "INDUSTRY", 1500),
    ("NCT07659574", "Phase III Study of UBT251 Injection in Patients With Type 2 Diabetes Mellitus With Inadequate Glycemic Control on Diet and Exercise Alone（UNIGUIDE-1）", "The United Bio-Technology (Hengqin) Co., Ltd.", "INDUSTRY", 360),
    ("NCT04786262", "A Safety, Tolerability, and Efficacy Study of VX-880 and VX-017 in Participants With Type 1 Diabetes", "Vertex Pharmaceuticals Incorporated", "INDUSTRY", 57),
    ("NCT07351045", "A Clinical Study to Evaluate the Effects of Enicepatide (RO7795068) in Participants With Obesity or Overweight Without Type 2 Diabetes", "Hoffmann-La Roche", "INDUSTRY", 2000),
    ("NCT07581145", "Effect of Semaglutide on Healing of Foot Ulcers in Type 2 Diabetes Patients", "Ole Lander Svendsen", "OTHER", 52),
    ("NCT07817251", "Research Study on How People With Type 2 Diabetes Tolerate Switching From Semaglutide to Cagrisema", "Novo Nordisk A/S", "INDUSTRY", 210),
    ("NCT06192693", "Fecal Microbiota Transfer to Improve Diabetes Control Post-bariatric Surgery", "Assistance Publique - Hôpitaux de Paris", "OTHER", 54),
    ("NCT07668336", "A Study of Orforglipron (LY3502970) Compared With Dulaglutide in Pediatric Participants With Type 2 Diabetes", "Eli Lilly and Company", "INDUSTRY", 170),
    ("NCT07392190", "A Study of Eloralintide (LY3841136) in Participants With Persistent Obesity Who Are Treated With a Weekly Incretin", "Eli Lilly and Company", "INDUSTRY", 900),
    ("NCT06647745", "A Randomized, Double-blind, Multi-center, Active-controlled, Phase 3 Clinical Trial to Evaluate the Efficacy and Safety of Combination Therapy of THP-00101, THP-00102, and THP-00103 in Subjects With T2DM and Essential Hypertension", "THPharm Corp.", "INDUSTRY", 221),
    ("NCT06451757", "KHENERFIN Study: A Trial to Evaluate the Efficacy and Safety of Sonlicromanol in Primary Mitochondrial Diseases", "Khondrion BV", "INDUSTRY", 220),
    ("NCT07082114", "A Phase 3 Study to Evaluate Efficacy and Safety of HDM1002 Tablets in Adults With Type 2 Diabetes Mellitus", "Hangzhou Zhongmei Huadong Pharmaceutical Co., Ltd.", "INDUSTRY", 800),
    ("NCT05605704", "Olive Leaf Extracts in the Control of Diabet", "University of Monastir", "OTHER", 500),
    ("NCT07093476", "Efficacy and Safety of Add-On Therapy With Empagliflozin in Patients With Type 2 Diabetes on a Background of Alogliptin and Metformin", "Celltrion", "INDUSTRY", 171),
    ("NCT07595549", "A Study to Learn About the Study Medicine Called Berobenatide (PF-08653944) in People With Overweight or Obesity", "Pfizer", "INDUSTRY", 954),
    ("NCT07670416", "A Study to Evaluate the Effects of Enicepatide in Participants With Obesity or Overweight, With or Without Type 2 Diabetes", "Hoffmann-La Roche", "INDUSTRY", 300),
    ("NCT05427084", "Canagliflozin Targeting Vascular Inflammation", "Ottawa Heart Institute Research Corporation", "OTHER", 24),
]


def main() -> None:
    """Compute and print the landscape statistics."""
    enrollments = [enrollment for (_, _, _, _, enrollment) in TRIALS]

    trials = len(TRIALS)
    mean_enrollment = mean(enrollments)
    median_enrollment = median(enrollments)
    industry_sponsored = sum(
        1 for (_, _, _, sponsor_class, _) in TRIALS if sponsor_class == "INDUSTRY"
    )

    print(f"trials={trials}")
    print(f"mean_enrollment={mean_enrollment}")
    print(f"median_enrollment={median_enrollment}")
    print(f"industry_sponsored={industry_sponsored}")


if __name__ == "__main__":
    main()