# GA4 Audit Methodology

## Overview

The GA4 Audit Claude Skill performs a structured audit across 8 weighted dimensions, producing a Health Score (0-100) with prioritized recommendations.

## Audit Dimensions and Weights

### E-commerce Properties

| Dimension | Weight | Checks |
|-----------|--------|--------|
| Data Streams | 10% | Stream config, enhanced measurement, filters, retention |
| Events | 20% | Coverage, naming, parameters, firing, debug |
| Conversions | 15% | Setup, counting, values, Ads import, dedup |
| Audiences | 10% | Essential, predictive, triggers, duration, exclusions |
| Attribution | 10% | Model, lookback, paths, channels, Ads alignment |
| E-commerce | 15% | Funnel events, items array, revenue, completeness |
| Custom Dimensions | 10% | Registration, quota, coverage, data quality |
| Integrations | 10% | Ads, SC, BQ, Firebase, GTM |

### Non-E-commerce Properties

The 15% e-commerce weight is redistributed:
- Events: 25% (+5%)
- Conversions: 20% (+5%)
- Custom Dimensions: 15% (+5%)
- E-commerce: 0%

## Scoring Method

### Per-Dimension Scoring

Each dimension has a set of checks. Each check is scored as:
- **Pass** (1 point) — Meets the standard
- **Fail** (0 points) — Does not meet the standard
- **Warning** (0.5 points) — Partially meets or has a minor issue
- **N/A** (excluded) — Not applicable to this property type

**Dimension Score = (earned points / applicable points) * 100**

### Health Score Calculation

**Health Score = Sum of (dimension_score * dimension_weight) for all dimensions**

If a dimension cannot be assessed, its weight is redistributed proportionally to the remaining dimensions.

### Grade Assignment

| Score Range | Grade | Label | Interpretation |
|-------------|-------|-------|---------------|
| 90-100 | A | Excellent | Production-ready, well-optimized |
| 75-89 | B | Good | Minor gaps, mostly functional |
| 50-74 | C | Fair | Significant gaps affecting data quality |
| 25-49 | D | Poor | Major issues, unreliable data |
| 0-24 | F | Critical | Fundamentally broken, needs rebuild |

## Finding Prioritization

All failed checks are categorized into priority levels:

### Priority 1: Critical (Fix Immediately)
- Active data loss (events not firing, parameters not captured)
- Revenue tracking errors (duplicate purchases, wrong values)
- Compliance risks (PII in tracking, consent not implemented)
- Complete feature failure (no conversions configured)

### Priority 2: High (Fix This Week)
- Missing recommended events for business type
- Default settings that should be changed (2-month retention)
- Broken integrations (Ads not linked despite running campaigns)
- Internal traffic polluting data

### Priority 3: Medium (Fix This Month)
- Suboptimal configuration (could be better but not broken)
- Missing nice-to-have features (audiences, explorations)
- Incomplete implementations (some events missing parameters)

### Priority 4: Low (Improvement Opportunity)
- Optimization opportunities (predictive audiences, BigQuery)
- Cosmetic issues (naming inconsistencies)
- Advanced features not yet utilized

## Audit Prerequisites

### Required Access
- GA4 property access (Viewer role minimum, Admin preferred)
- Website access for tag inspection
- GTM access (if applicable)

### Recommended Access
- Google Ads account access
- Search Console access
- BigQuery project access
- Server-side access for data layer inspection

### Information Needed
1. GA4 Property ID
2. Website URL
3. Business type classification
4. Google Ads account ID (if applicable)
5. GTM container ID (if applicable)
6. Expected conversion actions
7. Backend revenue data (for e-commerce validation)

## Audit Frequency

| Property Type | Recommended Frequency |
|--------------|----------------------|
| E-commerce (high traffic) | Monthly |
| E-commerce (low-mid traffic) | Quarterly |
| Lead generation | Quarterly |
| SaaS | Quarterly |
| Content / Media | Semi-annually |
| After major site changes | Immediately |
| After GTM container updates | Within 1 week |
| After GA4 product updates | Within 2 weeks |
