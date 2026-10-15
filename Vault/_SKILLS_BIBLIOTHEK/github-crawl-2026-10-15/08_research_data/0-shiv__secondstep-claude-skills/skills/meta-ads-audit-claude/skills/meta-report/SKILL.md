# Meta Ads Audit Report Generator

## Command
`/meta report`

## Description
Generates a comprehensive, branded Meta Ads audit report compiling scores from all audit dimensions, creating a visual health score radar chart, summarizing top findings, and producing a prioritized action plan. This is the final deliverable that brings together all individual audit results into a cohesive, client-ready document.

## Why a Structured Report Matters

Raw audit data is overwhelming. A well-structured report transforms 150+ data points into:

- **Executive summary**: One-page overview for decision makers
- **Visual health score**: Radar chart showing strengths and weaknesses at a glance
- **Prioritized actions**: Ordered by impact and effort, so the team knows what to fix first
- **Benchmark context**: Performance framed against industry standards
- **Revenue impact estimates**: Projected improvement from fixing identified issues

## Report Structure

### 1. Cover Page
```
META ADS AUDIT REPORT
[Account Name]
[Date Range Analyzed]
[Prepared by: Second Step]

Overall Health Score: XX/100 (Grade: X)
```

### 2. Executive Summary (1 page)

- **Account Overview**: Account name, monthly spend, campaigns active, date range
- **Health Score**: XX/100 with letter grade
- **Top 3 Wins**: What the account does well
- **Top 3 Issues**: Most impactful problems found
- **Estimated Impact**: Projected CPA reduction and ROAS improvement from fixing issues
- **Urgency Level**: Immediate action required / Optimization opportunity / Fine-tuning

### 3. Health Score Radar Chart

The radar chart visualizes all 7 audit dimensions:

```
                    Pixel & Tracking (XX/100)
                          /\
                         /  \
    Ad Copy &           /    \          Conversions
    Placements         /      \         API (XX/100)
    (XX/100)     ----/--------\----
                    /   SCORE    \
                   /    XX/100    \
    Advantage+    /                \    Creative
    Config       /                  \   Health
    (XX/100)    \                  /    (XX/100)
                 \                /
                  \              /
    Budget &      \            /     Audience
    Bidding        \          /      Strategy
    (XX/100)        \--------/       (XX/100)
```

**Dimension Scores Table:**
| Dimension | Score | Grade | Weight | Weighted Score |
|-----------|-------|-------|--------|---------------|
| Pixel & Tracking | /100 | | 20% | |
| Conversions API | /100 | | 15% | |
| Creative Health | /100 | | 20% | |
| Audience Strategy | /100 | | 15% | |
| Budget & Bidding | /100 | | 10% | |
| Advantage+ Config | /100 | | 10% | |
| Ad Copy & Placements | /100 | | 10% | |
| **Composite Score** | **/100** | | **100%** | |

### 4. Dimension-by-Dimension Breakdown

For each of the 7 dimensions, include:
- Score and grade
- Key metrics
- Specific findings with data
- Comparison to industry benchmark
- Recommended actions

### 5. Top 10 Critical Findings

Ranked by impact (estimated CPA/ROAS improvement if fixed):

| # | Finding | Dimension | Impact | Effort | Priority |
|---|---------|-----------|--------|--------|----------|
| 1 | [Finding] | [Dim] | High | Low | P0 |
| 2 | [Finding] | [Dim] | High | Medium | P0 |
| ... | ... | ... | ... | ... | ... |
| 10 | [Finding] | [Dim] | Medium | Low | P1 |

### 6. Industry Benchmark Comparison

| Metric | Account | Industry Avg | Delta | Status |
|--------|---------|-------------|-------|--------|
| CPM | $ | $ | | Above/Below |
| CTR | % | % | | Above/Below |
| CPC | $ | $ | | Above/Below |
| Conv Rate | % | % | | Above/Below |
| ROAS | x | x | | Above/Below |
| Frequency (7d) | | < 3.0 | | OK/High |
| EMQ Score | /10 | 6.0+ | | OK/Low |

### 7. Prioritized Action Plan

#### Quick Wins (This Week) — High Impact, Low Effort
1. [Action item with specific steps]
2. [Action item with specific steps]
3. [Action item with specific steps]

#### Medium-Term (Next 2-4 Weeks) — High Impact, Medium Effort
1. [Action item with specific steps]
2. [Action item with specific steps]
3. [Action item with specific steps]

#### Strategic (Next 1-3 Months) — Foundational Improvements
1. [Action item with specific steps]
2. [Action item with specific steps]
3. [Action item with specific steps]

### 8. Appendix

- Full checklist results (150+ points)
- Raw data tables
- Methodology notes
- Tool and resource references

## Report Generation Process

When `/meta report` is triggered:

1. **Collect Sub-Scores**: Pull scores from each completed sub-skill audit
2. **Calculate Composite**: Apply weighted average formula
3. **Rank Findings**: Sort all findings by impact score
4. **Generate Benchmark Comparison**: Match account industry to benchmark table
5. **Build Action Plan**: Categorize findings into Quick Win / Medium / Strategic
6. **Format Report**: Apply template structure with all data populated
7. **Output**: Deliver as structured markdown (convertible to PDF)

## Score Calculation Formula

```
composite_score = (
    pixel_score * 0.20 +
    capi_score * 0.15 +
    creative_score * 0.20 +
    audience_score * 0.15 +
    budget_score * 0.10 +
    advantage_score * 0.10 +
    copy_placement_score * 0.10
)
```

## Impact Estimation Framework

Each finding gets an estimated impact score based on:

| Factor | Low (1) | Medium (2) | High (3) |
|--------|---------|-----------|----------|
| Spend affected | < 10% of budget | 10-30% | > 30% |
| CPA impact | < 5% improvement | 5-15% | > 15% |
| Implementation effort | > 2 weeks | 1-2 weeks | < 1 week |
| Risk of not fixing | Low | Medium | Revenue loss |

**Priority Matrix:**
| | Low Effort | Medium Effort | High Effort |
|---|-----------|--------------|------------|
| **High Impact** | P0 — Do Now | P0 — Plan This Week | P1 — Schedule |
| **Medium Impact** | P1 — Quick Win | P2 — Backlog | P2 — Evaluate |
| **Low Impact** | P2 — If Time | P3 — Deprioritize | P3 — Skip |

## Output Formats

The report can be generated in:
1. **Markdown** — Default output, easily shared and versioned
2. **HTML** — Styled for browser viewing
3. **PDF** — Client-ready branded document (via CSS + Chrome headless)

## Common Report Customizations

- **White-label**: Remove branding for agency resale
- **Client-specific language**: Adjust technical depth for audience
- **Selective dimensions**: Report on specific dimensions only (e.g., Pixel + CAPI only)
- **Comparative**: Compare current audit to previous audit (if available)
- **Multi-account**: Roll up scores across multiple ad accounts for portfolio view
