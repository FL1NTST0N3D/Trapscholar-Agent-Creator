# Schema Markup Generator for Claude Code

> Rich results get 58% of clicks. This skill generates, validates, and deploys JSON-LD structured data for 20+ schema types.

[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-blue)](https://github.com/0-shiv/schema-markup-claude)
[![Schema.org](https://img.shields.io/badge/Schema.org-v26.0-green)](https://schema.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Why Schema Markup Matters

| Metric | Value |
|--------|-------|
| Clicks to rich results | **58%** of all SERP clicks |
| CTR increase with schema | **20-30%** average lift |
| Domains using Schema.org | **45M+** worldwide |
| Available schema types | **800+** in the Schema.org vocabulary |

Structured data is no longer optional. Google, Bing, and AI engines rely on JSON-LD schema to understand page content, power rich results (stars, FAQs, breadcrumbs, product cards), and feed AI-generated answers. Without it, you are invisible to the machines that decide what users see.

---

## Quick Start

### Install

```bash
claude skill install 0-shiv/schema-markup-claude
```

### Usage

```
/schema generate <type>        Generate schema for any supported type
/schema organization           Organization schema with social profiles
/schema local-business         LocalBusiness with NAP, hours, geo
/schema product                Product + Offer for e-commerce
/schema faq                    FAQPage with Q&A pairs
/schema howto                  HowTo with steps, tools, supplies
/schema article                Article/BlogPosting/NewsArticle
/schema video                  VideoObject + BroadcastEvent
/schema breadcrumb             BreadcrumbList navigation paths
/schema event                  Event with location, performer, offers
/schema validate               Validate existing schema markup
/schema report                 Schema coverage report for a site
```

---

## Supported Schema Types

### Core Types (11 dedicated sub-skills)
- **Organization** -- Company identity, logo, social profiles, contact points
- **LocalBusiness** -- NAP consistency, opening hours, geo coordinates, service areas
- **Product** -- E-commerce: price, availability, reviews, SKU/GTIN
- **FAQPage** -- Question/Answer pairs (note 2023 Google restrictions)
- **HowTo** -- Step-by-step instructions with tools and supplies
- **Article** -- Blog posts, news articles, author attribution
- **VideoObject** -- Video metadata, thumbnails, livestream support
- **BreadcrumbList** -- Navigation hierarchy for large sites
- **Event** -- Physical and virtual events with ticketing
- **Validator** -- Error checking, deprecation warnings, eligibility audit
- **Report** -- Site-wide schema coverage and opportunity analysis

### Additional Types (via /schema generate)
- Service, Review, SoftwareApplication, Course, Recipe, JobPosting, Person, WebSite, SearchAction, Speakable, and more

---

## Project Structure

```
schema-markup-claude/
  SKILL.md                    # Main skill definition
  skills/
    schema-organization/      # Organization schema sub-skill
    schema-local-business/    # LocalBusiness schema sub-skill
    schema-product/           # Product + Offer sub-skill
    schema-faq/               # FAQPage sub-skill
    schema-howto/             # HowTo sub-skill
    schema-article/           # Article/BlogPosting sub-skill
    schema-video/             # VideoObject sub-skill
    schema-breadcrumb/        # BreadcrumbList sub-skill
    schema-event/             # Event sub-skill
    schema-validator/         # Schema validation sub-skill
    schema-report/            # Coverage report sub-skill
  templates/                  # JSON-LD template files
  scripts/                    # Python utilities
  agents/                     # Agent definitions
  docs/                       # Documentation
  assets/                     # Static assets
  schema/                     # Schema definitions
```

---

## Templates

Pre-built JSON-LD templates in `templates/` for instant use:

| Template | File | Use Case |
|----------|------|----------|
| Organization | `organization.json` | Company homepage |
| Local Business | `local-business.json` | Location pages |
| Product | `product.json` | Product detail pages |
| FAQ | `faq.json` | FAQ sections |
| HowTo | `howto.json` | Tutorial pages |
| Article | `article.json` | Blog posts |
| Video | `video.json` | Video pages |
| Breadcrumb | `breadcrumb.json` | All pages |
| Event | `event.json` | Event listings |
| Service | `service.json` | Service pages |
| Review | `review.json` | Review sections |
| Speakable | `speakable.json` | Voice search optimization |

---

## Scripts

| Script | Purpose |
|--------|---------|
| `schema_generator.py` | Programmatic schema generation from data sources |
| `schema_validator.py` | Validate JSON-LD against Schema.org spec + Google requirements |
| `generate_schema_report.py` | Crawl pages and produce schema coverage report |

---

## Agents

| Agent | Purpose |
|-------|---------|
| `schema-audit-agent` | Full-site schema audit with prioritized recommendations |
| `schema-migration-agent` | Migrate from Microdata/RDFa to JSON-LD |
| `schema-deployment-agent` | Deploy schema via GTM, WordPress, or direct injection |

---

## Key Principles

1. **JSON-LD only** -- Google's recommended format. No Microdata or RDFa generation.
2. **Google-first validation** -- We validate against Google's rich result requirements, not just Schema.org spec.
3. **Copy-paste ready** -- Every output is a complete `<script type="application/ld+json">` block.
4. **Nesting over flat** -- Nested entities are preferred for clarity and Google's parser.
5. **Real URLs only** -- No example.com placeholders. Always prompt for actual values.

---

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))

Built with Claude Code.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
