# Email Report — Sub-Skill

## Overview

The Email Report sub-skill generates a comprehensive audit report combining scores from all other sub-skills into an actionable document. It includes the Email Health Score, dimension breakdowns, priority fixes, and a 30-60-90 day action plan.

**Command:** `/email report`

---

## Report Generation Process

1. Collect scores from all 10 dimensions (run other sub-skills first or use provided data)
2. Calculate the weighted Email Health Score
3. Identify top 5 priority fixes
4. Generate 30-60-90 day action plan
5. Format into a structured report

---

## Report Template

### Header Section

```
====================================================
         EMAIL MARKETING AUDIT REPORT
====================================================
Client:        [Client/Brand Name]
Industry:      [Industry Vertical]
ESP/Platform:  [Mailchimp/Klaviyo/HubSpot/etc.]
List Size:     [Number of subscribers]
Monthly Volume:[Number of emails sent per month]
Audit Date:    [Date]
Auditor:       Claude Code — Email Marketing Skill
====================================================
```

### Email Health Score

```
OVERALL EMAIL HEALTH SCORE: [XX] / 100  [Grade: X]

Score Breakdown:
┌──────────────────┬────────┬────────┬──────────────┐
│ Dimension        │ Weight │ Score  │ Weighted     │
├──────────────────┼────────┼────────┼──────────────┤
│ Deliverability   │ 20%    │ XX/100 │ XX.X         │
│ Subject Lines    │ 10%    │ XX/100 │ XX.X         │
│ Sequences        │ 15%    │ XX/100 │ XX.X         │
│ Segmentation     │ 10%    │ XX/100 │ XX.X         │
│ A/B Testing      │  5%    │ XX/100 │ XX.X         │
│ Templates        │ 10%    │ XX/100 │ XX.X         │
│ Automation       │ 10%    │ XX/100 │ XX.X         │
│ Analytics        │  5%    │ XX/100 │ XX.X         │
│ Compliance       │ 10%    │ XX/100 │ XX.X         │
│ List Health      │  5%    │ XX/100 │ XX.X         │
├──────────────────┼────────┼────────┼──────────────┤
│ TOTAL            │ 100%   │        │ XX.X / 100   │
└──────────────────┴────────┴────────┴──────────────┘
```

### Score Interpretation

| Score Range | Grade | Meaning |
|------------|-------|---------|
| 90-100 | A+ | Elite — top 5% of email programs |
| 80-89 | A | Excellent — minor optimizations only |
| 70-79 | B | Strong — a few areas need attention |
| 60-69 | C | Average — significant revenue left on the table |
| 50-59 | D | Below average — multiple areas need work |
| 40-49 | F | Poor — major overhaul required |
| 0-39 | Critical | Emails are likely hurting your brand |

---

### Performance vs Benchmarks

```
METRICS vs INDUSTRY BENCHMARKS ([Industry])

┌──────────────┬──────────┬──────────────┬────────────┐
│ Metric       │ Yours    │ Benchmark    │ Status     │
├──────────────┼──────────┼──────────────┼────────────┤
│ Open Rate    │ XX.XX%   │ XX.XX%       │ [Above/Below] │
│ Click Rate   │ XX.XX%   │ XX.XX%       │ [Above/Below] │
│ CTOR         │ XX.XX%   │ XX.XX%       │ [Above/Below] │
│ Bounce Rate  │ XX.XX%   │ XX.XX%       │ [Above/Below] │
│ Unsub Rate   │ XX.XX%   │ XX.XX%       │ [Above/Below] │
│ Spam Rate    │ XX.XX%   │ <0.10%       │ [Above/Below] │
└──────────────┴──────────┴──────────────┴────────────┘
```

---

### Deliverability Summary

```
DELIVERABILITY: [Score]/100

Authentication:
  SPF:   [PASS/FAIL] — [details]
  DKIM:  [PASS/FAIL] — [details]
  DMARC: [PASS/FAIL] — [policy: none/quarantine/reject]

Reputation:
  Sender Score:  [XX/100]
  Blacklists:    [Clean / Listed on X]
  Bounce Rate:   [XX.XX%] — [status]
  Spam Complaints: [XX.XX%] — [status]

Key Findings:
  1. [Finding]
  2. [Finding]
  3. [Finding]
```

---

### Sequence Analysis

```
SEQUENCES: [Score]/100

┌──────────────────┬────────┬────────┬──────────────────────┐
│ Sequence         │ Exists │ Emails │ Status               │
├──────────────────┼────────┼────────┼──────────────────────┤
│ Welcome          │ Y/N    │ X      │ [Good/Needs work]    │
│ Nurture          │ Y/N    │ X      │ [Good/Needs work]    │
│ Abandoned Cart   │ Y/N    │ X      │ [Good/Needs work/NA] │
│ Win-Back         │ Y/N    │ X      │ [Good/Needs work]    │
│ Onboarding       │ Y/N    │ X      │ [Good/Needs work]    │
│ Post-Purchase    │ Y/N    │ X      │ [Good/Needs work]    │
└──────────────────┴────────┴────────┴──────────────────────┘

Key Findings:
  1. [Finding]
  2. [Finding]
```

---

### Segmentation Assessment

```
SEGMENTATION: [Score]/100

Current Segments: [List segments found]
Segment Depth:    [Basic/Intermediate/Advanced]
Dynamic Segments: [Yes/No]
RFM Model:        [Implemented/Not implemented]
Engagement Score:  [Implemented/Not implemented]
Lifecycle Stages:  [Mapped/Not mapped]

Key Findings:
  1. [Finding]
  2. [Finding]
```

---

### Top 5 Priority Fixes

```
PRIORITY FIXES (Ordered by Impact)

1. [CRITICAL] [Fix description]
   Impact: [Expected improvement]
   Effort: [Low/Medium/High]
   Timeline: [Immediate/This week/This month]

2. [HIGH] [Fix description]
   Impact: [Expected improvement]
   Effort: [Low/Medium/High]
   Timeline: [This week/This month]

3. [HIGH] [Fix description]
   Impact: [Expected improvement]
   Effort: [Low/Medium/High]
   Timeline: [This week/This month]

4. [MEDIUM] [Fix description]
   Impact: [Expected improvement]
   Effort: [Low/Medium/High]
   Timeline: [This month/Next month]

5. [MEDIUM] [Fix description]
   Impact: [Expected improvement]
   Effort: [Low/Medium/High]
   Timeline: [This month/Next month]
```

---

### Revenue Impact Estimate

```
ESTIMATED REVENUE IMPACT

Current State:
  List Size:        [X] subscribers
  Monthly Sends:    [X] emails
  Open Rate:        [X]%
  Click Rate:       [X]%
  Conversion Rate:  [X]%
  Avg Order Value:  $[X]

Projected After Fixes:
  Open Rate:        [X]% (+[X]% improvement)
  Click Rate:       [X]% (+[X]% improvement)
  Conversion Rate:  [X]% (+[X]% improvement)

  Estimated Additional Monthly Revenue: $[X]
  Estimated Additional Annual Revenue:  $[X]
```

---

### 30-60-90 Day Action Plan

```
30-60-90 DAY ACTION PLAN

DAYS 1-30: Foundation
□ [Action item 1 — typically deliverability fixes]
□ [Action item 2 — typically compliance fixes]
□ [Action item 3 — typically quick wins]
□ [Action item 4]
□ [Action item 5]

DAYS 31-60: Optimization
□ [Action item 6 — typically sequence improvements]
□ [Action item 7 — typically segmentation setup]
□ [Action item 8 — typically template improvements]
□ [Action item 9]
□ [Action item 10]

DAYS 61-90: Growth
□ [Action item 11 — typically A/B testing program]
□ [Action item 12 — typically advanced automation]
□ [Action item 13 — typically analytics maturation]
□ [Action item 14]
□ [Action item 15]
```

---

### Appendix

The report appendix should include:
- Full authentication record details
- Blacklist check results
- Subject line analysis for last 10 sends
- Sequence flow diagrams
- Segment definitions and sizes
- Template rendering screenshots (if available)
- Compliance checklist with pass/fail for each item

---

## Report Scoring

The report sub-skill itself is scored on completeness:

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| All 10 dimensions scored | 30% | 0-100 |
| Benchmarks compared | 15% | 0 or 100 |
| Priority fixes identified | 20% | 0-100 |
| Revenue impact estimated | 15% | 0 or 100 |
| 30-60-90 plan created | 20% | 0 or 100 |
