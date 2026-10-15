# Local Geo-Targeting — Google Ads Local Setup & Keyword Strategy

## Description

Audits Google Ads geo-targeting configuration, location extensions, local keyword strategy, and campaign structure for local businesses. Misconfigured geo-targeting is the #1 cause of wasted ad spend for local advertisers — "Presence or interest" targeting (Google's default) can show ads to users thousands of miles away who merely researched the area.

## Command

```
/local geo "Business Name" "City, State"
/local geo "Business Name" --radius "25 miles" --services "plumbing, drain cleaning"
```

## What Gets Audited

### 1. Location Targeting Settings (4 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Targeting method | "Presence: People in or regularly in" (NOT "Presence or interest") | 2 |
| Exclusion method | "Presence: People in" for excluded locations | 0.5 |
| Geographic scope | Appropriate radius or city/zip targeting | 1 |
| Negative locations | Irrelevant nearby areas excluded | 0.5 |

**Critical Setting — Targeting Method:**

Google Ads offers three options under Settings > Locations > Target:

| Option | What It Does | Recommendation |
|--------|-------------|----------------|
| Presence or interest (default) | Targets people IN the area OR who SEARCHED for the area | NEVER use for local businesses |
| Presence: People in or regularly in | Only targets people physically in the area | ALWAYS use for local businesses |
| Search interest | Only targets people who searched for the area | Rarely appropriate |

**Why "Presence or interest" wastes money:**
- A user in New York searching "best plumber in Dallas" triggers your Dallas ad
- They will never become a customer
- Google defaults to this setting — you must manually change it
- This single setting can waste 20-40% of local ad budgets

**Radius vs. City/Zip Targeting:**

| Method | Best For | Notes |
|--------|----------|-------|
| Radius targeting | Service area businesses | Set from business address; 10-30 mile typical |
| City targeting | Businesses serving specific cities | Select individual cities |
| Zip code targeting | Dense urban areas | Granular control, good for bid adjustments |
| County targeting | Rural service areas | Broader coverage, less granular |

**Radius Targeting Guidelines:**
- Home services: 15-30 miles from business address
- Restaurants: 5-10 miles (15 miles for destination dining)
- Healthcare: 10-20 miles
- Legal: 20-50 miles (depends on practice area)
- Do not set radius larger than your actual service area

### 2. Location Extensions & Assets (3 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Location asset linked | Google Business Profile linked to Ads account | 1 |
| Location showing in ads | Location extension appearing on search ads | 0.5 |
| Call extension | Local phone number in call extension | 0.5 |
| Sitelink extensions | Location-specific sitelinks (directions, hours) | 0.5 |
| Structured snippets | Service types or neighborhoods listed | 0.5 |

**Linking GBP to Google Ads:**
1. In Google Ads: Assets > Location assets
2. Link your Google Business Profile account
3. Select the specific locations to show
4. Enable call reporting to track calls from ads

**Location Extension Benefits:**
- Show business address below the ad
- Show distance from the searcher ("2.3 miles away")
- Add a "Directions" link
- Increase ad real estate and click-through rate by 10-15%

### 3. Local Keyword Strategy (4 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Location modifiers | "[service] + [city]" keywords present | 1 |
| Near me keywords | "near me" and "nearby" variations included | 0.5 |
| Neighborhood keywords | Sub-city neighborhood terms used | 0.5 |
| Negative keywords | Non-local and irrelevant terms excluded | 1 |
| Match types | Appropriate match type usage | 1 |

**Local Keyword Framework:**

| Keyword Pattern | Example | Volume | Intent |
|----------------|---------|--------|--------|
| [service] + [city] | "plumber dallas" | High | High |
| [service] + near me | "plumber near me" | High | Very High |
| [service] + [neighborhood] | "plumber uptown dallas" | Low | Very High |
| [service] + [zip] | "plumber 75201" | Low | Very High |
| best + [service] + [city] | "best plumber dallas" | Medium | High |
| [service] + [city] + reviews | "plumber dallas reviews" | Medium | Research |
| emergency + [service] + [city] | "emergency plumber dallas" | Medium | Urgent |
| [service] + open now + [city] | "plumber open now dallas" | Low | Urgent |

**Negative Keyword Essentials for Local:**
```
# Non-local intent
jobs
hiring
salary
careers
training
school
classes
DIY
how to

# Irrelevant cities (add your non-service areas)
[competitor city names]

# Price shoppers (optional, depends on strategy)
free
cheap
discount
coupon
```

**Match Type Strategy for Local:**
- **Exact match** `[plumber dallas]`: Highest control, use for top-converting terms
- **Phrase match** `"plumber dallas"`: Good reach with relevance, primary match type
- **Broad match**: Only with Smart Bidding and tight geo-targeting; monitor closely

### 4. Campaign Structure for Local (3 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Location-specific campaigns | Separate campaigns per city/region (if multi-location) | 1 |
| Ad copy localization | City name in headlines and descriptions | 1 |
| Landing page relevance | Ads point to location-specific landing pages | 1 |

**Recommended Local Campaign Structure:**

```
Account
  Campaign: [City A] — Search
    Ad Group: [Service 1] + [City A]
    Ad Group: [Service 2] + [City A]
    Ad Group: Brand + [City A]
  Campaign: [City A] — PMax (Local)
    Asset Group: [Service 1]
    Asset Group: [Service 2]
  Campaign: [City B] — Search
    ...
```

**Ad Copy Localization Checklist:**
- [ ] City name in Headline 1 or 2
- [ ] Neighborhood or landmark reference in descriptions
- [ ] Local phone number in call extension
- [ ] "Serving [City] since [Year]" in description
- [ ] Location-specific offer if applicable

**Landing Page Alignment:**
- Search ad for "plumber dallas" must land on `/plumbing-dallas` or `/locations/dallas`, NOT the homepage
- Landing page must include the city name in H1
- Landing page must show the local address and phone number
- Landing page must have a clear CTA above the fold

### 5. Bid Adjustments (2 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Location bid adjustments | Higher bids for high-value zip codes | 1 |
| Device bid adjustments | Mobile bid adjustment for local (typically +20-30%) | 0.5 |
| Schedule bid adjustments | Higher bids during business hours | 0.5 |

**Location Bid Adjustment Strategy:**
- Increase bids +20-50% for zip codes within 5 miles of business
- Decrease bids -20-30% for zip codes at the edge of service area
- Exclude zip codes outside service area entirely
- Review location reports monthly and adjust based on conversion data

## Output Format

```
GEO-TARGETING AUDIT: [Business Name] — [City, State]
Score: [X]/16 (weighted to [X]/10 for final report)

LOCATION TARGETING:
  [FAIL] Using "Presence or interest" — CHANGE TO "Presence only"
  [PASS] Targeting: 25-mile radius from business address
  [WARN] No negative locations set — exclude [irrelevant areas]
  Subtotal: [X]/4

LOCATION EXTENSIONS:
  [PASS] GBP linked to Ads account
  [PASS] Location extensions showing on ads
  [FAIL] No call extension set
  [WARN] No location-specific sitelinks
  Subtotal: [X]/3

LOCAL KEYWORDS:
  [PASS] 23 "[service] + [city]" keywords active
  [PASS] "near me" variations included
  [MISS] No neighborhood-level keywords
  [WARN] Only 12 negative keywords (need 50+)
  [PASS] Phrase match used appropriately
  Subtotal: [X]/4

CAMPAIGN STRUCTURE:
  [PASS] Separate campaigns per location
  [WARN] Ad copy mentions city in only 2 of 5 headlines
  [FAIL] Ads pointing to homepage instead of location pages
  Subtotal: [X]/3

BID ADJUSTMENTS:
  [MISS] No location bid adjustments set
  [PASS] Mobile bid +25%
  [MISS] No ad schedule bid adjustments
  Subtotal: [X]/2

PRIORITY ACTIONS:
1. [Critical] Change targeting to "Presence: People in or regularly in"
2. [Critical] Point ads to location-specific landing pages
3. [High] Add call extension with local phone number
4. [High] Add 40+ negative keywords (jobs, DIY, free, etc.)
5. [Medium] Add neighborhood keywords for high-value areas
6. [Medium] Set location bid adjustments by zip code
7. [Low] Add location-specific sitelinks
```

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
