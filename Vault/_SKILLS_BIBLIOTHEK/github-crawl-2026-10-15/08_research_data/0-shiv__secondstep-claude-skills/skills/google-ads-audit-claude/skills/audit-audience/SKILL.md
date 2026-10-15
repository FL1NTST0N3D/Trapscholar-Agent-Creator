---
name: audit-audience
description: Audits audience strategy including observation vs targeting modes, RLSA setup, in-market audiences, custom segments, customer match freshness, similar audiences, demographic targeting, audience exclusions, and audience performance analysis.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Audience Audit

## Overview

Audience targeting in Google Ads has evolved from a Display-only feature to a critical component of Search, Shopping, and PMax campaigns. Proper audience strategy enables bid modifiers on high-value segments, exclusion of low-value users, and layering of intent signals on top of keyword targeting.

**Two audience modes in Search:**
1. **Observation** (recommended starting point): Audiences are applied for bid adjustment and reporting, but don't restrict targeting. You still reach all searchers, but can bid more/less based on audience membership.
2. **Targeting**: Only users in the selected audiences can see your ads. Restricts reach but maximizes relevance. Used for RLSA campaigns, remarketing-only campaigns, or highly specific audiences.

**Key principle:** Every Search campaign should have audiences in observation mode at minimum — it's free data that enables smarter bidding and reveals audience-level performance differences.

## Audit Checks (15 Total)

### Audience Application & Mode (3 checks)

**Check 1: Audience Coverage Across Search Campaigns**
- Pass: 100% of Search campaigns have at least one audience applied in observation mode
- Fail: Campaigns with zero audiences applied (missing free performance data and bid signal opportunities)
- Scoring: 8 points
- Minimum audiences for every Search campaign:
  - All website visitors (remarketing)
  - All converters (for bid adjustment and exclusion if needed)
  - 2-3 relevant in-market audiences
- Note: With smart bidding, Google uses audience signals automatically — but observation mode still provides valuable reporting data

**Check 2: Observation vs Targeting Mode Clarity**
- Pass: Clear strategy for when observation vs targeting is used; targeting only used for specific RLSA or remarketing campaigns
- Fail: Targeting mode accidentally applied on prospecting campaigns (restricting reach unintentionally)
- Scoring: 6 points
- Critical error: Targeting mode on a broad Search campaign means only users in your audience lists see ads — dramatically reducing reach

**Check 3: Audience List Diversity**
- Pass: Mix of audience types applied — remarketing, customer match, in-market, custom segments, demographics
- Fail: Only one audience type used across the account
- Scoring: 4 points

### RLSA (Remarketing Lists for Search Ads) (3 checks)

**Check 4: RLSA Setup**
- Pass: RLSA audiences (website visitors) applied to Search campaigns with bid adjustments (typically +20-50% for past visitors)
- Fail: No RLSA audiences on Search campaigns
- Scoring: 7 points
- Impact: RLSA typically improves conversion rate by 30-50% — past visitors who search again are much more likely to convert
- Bid adjustment benchmark: +20-50% for all visitors, +50-100% for cart abandoners, +100-150% for high-intent page visitors

**Check 5: RLSA List Segmentation**
- Pass: Multiple remarketing lists with different recency windows (7-day, 30-day, 90-day, 180-day, 540-day visitors) and different behaviors (all visitors, product viewers, cart abandoners, converters)
- Fail: Single "All Visitors" list with no segmentation
- Scoring: 5 points
- Recommended lists:
  - All visitors (1-30 days) — hottest audience
  - All visitors (31-90 days) — warm audience
  - All visitors (91-540 days) — cold audience
  - Product/service page viewers — intent signal
  - Cart/form abandoners — high intent, didn't convert
  - Past converters — for upsell/cross-sell or exclusion

**Check 6: RLSA Bid Adjustments by Performance**
- Pass: Bid adjustments differentiated based on actual RLSA performance data (higher bids for lists with higher CVR)
- Fail: Same bid adjustment for all remarketing lists despite different conversion rates
- Scoring: 3 points

### In-Market & Custom Segments (2 checks)

**Check 7: In-Market Audience Utilization**
- Pass: Relevant in-market audiences applied in observation mode with performance data being collected; top-performing in-market segments have positive bid adjustments
- Fail: No in-market audiences applied
- Scoring: 5 points
- In-market audiences = users actively researching or comparing products/services in a category
- Strategy: Apply 5-10 relevant in-market audiences in observation → after 30 days, bid up on high-CVR segments, bid down on low-CVR
- Examples: "Business Services", "Real Estate", "Software", "Travel", "Education" (hundreds of sub-categories available)

**Check 8: Custom Segment Creation & Quality**
- Pass: Custom segments created based on search behavior (competitor keywords, related queries) and website interests (competitor URLs); segments are specific with 10-50 terms/URLs each
- Fail: No custom segments despite clear competitor or interest-based targeting opportunities
- Scoring: 5 points
- Custom segment types:
  - People who searched for: [your competitors, related services, problem-aware queries]
  - People who browse websites similar to: [competitor websites, industry publications]
  - People who use apps similar to: [related apps]
- Best practice: Create 3-5 custom segments targeting different angles (competitor, intent, interest)

### Customer Match (2 checks)

**Check 9: Customer Match List Upload**
- Pass: Customer email/phone lists uploaded and active; list size > 1,000 matched users (Google's minimum for most targeting)
- Fail: No customer match lists despite having a CRM or email database
- Scoring: 5 points
- Impact: Customer Match enables:
  - Bid adjustments on known customers searching again
  - Exclusion of existing customers from acquisition campaigns
  - Similar audience creation (Google finds new users like your customers)
  - Cross-sell/upsell targeting

**Check 10: Customer Match List Freshness**
- Pass: Customer lists updated at least monthly (automated sync preferred via CRM integration)
- Fail: Customer lists uploaded once and never updated (stale data, growing mismatch between list and reality)
- Scoring: 3 points
- Best practice: Set up automated Customer Match sync via:
  - Zapier/Make → Google Ads API
  - HubSpot/Salesforce native Google Ads integration
  - Google Ads Customer Match scheduled uploads
- Match rate benchmark: 30-60% match rate is typical; < 20% indicates data quality issues

### Audience Exclusions & Demographics (3 checks)

**Check 11: Audience Exclusions**
- Pass: Existing customers/converters excluded from acquisition campaigns (prevents paying to acquire someone you already have); irrelevant demographics excluded
- Fail: No exclusions — paying to acquire existing customers or targeting clearly irrelevant demographics
- Scoring: 6 points
- Key exclusions for acquisition campaigns:
  - Past converters (last 30-90 days, depending on repurchase cycle)
  - Current customers (via Customer Match)
  - Employees (exclude company IP or employee list)
- Key exclusions for remarketing campaigns:
  - Recent converters (don't remarket immediately after purchase)
  - Users who bounced in < 5 seconds (low quality)

**Check 12: Demographic Targeting Review**
- Pass: Demographic data (age, gender, household income, parental status) reviewed and adjusted based on performance
- Fail: No demographic review despite 30+ days of data; spending equally across all demographics regardless of conversion rate
- Scoring: 4 points
- Strategy:
  - Review conversion rates by age bracket, gender, HHI
  - Increase bids on high-converting demographics
  - Decrease bids (or exclude) demographics with zero conversions and significant spend
  - Caution: Don't exclude too aggressively — some demographics may convert at low rates but still profitably

**Check 13: Audience Performance Analysis**
- Pass: Regular audience performance review conducted — CPA/ROAS compared across all applied audiences; insights used to inform bid adjustments and creative strategy
- Fail: Audiences applied but performance never reviewed (data collected but not acted upon)
- Scoring: 5 points
- Analysis cadence: Monthly minimum
- Metrics to compare: CTR, CVR, CPA, ROAS by audience segment
- Action framework:
  - CVR 2x average → Increase bid +50-100%
  - CVR at average → No change
  - CVR 50% below average → Decrease bid -20-30%
  - CVR zero after 100+ clicks → Consider exclusion

### Similar/Lookalike Audiences (2 checks)

**Check 14: Similar Audience Replacement Strategy**
- Pass: Since Google deprecated Similar Audiences (May 2023), account has transitioned to custom segments and optimized targeting as replacements
- Fail: Still relying on legacy Similar Audience lists or no replacement strategy implemented
- Scoring: 3 points
- Replacement options:
  - Custom segments based on converter behavior
  - Optimized targeting in Display/Video campaigns
  - Customer Match for lookalike expansion via PMax audience signals

**Check 15: First-Party Data Strategy Completeness**
- Pass: Comprehensive first-party data strategy covering website visitors, converters, CRM data, and app users where applicable
- Fail: Fragmented first-party data usage — some sources connected, others not
- Scoring: 4 points
- First-party data sources to leverage:
  - Website visitors (Google Ads tag / GA4 audiences)
  - CRM contacts (Customer Match)
  - App users (if applicable)
  - YouTube viewers/subscribers
  - Lead form submitters
  - Offline store visitors (if applicable)

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Sophisticated audience strategy maximizing relevance and efficiency |
| 75-89 | Good | Strong audience foundation with optimization opportunities |
| 60-74 | Average | Basic audience setup — significant data and optimization opportunities untapped |
| 40-59 | Below Average | Minimal audience strategy; missing key targeting and exclusion capabilities |
| 0-39 | Poor | No audience strategy — operating without audience intelligence |

**Total possible points: 73** (normalized to 100-point scale)

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Search campaigns with audiences | 100% | 80%+ | 50-80% | < 50% |
| RLSA CVR vs non-RLSA | 2-3x higher | 1.5-2x | 1.2-1.5x | < 1.2x |
| Remarketing list segments | 5+ | 3-5 | 1-2 | 0 |
| Customer Match match rate | > 50% | 30-50% | 15-30% | < 15% |
| Audience exclusions active | Yes (3+ types) | Yes (1-2 types) | No | No |
| Custom segments | 3+ | 1-2 | 0 | 0 |

## Output Format

```markdown
## Audience Audit Results

**Overall Score: [X]/100 — [Rating]**

### Audience Coverage
| Campaign | Audiences Applied | Mode | RLSA | In-Market | Custom | Exclusions |
|----------|------------------|------|------|-----------|--------|-----------|
| ... | X | Obs/Target | Yes/No | Yes/No | Yes/No | Yes/No |

### Remarketing Lists
| List | Size | Recency | Bid Adj | CVR vs Avg |
|------|------|---------|---------|-----------|
| All Visitors | X | 30 days | +X% | Xx |
| ... | ... | ... | ... | ... |

### Customer Match Status
- Lists uploaded: Yes/No
- List size: X matched users
- Last updated: [Date]
- Match rate: X%

### Audience Performance Summary
| Audience | Impressions | Clicks | CVR | CPA | Bid Adj | Recommendation |
|----------|-----------|--------|-----|-----|---------|---------------|
| ... | ... | ... | ... | ... | ... | Increase/Decrease/Exclude |

### Key Findings
1. ...

### Recommendations
1. [Apply audiences to uncovered campaigns]
2. [Create RLSA segments]
3. [Upload customer match list]
4. [Set up audience exclusions]
```
