# A/B Test Plan

## Test Name: [DESCRIPTIVE NAME]
## Campaign: [CAMPAIGN]
## Ad Group: [AD GROUP]
## Start Date: [DATE]
## Owner: [NAME]

---

## Hypothesis

"Changing [specific element] from [current version] to [new version]
will [increase/decrease] [metric] by [estimated %]
because [reasoning]."

---

## Variants

### Control (Current Ad)

**Headlines:**
| # | Headline | Chars |
|---|----------|-------|
| H1 | | /30 |
[All headlines]

**Descriptions:**
| # | Description | Chars |
|---|-------------|-------|
| D1 | | /90 |
[All descriptions]

### Challenger (Test Variant)

**Headlines:**
| # | Headline | Chars | Changed? |
|---|----------|-------|----------|
| H1 | | /30 | |
[All headlines]

**Descriptions:**
| # | Description | Chars | Changed? |
|---|-------------|-------|----------|
| D1 | | /90 | |
[All descriptions]

---

## Changes Summary

| Element | Control | Challenger | Variable Being Tested |
|---------|---------|------------|----------------------|
| | | | |

---

## Metrics

| Metric | Type | Target |
|--------|------|--------|
| [CTR / CVR / CPA] | Primary | +X% improvement |
| [Secondary metric] | Secondary | No decline |
| [Guardrail metric] | Guardrail | Must not decrease >5% |

---

## Sample Size & Duration

- **Baseline CTR:** X%
- **Minimum detectable effect:** X%
- **Confidence level:** 95%
- **Impressions needed per variant:** [calculated]
- **Daily impressions (estimated):** [number]
- **Estimated test duration:** [X days]

---

## Stop Criteria

- Pause challenger if it underperforms by >20% after 50% sample reached
- Pause if conversion rate drops below [minimum acceptable]
- Do NOT stop early for positive results unless 95% confidence reached

---

## Results (Fill After Test)

| Metric | Control | Challenger | Lift | Confidence |
|--------|---------|------------|------|------------|
| | | | | |

**Winner:** [Control / Challenger]
**Decision:** [Implement / Iterate / Inconclusive]

---

## Learnings

[What did we learn? What do we test next?]

## Next Test

[Hypothesis for the follow-up test based on these results]
