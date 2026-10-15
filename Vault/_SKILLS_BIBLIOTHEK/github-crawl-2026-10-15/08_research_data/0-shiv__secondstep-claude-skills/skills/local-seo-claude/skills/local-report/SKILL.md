# Local Report — Comprehensive Local SEO Report Generation

## Description

Generates a client-ready local SEO audit report by aggregating scores and findings from all sub-skills (GBP, NAP, Reviews, Citations, Schema, Content). The report includes an overall score, component breakdowns, competitive benchmarks, priority action items, and a 90-day roadmap. Designed for agency teams presenting findings to local business clients.

## Command

```
/local report "Business Name" "City, State"
/local report "Business Name" --format pdf
/local report "Business Name" --competitors "Comp1, Comp2, Comp3"
```

## Report Sections

### 1. Executive Summary

The first page of the report. Non-technical. Written for a business owner.

**Contents:**
- Business name, location, date of audit
- Overall Local SEO Score (0-100) with letter grade
- One-paragraph plain-English summary of findings
- Top 3 wins (what the business is doing well)
- Top 3 urgent fixes (what needs immediate attention)
- Projected impact statement ("Fixing these 3 issues could increase local visibility by X%")

**Score Visualization:**
```
OVERALL LOCAL SEO SCORE: 67/100 (C+)

[===================................] 67%

Component Breakdown:
  GBP Completeness   ████████████████░░░░░ 18/25
  NAP Consistency     ████████████████████░ 19/20
  Reviews             ████████████░░░░░░░░ 12/20
  Citations           ██████████░░░░░░░░░░  9/15
  Schema Markup       ████░░░░░░░░░░░░░░░░  4/10
  Local Content       ████████░░░░░░░░░░░░  5/10
```

### 2. Component Detail Sections

Each component gets its own section with:

| Element | Description |
|---------|-------------|
| Component score | X/Y with percentage and letter grade |
| Findings table | Each check with PASS/FAIL/WARN status |
| Evidence | Screenshots or data supporting the finding |
| Impact assessment | How this affects rankings and conversions |
| Fix instructions | Step-by-step remediation for each issue |

**Component Sections:**
1. Google Business Profile Audit (from `/local gbp`)
2. NAP Consistency Audit (from `/local nap`)
3. Review Profile Analysis (from `/local reviews`)
4. Citation Audit (from `/local citations`)
5. Schema Markup Validation (from `/local schema`)
6. Local Content Evaluation (from `/local content`)

### 3. Competitive Benchmark

| Metric | Client | Comp A | Comp B | Comp C | Gap |
|--------|--------|--------|--------|--------|-----|
| GBP completeness | 72% | 88% | 65% | 91% | -19% vs leader |
| Google reviews | 47 | 124 | 65 | 203 | -156 vs leader |
| Google rating | 4.4 | 4.2 | 4.6 | 4.1 | +0.2 above avg |
| Review velocity | 3/mo | 6/mo | 2/mo | 8/mo | -5 vs leader |
| Citation count | 28 | 42 | 31 | 55 | -27 vs leader |
| Schema present | No | Yes | No | Yes | Behind 2 of 3 |

**Competitive Intelligence Notes:**
- Identify who dominates the local 3-pack for primary keywords
- Note competitors' GBP post frequency
- Compare photo counts and quality
- Identify gaps the client can exploit (e.g., competitor has no reviews on Yelp)

### 4. Priority Action Items

Actions ranked by impact and effort:

| Priority | Action | Impact | Effort | Component |
|----------|--------|--------|--------|-----------|
| P0 — Critical | Fix geo-targeting to "Presence only" | High | Low | Geo |
| P0 — Critical | Add missing phone to schema | High | Low | Schema |
| P1 — High | Respond to all negative reviews | High | Medium | Reviews |
| P1 — High | Claim Bing Places listing | Medium | Low | Citations |
| P2 — Medium | Create 3 service area pages | High | High | Content |
| P2 — Medium | Submit to data aggregators | Medium | Medium | Citations |
| P3 — Low | Add priceRange to schema | Low | Low | Schema |
| P3 — Low | Seed GBP Q&A section | Low | Medium | GBP |

**Priority Definitions:**
- **P0 — Critical:** Actively harming rankings or wasting money. Fix this week.
- **P1 — High:** Significant ranking opportunity. Fix within 2 weeks.
- **P2 — Medium:** Notable improvement potential. Fix within 30 days.
- **P3 — Low:** Polish and optimization. Fix within 60 days.

### 5. 90-Day Roadmap

| Week | Actions | Expected Outcome |
|------|---------|-----------------|
| 1-2 | Fix all P0 issues, claim missing primary listings | Stop bleeding; foundation set |
| 3-4 | Address P1 issues, start review generation | NAP consistency achieved |
| 5-6 | Build industry-specific citations, create location pages | Citation score improvement |
| 7-8 | Launch local content calendar, optimize schema | Content signals strengthening |
| 9-10 | Submit to data aggregators, build unstructured citations | Aggregator propagation begins |
| 11-12 | Re-audit all components, measure progress | Validate improvements, set new targets |

**Monthly Ongoing Tasks:**
- Publish 2-4 locally-focused blog posts
- Post weekly on GBP
- Respond to all new reviews within 24 hours
- Add 3-5 new GBP photos
- Monitor NAP consistency (re-run `/local nap` monthly)
- Track local pack rankings for primary keywords

### 6. Appendix

| Section | Contents |
|---------|----------|
| Methodology | Scoring system explanation, data sources |
| Glossary | NAP, GBP, Local Pack, Schema, Citation definitions |
| Tools used | Google Rich Results Test, schema validators, etc. |
| Data snapshots | Raw data collected during audit |

## Report Formatting

### Output Formats

| Format | Command Flag | Use Case |
|--------|-------------|----------|
| Markdown (default) | none | Quick review, internal use |
| Structured text | `--format text` | Terminal output, copy-paste |
| PDF-ready HTML | `--format pdf` | Client presentation |
| JSON | `--format json` | API integration, dashboards |

### PDF Branding (when `--format pdf`)

- Header: Business name + audit date
- Color scheme: Dark background (#1b1b1b), accent (#E87811)
- Font: Inter
- Footer: "Prepared by [Agency Name] | getsecondstep.com"
- Cover page with overall score
- Table of contents
- Page numbers

## Scoring Aggregation

The report aggregates scores from all sub-skills using these weights:

| Component | Raw Max | Weight | Weighted Max |
|-----------|---------|--------|-------------|
| GBP Completeness | 25 | 25% | 25 |
| NAP Consistency | 20 | 20% | 20 |
| Reviews | 20 | 20% | 20 |
| Citations | 15 | 15% | 15 |
| Schema Markup | 10 | 10% | 10 |
| Local Content | 10 | 10% | 10 |
| **Total** | **100** | **100%** | **100** |

**Grade Thresholds:**

| Grade | Score | Description |
|-------|-------|-------------|
| A+ | 95-100 | Elite local presence — maintain and defend |
| A | 90-94 | Excellent — minor polish needed |
| B+ | 85-89 | Strong — a few gaps to close |
| B | 80-84 | Good — clear improvement opportunities |
| C+ | 70-79 | Fair — multiple areas need work |
| C | 60-69 | Below average — significant gaps |
| D | 50-59 | Poor — major overhaul required |
| F | Below 50 | Critical — local presence severely lacking |

## Output Format

```
============================================================
        LOCAL SEO AUDIT REPORT
        [Business Name] | [City, State]
        Audit Date: [Date]
============================================================

OVERALL SCORE: [X]/100 ([Grade])

EXECUTIVE SUMMARY:
[Business Name] has a [grade-description] local SEO presence.
Key strengths include [top 2 strengths]. The most critical gaps
are [top 2 issues], which are likely costing the business
[estimated impact]. Addressing the priority items below could
improve local visibility by an estimated [X]% within 90 days.

TOP WINS:
  1. Strong NAP consistency (19/20) — well-maintained listings
  2. Good Google rating (4.4 stars) — above competitor average
  3. Schema markup present on location pages

URGENT FIXES:
  1. Review response rate is only 20% — respond to all reviews
  2. No Bing Places listing — missing a primary citation
  3. Location pages have duplicate content — rewrite needed

COMPONENT SCORES:
  GBP:       18/25 (72%) — B
  NAP:       19/20 (95%) — A
  Reviews:   12/20 (60%) — C
  Citations:  9/15 (60%) — C
  Schema:     4/10 (40%) — F
  Content:    5/10 (50%) — D

[... detailed sections follow ...]

PRIORITY ACTIONS (by urgency):
  P0: [list]
  P1: [list]
  P2: [list]
  P3: [list]

90-DAY ROADMAP:
  [week-by-week plan]

============================================================
  Prepared by Second Step | getsecondstep.com
  Audit powered by local-seo-claude
============================================================
```

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
