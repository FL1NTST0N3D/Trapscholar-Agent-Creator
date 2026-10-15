# Schema: Report

Generate comprehensive schema coverage reports for websites. Analyze which pages have schema markup, which types are used, identify validation issues, and surface missing opportunities where schema could improve search visibility.

## Command

`/schema report`

## When to Use

Use the report sub-skill when performing a site-wide schema audit, onboarding a new client for SEO work, evaluating a competitor's structured data strategy, or creating a roadmap for schema implementation. The report provides a bird's-eye view of structured data health across an entire domain, identifying both what exists and what is missing.

## Report Sections

### 1. Executive Summary
- Total pages analyzed
- Pages with schema vs pages without
- Schema coverage percentage
- Number of distinct schema types found
- Overall schema health score (0-100)
- Top 3 priorities for improvement

### 2. Schema Type Inventory
A complete listing of every schema type found across the site:

| Type | Count | Pages | Validity | Rich Result Eligible |
|------|-------|-------|----------|---------------------|
| Organization | 1 | Homepage | Valid | Yes (Knowledge Panel) |
| BreadcrumbList | 45 | All inner pages | 2 errors | Yes |
| Article | 28 | Blog posts | Valid | Yes |
| Product | 120 | Product pages | 15 warnings | Yes (12 missing availability) |
| FAQPage | 8 | Service pages | Valid | No (2023 restriction) |

### 3. Page-Level Analysis
For each page (or a representative sample for large sites):

- URL
- Schema types present
- Validation status (pass/warning/error)
- Missing recommended schema types
- Specific issues found

### 4. Validation Summary
Aggregate validation results across all pages:

- Total errors by severity (ERROR, WARNING, DEPRECATED, MISSING)
- Most common error types
- Pages with the most issues
- Error distribution by schema type

### 5. Opportunity Analysis
Pages and page types that are missing schema entirely or missing beneficial schema types:

- **Product pages without Product schema**: Lost opportunity for product rich results
- **Blog posts without Article schema**: Missing author attribution and article rich results
- **Location pages without LocalBusiness schema**: No local pack signal reinforcement
- **All pages missing BreadcrumbList**: Easy win for breadcrumb rich results
- **Video content without VideoObject schema**: Missing video carousel eligibility
- **Event pages without Event schema**: No Google Events integration

### 6. Competitive Benchmark
Compare schema implementation against 2-3 competitors:

- Which schema types they use that you do not
- Their rich result coverage vs yours
- Unique schema implementations worth adopting

### 7. Implementation Roadmap
Prioritized list of schema improvements:

| Priority | Action | Pages Affected | Effort | Impact |
|----------|--------|---------------|--------|--------|
| P0 | Fix Product schema errors | 15 product pages | Low | High |
| P1 | Add BreadcrumbList to all pages | ~200 pages | Medium | Medium |
| P1 | Add Article schema to blog | 28 pages | Low | Medium |
| P2 | Add Organization schema | 1 page | Low | Medium |
| P2 | Add VideoObject to video pages | 12 pages | Low | High |
| P3 | Add Event schema to event pages | 5 pages | Low | Medium |

## Data Collection Methods

The report can be generated from several data sources:

### Option 1: URL List
Provide a list of URLs to analyze. The validator extracts and checks schema from each page.

### Option 2: Sitemap
Provide the sitemap URL. The script crawls all URLs from the sitemap and analyzes schema on each.

### Option 3: Manual Schema Input
For sites without crawl access, paste the JSON-LD blocks from key page templates and the report analyzes what is provided.

### Option 4: Screaming Frog Export
Import a Screaming Frog crawl export (CSV) that includes structured data columns. The report processes the pre-crawled data.

## Health Score Calculation

The overall schema health score (0-100) is calculated as:

- **Coverage (40 points)**: Percentage of pages that have at least one relevant schema type
- **Validity (30 points)**: Percentage of schema blocks that pass validation without errors
- **Completeness (20 points)**: Average percentage of recommended properties included
- **Best Practices (10 points)**: Use of @id, @graph, proper entity referencing, no duplicates

Scoring thresholds:
- 90-100: Excellent -- schema is comprehensive and well-implemented
- 70-89: Good -- most schema is in place but gaps exist
- 50-69: Fair -- basic schema exists but significant gaps and errors
- 30-49: Poor -- minimal schema implementation with many issues
- 0-29: Critical -- schema is essentially absent or broken

## Output Formats

The report can be generated in:

- **Markdown**: For internal documentation and handoff to developers
- **HTML**: For client-facing presentations
- **JSON**: For programmatic consumption and dashboard integration
- **CSV**: For spreadsheet analysis and tracking

## Automated Reporting Script

The `scripts/generate_schema_report.py` script automates data collection and report generation. It accepts a domain or URL list, crawls pages, extracts schema, runs validation, and produces the full report in the chosen format.

## Recurring Audits

Schema markup can degrade over time as pages are added, templates change, and CMS plugins update. Recommended audit frequency:

- **Monthly**: Quick check of key page templates (5-10 pages)
- **Quarterly**: Full site audit with validation and opportunity analysis
- **After major changes**: Full audit after site redesigns, CMS migrations, or template updates
