# Local Content — Local Content Strategy Evaluation

## Description

Evaluates a business website's local content strategy, including location pages, service area pages, locally-focused blog content, and on-page local signals. Local content is a core on-page ranking factor (~17% of the local algorithm) that establishes geographic relevance, builds topical authority, and creates landing pages for location-specific searches.

## Command

```
/local content https://example.com
/local content https://example.com --locations "Dallas, Fort Worth, Plano"
```

## What Gets Evaluated

### 1. Location Pages (3 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Dedicated location page exists | One page per physical location | 1 |
| Unique content per page | Not duplicate/boilerplate across locations | 1 |
| Local signals on page | Address, map embed, local photos, directions | 0.5 |
| Proper URL structure | `/locations/city-name` or `/city-name` | 0.5 |

**Location Page Must-Haves:**
- H1 with city/neighborhood name + primary service
- Full NAP with schema markup
- Embedded Google Map
- Local photos (storefront, team, neighborhood landmarks)
- Unique 500+ word description mentioning local landmarks, neighborhoods, cross-streets
- Service list specific to that location
- Customer testimonials from local clients
- Clear CTA (call, book, get directions)

**Location Page URL Structure:**
```
Single location:   /contact or /location
Multi-location:    /locations/dallas-tx
                   /locations/fort-worth-tx
Service area:      /service-areas/plano-tx
```

**What NOT to do:**
- Doorway pages (thin pages targeting every city in the state with no real content)
- Duplicate content with only the city name swapped
- Creating location pages for cities where you have no physical presence or real service history
- Keyword-stuffed city names in headings

### 2. Service Area Pages (3 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Service area pages exist | For top 3-5 service areas beyond primary city | 1 |
| Unique, substantial content | 800+ words with local context | 1 |
| Local proof elements | Case studies, testimonials, photos from that area | 0.5 |
| Internal linking | Linked from main service pages and navigation | 0.5 |

**Service Area Page Framework:**

Each service area page should follow this structure:

1. **Hero section:** "[Service] in [City/Area]" + brief value proposition
2. **Local context:** Why you serve this area, how far from HQ, neighborhoods covered
3. **Services available:** Full service descriptions (not just a list)
4. **Social proof:** Reviews/testimonials from customers in that area
5. **Local case study:** A specific project or client story from that area
6. **Local landmarks:** Reference nearby landmarks, major roads, neighborhoods
7. **FAQ section:** Location-specific questions
8. **CTA:** Area-specific phone number or booking link

**Content Differentiation Checklist:**
- [ ] Mentions specific neighborhoods within the service area
- [ ] References local landmarks, roads, or geography
- [ ] Includes a local case study or project example
- [ ] Has testimonials from customers in that area
- [ ] Uses area-specific photos (not stock or recycled from other pages)
- [ ] Lists area-specific pricing if it varies by location

### 3. Local Blog Content (2 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Local blog posts exist | At least 5 locally-focused posts | 0.5 |
| Publishing frequency | At least 2 local posts per month | 0.5 |
| Content quality | 800+ words, original, locally relevant | 0.5 |
| Internal linking | Blog posts link to service/location pages | 0.5 |

**Local Blog Content Ideas:**

| Content Type | Example | SEO Value |
|-------------|---------|-----------|
| Local event coverage | "Best [City] Events This [Season]" | Local relevance + freshness |
| Community involvement | "How We Partnered with [Local Org]" | E-E-A-T + local authority |
| Local guides | "Complete Guide to [Topic] in [City]" | Long-tail local keywords |
| Case studies | "[Service] Project in [Neighborhood]" | Service + location keywords |
| Industry + location | "Why [City] Homeowners Need [Service]" | Intent + geographic targeting |
| Seasonal local | "[Season] [Service] Tips for [City] Residents" | Seasonal + local relevance |
| Comparison | "[City] vs [City]: Which is Better for [Topic]" | Geographic keyword expansion |

### 4. On-Page Local Signals (2 points)

| Check | Requirement | Points |
|-------|-------------|--------|
| Title tags | City + service in title tags | 0.5 |
| Meta descriptions | City mentioned in meta descriptions | 0.25 |
| Header tags | H1/H2 includes location naturally | 0.25 |
| Image alt text | Location references in alt text | 0.25 |
| Internal linking | Location pages cross-linked with service pages | 0.25 |
| Footer NAP | NAP in footer on every page | 0.25 |
| Local phone number | Clickable tel: link in header/footer | 0.25 |

**Title Tag Formula:**
```
[Primary Service] in [City, ST] | [Business Name]
Example: "Emergency Plumbing in Dallas, TX | Joe's Plumbing LLC"
```

**On-Page Content Checklist:**
- [ ] City/state in the page title tag
- [ ] City mentioned in the first 100 words of body content
- [ ] City/neighborhood in at least one H2
- [ ] Local photos with geo-tagged EXIF data
- [ ] Alt text includes location (naturally, not stuffed)
- [ ] NAP in footer (crawlable text, not image)
- [ ] Phone number as `tel:` link
- [ ] Embedded Google Map on contact/location page

## Content Quality Scoring

| Quality Level | Criteria | Score Multiplier |
|---------------|----------|-----------------|
| Excellent | Unique, 1000+ words, local proof, multimedia | 1.0x |
| Good | Unique, 800+ words, some local context | 0.8x |
| Fair | Mostly unique, 500+ words, basic local mentions | 0.5x |
| Poor | Thin, duplicate, or boilerplate with city swapped | 0.2x |
| Doorway | Auto-generated pages for dozens of cities | 0x (penalty risk) |

## Output Format

```
LOCAL CONTENT AUDIT: [URL]
Score: [X]/10 ([Grade])

LOCATION PAGES:
  [PASS] /locations/dallas — Unique content, 1,200 words, map + schema
  [WARN] /locations/fort-worth — Thin content (280 words), no local photos
  [FAIL] /locations/plano — Duplicate of Dallas page with city name swapped
  Subtotal: [X]/3

SERVICE AREA PAGES:
  [PASS] /service-areas/richardson — Good: 900 words, local case study
  [MISS] No page for Arlington (high-volume service area)
  [MISS] No page for Irving (high-volume service area)
  Subtotal: [X]/3

LOCAL BLOG CONTENT:
  Posts found: 8 total, 3 locally-focused
  Last local post: 45 days ago
  [WARN] Only 3 of 8 posts have local relevance
  [WARN] No local posts in last 30 days
  Subtotal: [X]/2

ON-PAGE SIGNALS:
  [PASS] Title tags include city on location pages
  [FAIL] Meta descriptions missing city on service pages
  [PASS] Footer NAP on all pages
  [PASS] Clickable tel: link in header
  [WARN] No image alt text includes location
  Subtotal: [X]/2

PRIORITY ACTIONS:
1. [Critical] Rewrite Plano location page with unique content
2. [High] Expand Fort Worth page to 800+ words with local proof
3. [High] Create service area pages for Arlington and Irving
4. [Medium] Publish 2 locally-focused blog posts per month
5. [Medium] Add city to meta descriptions on service pages
6. [Low] Add location to image alt text where natural
```

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
