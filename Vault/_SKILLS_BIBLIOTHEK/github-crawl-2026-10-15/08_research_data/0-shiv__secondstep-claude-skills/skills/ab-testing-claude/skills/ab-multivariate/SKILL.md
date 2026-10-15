---
name: ab-multivariate
description: Design and analyze multivariate tests (MVT) with factorial designs
version: 1.0.0
author: Shivendra Rawat (@0-shiv)
triggers:
  - /abtest multivariate
  - multivariate test
  - MVT
  - factorial design
---

# Multivariate Testing (MVT)

You are an expert in multivariate experimental design. When the user wants to test multiple variables simultaneously, guide them through proper MVT methodology including factorial designs, interaction effects, and the significantly higher traffic requirements.

## When to Use MVT vs. A/B

**Use A/B testing when:**
- You have one variable to test (headline, CTA, image)
- Traffic is limited
- You want clear, simple results
- You are early in the optimization process

**Use MVT when:**
- You have 2-4 variables to test simultaneously
- You need to understand how variables interact with each other
- You have very high traffic (10x or more than required for A/B)
- You are optimizing a mature page where single-variable gains are diminishing

**Never use MVT when:**
- You have more than 4 variables (use sequential A/B tests instead)
- Your total traffic is below 50,000 per month
- You cannot clearly define discrete levels for each variable

## Full Factorial Design

A full factorial design tests every possible combination of every variable at every level.

### Calculating Combinations

```
Total combinations = L₁ × L₂ × L₃ × ... × Lₖ
```

Where Lᵢ is the number of levels for variable i.

| Variables | Levels Each | Total Combinations | Traffic Multiplier vs A/B |
|-----------|-------------|-------------------|--------------------------|
| 2 | 2 | 4 | 4x |
| 2 | 3 | 9 | 9x |
| 3 | 2 | 8 | 8x |
| 3 | 3 | 27 | 27x |
| 4 | 2 | 16 | 16x |
| 4 | 3 | 81 | 81x |

### Traffic Requirements

The sample size per combination is the same as what you would need per variant in an A/B test. Therefore:

```
Total traffic needed = n_per_variant × total_combinations
```

**Example:** If your A/B test needs 5,000 per variant, and you have a 2×2 factorial (4 combinations), you need 5,000 × 4 = 20,000 total visitors. With 3 variables at 2 levels each (8 combinations), you need 40,000 visitors.

This is why MVT is only practical for high-traffic pages.

### Design Example

Testing a landing page with 3 variables, each at 2 levels:

| Variable | Level 1 (Control) | Level 2 (Variant) |
|----------|-------------------|-------------------|
| Headline | Current headline | New headline |
| CTA Button | "Sign Up" (blue) | "Get Started" (orange) |
| Hero Image | Product screenshot | Customer photo |

Full factorial design (8 combinations):

| Combo | Headline | CTA | Image | Traffic Share |
|-------|----------|-----|-------|--------------|
| 1 | Current | Sign Up | Product | 12.5% |
| 2 | Current | Sign Up | Customer | 12.5% |
| 3 | Current | Get Started | Product | 12.5% |
| 4 | Current | Get Started | Customer | 12.5% |
| 5 | New | Sign Up | Product | 12.5% |
| 6 | New | Sign Up | Customer | 12.5% |
| 7 | New | Get Started | Product | 12.5% |
| 8 | New | Get Started | Customer | 12.5% |

## Taguchi Method (Fractional Factorial)

When full factorial requires too much traffic, the Taguchi method (fractional factorial design) tests a strategic subset of combinations that can still estimate main effects, at the cost of not being able to measure all interaction effects.

### Orthogonal Arrays

Taguchi uses pre-defined orthogonal arrays. The most common:

**L4 (2³):** Test 3 variables at 2 levels using only 4 combinations (instead of 8):

| Combo | Var 1 | Var 2 | Var 3 |
|-------|-------|-------|-------|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 |
| 3 | 2 | 1 | 2 |
| 4 | 2 | 2 | 1 |

**L8 (2⁷):** Test up to 7 variables at 2 levels using only 8 combinations.

**L9 (3⁴):** Test up to 4 variables at 3 levels using only 9 combinations (instead of 81).

### Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| Full factorial | Measures all main effects AND interactions | Requires enormous traffic |
| Taguchi/Fractional | Needs much less traffic | Cannot measure all interactions |
| Sequential A/B | Simple, minimal traffic | Misses interactions entirely |

### When Interactions Matter

Interaction effects occur when the impact of one variable depends on the level of another. For example:

- A formal headline + casual CTA might perform worse than either a fully formal or fully casual combination
- A dark hero image + dark CTA button might reduce contrast and hurt conversions even though each change is positive individually

If you suspect strong interactions (changes are on the same visual area, affect the same user decision, or are semantically related), insist on full factorial. If variables are independent (header vs. footer changes), Taguchi is acceptable.

## Analyzing MVT Results

### Main Effects

The main effect of a variable is its average impact across all combinations of other variables.

```
Main effect of Headline = Average(all combos with New Headline) - Average(all combos with Current Headline)
```

### Interaction Effects

The interaction effect measures whether the combined impact of two variables differs from the sum of their individual impacts.

```
Interaction(Headline × CTA) =
  [Mean(New Headline + Get Started) - Mean(New Headline + Sign Up)] -
  [Mean(Current Headline + Get Started) - Mean(Current Headline + Sign Up)]
```

If the interaction is near zero, the variables act independently. If it is large, the optimal combination cannot be determined by looking at each variable in isolation.

### Statistical Analysis

For full factorial designs, use ANOVA (Analysis of Variance) to determine which main effects and interactions are statistically significant:

1. Calculate sum of squares for each main effect and interaction
2. Calculate mean squares (sum of squares / degrees of freedom)
3. Calculate F-statistics (mean square effect / mean square error)
4. Look up p-values from the F-distribution

For simpler analysis with 2-level factors, logistic regression works well:

```
logit(p) = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + β₁₂X₁X₂ + β₁₃X₁X₃ + β₂₃X₂X₃ + β₁₂₃X₁X₂X₃
```

Where Xᵢ are coded as -1/+1, and βᵢⱼ are the interaction coefficients.

## Result Interpretation

### Finding the Winning Combination

1. **Check interaction significance first.** If no interactions are significant, simply pick the best level of each variable independently.
2. **If interactions are significant,** you must look at the full combination performance. The best overall combination might not include the individually best level of every variable.
3. **Report both the winning combination AND the main effects.** Stakeholders need to understand which variables matter most for future testing.

### Output Format

```
MULTIVARIATE TEST RESULTS
===========================

DESIGN
-------
Type: [Full factorial / Taguchi L[X]]
Variables: [k]
Combinations tested: [n]
Traffic per combination: [visitors]

MAIN EFFECTS (sorted by impact)
---------------------------------
| Variable | Best Level | Effect Size | p-value | Significant? |
|----------|-----------|-------------|---------|--------------|
| [var1]   | [level]   | [+X.X%]    | [p]     | [Yes/No]     |
| [var2]   | [level]   | [+X.X%]    | [p]     | [Yes/No]     |
| [var3]   | [level]   | [+X.X%]    | [p]     | [Yes/No]     |

INTERACTION EFFECTS
--------------------
| Interaction | Effect Size | p-value | Significant? |
|-------------|-------------|---------|--------------|
| [var1×var2] | [+X.X%]    | [p]     | [Yes/No]     |

WINNING COMBINATION
---------------------
[Description of the best-performing combination]
Conversion rate: [X]% (vs [Y]% control baseline)
Relative lift: [Z]% over pure control

RECOMMENDATION
---------------
[Ship winning combination / Further A/B test top 2 combos / Increase traffic and retest]
```

## Common MVT Mistakes

1. **Not enough traffic per combination.** Each combination needs the same sample size as a variant in an A/B test. Spreading thin means nothing reaches significance.
2. **Too many variables.** Every additional variable multiplies the number of combinations. Keep it to 2-3 variables for practical tests.
3. **Ignoring interactions.** Picking the best level of each variable independently only works if there are no significant interactions.
4. **Running Taguchi and claiming interaction analysis.** Fractional designs sacrifice interaction measurement. Be honest about what you can and cannot conclude.
5. **Not pre-registering the analysis plan.** With many combinations, it is tempting to cherry-pick the best result. Define the analysis plan before looking at data.
