---
name: audit-bidding
description: Evaluates bid strategy selection, learning phase status, portfolio vs standard bidding, target CPA/ROAS analysis, bid adjustment optimization, auction insights competitiveness, and impression share breakdown across all campaigns.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Bidding Strategy Audit

## Overview

Bid strategy is the single largest lever in Google Ads performance. The wrong strategy or misconfigured targets can waste 30-60% of budget. This audit evaluates whether each campaign uses the optimal bidding approach, whether targets are realistic, whether the algorithm has enough data to optimize, and whether manual adjustments are being used appropriately alongside automated bidding.

**Key principle:** Smart bidding (tCPA, tROAS, Max Conversions, Max Conv Value) requires sufficient conversion volume (minimum 15-30 conversions per month per campaign) and accurate conversion tracking to function properly.

## Audit Checks (30 Total)

### Bid Strategy Identification & Fit (6 checks)

**Check 1: Bid Strategy Appropriateness per Campaign**
- Pass: Each campaign's bid strategy matches its goal and data volume
- Fail: Mismatched strategies (e.g., tROAS on a lead gen campaign with no revenue values, or Max Conversions on a brand awareness campaign)
- Scoring: 6 points
- Decision framework:
  - < 15 conversions/month → Manual CPC or Maximize Clicks (with cap)
  - 15-30 conversions/month → Max Conversions (no target initially)
  - 30+ conversions/month → tCPA or tROAS
  - 50+ conversions/month → tROAS (if value tracking exists)

**Check 2: Conversion Volume Sufficiency**
- Pass: Every campaign using smart bidding has 15+ conversions in the last 30 days
- Fail: Smart bidding campaigns with < 15 conversions/month (algorithm cannot optimize reliably)
- Scoring: 6 points
- Benchmark: Google recommends 30+ conversions/month for tCPA; 50+ for tROAS

**Check 3: Bid Strategy Consistency Across Similar Campaigns**
- Pass: Similar campaigns (same goal, same funnel stage) use the same bid strategy
- Fail: Inconsistent strategies across similar campaigns without documented reasoning
- Scoring: 3 points

**Check 4: Manual CPC Justification**
- Pass: If Manual CPC is used, there is a clear reason (low volume, new campaign, testing phase)
- Fail: Manual CPC on campaigns with sufficient conversion volume to use smart bidding
- Scoring: 4 points
- Note: Enhanced CPC (eCPC) is deprecated for Search — flag if still in use

**Check 5: Maximize Clicks with Bid Cap**
- Pass: All Max Clicks campaigns have a maximum CPC bid cap set
- Fail: Max Clicks without bid cap (Google will spend aggressively, often at inflated CPCs)
- Scoring: 4 points
- Benchmark: Bid cap should be set at 1.5-2x the average CPC you'd expect for the keywords

**Check 6: Bid Strategy Change History**
- Pass: Bid strategy changes are infrequent (not more than once per 2-3 weeks) to allow learning
- Fail: Frequent bid strategy changes (weekly or more) preventing algorithm learning
- Scoring: 3 points

### Learning Phase Management (4 checks)

**Check 7: Learning Phase Status**
- Pass: No campaigns currently stuck in "Learning" for more than 14 days
- Fail: Campaigns in "Learning" status for 14+ days (indicates insufficient volume or too many changes)
- Scoring: 5 points
- Benchmark: Learning phase should complete in 7-14 days with adequate conversion volume

**Check 8: Learning Phase Triggers**
- Pass: No unnecessary changes triggering repeated learning phases (bid target changes > 15%, budget changes > 20%, conversion action changes, ad group additions)
- Fail: Multiple learning phase resets in 30 days from unnecessary changes
- Scoring: 4 points

**Check 9: "Learning (limited)" Status**
- Pass: No campaigns showing "Learning (limited)" — which means not enough conversions to exit learning
- Fail: Campaigns stuck in "Learning (limited)" with no remediation plan
- Scoring: 4 points
- Fix: Consolidate campaigns, broaden targeting, use micro-conversions, or switch to simpler bid strategy

**Check 10: Post-Learning Performance Validation**
- Pass: Campaigns that exited learning phase are meeting or approaching their targets within 20%
- Fail: Campaigns operating well outside targets after learning phase completion
- Scoring: 3 points

### Target Analysis (5 checks)

**Check 11: tCPA Target vs Actual CPA**
- Pass: Actual CPA is within 20% of tCPA target
- Fail: Actual CPA > 30% above tCPA (target too aggressive) or > 30% below (target too conservative, leaving volume on table)
- Scoring: 5 points
- Benchmark: Target should be set at or slightly above (10-15%) the historical 30-day average CPA

**Check 12: tROAS Target vs Actual ROAS**
- Pass: Actual ROAS is within 20% of tROAS target
- Fail: Significant deviation (target too aggressive limits spend; too conservative wastes margin)
- Scoring: 5 points

**Check 13: Target Setting Methodology**
- Pass: Targets based on historical performance data (last 30-60 day average, adjusted for business goals)
- Fail: Arbitrary targets not grounded in data (e.g., "I want $10 CPA" when historical is $40)
- Scoring: 4 points

**Check 14: Target Adjustment Cadence**
- Pass: Targets adjusted gradually (10-15% increments, no more than every 2 weeks)
- Fail: Large target changes (> 20%) or frequent changes (more than weekly)
- Scoring: 3 points

**Check 15: Portfolio Bid Strategy Targets**
- Pass: If portfolio strategies are used, the target accounts for the combined performance of all included campaigns
- Fail: Portfolio strategy grouping dissimilar campaigns with very different CPAs
- Scoring: 3 points

### Portfolio vs Standard Bidding (3 checks)

**Check 16: Portfolio Strategy Usage Assessment**
- Pass: Portfolio strategies used appropriately to pool conversion data from related campaigns (especially campaigns with < 30 conversions individually)
- Fail: Low-volume campaigns using individual bid strategies when they could benefit from portfolio pooling
- Scoring: 4 points

**Check 17: Portfolio Strategy Grouping Logic**
- Pass: Portfolio strategies group campaigns with similar CPAs, conversion types, and business objectives
- Fail: Portfolio groups campaigns with vastly different CPAs (e.g., brand at $5 CPA with non-brand at $50 CPA)
- Scoring: 3 points

**Check 18: Shared Budget + Portfolio Interaction**
- Pass: Shared budgets and portfolio strategies are used intentionally and not conflicting
- Fail: Conflicting shared budget and portfolio strategy configurations
- Scoring: 2 points

### Bid Adjustment Analysis (5 checks)

**Check 19: Device Bid Adjustments with Smart Bidding**
- Pass: If using smart bidding, device bid adjustments are understood to be largely ignored (except -100% to exclude a device)
- Fail: Setting device bid adjustments on smart bidding campaigns expecting them to work (they don't, except -100%)
- Scoring: 3 points

**Check 20: Location Bid Adjustments**
- Pass: Location bid adjustments reflect geographic performance data; manual CPC campaigns have active geo adjustments
- Fail: No location adjustments despite significant geographic performance variation
- Scoring: 3 points

**Check 21: Audience Bid Adjustments**
- Pass: Audience bid adjustments set for observation-mode audiences based on performance (RLSA, in-market)
- Fail: Audiences added in observation mode but no bid adjustments applied
- Scoring: 3 points

**Check 22: Time-of-Day Bid Adjustments**
- Pass: Ad schedule bid adjustments align with conversion rate patterns by hour/day
- Fail: Flat bids despite significant time-based performance variation
- Scoring: 3 points

**Check 23: Bid Adjustment Conflicts**
- Pass: Bid adjustments don't stack to extreme values (e.g., +50% device + 50% location + 30% audience = 2.9x base bid)
- Fail: Stacked bid adjustments creating unexpectedly high or low bids
- Scoring: 2 points

### Auction Insights & Competitive Position (4 checks)

**Check 24: Impression Share Analysis**
- Pass: Top campaigns have 60%+ impression share; account overall has 40%+ for priority terms
- Fail: Priority campaigns below 30% impression share
- Scoring: 4 points
- Benchmark: Brand campaigns: 90%+ IS target | Non-brand: 40-70% IS is typical

**Check 25: Impression Share Lost to Rank vs Budget**
- Pass: IS lost primarily to budget (solvable by increasing budget) rather than rank (needs QS/bid improvement)
- Fail: > 30% IS lost to rank on priority campaigns (indicates QS or bid problems)
- Scoring: 4 points

**Check 26: Auction Insights Competitor Trends**
- Pass: Competitive position (overlap rate, outranking share) is stable or improving
- Fail: Significant competitive position decline over last 90 days
- Scoring: 3 points

**Check 27: Top of Page Rate**
- Pass: High-intent non-brand campaigns achieving 50%+ top-of-page rate (abs)
- Fail: Key campaigns below 30% top-of-page rate
- Scoring: 3 points
- Benchmark: Brand: 80%+ absolute top IS | Non-brand: 40-60% top IS is healthy

### Max Conversions vs Max Conv Value (3 checks)

**Check 28: Value-Based Bidding Assessment**
- Pass: If conversion values vary (e-commerce, or lead gen with VBB), Max Conv Value / tROAS is used
- Fail: Using Max Conversions when conversion values are tracked and vary significantly
- Scoring: 4 points

**Check 29: Value-Based Bidding Data Quality**
- Pass: Conversion values are accurate and meaningful (actual revenue or lead quality scores)
- Fail: Placeholder or inaccurate conversion values feeding into VBB
- Scoring: 3 points

**Check 30: Micro-Conversion Strategy**
- Pass: If primary conversion volume is low, micro-conversions (form starts, page views, engaged sessions) supplement bidding signals
- Fail: Smart bidding with < 10 primary conversions/month and no micro-conversion strategy
- Scoring: 3 points

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Optimal bidding setup maximizing ROAS/efficiency |
| 75-89 | Good | Well-configured bidding with minor optimization needed |
| 60-74 | Average | Bidding is functional but leaving performance on the table |
| 40-59 | Below Average | Significant bidding issues impacting performance |
| 0-39 | Poor | Bidding strategy requires fundamental restructuring |

**Total possible points: 110** (normalized to 100-point scale)

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Campaigns in learning | 0 | 0-1 | 2-3 | 4+ |
| tCPA variance (actual vs target) | < 10% | 10-20% | 20-35% | > 35% |
| Impression share (brand) | > 90% | 75-90% | 50-75% | < 50% |
| Impression share (non-brand) | > 60% | 40-60% | 25-40% | < 25% |
| IS lost to rank | < 10% | 10-20% | 20-35% | > 35% |
| IS lost to budget | < 10% | 10-25% | 25-40% | > 40% |

## Output Format

```markdown
## Bidding Strategy Audit Results

**Overall Score: [X]/100 — [Rating]**

### Bid Strategy Map
| Campaign | Strategy | Target | Actual | Conv/30d | Status |
|----------|----------|--------|--------|----------|--------|
| ... | tCPA | $30 | $35 | 45 | Eligible |

### Learning Phase Status
| Campaign | Status | Days in Learning | Issue |
|----------|--------|-----------------|-------|
| ... | ... | ... | ... |

### Impression Share Analysis
| Campaign | IS % | Lost to Rank | Lost to Budget | Top of Page |
|----------|------|-------------|---------------|-------------|
| ... | ... | ... | ... | ... |

### Critical Findings
1. ...

### Recommendations
1. [Immediate changes]
2. [Strategy shifts]
3. [Target adjustments]
```
