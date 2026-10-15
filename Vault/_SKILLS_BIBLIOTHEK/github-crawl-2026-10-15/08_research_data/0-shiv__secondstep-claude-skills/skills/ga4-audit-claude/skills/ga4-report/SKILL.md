# GA4 Audit Report Generation

## Command
`/ga4 report`

## Purpose
Compile all individual audit dimension findings into a comprehensive GA4 Audit Report with an overall Health Score, prioritized recommendations, and implementation roadmap. This is the final step in the audit process — it transforms raw audit findings into an actionable document that can be shared with clients, stakeholders, or development teams.

## Report Generation Process

### Step 1: Collect All Dimension Scores

Gather scores from each completed sub-skill audit:

| Dimension | Sub-skill | Weight |
|-----------|-----------|--------|
| Data Streams | ga4-data-streams | 10% |
| Events | ga4-events | 20% |
| Conversions | ga4-conversions | 15% |
| Audiences | ga4-audiences | 10% |
| Attribution | ga4-attribution | 10% |
| E-commerce | ga4-ecommerce | 15% |
| Custom Dimensions | ga4-custom-dimensions | 10% |
| Integrations | ga4-integrations | 10% |

Note: Reporting (ga4-reporting) is assessed qualitatively and does not have a direct weight in the Health Score, but findings are included in the report.

### Step 2: Calculate Health Score

```
Health Score = (
    streams_score * 0.10 +
    events_score * 0.20 +
    conversions_score * 0.15 +
    audiences_score * 0.10 +
    attribution_score * 0.10 +
    ecommerce_score * 0.15 +
    dimensions_score * 0.10 +
    integrations_score * 0.10
)
```

For non-e-commerce properties, redistribute the 15% e-commerce weight:
- Events: +5% (25% total)
- Conversions: +5% (20% total)
- Custom Dimensions: +5% (15% total)

### Step 3: Grade Assignment

| Score | Grade | Label |
|-------|-------|-------|
| 90-100 | A | Excellent |
| 75-89 | B | Good |
| 50-74 | C | Fair |
| 25-49 | D | Poor |
| 0-24 | F | Critical |

### Step 4: Prioritize Findings

All findings from all dimensions are consolidated and prioritized:

**Priority 1 — Critical (Fix Immediately):**
- Data loss issues (unregistered parameters, missing events)
- Revenue tracking errors (wrong values, duplicate purchases)
- Conversion tracking failures (no conversions, wrong counting)
- Google Ads integration broken (no conversion import)
- PII in tracking (legal/compliance risk)

**Priority 2 — High (Fix This Week):**
- Missing recommended events for business type
- Data retention at 2 months
- Internal traffic filter not active
- Attribution model not configured
- Key audiences not created

**Priority 3 — Medium (Fix This Month):**
- Enhanced measurement misconfigurations
- Cross-domain tracking gaps
- Referral exclusion missing payment gateways
- Custom dimensions underutilized
- Reporting not customized

**Priority 4 — Low (Improvement Opportunity):**
- Predictive audiences not explored
- Looker Studio not connected
- BigQuery export not enabled
- Exploration templates not created
- Event naming inconsistencies (cosmetic)

## Report Template

The final report follows this structure:

```markdown
# GA4 Audit Report

**Property:** [Property Name] (properties/XXXXXXXX)
**Website:** [URL]
**Business Type:** [E-commerce / Lead Gen / SaaS / Content / Travel]
**Audit Date:** [Date]
**Auditor:** [Name]

---

## Executive Summary

**Overall Health Score: XX/100 (Grade: X — Label)**

[2-3 sentence summary of the property's GA4 implementation quality,
biggest strength, and most critical gap.]

### Score Breakdown

| Dimension | Score | Grade | Status |
|-----------|-------|-------|--------|
| Data Streams | XX/100 | X | icon |
| Events | XX/100 | X | icon |
| Conversions | XX/100 | X | icon |
| Audiences | XX/100 | X | icon |
| Attribution | XX/100 | X | icon |
| E-commerce | XX/100 | X | icon |
| Custom Dimensions | XX/100 | X | icon |
| Integrations | XX/100 | X | icon |

---

## Critical Findings (Priority 1)

### Finding 1: [Title]
- **Dimension:** [Which audit dimension]
- **Impact:** Critical — [description of business impact]
- **Current State:** [What is currently configured]
- **Recommended:** [What should be configured]
- **Fix Steps:**
  1. Step-by-step instructions
  2. With specific navigation paths
  3. And expected outcomes

[Repeat for each critical finding]

---

## High Priority Findings (Priority 2)

[Same format as critical findings]

---

## Medium Priority Findings (Priority 3)

[Same format, may be abbreviated]

---

## Low Priority / Improvements (Priority 4)

[Brief list format]

---

## Implementation Roadmap

### Week 1: Critical Fixes
- [ ] Fix 1 description (est. X hours)
- [ ] Fix 2 description (est. X hours)

### Week 2: High Priority
- [ ] Fix 3 description (est. X hours)
- [ ] Fix 4 description (est. X hours)

### Week 3-4: Medium Priority
- [ ] Fix 5 description (est. X hours)
- [ ] Fix 6 description (est. X hours)

### Ongoing: Improvements
- [ ] Improvement 1
- [ ] Improvement 2

---

## Detailed Dimension Reports

### Data Streams
[Full output from ga4-data-streams audit]

### Events
[Full output from ga4-events audit]

### Conversions
[Full output from ga4-conversions audit]

### Audiences
[Full output from ga4-audiences audit]

### Attribution
[Full output from ga4-attribution audit]

### E-commerce
[Full output from ga4-ecommerce audit]

### Custom Dimensions
[Full output from ga4-custom-dimensions audit]

### Reporting
[Full output from ga4-reporting audit]

### Integrations
[Full output from ga4-integrations audit]

---

## Methodology

This audit evaluated the GA4 property across 8 weighted dimensions
using [X] individual checks. Each check was scored as passed, failed,
or warning. The Health Score is a weighted average of all dimension
scores.

**Audit tool:** GA4 Audit Claude Skill v1.0.0
**Checks performed:** [total count]
**Passed:** [count] | **Failed:** [count] | **Warnings:** [count]

---

## Next Steps

1. Share this report with your development/analytics team
2. Begin with Critical (P1) fixes immediately
3. Schedule a follow-up audit in 30 days to measure improvement
4. Set up ongoing monitoring via GA4 alerts and Looker Studio dashboards

---

*Report generated by GA4 Audit Claude Skill*
*Author: [Auditor Name]*
*For questions: [Contact]*
```

## Report Delivery Options

The report can be generated in the following formats:

1. **Markdown** — Default output, can be copied into any document
2. **PDF** — Using the Second Step branded PDF pipeline (if available)
3. **Google Doc** — Via Docs API integration (if configured)
4. **Notion** — Via Notion API integration (if configured)

## Scoring Validation

Before generating the final report, validate:

- [ ] All applicable sub-skill audits have been completed
- [ ] No dimension has a score of 0 unless genuinely everything failed
- [ ] Total checks count matches the sum of individual dimension checks
- [ ] Health Score arithmetic is correct
- [ ] Priority assignments align with impact severity
- [ ] Implementation time estimates are reasonable
- [ ] Fix instructions are actionable (not vague suggestions)

## Common Report Patterns

**Pattern: "Looks good on the surface"** (Score 60-75)
- Basics are in place (stream, some events, conversions exist)
- Missing depth (no custom dimensions, default attribution, no audiences)
- Quick wins available with modest effort

**Pattern: "Partial implementation"** (Score 40-59)
- Stream configured but enhanced measurement defaults never reviewed
- Some events firing but missing recommended events for business type
- No Google Ads integration despite running campaigns
- Significant data quality issues

**Pattern: "Needs rebuild"** (Score 0-39)
- Multiple critical issues (no conversions, wrong stream, PII in events)
- Faster to rebuild than fix incrementally
- Recommend a fresh implementation with proper planning

**Pattern: "Well implemented"** (Score 80-95)
- All basics covered plus advanced features
- Minor gaps in audiences, attribution tuning, or predictive features
- Focus on optimization, not fixing
