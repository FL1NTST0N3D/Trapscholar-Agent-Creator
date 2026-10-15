# Local Citations — Citation Audit & Scoring

## Description

Audits a business's structured and unstructured citations across the web. Structured citations are directory listings (Yelp, YP, BBB); unstructured citations are mentions of the business NAP on blogs, news sites, and other web pages. Citation volume, accuracy, and quality contribute ~7% of the local ranking algorithm, but citation errors actively harm rankings by creating NAP inconsistency.

## Command

```
/local citations "Business Name" "City, State"
/local citations "Business Name" "123 Main St, City, ST 12345" "(555) 123-4567"
```

## What Gets Audited

### 1. Core Structured Citations (5 points)

These are the must-have directories. Missing listings here are critical gaps.

| Directory | Category | Points |
|-----------|----------|--------|
| Google Business Profile | Primary | 1 |
| Apple Maps / Apple Business Connect | Primary | 0.5 |
| Bing Places | Primary | 0.5 |
| Yelp | General | 0.5 |
| Facebook Business Page | Social | 0.5 |
| Yellow Pages (YP.com) | General | 0.5 |
| BBB (Better Business Bureau) | Trust | 0.5 |
| Foursquare / Swarm | Social | 0.25 |
| MapQuest | Maps | 0.25 |
| Manta | General | 0.25 |
| Superpages | General | 0.25 |

**Scoring per listing:**
- Present + accurate NAP = full points
- Present + minor NAP error = half points
- Present + major NAP error = zero points
- Missing entirely = zero points

### 2. Industry-Specific Citations (4 points)

| Industry | Priority Directories | Points (each) |
|----------|---------------------|---------------|
| Restaurants | TripAdvisor, OpenTable, Zomato, DoorDash, UberEats | 0.8 |
| Healthcare | Healthgrades, Vitals, WebMD, Zocdoc, RateMDs | 0.8 |
| Legal | Avvo, FindLaw, Justia, Lawyers.com, Martindale | 0.8 |
| Home Services | Angi, HomeAdvisor, Thumbtack, Houzz, Porch | 0.8 |
| Hotels/Lodging | Booking.com, TripAdvisor, Expedia, Hotels.com, Airbnb | 0.8 |
| Real Estate | Zillow, Realtor.com, Trulia, Redfin, LoopNet | 0.8 |
| Automotive | Cars.com, AutoTrader, CarGurus, DealerRater, Edmunds | 0.8 |
| Financial | NerdWallet, Bankrate, WalletHub, Credit Karma | 0.8 |

**Requirement:** At least 5 industry-relevant citations with accurate NAP for full marks.

### 3. Data Aggregator Submissions (3 points)

| Aggregator | Downstream Reach | Points |
|------------|-----------------|--------|
| Data Axle (InfoUSA) | 100+ directories | 1 |
| Neustar Localeze | 100+ directories | 1 |
| Foursquare (data licensing) | Apps + directories | 0.5 |
| Factual (now Foursquare) | Apps + directories | 0.5 |

**Why aggregators matter:**
- Fixing NAP at the aggregator level cascades to hundreds of downstream sites
- Single point of correction instead of updating 50+ directories manually
- Takes 2-8 weeks for changes to propagate fully

### 4. Unstructured Citations (2 points)

Unstructured citations are mentions of the business (with NAP data) on non-directory pages.

| Source Type | Examples | Points |
|-------------|----------|--------|
| Local news sites | City newspaper, local magazine | 0.5 |
| Local blogs | Community blogs, neighborhood sites | 0.5 |
| Chamber of Commerce | City/county chamber website | 0.5 |
| Sponsorship pages | Local events, charities, sports teams | 0.25 |
| Press releases | Distributed press releases with NAP | 0.25 |

**How to build unstructured citations:**
- Sponsor local events, teams, or charities (get listed on their site with NAP)
- Contribute guest posts to local blogs
- Issue press releases for business milestones
- Join the local Chamber of Commerce
- Get listed on your city or county government website

### 5. Duplicate & Error Detection (1 point)

| Check | Points |
|-------|--------|
| No duplicate listings on any platform | 0.5 |
| No closed/old-address listings still live | 0.5 |

**Duplicate Detection Signals:**
- Same business name at a different address (old location)
- Same address with a slightly different name
- Same phone number tied to a different listing
- Multiple GBP listings for the same business

**Duplicate Resolution:**
- Google: Report via "Suggest an edit" > "Close or remove" > "Duplicate"
- Yelp: Report duplicate via Yelp for Business
- Facebook: Report via "Is this your business?" merge flow
- Other directories: Contact support with proof of ownership

## Citation Quality Factors

Not all citations are equal. Quality is determined by:

1. **Domain Authority (DA)** — A citation on a DA 70+ site (Yelp, BBB) is worth more than a DA 10 directory
2. **Relevance** — Industry-specific directories signal topical authority
3. **Completeness** — Listings with full NAP + hours + description + photos outperform bare-minimum entries
4. **Activity** — Claimed and actively managed listings rank higher
5. **Link quality** — Dofollow links from citations pass more value (though most are nofollow)

## Output Format

```
CITATION AUDIT: [Business Name]
Score: [X]/15 ([Grade])

CORE STRUCTURED CITATIONS:
  [FOUND]    Google Business Profile — NAP accurate
  [FOUND]    Apple Maps — NAP accurate
  [MISSING]  Bing Places — No listing found
  [FOUND]    Yelp — NAP accurate
  [FOUND]    Facebook — Minor: phone format differs
  [FOUND]    Yellow Pages — NAP accurate
  [MISSING]  BBB — No listing found
  [FOUND]    Foursquare — NAP accurate
  Subtotal: [X]/5

INDUSTRY CITATIONS ([Industry]):
  [FOUND]    TripAdvisor — NAP accurate
  [FOUND]    OpenTable — NAP accurate
  [MISSING]  Zomato — No listing found
  [MISSING]  DoorDash — No listing found
  [FOUND]    UberEats — Address mismatch
  Subtotal: [X]/4

DATA AGGREGATORS:
  [SUBMITTED] Data Axle — Last updated: 2026-01-15
  [UNKNOWN]   Neustar Localeze — Status unknown
  [SUBMITTED] Foursquare — NAP accurate
  Subtotal: [X]/3

UNSTRUCTURED CITATIONS:
  [FOUND] Dallas Morning News — Business feature article
  [FOUND] Dallas Chamber of Commerce — Member listing
  [FOUND] Local food blog — Restaurant review with NAP
  Subtotal: [X]/2

DUPLICATES & ERRORS:
  [WARN] Yelp: 2 listings found — merge required
  [WARN] Old GBP listing at previous address — request removal
  Subtotal: [X]/1

TOTAL: [X]/15

PRIORITY ACTIONS:
1. [Critical] Claim Bing Places listing
2. [High] Merge duplicate Yelp listings
3. [High] Submit to BBB for trust signal
4. [Medium] Submit NAP corrections to Neustar Localeze
5. [Medium] Create DoorDash listing
6. [Low] Fix phone format on Facebook
```

## Citation Building Strategy

### Phase 1: Foundation (Week 1-2)
- Claim and optimize GBP, Apple Maps, Bing Places
- Submit to Data Axle and Neustar Localeze
- Claim Yelp, Facebook, YP, BBB

### Phase 2: Industry (Week 3-4)
- Create/claim 5 industry-specific directory listings
- Ensure full profiles (photos, descriptions, hours)

### Phase 3: Local Authority (Week 5-8)
- Join Chamber of Commerce
- Pursue 3-5 unstructured citations via local press/blogs/sponsorships
- Monitor aggregator propagation

### Phase 4: Maintenance (Ongoing)
- Monthly duplicate scan
- Quarterly NAP accuracy re-check
- Add new citations as directories emerge

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
