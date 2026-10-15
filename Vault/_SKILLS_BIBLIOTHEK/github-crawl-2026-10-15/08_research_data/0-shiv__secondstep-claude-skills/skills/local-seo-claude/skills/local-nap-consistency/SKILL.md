# Local NAP Consistency — Name, Address, Phone Audit

## Description

Audits NAP (Name, Address, Phone) consistency across the business website, Google Business Profile, and major online directories. NAP inconsistencies are one of the top negative local ranking factors. Even small variations — "St" vs "Street," "Suite 100" vs "#100" — can fragment your local authority and confuse both Google and potential customers.

## Command

```
/local nap "Business Name" "Full Address" "Phone Number"
/local nap "Business Name" "123 Main St, Dallas, TX 75201" "(214) 555-1234"
```

## What Gets Audited

### 1. Primary Sources (8 points)

These are the highest-authority sources. Inconsistencies here are critical.

| Source | Weight | Check |
|--------|--------|-------|
| Google Business Profile | 3 | Name, address, phone, website URL |
| Business Website | 3 | Header/footer NAP, contact page, schema markup |
| Apple Maps | 1 | Name, address, phone |
| Bing Places | 1 | Name, address, phone |

**Website NAP Placement:**
- NAP should appear in the site footer (every page)
- NAP should appear on the Contact page
- NAP should be in LocalBusiness schema markup
- NAP text must be crawlable (not embedded in images)
- Phone number should be a clickable `tel:` link

### 2. Major Directories (6 points)

| Directory | Industry Focus | Check |
|-----------|---------------|-------|
| Yelp | General | Name, address, phone, hours, categories |
| Facebook Business | General | Name, address, phone, hours |
| Yellow Pages (YP.com) | General | Name, address, phone |
| BBB (Better Business Bureau) | General / Trust | Name, address, phone |
| Industry-Specific #1 | Varies | Name, address, phone |
| Industry-Specific #2 | Varies | Name, address, phone |

**Industry-Specific Directories by Vertical:**

| Industry | Key Directories |
|----------|----------------|
| Restaurants | OpenTable, TripAdvisor, Zomato, Grubhub |
| Hotels/Lodging | TripAdvisor, Booking.com, Expedia, Hotels.com |
| Healthcare | Healthgrades, Vitals, WebMD, Zocdoc |
| Legal | Avvo, FindLaw, Justia, Lawyers.com |
| Real Estate | Zillow, Realtor.com, Trulia |
| Home Services | HomeAdvisor, Angi, Thumbtack, Houzz |
| Automotive | Cars.com, AutoTrader, CarGurus |
| Financial | NerdWallet, Bankrate, WalletHub |

### 3. Data Aggregators (6 points)

Data aggregators feed NAP data to hundreds of directories. Fixing NAP at the aggregator level cascades corrections downstream.

| Aggregator | Coverage | Points |
|------------|----------|--------|
| Data Axle (InfoUSA) | 100+ directories | 2 |
| Neustar Localeze | 100+ directories | 2 |
| Foursquare | Social + directories | 1 |
| Factual | Apps + directories | 1 |

## NAP Consistency Rules

### Name Consistency
- Use the exact legal business name everywhere
- Do not abbreviate inconsistently ("LLC" vs no "LLC")
- Do not add location modifiers on some platforms and not others
- Do not add keywords to the name on any platform

**Common Name Inconsistencies:**
```
INCONSISTENT:
- "Joe's Plumbing"
- "Joe's Plumbing LLC"
- "Joe's Plumbing - Dallas"
- "Joes Plumbing" (missing apostrophe)

CONSISTENT:
- "Joe's Plumbing LLC" (everywhere)
```

### Address Consistency
- Use identical formatting everywhere
- Standardize abbreviations (always "St" or always "Street" — pick one)
- Include or exclude suite/unit numbers consistently
- Use USPS-standardized format as the canonical version

**Common Address Inconsistencies:**
```
INCONSISTENT:
- "123 Main Street, Suite 100"
- "123 Main St, Ste 100"
- "123 Main St #100"
- "123 Main Street"  (missing suite)

CONSISTENT (USPS Standard):
- "123 Main St Ste 100" (everywhere)
```

**USPS Address Standardization:**
- Street → St
- Avenue → Ave
- Boulevard → Blvd
- Drive → Dr
- Lane → Ln
- Road → Rd
- Suite → Ste
- Apartment → Apt
- No periods after abbreviations
- No commas between street and suite

### Phone Consistency
- Use identical formatting everywhere
- Choose one format: (214) 555-1234 or 214-555-1234 or 2145551234
- Use a local number, not toll-free (unless national brand)
- If using call tracking, only use tracking number on website — real number on all directories and GBP

**Call Tracking Warning:**
Using different call tracking numbers on different directories creates NAP inconsistency. Best practice:
1. Real local number on GBP and all directories
2. Call tracking number on website only
3. Or use a DNI (Dynamic Number Insertion) solution that swaps numbers on-page without affecting the crawled HTML

## Scoring

| Consistency Level | Points Deducted |
|-------------------|----------------|
| Exact match | 0 |
| Minor variation (abbreviation) | -0.5 per source |
| Major variation (wrong info) | -1 per source |
| Missing listing | -1 per source |
| Duplicate listing | -1.5 per source |

**Total possible: 20 points**

## Output Format

```
NAP CONSISTENCY AUDIT: [Business Name]
Score: [X]/20 ([Grade])

CANONICAL NAP:
  Name:    Joe's Plumbing LLC
  Address: 123 Main St Ste 100, Dallas, TX 75201
  Phone:   (214) 555-1234

PRIMARY SOURCES:
  [MATCH]     Google Business Profile
  [MISMATCH]  Website — Phone shows (214) 555-0000 (old number)
  [MATCH]     Apple Maps
  [MISSING]   Bing Places — No listing found

MAJOR DIRECTORIES:
  [MATCH]     Yelp
  [MISMATCH]  Facebook — Name shows "Joe's Plumbing" (missing LLC)
  [MISMATCH]  Yellow Pages — Address shows "123 Main Street" (not standardized)
  [MATCH]     BBB

DATA AGGREGATORS:
  [MATCH]     Data Axle
  [UNKNOWN]   Neustar Localeze — Unable to verify
  [MISMATCH]  Foursquare — Old address on file

DUPLICATES FOUND:
  - Yelp: 2 listings found (merge required)
  - Google: 1 duplicate at old address (request removal)

PRIORITY FIXES:
1. [Critical] Update phone number on website to match GBP
2. [High] Claim and fix Bing Places listing
3. [High] Merge duplicate Yelp listings
4. [Medium] Standardize Facebook business name to include LLC
5. [Medium] Update Yellow Pages address formatting
6. [Low] Submit corrections to Foursquare
```

## How to Fix NAP Issues

### Step 1: Establish Canonical NAP
- Use USPS-standardized address
- Use the exact legal business name
- Choose one phone number format

### Step 2: Fix Primary Sources First
1. Update GBP
2. Update website (footer, contact page, schema)
3. Claim/update Apple Maps and Bing Places

### Step 3: Fix Data Aggregators
- Submit corrections to Data Axle and Neustar Localeze
- Changes cascade to 100+ downstream directories over 2-8 weeks

### Step 4: Fix Major Directories
- Claim and update each listing manually
- Remove duplicates (merge where possible)

### Step 5: Monitor Monthly
- Re-run `/local nap` check monthly
- New inconsistencies appear as data aggregators resync

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
