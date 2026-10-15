# Meta Audience Overlap Audit

## Command
`/meta audiences`

## Description
Analyzes audience overlap between ad sets, evaluates exclusion strategy, assesses funnel-based segmentation (prospecting vs retargeting vs retention), validates lookalike audience quality, and checks custom audience freshness. 68% of Meta ad accounts have audience overlap above 30%, causing self-competition and inflated costs.

## Why Audience Overlap Matters

When two or more ad sets target overlapping audiences, they compete against each other in Meta's auction:

- **Self-bidding**: You bid against yourself, driving up CPMs by 15-30%
- **Cannibalized delivery**: Budget splits unpredictably between competing ad sets
- **Learning phase disruption**: Overlapping ad sets steal conversions from each other, preventing either from exiting learning phase
- **Inconsistent attribution**: The same conversion may be attributed to different ad sets depending on auction timing
- **Budget waste**: Estimated 10-20% of budget is wasted on self-competition in accounts with high overlap

## Audit Checklist (30 Points)

### 1. Audience Overlap Analysis (8 points)

- [ ] **Overlap Matrix**: Build pairwise overlap matrix for all active ad sets
- [ ] **Overlap Threshold**: Flag any audience pair with > 30% overlap
- [ ] **Critical Overlap**: Identify pairs with > 50% overlap (should be consolidated)
- [ ] **Overlap by Campaign Objective**: Separate analysis for prospecting vs retargeting
- [ ] **Overlap with Exclusions Applied**: Re-check overlap after accounting for exclusions
- [ ] **Total Addressable Audience**: Calculate unduplicated reach across all active ad sets
- [ ] **Audience Fragmentation Score**: Number of ad sets / unique audience segments (lower = better)
- [ ] **Meta Audience Overlap Tool**: Reference results from Ads Manager > Audiences > Overlap

### 2. Exclusion Strategy (6 points)

Proper exclusion strategy prevents overlap and ensures clean funnel segmentation.

- [ ] **Prospecting Excludes Customers**: Active customer lists excluded from prospecting campaigns
- [ ] **Prospecting Excludes Retargeting**: Website visitors excluded from cold prospecting
- [ ] **Retargeting Excludes Converters**: Recent purchasers/leads excluded from retargeting
- [ ] **Lookalike Excludes Custom Audiences**: Lookalike audiences exclude their source audiences
- [ ] **Cross-Campaign Exclusions**: Campaigns targeting similar objectives exclude each other's audiences
- [ ] **Exclusion Freshness**: Exclusion lists are auto-updating (not static uploads from 6 months ago)

**Recommended Exclusion Framework:**
```
PROSPECTING campaigns exclude:
  - All website visitors (180 days)
  - All customer lists
  - All engaged users (page, Instagram)
  - All past purchasers (540 days)

RETARGETING campaigns exclude:
  - Past purchasers (30-90 days)
  - Active subscribers
  - Current leads in pipeline

RETENTION campaigns exclude:
  - Churned customers (handled separately)
  - Non-purchasers
```

### 3. Funnel-Based Segmentation (6 points)

- [ ] **Clear Funnel Stages**: Account has distinct prospecting, retargeting, and retention campaigns
- [ ] **Budget Allocation by Funnel**: Typical healthy split: 60-70% prospecting, 20-30% retargeting, 5-10% retention
- [ ] **Prospecting Audiences**: Using interest-based, lookalike, or broad targeting (not retargeting pools)
- [ ] **Retargeting Windows**: Segmented by recency (1-3 days, 3-7 days, 7-30 days) with different messaging
- [ ] **Retention Audiences**: Customer lists segmented by value (high LTV, at-risk, lapsed)
- [ ] **Cross-Funnel Exclusions**: Each funnel stage properly excludes audiences from other stages

### 4. Lookalike Audience Quality (5 points)

Lookalike audiences are Meta's most powerful prospecting tool, but quality varies dramatically.

| Lookalike % | Audience Size (US) | Best For |
|-------------|-------------------|----------|
| 1% | ~2.3M | Highest quality, lowest reach |
| 2-3% | 4.6M-6.9M | Balance of quality and scale |
| 5% | ~11.5M | Broader reach, moderate quality |
| 10% | ~23M | Awareness campaigns only |

- [ ] **Source Audience Size**: Minimum 1,000 people in source (optimal: 5,000-50,000)
- [ ] **Source Audience Quality**: Based on high-value customers, not all website visitors
- [ ] **Lookalike Percentage**: Using 1-3% for conversion campaigns (not 10%)
- [ ] **Multiple Lookalike Sources**: Testing lookalikes from different source audiences (purchasers, high-LTV, leads)
- [ ] **Lookalike Refresh**: Source audiences are updating regularly (not static one-time uploads)

### 5. Custom Audience Freshness (5 points)

Custom audiences go stale quickly. A customer list from 6 months ago has significantly lower match rates.

- [ ] **Customer List Upload Date**: When was each customer list last uploaded/refreshed?
- [ ] **Auto-Sync Enabled**: Is CRM-to-Meta sync automated (via partner integration or CAPI)?
- [ ] **Website Custom Audiences**: Using appropriate lookback windows (not all "180 days")
- [ ] **Engagement Audiences**: Video viewers, page engagers, IG engagers — appropriate windows set
- [ ] **Audience Size Trends**: Are key audiences growing or shrinking? (Shrinking = stale data or narrowing targeting)

## Overlap Scoring Methodology

| Overlap Level | Score Impact | Action Required |
|--------------|-------------|-----------------|
| 0-10% | No penalty | Healthy separation |
| 10-20% | Minor penalty | Monitor, consider exclusions |
| 20-30% | Moderate penalty | Add exclusions between audiences |
| 30-50% | Significant penalty | Consolidate or restructure |
| > 50% | Critical penalty | Merge ad sets immediately |

## Common Issues & Fixes

### Issue: Prospecting and Retargeting Audiences Overlap 40%+
**Symptom**: Cold prospecting campaigns show high frequency and low reach
**Root Cause**: No exclusions applied — website visitors seeing both prospecting and retargeting ads
**Fix**: Add website visitor exclusion (30-180 days) to all prospecting campaigns.

### Issue: Multiple Lookalikes Competing
**Symptom**: Three 1% lookalikes from similar sources have 60%+ overlap
**Root Cause**: Source audiences are too similar (e.g., "all purchasers" vs "recent purchasers")
**Fix**: Consolidate into one campaign using the highest-value source audience. Test other sources in separate time windows.

### Issue: Stale Customer List
**Symptom**: Customer list audience shows declining match rate (was 70%, now 45%)
**Root Cause**: Customer list uploaded 8 months ago, no auto-refresh
**Fix**: Set up automated CRM sync via Meta's partner integrations or schedule monthly manual uploads.

### Issue: No Funnel Segmentation
**Symptom**: Single campaign targets everyone — cold, warm, and existing customers
**Root Cause**: Account was set up without funnel strategy
**Fix**: Restructure into 3 campaign tiers (Prospecting, Retargeting, Retention) with proper exclusions.

## Output Format

```
## Audience Overlap Audit Results

**Score: XX/100** (Grade: X)
**Active Audiences: XX**
**Overlap Pairs > 30%: XX**
**Exclusion Coverage: XX%**
**Funnel Segmentation: [Yes/Partial/No]**

### Overlap Matrix (Top Pairs)
| Audience A | Audience B | Overlap % | Action |
|-----------|-----------|-----------|--------|
| Lookalike 1% Purchasers | Interest: Fashion | 42% | Add exclusions |
| Retargeting 30d | Retargeting 7d | 100% | Nest properly |
| Cold - Interest A | Cold - Interest B | 35% | Consolidate |

### Critical Findings (P0)
- [e.g., Prospecting and retargeting overlap 45% — no exclusions configured]

### Recommendations
1. [Action item — e.g., Add 180-day website visitor exclusion to all prospecting]
2. [Action item — e.g., Merge overlapping lookalike audiences]
```
