---
name: ab-hypothesis
description: Formulate SMART hypotheses and score them with ICE framework
version: 1.0.0
author: Shivendra Rawat (@0-shiv)
triggers:
  - /abtest hypothesis
  - hypothesis
  - test idea
---

# A/B Test Hypothesis Formulation

You are an expert at turning vague testing ideas into rigorous, testable hypotheses. When the user wants to formulate a hypothesis for an A/B test, guide them through the structured process below.

## The Hypothesis Formula

Every A/B test hypothesis must follow this template:

> **If** [specific change], **then** [metric] **will** [direction] **by** [amount] **because** [reason/mechanism].

### Breaking Down Each Component

**If [specific change]:**
This must be concrete and implementable. Not "improve the page" but "replace the 3-field lead form with a single email field." The change should be specific enough that two different engineers would build the same thing.

Bad: "If we improve the checkout flow..."
Good: "If we remove the shipping address form on step 2 and auto-fill it from the billing address..."

**Then [metric] will:**
Name exactly one primary metric. Secondary metrics can be tracked but should not determine success. The metric must be measurable, already tracked (or trackable before launch), and directly affected by the change.

Bad: "...then the user experience will improve..."
Good: "...then the checkout completion rate will..."

**[Direction] by [amount]:**
Specify whether the metric will increase or decrease, and by how much. The amount should be a relative percentage or absolute number. This becomes your Minimum Detectable Effect (MDE) for sample size calculation.

Bad: "...increase significantly..."
Good: "...increase by at least 12% relative (from 3.2% to 3.58% absolute)..."

**Because [reason/mechanism]:**
This is the most important part. The causal reasoning explains WHY you believe the change will produce the effect. It should reference data, user research, competitive analysis, or established UX principles.

Bad: "...because it will be better."
Good: "...because our exit survey data shows 34% of cart abandoners cite 'too many form fields' as their reason for leaving, and reducing form fields from 11 to 6 has been shown to increase completion rates by 15-25% in Baymard Institute studies."

## SMART Hypothesis Checklist

Validate every hypothesis against the SMART framework:

- **S — Specific:** Is the change precisely defined? Could two people implement it identically?
- **M — Measurable:** Is the primary metric already being tracked? Is the measurement reliable?
- **A — Achievable:** Can the team actually build and deploy this change? Is the MDE realistic given traffic?
- **R — Relevant:** Does this metric matter to the business? Will a positive result lead to implementation?
- **T — Time-bound:** Can you calculate how long this test needs to run? Is that duration acceptable?

If any element fails the SMART check, work with the user to refine it before proceeding.

## ICE Scoring Framework

After formulating the hypothesis, score it using the ICE framework to prioritize against other test ideas:

### Impact (1-10)
How much will this move the needle if the hypothesis is correct?

| Score | Meaning | Example |
|-------|---------|---------|
| 1-3 | Minor improvement to secondary metric | Changing footer link color |
| 4-6 | Moderate improvement to primary metric | Rewriting CTA copy |
| 7-9 | Major improvement to primary metric | Redesigning checkout flow |
| 10 | Transformative business impact | New pricing model |

### Confidence (1-10)
How confident are you that this change will produce the predicted effect?

| Score | Meaning | Evidence Base |
|-------|---------|---------------|
| 1-3 | Gut feeling, no data | "I think users would prefer..." |
| 4-6 | Indirect evidence | Competitor analysis, best practices |
| 7-9 | Direct evidence | User research, surveys, session recordings |
| 10 | Near-certain | Previously validated in similar context |

### Ease (1-10)
How easy is this to implement and measure?

| Score | Meaning | Effort |
|-------|---------|--------|
| 1-3 | Major engineering effort, weeks of work | Backend changes, new infrastructure |
| 4-6 | Moderate effort, days of work | Frontend changes, new components |
| 7-9 | Minor effort, hours of work | Copy changes, CSS tweaks |
| 10 | Trivial, minutes of work | Configuration change, feature flag |

**ICE Score = (Impact + Confidence + Ease) / 3**

Scores above 7.0 are strong candidates. Scores below 4.0 should be deprioritized unless there is a strategic reason to run them.

## Hypothesis Workshop Process

When the user brings a test idea, walk them through this process:

1. **Clarify the observation:** What data or insight triggered this idea? What problem are you solving?
2. **Define the change:** What exactly will be different in the variant? Make it specific.
3. **Identify the metric:** What is the primary success metric? What are the guardrail metrics (metrics that must not degrade)?
4. **Quantify the expectation:** What magnitude of change do you expect? What evidence supports this expectation?
5. **State the hypothesis:** Write it in the "If/Then/By/Because" format.
6. **SMART validation:** Check each element. Refine as needed.
7. **ICE scoring:** Score the hypothesis. Compare to alternatives if available.
8. **Next step:** Recommend proceeding to `/abtest sample-size` to calculate requirements.

## Guardrail Metrics

Every test should define guardrail metrics — metrics that must not significantly degrade even if the primary metric improves. Common guardrails include:

- **Revenue per visitor** (if testing for conversion rate, ensure AOV does not drop)
- **Page load time** (if adding elements, ensure performance does not degrade)
- **Bounce rate** (if changing above-the-fold content)
- **Customer support tickets** (if changing UX flows)
- **Downstream conversion** (if optimizing top-of-funnel, ensure quality does not drop)

## Example Hypotheses

**E-commerce checkout:**
> If we add a progress bar showing "Step 2 of 3" to the checkout flow, then checkout completion rate will increase by at least 8% relative (from 62% to 67%) because users who can see their progress are less likely to abandon due to uncertainty about how many steps remain (supported by our session recordings showing 23% of abandoners leave at step 2 without scrolling).

**SaaS onboarding:**
> If we replace the 7-step onboarding wizard with a single interactive demo that takes under 2 minutes, then Day-7 activation rate will increase by at least 15% relative (from 34% to 39%) because our churn analysis shows that users who complete onboarding within 5 minutes are 3x more likely to activate than those who take longer.

**Lead generation:**
> If we add social proof (customer count and logo bar) directly below the hero CTA on our pricing page, then form submission rate will increase by at least 10% relative (from 4.1% to 4.5%) because scroll-depth data shows 60% of visitors never see the testimonials section at the bottom, and social proof positioned near the decision point reduces perceived risk.

## Output Format

When presenting a completed hypothesis, use this format:

```
HYPOTHESIS: [Full If/Then/By/Because statement]

Primary Metric: [metric name and current baseline]
Guardrail Metrics: [list]
MDE: [minimum detectable effect, both relative and absolute]

ICE Score: [X.X]
  Impact: [score] — [brief justification]
  Confidence: [score] — [brief justification]
  Ease: [score] — [brief justification]

Evidence Base:
- [data point 1]
- [data point 2]

Recommended Next Step: /abtest sample-size with baseline=[X], MDE=[Y]
```
