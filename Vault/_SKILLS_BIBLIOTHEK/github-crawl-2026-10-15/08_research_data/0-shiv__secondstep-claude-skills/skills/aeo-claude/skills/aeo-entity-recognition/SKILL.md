# AEO Entity Recognition — AI Entity Optimization

## Description

The entity recognition sub-skill ensures that AI engines recognize your business, brand, or organization as a **distinct, identifiable entity** rather than a generic term or ambiguous reference. AI engines must resolve entity identity before they can attribute information — if the engine cannot confidently identify *which* "Acme Corp" you are, it will avoid citing you entirely.

Entity Recognition carries 10% of the total AEO Visibility Score. While lower-weighted than content dimensions, it is a foundational requirement — poor entity recognition creates a ceiling that limits the effectiveness of all other AEO efforts.

## Command

```
/aeo entity <url|brand_name> [--type organization|person|product]
```

## Why Entity Recognition Matters for AEO

AI engines process information through an **entity-centric** lens. When a user asks ChatGPT "What is the best supply chain automation platform?", the engine:

1. Identifies the **entity type** being asked about (software product)
2. Searches its knowledge for **recognized entities** in that category
3. Evaluates **entity authority signals** for each candidate
4. Selects the entities with the **strongest recognition signals** to cite

If your brand is not recognized as a distinct entity, it cannot enter step 2 — regardless of how good your content is. Entity recognition is the gateway to AI citation.

## What Gets Measured

### 1. Knowledge Panel Signals (30 points)

Google's Knowledge Panel is the strongest signal that an entity is recognized by AI systems. The skill checks:

- **Knowledge Panel existence** — Does searching your brand name trigger a Knowledge Panel?
- **Panel completeness** — Does it include description, category, founding date, location, social profiles?
- **Panel accuracy** — Is the information correct and up-to-date?
- **Panel source** — Is it sourced from Wikipedia, Wikidata, or verified business data?
- **Related entities** — Are competitors, industry, and related brands correctly linked?

**Scoring:**
- No Knowledge Panel = 0-5 points
- Partial/inaccurate Panel = 6-15 points
- Complete, accurate Panel = 16-25 points
- Panel with rich data (founded, CEO, revenue, etc.) = 26-30 points

### 2. Wikidata Presence (20 points)

Wikidata is the structured data backbone that many AI engines use for entity resolution:

- **Wikidata entry exists** — Does the entity have a QID?
- **Properties populated** — Instance of, industry, country, official website, social media
- **Relationships mapped** — Subsidiaries, parent company, founders, competitors
- **External identifiers** — Links to other knowledge bases (Freebase, VIAF, ISNI)
- **Wikipedia link** — Wikidata entry connected to a Wikipedia article

**Scoring:**
- No Wikidata entry = 0 points
- Entry with minimal properties = 1-8 points
- Entry with 10+ properties = 9-14 points
- Entry with Wikipedia link + full relationships = 15-20 points

### 3. NAP Consistency (25 points)

Name, Address, Phone (NAP) consistency across the web is a strong entity disambiguation signal:

- **Business name consistency** — Same exact name used across all platforms (website, Google Business Profile, LinkedIn, social media, directories)
- **Address format consistency** — Identical address formatting across all listings
- **Phone number consistency** — Same phone number with consistent formatting
- **URL consistency** — Consistent use of www vs non-www, trailing slashes
- **Cross-platform verification** — Name matches across Google, Bing, Apple Maps, Yelp, industry directories

**Common issues detected:**
- "Example Corp" vs "Example Corporation" vs "Example Corp, Inc."
- Different phone numbers on website vs Google Business Profile
- Outdated addresses on directory listings
- Inconsistent URLs across social media profiles

### 4. Schema.org Organization Markup (25 points)

Structured data markup provides explicit entity signals that AI engines can parse:

- **Organization schema present** — `@type: Organization` or more specific type
- **Required properties** — name, url, logo, description
- **Recommended properties** — foundingDate, founders, numberOfEmployees, address
- **Social profiles** — sameAs property linking to all social media profiles
- **Contact information** — contactPoint with type, telephone, email
- **Additional types** — LocalBusiness, Corporation, EducationalOrganization as appropriate
- **JSON-LD format** — Preferred format for schema markup (over Microdata/RDFa)

**Scoring breakdown:**
- No schema markup = 0 points
- Basic Organization schema = 1-8 points
- Complete Organization with social links = 9-16 points
- Full schema with ContactPoint, founders, employees = 17-25 points

## Output Format

```markdown
## Entity Recognition Score: [XX]/100

### Entity: [Brand/Organization Name]
### Entity Type: [Organization/Person/Product]

### Knowledge Panel
- Status: [Found/Not Found]
- Completeness: [XX]%
- Accuracy: [Verified/Issues Found]
- Source: [Wikipedia/Google/Wikidata]

### Wikidata
- QID: [QXXXXXXX / Not Found]
- Properties: [N] populated
- Wikipedia link: [Yes/No]
- External identifiers: [N]

### NAP Consistency
- Platforms checked: [N]
- Consistent: [N] ([%])
- Inconsistencies found: [N]
- Most common name variant: "[Name]"

### Schema.org Markup
- Present: [Yes/No]
- Type: [@type value]
- Properties: [N]/[Total recommended]
- Social profiles linked: [N]
- Format: [JSON-LD/Microdata/RDFa]

### Entity Disambiguation
- Unique entity: [Yes/Conflicts detected]
- Competing entities: [List of entities with similar names]
- Disambiguation signals: [What makes this entity distinct]

### Recommendations
1. [Highest-priority action]
2. [Second action]
3. [Third action]

### Schema.org Markup Template
```json
[Generated schema markup for the entity]
```
```

## Entity Building Strategies

### Quick Wins (1-2 weeks)
- Add comprehensive Organization schema markup to your homepage
- Ensure NAP consistency across Google Business Profile, LinkedIn, and website
- Create or update your Wikidata entry with basic properties
- Claim and complete profiles on all major platforms using exact brand name

### Medium Effort (1-3 months)
- Build Wikipedia notability through press coverage (3+ independent, reliable sources)
- Add `sameAs` schema property linking to all verified social profiles
- Fix NAP inconsistencies across all directory listings
- Add founder/leadership schema markup with person entities

### High Effort (3-6 months)
- Achieve Knowledge Panel through sustained entity signals
- Get featured in industry databases and authoritative directories
- Create entity relationships in Wikidata (industry, competitors, products)
- Develop a brand consistency guide for all external communications

## Integration

This sub-skill feeds the Entity Recognition dimension (10% weight) of the composite AEO Visibility Score. It can be run standalone or as part of `/aeo audit`.

Entity recognition is foundational — improving entity signals amplifies the effectiveness of all other AEO dimensions, particularly Brand Authority and Knowledge Graph positioning.
