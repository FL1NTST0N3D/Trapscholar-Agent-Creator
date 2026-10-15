# Local Schema — LocalBusiness Structured Data Validation

## Description

Validates LocalBusiness schema markup (JSON-LD) on a business website against Google's requirements and best practices. Proper schema markup helps Google understand the business entity, can trigger rich results, and reinforces NAP consistency signals. Schema errors or missing properties reduce local ranking potential and can prevent rich result eligibility.

## Command

```
/local schema https://example.com
/local schema https://example.com/locations/dallas
```

## What Gets Validated

### 1. Schema Presence & Format (3 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Schema exists | LocalBusiness (or subtype) markup found on page | 1 |
| Format is JSON-LD | Not Microdata or RDFa (JSON-LD is Google's preferred format) | 1 |
| Placed in `<head>` or `<body>` | Valid HTML placement | 0.5 |
| No syntax errors | Valid JSON, no trailing commas, proper escaping | 0.5 |

**Supported Schema Types:**

Use the most specific subtype available:

| Business Type | Schema Type |
|---------------|-------------|
| General | `LocalBusiness` |
| Restaurant | `Restaurant` |
| Bar | `BarOrPub` |
| Dentist | `Dentist` |
| Physician | `Physician` |
| Attorney | `Attorney` |
| Auto Dealer | `AutoDealer` |
| Auto Repair | `AutoRepair` |
| Beauty Salon | `BeautySalon` |
| Hotel | `Hotel` or `LodgingBusiness` |
| Real Estate | `RealEstateAgent` |
| Gym | `HealthClub` |
| Store | `Store` |
| Plumber | `Plumber` |
| Electrician | `Electrician` |
| HVAC | `HVACBusiness` |

### 2. Required Properties (4 points)

| Property | Check | Points |
|----------|-------|--------|
| `@type` | Correct LocalBusiness subtype | 0.5 |
| `name` | Matches GBP and canonical NAP | 0.5 |
| `address` (PostalAddress) | Complete: street, city, state, zip, country | 1 |
| `telephone` | Matches GBP and canonical NAP | 0.5 |
| `url` | Points to correct page | 0.25 |
| `image` | Valid image URL | 0.25 |
| `openingHoursSpecification` | Hours for each day | 0.5 |
| `geo` (GeoCoordinates) | Latitude and longitude present | 0.5 |

**Minimum Viable Schema (JSON-LD):**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Joe's Plumbing LLC",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St Ste 100",
    "addressLocality": "Dallas",
    "addressRegion": "TX",
    "postalCode": "75201",
    "addressCountry": "US"
  },
  "telephone": "(214) 555-1234",
  "url": "https://www.joesplumbing.com",
  "image": "https://www.joesplumbing.com/images/storefront.jpg",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 32.7767,
    "longitude": -96.7970
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "08:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "09:00",
      "closes": "14:00"
    }
  ]
}
```

### 3. Recommended Properties (2 points)

| Property | Description | Points |
|----------|-------------|--------|
| `description` | Business description (match GBP) | 0.25 |
| `priceRange` | "$" to "$$$$" scale | 0.25 |
| `areaServed` | Service area definition | 0.25 |
| `sameAs` | Social profile URLs (Facebook, Yelp, etc.) | 0.25 |
| `aggregateRating` | Star rating + review count | 0.25 |
| `review` | Individual review markup | 0.25 |
| `hasMap` | Google Maps embed URL | 0.125 |
| `paymentAccepted` | Payment methods | 0.125 |

**`sameAs` Best Practice:**
```json
"sameAs": [
  "https://www.facebook.com/joesplumbing",
  "https://www.yelp.com/biz/joes-plumbing-dallas",
  "https://www.instagram.com/joesplumbing",
  "https://twitter.com/joesplumbing"
]
```

### 4. Multi-Location Schema (1 point)

For businesses with multiple locations:

| Check | Requirement | Points |
|-------|-------------|--------|
| Organization + locations | Parent `Organization` with child `LocalBusiness` entities | 0.5 |
| Unique schema per location | Each location page has its own schema block | 0.5 |

**Multi-Location Pattern:**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Joe's Plumbing LLC",
  "url": "https://www.joesplumbing.com",
  "subOrganization": [
    {
      "@type": "Plumber",
      "name": "Joe's Plumbing LLC - Dallas",
      "address": { ... },
      "url": "https://www.joesplumbing.com/locations/dallas"
    },
    {
      "@type": "Plumber",
      "name": "Joe's Plumbing LLC - Fort Worth",
      "address": { ... },
      "url": "https://www.joesplumbing.com/locations/fort-worth"
    }
  ]
}
```

## Testing & Validation Tools

| Tool | URL | Purpose |
|------|-----|---------|
| Google Rich Results Test | https://search.google.com/test/rich-results | Test if markup qualifies for rich results |
| Schema.org Validator | https://validator.schema.org | Validate against schema.org spec |
| Google Search Console | Enhancements > Unparsable structured data | Monitor schema errors at scale |

## Output Format

```
SCHEMA VALIDATION: [URL]
Score: [X]/10 ([Grade])

PRESENCE & FORMAT:
  [PASS] LocalBusiness schema found (type: Restaurant)
  [PASS] Format: JSON-LD
  [PASS] Valid JSON syntax
  [PASS] Placed in <head>

REQUIRED PROPERTIES:
  [PASS] @type: Restaurant
  [PASS] name: "Joe's Italian Kitchen"
  [PASS] address: Complete PostalAddress
  [FAIL] telephone: Missing
  [PASS] url: https://www.joesitaliankitchen.com
  [WARN] image: Present but low resolution (400px)
  [FAIL] openingHoursSpecification: Missing
  [PASS] geo: Lat/Long present

RECOMMENDED PROPERTIES:
  [PASS] description: Present (320 characters)
  [PASS] priceRange: "$$"
  [MISS] areaServed: Not set
  [PASS] sameAs: 3 social profiles linked
  [MISS] aggregateRating: Not set
  [MISS] review: Not set

MULTI-LOCATION: N/A (single location)

NAP CONSISTENCY CHECK:
  [PASS] Schema NAP matches GBP
  [WARN] Schema phone missing — cannot validate

PRIORITY ACTIONS:
1. [Critical] Add telephone property to schema
2. [Critical] Add openingHoursSpecification
3. [Medium] Add aggregateRating markup
4. [Low] Add areaServed property
5. [Low] Upgrade image to 720px+ resolution
```

## Common Schema Mistakes

1. **Using Microdata instead of JSON-LD** — Google strongly prefers JSON-LD; easier to implement and maintain
2. **Missing geo coordinates** — Required for local pack eligibility; use Google Maps to find exact lat/long
3. **NAP mismatch between schema and GBP** — Schema must be byte-for-byte consistent with GBP
4. **Hardcoded hours that are never updated** — Keep schema hours in sync with GBP special hours
5. **Using `LocalBusiness` when a subtype exists** — Always use the most specific type (e.g., `Dentist` not `LocalBusiness`)
6. **Invalid JSON syntax** — Trailing commas, unescaped quotes, missing brackets
7. **Duplicate schema blocks** — Multiple conflicting LocalBusiness blocks on the same page
8. **Self-serving reviews in schema** — Google penalizes fake or gated review markup

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
