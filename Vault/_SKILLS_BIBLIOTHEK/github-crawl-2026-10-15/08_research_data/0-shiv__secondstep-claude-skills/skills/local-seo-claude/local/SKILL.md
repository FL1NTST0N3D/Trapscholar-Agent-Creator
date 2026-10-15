# Local SEO & Google Business Profile Audit — Main Skill

## Description

This skill provides a comprehensive local SEO audit framework covering Google Business Profile optimization, NAP consistency, review management, citation building, local schema markup, content strategy, and geo-targeting. It is designed for performance marketers, SEO specialists, and agency teams managing local businesses.

## When to Use This Skill

Invoke this skill when a user needs to:
- Audit a local business's online presence
- Optimize a Google Business Profile listing
- Check NAP consistency across directories
- Analyze review profiles and develop response strategies
- Find and fix citation issues
- Implement LocalBusiness structured data
- Build a local content strategy
- Set up geo-targeted Google Ads campaigns
- Generate a client-ready local SEO report

## Commands

### `/local audit` — Full Local SEO Audit

Runs all eight sub-skills in sequence and produces a consolidated score.

**Usage:**
```
/local audit "Business Name" "City, State"
```

**Process:**
1. Pull GBP data and score completeness (25 pts)
2. Check NAP consistency across top directories (20 pts)
3. Analyze review profile vs competitors (20 pts)
4. Audit citation presence and quality (15 pts)
5. Validate schema markup on website (10 pts)
6. Evaluate local content depth (10 pts)
7. Compile findings into scored report

**Output:** A structured report with:
- Overall Local SEO Score (0-100)
- Component scores with pass/fail indicators
- Priority-ranked action items
- Competitive benchmarks

### `/local gbp` — Google Business Profile Audit

Audits GBP listing completeness against Google's best practices.

**Delegates to:** `skills/local-gbp-audit/SKILL.md`

### `/local nap` — NAP Consistency Check

Checks Name, Address, Phone consistency across directories and the business website.

**Delegates to:** `skills/local-nap-consistency/SKILL.md`

### `/local reviews` — Review Analysis

Analyzes review count, rating, velocity, response rate, and sentiment.

**Delegates to:** `skills/local-reviews/SKILL.md`

### `/local citations` — Citation Audit

Audits structured and unstructured citations for presence, accuracy, and duplicates.

**Delegates to:** `skills/local-citations/SKILL.md`

### `/local schema` — Schema Markup Validation

Validates LocalBusiness schema and related structured data on the website.

**Delegates to:** `skills/local-schema/SKILL.md`

### `/local content` — Local Content Strategy

Evaluates location pages, service area pages, and local blog content.

**Delegates to:** `skills/local-content/SKILL.md`

### `/local geo` — Geo-Targeting Audit

Audits Google Ads geo-targeting setup, location extensions, and local keyword strategy.

**Delegates to:** `skills/local-geo-targeting/SKILL.md`

### `/local report` — Generate Report

Generates a comprehensive, client-ready local SEO audit report.

**Delegates to:** `skills/local-report/SKILL.md`

## Scoring Framework

### Component Weights

| Component | Weight | Max Score |
|-----------|--------|-----------|
| GBP Completeness | 25% | 25 |
| NAP Consistency | 20% | 20 |
| Reviews | 20% | 20 |
| Citations | 15% | 15 |
| Schema Markup | 10% | 10 |
| Local Content | 10% | 10 |
| **Total** | **100%** | **100** |

### Grading Scale

| Grade | Score | Meaning |
|-------|-------|---------|
| A+ | 95-100 | Elite local presence |
| A | 90-94 | Excellent — minor polish needed |
| B+ | 85-89 | Strong — a few gaps |
| B | 80-84 | Good — noticeable improvements available |
| C+ | 70-79 | Fair — multiple areas need attention |
| C | 60-69 | Below average — significant work required |
| D | 50-59 | Poor — major gaps across the board |
| F | Below 50 | Critical — local presence is severely lacking |

## Local SEO Ranking Factors (2024-2026)

Based on aggregated industry research, the top local ranking factors are:

### Google Business Profile Signals (32%)
- Primary category relevance
- Business name keywords (natural, not stuffed)
- Proximity to searcher
- Physical address in city of search
- GBP completeness and activity

### Review Signals (16%)
- Review quantity
- Review velocity (rate of new reviews)
- Review diversity (across platforms)
- Review response rate
- Keywords in review text

### On-Page Signals (17%)
- NAP consistency on website
- City/state in title tags
- Domain authority
- LocalBusiness schema markup
- Location-specific landing pages

### Link Signals (13%)
- Quality of inbound links
- Local/relevant linking domains
- Anchor text with location terms

### Citation Signals (7%)
- Citation volume
- NAP consistency across citations
- Citation quality (DA of directories)

### Behavioral Signals (7%)
- Click-through rate from local pack
- Mobile clicks-to-call
- Check-ins
- Driving directions requests

### Personalization Signals (6%)
- Searcher proximity
- Search history

## Dependencies

This skill uses the following sub-skills:
- `local-gbp-audit` — GBP completeness scoring
- `local-nap-consistency` — Cross-directory NAP validation
- `local-reviews` — Review profile analysis
- `local-citations` — Citation audit and scoring
- `local-schema` — Structured data validation
- `local-content` — Content strategy evaluation
- `local-geo-targeting` — Ads geo-targeting audit
- `local-report` — Report compilation and formatting

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
