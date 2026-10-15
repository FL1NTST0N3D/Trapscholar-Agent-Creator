# A/B Testing — Ad Variation Generator & Statistical Testing Framework

## Command: `/copy test`

Generate systematic ad variations for A/B testing, define test hypotheses, calculate statistical significance, and identify winners.

## Required Inputs

- **Current ad copy**: The existing RSA (headlines + descriptions) to test against
- **What to test**: Messaging angle, CTA, offer, emotional tone, or structure
- **Campaign metrics**: Current CTR, conversion rate, impressions (for significance calculations)
- **Test duration preference**: How long the user wants to run the test
- **Budget**: Daily spend for the ad group (affects how fast you reach significance)

## A/B Test Hierarchy

Not all tests are equal. Follow this priority order — test the highest-impact elements first:

| Priority | Element | Expected Impact | Min Test Duration |
|----------|---------|----------------|-------------------|
| 1 | **Value proposition / Offer** | Very High (20-50% lift) | 2-4 weeks |
| 2 | **CTA type** | High (10-30% lift) | 2-3 weeks |
| 3 | **Emotional angle** | High (10-25% lift) | 2-3 weeks |
| 4 | **Headline framework** | Medium (5-15% lift) | 2-4 weeks |
| 5 | **Specific wording** | Low-Medium (3-10% lift) | 3-4 weeks |
| 6 | **Punctuation / formatting** | Low (1-5% lift) | 4+ weeks |

## Variation Generation Framework

### Method 1: Single Variable Testing (Recommended)

Change ONE element between variants to isolate what drives performance.

```
CONTROL RSA:
  H1: "Get 50% Off Premium Widgets"
  H2: "Trusted by 10,000+ Buyers"
  H3: "Free Shipping on All Orders"
  D1: "Premium widgets at half price. Rated 4.9/5 by 10K+ customers. Shop the sale now."

VARIANT A — Testing: CTA change
  H1: "Get 50% Off Premium Widgets" (same)
  H2: "Trusted by 10,000+ Buyers" (same)
  H3: "Free Shipping on All Orders" (same)
  D1: "Premium widgets at half price. Rated 4.9/5 by 10K+ customers. Order yours today."
       (only CTA changed: "Shop the sale now" → "Order yours today")

HYPOTHESIS: "Order yours today" will increase conversion rate because it implies personal ownership.
```

### Method 2: Messaging Angle Testing

Test fundamentally different value propositions to find what resonates.

```
VARIANT A — Price-focused:
  H1: "Save 50% on Premium Widgets"
  H2: "Lowest Prices Guaranteed"
  H3: "Budget-Friendly Quality"
  D1: "Why pay more? Get premium widgets at half the price. Free shipping included. Shop now."

VARIANT B — Quality-focused:
  H1: "Premium Handcrafted Widgets"
  H2: "Built to Last a Lifetime"
  H3: "Award-Winning Craftsmanship"
  D1: "Handcrafted from aircraft-grade aluminum. Each widget inspected 3x. Discover the difference."

HYPOTHESIS: Quality messaging will attract higher-value customers with better ROAS, even if CTR is lower.
```

### Method 3: Emotional Angle Testing

Same product, different emotional triggers.

```
VARIANT A — Fear/Loss Aversion:
  H1: "Stop Wasting Money on Ads"
  H2: "Your Competitors Are Ahead"
  D1: "Every day without optimization costs you leads. Our tool fixes wasted ad spend in minutes."

VARIANT B — Aspiration/Growth:
  H1: "Double Your Ad Performance"
  H2: "Join the Top 10% of Advertisers"
  D1: "Top advertisers use AI to optimize every dollar. Join 5,000+ teams growing faster with us."

HYPOTHESIS: Aspiration messaging will outperform fear for top-of-funnel campaigns because searchers are solution-seeking, not problem-aware.
```

## Statistical Significance Calculator

### Required Data Points
- **Impressions** per variant (minimum 1,000 each)
- **Clicks** per variant
- **Conversions** per variant
- **Confidence level** target (standard: 95%)

### Minimum Sample Size Formula

To detect a meaningful difference, calculate minimum impressions needed:

```
For CTR testing:
  Baseline CTR: [current CTR]
  Minimum detectable effect: [desired improvement, e.g., 20% relative]
  Confidence level: 95%
  Power: 80%

  Approximate formula:
  n = (16 * p * (1-p)) / (MDE)^2

  Where:
    p = baseline CTR (as decimal)
    MDE = minimum detectable effect (absolute, not relative)
    n = impressions needed PER variant
```

### Quick Reference Table

| Baseline CTR | Detect 10% Lift | Detect 20% Lift | Detect 30% Lift |
|-------------|----------------|----------------|----------------|
| 2% | 78,400 per variant | 19,600 | 8,711 |
| 5% | 30,400 | 7,600 | 3,378 |
| 8% | 18,400 | 4,600 | 2,044 |
| 10% | 14,400 | 3,600 | 1,600 |
| 15% | 9,067 | 2,267 | 1,007 |

### Duration Estimate

```
Days needed = (Impressions needed per variant * 2) / Daily impressions
```

Example: Need 7,600 impressions per variant, ad group gets 500 impressions/day:
- Total needed: 15,200
- Days: 15,200 / 500 = ~30 days

## Test Hypothesis Framework

Every test must have a clear hypothesis BEFORE launching:

### Hypothesis Template

```
TEST NAME: [descriptive name]
DATE: [start date]
AD GROUP: [ad group name]

HYPOTHESIS:
"Changing [specific element] from [current version] to [new version]
will [increase/decrease] [metric] by [estimated %]
because [reasoning based on audience behavior or framework]."

CONTROL: [current ad copy]
VARIANT: [new ad copy]

PRIMARY METRIC: [CTR / Conversion Rate / CPA]
SECONDARY METRICS: [list]
GUARDRAIL METRICS: [metrics that should NOT decrease, e.g., conversion rate when testing CTR]

SAMPLE SIZE NEEDED: [calculated]
ESTIMATED DURATION: [days]
STOP CRITERIA: If variant underperforms control by >20% after 50% of sample, pause early.
```

## Winner Identification Criteria

### When to Call a Winner

| Criteria | Threshold |
|----------|-----------|
| Statistical confidence | 95% or higher |
| Minimum sample | At least 100 conversions per variant (for CPA tests) |
| Duration | At least 14 days (to account for day-of-week variation) |
| Consistent direction | Winner has been ahead for at least 7 consecutive days |
| Business impact | Lift is meaningful (>5% relative improvement) |

### When NOT to Call a Winner

- Fewer than 1,000 impressions per variant
- Confidence below 90%
- Results flip-flopped multiple times during the test period
- Major external factor during test (holiday, competitor action, budget change)
- Guardrail metrics declined significantly

### Post-Test Actions

```
WINNER: [Variant A or B]
CONFIDENCE: [X%]
LIFT: [+X% on primary metric]

ACTION:
  1. Pause the losing variant
  2. Apply winning messaging to other ad groups with similar themes
  3. Document what worked and why
  4. Plan the next test (iterate on the winner)

NEXT TEST:
  Based on this result, test [next hypothesis]
```

## Output Format

```
=== A/B TEST PLAN ===

TEST: [name]
HYPOTHESIS: "[hypothesis]"

CONTROL (Current Ad):
  H1-H15: [headlines]
  D1-D4: [descriptions]

VARIANT (Challenger):
  H1-H15: [headlines]
  D1-D4: [descriptions]

CHANGES MADE:
  - H3: Changed from "[old]" to "[new]" (testing: [variable])
  - D1: Changed from "[old]" to "[new]" (testing: [variable])

METRICS:
  Primary: [metric]
  Secondary: [metrics]
  Guardrail: [metrics]

SAMPLE SIZE: [number] per variant
ESTIMATED DURATION: [days]
STOP CRITERIA: [criteria]

--- ADDITIONAL VARIANTS (for sequential testing) ---
VARIANT B: [next test after winner is found]
VARIANT C: [test after that]
```

## Common Testing Mistakes to Avoid

1. **Testing too many variables at once** — isolate one change per test
2. **Calling winners too early** — wait for statistical significance
3. **Ignoring guardrail metrics** — a CTR winner that tanks conversion rate is not a winner
4. **Not documenting learnings** — every test should produce a written insight
5. **Testing trivial changes** — "Shop Now" vs "Shop now" is not worth 3 weeks of data
6. **Running during anomalies** — holidays, outages, or budget changes invalidate results
7. **Not having a next test planned** — testing should be a continuous program
8. **Testing in low-volume ad groups** — you'll never reach significance with 50 impressions/day
