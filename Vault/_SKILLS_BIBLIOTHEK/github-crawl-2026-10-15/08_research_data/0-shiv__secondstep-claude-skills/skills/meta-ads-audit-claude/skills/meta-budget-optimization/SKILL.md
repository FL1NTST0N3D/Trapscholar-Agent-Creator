# Meta Budget Optimization Audit

## Command
`/meta budget`

## Description
Analyzes Campaign Budget Optimization (CBO) vs Ad Set Budget Optimization (ABO) configuration, budget distribution across ad sets, minimum budget thresholds for exiting learning phase, learning phase health across the account, and delivery optimization selection. Proper budget setup is the difference between Meta's algorithm working for you vs against you.

## Why Budget Optimization Matters

Meta's delivery algorithm needs sufficient data to optimize. Underfunded ad sets, wrong optimization events, and poor budget distribution lead to:

- **Perpetual learning phase**: Ad sets that never exit learning phase cost 30-50% more per result
- **Budget starvation**: In CBO, some ad sets get 0-5% of budget while others consume everything
- **Wrong optimization signals**: Optimizing for link clicks when you want purchases trains the algorithm for the wrong outcome
- **Bid ceiling issues**: Aggressive bid caps prevent delivery entirely during high-competition periods
- **Missed opportunities**: Insufficient budget during peak conversion windows

Accounts with properly configured budgets see **20-35% better cost per acquisition** compared to accounts with budget and delivery issues.

## Audit Checklist (25 Points)

### 1. CBO vs ABO Analysis (6 points)

Campaign Budget Optimization (CBO) gives Meta control over budget distribution. Ad Set Budget Optimization (ABO) gives the advertiser manual control.

| Factor | CBO Better | ABO Better |
|--------|-----------|-----------|
| Budget size | > $100/day per campaign | < $50/day per campaign |
| Ad set count | 3-5 ad sets | 1-2 ad sets |
| Audience similarity | Different audiences | Very different audiences |
| Testing phase | Not ideal | Better for controlled tests |
| Scale phase | Excellent | Less efficient |
| Control needed | Low control | Precise control |

- [ ] **CBO/ABO Distribution**: Document which campaigns use CBO vs ABO
- [ ] **CBO Appropriateness**: CBO campaigns have 3+ ad sets with comparable audiences
- [ ] **ABO Justification**: ABO campaigns have a clear reason (testing, very different audiences)
- [ ] **Minimum Budget per Ad Set (ABO)**: Each ad set has enough budget for 50 conversions/week
- [ ] **CBO Minimum Spend Limits**: Check if ad set minimum/maximum spend limits are set within CBO
- [ ] **Hybrid Strategy Check**: If mixing CBO and ABO, verify no overlap between campaigns

### 2. Budget Distribution Analysis (5 points)

- [ ] **CBO Distribution Check**: In CBO campaigns, identify if any ad set gets < 10% of campaign budget
- [ ] **Budget Hoarding**: Flag if one ad set in CBO consumes > 70% of campaign budget
- [ ] **Spend vs Budget Ratio**: Are campaigns spending their full daily budget? (< 70% utilization = problem)
- [ ] **Budget Pacing**: Check "Delivery" column — Accelerated vs Standard pacing review
- [ ] **Day-of-Week Patterns**: Budget utilization by day — identify if weekends are starved or overspent

### 3. Learning Phase Health (6 points)

Meta's learning phase requires approximately **50 optimization events per ad set per week** to exit.

| Learning Status | Meaning | Action |
|----------------|---------|--------|
| Active (Learning) | < 50 events in 7 days | Wait or increase budget |
| Learning Limited | Cannot reach 50 events with current budget | Increase budget or change optimization |
| Active | Exited learning phase | Healthy — do not make significant edits |

- [ ] **Learning Phase Status**: Pull status for every active ad set
- [ ] **Learning Limited Count**: How many ad sets are "Learning Limited"? (Target: 0)
- [ ] **Time in Learning**: How long has each ad set been in learning? (> 14 days = stalled)
- [ ] **Conversion Volume**: Is each ad set getting 50+ optimization events per week?
- [ ] **Edit Frequency**: Are advertisers resetting learning phase with frequent edits? (any significant edit resets learning)
- [ ] **Optimization Event Selection**: Is the optimization event achievable with the budget? (e.g., optimizing for Purchase but budget only supports 20/week)

**Significant Edits That Reset Learning Phase:**
- Bid/budget changes > 20%
- Audience changes
- Creative additions/removals
- Optimization event changes
- Pause/unpause of 7+ days

### 4. Minimum Budget Thresholds (4 points)

| Optimization Event | Min Daily Budget (Rule of Thumb) |
|-------------------|--------------------------------|
| Purchase ($50 AOV) | $50 x 50 / 7 = $357/day per ad set |
| Purchase ($100 AOV) | $100 x 50 / 7 = $714/day per ad set |
| Lead ($10 CPL) | $10 x 50 / 7 = $71/day per ad set |
| Add to Cart ($5 cost) | $5 x 50 / 7 = $36/day per ad set |
| Link Click ($1 CPC) | $1 x 50 / 7 = $7/day per ad set |

- [ ] **Budget vs Optimization Event**: Does each ad set have enough budget for 50 weekly events?
- [ ] **Underfunded Ad Sets**: Flag ad sets below minimum threshold
- [ ] **Consolidation Opportunity**: Could merging small ad sets create a properly funded one?
- [ ] **Budget Scaling Path**: Is there a clear plan for scaling budget without disrupting learning?

### 5. Delivery Optimization Selection (4 points)

- [ ] **Correct Optimization Event**: Campaigns optimizing for the right event (Purchase, not Link Clicks, for e-commerce)
- [ ] **Conversion Window**: Appropriate attribution window selected (7-day click, 1-day view is default and usually best)
- [ ] **Bid Strategy**: Cost per result goals vs bid caps vs highest volume — appropriate for each campaign's maturity
- [ ] **Delivery Type**: Standard delivery (not accelerated) for most campaigns

## Budget Health Scoring

| Score Range | Grade | What It Means |
|-------------|-------|---------------|
| 90-100 | A+ | Budget structure maximizes Meta's algorithm |
| 80-89 | A | Minor optimization opportunities |
| 70-79 | B | Some ad sets underfunded or stuck in learning |
| 60-69 | C | Significant budget structure issues |
| 40-59 | D | Multiple ad sets learning limited, poor distribution |
| 0-39 | F | Budget structure actively working against optimization |

## Common Issues & Fixes

### Issue: 80% of Ad Sets "Learning Limited"
**Symptom**: Most ad sets never exit learning phase
**Root Cause**: Budget too low for the optimization event, or too many ad sets splitting budget
**Fix**: Consolidate to fewer ad sets (3-5 per campaign), increase budget, or switch optimization to a more frequent event (AddToCart instead of Purchase) temporarily.

### Issue: CBO Hoarding — One Ad Set Gets Everything
**Symptom**: One ad set consumes 90% of CBO budget, others are starved
**Root Cause**: Meta concentrates spend on the ad set with highest estimated conversion rate
**Fix**: Set minimum spend limits on underperforming ad sets, or move to ABO if audiences need equal testing.

### Issue: Budget Utilization Below 50%
**Symptom**: Campaign has $500/day budget but only spends $200
**Root Cause**: Audience too narrow, bid cap too low, or creative quality too poor for delivery
**Fix**: Widen audience targeting, remove or increase bid caps, refresh creative.

### Issue: Constant Learning Phase Resets
**Symptom**: Ad sets keep returning to learning phase every week
**Root Cause**: Advertiser making frequent significant edits (budget changes, audience tweaks, creative swaps)
**Fix**: Batch all changes together, make changes no more than once per week, keep budget changes < 20%.

## Output Format

```
## Budget Optimization Audit Results

**Score: XX/100** (Grade: X)
**CBO Campaigns: X | ABO Campaigns: X**
**Learning Phase: X Active, X Limited, X Healthy**
**Budget Utilization: XX%**

### Budget Health by Campaign
| Campaign | Type | Budget | Spend | Util % | Learning Status |
|----------|------|--------|-------|--------|----------------|
| Campaign A | CBO | $500 | $480 | 96% | Active |
| Campaign B | ABO | $100 | $45 | 45% | Learning Limited |

### Critical Findings (P0)
- [e.g., 5/8 ad sets are Learning Limited — budget too low for Purchase optimization]

### Recommendations
1. [Action item — e.g., Consolidate 6 ad sets into 3 to meet minimum budget thresholds]
```
