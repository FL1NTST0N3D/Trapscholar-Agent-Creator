---
name: bid-report
description: Generate a comprehensive bidding audit report combining strategy recommendations, learning phase status, target adjustment plans, auction position summary, and prioritized action items with implementation timeline.
allowed-tools:
  - Bash
  - Read
  - Write
  - Grep
---

# Bidding Audit Report Generator

You are generating a comprehensive Smart Bidding audit report. This report synthesizes findings from all bidding analysis dimensions into a single deliverable that can be shared with clients, stakeholders, or used as an internal optimization plan. The report should be actionable, data-driven, and prioritized.

## Report Structure

### Section 1: Executive Summary

Write a 3-5 sentence overview that covers:
- Account-level bidding health (Bidding Health Score 0-100)
- Number of campaigns analyzed and key finding categories
- Most impactful opportunity identified
- Estimated performance improvement potential

**Tone**: Professional, direct, no jargon. A non-PPC executive should understand the summary.

**Example:**
> "This account scores 62/100 on Bidding Health. Of 12 active campaigns, 4 are using suboptimal bid strategies and 3 have miscalibrated targets that are limiting conversion volume by an estimated 25-35%. The most impactful change is raising the tCPA target on the non-brand Search campaign from $35 to $48, which should recover approximately 40 conversions per month currently being lost to aggressive bidding. Total estimated improvement: 15-25% more conversions at similar or better efficiency."

### Section 2: Bidding Health Score

Present the score with dimension breakdown:

```
BIDDING HEALTH SCORE: XX/100

Dimension Breakdown:
├── Strategy Fit:       XX/100 (25% weight) = XX points
├── Target Accuracy:    XX/100 (20% weight) = XX points
├── Learning Stability: XX/100 (20% weight) = XX points
├── Conversion Volume:  XX/100 (15% weight) = XX points
├── Auction Position:   XX/100 (10% weight) = XX points
└── Adjustment Hygiene: XX/100 (10% weight) = XX points

Score Interpretation: [Elite / Healthy / Needs Work / Critical / Emergency]
```

For each dimension, provide a 1-2 sentence explanation of why it received its score.

### Section 3: Strategy Assessment

For each campaign, present:

| Campaign | Type | Current Strategy | Recommended Strategy | Fit Score | Issue |
|----------|------|-----------------|---------------------|-----------|-------|
| Brand Search | Search | tCPA ($15) | Target Imp Share (90%) | 60 | Brand should prioritize visibility |
| Non-Brand Search | Search | Max Conv | tCPA ($48) | 45 | Ready to graduate — 52 conv/month |
| Shopping - All | Shopping | tROAS (400%) | tROAS (320%) | 70 | Target too aggressive, losing volume |
| PMax - Prospecting | PMax | Max Conv Value | tROAS (280%) | 50 | Ready — 68 conv with value/month |

**Strategy Mismatch Summary:**
- Campaigns on optimal strategy: X
- Campaigns needing strategy change: X
- Campaigns needing target adjustment: X
- Campaigns needing more data before changing: X

### Section 4: Target Analysis

For campaigns with tCPA or tROAS targets:

| Campaign | Target | Actual (30d) | Ratio | Assessment | Recommended Target |
|----------|--------|-------------|-------|------------|-------------------|
| Non-Brand Search | $35 tCPA | $52 | 0.67 | TOO AGGRESSIVE | $48 |
| Shopping | 400% tROAS | 310% | 1.29 | TOO AGGRESSIVE | 320% |
| Display Retargeting | $25 tCPA | $22 | 1.14 | OPTIMAL | No change |

**Target Ratcheting Plans:**
For each campaign needing target adjustment, provide a week-by-week plan:

```
Campaign: Non-Brand Search
Current Target: $35 → Recommended: $48

Week 0 (now):   Raise target to $48 (+37% — larger jump justified
                because current target is severely limiting volume)
Week 2:         Evaluate. If CPA stabilizes at $45-50, hold.
Week 4:         If CPA < $48 for 2 weeks, lower to $44 (-8%)
Week 6:         If CPA < $44 for 2 weeks, lower to $41 (-7%)
Week 8:         Evaluate final state. Target ~$40-42 is realistic goal.
```

### Section 5: Learning Phase Status

| Campaign | Status | Days in Learning | Trigger | Est. Exit | Action |
|----------|--------|-----------------|---------|-----------|--------|
| Non-Brand Search | Learning | 8 days | Target change | ~6 more days | Wait |
| Display Prospecting | Stuck | 22 days | Conv action change | Unknown | Intervene |
| Shopping - All | Eligible | N/A | N/A | N/A | None |

**Learning Phase Cost:**
- Total estimated cost of active learning phases: $X
- Campaigns stuck in learning (>14 days): X
- Recommended interventions: [list]

### Section 6: Auction Position Summary

| Campaign | Impr Share | Lost (Budget) | Lost (Rank) | Top of Page | Abs Top | Position |
|----------|-----------|---------------|-------------|-------------|---------|----------|
| Brand Search | 92% | 3% | 5% | 88% | 72% | Dominant |
| Non-Brand Search | 34% | 8% | 58% | 41% | 18% | Weak |
| Shopping | 48% | 22% | 30% | N/A | N/A | Moderate |

**Competitive Threats:**
- Top competitor: [domain] — [overlap rate]% overlap, outranks you [X]% of the time
- Emerging competitor: [domain] — appeared in last 30 days, [IS]% impression share
- Declining competitor: [domain] — IS dropped [X]% month-over-month

**Positioning Map:**
```
                High IS
                  |
    Expensive ----+---- Efficient
    Winner        |     Winner
                  |
         High CPA + Low CPA
                  |
    Expensive ----+---- Efficient
    Loser         |     Niche
                  |
                Low IS

Campaign positions:
- Brand Search: Efficient Winner ★
- Non-Brand Search: Expensive Loser ⚠
- Shopping: Moderate (center)
```

### Section 7: Bid Adjustment Cleanup

| Campaign | Adjustment | Current | Status | Recommendation |
|----------|-----------|---------|--------|---------------|
| Non-Brand Search | Mobile | -30% | IGNORED | Remove (Smart Bidding ignores) |
| Non-Brand Search | California | +20% | IGNORED | Remove |
| Display | Tablet | -100% | ACTIVE | Keep (tablets don't convert) |
| Brand Search | In-Market Auto | +50% | IGNORED | Remove |

**Cleanup Summary:**
- Adjustments to remove (zero impact): X
- Adjustments to evaluate: X
- Adjustments to keep: X

### Section 8: Prioritized Action Plan

Rank all recommendations by impact and urgency:

```
IMMEDIATE (This Week):
1. [Highest impact action — expected result]
2. [Second action]

SHORT-TERM (Weeks 2-4):
3. [Action after learning phases complete]
4. [Action requiring data gathering first]

MEDIUM-TERM (Weeks 4-8):
5. [Target ratcheting steps]
6. [Strategy graduation]

ONGOING:
7. [Monitoring items]
8. [Quarterly review items]
```

For each action item, include:
- **What**: Specific change to make
- **Where**: Campaign and setting to modify
- **Why**: Problem this solves
- **Expected impact**: Estimated improvement (conversions, CPA, ROAS)
- **Risk**: What could go wrong and how to mitigate
- **Timeline**: When to make the change and when to evaluate results
- **Success criteria**: How to know if the change worked

### Section 9: Monitoring Dashboard Setup

Recommend key metrics to monitor post-implementation:

**Daily Checks:**
- Any campaigns enter learning phase? (bid strategy status column)
- Spend rate vs budget (catch underspend early)

**Weekly Checks:**
- CPA/ROAS vs target by campaign
- Conversion volume trends
- Impression share changes
- Any new competitors in Auction Insights?

**Monthly Checks:**
- Bidding Health Score recalculation
- Target accuracy reassessment
- Competitive position shifts
- Strategy graduation candidates

### Section 10: Appendix

Include raw data tables, methodology notes, and any caveats:
- Date range analyzed
- Conversion actions included
- Attribution model in use
- Seasonality considerations
- Account structure notes
- Known data quality issues

## Report Generation Rules

1. **Be specific**: Never say "improve bid strategy." Say "change Campaign X from Max Conversions to tCPA at $48."
2. **Quantify impact**: Every recommendation should have an estimated impact range (e.g., "expected to recover 30-50 conversions/month").
3. **Acknowledge uncertainty**: Use ranges, not exact predictions. Smart Bidding outcomes are probabilistic.
4. **Prioritize ruthlessly**: If there are 15 findings, the top 3 should deliver 80% of the improvement. Highlight these.
5. **Account for learning phase**: Every strategy/target change triggers learning. Sequence changes to minimize overlapping learning phases.
6. **Seasonal context**: Note if the analysis period includes seasonal anomalies that could skew recommendations.
7. **Client-safe language**: Avoid blaming the advertiser for misconfiguration. Frame findings as "opportunities" and "optimizations."

## Output Format

Generate the report in clean markdown format suitable for sharing. Include:
- Table of contents with section links
- Color-coded severity indicators (use text labels: CRITICAL, WARNING, OK)
- Summary statistics at the top
- Detailed analysis in the body
- Action plan with timelines at the end
