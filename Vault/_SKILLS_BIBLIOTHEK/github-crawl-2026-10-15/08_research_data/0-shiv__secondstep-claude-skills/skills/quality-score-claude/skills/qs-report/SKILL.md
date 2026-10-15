# QS Audit Report Generator

## Command
`/qs report`

## Purpose

Generate a comprehensive Quality Score audit report suitable for client presentations, internal reviews, or stakeholder communication. The report combines findings from all QS sub-skills into a single, structured document with executive summary, detailed analysis, and actionable recommendations with estimated dollar savings.

## Report Structure

The QS audit report follows a fixed structure designed for maximum clarity and impact. Every section builds on the previous one, moving from overview to detail to action.

### Section 1: Executive Summary

A one-page summary for stakeholders who will not read the full report. Contains:

- **Account Name and Audit Period** — Date range of data analyzed
- **Overall QS Health Score** — A/B/C/D/F grade based on weighted average QS
- **Key Finding** — The single most important discovery (e.g., "67% of your $45,000 monthly spend goes to keywords with QS below 7, costing an estimated $12,400/month in excess CPC")
- **Estimated Monthly Savings** — Total realistic savings from QS optimization
- **Top 3 Recommendations** — Highest-impact actions in plain language
- **Timeline** — When savings should materialize (typically 30-90 days)

**Grading Scale:**
| Grade | Criteria |
|:--:|:--|
| A | 70%+ keywords at QS 7+, weighted avg QS > 7.5 |
| B | 60-70% keywords at QS 7+, weighted avg QS 6.5-7.5 |
| C | 45-60% keywords at QS 7+, weighted avg QS 5.5-6.5 |
| D | 30-45% keywords at QS 7+, weighted avg QS 4.5-5.5 |
| F | <30% keywords at QS 7+, weighted avg QS < 4.5 |

### Section 2: QS Distribution Histogram

Visual representation of QS distribution with:

- Bar chart showing keyword count by QS value (1-10)
- Overlay showing spend by QS value
- Comparison to benchmark distribution
- QS band summary table (Critical / Poor / Average / Good / Excellent)
- Spend concentration analysis (what % of budget goes to each QS band)

```
QS Distribution Summary
=========================
Band          Keywords    % of KWs    Monthly Spend    % of Spend
Critical(1-2)    40        3.2%         $3,200          7.1%
Poor (3-4)      112        9.0%         $5,800         12.9%
Average (5-6)   323       25.9%         $9,400         20.9%
Good (7)        312       25.0%        $11,200         24.9%
Excellent(8-10) 410       32.9%        $14,200         31.6%
Null             50        4.0%         $1,200          2.7%
─────────────────────────────────────────────────────────────
Total          1,247      100%         $45,000         100%

Keywords at QS 7+: 722 (57.9%) — Target: 60%+
Weighted Average QS: 6.4 — Target: 7.0+
Grade: C
```

### Section 3: CPC Impact Analysis

The money section. Quantifies the cost of suboptimal Quality Scores:

- **Total Monthly Waste** — Sum of excess CPC across all keywords below QS 10
- **Realistic Monthly Savings** — Achievable savings based on realistic QS targets
- **Top 20 Keywords by Waste** — Table showing keyword, current QS, monthly spend, monthly waste, weakest component
- **Waste Waterfall** — Cumulative waste chart showing how the top keywords account for most of the waste (Pareto principle: top 20% of keywords typically account for 70-80% of waste)

```
CPC Impact Summary
====================
Maximum theoretical savings (all KWs at QS 10):    $15,800/month
Realistic savings (achievable targets):              $9,200/month
90-day achievable savings:                           $6,100/month

Annual realistic savings:                           $110,400/year

Top 5 Keywords by Monthly Waste:
Rank  Keyword                    QS   Spend    Waste/Mo   Weakest Component
1.    "emergency plumber"         3   $5,625   $3,750     Landing Page (Below Avg)
2.    "plumber near me"           4   $3,724   $1,862     Ad Relevance (Below Avg)
3.    "plumbing services"         5   $2,890   $1,156     Expected CTR (Below Avg)
4.    "water heater repair"       4   $2,100   $1,050     Landing Page (Below Avg)
5.    "drain cleaning service"    3   $1,980     $990     All Below Avg
```

### Section 4: Component Breakdown

Analysis of the three QS components across the account:

```
Component Health Summary
=========================
                    Above Avg    Average    Below Avg    Biggest Issue
Expected CTR:         35%         40%         25%        Ad fatigue in 3 campaigns
Ad Relevance:         28%         45%         27%        12 ad groups with 20+ keywords
Landing Page:         20%         35%         45%        ← Weakest component overall
```

- Identify which component is the primary drag on QS account-wide
- Show component ratings by campaign
- Highlight the campaigns and ad groups with the worst component ratings
- Connect each Below Average rating to a specific, fixable root cause

### Section 5: Top 20 Keywords to Fix

The prioritized fix list. For each keyword:

| Field | Description |
|:--|:--|
| Rank | Priority ranking (1 = highest impact) |
| Keyword | Keyword text and match type |
| Campaign / Ad Group | Location in account |
| Current QS | Current Quality Score |
| Target QS | Realistic target |
| Expected CTR | Component rating |
| Ad Relevance | Component rating |
| Landing Page | Component rating |
| Monthly Spend | Current monthly cost |
| Monthly Waste | Estimated excess spend |
| Root Cause | Primary issue identified |
| Fix Action | Specific recommended action |
| Fix Effort | Low / Medium / High |
| Expected Savings | Monthly savings if target QS reached |

### Section 6: Landing Page Analysis

Summary of landing page performance:

- Table of all unique landing pages with keyword count, average QS, and LP Experience ratings
- Top 5 worst-performing landing pages with specific issues
- Page speed scores for priority pages
- Mobile responsiveness status
- Content relevance assessment

### Section 7: Ad Group Structure Assessment

Analysis of ad group organization:

- Ad groups by keyword count (histogram)
- Ad groups with theme tightness issues
- Ad copy-keyword alignment audit for priority ad groups
- RSA headline coverage analysis
- Extension coverage by campaign

### Section 8: Estimated Monthly Savings

A clear savings projection broken down by fix category:

```
Estimated Monthly Savings by Fix Category
============================================
Category                      Actions    Est. Savings    Effort    Timeline
Landing Page Speed Fixes         5         $3,200        Low       1-2 weeks
Landing Page Content Updates     8         $2,100        Medium    2-3 weeks
Ad Group Restructuring          12         $1,800        Medium    2-4 weeks
Ad Copy Rewrites                15         $1,200        Low       1-2 weeks
Extension Buildout               4           $600        Low       1-2 days
Match Type Cleanup               -           $300        Low       1 week
────────────────────────────────────────────────────────────────────────────
Total                           44         $9,200/month            4-8 weeks
                                          $110,400/year
```

### Section 9: 30-60-90 Day Action Plan

Sequenced execution roadmap:

**Days 1-30:**
- Fix landing page speed issues (5 pages)
- Add missing ad extensions across all campaigns
- Add negative keywords from search terms report
- Begin ad group restructuring (top 5 by spend)

**Days 31-60:**
- Complete ad group restructuring
- Rewrite ad copy for all Below Average Ad Relevance ad groups
- Update landing page content for keyword relevance
- Implement device and geographic bid adjustments

**Days 61-90:**
- Monitor QS changes from first round of fixes
- A/B test new ad copy variations
- Create dedicated landing pages for remaining high-spend keyword themes
- Set up automated weekly QS tracking

### Section 10: Appendix

- Full keyword-level data table (sortable)
- Methodology notes and assumptions
- QS component weight sources and disclaimers
- Glossary of terms

## Report Generation Guidelines

When generating the report:

1. **Use the user's actual data.** Never use placeholder numbers if real data is available.
2. **Round dollar amounts to the nearest $10.** False precision undermines credibility.
3. **Be conservative on savings estimates.** Under-promise, over-deliver. Use realistic target QS, not theoretical maximum.
4. **Include caveats.** Note that QS improvements take time, CPC reductions are approximate, and competitive dynamics can affect outcomes.
5. **Make it actionable.** Every finding must have a specific recommended action. Diagnosis without prescription is useless.
6. **Prioritize ruthlessly.** The Top 20 list matters more than the full keyword dump. Focus attention on what moves the needle.

## Output Formats

The report can be generated as:
- **Markdown** — For pasting into documents, Notion, or Slack
- **Structured text** — For terminal/CLI output
- **CSV data tables** — For the appendix data, importable to spreadsheets
- **PDF-ready HTML** — When used with the Second Step PDF pipeline

## Data Requirements

Minimum data needed to generate the report:
- Keyword text
- Quality Score (1-10)
- Three component ratings
- Monthly spend or impressions + CPC

Full report requires all columns listed in the main SKILL.md data requirements section.
