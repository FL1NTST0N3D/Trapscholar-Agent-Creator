---
name: ab-statistical-analysis
description: Run frequentist statistical analysis on A/B test results
version: 1.0.0
author: Shivendra Rawat (@0-shiv)
triggers:
  - /abtest analyze
  - analyze results
  - statistical analysis
  - is this significant
---

# Frequentist Statistical Analysis for A/B Tests

You are an expert statistician. When the user provides A/B test results, perform rigorous frequentist analysis and provide clear, actionable interpretation.

## Required Data

Collect from the user:

**For conversion rate tests (proportions):**
- Control: number of visitors (n₁) and conversions (x₁)
- Variant: number of visitors (n₂) and conversions (x₂)

**For continuous metric tests (revenue, time, etc.):**
- Control: sample size (n₁), mean (x̄₁), standard deviation (s₁)
- Variant: sample size (n₂), mean (x̄₂), standard deviation (s₂)

**Context:**
- Significance level (alpha, default 0.05)
- One-tailed or two-tailed (default: two-tailed)
- Whether multiple comparisons are involved

## Z-Test for Proportions

The standard test for comparing conversion rates between two groups.

### When to Use
- Binary outcome (converted / did not convert)
- Sample sizes > 30 per group (for normal approximation to hold)
- Expected number of successes and failures > 5 in each group (np > 5 and n(1-p) > 5)

### Calculation

```
Step 1: Calculate conversion rates
p₁ = x₁ / n₁  (control conversion rate)
p₂ = x₂ / n₂  (variant conversion rate)

Step 2: Calculate pooled proportion
p_pool = (x₁ + x₂) / (n₁ + n₂)

Step 3: Calculate standard error
SE = sqrt(p_pool × (1 - p_pool) × (1/n₁ + 1/n₂))

Step 4: Calculate Z-statistic
Z = (p₂ - p₁) / SE

Step 5: Calculate p-value
p_value = 2 × (1 - Phi(|Z|))   # two-tailed
p_value = 1 - Phi(Z)            # one-tailed (variant > control)

Step 6: Calculate confidence interval for the difference
CI = (p₂ - p₁) ± Z_α/2 × sqrt(p₁(1-p₁)/n₁ + p₂(1-p₂)/n₂)
```

### Interpretation Guide

| p-value | Interpretation |
|---------|---------------|
| < 0.001 | Very strong evidence against null hypothesis |
| 0.001 - 0.01 | Strong evidence against null hypothesis |
| 0.01 - 0.05 | Moderate evidence against null hypothesis |
| 0.05 - 0.10 | Weak evidence (some use 0.10 threshold) |
| > 0.10 | Insufficient evidence to reject null hypothesis |

**Critical reminder:** A p-value is NOT the probability that the null hypothesis is true. It is the probability of observing results at least as extreme as these, assuming the null hypothesis is true.

## T-Test for Means

For comparing continuous metrics (average order value, time on page, revenue per user).

### When to Use
- Continuous outcome variable
- Groups are independent
- Data is approximately normally distributed (or n > 30 by CLT)

### Calculation (Welch's t-test, preferred for unequal variances)

```
Step 1: Calculate means
x̄₁, x̄₂ (provided by user)

Step 2: Calculate t-statistic
t = (x̄₂ - x̄₁) / sqrt(s₁²/n₁ + s₂²/n₂)

Step 3: Calculate degrees of freedom (Welch-Satterthwaite)
df = (s₁²/n₁ + s₂²/n₂)² / ((s₁²/n₁)²/(n₁-1) + (s₂²/n₂)²/(n₂-1))

Step 4: Calculate p-value from t-distribution with df degrees of freedom

Step 5: Confidence interval
CI = (x̄₂ - x̄₁) ± t_α/2,df × sqrt(s₁²/n₁ + s₂²/n₂)
```

## Chi-Square Test

For comparing distributions across multiple categories (e.g., comparing conversion rates across 3+ variants simultaneously).

### When to Use
- Categorical outcomes
- 3 or more groups to compare simultaneously
- Expected frequency in each cell > 5

### Calculation

```
Step 1: Build contingency table
         | Converted | Not Converted | Total
Control  | x₁        | n₁ - x₁      | n₁
Var B    | x₂        | n₂ - x₂      | n₂
Var C    | x₃        | n₃ - x₃      | n₃

Step 2: Calculate expected values
E_ij = (Row_i_total × Column_j_total) / Grand_total

Step 3: Calculate chi-square statistic
χ² = Σ (O_ij - E_ij)² / E_ij

Step 4: Degrees of freedom
df = (rows - 1) × (columns - 1)

Step 5: p-value from chi-square distribution
```

If the chi-square test is significant, follow up with pairwise Z-tests (with Bonferroni correction) to identify which specific variants differ from control.

## Effect Size: Cohen's h

Statistical significance alone is insufficient. Always calculate and report effect size.

### Cohen's h (for proportions)

```
h = 2 × arcsin(sqrt(p₂)) - 2 × arcsin(sqrt(p₁))
```

| |h| | Interpretation |
|-----|----------------|
| 0.2 | Small effect |
| 0.5 | Medium effect |
| 0.8 | Large effect |

### Relative Lift

```
Relative lift = (p₂ - p₁) / p₁ × 100%
```

This is the business-facing metric. A 0.5 percentage point increase from 5% to 5.5% is a 10% relative lift.

## Practical vs. Statistical Significance

Always address both dimensions:

**Statistically significant + Practically significant:**
> The variant shows a [X]% relative lift with p=[value]. The effect size (Cohen's h = [value]) is [small/medium/large]. This improvement, if sustained, would generate approximately [estimated business impact]. Recommend: ship the variant.

**Statistically significant + NOT practically significant:**
> The variant shows a statistically significant difference (p=[value]), but the absolute improvement is only [X] percentage points ([Y]% relative lift). The engineering and maintenance cost of this change likely exceeds its business value. Recommend: do not ship. Test a bolder change.

**NOT statistically significant + Large observed effect:**
> The observed lift of [X]% is not statistically significant (p=[value]). The test may be underpowered. Current sample size gives [actual_power]% power to detect this effect size. Consider extending the test to [recommended_n] per variant ([additional_days] more days).

**NOT statistically significant + Small observed effect:**
> No significant difference detected (p=[value]). The observed lift of [X]% is small and within random variation. The test had [power]% power to detect a [MDE]% effect. Recommend: reject this hypothesis and move to the next test.

## Output Format

```
A/B TEST ANALYSIS RESULTS
===========================

SUMMARY
--------
Test:     [name]
Duration: [dates]
Status:   [SIGNIFICANT / NOT SIGNIFICANT / INCONCLUSIVE]

RESULTS
--------
           | Visitors | Conversions | Rate    |
Control    | [n₁]     | [x₁]        | [p₁]%  |
Variant    | [n₂]     | [x₂]        | [p₂]%  |

Observed lift:     [relative]% relative ([absolute] pp absolute)
Confidence interval: [[lower]%, [upper]%] for the difference

STATISTICAL TESTS
------------------
Test used:     [Z-test / t-test / chi-square]
Test statistic: [value]
p-value:       [value]
Significance:  [Yes/No] at alpha = [value]
Effect size:   Cohen's h = [value] ([small/medium/large])
Power:         [actual power given observed effect size]

INTERPRETATION
---------------
[2-3 sentences interpreting the result in plain language]

RECOMMENDATION
---------------
[Ship / Do not ship / Extend test / Redesign test]
[Reasoning for recommendation]

NEXT STEPS
-----------
[Specific follow-up actions]
```

## Using the Python Script

For exact calculations, run:

```bash
python scripts/statistical_analyzer.py \
  --control-visitors 5000 --control-conversions 150 \
  --variant-visitors 5000 --variant-conversions 185 \
  --alpha 0.05
```

## Sanity Checks Before Analysis

Before running any analysis, verify:

1. **Sample Ratio Mismatch (SRM):** Check that the actual traffic split matches the intended split. A chi-square test on the visitor counts should have p > 0.001. SRM indicates a bug in the randomization or tracking.
2. **Data quality:** Check for duplicate users, bot traffic, or data pipeline delays.
3. **Time integrity:** Confirm the test ran for the planned duration without interruptions.
4. **Novelty/primacy effects:** If the test ran for less than 2 weeks, note that results may include novelty effects.
