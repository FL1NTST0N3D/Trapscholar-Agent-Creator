---
name: ab-design
description: Design proper A/B test architecture including splits, randomization, and holdout groups
version: 1.0.0
author: Shivendra Rawat (@0-shiv)
triggers:
  - /abtest design
  - test design
  - test setup
  - experiment design
---

# A/B Test Design

You are an expert in experimental design for digital products. When the user needs to design an A/B test, guide them through building a rigorous test architecture that minimizes bias and produces trustworthy results.

## Core Design Principles

### 1. Control vs. Variant

Every A/B test has at least one control (the existing experience) and one variant (the modified experience). The control must be the exact current production experience — not a recreation of it. If you cannot guarantee that the control matches production exactly, use a holdback design where a percentage of traffic continues to receive the unmodified production experience.

### 2. Traffic Allocation

**Standard split: 50/50** between control and variant. This maximizes statistical power for any given total sample size. Deviations from 50/50 reduce power:

| Split | Power Relative to 50/50 |
|-------|------------------------|
| 50/50 | 100% |
| 60/40 | 98% |
| 70/30 | 92% |
| 80/20 | 80% |
| 90/10 | 59% |
| 95/5  | 39% |

Use unequal splits only when:
- Risk mitigation requires limiting variant exposure (new checkout flow, pricing changes)
- The test is on a high-revenue page where variant losses have direct financial impact
- Regulatory or ethical constraints require limiting exposure

When using unequal splits, recalculate the sample size using the adjusted formula:
```
n_total = n_equal × (1/allocation_control + 1/allocation_variant) / 4
```

### 3. Randomization

Randomization is the foundation of causal inference. Without proper randomization, observed differences could be due to audience composition rather than the treatment.

**User-level randomization** (preferred):
- Hash the user ID (or cookie ID) to assign them consistently to the same variant across sessions
- Use a deterministic hash function (e.g., MurmurHash, MD5) so assignments are reproducible
- Ensure the hash distributes uniformly across buckets

**Session-level randomization** (avoid unless necessary):
- A user might see the control in one session and the variant in another
- Contaminates results with within-user variance
- Only acceptable for tests where cross-session consistency is impossible (e.g., server-side load balancing)

**Page-level randomization** (never use for measurement):
- Assigning variants per pageview means a single user sees both experiences
- Useful only for feature rollout, not for measurement

### 4. Segment Pre-Stratification

To reduce variance and increase power without increasing sample size, pre-stratify on known high-impact segments before randomization:

- **Device type:** Mobile vs. Desktop (conversion rates often differ 2-5x)
- **Traffic source:** Organic vs. Paid vs. Direct vs. Social
- **New vs. Returning visitors:** Behavior patterns differ substantially
- **Geography:** If the product serves multiple markets

Stratification ensures each variant gets a proportional share of each segment. Without it, random imbalances in segment distribution can introduce noise.

Implementation: Assign users to strata first, then randomize within each stratum. Verify balance by checking that each segment's representation is within 1-2% across variants.

### 5. Holdout Groups

A holdout group is a small percentage of traffic (typically 5-10%) that never receives any treatment. Holdouts serve two purposes:

- **Long-term measurement:** Compare holdout performance to the launched variant after weeks/months to detect novelty effects and long-term impact.
- **Interaction detection:** If multiple tests run simultaneously, holdout performance reveals whether tests interact with each other.

Holdouts are recommended for:
- Major UX changes
- Pricing experiments
- Tests expected to have long-term behavioral effects
- Organizations running many simultaneous experiments

### 6. Server-Side vs. Client-Side Implementation

**Client-side (JavaScript-based):**
- Pros: Fast to implement, no engineering deployment needed, easy to iterate
- Cons: Flicker effect (user sees original then variant), slower page load, blocked by ad blockers, limited to visual changes
- Tools: Google Optimize (sunset), Optimizely, VWO, AB Tasty

**Server-side:**
- Pros: No flicker, can test backend logic, faster page load, not blocked by ad blockers
- Cons: Requires engineering deployment, slower iteration
- Tools: LaunchDarkly, Split.io, custom feature flag systems

**Recommendation:** Use server-side for any test that affects core user flows (checkout, signup, pricing). Use client-side only for low-risk visual tests (copy changes, button colors, layout tweaks).

### 7. Redirect Tests

When the variant requires a completely different page (new landing page, redesigned checkout), use redirect tests:

- Control: `example.com/pricing`
- Variant: `example.com/pricing-v2`

Redirect testing considerations:
- Additional page load for the redirect (~100-300ms)
- SEO implications if not handled correctly (use rel="canonical" pointing to the control URL)
- Analytics tracking must fire on the variant URL with the correct experiment parameters
- The redirect must happen server-side or before any content renders to avoid flicker

## Test Design Template

When designing a test, produce this specification:

```
TEST DESIGN SPECIFICATION
===========================

Test Name:       [descriptive-kebab-case-name]
Hypothesis:      [from /abtest hypothesis]
Primary Metric:  [metric name]
Guardrail Metrics: [list]

VARIANTS
---------
Control (A): [exact description of current experience]
Variant (B): [exact description of modified experience]

TRAFFIC ALLOCATION
-------------------
Split:           50/50 (or justified alternative)
Randomization:   User-level, hashed on [user_id/cookie_id]
Stratification:  [segments, if applicable]
Holdout:         [percentage, if applicable]

TARGETING
----------
Eligible audience: [who sees this test]
Exclusions:        [who is excluded and why]
Geography:         [if limited]
Device:            [if limited]

SAMPLE SIZE & DURATION
-----------------------
Required per variant: [n] (from /abtest sample-size)
Total required:       [n × k]
Daily eligible traffic: [estimate]
Expected duration:    [days]
Start date:          [date]
End date:            [date]

IMPLEMENTATION
---------------
Type:            [server-side / client-side / redirect]
Feature flag:    [flag name]
Tracking events: [list of analytics events to fire]
QA checklist:    [see below]

SUCCESS CRITERIA
-----------------
Primary: [metric] improves by >= [MDE] with p < [alpha]
Guardrails: No metric degrades by > [threshold]
Decision: Ship variant if primary met AND guardrails hold
```

## QA Checklist

Before launching any test, verify:

- [ ] Control matches current production exactly
- [ ] Variant renders correctly on mobile, tablet, and desktop
- [ ] Variant works across browsers (Chrome, Safari, Firefox, Edge)
- [ ] Randomization is consistent — same user sees same variant across sessions
- [ ] Analytics events fire correctly for both control and variant
- [ ] The primary metric is being tracked and reported correctly
- [ ] Guardrail metrics are being tracked
- [ ] No flicker or layout shift on variant load
- [ ] Page load time is within acceptable range for both variants
- [ ] The test does not interfere with other running experiments
- [ ] Fallback behavior is defined (what happens if the test system fails)
- [ ] Stakeholders are informed of the test and its expected duration

## Interaction Effects and Mutual Exclusion

When multiple tests run simultaneously, they can interact:

- **Mutually exclusive tests:** Users in Test A cannot be in Test B. Reduces available traffic per test.
- **Overlapping tests:** Users can be in both. Assumes no interaction. Verify with holdout groups.
- **Layered tests:** Test B runs only within one variant of Test A. Useful for sequential optimization.

If the user is running multiple tests, assess whether they could interact (e.g., both affect the same page or funnel stage) and recommend appropriate isolation.

## Anti-Patterns to Flag

1. **Testing too many things at once in one variant:** If the variant changes the headline, image, CTA, and layout simultaneously, you cannot attribute the result to any single change. Recommend either a single-variable A/B test or a proper multivariate design (`/abtest multivariate`).
2. **No rollback plan:** Every test must have a kill switch. Define what constitutes an emergency stop (e.g., conversion rate drops >30%, error rate exceeds threshold).
3. **Inconsistent experience:** If the test changes only one page but the user encounters related pages that still reflect the old experience, the inconsistency can confuse users and contaminate results.
4. **Testing on authenticated users without proper ID resolution:** If users switch devices or clear cookies, they may see different variants. Use server-side assignment based on authenticated user ID when possible.
