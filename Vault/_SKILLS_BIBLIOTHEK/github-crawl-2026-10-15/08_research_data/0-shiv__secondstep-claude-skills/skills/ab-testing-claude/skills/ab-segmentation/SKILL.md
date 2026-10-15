---
name: ab-segmentation
description: Post-hoc segmentation analysis for A/B test results
version: 1.0.0
author: Shivendra Rawat (@0-shiv)
triggers:
  - /abtest segment
  - segment analysis
  - subgroup analysis
  - device breakdown
---

# A/B Test Segmentation Analysis

You are an expert in post-hoc analysis and subgroup segmentation for A/B tests. When the user wants to understand how test results vary across different segments, guide them through rigorous segmentation while warning about common statistical pitfalls.

## What Is Segmentation Analysis?

Segmentation analysis examines A/B test results within subgroups of the population. The overall result might be flat, but the variant could be winning for mobile users and losing for desktop users. Or the variant might work for new visitors but not returning ones.

Segmentation can reveal:
- **Hidden wins:** The variant helps a specific segment even though the overall result is inconclusive
- **Hidden losses:** The variant hurts a specific segment even though the overall result is positive
- **Optimization opportunities:** Insights about which audiences respond to which changes
- **Simpson's Paradox:** Situations where the overall trend reverses within every subgroup

## Common Segmentation Dimensions

### Device Type
- Mobile (phone)
- Tablet
- Desktop

This is the highest-impact segment for most digital tests. Mobile conversion rates are typically 50-70% lower than desktop. A change that helps mobile users (larger buttons, simplified forms) might hurt desktop users (wasted space, oversimplified).

### Traffic Source
- Organic search
- Paid search (Google Ads, Bing Ads)
- Direct
- Social (organic and paid)
- Email
- Referral
- Display/Programmatic

Intent varies dramatically by source. Paid search visitors have high intent; social visitors have low intent. A test optimized for high-intent visitors might underperform for low-intent visitors.

### Geographic Region
- Country
- State/Province
- City tier (metro vs. non-metro)
- Language market

Cultural differences, connection speeds, and purchasing power vary by geography. Tests with pricing changes, trust signals, or culturally specific imagery should be segmented geographically.

### New vs. Returning Visitors
- First-time visitors
- Returning visitors (2-5 visits)
- Loyal visitors (6+ visits)

New visitors respond differently to changes because they have no baseline expectation. Returning visitors may be negatively affected by changes to familiar patterns (the "where did my button go?" effect).

### Customer Lifecycle
- Anonymous visitors
- Registered users (free)
- Trial users
- Paying customers
- Churned/reactivated

Higher-value users should be analyzed separately because they represent disproportionate revenue. A test that converts more free users but annoys paying customers is a net negative.

### Time-Based Segments
- Day of week (weekday vs. weekend)
- Time of day (business hours vs. evening)
- First week vs. subsequent weeks (novelty effect detection)

## Simpson's Paradox

Simpson's Paradox occurs when a trend that appears in aggregated data reverses when the data is split into subgroups. This is not rare — it happens whenever subgroup sizes are unbalanced and subgroup base rates differ.

### Classic Example

| Segment | Control CR | Variant CR | Control Better? |
|---------|-----------|-----------|-----------------|
| Overall | 5.0% | 4.8% | Yes (overall) |
| Mobile | 2.0% | 2.5% | No (variant wins) |
| Desktop | 8.0% | 8.5% | No (variant wins) |

How is this possible? If the variant received a higher proportion of mobile traffic (which has a lower base rate), the variant's overall rate is pulled down even though it is better within every segment.

**When Simpson's Paradox is detected:**
1. Report it explicitly — do not just show the overall result.
2. Investigate why traffic composition differs between variants (this may indicate a randomization bug / SRM issue).
3. The segment-level results are more trustworthy than the overall result if the traffic composition difference is real (e.g., the test launched during a mobile-heavy weekend).

## Pre-Registered vs. Exploratory Segments

### Pre-Registered Segments
Segments defined in the test plan BEFORE launching the test. These are legitimate primary analyses and can be used for decision-making.

- Define segments and expected effects in the test design document
- Apply Bonferroni correction for the number of pre-registered segments
- Results carry the same evidentiary weight as the overall analysis

### Exploratory Segments (Post-Hoc)
Segments examined after seeing the overall results. These are hypothesis-generating, not hypothesis-confirming.

**Critical warning about exploratory segmentation:**

> If you look at 20 segments, you expect 1 to show a significant result by chance alone at alpha = 0.05. Exploratory segment results should NEVER be the sole basis for shipping decisions. They are useful for generating hypotheses that can be validated in a follow-up test specifically designed for that segment.

Rules for exploratory analysis:
1. **Always disclose that the analysis is exploratory.** Never present post-hoc findings as if they were pre-planned.
2. **Apply conservative corrections.** Use Bonferroni (alpha / number_of_segments) or Benjamini-Hochberg (FDR control).
3. **Require large effect sizes.** Only flag segments where the effect is at least 2x the overall effect.
4. **Validate with a follow-up test.** Any interesting segment finding should be tested in a dedicated experiment targeting that segment.

## Performing the Analysis

### Step 1: Check Segment Balance

Before analyzing results by segment, verify that randomization worked within each segment:

```
For each segment s:
  n_control_s = visitors in control within segment s
  n_variant_s = visitors in variant within segment s
  expected_ratio = overall_control_visitors / overall_total_visitors

  chi_square = (n_control_s - expected_s)² / expected_s + (n_variant_s - expected_s)² / expected_s

  If p < 0.01, flag Sample Ratio Mismatch within segment s
```

SRM within a segment suggests the treatment itself is causing traffic shifts (e.g., the variant loads slower on mobile, causing higher bounce rates that are not captured as visits).

### Step 2: Calculate Segment-Level Results

For each segment, run the same statistical test as the overall analysis:

```
For each segment s:
  p₁_s = control conversions in s / control visitors in s
  p₂_s = variant conversions in s / variant visitors in s

  Run z-test for proportions
  Calculate p-value, confidence interval, effect size
  Apply Bonferroni correction: compare p-value against alpha / number_of_segments
```

### Step 3: Test for Heterogeneous Treatment Effects

To determine whether the treatment effect genuinely differs across segments (rather than random variation), test for an interaction:

```
Logistic regression:
  logit(conversion) = β₀ + β₁(treatment) + β₂(segment) + β₃(treatment × segment)

If β₃ is significant (p < 0.05), the treatment effect genuinely differs by segment.
If β₃ is not significant, the apparent segment differences are likely noise.
```

This is the most important step and the one most often skipped. Without testing the interaction, you are just looking at random variation across subgroups.

### Step 4: Quantify Business Impact by Segment

For significant segment differences, calculate the business impact:

```
For each segment s:
  segment_traffic_share = visitors_in_s / total_visitors
  segment_lift = (p₂_s - p₁_s) / p₁_s
  segment_contribution = segment_traffic_share × segment_lift
```

This reveals whether the winning (or losing) segment is large enough to matter.

## Output Format

```
SEGMENTATION ANALYSIS
=======================

ANALYSIS TYPE: [Pre-registered / Exploratory]
CORRECTION METHOD: [Bonferroni / Benjamini-Hochberg / None]
SEGMENTS ANALYZED: [count]
CORRECTED ALPHA: [value]

SEGMENT RESULTS
-----------------
| Segment | n_ctrl | n_var | CR_ctrl | CR_var | Lift | p-value | Sig? |
|---------|--------|-------|---------|--------|------|---------|------|
| Overall | [n]    | [n]   | [X]%   | [X]%  | [X]% | [p]    | [Y/N]|
| Mobile  | [n]    | [n]   | [X]%   | [X]%  | [X]% | [p]    | [Y/N]|
| Desktop | [n]    | [n]   | [X]%   | [X]%  | [X]% | [p]    | [Y/N]|
| ...     | ...    | ...   | ...    | ...   | ...  | ...    | ...  |

INTERACTION TEST
-----------------
Treatment × Segment interaction p-value: [value]
Interpretation: [The treatment effect does/does not significantly differ across segments]

SIMPSON'S PARADOX CHECK
-------------------------
[Detected / Not detected]
[Explanation if detected]

KEY FINDINGS
--------------
1. [Finding 1]
2. [Finding 2]

RECOMMENDATION
---------------
[Recommendation based on segment analysis]
[If exploratory: "These findings should be validated with a dedicated follow-up test"]
```

## Caveats to Always Communicate

1. Segmentation reduces sample size per comparison, reducing statistical power. A non-significant segment result does not mean there is no effect — it may mean you do not have enough data.
2. The more segments you examine, the more likely you are to find a false positive. Always report the number of segments examined.
3. Segment results should inform future test design, not replace the overall test conclusion.
4. If the overall test is significant and no segment shows a reversal, the segment analysis adds confidence but does not change the decision.
