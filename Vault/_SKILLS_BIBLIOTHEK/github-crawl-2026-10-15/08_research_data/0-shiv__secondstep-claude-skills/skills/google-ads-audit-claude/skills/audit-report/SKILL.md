---
name: audit-report
description: Generates the final Google Ads audit report including executive summary, overall weighted score with radar chart data, dimension-by-dimension breakdown, top 10 findings by impact, prioritized action plan (Quick Wins / Medium Effort / Complex Projects), estimated monthly savings, benchmark comparison, and next steps. Outputs in both Markdown and PDF formats.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Audit Report Generation

## Overview

The audit report is the final deliverable — a comprehensive document that synthesizes findings from all 12 audit dimensions into a single, actionable report. It translates technical audit data into business-impact language that stakeholders at every level can understand and act upon.

This skill orchestrates the output from all other audit skills (campaign structure, keywords, quality score, bidding, extensions, conversion tracking, negative keywords, budget, ad copy, landing pages, PMax, and audience) into a weighted overall score, highlights the top findings by impact, and produces a prioritized action plan with estimated cost savings and performance improvements.

**Key principle:** The report must answer three questions for every stakeholder:
1. How healthy is this account?
2. Where is money being wasted?
3. What should we fix first, and what will it save?

## Report Structure

### Section 1: Executive Summary

The executive summary must fit on one page and be comprehensible by a non-technical stakeholder.

**Required elements:**
- Overall account health score (0-100) with letter grade and color indicator
- One-paragraph assessment of account state (3-5 sentences)
- Total estimated monthly waste in dollars
- Top 3 most impactful findings (one sentence each, quantified)
- Recommended immediate actions (next 48 hours — max 3 items)
- Account metadata: name, monthly spend, date range analyzed, number of campaigns

**Tone guidance:**
- Professional but not alarmist — even low-scoring accounts should frame findings as opportunities
- Lead with the positive before the negative (e.g., "Conversion tracking is solid. However, keyword management has significant gaps.")
- Use dollar amounts over percentages when possible (stakeholders respond more to "$4,200 wasted monthly" than "15% waste rate")

### Section 2: Score Dashboard with Radar Chart Data

**Overall Weighted Score:**

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| Conversion Tracking | 15% | X/100 | X.X |
| Bidding Strategy | 12% | X/100 | X.X |
| Keyword Strategy | 10% | X/100 | X.X |
| Quality Score | 10% | X/100 | X.X |
| Budget Management | 10% | X/100 | X.X |
| Campaign Structure | 8% | X/100 | X.X |
| Negative Keywords | 8% | X/100 | X.X |
| Ad Copy Quality | 7% | X/100 | X.X |
| Landing Pages | 7% | X/100 | X.X |
| Performance Max | 5% | X/100 | X.X |
| Ad Extensions | 4% | X/100 | X.X |
| Audience Targeting | 4% | X/100 | X.X |
| **OVERALL** | **100%** | — | **X.X/100** |

**Radar Chart Data Format** (for visualization):
```json
{
  "labels": ["Conv Tracking", "Bidding", "Keywords", "Quality Score", "Budget", "Structure", "Negatives", "Ad Copy", "Landing Pages", "PMax", "Extensions", "Audiences"],
  "data": [85, 72, 65, 78, 60, 80, 45, 70, 55, 68, 50, 40],
  "benchmarks": [75, 70, 65, 70, 65, 70, 60, 65, 60, 60, 60, 55]
}
```

**Color coding:**
- Green (90-100): Excellent — maintain and refine
- Yellow-Green (75-89): Good — specific improvements available
- Yellow (60-74): Average — meaningful optimization needed
- Orange (40-59): Below Average — significant issues
- Red (0-39): Poor — urgent remediation required

**Weight Adjustments:**
- No PMax campaigns: Redistribute 5% PMax weight proportionally across other dimensions
- Display-only accounts: Increase Audience weight to 10%, reduce Keyword weight to 5%
- Brand-only accounts: Reduce Negative Keywords weight to 4%, increase Ad Copy to 11%
- New accounts (< 90 days): Add caveat that scores may improve with data accumulation

### Section 3: Dimension-by-Dimension Analysis

For each of the 12 audit dimensions, output a structured block:

```markdown
### [Dimension Name] — Score: X/100 ([Grade])

**Summary:** [2-3 sentence overview of findings]

**Critical Issues:**
- [Issue 1 with specific data point]
- [Issue 2 with specific data point]

**What's Working:**
- [Positive finding 1]
- [Positive finding 2]

**Recommendations:**
1. [Action] — Est. impact: [quantified improvement]
2. [Action] — Est. impact: [quantified improvement]
```

**Dimension order in report** (highest weight first):
1. Conversion Tracking (15%)
2. Bidding Strategy (12%)
3. Keyword Strategy (10%)
4. Quality Score (10%)
5. Budget Management (10%)
6. Campaign Structure (8%)
7. Negative Keywords (8%)
8. Ad Copy Quality (7%)
9. Landing Pages (7%)
10. Performance Max (5%)
11. Ad Extensions (4%)
12. Audience Targeting (4%)

### Section 4: Top 10 Critical Findings

Ranked by estimated financial impact (highest dollar savings to lowest):

| Rank | Finding | Dimension | Severity | Est. Monthly Impact | Fix Complexity | Time to Fix |
|------|---------|-----------|----------|-------------------|----------------|-------------|
| 1 | [Description] | [Dimension] | Critical | $X,XXX | Quick Win | 1-2 hours |
| 2 | [Description] | [Dimension] | Critical | $X,XXX | Medium | 1-2 weeks |
| ... | ... | ... | ... | ... | ... | ... |

**Severity definitions:**
- **Critical:** Actively wasting significant budget or producing incorrect data; fix immediately
- **High:** Meaningful performance drag; fix within 1 week
- **Medium:** Optimization opportunity; fix within 2-4 weeks
- **Low:** Nice-to-have improvement; address when bandwidth allows

**Each finding detail block:**
```markdown
#### Finding #X: [Title]
**Dimension:** [Name] | **Severity:** [Level] | **Est. Monthly Impact:** $X,XXX

**What's happening:** [Specific, data-backed description of the issue]

**Why it matters:** [Business impact — cost, conversions lost, data integrity risk]

**How to fix it:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected improvement:** [Quantified — e.g., "Reduce CPA by ~15% ($X/month savings)" or "Recover ~20% of missing conversion data"]
```

### Section 5: Prioritized Action Plan

#### Quick Wins (1-2 hours each, implement this week)
Tasks that can be completed in the Google Ads interface immediately with no external dependencies.

Examples:
- Pause high-spend zero-conversion keywords ($X/month savings)
- Add 50 negative keywords from N-gram analysis ($X/month savings)
- Fix conversion counting from "Every" to "One" (data accuracy)
- Turn off Display Network on Search campaigns ($X/month savings)
- Switch location targeting from "Presence or Interest" to "Presence Only"
- Add missing ad extensions (sitelinks, callouts, structured snippets)
- Set device bid adjustments based on performance data
- Exclude existing customers from acquisition campaigns

#### Medium-Term Projects (1-2 weeks, plan and execute)
Tasks requiring some planning, creative development, or testing setup.

Examples:
- Rewrite RSA ad copy to achieve "Excellent" Ad Strength
- Restructure campaigns for better keyword-to-ad relevance
- Implement RLSA audiences across all Search campaigns
- Set up Enhanced Conversions for Web (EC4W)
- Build shared negative keyword lists by category
- Create custom audience segments from competitor analysis
- Optimize bid strategy targets based on 30-day data
- Build new landing page variants for A/B testing

#### Complex Projects (2-4 weeks, requires resources)
Tasks requiring development, design, cross-team coordination, or significant strategic shifts.

Examples:
- Landing page redesign for message match and speed
- Server-side GTM implementation
- Enhanced Conversions for Leads (EC4L) pipeline setup
- Offline conversion import CRM integration
- PMax campaign restructuring with proper asset groups
- Full account restructure (campaign consolidation or expansion)
- Customer Match automation setup

### Section 6: Estimated Monthly Savings Calculation

**Savings methodology:**

| Source of Savings | Calculation | Est. Monthly Savings |
|-------------------|-----------|---------------------|
| Negative keyword waste elimination | Irrelevant search term spend x reduction % | $X |
| Keyword pause (high spend, no conv) | Sum of wasted keyword spend | $X |
| QS improvement CPC reduction | QS tax calculation | $X |
| Display network removal from Search | Display spend in Search campaigns | $X |
| Geo targeting fix (Presence Only) | Out-of-area click estimate x CPC | $X |
| Budget reallocation | Marginal CPA improvement from shift | $X |
| Conversion tracking fix impact | Smart bidding efficiency gain | $X |
| **TOTAL ESTIMATED SAVINGS** | | **$X,XXX** |

**Projected performance improvements:**
- CPA reduction: X-Y% (from $X to $Y)
- Conversion volume increase: +X-Y% (from X to Y/month)
- ROAS improvement: X-Y% (from Xx to Yx)
- CTR improvement: X-Y% (from X% to Y%)

**Confidence levels:**
- High confidence (data-backed): Savings from keyword pauses, negative keywords, budget reallocation
- Medium confidence (estimated): QS improvement impact, bid strategy optimization
- Low confidence (projected): Landing page improvements, audience optimization, PMax restructuring

### Section 7: Benchmark Comparison

Compare key account metrics against industry benchmarks:

| Metric | Account | Industry Avg | Top 25% | Assessment |
|--------|---------|-------------|---------|------------|
| Search CTR | X% | 3-5% | 6-8% | Above/Below |
| Search CVR | X% | 2-5% | 5-10% | Above/Below |
| CPA | $X | $XX-$XX | $XX | Above/Below |
| Quality Score (avg) | X | 5-6 | 7+ | Above/Below |
| Impression Share | X% | 40-60% | 70%+ | Above/Below |
| Ad Strength (% Good+) | X% | 50-60% | 80%+ | Above/Below |

**Industry benchmark sources:**
- Google Ads benchmarks by industry (WordStream/LOCALiQ annual reports)
- Internal database of audited accounts
- Google Ads Recommendations tab benchmarks

### Section 8: Next Steps & Timeline

**Immediate (This Week):**
- Complete Quick Win actions
- Schedule follow-up meeting to review findings

**Short-Term (Weeks 2-4):**
- Execute Medium-Term projects
- Monitor impact of Quick Win changes
- Begin planning Complex Projects

**Medium-Term (Weeks 5-8):**
- Execute Complex Projects
- Conduct A/B tests on new ad copy and landing pages
- Review initial results from changes made

**Re-Audit (90 Days):**
- Conduct follow-up audit to measure improvement
- Compare scores across all dimensions
- Identify new optimization opportunities
- Calculate actual savings achieved vs projected

## Grade Scale

| Score | Grade | Label | Color |
|-------|-------|-------|-------|
| 90-100 | A | Excellent | Green |
| 80-89 | B+ | Very Good | Light Green |
| 75-79 | B | Good | Yellow-Green |
| 65-74 | C+ | Above Average | Yellow |
| 60-64 | C | Average | Orange |
| 50-59 | D | Below Average | Light Red |
| 40-49 | D- | Poor | Red |
| 0-39 | F | Critical | Dark Red |

## Output Formats

### Markdown Report
- Full report in Markdown format
- All tables formatted for GitHub/Notion rendering
- Saved to `output/[account-name]-audit-[date].md`
- Includes all 8 sections above

### PDF Report
- Generated from Markdown via HTML + CSS styling + Chrome headless `--print-to-pdf`
- Professional formatting suitable for client delivery
- Includes radar chart visualization for dimension scores
- Color-coded findings table and score indicators
- Saved to `output/[account-name]-audit-[date].pdf`
- PDF styling: dark theme (#1b1b1b background option or clean white), accent color customizable, professional fonts

### Standalone Outputs
- **Executive Summary**: One-page document for C-suite → `output/[account-name]-executive-summary-[date].md`
- **Action Plan**: Task-level detail for implementation team → `output/[account-name]-action-plan-[date].md`
- **Score Card**: One-page score overview with radar chart → `output/[account-name]-scorecard-[date].md`

## Process Flow

```
1. Collect dimension scores from all 12 audit skills
2. Apply weight adjustments (PMax N/A, account type, etc.)
3. Calculate weighted overall score
4. Rank all findings by estimated financial impact
5. Categorize top 10 findings with severity and complexity
6. Generate Quick Win / Medium / Complex action tiers
7. Calculate estimated monthly savings from each source
8. Pull industry benchmarks for comparison
9. Build timeline and next steps
10. Populate report template with all data
11. Generate Markdown report
12. Generate PDF version with charts and styling
13. Generate standalone executive summary and action plan
14. Output all files to output/ directory
```

## Quality Checklist

Before finalizing the report, verify:
- [ ] All 12 dimension scores are populated (or marked N/A with rationale and weight redistributed)
- [ ] Overall score calculation is correct (weights sum to 100%)
- [ ] Top 10 findings are ordered by financial impact (highest first)
- [ ] Every finding has a specific, quantified recommendation
- [ ] Estimated savings calculations are reasonable and documented with methodology
- [ ] Action plan covers all Critical and High severity findings
- [ ] Executive summary accurately reflects the full report
- [ ] No contradictions between dimension sections
- [ ] All data references are from the analyzed date range
- [ ] Benchmark comparisons use appropriate industry vertical
- [ ] PDF renders correctly with proper formatting
- [ ] Radar chart data array has correct values for all 12 dimensions
- [ ] Timeline is realistic for the client's team size and resources

## Report Tone by Score

**Healthy Account (Score 80+):** Lead with what's working well. Focus on incremental optimizations, testing opportunities, and scaling strategies. Position the audit as a validation with fine-tuning recommendations. Estimated savings will be modest.

**Moderate Issues (Score 60-79):** Balanced tone — acknowledge strengths while clearly identifying 3-5 high-impact fixes. Quantify the opportunity cost of not acting. Budget reallocation and negative keywords are usually the biggest wins.

**Troubled Account (Score < 60):** Lead with the most foundational issue (usually conversion tracking or structural problems). Propose a phased remediation plan — do not overwhelm with 50 recommendations. Prioritize ruthlessly. Frame as a turnaround opportunity with significant savings potential.

**New Account (< 90 days data):** Adjust expectations for data volume. Focus on setup correctness rather than optimization. Flag areas that need data accumulation before conclusions can be drawn. Score leniently on performance-dependent checks.
