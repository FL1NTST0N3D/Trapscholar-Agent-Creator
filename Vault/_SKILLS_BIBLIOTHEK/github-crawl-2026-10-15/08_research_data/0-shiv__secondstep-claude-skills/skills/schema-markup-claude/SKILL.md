# Schema Markup Generator

Generate, validate, and deploy JSON-LD structured data for 20+ schema types. Optimized for Google rich results eligibility.

## Commands

- `/schema generate <type>` -- Generate JSON-LD schema for any supported type
- `/schema organization` -- Organization schema with social profiles and contact points
- `/schema local-business` -- LocalBusiness with NAP, hours, geo coordinates, service areas
- `/schema product` -- Product + Offer schema for e-commerce pages
- `/schema faq` -- FAQPage with Question/Answer pairs
- `/schema howto` -- HowTo with steps, tools, supplies, timing
- `/schema article` -- Article, BlogPosting, or NewsArticle schema
- `/schema video` -- VideoObject with thumbnails, duration, livestream support
- `/schema breadcrumb` -- BreadcrumbList for site navigation hierarchy
- `/schema event` -- Event with location, performer, offers, status
- `/schema validate` -- Validate existing schema against Google requirements
- `/schema report` -- Schema coverage report for a site or page set

## Context

Structured data (schema markup) tells search engines exactly what your content is about. When implemented correctly as JSON-LD, it enables rich results in Google Search -- star ratings, FAQ dropdowns, recipe cards, event listings, product prices, and more. Pages with rich results capture 58% of clicks on average, with CTR improvements of 20-30% being typical.

Google recommends JSON-LD as the preferred format for structured data. This skill generates exclusively JSON-LD markup, validates it against both the Schema.org specification and Google's stricter rich result requirements, and provides deployment guidance for any platform.

### Schema.org vs Google Requirements

Schema.org defines 800+ types with thousands of properties. Google supports rich results for a subset of approximately 30 types, and within those types, Google requires specific properties beyond what Schema.org mandates. This skill handles both layers:

- **Schema.org compliance**: Valid vocabulary, correct types, proper nesting
- **Google rich result eligibility**: Required properties for each supported rich result type, content policies, technical requirements

### 2023-2024 Changes

Google significantly restricted FAQ and HowTo rich results in August 2023. FAQ rich results now only appear for well-known government and health websites. HowTo rich results were removed from Google Search entirely. This skill still generates valid schema for these types (useful for Bing and other engines) but clearly flags the Google restrictions.

### Output Format

All schema output follows this pattern:

1. Complete JSON-LD wrapped in `<script type="application/ld+json">` tags
2. Comments explaining each property's purpose
3. Validation notes (required vs recommended properties)
4. Rich result eligibility status
5. Implementation instructions for the target platform

### Supported Platforms

- WordPress (Yoast, RankMath, custom theme injection)
- Shopify (theme.liquid, section schema)
- Next.js / React (Head component, next-seo)
- Google Tag Manager (Custom HTML tag)
- Static HTML (direct script injection)
- Any CMS with custom code injection

### Multi-Schema Pages

Many pages need multiple schema types. A product page might need Product + BreadcrumbList + Organization. A blog post might need Article + BreadcrumbList + FAQPage. This skill handles multi-schema generation with proper `@graph` notation when combining types on a single page.

### Validation Pipeline

The validation sub-skill checks schema against:

1. JSON syntax validity
2. Schema.org vocabulary compliance
3. Google required property checklist
4. Google content policy alignment
5. URL accessibility (if URLs are provided)
6. Image dimension requirements
7. Date format compliance (ISO 8601)
8. Deprecated property detection

### Integration with SEO Workflow

Schema markup is one layer of a complete SEO strategy. This skill integrates with broader SEO workflows:

- **Technical SEO**: Schema is part of the technical foundation alongside sitemaps, robots.txt, and page speed
- **Content strategy**: Schema types should align with content types (articles get Article schema, products get Product schema)
- **Local SEO**: LocalBusiness schema must match Google Business Profile data exactly
- **E-commerce SEO**: Product schema feeds Google Shopping and Merchant Center

## Sub-Skills

Each schema type has a dedicated sub-skill with deep knowledge of that type's properties, requirements, common mistakes, and best practices. See the `skills/` directory for individual sub-skill documentation.
