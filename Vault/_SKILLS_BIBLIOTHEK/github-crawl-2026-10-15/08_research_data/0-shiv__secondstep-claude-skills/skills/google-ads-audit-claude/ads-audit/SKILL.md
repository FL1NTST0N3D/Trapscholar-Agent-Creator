---
name: ads-audit
description: >
  Comprehensive Google Ads account audit with 200+ checks across campaigns, keywords,
  Quality Score, bidding, extensions, conversion tracking, negative keywords, PMax & more.
  Triggers on: "ads", "google ads", "audit", "ppc", "adwords", "campaign audit"
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Google Ads Audit — Main Orchestrator

## Quick Reference

| Command | Sub-Skill | Description |
|---------|-----------|-------------|
| `/ads audit` | Full audit | All 200+ checks with 5 parallel agents |
| `/ads quick` | Quick scan | Top 20 critical issues in 5 minutes |
| `/ads keywords` | audit-keywords | Match types, search terms, cannibalization |
| `/ads quality-score` | audit-quality-score | QS components & CPC impact |
| `/ads bidding` | audit-bidding | Bid strategy & learning phase |
| `/ads budget` | audit-budget | Impression share & pacing |
| `/ads extensions` | audit-extensions | Ad assets coverage scoring |
| `/ads conversions` | audit-conversion-tracking | Tag health, EC, attribution |
| `/ads negatives` | audit-negative-keywords | N-gram analysis & conflict detection |
| `/ads copy` | audit-ad-copy | RSA scoring & headline diversity |
| `/ads landing-pages` | audit-landing-pages | CRO, speed, message match |
| `/ads pmax` | audit-pmax | Performance Max audit |
| `/ads audiences` | audit-audience | Audience strategy review |
| `/ads report` | audit-report | Markdown audit report |
| `/ads report-pdf` | audit-report | PDF with charts & scorecards |

## Account Type Detection

Before running the audit, detect the account type to apply the right benchmarks:

| Account Type | Signals | Benchmark Set |
|-------------|---------|---------------|
| E-commerce | Shopping campaigns, product feeds, ROAS bidding | E-commerce benchmarks |
| Lead Gen | Lead form extensions, tCPA bidding, call tracking | Lead gen benchmarks |
| SaaS | Trial/demo conversions, long sales cycles | SaaS/B2B benchmarks |
| Local Service | Location extensions, radius targeting, call campaigns | Local benchmarks |
| Brand | Brand keywords, high CTR, low CPC | Brand benchmarks |
| App | App campaigns, install tracking, in-app events | App benchmarks |

## Full Audit Orchestration

When the user runs `/ads audit`, execute this flow:

### Phase 1: Data Collection
1. Ask the user for account data. Accept any of:
   - Google Ads CSV export (campaign, keyword, search term reports)
   - Google Ads Editor file (backup)
   - Manual description of account structure
   - Screenshots of the Google Ads interface
2. Parse and normalize the data for analysis

### Phase 2: Account Type Detection
1. Analyze campaign types, bidding strategies, and conversion actions
2. Classify as: E-commerce, Lead Gen, SaaS, Local Service, Brand, or App
3. Load corresponding benchmark set

### Phase 3: Parallel Agent Delegation
Launch 5 subagents simultaneously:

```
Agent: campaign-health
├── Campaign structure analysis
├── Settings audit (networks, geo, schedule, devices)
├── Naming convention check
└── Score: Campaign Structure (15% weight)

Agent: keyword-intelligence
├── Keyword match type distribution
├── Search term analysis
├── Quality Score distribution
├── Keyword cannibalization detection
├── Negative keyword gaps
└── Score: Keyword Health (20%) + Quality Score (15%) + Negatives (5%)

Agent: conversion-pipeline
├── Conversion tracking validation
├── Enhanced Conversions check
├── Attribution model review
├── Conversion action settings
└── Score: Conversion Tracking (15%)

Agent: creative-quality
├── RSA ad copy scoring
├── Ad Strength analysis
├── Extension coverage
├── Landing page assessment
└── Score: Ad Copy (10%) + Extensions (5%)

Agent: budget-efficiency
├── Bid strategy analysis
├── Budget pacing
├── Impression share analysis
├── Wasted spend calculation
└── Score: Bidding & Budget (15%)
```

### Phase 4: Score Compilation
1. Collect scores from all 5 agents
2. Apply weights to compute composite Ads Health Score (0-100)
3. Classify overall rating: Excellent (90+), Good (75-89), Average (60-74), Below Average (40-59), Critical (0-39)

### Phase 5: Report Generation
1. Generate executive summary with composite score
2. List top 10 findings by impact
3. Create prioritized action plan (Quick Wins → Medium Effort → Complex)
4. Calculate estimated monthly savings opportunity
5. Output as markdown (default) or PDF (if `/ads report-pdf`)

## Quick Audit Flow (`/ads quick`)

When user runs `/ads quick`, run a streamlined 20-check audit:

1. ✅ Conversion tracking is set up and firing
2. ✅ Enhanced Conversions enabled
3. ✅ No "Search with Display" campaigns
4. ✅ Location targeting set to "Presence" (not "Presence or Interest")
5. ✅ Negative keyword lists applied to all campaigns
6. ✅ No broad match keywords without negative keywords
7. ✅ Quality Score distribution (% of keywords QS ≥ 7)
8. ✅ Ad Strength "Good" or "Excellent" on all RSAs
9. ✅ At least 4 sitelink extensions per campaign
10. ✅ No campaigns limited by budget
11. ✅ Smart bidding not in learning phase for >14 days
12. ✅ Search term irrelevancy rate < 20%
13. ✅ No keyword cannibalization across campaigns
14. ✅ Landing pages load in < 3 seconds
15. ✅ Mobile bid adjustments set appropriately
16. ✅ Ad schedule aligns with conversion patterns
17. ✅ Geographic performance reviewed (exclude poor areas)
18. ✅ Audience lists applied (at minimum, observation mode)
19. ✅ Performance Max not cannibalizing Search
20. ✅ Monthly spend pacing within 5% of budget

## Scoring Methodology

### Dimension Weights

| Dimension | Weight | Checks |
|-----------|--------|--------|
| Keyword Health | 20% | 35 checks |
| Campaign Structure | 15% | 25 checks |
| Quality Score | 15% | 20 checks |
| Conversion Tracking | 15% | 25 checks |
| Bidding & Budget | 15% | 30 checks |
| Ad Copy Quality | 10% | 25 checks |
| Extensions/Assets | 5% | 20 checks |
| Negative Keywords | 5% | 20 checks |

### Score Calculation Per Dimension

Each check within a dimension is scored:
- **Pass** = full points
- **Warning** = half points
- **Fail** = zero points
- **Critical** = negative points (drags score down)

Dimension Score = (Total Points Earned / Total Points Possible) × 100

### Composite Score

Ads Health Score = Σ (Dimension Score × Dimension Weight)

### Severity Classification

| Severity | Description | Score Impact |
|----------|-------------|-------------|
| 🔴 Critical | Immediate fix needed, major money waste | -10 to -5 points |
| 🟠 High | Significant impact on performance | 0 points (fail) |
| 🟡 Medium | Optimization opportunity | Half points |
| 🟢 Low | Minor improvement, nice-to-have | Noted but minimal impact |

## Industry Benchmarks

### Search Campaign Benchmarks

| Industry | CTR | CPC | Conv Rate | CPA |
|----------|-----|-----|-----------|-----|
| E-commerce | 2.69% | $1.16 | 2.81% | $45.27 |
| Legal | 1.35% | $6.75 | 6.98% | $86.02 |
| Real Estate | 3.71% | $2.37 | 2.47% | $116.61 |
| Healthcare | 3.27% | $2.62 | 3.36% | $78.09 |
| SaaS/Tech | 2.09% | $3.80 | 2.92% | $133.52 |
| Finance | 2.91% | $3.44 | 5.10% | $81.93 |
| Education | 3.78% | $2.40 | 3.39% | $72.70 |
| Home Services | 2.93% | $6.40 | 4.80% | $66.02 |
| Automotive | 4.00% | $2.46 | 6.03% | $33.52 |
| B2B | 2.41% | $3.33 | 3.04% | $116.13 |
| Staffing | 2.15% | $4.20 | 4.12% | $95.40 |
| Travel | 4.68% | $1.53 | 3.55% | $44.73 |

### Quality Score Benchmarks

| QS Range | Rating | Expected CPC Impact |
|----------|--------|-------------------|
| 8-10 | Excellent | -30% to -50% CPC discount |
| 7 | Good | Baseline (no adjustment) |
| 5-6 | Average | +25% to +67% CPC premium |
| 3-4 | Below Average | +100% to +200% CPC premium |
| 1-2 | Poor | +400%+ CPC premium |

## Output Files

| Command | Output File | Format |
|---------|------------|--------|
| `/ads audit` | `ads-audit-report.md` | Markdown |
| `/ads quick` | `ads-quick-check.md` | Markdown |
| `/ads report-pdf` | `ads-audit-report.pdf` | PDF with charts |
| `/ads keywords` | `ads-keyword-analysis.md` | Markdown |
| `/ads quality-score` | `ads-quality-score.md` | Markdown |

## Quality Gates

- Maximum 50 campaigns per audit run (warn at 30)
- Skip paused campaigns older than 90 days
- Respect account access limitations
- Never modify account data — read-only audit
- Flag data quality issues before scoring
