# YouTube Audit Report Skill

**Command:** `/yt report`

## Purpose

Generates a comprehensive YouTube advertising audit report combining scores from all sub-skills into a unified deliverable. This report is designed to be shared with clients, stakeholders, or internal teams as a complete assessment of YouTube advertising health. The report includes the YouTube Ads Score (0-100), dimension-level scores, creative evaluations, targeting analysis, and a prioritized action plan.

## Report Structure

### Section 1: Executive Summary

Provide a 3-5 sentence overview that a non-technical stakeholder can understand in 30 seconds:

- Overall YouTube Ads Score and what it means
- The single biggest opportunity identified
- The most critical issue that needs immediate attention
- Estimated impact of implementing recommendations (qualitative: significant, moderate, incremental)

### Section 2: YouTube Ads Score Dashboard

The composite score across all 8 weighted dimensions:

```
## YouTube Ads Score: [X]/100

| Dimension | Score | Weight | Weighted Score | Rating |
|-----------|-------|--------|---------------|--------|
| Campaign Structure | /100 | 15% | /15 | |
| Creative Quality | /100 | 20% | /20 | |
| Targeting Precision | /100 | 15% | /15 | |
| Bidding Strategy | /100 | 10% | /10 | |
| Placement Hygiene | /100 | 10% | /10 | |
| Remarketing Depth | /100 | 10% | /10 | |
| Shorts Readiness | /100 | 10% | /10 | |
| Measurement Setup | /100 | 10% | /10 | |
| **TOTAL** | | **100%** | **/100** | |

Rating Scale:
90-100 = Elite | 70-89 = Strong | 50-69 = Average | 30-49 = Weak | 0-29 = Critical
```

### Section 3: Campaign Structure Analysis

Summarize findings from the campaign audit:

- Total number of campaigns and ad groups
- Objective alignment assessment
- Format mix coverage
- Budget distribution analysis
- Naming convention quality
- Frequency management status
- Key structural issues identified

### Section 4: Creative Performance Review

For each active video creative, provide:

```
### Creative: [Video Title / ID]
- Format: [Skippable / Non-Skip / Bumper / Shorts / In-Feed]
- Duration: [Xs]
- ABCD Score: [X/100]
  - Attract (Hook): [X/25]
  - Brand: [X/25]
  - Connect: [X/25]
  - Direct (CTA): [X/25]
- View Rate: [X%] (Benchmark: [X%])
- CTR: [X%] (Benchmark: [X%])
- Key Strength: [One line]
- Key Weakness: [One line]
- Priority Fix: [One actionable recommendation]
```

If multiple creatives exist, rank them by ABCD score and highlight the top performer and bottom performer.

### Section 5: Audience & Targeting Assessment

Summarize targeting strategy findings:

- Audience types in use vs. available
- Custom Intent coverage and keyword quality
- In-Market segment relevance
- Remarketing list depth and tiering
- Audience exclusion hygiene
- Demographic filtering assessment
- Audience overlap analysis

### Section 6: Bidding & Budget Optimization

- Current bid strategies per campaign
- Bid strategy alignment with objectives
- Campaign maturity assessment
- Conversion volume sufficiency for automated bidding
- Seasonal considerations
- Budget allocation efficiency (spend vs. return by campaign)
- Recommended bid strategy changes

### Section 7: Placement & Brand Safety Review

- Current inventory type setting
- Content exclusion configuration
- Channel exclusion list size and quality
- Top wasteful placements identified
- Brand safety vendor status
- Placement performance: managed vs. automatic

### Section 8: Measurement & Tracking Audit

Verify the measurement foundation:

| Tracking Element | Status | Impact |
|-----------------|--------|--------|
| Google Ads conversion tag | Active / Missing | Critical |
| View-through conversions | Enabled / Disabled | High |
| Conversion window (should be 30d) | [Current setting] | High |
| Enhanced Conversions | Active / Missing | Medium |
| GA4 linked to Google Ads | Yes / No | Medium |
| YouTube channel linked | Yes / No | Medium |
| Offline conversion import | Active / N/A | Varies |
| Consent Mode v2 | Active / Missing | Medium (EU) |

### Section 9: Competitive Context

If competitive data is available or can be inferred:

- How does the account compare to industry YouTube benchmarks?
- Are competitors active on YouTube? (Can check via ads transparency center)
- What formats are competitors using?
- Opportunities competitors are missing

### Section 10: Prioritized Action Plan

Organize all recommendations into a tiered, time-bound plan:

```
## Critical Issues (Fix This Week)
Issues that are actively wasting budget or causing measurement failures.
1. [Issue] — Impact: [High] — Effort: [Low/Med/High]
2. ...

## High Priority (Fix Within 2 Weeks)
Issues with significant performance impact.
1. ...

## Medium Priority (Fix Within 30 Days)
Optimizations that will improve efficiency.
1. ...

## Quick Wins (Implement Anytime)
Low-effort changes with positive impact.
1. ...

## Strategic Initiatives (30-90 Day Roadmap)
Larger projects that require planning and resources.
1. ...
```

### Section 11: 90-Day Roadmap

```
## Month 1: Foundation
Week 1: [Actions]
Week 2: [Actions]
Week 3: [Actions]
Week 4: [Actions]

## Month 2: Optimization
Week 5-6: [Actions]
Week 7-8: [Actions]

## Month 3: Scale
Week 9-10: [Actions]
Week 11-12: [Actions]

## Expected Outcomes After 90 Days
- YouTube Ads Score improvement: [Current] → [Projected]
- Estimated efficiency gain: [X% lower CPV/CPA]
- New format adoption: [Formats to launch]
- Audience expansion: [New audiences to test]
```

## Report Generation Process

When the user triggers `/yt report`, follow this process:

1. **Check available data:** Ask the user what data they can provide (campaign reports, creative assets, audience reports, placement reports)
2. **Run applicable sub-skills:** Execute relevant sub-skill analyses based on available data
3. **Aggregate scores:** Compute the weighted YouTube Ads Score
4. **Generate the report:** Produce all 11 sections with specific, actionable findings
5. **Prioritize actions:** Rank all recommendations by impact and effort
6. **Present the report:** Format as a clean, scannable document

## Report Formatting Guidelines

- Use tables for data-heavy sections (easier to scan than paragraphs)
- Bold key findings and scores for quick scanning
- Include benchmark comparisons wherever possible
- Keep recommendations specific and actionable (not "improve creative" but "rewrite hook for Video X to lead with the customer pain point")
- Include estimated impact where possible (qualitative if not quantitative)
- End with clear next steps and ownership assignments

## Data Gaps Handling

If the user cannot provide all requested data:

- Note which dimensions could not be fully scored
- Provide the score based on available data with a confidence indicator
- Mark missing dimensions as "Unable to assess — data required: [specific data needed]"
- Still provide general best-practice recommendations for unscored dimensions
- Recommend the user pull specific reports for a complete audit
