# Report Sub-Skill

## Purpose

Generate a structured LinkedIn Ads audit report with health scores, dimension breakdowns, prioritized action items, and benchmark comparisons. Output in markdown format suitable for client delivery or internal review.

## Report Template

When generating a LinkedIn Ads audit report, follow this exact structure. Fill in each section based on data collected from the other 7 sub-skills.

### Report Structure

```markdown
# LinkedIn Ads Audit Report

**Client:** [Company Name]
**Audit Date:** [Date]
**Auditor:** [Name]
**Reporting Period:** [Start Date] - [End Date]
**Account ID:** [LinkedIn Ad Account ID]

---

## Executive Summary

**Overall Health Score: [X]/100 | Rating: [Elite/Strong/Average/Weak/Critical]**

[2-3 sentence summary of account health, biggest strengths, and most critical issues.]

### Score Breakdown

| Dimension | Score | Max | Rating |
|-----------|-------|-----|--------|
| Campaign Structure | X | 15 | [Rating] |
| Targeting Quality | X | 20 | [Rating] |
| Lead Gen Forms | X | 15 | [Rating] |
| Content Formats | X | 10 | [Rating] |
| Budget & CPL | X | 15 | [Rating] |
| Audience Building | X | 10 | [Rating] |
| Conversion Tracking | X | 10 | [Rating] |
| Reporting Setup | X | 5 | [Rating] |
| **TOTAL** | **X** | **100** | **[Rating]** |

---

## Key Metrics Overview

| Metric | Current | Benchmark | Status |
|--------|---------|-----------|--------|
| Monthly Spend | $X | - | - |
| Total Leads (LGF) | X | - | - |
| Average CPL | $X | $X-$X | [Above/At/Below] |
| Average CTR | X% | 0.5% | [Above/At/Below] |
| Average CPC | $X | $3-$7 | [Above/At/Below] |
| Lead Gen Form Completion | X% | 13% | [Above/At/Below] |
| Active Campaigns | X | - | - |
| Active Ad Formats | X | 3+ | [Met/Not Met] |

---

## Top 3 Critical Findings

### 1. [Finding Title]
**Impact:** [High/Medium/Low]
**Current State:** [What is happening]
**Recommended Action:** [Specific action to take]
**Expected Result:** [Quantified improvement estimate]

### 2. [Finding Title]
...

### 3. [Finding Title]
...

---

## Detailed Audit by Dimension

### 1. Campaign Structure (X/15)

**Findings:**
- [Finding 1]
- [Finding 2]
- [Finding 3]

**Recommendations:**
1. [High Priority] [Action item]
2. [Medium Priority] [Action item]
3. [Low Priority] [Action item]

### 2. Targeting Quality (X/20)

**Findings:**
- [Finding 1]
- [Finding 2]

**Audience Summary:**
| Campaign | Audience Size | Layers | Exclusions | Status |
|----------|-------------|--------|------------|--------|
| [Name] | X | X | Yes/No | [OK/Issue] |

**Recommendations:**
1. [Action item]
2. [Action item]

### 3. Lead Gen Forms (X/15)

**Form Performance:**
| Form Name | Fields | Completion Rate | CPL | Status |
|-----------|--------|----------------|-----|--------|
| [Name] | X | X% | $X | [OK/Issue] |

**Findings:**
- [Finding 1]
- [Finding 2]

**Recommendations:**
1. [Action item]
2. [Action item]

### 4. Content Formats (X/10)

**Format Mix:**
| Format | Campaigns | Spend % | CTR | CPL | Status |
|--------|-----------|---------|-----|-----|--------|
| Single Image | X | X% | X% | $X | [OK/Issue] |
| Video | X | X% | X% | $X | [OK/Issue] |
| Document | X | X% | X% | $X | [OK/Issue] |
| Carousel | X | X% | X% | $X | [OK/Issue] |

**Recommendations:**
1. [Action item]
2. [Action item]

### 5. Budget & CPL (X/15)

**Budget Allocation:**
| Funnel Stage | Budget | % of Total | Recommended % | Status |
|-------------|--------|-----------|---------------|--------|
| TOFU | $X | X% | 20-30% | [OK/Issue] |
| MOFU | $X | X% | 50-60% | [OK/Issue] |
| BOFU | $X | X% | 15-25% | [OK/Issue] |

**CPL Analysis:**
| Campaign | CPL | Benchmark | Variance | Action |
|----------|-----|-----------|----------|--------|
| [Name] | $X | $X | +/-X% | [Keep/Optimize/Pause] |

**Recommendations:**
1. [Action item]
2. [Action item]

### 6. Audience Building (X/10)

**Matched Audiences:**
| Audience Type | Status | Size | Freshness |
|--------------|--------|------|-----------|
| Website Retargeting | Active/Missing | X | X days |
| Contact Lists | Active/Missing | X | X days old |
| Lookalike | Active/Missing | X | - |
| Video Viewers | Active/Missing | X | - |
| LGF Openers | Active/Missing | X | - |

**Recommendations:**
1. [Action item]
2. [Action item]

### 7. Conversion Tracking (X/10)

**Tracking Infrastructure:**
| Component | Status | Notes |
|-----------|--------|-------|
| Insight Tag | Active/Missing/Broken | [Details] |
| Conversion Events | X configured | [Details] |
| CAPI | Active/Not Set Up | [Details] |
| Offline Conversions | Active/Not Set Up | [Details] |
| Attribution Windows | [Settings] | [Appropriate/Needs Adjustment] |

**Recommendations:**
1. [Action item]
2. [Action item]

### 8. Reporting Setup (X/5)

**Findings:**
- UTM Parameters: [Consistent/Inconsistent/Missing]
- CRM Integration: [Active/Partial/Missing]
- Dashboard: [Configured/Not Set Up]
- Naming Convention: [Consistent/Inconsistent]

**Recommendations:**
1. [Action item]

---

## 30-Day Action Plan

### Week 1: Quick Wins
- [ ] [Action 1] -- [Expected impact]
- [ ] [Action 2] -- [Expected impact]

### Week 2: Structural Fixes
- [ ] [Action 1] -- [Expected impact]
- [ ] [Action 2] -- [Expected impact]

### Week 3: Optimization
- [ ] [Action 1] -- [Expected impact]
- [ ] [Action 2] -- [Expected impact]

### Week 4: Measurement & Review
- [ ] [Action 1] -- [Expected impact]
- [ ] Review all changes and measure impact

---

## Appendix

### A. Industry Benchmark Reference
[Include relevant industry benchmarks from li-budget-cpl]

### B. LinkedIn Ads Glossary
[Key terms used in this report]

### C. Methodology
This audit evaluates LinkedIn Ads accounts across 8 dimensions and 25+ individual checks. Scoring is based on industry best practices, LinkedIn's own recommendations, and performance benchmarks from B2B advertising data.

---

*Report generated by LinkedIn B2B Ads Audit Skill*
*Second Step | getsecondstep.com*
```

## Reporting Setup Audit (5 Points)

This dimension evaluates the operational reporting infrastructure:

1. **UTM Parameter Consistency** (2 pts)
   - Are all LinkedIn ads tagged with consistent UTM parameters?
   - Format: `utm_source=linkedin&utm_medium=paid_social&utm_campaign=[name]&utm_content=[ad_name]`
   - Are UTMs maintained in a tracking spreadsheet or naming convention doc?

2. **CRM Integration** (2 pts)
   - Are Lead Gen Form submissions flowing to CRM automatically?
   - Is there a lead scoring model that incorporates LinkedIn source?
   - Are offline conversions being sent back to LinkedIn?

3. **Dashboard Configuration** (1 pt)
   - Is there a LinkedIn-specific reporting dashboard (Campaign Manager, Looker, etc.)?
   - Are reports scheduled for regular delivery?

## Scoring

| Score | Rating | Meaning |
|-------|--------|---------|
| 5 | Elite | Full UTM tracking, CRM integration, automated reporting |
| 4 | Strong | Good tracking with minor gaps |
| 3 | Average | Partial UTMs, basic CRM integration |
| 2 | Weak | Inconsistent tracking, no CRM integration |
| 0-1 | Critical | No UTMs, no CRM connection, no reporting structure |

## Report Delivery Guidelines

1. **Format**: Deliver as markdown (convertible to PDF or Google Docs)
2. **Length**: Executive summary on page 1, full details in subsequent sections
3. **Tone**: Professional, data-driven, actionable
4. **Visuals**: Use tables for all data comparisons
5. **Prioritization**: Always rank recommendations by impact (High > Medium > Low)
6. **Timeline**: Include a 30-day action plan with weekly milestones
7. **Benchmarks**: Always reference industry-specific benchmarks, not generic averages
