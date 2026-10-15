# QS Expected CTR Analysis

## Command
`/qs ctr`

## Purpose

Analyze the Expected Click-Through Rate component of Quality Score. Investigate why certain keywords have Below Average Expected CTR ratings, identify the factors within your control, separate structural CTR limitations from fixable issues, and produce a plan to improve CTR performance relative to competitors.

## Understanding Expected CTR

Expected CTR is Google's prediction of how likely your ad is to be clicked when shown for a specific keyword. This is the most nuanced QS component because it accounts for factors beyond your control.

**Weight in Quality Score: ~39%**

**Key distinction:** Expected CTR is not your actual CTR. Google normalizes for ad position — a lower position does not automatically mean a lower Expected CTR rating. Google compares your CTR against other advertisers in similar positions bidding on the same keyword.

### What Expected CTR Measures

Google asks: "If we show this advertiser's ad for this keyword, how likely is a click compared to other advertisers' ads for the same keyword?"

This comparison means:
- You could have a 5% CTR and still be rated Below Average if competitors average 8%
- You could have a 2% CTR and be rated Above Average if it is a low-CTR keyword category
- Position normalization means your ad at position 4 is compared to competitors at similar positions, not just the top-position ads

### Factors That Drive Expected CTR

#### Within Your Control

1. **Ad Copy Quality**
   - Compelling headlines that create urgency or curiosity
   - Clear value proposition differentiated from competitors
   - Strong call-to-action that motivates clicks
   - Emotional triggers appropriate to the keyword intent
   - Numbers, statistics, and specifics ("Save 47%", "Since 2005", "500+ Reviews")

2. **Ad Extensions**
   - Sitelink extensions (add 4-6 relevant sitelinks)
   - Callout extensions (highlight unique selling points)
   - Structured snippet extensions (list services, brands, types)
   - Call extensions (especially for mobile and local searches)
   - Location extensions (for local businesses)
   - Price extensions (for e-commerce and services with clear pricing)
   - Image extensions (where available)

   Extensions increase ad real estate, which directly improves CTR. Accounts with full extension coverage typically see 10-15% higher CTR.

3. **Match Type Strategy**
   - Broad match keywords may trigger for loosely related queries with low CTR
   - Phrase match provides better intent alignment
   - Exact match has the highest CTR but lowest volume
   - Negative keywords prevent irrelevant impressions that dilute CTR

4. **Ad Rotation and Testing**
   - Stale ads lose CTR over time (ad fatigue)
   - Regular testing of new headlines keeps ads fresh
   - Use "Optimize" rotation to let Google favor higher-CTR ads
   - Test at least 2-3 RSA variations per ad group

5. **Device Bid Adjustments**
   - If mobile CTR is significantly lower, consider mobile bid adjustments
   - Desktop and mobile users respond to different ad copy styles
   - Create device-specific ad variations where possible

#### Partially Within Your Control

6. **Keyword-Ad Alignment**
   - Better alignment between keyword and ad copy naturally improves CTR
   - This overlaps with Ad Relevance but also directly impacts click probability

7. **Audience Targeting**
   - Observation-mode audiences can inform bid adjustments
   - Targeting higher-intent audiences improves CTR on average
   - Remarketing lists for search ads (RLSA) typically have higher CTR

#### Outside Your Control

8. **Competitive Landscape**
   - New competitors entering the auction with aggressive offers
   - Competitor ads with better offers, lower prices, or stronger brands
   - Seasonal competitive intensity changes

9. **Keyword Category**
   - Some keyword categories have inherently low CTR (informational queries, high-competition verticals)
   - Brand terms naturally have higher CTR than generic terms
   - Long-tail keywords often have higher CTR than head terms

10. **Search Intent Alignment**
    - If the keyword's primary intent does not align with paid ads (e.g., informational searches), CTR will be lower regardless of ad quality

## Analysis Methodology

### Step 1: Segment by Expected CTR Rating

```
Expected CTR Distribution
==========================
Above Average:  425 keywords (34%)  — $15,200/mo spend
Average:        512 keywords (41%)  — $18,900/mo spend
Below Average:  310 keywords (25%)  — $10,900/mo spend
```

### Step 2: Cross-Reference with Actual CTR

Compare Expected CTR ratings with actual CTR values to identify discrepancies:

```
Expected CTR vs Actual CTR Analysis
====================================
                    Avg Actual CTR    Expected CTR Rating
Above Average:      7.2%              Good — actual performance matches rating
Average:            4.1%              Normal — room for improvement
Below Average:      2.3%              Problem — significant gap

Account average:    4.5%
Industry benchmark: 3.8%              Above industry average overall
```

### Step 3: Identify Below Average Root Causes

For each Below Average keyword, diagnose the likely cause:

| Root Cause | Diagnostic Signal | Fix |
|:--|:--|:--|
| **Poor ad copy** | Below Avg CTR across multiple keywords in same ad group | Rewrite ads with stronger headlines |
| **Missing extensions** | Ad group/campaign has few or no extensions | Add all relevant extension types |
| **Match type bleed** | Broad match keyword with low CTR on search terms report | Add negatives, tighten match types |
| **Ad fatigue** | CTR declined over time, same ads running 6+ months | Create new ad variations |
| **Wrong audience** | CTR fine on some devices/locations, poor on others | Adjust device/geo bid modifiers |
| **Inherently low CTR** | Informational keyword, all competitors also low CTR | Accept or reconsider keyword strategy |

### Step 4: Extension Audit

Audit extension coverage across all campaigns:

```
Extension Coverage Report
===========================
                    Campaigns with Extension    Quality
Sitelinks:          8/12 (67%)                  3 campaigns have generic sitelinks
Callouts:           5/12 (42%)                  ← Gap!
Structured Snippets: 3/12 (25%)                 ← Gap!
Call Extensions:    10/12 (83%)                  Good
Location:           6/12 (50%)                  Missing for local campaigns
Price:              2/12 (17%)                   ← Gap!
Image:              0/12 (0%)                    ← Gap!
```

### Step 5: Geographic CTR Variation

Analyze CTR by geographic area to identify location-specific issues:

```
CTR by Region
===============
New York Metro:     5.2% (Above Avg)
Los Angeles:        4.1% (Average)
Chicago:            3.8% (Average)
Rural areas:        1.9% (Below Avg) — Consider geo bid adjustments
```

### Step 6: Device Performance

```
CTR by Device
===============
Desktop:    5.8% CTR — Above Average
Mobile:     3.2% CTR — Average
Tablet:     2.1% CTR — Below Average — Consider tablet bid reduction
```

## Optimization Playbook for Expected CTR

### Quick Wins (implement in 1-2 days)
1. Add missing ad extensions to all campaigns
2. Add negative keywords for irrelevant search terms bleeding CTR
3. Pin best-performing headlines to Position 1 in RSAs

### Medium-Term Fixes (1-2 weeks)
4. Rewrite ads for all Below Average Expected CTR ad groups
5. Create device-specific ad copy variations
6. Implement RLSA bid adjustments for higher-intent audiences
7. Test new headline angles: questions, numbers, urgency, social proof

### Structural Changes (2-4 weeks)
8. Move broad match keywords to their own campaigns with dedicated budgets
9. Create SKAG/STAG structure for top 20 keywords by spend
10. Build out geographic-specific ad groups for local services

## Output Format

1. **Expected CTR Summary** — Distribution of ratings with spend weighting
2. **CTR Benchmark Comparison** — Your CTR vs industry benchmarks by keyword category
3. **Extension Coverage Report** — Gaps in extension coverage across campaigns
4. **Below Average Keywords** — Top 20 by spend with diagnosed root cause
5. **Device & Geo Analysis** — CTR variation by device and location
6. **Optimization Plan** — Prioritized list of fixes with estimated CTR improvement
7. **Estimated QS Impact** — How many QS points would improve if Expected CTR moves from Below Avg to Avg/Above Avg
