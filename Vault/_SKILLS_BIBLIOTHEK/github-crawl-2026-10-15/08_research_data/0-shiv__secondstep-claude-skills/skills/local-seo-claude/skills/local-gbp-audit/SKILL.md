# Local GBP Audit — Google Business Profile Completeness

## Description

Audits a Google Business Profile listing for completeness, accuracy, and optimization against Google's best practices. A complete GBP listing makes your business 2.7x more likely to be considered reputable and 70% more likely to attract location visits.

## Command

```
/local gbp "Business Name"
/local gbp "Business Name" "City, State"
```

## What Gets Audited

### 1. Business Identity (5 points)

| Field | Check | Points |
|-------|-------|--------|
| Business Name | Matches legal name, no keyword stuffing | 1 |
| Primary Category | Most specific category selected | 2 |
| Secondary Categories | 2-5 relevant categories added | 1 |
| Business Description | 750 characters, keyword-rich, no links | 1 |

**Business Name Rules:**
- Must match the real-world business name exactly
- No geographic modifiers unless part of legal name
- No keywords appended (e.g., "Joe's Plumbing | Best Plumber in Dallas" is a violation)
- Violations risk suspension

**Category Selection:**
- Primary category is the single most important GBP ranking factor
- Choose the most specific category available (e.g., "Vietnamese Restaurant" over "Restaurant")
- Add 2-5 secondary categories that describe additional services
- Do not add categories you do not directly serve

**Description Best Practices:**
- Use all 750 characters
- Lead with your primary service and location
- Include natural keyword variations
- Mention what differentiates you from competitors
- No URLs, phone numbers, or promotional language
- No ALL CAPS

### 2. Contact & Location (5 points)

| Field | Check | Points |
|-------|-------|--------|
| Phone Number | Local number (not toll-free unless national brand) | 1 |
| Website URL | Points to correct landing page | 1 |
| Address | Complete, matches website and directories | 1 |
| Service Area | Defined if service-area business | 1 |
| Appointment URL | Set if business takes appointments | 1 |

**Phone Number:**
- Local area code strongly preferred
- Must match website and all directory listings exactly
- Call tracking numbers: use on website only, keep real number on GBP
- Enable messaging if you can respond within 24 hours

**Service Area Businesses (SAB):**
- Hide street address if you go to customers (plumbers, cleaners, etc.)
- Define service areas by city, county, or zip code
- Maximum 20 service areas
- Do not set a radius larger than 2 hours driving distance

### 3. Hours & Attributes (5 points)

| Field | Check | Points |
|-------|-------|--------|
| Regular Hours | Set for all 7 days | 1 |
| Special Hours | Holiday hours set for next 3 months | 1 |
| More Hours | Department-specific hours if applicable | 0.5 |
| Attributes | All relevant attributes selected | 1.5 |
| From the Business | Highlights section completed | 1 |

**Attributes to Check:**
- Accessibility: wheelchair accessible entrance/parking/seating
- Amenities: Wi-Fi, restroom, parking
- Crowd: LGBTQ+ friendly, family-friendly
- Dining: dine-in, takeout, delivery, curbside pickup
- Health & Safety: mask required, staff vaccinated
- Payments: credit cards, NFC, checks
- Service Options: online appointments, on-site services

### 4. Photos & Media (5 points)

| Field | Check | Points |
|-------|-------|--------|
| Cover Photo | High-quality, represents business | 1 |
| Logo | Clear, matches brand | 0.5 |
| Exterior Photos | 3+ photos showing entrance from different angles | 1 |
| Interior Photos | 3+ photos showing inside the business | 1 |
| Team Photos | 2+ photos of staff/team | 0.5 |
| Product/Service Photos | 5+ photos of products or work examples | 1 |

**Photo Requirements:**
- Format: JPG or PNG
- Size: between 10 KB and 5 MB
- Resolution: 720px minimum on each side
- No stock photos — Google can detect and penalize
- Geo-tag photos with business location before uploading
- Add new photos weekly to signal activity

**Photo Benchmarks:**
- Businesses with 100+ photos get 520% more calls than average
- Businesses with 100+ photos get 2,717% more direction requests
- Minimum viable: 25 photos across all categories

### 5. Engagement Features (5 points)

| Field | Check | Points |
|-------|-------|--------|
| Google Posts | Active posts (within last 7 days) | 1 |
| Products/Services | Listed with descriptions and prices | 1.5 |
| Q&A | Seeded with common questions and answers | 1 |
| Booking Button | Integrated if applicable | 0.5 |
| Verification Status | Verified (mandatory) | 1 |

**Google Posts Best Practices:**
- Post at least weekly (posts expire after 7 days)
- Types: What's New, Events, Offers, Products
- Include a CTA button (Learn More, Book, Call, etc.)
- Add a high-quality image to every post
- Keep text under 300 words, front-load important info
- Track post views and clicks in GBP Insights

**Products & Services:**
- List every service with a clear description
- Include pricing where possible (even ranges)
- Group services into logical categories
- Link each product/service to a relevant landing page

**Q&A Management:**
- Seed 10-15 frequently asked questions yourself
- Answer your own seeded questions with detailed, keyword-rich responses
- Monitor for new questions daily — anyone can answer
- Report spam/fake questions
- Upvote your own answers to keep them on top

## Output Format

```
GBP AUDIT: [Business Name]
Score: [X]/25 ([Grade])

BUSINESS IDENTITY: [X]/5
  [PASS] Business name matches legal name
  [FAIL] Only 1 secondary category (need 2-5)
  [PASS] Description is 748/750 characters
  ...

CONTACT & LOCATION: [X]/5
  ...

HOURS & ATTRIBUTES: [X]/5
  ...

PHOTOS & MEDIA: [X]/5
  ...

ENGAGEMENT: [X]/5
  ...

PRIORITY ACTIONS:
1. [High] Add 3 more secondary categories
2. [High] Upload 15 more photos (currently at 10)
3. [Medium] Create weekly Google Posts schedule
4. [Low] Seed Q&A section with 10 common questions
```

## Common GBP Issues

1. **Keyword-stuffed business name** — #1 cause of suspension
2. **Wrong primary category** — biggest single ranking factor
3. **No photos or stock photos only** — kills trust signals
4. **Stale profile** — no posts, no new photos, no Q&A
5. **Unverified listing** — invisible in local pack
6. **Missing special hours** — hurts user experience, triggers "might be closed"
7. **Duplicate listings** — confuses Google, splits authority

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
