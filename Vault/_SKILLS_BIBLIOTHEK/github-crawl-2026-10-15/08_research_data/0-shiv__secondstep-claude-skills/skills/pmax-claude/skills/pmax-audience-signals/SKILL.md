---
name: pmax-audience-signals
description: "Evaluate Performance Max audience signal quality, diversity, and configuration. Analyzes custom segments, your data signals, interests, and demographics to ensure PMax has strong targeting guidance."
allowed-tools:
  - Bash
  - Read
  - Grep
---

# PMax Audience Signals Skill

## Purpose

Audience signals are the single most important lever advertisers have to guide Performance Max's machine learning. Unlike traditional targeting, signals are "suggestions" — PMax can (and will) go beyond them. This skill evaluates whether your signals are strong enough to steer PMax in the right direction, diverse enough to cover your audience, and fresh enough to reflect current customer behavior.

## Trigger

Activated by `/pmax signals` or as part of `/pmax audit`.

## Data Requirements

Ask the user for:
1. Audience signal configuration per asset group
2. Custom segment definitions (search terms, URLs, apps)
3. Customer list sizes and recency
4. Website visitor audience sizes and lookback windows
5. Demographic targeting settings

## Audience Signal Types

### 1. Custom Segments

Custom segments are the most powerful signal type. They tell Google's AI what kind of people you want to reach.

#### Search Term-Based Custom Segments
- **What**: Keywords your ideal customers search for
- **Minimum terms**: 5 per segment (Google recommendation)
- **Ideal**: 15-25 terms per segment
- **Maximum**: 50 terms per segment (diminishing returns beyond this)
- **Best practices**:
  - Use a mix of branded, category, competitor, and long-tail terms
  - Include terms from your top-performing Search campaigns
  - Do NOT just copy your Search campaign keywords — add discovery terms
  - Group semantically related terms into separate segments
  - Include terms your competitors rank for but you don't
  - Refresh quarterly based on Search Terms report data
  - Avoid overly broad terms (e.g., "shoes") — be specific (e.g., "waterproof hiking shoes size 12")

#### URL-Based Custom Segments
- **What**: URLs of websites your ideal customers visit
- **Ideal count**: 5-15 URLs per segment
- **Best practices**:
  - Include competitor URLs (their homepage, product pages)
  - Include industry publication URLs
  - Include review site URLs relevant to your product
  - Use specific pages, not just domains (e.g., competitor.com/product-page, not just competitor.com)
  - Include URLs from Google's "similar audiences" suggestions
  - Test niche blogs/forums your audience frequents

#### App-Based Custom Segments
- **What**: Apps your ideal customers use
- **Best for**: Mobile-first businesses, app verticals
- **Best practices**:
  - Include competitor apps
  - Include complementary apps (e.g., fitness tracker app for a supplement brand)
  - Less commonly used but powerful for specific verticals

### 2. Your Data (First-Party Signals)

Your data signals leverage your own customer information. These are the highest-quality signals because they represent actual customers.

#### Customer Lists
- **What**: Uploaded email/phone lists of existing customers
- **Minimum size**: 1,000 records (Google minimum for matching)
- **Ideal size**: 5,000+ records for effective modeling
- **Match rate benchmark**: 40-60% is normal, >60% is excellent
- **Best practices**:
  - Upload SEPARATE lists for different customer segments:
    - All customers (broad signal)
    - High-value customers (top 20% by revenue)
    - Recent purchasers (last 90 days)
    - Churned customers (for exclusion or win-back)
  - Update lists monthly at minimum
  - Include both email AND phone for better match rates
  - Use Customer Match formatting guidelines exactly
  - Hash data before upload if using the API

#### Website Visitors
- **What**: Google Ads remarketing audiences based on site behavior
- **Minimum size**: 100 users in last 30 days
- **Ideal**: 1,000+ users for effective signal strength
- **Lookback windows to configure**:
  - All visitors (30 days, 90 days, 180 days, 540 days)
  - Product/service page visitors (shorter windows: 7, 14, 30 days)
  - Cart/form abandoners (7, 14, 30 days)
  - Converters (30, 90, 180 days) — for lookalike modeling
- **Best practices**:
  - Layer multiple visitor audiences as signals
  - Shorter lookback = higher intent signal
  - Converters list as signal helps PMax find similar users
  - Ensure Google Ads remarketing tag fires on all relevant pages
  - Verify audience sizes in Google Ads > Tools > Audience Manager

#### App Users
- **What**: Users of your mobile app (if applicable)
- **Signal types**: All users, active users, lapsed users, in-app purchasers
- **Best practices**: Segment by engagement level and recency

### 3. Interests & Detailed Demographics

Google's pre-built audience segments based on user behavior patterns.

#### In-Market Audiences
- **What**: Users actively researching or comparing products in your category
- **Signal strength**: High — these users have demonstrated purchase intent
- **Best practices**:
  - Select 3-5 most relevant in-market segments
  - Layer with custom segments for reinforced signaling
  - Check Google's taxonomy — some in-market segments are very specific
  - These work well for top-of-funnel discovery within PMax

#### Affinity Audiences
- **What**: Users with long-term interests aligned with your brand
- **Signal strength**: Medium — broad interests, not purchase intent
- **Best practices**:
  - Use sparingly — these are very broad
  - Best for brand awareness objectives
  - Combine with narrower signals (custom segments + affinity)
  - Don't rely solely on affinity signals

#### Life Events
- **What**: Users going through major life changes (moving, graduating, getting married)
- **Signal strength**: Medium-High — time-sensitive and specific
- **Best practices**:
  - Highly relevant for certain verticals (real estate, insurance, wedding)
  - Time-sensitive by nature — users move through these quickly
  - Powerful when combined with geographic signals

#### Detailed Demographics
- **What**: Age, gender, household income, parental status, education, homeownership
- **Best practices**:
  - Use demographic signals cautiously — they narrow your audience significantly
  - Household income tiers are powerful for luxury/premium products
  - Do NOT exclude demographics unless you have data proving they don't convert
  - Let PMax discover — demographics as signals, not restrictions

## Signal Quality Assessment

### Signal Strength Rating

| Rating | Criteria |
|---|---|
| **Strong** | 3+ custom segments with 15+ terms each, customer list >5K, website visitors >1K, in-market audiences selected |
| **Moderate** | 1-2 custom segments, customer list 1-5K, some website visitors, basic interests |
| **Weak** | No custom segments, no customer lists, only broad interests/demographics |
| **None** | No audience signals configured (PMax running fully blind) |

### Signal Freshness Assessment

| Rating | Criteria |
|---|---|
| **Fresh** | Customer lists updated <30 days ago, custom segments reviewed <90 days ago |
| **Stale** | Lists 30-90 days old, segments not reviewed in 3-6 months |
| **Outdated** | Lists >90 days old, segments never updated since creation |

### Signal Diversity Assessment

| Rating | Criteria |
|---|---|
| **Diverse** | Uses all 3 signal types (custom segments + your data + interests) |
| **Partial** | Uses 2 of 3 signal types |
| **Narrow** | Uses only 1 signal type |

## Scoring Rubric (0-100)

### Custom Segments (0-35 points)

| Criteria | Points |
|---|---|
| 3+ search term segments with 15+ terms each | 15 |
| URL-based segments with 5+ competitor/industry URLs | 10 |
| Terms reflect actual customer search behavior (not just keywords) | 5 |
| Segments updated within last 90 days | 5 |

### Your Data Signals (0-35 points)

| Criteria | Points |
|---|---|
| Customer list uploaded with >5K records | 10 |
| Multiple customer segments (high-value, recent, all) | 8 |
| Website visitor audiences configured (multiple lookbacks) | 7 |
| Converters list used as signal | 5 |
| Lists updated within last 30 days | 5 |

### Interests & Demographics (0-15 points)

| Criteria | Points |
|---|---|
| Relevant in-market audiences selected (3-5) | 8 |
| Life events used where applicable | 4 |
| Demographics not overly restrictive | 3 |

### Signal Architecture (0-15 points)

| Criteria | Points |
|---|---|
| All 3 signal types used | 5 |
| Different asset groups have different signals | 5 |
| Signal strategy documented and intentional | 5 |

## Common Issues to Flag

1. **No audience signals at all** — PMax is flying completely blind. Critical issue.
2. **Only broad interests/demographics** — Weak signals that don't meaningfully guide PMax.
3. **Customer lists under 1,000** — Too small for effective matching and modeling.
4. **Stale customer lists** — Lists not updated in 90+ days miss new customer patterns.
5. **Copy-pasted Search keywords as custom segments** — Custom segments should include discovery terms, not just existing keywords.
6. **Same signals across all asset groups** — Each asset group should target a distinct audience segment.
7. **Overly restrictive demographics** — Narrowing demographics defeats PMax's discovery advantage.
8. **No website visitor signals** — Missing easy, high-quality first-party data signals.
9. **No converters list** — The converters audience is the strongest signal for lookalike modeling.
10. **Single custom segment with <5 terms** — Insufficient data for Google's AI to model from.

## Output Format

```
## Audience Signal Audit Results

### Signal Quality Score: XX/100

### Signal Inventory
| Signal Type | Configured | Details | Status |
|---|---|---|---|
| Custom Segments (Search) | Yes/No | X segments, Y terms | STRONG/MODERATE/WEAK |
| Custom Segments (URL) | Yes/No | X segments, Y URLs | STRONG/MODERATE/WEAK |
| Customer Lists | Yes/No | X records, updated MM/DD | STRONG/MODERATE/WEAK |
| Website Visitors | Yes/No | X audiences, Y total users | STRONG/MODERATE/WEAK |
| In-Market | Yes/No | X segments selected | OK/WARNING |
| Demographics | Yes/No | Restrictions: [list] | OK/WARNING |

### Signal Strength: [Strong/Moderate/Weak/None]
### Signal Freshness: [Fresh/Stale/Outdated]
### Signal Diversity: [Diverse/Partial/Narrow]

### Critical Issues
- [List findings]

### Recommendations
1. [Prioritized action items]
```
