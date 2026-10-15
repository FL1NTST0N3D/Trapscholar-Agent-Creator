---
name: audit-campaign-structure
description: Analyzes Google Ads campaign hierarchy, naming conventions, network targeting, geographic settings, ad schedules, device adjustments, and campaign-level configuration for structural integrity and best-practice compliance.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Campaign Structure Audit

## Overview

Campaign structure is the foundation of a well-managed Google Ads account. Poor structure leads to wasted spend, reporting blindness, and inability to optimize effectively. This skill audits the complete campaign hierarchy — from naming conventions to network settings to geographic targeting — producing a scored assessment with prioritized recommendations.

A properly structured account enables:
- Granular budget control aligned to business objectives
- Clean reporting and attribution
- Efficient optimization and bid strategy deployment
- Proper audience and geographic targeting
- Scalability as the account grows

## Audit Checks (25 Total)

### Naming Convention Checks (5 checks)

**Check 1: Campaign Naming Convention Consistency**
- Pass: All campaigns follow a consistent naming pattern (e.g., `[Network]_[Goal]_[GeoTarget]_[Audience/Theme]`)
- Fail: Campaign names are inconsistent, use default names ("Campaign 1"), or lack descriptive structure
- Scoring: 4 points — deduct 1 point per inconsistency pattern found (min 0)

**Check 2: Ad Group Naming Convention**
- Pass: Ad group names clearly describe the keyword theme they contain
- Fail: Generic names like "Ad Group 1" or names that don't match contained keywords
- Scoring: 4 points

**Check 3: Campaign Name Contains Network Type**
- Pass: Campaign names indicate Search, Display, Shopping, Video, PMax, or Demand Gen
- Fail: No network indicator in naming
- Scoring: 3 points

**Check 4: Campaign Name Contains Geographic Target**
- Pass: Geo target is part of the campaign name (e.g., `_US_`, `_NYC_`, `_National_`)
- Fail: No geographic indicator when account targets multiple regions
- Scoring: 2 points

**Check 5: Campaign Name Contains Goal/Funnel Stage**
- Pass: Names include goal indicators like `_Brand_`, `_NonBrand_`, `_Remarketing_`, `_Prospecting_`
- Fail: No goal or funnel stage in naming
- Scoring: 2 points

### Network Targeting Checks (4 checks)

**Check 6: Search/Display Network Separation**
- Pass: Search campaigns have "Display Network" opted OUT; Display campaigns run independently
- Fail: Search campaigns include Display Network (Google's default setting — almost always wasteful)
- Scoring: 8 points — this is a critical finding
- Benchmark: Display expansion on Search campaigns typically wastes 10-30% of budget on low-quality placements

**Check 7: Search Partners Setting**
- Pass: Search Partners is either deliberately opted in with documented reasoning OR opted out
- Fail: Search Partners is on by default with no performance review
- Scoring: 3 points
- Benchmark: Search Partners typically delivers 20-40% lower CTR and conversion rates; acceptable for brand campaigns, often wasteful for non-brand

**Check 8: Campaign Type Appropriateness**
- Pass: Campaign types align with business objectives (Search for high-intent, Display for awareness, PMax for full-funnel, Shopping for e-commerce)
- Fail: Mismatched campaign types (e.g., Display-only for a lead gen business with no remarketing lists)
- Scoring: 5 points

**Check 9: Campaign Type Diversity**
- Pass: Account uses appropriate mix of campaign types for the business model
- Fail: Over-reliance on a single campaign type when diversification would improve results
- Scoring: 3 points

### Geographic Targeting Checks (4 checks)

**Check 10: Location Targeting Method — CRITICAL**
- Pass: Set to "Presence: People in or regularly in your targeted locations"
- Fail: Set to "Presence or Interest: People in, regularly in, or who've shown interest in your targeted locations" (Google's default — can waste 20-50% of budget on out-of-area traffic)
- Scoring: 8 points
- Benchmark: Switching from "Presence or Interest" to "Presence Only" typically reduces wasted spend by 15-35% for local businesses

**Check 11: Geographic Target Granularity**
- Pass: Targeting is appropriately granular (city/metro for local, state for regional, country for national) with bid adjustments by location performance
- Fail: Overly broad targeting (e.g., entire US for a single-city service business)
- Scoring: 5 points

**Check 12: Geographic Exclusions**
- Pass: Irrelevant or poor-performing locations are excluded
- Fail: No exclusions set despite having location-specific services
- Scoring: 3 points

**Check 13: Location Bid Adjustments**
- Pass: Bid adjustments reflect location performance data (higher bids in high-converting areas)
- Fail: No location bid adjustments despite 30+ days of data
- Scoring: 3 points

### Ad Schedule Checks (4 checks)

**Check 14: Ad Schedule Configured**
- Pass: Ad schedule is configured and aligns with business hours or conversion patterns
- Fail: Running 24/7 with no ad schedule review despite data availability
- Scoring: 4 points

**Check 15: Ad Schedule Bid Adjustments**
- Pass: Time-of-day bid adjustments reflect conversion rate patterns (higher bids during peak, lower during off-peak)
- Fail: Flat bids across all hours despite significant performance variation
- Scoring: 3 points

**Check 16: Day-of-Week Performance**
- Pass: Day-of-week bid adjustments reflect performance patterns (e.g., reduce bids on low-converting weekends for B2B)
- Fail: No day-parting despite significant day-of-week variance
- Scoring: 3 points

**Check 17: Off-Hours Strategy**
- Pass: Clear strategy for off-hours (reduce bids, pause, or maintain based on data)
- Fail: No off-hours strategy despite business being closed at certain times
- Scoring: 2 points

### Device Targeting Checks (4 checks)

**Check 18: Device Bid Adjustments Set**
- Pass: Device bid adjustments reflect performance by device (desktop, mobile, tablet)
- Fail: No device bid adjustments despite 30+ days of conversion data
- Scoring: 4 points
- Benchmark: Mobile typically converts 20-40% lower for lead gen; mobile often converts higher for click-to-call

**Check 19: Mobile Performance Review**
- Pass: Mobile bid adjustment reflects actual mobile conversion rate vs desktop
- Fail: Mobile running at same bid despite significantly different conversion rates
- Scoring: 4 points

**Check 20: Tablet Strategy**
- Pass: Tablet bid adjustment set (often -100% or reduced since tablet traffic is usually low-quality)
- Fail: Tablet running at desktop bids with no review
- Scoring: 2 points

**Check 21: Device-Specific Landing Pages**
- Pass: Mobile users get mobile-optimized landing pages (if applicable)
- Fail: Desktop-only landing pages served to mobile traffic
- Scoring: 3 points

### Campaign-Level Settings Checks (4 checks)

**Check 22: Campaign Goal Alignment**
- Pass: Campaign objectives (Sales, Leads, Website Traffic, Awareness) match business goals
- Fail: Default or mismatched campaign goals
- Scoring: 3 points

**Check 23: Language Targeting**
- Pass: Language targeting matches target audience; English-only for English-speaking markets unless bilingual targeting is intentional
- Fail: "All languages" selected without reason (can waste budget on non-English queries)
- Scoring: 3 points

**Check 24: URL Options (Tracking Templates)**
- Pass: Tracking templates set at account or campaign level for proper attribution (UTM parameters, GCLID passback)
- Fail: No tracking template; relying solely on auto-tagging
- Scoring: 3 points

**Check 25: Campaign Status Hygiene**
- Pass: No paused campaigns older than 90 days cluttering the account; archived or removed
- Fail: Multiple legacy paused campaigns creating noise
- Scoring: 2 points

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Best-in-class structure; minor tweaks only |
| 75-89 | Good | Solid structure with some optimization opportunities |
| 60-74 | Average | Functional but multiple structural issues need attention |
| 40-59 | Below Average | Significant structural problems causing wasted spend |
| 0-39 | Poor | Fundamental restructuring required |

**Total possible points: 100** (checks are weighted as shown above, normalized to 100)

## Benchmark Data

| Metric | Good | Average | Poor |
|--------|------|---------|------|
| Search/Display separation rate | 100% | 80% | < 50% |
| Location targeting method correct | Presence Only | — | Presence or Interest |
| Campaigns with ad schedules | 100% | 60% | 0% |
| Campaigns with device adjustments | 100% | 50% | 0% |
| Naming convention compliance | 100% | 70% | < 40% |
| Search Partners CTR vs Search | Within 20% | 20-40% lower | > 40% lower |

## Output Format

```markdown
## Campaign Structure Audit Results

**Overall Score: [X]/100 — [Rating]**

### Critical Findings
- [List any check scoring 0 that has 5+ point weight]

### Check Results Table
| # | Check | Status | Points | Notes |
|---|-------|--------|--------|-------|
| 1 | Naming Convention | Pass/Fail | X/4 | ... |
...

### Top Recommendations (Priority Order)
1. [Highest impact fix]
2. [Second highest]
3. ...

### Estimated Impact
- Monthly spend at risk from structural issues: $[X]
- Projected improvement from fixes: [X-Y]%
```
