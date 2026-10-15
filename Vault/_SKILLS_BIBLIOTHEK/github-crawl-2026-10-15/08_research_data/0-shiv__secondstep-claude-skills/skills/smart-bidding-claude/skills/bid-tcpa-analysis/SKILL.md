---
name: bid-tcpa-analysis
description: Deep dive analysis of Target CPA bidding campaigns — actual vs target CPA comparison, conversion volume sufficiency validation, target aggressiveness assessment, and tCPA ratcheting strategy development.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Target CPA (tCPA) Deep Dive Analysis

You are performing a specialized analysis of all campaigns using Target CPA bidding. tCPA is the most commonly used Smart Bidding strategy and the most frequently misconfigured. Your goal is to evaluate target accuracy, volume sufficiency, CPA stability, and develop a ratcheting strategy for gradual target optimization.

## How tCPA Actually Works (Internal Mechanics)

Understanding the algorithm helps diagnose problems:

1. **Auction-time bidding**: Google evaluates each auction individually using signals like device, location, time of day, query intent, audience membership, browser, OS, and hundreds of contextual signals.

2. **CPA is an AVERAGE target, not a maximum**: Google will bid above your tCPA for auctions it predicts are high-converting and below for low-probability auctions. Some individual conversions will cost 2-3x your target. This is normal.

3. **The algorithm needs conversion signal**: With fewer than 30 conversions/month, the algorithm is making predictions with insufficient data. It becomes conservative (underspends) or erratic.

4. **Learning period behavior**: During the first 7-14 days after a tCPA change, the algorithm is recalibrating. Performance may temporarily worsen. This is NOT a reason to change the target again.

5. **Budget interaction**: If your daily budget is less than 5x your tCPA, Smart Bidding has limited room to optimize across the day. Google recommends budget >= 10x tCPA for optimal performance.

## Analysis Steps

### Step 1: tCPA Campaign Inventory

For each tCPA campaign, collect:

| Metric | Source | Why It Matters |
|--------|--------|---------------|
| Target CPA | Campaign settings | The goal Smart Bidding optimizes toward |
| Actual CPA (7d) | Campaign stats | Recent trend — is CPA moving toward or away from target? |
| Actual CPA (30d) | Campaign stats | Stable baseline for target evaluation |
| Actual CPA (90d) | Campaign stats | Long-term average — accounts for seasonality |
| Conversions (30d) | Campaign stats | Volume sufficiency check |
| Conversion rate | Campaign stats | Low CVR + high CPC = structural CPA problem |
| Avg CPC | Campaign stats | Input cost — tCPA can't go below CPC / CVR |
| Search Impr Share | Campaign stats | Is the target limiting volume? |
| Search Lost IS (Budget) | Campaign stats | Budget-limited = different problem than target-limited |
| Search Lost IS (Rank) | Campaign stats | Rank-limited = target may be too low for auction |
| Daily budget | Campaign settings | Budget-to-target ratio check |
| Conversion action | Campaign settings | What counts as a conversion? |
| Attribution model | Campaign settings | DDA vs last-click affects conversion counts |
| Last target change | Change history | How recently was the target modified? |
| Learning status | Campaign status | Is the campaign currently in learning? |

### Step 2: Volume Sufficiency Analysis

Evaluate whether each campaign has enough conversion data for tCPA to work effectively:

```
Conversions/Month Assessment:

50+   = EXCELLENT: Full algorithmic power. tCPA can optimize aggressively.
        The algorithm has strong signal for auction-time predictions.

30-49 = ADEQUATE: Meets Google's recommendation. tCPA will work but
        may take longer to optimize. Avoid frequent target changes.

15-29 = MARGINAL: Below recommended minimum. tCPA will be conservative
        and may underperform. Consider Max Conversions instead, or
        combine with similar campaigns in a portfolio strategy.

< 15  = INSUFFICIENT: Not enough data for meaningful optimization.
        tCPA is essentially guessing. Switch to Max Conversions or
        Manual CPC until volume builds.
```

**Volume Enhancement Options** (when volume is too low):
- Broaden keyword match types (phrase -> broad with Smart Bidding)
- Add micro-conversions as secondary conversion actions (for signal, not optimization)
- Combine low-volume campaigns into one campaign with ad groups
- Use portfolio bidding to pool volume across campaigns
- Extend conversion window (if conversions are being missed due to short window)

### Step 3: Target vs Actual CPA Assessment

Calculate the Target-to-Actual ratio and assess:

```python
ratio = target_cpa / actual_cpa_30d

if ratio < 0.60:
    severity = "CRITICAL"
    diagnosis = "Target is dangerously aggressive"
    symptoms = [
        "Campaign spending well below daily budget",
        "Impression share dropping week over week",
        "Fewer conversions than before tCPA was set",
        "Google showing 'limited by bid strategy' status"
    ]
    fix = "Raise target to 90-100% of actual CPA immediately"

elif ratio < 0.80:
    severity = "WARNING"
    diagnosis = "Target is too aggressive"
    symptoms = [
        "Budget underspend of 20-40%",
        "Conversion volume declining",
        "Higher quality but much lower quantity"
    ]
    fix = "Raise target by 15-20%, wait 2 weeks, reassess"

elif ratio < 0.90:
    severity = "MINOR"
    diagnosis = "Target is slightly aggressive"
    symptoms = [
        "Slight budget underspend",
        "Marginal volume pressure"
    ]
    fix = "Acceptable if intentional. Monitor weekly."

elif ratio <= 1.20:
    severity = "OPTIMAL"
    diagnosis = "Target is well-calibrated"
    symptoms = [
        "Budget fully utilized",
        "Stable conversion volume",
        "CPA hovering around target"
    ]
    fix = "No changes needed. Consider gradual ratcheting."

elif ratio <= 1.50:
    severity = "CONSERVATIVE"
    diagnosis = "Target is too loose"
    symptoms = [
        "CPA consistently below target",
        "Budget fully spent but at higher CPA than necessary",
        "Smart Bidding has no incentive to find cheaper conversions"
    ]
    fix = "Lower target by 10-15%, wait 2 weeks, reassess"

else:
    severity = "WARNING"
    diagnosis = "Target is far too conservative"
    symptoms = [
        "Significantly overpaying per conversion",
        "CPA well below target with no improvement trend",
        "Wasted budget on expensive clicks"
    ]
    fix = "Lower target to 110-120% of actual CPA"
```

### Step 4: CPA Stability Analysis

Evaluate CPA variance to determine if tCPA is the right strategy:

```
Weekly CPA Variance = StdDev(weekly_cpa) / Mean(weekly_cpa)

< 0.15 (15%)  = STABLE: Excellent candidate for tCPA.
0.15-0.25     = MODERATE: tCPA will work but needs wider tolerance.
0.25-0.40     = VOLATILE: tCPA may struggle. Investigate causes.
> 0.40 (40%)  = UNSTABLE: tCPA is inappropriate. Use Max Conversions
                or investigate root cause of instability.
```

**Common causes of CPA instability:**
- Mixed conversion actions (lead form + phone call + chat) with different values
- Delayed conversions extending beyond the conversion window
- Seasonal demand fluctuations
- Competitor bid changes
- Landing page issues (intermittent errors, slow load times)
- Ad copy rotation introducing high-variance creative
- Broad match keywords matching irrelevant queries

### Step 5: tCPA Ratcheting Strategy

Develop a gradual target reduction plan to improve efficiency without shocking the algorithm:

**Ratcheting Rules:**
1. Never reduce tCPA by more than 15-20% in a single change
2. Wait a minimum of 14 days between adjustments (full learning cycle)
3. Only ratchet down if the campaign achieved the current target for 2+ consecutive weeks
4. If a ratchet causes volume to drop > 25%, revert to previous target
5. Account for seasonality — don't ratchet during known high/low periods
6. Never ratchet during holidays, major promotions, or budget changes

**Ratcheting Plan Template:**

```
Current actual CPA: $50
Current target CPA: $55
Goal CPA: $40

Week 0:  Target = $55 (current, verify stable)
Week 2:  If CPA stable at/below $55 → Lower to $48 (-13%)
Week 4:  If CPA stable at/below $48 → Lower to $43 (-10%)
Week 6:  If CPA stable at/below $43 → Lower to $40 (-7%)
Week 8:  Monitor at $40. If CPA < $38, goal achieved.
         If CPA = $42-45, $40 target is a stretch — consider $42.

Total timeline: 8 weeks for $15 CPA reduction
```

### Step 6: Budget-to-Target Ratio Check

```
Ratio = Daily Budget / Target CPA

< 2x   = CRITICAL: Budget too low. Smart Bidding can't get enough
         conversions per day to learn. Increase budget or raise CPA target.

2-5x   = WARNING: Budget is tight. Smart Bidding has limited flexibility.
         May see erratic daily performance.

5-10x  = GOOD: Adequate room for Smart Bidding to operate.

10-20x = OPTIMAL: Full algorithmic flexibility. Best performance zone.

> 20x  = FINE: Large budget relative to CPA. No issues, but monitor
         for wasteful spending on low-quality conversions.
```

## Output Format

```
## tCPA Analysis Results

### Summary
- Campaigns analyzed: X
- Optimal targets: X
- Targets too aggressive: X
- Targets too conservative: X
- Insufficient volume: X

### Campaign Details
[Per-campaign analysis with target assessment]

### Ratcheting Plans
[Per-campaign ratcheting timeline where applicable]

### Volume Enhancement Recommendations
[For campaigns with insufficient conversion volume]

### Priority Actions
1. [Immediate target adjustments needed]
2. [Volume building actions]
3. [Monitoring items]
```
