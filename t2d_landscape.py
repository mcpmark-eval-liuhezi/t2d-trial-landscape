#!/usr/bin/env python3
"""
t2d_landscape.py
================

Type 2 diabetes trial landscape brief - summary statistics.

Computes landscape statistics from the first 20 interventional, Phase 3,
currently RECRUITING type 2 diabetes trials recorded from the
ClinicalTrials.gov registry (search condition: "type 2 diabetes").

Each trial record captured: NCT ID, brief title, lead sponsor,
sponsor class, and enrollment target.

Statistics printed (one per line, key=value):
    trials              - total number of trials analyzed
    mean_enrollment     - mean enrollment target across the trials
    median_enrollment   - median enrollment target across the trials
    industry_sponsored  - number of trials with an INDUSTRY lead sponsor
"""

from statistics import mean, median

# (nct_id, lead_sponsor, sponsor_class, enrollment_target)
TRIALS = [
    ("NCT06220773", "Boryung Pharmaceutical Co., Ltd", "INDUSTRY", 276),
    ("NCT07481747", "Hudson Biotech", "INDUSTRY", 2539),
    ("NCT07662135", "AstraZeneca", "INDUSTRY", 900),
    ("NCT07754461", "Boehringer Ingelheim", "INDUSTRY", 600),
    ("NCT07613307", "Eli Lilly and Company", "INDUSTRY", 130),
    ("NCT07282600", "Eli Lilly and Company", "INDUSTRY", 1035),
    ("NCT05028140", "EMS", "INDUSTRY", 480),
    ("NCT06246799", "The University of Texas Health Science Center at San Antonio", "OTHER", 256),
    ("NCT05427084", "Ottawa Heart Institute Research Corporation", "OTHER", 24),
    ("NCT07082114", "Hangzhou Zhongmei Huadong Pharmaceutical Co., Ltd.", "INDUSTRY", 800),
    ("NCT07775404", "AstraZeneca", "INDUSTRY", 351),
    ("NCT05569772", "Universitaire Ziekenhuizen KU Leuven", "OTHER", 252),
    ("NCT07527078", "Gan & Lee Pharmaceuticals.", "INDUSTRY", 350),
    ("NCT07059377", "Ottawa Heart Institute Research Corporation", "OTHER", 100),
    ("NCT07060456", "Fujian Shengdi Pharmaceutical Co., Ltd.", "INDUSTRY", 300),
    ("NCT07662109", "AstraZeneca", "INDUSTRY", 2000),
    ("NCT06739122", "Eli Lilly and Company", "INDUSTRY", 55),
    ("NCT07784270", "AstraZeneca", "INDUSTRY", 1500),
    ("NCT07448974", "Tufts Medical Center", "OTHER", 100),
    ("NCT07662213", "AstraZeneca", "INDUSTRY", 1200),
]


def main() -> None:
    """Compute and print the landscape statistics."""
    enrollments = [enrollment for (_, _, _, enrollment) in TRIALS]

    trials = len(TRIALS)
    mean_enrollment = mean(enrollments)
    median_enrollment = median(enrollments)
    industry_sponsored = sum(
        1 for (_, _, sponsor_class, _) in TRIALS if sponsor_class == "INDUSTRY"
    )

    print(f"trials={trials}")
    print(f"mean_enrollment={mean_enrollment}")
    print(f"median_enrollment={median_enrollment}")
    print(f"industry_sponsored={industry_sponsored}")


if __name__ == "__main__":
    main()
