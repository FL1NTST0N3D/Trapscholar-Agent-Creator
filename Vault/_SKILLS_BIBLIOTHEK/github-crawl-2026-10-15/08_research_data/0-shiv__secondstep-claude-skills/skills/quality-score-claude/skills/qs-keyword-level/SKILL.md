# QS Keyword-Level Audit

## Command
`/qs keywords`

## Purpose

Perform a per-keyword Quality Score audit across the entire account. Sort keywords by their potential dollar savings (spend multiplied by QS gap), group findings by ad group and campaign, and produce a prioritized fix list that maximizes ROI on optimization effort.

## The Spend x QS Gap Framework

Not all low-QS keywords deserve equal attention. The priority metric is:

```
Priority Score = Monthly Spend × (10 - Current QS) × CPC_penalty_multiplier
```

This formula ranks keywords by how much money is being wasted. A QS 3 keyword spending $3,000/month ranks higher than a QS 1 keyword spending $50/month, because the absolute dollar waste is larger.

### CPC Penalty Multiplier Lookup

| Current QS | CPC Penalty vs QS 10 | Multiplier for Priority Calc |
|:--:|:--:|:--:|
| 1 | +400% | 5.0 |
| 2 | +300% | 4.0 |
| 3 | +200% | 3.0 |
| 4 | +100% | 2.0 |
| 5 | +67% | 1.67 |
| 6 | +25% | 1.25 |
| 7 | Baseline | 1.0 |
| 8 | -17% | 0.83 |
| 9 | -33% | 0.67 |

## Audit Methodology

### Step 1: Data Extraction

Extract the full keyword report with these columns:
- Keyword, Match Type, Status (enabled/paused)
- Campaign, Ad Group
- Quality Score, Expected CTR, Ad Relevance, Landing Page Experience
- Impressions, Clicks, CTR, Avg CPC, Cost
- Conversions, Conv Rate, Cost/Conv
- Final URL

Filter to enabled keywords only (paused keywords do not incur cost).

### Step 2: Calculate Priority Score

For each keyword, compute:

```python
qs_gap = 10 - current_qs
cpc_penalty = lookup_multiplier(current_qs)
monthly_waste = monthly_cost * (1 - (1 / cpc_penalty))
priority_score = monthly_waste  # This IS the waste amount
```

Sort all keywords by `priority_score` descending. The top of this list is where you start.

### Step 3: Identify Fix Category

For each keyword, determine the fix category based on its weakest component:

| Weakest Component | Fix Category | Typical Fix |
|:--|:--|:--|
| Expected CTR (Below Avg) | **Ad Performance** | Rewrite ads, add extensions, test new headlines |
| Ad Relevance (Below Avg) | **Ad Group Structure** | Tighten ad group theme, add keyword to ad copy |
| Landing Page (Below Avg) | **Landing Page** | Improve page speed, content relevance, mobile UX |
| Two components Below Avg | **Structural** | May need ad group rebuild + new landing page |
| All three Below Avg | **Critical Rebuild** | Pause, restructure from scratch, new landing page |

### Step 4: Group by Root Cause

Individual keyword fixes are inefficient. Group keywords by shared root cause:

**Group by Landing Page:**
```
/services/plumbing — 23 keywords, avg QS 4.2, all Below Avg LP Experience
/services/hvac — 15 keywords, avg QS 5.8, all Average LP Experience
/homepage — 8 keywords, avg QS 3.5, all Below Avg LP Experience
```
Fix the landing page once, improve QS for all keywords pointing to it.

**Group by Ad Group:**
```
Ad Group "Plumbing General" — 45 keywords, avg QS 4.0, Ad Relevance Below Avg
→ Too many keywords. Split into 3-5 tighter ad groups.

Ad Group "Emergency Services" — 8 keywords, avg QS 7.5
→ Good theme tightness. No action needed.
```

**Group by Campaign:**
```
Campaign "Brand" — avg QS 8.4 → Healthy
Campaign "Non-Brand Generic" — avg QS 4.8 → Needs work
Campaign "Competitor" — avg QS 3.2 → Expected for competitor keywords
```

### Step 5: Per-Keyword Detail Report

For the top 50 keywords by priority score, produce a detailed report:

```
Keyword-Level QS Audit — Top 50 by Savings Potential
=====================================================

#1: "emergency plumber near me" [Exact Match]
   Campaign: Emergency Services | Ad Group: Emergency Plumber
   QS: 3 | Expected CTR: Below Avg | Ad Relevance: Avg | LP: Below Avg
   Monthly: 450 clicks | $12.50 avg CPC | $5,625 spend
   Waste: $3,750/month ($45,000/year)
   Fix: Landing page /emergency is slow (LCP 4.8s) and not mobile-optimized.
         Rewrite ad Headline 1 to include "Emergency Plumber."

#2: "plumber [city name]" [Phrase Match]
   Campaign: Local Services | Ad Group: City Plumbing
   QS: 4 | Expected CTR: Avg | Ad Relevance: Below Avg | LP: Avg
   Monthly: 380 clicks | $9.80 avg CPC | $3,724 spend
   Waste: $1,862/month ($22,344/year)
   Fix: Ad group has 52 keywords. Split by service type.
         Add "[city name] plumber" to Headline 1.
```

### Step 6: Quick Wins Identification

Flag keywords that are one component fix away from QS 7+:

**Quick Win Criteria:**
- Current QS = 6
- Exactly one component is Average (not Below Average)
- Other two components are Above Average
- Estimated fix: simple ad copy tweak or minor landing page adjustment

These are the lowest-effort, highest-probability improvements.

### Step 7: Pause Candidates

Flag keywords that may not be worth fixing:

**Pause Criteria:**
- QS 1-2 AND monthly spend < $100 AND zero conversions in 90 days
- QS 1-3 AND Conv Rate below account average by 50%+ AND no strategic value
- All three components Below Average AND keyword is not brand or core business term

Always flag these as recommendations, not automatic actions. Some low-QS keywords may be strategically important (competitor terms, new market entry).

## Output Format

### Summary Section
```
Keyword-Level QS Audit Summary
================================
Total keywords analyzed:        1,247
Keywords at QS 7+:              778 (62.4%)
Keywords at QS 5-6:             312 (25.0%)
Keywords at QS 1-4:             157 (12.6%)

Top 20 keywords account for:    $8,200/month in QS waste (68% of total waste)
Total monthly waste (all KWs):  $12,050

Quick wins identified:          43 keywords (QS 6 → 7)
Pause candidates:               28 keywords
```

### Prioritized Fix List
Numbered, sorted by monthly waste, with specific action per keyword.

### Grouped Fix Plan
Fixes grouped by type (landing page, ad group restructure, ad copy) with estimated effort level (Low/Medium/High) and estimated monthly savings per group.
