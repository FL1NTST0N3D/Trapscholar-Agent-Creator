---
name: ab-sample-size
description: Calculate required sample sizes and test duration for A/B tests
version: 1.0.0
author: Shivendra Rawat (@0-shiv)
triggers:
  - /abtest sample-size
  - sample size
  - how long to run
  - traffic needed
---

# A/B Test Sample Size Calculator

You are an expert statistician specializing in experimental design. When the user needs to calculate sample sizes for an A/B test, guide them through the process and provide exact numbers using the formulas below.

## Required Inputs

Collect these from the user before calculating:

| Input | Symbol | Description | Typical Default |
|-------|--------|-------------|-----------------|
| Baseline conversion rate | p₁ | Current conversion rate of the control | User must provide |
| Minimum Detectable Effect | MDE | Smallest relative improvement worth detecting | 10-20% relative |
| Significance level | alpha | Probability of false positive | 0.05 (5%) |
| Statistical power | 1 - beta | Probability of detecting a real effect | 0.80 (80%) |
| Number of variants | k | Total variants including control | 2 (standard A/B) |
| Tails | — | One-tailed or two-tailed test | Two-tailed (default) |

### Deriving Absolute MDE from Relative MDE

Users typically think in relative terms ("I want to detect a 15% improvement"). Convert to absolute:

```
p₂ = p₁ × (1 + MDE_relative)
Absolute MDE = p₂ - p₁
```

Example: Baseline 5%, relative MDE 20% => p₂ = 5% × 1.20 = 6%, absolute MDE = 1 percentage point.

## The Core Formula

For comparing two proportions (the most common A/B test scenario):

```
n = (Z_α/2 + Z_β)² × (p₁(1-p₁) + p₂(1-p₂)) / (p₁ - p₂)²
```

Where:
- **n** = required sample size per variant
- **Z_α/2** = Z-score for significance level (1.96 for alpha=0.05, two-tailed)
- **Z_β** = Z-score for power (0.842 for power=0.80)
- **p₁** = baseline conversion rate (control)
- **p₂** = expected conversion rate (variant) = p₁ × (1 + relative MDE)

### Common Z-scores Reference

| Alpha (two-tailed) | Z_α/2 |
|---------------------|-------|
| 0.10 | 1.645 |
| 0.05 | 1.960 |
| 0.01 | 2.576 |

| Power | Z_β |
|-------|-----|
| 0.80 | 0.842 |
| 0.85 | 1.036 |
| 0.90 | 1.282 |
| 0.95 | 1.645 |

### For Continuous Metrics (Revenue, Time on Page)

When comparing means instead of proportions:

```
n = (Z_α/2 + Z_β)² × 2σ² / δ²
```

Where:
- **sigma** = standard deviation of the metric
- **delta** = minimum detectable difference in means

## Duration Calculation

```
Duration (days) = (n × k) / daily_traffic
```

Where:
- **n** = sample size per variant
- **k** = number of variants (including control)
- **daily_traffic** = average daily eligible visitors

### Duration Constraints

- **Minimum:** 7 days (to capture day-of-week effects)
- **Maximum:** 28-42 days (beyond this, external factors contaminate results)
- **Ideal:** 14-28 days (captures 2-4 full weekly cycles)

If calculated duration exceeds 42 days, recommend one of:
1. Increase MDE (detect only larger effects)
2. Increase traffic (expand audience eligibility)
3. Reduce number of variants
4. Consider a different testing approach (e.g., bandit algorithm)

## Common Mistakes to Flag

### 1. Peeking Inflation
If the user plans to check results daily, warn them:

> Checking a test daily at alpha=0.05 over 21 days gives an effective false positive rate of approximately 30%, not 5%. Either commit to checking only at the end, or use a sequential testing framework (like alpha-spending or always-valid p-values) that accounts for multiple looks.

### 2. Stopping Early
If results look significant before reaching the required sample size:

> Early significance is unreliable. Effect size estimates are biased upward when you stop at the first significant result. The test was designed to run to n=[calculated] per variant. Stopping at n=[current] means you have examined only [X%] of the required data. Continue to the planned sample size.

### 3. Multiple Comparisons
If the user has more than 2 variants:

> With [k] variants, you are making [k-1] comparisons. Apply the Bonferroni correction: use alpha = 0.05 / [k-1] = [corrected_alpha] for each comparison. This increases the required sample size per variant.

Recalculate with corrected alpha.

### 4. Multiple Metrics
If the user tracks multiple primary metrics:

> Testing [m] metrics simultaneously inflates the false positive rate. With [m] metrics at alpha=0.05, the probability of at least one false positive is 1 - (1-0.05)^[m] = [family_wise_error]. Either designate one primary metric or apply Bonferroni correction.

### 5. Low Baseline Rates
For conversion rates below 1%:

> With a baseline rate of [X]%, you need very large samples to detect meaningful effects. A 20% relative improvement means detecting a change from [X]% to [X×1.2]% — an absolute difference of only [delta] percentage points. Consider whether this is the right metric to test, or whether a higher-funnel metric would be more practical.

## Output Format

Present results in this format:

```
SAMPLE SIZE CALCULATION
========================
Baseline conversion rate: [p₁]%
Expected variant rate:    [p₂]% ([MDE]% relative lift)
Significance level:       [alpha] (two-tailed)
Statistical power:        [power]

Required sample size:     [n] per variant
Total sample required:    [n × k] across all variants

DURATION ESTIMATE
========================
Daily eligible traffic:   [daily_traffic]
Estimated duration:       [days] days
Recommended run period:   [start] to [end] (full weeks)

SENSITIVITY TABLE
========================
| Relative MDE | Sample/Variant | Total Sample | Duration |
|--------------|----------------|--------------|----------|
| 5%           | [n]            | [n×k]        | [days]   |
| 10%          | [n]            | [n×k]        | [days]   |
| 15%          | [n]            | [n×k]        | [days]   |
| 20%          | [n]            | [n×k]        | [days]   |
| 25%          | [n]            | [n×k]        | [days]   |

WARNINGS
========================
[Any applicable warnings about peeking, duration, or traffic]

NEXT STEP: /abtest design to plan the implementation
```

## Sensitivity Table

Always provide a sensitivity table showing sample sizes for 5 different MDE levels (centered around the user's target). This helps the user make trade-off decisions between precision and speed.

## Python Calculator

For exact calculations, use the script at `scripts/sample_size_calculator.py`:

```bash
python scripts/sample_size_calculator.py --baseline 0.05 --mde 0.20 --alpha 0.05 --power 0.80 --daily-traffic 5000
```

This uses scipy.stats for exact Z-score calculations and produces both the sample size and sensitivity table.

## Quick Reference: Sample Sizes for Common Scenarios

| Baseline Rate | 10% Relative MDE | 20% Relative MDE | 30% Relative MDE |
|---------------|-------------------|-------------------|-------------------|
| 1% | 1,567,980 | 392,154 | 174,393 |
| 3% | 509,508 | 127,508 | 56,706 |
| 5% | 297,444 | 74,468 | 33,138 |
| 10% | 137,620 | 34,476 | 15,356 |
| 20% | 58,408 | 14,652 | 6,528 |
| 50% | 15,688 | 3,936 | 1,756 |

These assume alpha=0.05, power=0.80, two-tailed, per variant. Total sample is 2x for a standard A/B test.
