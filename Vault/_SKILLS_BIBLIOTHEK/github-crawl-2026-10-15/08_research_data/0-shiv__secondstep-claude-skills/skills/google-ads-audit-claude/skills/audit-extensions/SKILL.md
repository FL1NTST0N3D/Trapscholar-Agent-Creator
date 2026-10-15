---
name: audit-extensions
description: Audits ad extension (asset) coverage, performance, and completeness across all campaigns including sitelinks, callouts, structured snippets, call, location, image, price, promotion, and lead form extensions.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Ad Extensions (Assets) Audit

## Overview

Ad extensions (now called "Assets" in Google Ads) expand your ad with additional information, increasing real estate on the SERP and improving CTR. Google has confirmed that extensions are a factor in Ad Rank calculation — accounts with full extension coverage typically see 10-20% CTR improvement and pay lower CPCs through improved Ad Rank.

**Key insight:** Extensions are free to add and only show when Google predicts they'll improve performance. There is zero downside to having comprehensive extensions — but significant downside to missing them.

**Google's recommendation:** Every Search campaign should have at least 4 sitelinks, 4 callouts, and 1 structured snippet at minimum. Best practice is to have all applicable extension types active.

## Audit Checks (20 Total)

### Sitelink Extensions (3 checks)

**Check 1: Sitelink Coverage**
- Pass: 100% of Search campaigns have at least 4 sitelinks (Google requires minimum 2 to show, recommends 4+)
- Fail: Any Search campaign missing sitelinks or has fewer than 4
- Scoring: 8 points
- Best practice: 8-10 sitelinks per campaign (Google rotates and selects best performers)
- Each sitelink should have both description lines filled (25 char each)

**Check 2: Sitelink Quality & Relevance**
- Pass: Sitelinks link to distinct, relevant pages (not all pointing to homepage); descriptions are filled; URLs work
- Fail: Duplicate sitelink destinations, missing descriptions, broken URLs, or generic labels like "Learn More"
- Scoring: 5 points
- Best sitelinks: Product/service pages, pricing, testimonials, contact, specific offers, case studies

**Check 3: Sitelink Performance Review**
- Pass: Sitelinks with < 1% CTR over 90 days are refreshed; top performers retained
- Fail: Stale sitelinks running for 6+ months with no performance review
- Scoring: 3 points
- Benchmark: Good sitelink CTR: 5-10% of total clicks attributed to sitelinks

### Callout Extensions (2 checks)

**Check 4: Callout Coverage**
- Pass: 100% of Search campaigns have at least 4 callout extensions
- Fail: Campaigns missing callouts or have fewer than 4
- Scoring: 5 points
- Best practice: 8-10 callouts per campaign (25 characters each)
- Good callouts: "Free Shipping", "24/7 Support", "No Contract Required", "Same-Day Delivery", "Award-Winning"

**Check 5: Callout Diversity & Quality**
- Pass: Callouts highlight unique value propositions, not generic text; mix of benefits, features, and trust signals
- Fail: Generic callouts ("Great Service", "Best Quality") or all callouts saying similar things
- Scoring: 3 points

### Structured Snippet Extensions (2 checks)

**Check 6: Structured Snippet Coverage**
- Pass: 100% of Search campaigns have at least 1 structured snippet with 4+ values
- Fail: Campaigns missing structured snippets
- Scoring: 5 points
- Available headers: Amenities, Brands, Courses, Degree programs, Destinations, Featured hotels, Insurance coverage, Models, Neighborhoods, Service catalog, Shows, Styles, Types
- Best practice: 2-3 different headers per campaign, 4+ values each

**Check 7: Structured Snippet Relevance**
- Pass: Header type matches the business and values are specific, relevant items
- Fail: Mismatched headers (e.g., "Brands" header for a single-brand business) or generic values
- Scoring: 3 points

### Call Extensions (2 checks)

**Check 8: Call Extension Setup**
- Pass: Call extensions active on campaigns where phone calls are a conversion goal; call reporting enabled
- Fail: No call extensions on campaigns targeting call-driven businesses (local services, healthcare, legal, etc.)
- Scoring: 5 points
- Requirements: Verified phone number, call reporting ON, conversion tracking for calls (set appropriate duration: 30-60 seconds minimum)
- Schedule: Set to business hours only unless 24/7 support available

**Check 9: Call Extension Configuration**
- Pass: Call schedule matches business hours; call conversion tracking set with appropriate duration threshold
- Fail: Calls showing outside business hours, or call conversions counting at 0 seconds (inflating conversion numbers)
- Scoring: 3 points
- Benchmark: 60-second call duration threshold is standard for lead gen; 30 seconds for simple inquiries

### Location Extensions (2 checks)

**Check 10: Location Extension Setup**
- Pass: Location extensions active and linked to Google Business Profile for businesses with physical locations
- Fail: No location extensions for brick-and-mortar or service-area businesses
- Scoring: 4 points
- N/A: Online-only businesses without physical presence (mark as N/A, redistribute points)

**Check 11: Location Extension Accuracy**
- Pass: Location information is accurate, GBP listing is verified and up-to-date
- Fail: Outdated address, wrong hours, or unverified GBP listing
- Scoring: 2 points

### Image Extensions (2 checks)

**Check 12: Image Extension Coverage**
- Pass: Image extensions active on key Search campaigns (available for all eligible accounts)
- Fail: No image extensions despite account eligibility
- Scoring: 4 points
- Requirements: Square (1:1) images required; landscape (1.91:1) recommended; min 300x300px for square
- Best practice: 4+ unique images per campaign; product shots, lifestyle imagery, brand visuals

**Check 13: Image Extension Quality**
- Pass: Images are high-quality, relevant to ad content, meet Google's policies (no text overlays, no collages, clear subject)
- Fail: Low-quality images, stock photos that don't match brand, or policy violations
- Scoring: 2 points

### Price Extensions (1 check)

**Check 14: Price Extension Utilization**
- Pass: Price extensions set up for businesses with clear pricing tiers, products, or service packages
- Fail: No price extensions despite having fixed/semi-fixed pricing
- Scoring: 3 points
- Best for: E-commerce, SaaS, service packages, menu items, subscription tiers
- Minimum: 3 price items required; recommend 5-8
- Types: Brands, Events, Locations, Neighborhoods, Product categories, Product tiers, Service categories, Service tiers

### Promotion Extensions (1 check)

**Check 15: Promotion Extension Usage**
- Pass: Promotion extensions used during sales periods, seasonal events, or when active promotions exist
- Fail: Active promotions on the website but not reflected in ad extensions
- Scoring: 3 points
- Features: Occasion tags (Black Friday, Back to School, etc.), percentage or monetary discount, promo codes, date scheduling
- N/A: If business never runs promotions (redistribute points)

### Lead Form Extensions (1 check)

**Check 16: Lead Form Extension Setup**
- Pass: Lead form extensions active for lead gen campaigns (captures leads directly from SERP without landing page visit)
- Fail: No lead form extensions on lead gen campaigns where applicable
- Scoring: 3 points
- Consideration: Lead quality from form extensions is typically lower than landing page leads — monitor quality closely
- Best practice: Use qualifying questions, sync with CRM, set up auto-response

### Overall Extension Performance (4 checks)

**Check 17: Extension Coverage Score (All Types)**
- Pass: Account has 7+ of 9 applicable extension types active
- Fail: Fewer than 4 extension types active
- Scoring: 5 points
- Coverage tiers:
  - 9/9 types: Excellent coverage
  - 7-8/9: Good coverage
  - 5-6/9: Average coverage
  - 3-4/9: Below average
  - 1-2/9: Poor (significant Ad Rank penalty)

**Check 18: Extension-Level CTR Contribution**
- Pass: Extensions contribute 10%+ of total clicks (indicating they're showing and engaging users)
- Fail: Extensions contributing < 5% of clicks (may indicate low relevance or poor quality)
- Scoring: 3 points
- Benchmark: Sitelinks typically contribute 5-15% of clicks; call extensions 3-8%

**Check 19: Account-Level vs Campaign-Level Extensions**
- Pass: Combination of account-level defaults AND campaign-specific extensions where needed
- Fail: Only account-level extensions with no campaign-specific customization
- Scoring: 3 points
- Best practice: Set strong account-level defaults, then customize at campaign level for specific products/services

**Check 20: Extension Disapproval Check**
- Pass: No disapproved extensions; all assets reviewed and compliant
- Fail: Disapproved extensions reducing coverage and Ad Rank
- Scoring: 3 points

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Comprehensive extension strategy, maximizing SERP real estate |
| 75-89 | Good | Strong extension coverage with minor gaps |
| 60-74 | Average | Basic extensions present but missing types or optimization |
| 40-59 | Below Average | Significant extension gaps impacting Ad Rank and CTR |
| 0-39 | Poor | Minimal or no extensions — immediate action required |

**Total possible points: 80** (normalized to 100-point scale)

## Benchmark Data

| Extension Type | CTR Lift (avg) | Priority for Search |
|---------------|---------------|-------------------|
| Sitelinks | +10-20% | Critical |
| Callouts | +5-10% | Critical |
| Structured Snippets | +5-10% | High |
| Call Extensions | +5-8% (mobile) | High (local/service) |
| Location Extensions | +5-10% | High (local) |
| Image Extensions | +5-15% | High |
| Price Extensions | +5-10% | Medium-High |
| Promotion Extensions | +10-15% (seasonal) | Medium |
| Lead Form Extensions | +3-5% | Medium (lead gen) |

## Output Format

```markdown
## Extensions Audit Results

**Overall Score: [X]/100 — [Rating]**

### Extension Coverage Matrix
| Extension Type | Active | Campaign Coverage | Status |
|---------------|--------|------------------|--------|
| Sitelinks | Yes/No | X/Y campaigns | Pass/Fail |
| Callouts | Yes/No | X/Y campaigns | Pass/Fail |
| Structured Snippets | Yes/No | X/Y campaigns | Pass/Fail |
| Call | Yes/No | X/Y campaigns | Pass/Fail |
| Location | Yes/No | X/Y campaigns | Pass/Fail/N/A |
| Image | Yes/No | X/Y campaigns | Pass/Fail |
| Price | Yes/No | X/Y campaigns | Pass/Fail/N/A |
| Promotion | Yes/No | X/Y campaigns | Pass/Fail/N/A |
| Lead Form | Yes/No | X/Y campaigns | Pass/Fail/N/A |

**Coverage: [X]/9 extension types active**

### Performance Impact
- Estimated CTR lift from full extension coverage: [X]%
- Estimated CPC reduction from improved Ad Rank: [X]%

### Recommendations
1. [Add missing extension types]
2. [Improve existing extensions]
3. [Remove underperformers]
```
