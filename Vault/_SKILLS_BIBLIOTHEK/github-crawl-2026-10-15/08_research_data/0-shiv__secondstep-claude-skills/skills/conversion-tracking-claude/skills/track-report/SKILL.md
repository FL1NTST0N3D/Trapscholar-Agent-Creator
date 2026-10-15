# Track Report — Sub-Skill

## Command
`/track report`

## Description
Generates a comprehensive tracking audit report with platform-by-platform status, Tracking Health Score breakdown, prioritized fix list, and implementation guides. This is the output skill — it takes findings from all other sub-skills and assembles them into an actionable document that can be shared with clients, developers, or internal teams. The report answers three questions: What is working? What is broken? What should we fix first?

---

## Report Structure

### 1. Executive Summary
A 3-5 sentence overview for non-technical stakeholders:
- Overall Tracking Health Score (0-100)
- Number of critical issues found
- Estimated monthly spend at risk from tracking errors
- Top recommendation

**Template:**
```
TRACKING AUDIT — EXECUTIVE SUMMARY
====================================
Tracking Health Score: [XX]/100 — [Rating]
Critical Issues: [X]
High Priority Issues: [X]
Estimated Monthly Spend at Risk: $[X,XXX]

Your tracking implementation has [critical gaps / minor issues / is well-configured].
The most urgent fix is [top issue]. Addressing the [X] critical issues will recover
an estimated [X]% of currently lost conversion data.
```

### 2. Platform-by-Platform Status

For each active platform, report:

```
GOOGLE ADS TRACKING
====================
Component              | Status    | Score  | Notes
-----------------------|-----------|--------|------------------
Google Tag (gtag.js)   | [OK/FAIL] | [X/15] | [details]
Enhanced Conversions   | [OK/FAIL] | [X/15] | [EC Web + EC4L]
Server-Side GTM        | [OK/FAIL] | [X/15] | [sGTM status]
Offline Import         | [OK/FAIL] | [X/10] | [GCLID pipeline]

META ADS TRACKING
==================
Component              | Status    | Score  | Notes
-----------------------|-----------|--------|------------------
Meta Pixel             | [OK/FAIL] | [X/15] | [events, params]
Conversions API        | [OK/FAIL] | [X/15] | [EMQ score]
Event Deduplication    | [OK/FAIL] | [X/10] | [dedup status]

LINKEDIN ADS TRACKING
======================
Component              | Status    | Score  | Notes
-----------------------|-----------|--------|------------------
Insight Tag            | [OK/FAIL] | [X/5]  | [installation]
Conversion Tracking    | [OK/FAIL] | [X/5]  | [event vs URL]
LinkedIn CAPI          | [OK/FAIL] | [X/5]  | [if applicable]

TIKTOK ADS TRACKING
====================
Component              | Status    | Score  | Notes
-----------------------|-----------|--------|------------------
TikTok Pixel           | [OK/FAIL] | [X/5]  | [installation]
Standard Events        | [OK/FAIL] | [X/5]  | [events config]
Events API             | [OK/FAIL] | [X/5]  | [if applicable]

CROSS-PLATFORM
===============
Component              | Status    | Score  | Notes
-----------------------|-----------|--------|------------------
Attribution Models     | [OK/WARN] | [X/10] | [model alignment]
Cross-Platform Dedup   | [OK/WARN] | [X/5]  | [overlap ratio]
Data Freshness         | [OK/WARN] | [X/5]  | [reporting lag]
Consent Compliance     | [OK/WARN] | [X/5]  | [CMP status]
```

### 3. Tracking Health Score Breakdown

```
TRACKING HEALTH SCORE: [XX]/100
=================================

Category                        | Score | Max | Status
-------------------------------|-------|-----|--------
Tag Presence (all pages)        | [X]   | 15  | [status]
Event Configuration             | [X]   | 15  | [status]
Enhanced Conversions / Matching | [X]   | 15  | [status]
Server-Side Implementation     | [X]   | 15  | [status]
Offline Import Pipeline        | [X]   | 10  | [status]
Event Deduplication            | [X]   | 10  | [status]
Attribution Setup              | [X]   | 10  | [status]
Data Freshness                 | [X]   | 5   | [status]
Consent Compliance             | [X]   | 5   | [status]
-------------------------------|-------|-----|--------
TOTAL                          | [XX]  | 100 | [rating]
```

### 4. Issues Found — Prioritized

List every issue found, grouped by priority:

```
CRITICAL ISSUES (Fix immediately — data loss occurring)
========================================================
1. [Issue description]
   Platform: [Google/Meta/LinkedIn/TikTok]
   Impact: [What data is being lost]
   Fix: [Step-by-step fix instructions]
   Estimated effort: [X hours]

HIGH PRIORITY (Fix this week — degraded tracking)
===================================================
2. [Issue description]
   ...

MEDIUM PRIORITY (Fix this month — suboptimal configuration)
=============================================================
3. [Issue description]
   ...

LOW PRIORITY (Nice to have — incremental improvements)
========================================================
4. [Issue description]
   ...
```

### 5. Implementation Guide

For each critical and high-priority fix, provide step-by-step instructions:

**Format:**
```
FIX: [Issue Title]
Platform: [Platform]
Estimated Time: [X hours]
Requires: [Developer / GTM access / Platform admin]

Steps:
1. [First step with specific instructions]
2. [Second step]
3. [Third step]

Verification:
- [How to confirm the fix worked]
- [What to check after implementation]
```

### 6. Recommendations

Beyond fixes, include forward-looking recommendations:
- Server-side tracking adoption timeline
- Enhanced Conversions rollout plan
- Attribution model migration path
- Consent mode implementation
- Testing and QA process for ongoing tracking health

### 7. Appendix

- Full tag inventory (all tags found on site)
- Network request logs (key requests captured during audit)
- Platform diagnostic screenshots (if available)
- Configuration export (GTM container, conversion action settings)

---

## Report Generation Process

### Inputs Required
The report generator needs output from these sub-skills:
1. `/track google-tag` — Tag presence and conversion action data
2. `/track ec` — Enhanced Conversions status and match rates
3. `/track server-side` — sGTM deployment status
4. `/track offline` — GCLID pipeline and import status
5. `/track meta-pixel` — Pixel installation and event data
6. `/track capi` — CAPI status and EMQ scores
7. `/track linkedin` — Insight Tag and conversion data
8. `/track tiktok` — TikTok Pixel and Events API data
9. `/track attribution` — Attribution model analysis

### Scoring Algorithm

```python
def calculate_health_score(audit_data):
    score = 0

    # Tag Presence (15 points)
    score += assess_tag_presence(audit_data)

    # Event Configuration (15 points)
    score += assess_event_config(audit_data)

    # Enhanced Conversions / Matching (15 points)
    score += assess_enhanced_matching(audit_data)

    # Server-Side (15 points)
    score += assess_server_side(audit_data)

    # Offline Import (10 points)
    score += assess_offline_import(audit_data)

    # Deduplication (10 points)
    score += assess_deduplication(audit_data)

    # Attribution (10 points)
    score += assess_attribution(audit_data)

    # Data Freshness (5 points)
    score += assess_data_freshness(audit_data)

    # Consent (5 points)
    score += assess_consent(audit_data)

    return score  # 0-100
```

### Rating Thresholds
- 90-100: Excellent
- 70-89: Good
- 50-69: Needs Work
- 30-49: Poor
- 0-29: Critical

---

## Output Formats

### Markdown Report
Default output — structured markdown document suitable for sharing in Slack, email, or converting to PDF.

### Checklist Format
Condensed checklist version for developers to work through:
```
[ ] Critical: Fix missing Google Tag on /checkout and /thank-you pages
[ ] Critical: Enable Enhanced Conversions in Google Ads settings
[ ] High: Add event_id to Meta Pixel events for CAPI deduplication
[ ] High: Capture GCLID in hidden form field on lead forms
[ ] Medium: Increase Meta CAPI EMQ from 4.2 to 6.0+
```

### Client-Facing Summary
Simplified version without technical jargon, focused on business impact:
- What percentage of conversions are being tracked accurately
- Estimated revenue impact of tracking gaps
- Recommended investment in fixes
- Expected improvement after fixes

---

## Scoring Contribution

This sub-skill does not contribute points directly — it aggregates scores from all other sub-skills into the final Tracking Health Score and generates the report document.

---

## Usage

```bash
# Generate full report after running audit
claude "/track report"

# Generate report for specific platforms only
claude "/track report --platforms google,meta"

# Generate client-facing summary
claude "/track report --format client"

# Generate developer checklist
claude "/track report --format checklist"
```
