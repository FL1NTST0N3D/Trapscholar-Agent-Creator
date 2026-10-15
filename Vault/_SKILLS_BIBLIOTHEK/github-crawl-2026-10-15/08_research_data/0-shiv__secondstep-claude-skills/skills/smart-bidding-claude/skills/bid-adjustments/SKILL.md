---
name: bid-adjustments
description: Bid adjustment audit — identify device, location, audience, and ad schedule adjustments that conflict with Smart Bidding, detect redundant adjustments ignored by automated strategies, and clean up adjustment hygiene.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Bid Adjustment Audit

You are auditing bid adjustments across a Google Ads account to identify conflicts with Smart Bidding. This is one of the most misunderstood areas of Google Ads: most advertisers set bid adjustments without realizing Smart Bidding ignores nearly all of them. Your goal is to identify redundant adjustments, find the few that still work with automation, and clean up adjustment hygiene.

## The Critical Rule: Smart Bidding Ignores Most Bid Adjustments

When a campaign uses Smart Bidding (tCPA, tROAS, Max Conversions, Max Conv Value), the algorithm handles auction-time bid optimization using its own signals. Manual bid adjustments are redundant because the algorithm already accounts for device, location, time of day, and audience signals.

**What Smart Bidding IGNORES (adjustments have no effect):**
- Location bid adjustments (e.g., +20% for California)
- Ad schedule bid adjustments (e.g., +15% during business hours)
- Audience bid adjustments in OBSERVATION mode (e.g., +25% for in-market)
- Age, gender, household income bid adjustments
- Interaction bid adjustments
- Placement bid adjustments (Display)
- Topic bid adjustments (Display)
- Content bid adjustments

**What Smart Bidding RESPECTS (these still work):**
- **Device bid adjustment of -100%**: This completely excludes a device (mobile, desktop, or tablet). Smart Bidding respects this because it's a targeting exclusion, not a bid modifier.
- **Audience bid adjustments in TARGETING mode**: When an audience is set to "Targeting" (not "Observation"), bid adjustments may influence strategy behavior (though the algorithm still has latitude).

**The Exception: Manual CPC and eCPC**
Manual CPC and Enhanced CPC campaigns DO use bid adjustments. All adjustments are applied as multipliers to the base keyword bid.

## Analysis Steps

### Step 1: Inventory All Bid Adjustments

Scan every campaign and catalog all active bid adjustments:

| Campaign | Strategy | Adjustment Type | Target | Modifier | Status |
|----------|----------|----------------|--------|----------|--------|
| Campaign A | tCPA | Device - Mobile | Mobile | -30% | IGNORED |
| Campaign A | tCPA | Device - Mobile | Mobile | -100% | ACTIVE |
| Campaign B | tCPA | Location | California | +20% | IGNORED |
| Campaign C | Manual CPC | Ad Schedule | Mon 9am-5pm | +15% | ACTIVE |

For each adjustment, mark whether it is ACTIVE (affects bidding) or IGNORED (Smart Bidding overrides it).

### Step 2: Identify Conflicting Adjustments

Find adjustments that create confusion or false confidence:

**Conflict Type 1: Adjustments on Smart Bidding Campaigns**
```
Problem: Advertiser set +30% for California on a tCPA campaign.
Reality: Smart Bidding ignores this. The +30% shows in settings
         but has zero effect on bids.
Risk: Advertiser believes they're bidding 30% more in California
      and makes strategy decisions based on this false assumption.
Fix: Remove the adjustment. Add a note that Smart Bidding handles
     location-based bid optimization automatically.
```

**Conflict Type 2: Stacked Adjustments (Manual/eCPC)**
```
Problem: Campaign has +20% mobile, +15% California, +10% in-market audience,
         +25% Monday 9-5pm. These MULTIPLY, not add.
Actual modifier: 1.20 * 1.15 * 1.10 * 1.25 = 1.90x (90% bid increase)
Risk: Keyword with $2 CPC becomes $3.80 for a California mobile user
      in the in-market audience on Monday morning. Often unintentional.
Fix: Review stacked multiplier effect. Reduce adjustments to achieve
     the intended combined modifier.
```

**Conflict Type 3: Counterproductive -100% Device Adjustments**
```
Problem: Campaign excludes mobile via -100% but mobile traffic converts.
Reality: -100% device is respected by Smart Bidding. You're excluding
         all mobile auctions. If mobile converts at a reasonable CPA,
         you're leaving conversions on the table.
Check: Review device-level conversion data before maintaining -100%.
Fix: Only use -100% device if that device truly does not convert or
     converts at an unacceptable CPA that can't be fixed.
```

**Conflict Type 4: Observation Audience Adjustments on Smart Bidding**
```
Problem: +50% bid adjustment on "In-Market: Auto Buyers" in observation mode
         on a tCPA campaign.
Reality: Smart Bidding ignores this. The algorithm already considers
         audience signals (and many more signals than just Google's
         audience segments).
Risk: False confidence that audience strategy is active when it's not.
Fix: Remove the bid adjustment. Keep the audience in observation mode
     for reporting insights (you can still see performance by audience),
     but understand that the adjustment percentage does nothing.
```

### Step 3: Device Strategy Assessment

Device adjustments are the most impactful because -100% is the only adjustment Smart Bidding respects:

```
For each campaign, analyze device performance:

| Device | Conv | Cost | CPA | CVR | CPC | Action |
|--------|------|------|-----|-----|-----|--------|
| Desktop | | | | | | |
| Mobile | | | | | | |
| Tablet | | | | | | |

Assessment Logic:

If Mobile CPA > 2x Desktop CPA AND Mobile Conv < 10% of total:
  Consider -100% mobile. Low volume + high cost = not worth it.

If Mobile CPA > Desktop CPA but Mobile Conv > 20% of total:
  Do NOT exclude mobile. Smart Bidding will naturally bid less
  for mobile auctions where conversion probability is lower.
  Excluding mobile would lose significant volume.

If Tablet Conv < 5% of total AND Tablet CPA > Desktop CPA:
  Consider -100% tablet. Minimal volume impact, small efficiency gain.

If Desktop is the worst performer:
  Rarely exclude desktop. Instead, investigate landing page issues
  on desktop (load time, UX, mobile-responsive site showing poorly).

IMPORTANT: -100% is binary — it's all or nothing. You can't do -50%
and expect Smart Bidding to bid 50% less on mobile. It either excludes
the device entirely (-100%) or ignores the adjustment (any other value).
```

### Step 4: Location Adjustment Audit

Location adjustments are ignored by Smart Bidding but still worth auditing for Manual CPC campaigns and for identifying targeting gaps:

```
For Smart Bidding campaigns:
- Remove all location bid adjustments (they do nothing)
- If you want to bid differently by location, create separate campaigns
  per geo with different tCPA targets instead
- Document which locations perform best/worst for strategic insight

For Manual CPC campaigns:
- Verify adjustments reflect actual performance differences
- Check for stacking issues with other adjustment types
- Ensure adjustments are based on data, not assumptions
- Recommended: Adjust only if location CPA differs by > 30% from average

Location Targeting Check:
- Are campaigns targeting "presence in" or "presence or interest in"?
- "Presence or interest in" can show ads to users anywhere who are
  SEARCHING ABOUT your target location (not physically there)
- For local businesses: always use "presence in" targeting
```

### Step 5: Ad Schedule Adjustment Audit

Ad schedule adjustments are ignored by Smart Bidding:

```
For Smart Bidding campaigns:
- Remove all ad schedule bid adjustments
- Smart Bidding's auction-time signals already include time-of-day
  and day-of-week optimization
- If you want to STOP serving during certain hours, use ad scheduling
  to exclude those times (this is targeting, not bid adjustment, and
  is respected)

For Manual CPC campaigns:
- Review hourly/day-of-week conversion data
- Verify adjustments match performance patterns
- Common issue: +20% during "business hours" when data shows
  evenings actually convert better (or vice versa)
- Consider: Is the schedule adjustment based on when conversions
  happen or when users click? These may differ for long-consideration
  purchases.

Day-Parting Analysis:
| Day/Time | Impressions | Clicks | Conv | CPA | Current Adj | Recommended |
```

### Step 6: Adjustment Cleanup Recommendations

Provide a prioritized cleanup plan:

```
Priority 1: Remove Conflicting Adjustments
- List all bid adjustments on Smart Bidding campaigns that are
  being ignored. These create false confidence.
- Removing them changes NOTHING about performance but improves
  account clarity and prevents strategic misunderstandings.

Priority 2: Evaluate -100% Device Exclusions
- Review each -100% device exclusion against actual performance data
- Remove if the excluded device converts within acceptable CPA range
- Keep if the excluded device truly doesn't convert

Priority 3: Review Manual CPC Adjustments
- Verify all active adjustments (on Manual CPC/eCPC campaigns)
  are based on performance data, not assumptions
- Calculate stacked multiplier effects
- Simplify where possible

Priority 4: Document Remaining Adjustments
- For each remaining active adjustment, document:
  - Why it exists
  - What data supports it
  - When it was last reviewed
  - When it should be reviewed next
```

## Output Format

```
## Bid Adjustment Audit Results

### Summary
- Total adjustments found: X
- Adjustments being IGNORED by Smart Bidding: X (X%)
- Active adjustments: X
- Conflicting adjustments: X
- Redundant adjustments: X

### Adjustment Inventory
[Full table of all adjustments with ACTIVE/IGNORED status]

### Conflicts Detected
[Detailed breakdown of each conflict type found]

### Device Strategy Assessment
[Per-campaign device performance and -100% evaluation]

### Cleanup Recommendations
1. [Adjustments to remove immediately (no performance impact)]
2. [Adjustments to evaluate with data (may keep or remove)]
3. [Adjustments to add (-100% device exclusions where warranted)]
4. [Manual CPC adjustments to review/update]

### Net Impact
[Estimated impact of cleanup: improved clarity, any performance changes]
```
