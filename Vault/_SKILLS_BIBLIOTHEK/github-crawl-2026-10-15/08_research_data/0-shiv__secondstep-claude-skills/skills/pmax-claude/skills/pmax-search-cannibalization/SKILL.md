---
name: pmax-search-cannibalization
description: "Detect Performance Max campaigns stealing branded and high-intent search traffic from dedicated Search campaigns. Identifies impression share displacement, converting term overlap, and recommends brand exclusion strategies."
allowed-tools:
  - Bash
  - Read
  - Grep
---

# PMax Search Cannibalization Skill

## Purpose

One of the most damaging and least understood PMax behaviors is search cannibalization. PMax participates in search auctions alongside your Search campaigns, and it frequently "wins" branded queries — appearing to drive conversions that your Search campaign would have captured at lower cost. This skill detects cannibalization, quantifies its impact, and provides remediation strategies.

## Trigger

Activated by `/pmax cannibalize` or as part of `/pmax audit`.

## Data Requirements

Ask the user for:
1. Search campaign performance data (impressions, clicks, conversions, cost) for last 90 days
2. PMax campaign performance data for the same period
3. Search Terms report from PMax (Insights tab or API)
4. Branded Search campaign data specifically
5. Timeline of when PMax was launched (to compare before/after)
6. Brand exclusion list configuration (if any)
7. Impression share data for branded terms

## Understanding PMax Search Cannibalization

### How It Happens

PMax competes in search auctions using this priority hierarchy:
1. **Exact match keyword in Search campaign** — Search campaign wins (theoretically)
2. **Phrase/Broad match or no matching keyword** — PMax competes via Ad Rank
3. **Shopping queries** — PMax always competes (Shopping is part of PMax inventory)

The problem: Google's "exact match priority" is imperfect. PMax frequently captures:
- Close variant searches that don't trigger exact match
- Branded searches when exact match brand keywords aren't present
- Long-tail branded queries (e.g., "brand name coupon code 2026")
- Misspellings of brand terms
- Branded queries in Shopping results (even with exact match in Search)

### Why It Matters

| Metric | Before PMax Cannibalizes | After Cannibalization |
|---|---|---|
| Branded CPC | $0.50-$1.00 | $1.50-$3.00+ |
| Branded CPA | $5-$10 | $15-$30+ |
| Branded Impression Share | 90%+ | 60-75% |
| Total conversions | X | X (same or slightly higher) |
| Total cost | Y | Y + 30-50% for same conversions |
| PMax "conversions" | Low | High (but stolen from Search) |

The net effect: You pay MORE for the SAME conversions. PMax reports look great because it's claiming credit for branded conversions, but your overall efficiency decreases.

### Typical Cannibalization Pattern

```
Month 1: PMax launches
├── Search branded conversions: 100/month
├── PMax conversions: 20/month (incremental)
├── Total: 120 conversions

Month 3: PMax learns your brand
├── Search branded conversions: 60/month (↓40%)
├── PMax conversions: 65/month (↑225%)
├── Total: 125 conversions (↑4% — marginal gain)
├── BUT: Cost increased 35% for 4% more conversions
```

## Detection Framework

### Step 1: Before/After Analysis

Compare these metrics for the 90 days before PMax launch vs. 90 days after:

| Metric | Before PMax | After PMax | Change | Flag If |
|---|---|---|---|---|
| Branded Search impressions | X | Y | Δ% | >15% decline |
| Branded Search impression share | X% | Y% | Δ% | >10pt decline |
| Branded Search conversions | X | Y | Δ% | >20% decline |
| Branded Search CPC | $X | $Y | Δ% | >25% increase |
| Total branded conversions (Search + PMax) | X | Y | Δ% | <10% increase |
| Total branded cost | $X | $Y | Δ% | >20% increase |

**Cannibalization confirmed if**: Branded Search metrics declined while PMax shows "conversions" on branded terms, AND total branded volume didn't increase proportionally.

### Step 2: Search Terms Overlap Analysis

Extract PMax search terms (from Insights > Search Terms or the API) and compare against Search campaign keywords:

1. **Exact brand matches**: PMax serving on your exact brand name
2. **Brand + modifier**: "brand name reviews", "brand name pricing"
3. **Brand + product**: "brand name [product category]"
4. **Brand misspellings**: Common typos of your brand
5. **Competitor brand + your brand**: Comparison searches

For each overlapping term:
- Which campaign is getting the impressions?
- Which campaign has higher CPA for that term?
- Is PMax CPA higher than Search CPA for the same query?

### Step 3: Impression Share Displacement

Check Search impression share trends:

```
Branded Exact Match Impression Share:
  Before PMax: 95%
  After PMax: 72%
  Lost to PMax: ~23%

Lost IS (Budget): Unchanged → Not a budget issue
Lost IS (Rank): Increased → PMax outranking your own Search ads
```

If "Lost IS (Rank)" increased after PMax launch, PMax is outbidding your own Search campaigns.

### Step 4: Incremental Lift Test

The gold standard for detecting cannibalization: run a geo-based incrementality test.

1. Select 2-4 geographic regions with similar performance profiles
2. In test regions: Pause PMax for 2-4 weeks
3. In control regions: Keep PMax running
4. Compare:
   - Did Search campaign conversions increase in test regions?
   - Did total conversions decrease in test regions?
   - If Search absorbed PMax conversions → cannibalization confirmed
   - If total conversions dropped → PMax was providing incremental value

### Step 5: Channel Breakdown Analysis

PMax doesn't report channel-level data natively. Estimate using:

1. **Insights tab**: Shows estimated channel split (Search, Shopping, Display, YouTube, etc.)
2. **Placement reports**: Shows which placements PMax used
3. **Search terms report**: Shows search queries PMax matched on
4. **Scripts/API**: Third-party scripts can extract more granular data

Key question: What percentage of PMax conversions come from Search placements vs. other channels?
- If >60% from Search → high cannibalization risk
- If <30% from Search → PMax providing genuine cross-channel value

## Cannibalization Risk Score

### Risk Levels

| Risk Level | Score | Criteria |
|---|---|---|
| **Critical** | 0-25 | Branded Search dropped >30%, PMax CPA higher than Search CPA, no brand exclusions |
| **High** | 26-50 | Branded Search dropped 15-30%, significant term overlap, PMax taking >40% of branded traffic |
| **Moderate** | 51-70 | Some branded overlap detected, <15% impression share shift, mixed CPA comparison |
| **Low** | 71-85 | Minimal overlap, brand exclusions in place, PMax primarily non-search channels |
| **None** | 86-100 | Brand exclusions active, no overlap detected, PMax demonstrably incremental |

## Remediation Strategies

### Strategy 1: Brand Exclusions (Recommended First Step)

Google now allows brand exclusions at the campaign level for PMax:

1. **Navigate**: Campaign Settings > Brand Safety > Brand Restrictions
2. **Add your brand**: Include your brand name and common variations
3. **Effect**: PMax will not serve on searches that Google identifies as branded
4. **Limitation**: Google's brand detection isn't perfect — misspellings and long-tail branded queries may still leak through

### Strategy 2: Account-Level Negative Keywords

As of 2024, Google allows account-level negative keywords that apply to PMax:

1. **Navigate**: Tools & Settings > Account-level Negative Keywords
2. **Add**: Your brand name, brand variations, brand misspellings
3. **Effect**: PMax cannot serve on these terms at all
4. **Warning**: This is aggressive — it blocks ALL brand presence in PMax including Shopping

### Strategy 3: Exact Match Brand Campaign

Ensure you have a dedicated branded Search campaign with:
- Exact match keywords for brand terms
- High bids (ensure you win the auction over PMax)
- Maximize impression share bidding strategy
- Goal: 95%+ impression share on brand terms

### Strategy 4: Asset Group Segmentation

Create separate asset groups for:
- Non-branded (prospecting) — broad audience signals
- Branded (if you want PMax to handle some branded traffic) — brand-focused signals

### Strategy 5: Budget Isolation

If PMax is spending too much on branded search:
- Reduce PMax budget
- Increase Search brand campaign budget
- Monitor if total conversions remain stable (confirming cannibalization)

## Scoring Rubric (0-100)

Higher score = lower cannibalization risk.

| Criteria | Points | Condition |
|---|---|---|
| Brand exclusions configured | 20 | Active = 20pts, not configured = 0pts |
| Branded Search impression share stable | 20 | <5% change = 20pts, 5-15% = 10pts, >15% = 0pts |
| PMax search terms don't contain brand | 20 | No brand terms = 20pts, some = 10pts, many = 0pts |
| PMax CPA vs Search CPA for overlapping terms | 15 | PMax lower = 15pts, similar = 8pts, higher = 0pts |
| Incremental lift evidence | 15 | Test confirms incremental = 15pts, no test = 5pts, test shows cannibalization = 0pts |
| Total branded conversion volume stable/growing | 10 | Growing = 10pts, stable = 7pts, declining = 0pts |

## Output Format

```
## Search Cannibalization Audit Results

### Cannibalization Risk Score: XX/100
### Risk Level: [Critical/High/Moderate/Low/None]

### Before/After Analysis
| Metric | Before PMax | After PMax | Change | Flag |
|---|---|---|---|---|
| Branded impressions | X | Y | Δ% | [flag] |
| Branded impression share | X% | Y% | Δ% | [flag] |
| Branded conversions | X | Y | Δ% | [flag] |
| Branded CPC | $X | $Y | Δ% | [flag] |

### Overlapping Search Terms
| Term | PMax Impressions | Search Impressions | PMax CPA | Search CPA |
|---|---|---|---|---|
| [term] | X | Y | $X | $Y |

### Brand Exclusion Status
- Campaign-level brand exclusions: [Active/Not configured]
- Account-level negative keywords: [Active/Not configured]
- Branded Search campaign exists: [Yes/No]
- Branded Search impression share: X%

### Estimated Cannibalization Impact
- Estimated branded conversions stolen by PMax: X/month
- Estimated excess cost from cannibalization: $X/month
- Estimated CPA inflation: X%

### Critical Issues
- [List findings]

### Remediation Plan
1. [Prioritized action items with expected impact]
```
