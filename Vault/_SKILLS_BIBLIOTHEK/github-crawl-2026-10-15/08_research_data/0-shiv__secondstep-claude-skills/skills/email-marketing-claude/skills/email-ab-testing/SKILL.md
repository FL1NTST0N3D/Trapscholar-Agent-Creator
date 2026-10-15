# Email A/B Testing — Sub-Skill

## Overview

A/B testing is the scientific method applied to email marketing. Without it, you're guessing. This sub-skill provides a framework for what to test, how to calculate sample sizes, how to determine statistical significance, and how to implement winners.

**Command:** `/email test`

---

## A/B Testing Audit Checklist

- [ ] A/B tests are run regularly (at least 2x/month)
- [ ] Only one variable is tested at a time
- [ ] Sample sizes are statistically valid
- [ ] Tests run long enough for significance (95% confidence)
- [ ] Winners are documented and applied to future sends
- [ ] Results are shared with the team
- [ ] Testing roadmap exists (not ad hoc)
- [ ] Both opens AND clicks are measured as success metrics
- [ ] Test results feed back into templates and sequences

---

## What to Test (Priority Order)

### High Impact — Test First

| Element | Variations | Expected Lift |
|---------|-----------|---------------|
| Subject Line | Different hooks, lengths, personalization | 10-30% open rate lift |
| Send Time | Morning vs afternoon, weekday vs weekend | 5-20% open rate lift |
| Sender Name | Brand name vs personal name vs combo | 10-25% open rate lift |
| CTA Button | Text, color, size, placement | 10-40% click rate lift |
| Offer/Incentive | 10% off vs free shipping vs $10 off | 15-50% conversion lift |

### Medium Impact

| Element | Variations | Expected Lift |
|---------|-----------|---------------|
| Email Length | Short (100 words) vs long (500+ words) | 5-15% click rate |
| Image vs No Image | Hero image vs text-only | 5-20% click rate |
| Personalization | With name vs without, dynamic content | 5-15% open/click rate |
| Preview Text | Different preheaders | 5-10% open rate |
| Number of CTAs | Single vs multiple | 5-15% click rate |

### Low Impact (But Worth Testing)

| Element | Variations | Expected Lift |
|---------|-----------|---------------|
| Font Size | 14px vs 16px body text | 2-5% click rate |
| Button Shape | Rounded vs square | 1-5% click rate |
| Social Proof | With testimonial vs without | 3-8% conversion |
| P.S. Line | With vs without | 2-5% click rate |
| Emoji in Subject | With vs without | Variable |

---

## Sample Size Calculator

To run a valid A/B test, you need enough subscribers in each variant to reach statistical significance.

### Formula

```
Required Sample Size per Variant =
  (Z-score^2 x p x (1-p)) / E^2

Where:
  Z-score = 1.96 (for 95% confidence)
  p = baseline conversion rate (as decimal)
  E = minimum detectable effect (as decimal)
```

### Quick Reference Table

| Baseline Rate | Min Detectable Effect | Sample Size per Variant | Total Sample Needed |
|--------------|----------------------|------------------------|-------------------|
| 20% open rate | 10% relative (2% absolute) | 1,537 | 3,074 |
| 20% open rate | 20% relative (4% absolute) | 385 | 770 |
| 20% open rate | 30% relative (6% absolute) | 171 | 342 |
| 3% click rate | 10% relative (0.3% absolute) | 39,444 | 78,888 |
| 3% click rate | 20% relative (0.6% absolute) | 9,861 | 19,722 |
| 3% click rate | 30% relative (0.9% absolute) | 4,383 | 8,766 |
| 1% conversion | 20% relative (0.2% absolute) | 95,512 | 191,024 |
| 1% conversion | 50% relative (0.5% absolute) | 15,074 | 30,148 |

### Practical Guidance

| List Size | What You Can Test | Recommended Approach |
|-----------|------------------|---------------------|
| <1,000 | Subject lines only | Test 25% of list (250 per variant), send winner to rest |
| 1,000-5,000 | Subject lines, send time | Test 30% of list, send winner to 70% |
| 5,000-25,000 | Subject, time, CTA, content | Test 15-20% of list |
| 25,000-100,000 | All elements | Test 10% of list, high confidence |
| 100,000+ | Multivariate possible | Test 5% of list, rapid iteration |

---

## Statistical Significance

### The 95% Confidence Rule

A result is statistically significant when you can be 95% confident that the difference between variants is real (not due to random chance).

**What this means:** There is a 5% or less probability that the observed difference happened by chance.

### How to Calculate

```
Z = (p1 - p2) / sqrt(p_pooled x (1 - p_pooled) x (1/n1 + 1/n2))

Where:
  p1 = conversion rate of Variant A
  p2 = conversion rate of Variant B
  p_pooled = (conversions_A + conversions_B) / (n1 + n2)
  n1, n2 = sample sizes

If Z > 1.96 (or Z < -1.96), the result is significant at 95% confidence.
```

### Common Mistakes

| Mistake | Why It's Bad | Fix |
|---------|-------------|-----|
| Ending test too early | Results haven't stabilized | Wait for full sample size |
| Testing too many variables | Can't attribute causation | One variable at a time |
| Ignoring confidence level | Implementing random noise | Require 95% confidence |
| Small sample sizes | High error rate | Use calculator above |
| Not documenting results | Repeating failed tests | Maintain a test log |
| Calling winner on opens only | Clicks/conversions matter more | Measure downstream |
| Testing on unrepresentative sample | Winner may not generalize | Randomize properly |

---

## Test Duration Recommendations

| Send Frequency | Minimum Test Duration | Reason |
|---------------|----------------------|--------|
| Daily sends | 3-7 days | Account for day-of-week effects |
| 3x/week | 1-2 weeks | Need enough data points |
| Weekly | 2-4 weeks | Minimum 2 full cycles |
| Bi-weekly | 4-6 weeks | Need 3+ data points minimum |
| Monthly | Not ideal for A/B | Consider multivariate or sequential |

**Rule of thumb:** Let a test run for at least 2 full send cycles, or until you hit required sample size, whichever is longer.

---

## Winner Criteria

### Primary Metrics (Choose One)

| Goal | Primary Metric | When to Use |
|------|---------------|-------------|
| Awareness | Open Rate | Newsletter, content emails |
| Engagement | Click-Through Rate | Most emails |
| Conversion | Conversion Rate | Sales, signups, downloads |
| Revenue | Revenue Per Email | E-commerce, offers |

### Decision Framework

```
1. Did both variants reach minimum sample size?
   → No: Keep running the test
   → Yes: Continue to step 2

2. Is the difference statistically significant (95% confidence)?
   → No: No winner. Consider testing a bigger difference.
   → Yes: Continue to step 3

3. Is the winning variant better on secondary metrics too?
   → Yes: Clear winner. Implement.
   → No: Evaluate trade-offs. The variant with better
     downstream metrics (clicks > opens, conversions > clicks)
     usually wins.
```

---

## Testing Roadmap Template

### Month 1: Foundations
- Week 1-2: Subject line formula test (question vs statement)
- Week 3-4: Send time test (morning vs afternoon)

### Month 2: Content
- Week 1-2: Sender name test (brand vs personal)
- Week 3-4: CTA button text test (action verb vs benefit)

### Month 3: Optimization
- Week 1-2: Email length test (short vs long)
- Week 3-4: Personalization test (with vs without first name)

---

## A/B Testing Score

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Tests run regularly (2+/month) | 25% | 0-100 |
| Single variable per test | 20% | 0 or 100 |
| Statistical significance measured | 25% | 0 or 100 |
| Results documented | 15% | 0 or 100 |
| Winners implemented | 15% | 0 or 100 |
