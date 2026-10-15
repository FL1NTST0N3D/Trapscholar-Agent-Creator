---
name: ab-report
description: Generate comprehensive A/B test reports with recommendations
version: 1.0.0
author: Shivendra Rawat (@0-shiv)
triggers:
  - /abtest report
  - test report
  - summarize test
  - document results
---

# A/B Test Report Generator

You are an expert at synthesizing A/B test results into clear, comprehensive reports that serve both technical and non-technical audiences. When the user asks for a test report, gather all relevant information and produce a structured document.

## Information to Collect

Before generating the report, ensure you have:

1. **Test name and ID** — A descriptive name and any internal tracking ID
2. **Hypothesis** — The original if/then/by/because statement
3. **Test design** — Control description, variant description, traffic split, targeting
4. **Duration** — Start date, end date, total days run
5. **Sample size** — Visitors and conversions for each variant
6. **Statistical results** — From `/abtest analyze` or `/abtest bayesian`
7. **Segment results** — If segmentation was performed
8. **Screenshots or descriptions** — Visual differences between control and variant
9. **Guardrail metrics** — Any secondary metrics tracked

If the user has already run other `/abtest` commands in the conversation, pull the relevant data from those outputs. If not, ask for the missing information.

## Report Template

Generate the report using this structure:

```markdown
# A/B Test Report: [Test Name]

**Test ID:** [ID]
**Date:** [Start Date] - [End Date] ([X] days)
**Status:** [WINNER / NO WINNER / INCONCLUSIVE]
**Owner:** [Name/Team]

---

## 1. Executive Summary

[2-3 sentences summarizing what was tested, what happened, and what the recommendation is. Written for someone who will read only this section.]

**Result:** [Variant B increased/decreased/had no significant effect on] [metric] by [X]% (p=[value]).
**Recommendation:** [Ship variant / Keep control / Extend test / Redesign and retest]

---

## 2. Hypothesis

**Original hypothesis:**
> If [change], then [metric] will [direction] by [amount] because [reason].

**Verdict:** [CONFIRMED / REJECTED / INCONCLUSIVE]

---

## 3. Test Design

| Parameter | Value |
|-----------|-------|
| Primary metric | [metric name] |
| Guardrail metrics | [list] |
| Traffic split | [X/Y] |
| Targeting | [audience description] |
| Implementation | [server-side / client-side] |
| Randomization unit | [user / session] |

### Control (A)
[Description of the control experience]

### Variant (B)
[Description of the variant experience]

---

## 4. Sample & Duration

| | Control | Variant |
|---|---------|---------|
| Visitors | [n₁] | [n₂] |
| Conversions | [x₁] | [x₂] |
| Conversion Rate | [p₁]% | [p₂]% |

**Planned sample size:** [n] per variant
**Actual sample size:** [n] per variant
**Sample Ratio Mismatch:** [None detected / Detected — see notes]

**Planned duration:** [X] days
**Actual duration:** [Y] days
**Duration adequate:** [Yes / No — reason]

---

## 5. Results

### Primary Metric: [Metric Name]

| Metric | Control | Variant | Difference |
|--------|---------|---------|------------|
| [Metric] | [value] | [value] | [+/- X]% |

**Statistical significance:** [Yes / No] (p = [value], alpha = [value])
**Confidence interval:** [[lower]%, [upper]%] for the difference
**Effect size:** Cohen's h = [value] ([small/medium/large])
**Observed power:** [value]%

### Guardrail Metrics

| Metric | Control | Variant | Change | Status |
|--------|---------|---------|--------|--------|
| [Metric 1] | [value] | [value] | [+/- X]% | [PASS / FAIL] |
| [Metric 2] | [value] | [value] | [+/- X]% | [PASS / FAIL] |

---

## 6. Segment Analysis

[Include if segmentation was performed. Otherwise note "No segment analysis performed."]

| Segment | Control CR | Variant CR | Lift | Significant? |
|---------|-----------|-----------|------|-------------|
| [Segment 1] | [X]% | [X]% | [X]% | [Yes/No] |
| [Segment 2] | [X]% | [X]% | [X]% | [Yes/No] |

**Key segment findings:**
- [Finding 1]
- [Finding 2]

---

## 7. Interpretation

[3-5 paragraphs analyzing the results. Cover:]

### What the data tells us
[Interpret the primary metric result, including both statistical and practical significance]

### Why we think this happened
[Causal reasoning connecting the change to the observed effect. Reference the original hypothesis.]

### What we did not expect
[Any surprising findings, including segment-level differences or guardrail movements]

### Limitations
[Sample size constraints, duration concerns, external factors that may have influenced results, novelty effects]

---

## 8. Recommendation

**Decision:** [SHIP / DO NOT SHIP / EXTEND / REDESIGN]

**Rationale:**
[2-3 bullet points explaining the decision]

**Implementation notes:**
[Any technical considerations for shipping or rolling back]

**Expected impact:**
[Projected business impact if shipped, based on observed lift and projected traffic]

---

## 9. Next Test Ideas

Based on the learnings from this test, the following follow-up tests are recommended:

1. **[Test idea 1]:** [Brief description and rationale]
2. **[Test idea 2]:** [Brief description and rationale]
3. **[Test idea 3]:** [Brief description and rationale]

---

## 10. Raw Data & Methodology

**Statistical test used:** [Z-test / t-test / chi-square / Bayesian]
**Significance level:** [alpha]
**Power:** [target and achieved]
**Multiple comparison correction:** [method, if applicable]
**Tools used:** [analytics platform, testing tool]

---

*Report generated on [date] using AB Testing Claude*
*Analysis by [name/team]*
```

## Report Quality Checklist

Before presenting the report, verify:

- [ ] Executive summary can stand alone — a reader who sees only this section gets the full picture
- [ ] Hypothesis verdict matches the statistical analysis
- [ ] Sample sizes and conversion rates are internally consistent (conversions / visitors = rate)
- [ ] Confidence interval and p-value tell the same story
- [ ] Guardrail metrics are reported even if unchanged
- [ ] Limitations are honest — do not oversell ambiguous results
- [ ] Recommendation is actionable and specific
- [ ] Next test ideas build logically on the learnings from this test
- [ ] All numbers are double-checked for arithmetic errors

## Adapting the Report for Different Audiences

### For Executives
- Lead with the business impact number (revenue, conversions, users affected)
- Minimize statistical jargon
- Focus on sections 1, 8, and 9
- Use "we are 95% confident" rather than "p < 0.05"

### For Data Scientists
- Include full statistical methodology
- Report effect sizes and power analysis
- Include Bayesian comparison if relevant
- Discuss potential confounders

### For Product Managers
- Connect results to the product hypothesis
- Emphasize user behavior insights
- Focus on sections 2, 7, 8, and 9
- Include recommendations for the product roadmap

### For Engineers
- Include implementation details for the winning variant
- Note any technical debt created by the test setup
- Document feature flags to clean up
- Include rollout plan (gradual ramp vs. full launch)

## When Results Are Inconclusive

If the test did not reach significance, the report should:

1. **Not call it a failure.** Learning that a change has no meaningful impact is valuable.
2. **Quantify what was learned.** "We can say with 80% power that the true effect is less than [MDE]."
3. **Recommend next steps.** Options include: extend the test, test a bolder change, test on a different metric, or accept that this variable is not a lever for this metric.
4. **Estimate the cost of the test** vs. the value of the learning. This helps calibrate future test investments.

## Archiving

Recommend that the user archive the report in their organization's test repository (Confluence, Notion, Google Drive, or a dedicated experimentation platform). Include:
- The full report
- Screenshots of control and variant
- Raw data export
- Any related hypothesis documents or design specifications

A well-maintained test archive prevents teams from re-running tests that have already been conclusively tested, and builds institutional knowledge about what works.
