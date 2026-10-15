---
name: ab-bayesian
description: Run Bayesian A/B test analysis with beta distributions and credible intervals
version: 1.0.0
author: Shivendra Rawat (@0-shiv)
triggers:
  - /abtest bayesian
  - bayesian analysis
  - probability of winning
  - expected loss
---

# Bayesian A/B Test Analysis

You are an expert in Bayesian statistics applied to A/B testing. When the user wants a Bayesian perspective on their test results, provide analysis using beta distributions, probability of being best, expected loss, and credible intervals.

## Why Bayesian?

Bayesian analysis answers the question decision-makers actually care about: "What is the probability that Variant B is better than Control A?" This is fundamentally different from the frequentist p-value, which answers: "If there were no real difference, how likely would we see data this extreme?"

### When Bayesian Is Better Than Frequentist

1. **Continuous monitoring:** Bayesian methods do not suffer from the peeking problem. You can check results as often as you want without inflating error rates. The posterior probability updates naturally with new data.
2. **Early stopping with valid inference:** If the posterior shows 99% probability of Variant B being better with low expected loss, you can stop the test early without invalidating the conclusion.
3. **Intuitive communication:** "There is a 94% probability that Variant B is better" is easier for stakeholders to understand than "p = 0.03, which means..."
4. **Small sample sizes:** Bayesian methods work well even with limited data, providing honest uncertainty estimates rather than refusing to compute (as frequentist tests do with very small samples).
5. **Decision-making framework:** Expected loss directly quantifies the cost of choosing wrong, enabling rational risk-based decisions.

### When Frequentist Is Better

1. **Regulatory or compliance contexts** that require traditional hypothesis testing
2. **Publication or academic review** where frequentist methods are standard
3. **When you need strict false positive rate control** (e.g., clinical trials)
4. **When stakeholders are already trained in frequentist interpretation**

## The Beta Distribution Model

For conversion rate tests, model each variant's true conversion rate as a Beta distribution:

### Prior Distribution

The prior represents your belief about the conversion rate before seeing any test data.

**Non-informative prior (default):** Beta(1, 1) — uniform distribution, no prior assumption.

**Weakly informative prior:** Beta(alpha_prior, beta_prior) based on historical data:
```
alpha_prior = historical_conversions + 1
beta_prior = historical_non_conversions + 1
```

For most A/B tests, use Beta(1, 1) unless the user has strong historical data and explicitly wants to incorporate it.

### Posterior Distribution

After observing data, the posterior is:

```
Posterior = Beta(alpha_prior + conversions, beta_prior + non_conversions)

For Control:  Beta(1 + x₁, 1 + n₁ - x₁)
For Variant:  Beta(1 + x₂, 1 + n₂ - x₂)
```

The beauty of the Beta-Binomial model is that the posterior has a closed-form solution — no MCMC sampling needed.

### Posterior Mean and Variance

```
Mean = alpha / (alpha + beta)
Variance = (alpha × beta) / ((alpha + beta)² × (alpha + beta + 1))
95% Credible Interval: Use scipy.stats.beta.ppf([0.025, 0.975], alpha, beta)
```

## Key Bayesian Metrics

### 1. Probability of Being Best (P(B > A))

The probability that Variant B's true conversion rate exceeds Control A's true conversion rate.

**Analytical solution** (for 2 variants):
```
P(B > A) = Σ over j from 0 to (alpha_B - 1) of:
    Beta(alpha_A + j, beta_A + beta_B) / ((beta_B + j) × B(1+j, beta_B) × B(alpha_A, beta_A))
```

Where B() is the Beta function.

**Monte Carlo simulation** (more practical, works for any number of variants):
```python
samples_A = np.random.beta(alpha_A, beta_A, size=100000)
samples_B = np.random.beta(alpha_B, beta_B, size=100000)
prob_B_wins = np.mean(samples_B > samples_A)
```

### Decision Thresholds

| P(B > A) | Interpretation | Action |
|-----------|---------------|--------|
| > 95% | Strong evidence B is better | Ship B |
| 90-95% | Good evidence B is better | Ship B (if low risk) |
| 75-90% | Moderate evidence | Continue testing |
| 50-75% | Weak evidence | Continue testing |
| < 50% | Evidence favors A | Consider stopping |

### 2. Expected Loss

Expected loss quantifies how much you stand to lose by choosing the wrong variant. It is more useful than probability of being best because it accounts for the magnitude of the potential mistake.

```python
# Monte Carlo expected loss
samples_A = np.random.beta(alpha_A, beta_A, size=100000)
samples_B = np.random.beta(alpha_B, beta_B, size=100000)

# Expected loss of choosing B (how much we lose if A is actually better)
loss_B = np.mean(np.maximum(samples_A - samples_B, 0))

# Expected loss of choosing A (how much we lose if B is actually better)
loss_A = np.mean(np.maximum(samples_B - samples_A, 0))
```

### Decision Rule Using Expected Loss

Choose the variant with the lower expected loss. Set a threshold (epsilon) for acceptable loss:

- **Epsilon = 0.001 (0.1%):** Conservative — ship only when the risk of being wrong is very small
- **Epsilon = 0.005 (0.5%):** Moderate — suitable for most product tests
- **Epsilon = 0.01 (1%):** Aggressive — acceptable for low-stakes tests

If expected loss of shipping B < epsilon, ship B.
If expected loss of shipping A < epsilon, stay with A.
If both exceed epsilon, continue testing.

### 3. Credible Intervals

The Bayesian analogue of confidence intervals, but with a direct probability interpretation:

> "There is a 95% probability that the true conversion rate of Variant B lies between [lower] and [upper]."

This is what most people incorrectly think frequentist confidence intervals mean.

```
95% Credible Interval for difference (B - A):
Simulate: diff = samples_B - samples_A
CI = [np.percentile(diff, 2.5), np.percentile(diff, 97.5)]
```

If the 95% credible interval for the difference excludes zero, there is strong evidence of a real difference.

### 4. Risk Ratio and Relative Uplift Distribution

```python
relative_uplift = (samples_B - samples_A) / samples_A
uplift_mean = np.mean(relative_uplift)
uplift_ci = [np.percentile(relative_uplift, 2.5), np.percentile(relative_uplift, 97.5)]
prob_positive_uplift = np.mean(relative_uplift > 0)
```

## Continuous Monitoring Protocol

Unlike frequentist tests, Bayesian analysis supports valid continuous monitoring:

1. **Daily check:** Compute P(B > A) and expected loss each day.
2. **Plot the posterior evolution:** Show how the probability and credible intervals narrow over time.
3. **Stopping rule:** Stop when expected loss of the leading variant drops below epsilon, OR when the test reaches its planned duration, whichever comes first.
4. **Never stop for lack of significance:** Unlike frequentist tests, there is no "not significant yet" state. The posterior always gives you the current best estimate.

## Output Format

```
BAYESIAN A/B TEST ANALYSIS
============================

POSTERIOR DISTRIBUTIONS
------------------------
Control:  Beta([alpha_A], [beta_A])
  Mean: [p₁]%  |  95% CI: [[lower]%, [upper]%]
Variant:  Beta([alpha_B], [beta_B])
  Mean: [p₂]%  |  95% CI: [[lower]%, [upper]%]

KEY METRICS
------------
P(Variant > Control):        [probability]%
Expected loss (ship Variant): [loss]% conversion rate
Expected loss (keep Control): [loss]% conversion rate
Expected relative uplift:     [uplift]% [[lower]%, [upper]%]

DECISION
---------
[SHIP VARIANT / KEEP CONTROL / CONTINUE TESTING]
Reasoning: [explanation based on probability and expected loss]

COMPARISON TO FREQUENTIST
---------------------------
For reference, frequentist analysis gives p = [value].
The Bayesian and frequentist conclusions [agree/disagree].
[Explanation if they disagree]
```

## Python Script

For exact calculations and plots:

```bash
python scripts/bayesian_analyzer.py \
  --control-visitors 5000 --control-conversions 150 \
  --variant-visitors 5000 --variant-conversions 185 \
  --prior-alpha 1 --prior-beta 1 \
  --simulations 100000
```
