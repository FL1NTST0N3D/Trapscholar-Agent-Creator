---
name: audit-conversion-tracking
description: Validates conversion tracking infrastructure including Google Tag, conversion actions configuration, Enhanced Conversions (web and leads), offline conversion imports, server-side tracking, cross-domain tracking, attribution models, conversion lag, and tag firing accuracy.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Conversion Tracking Audit

## Overview

Conversion tracking is the foundation upon which all optimization decisions are made. Inaccurate tracking leads to incorrect bidding signals, flawed ROAS calculations, and misguided budget allocation. A single misconfigured conversion action can corrupt an entire account's performance data and smart bidding algorithms.

**Impact of bad tracking:**
- Smart bidding optimizes toward the wrong signals
- ROAS/CPA reporting is inaccurate (leading to bad decisions)
- Budget allocation is misguided
- Client reporting is misleading
- Attribution is broken

**This audit is arguably the most important dimension** — if conversion tracking is broken, every other metric in the account is unreliable.

## Audit Checks (25 Total)

### Google Tag Validation (4 checks)

**Check 1: Google Tag (gtag.js or GTM) Presence**
- Pass: Google Ads conversion tag is present on all relevant pages via gtag.js, GTM, or Google Tag
- Fail: Tag missing from key pages (especially conversion/thank-you pages)
- Scoring: 8 points
- Verification: Check for `gtag('config', 'AW-XXXXXXXXX')` or GTM container with Google Ads tags
- Tools: Google Tag Assistant, Chrome DevTools Network tab, GTM preview mode

**Check 2: Tag Firing on Correct Pages**
- Pass: Conversion tags fire only on actual conversion events (form submission, purchase, call)
- Fail: Tags firing on page load of landing pages (inflating conversions) or not firing on confirmation pages
- Scoring: 7 points
- Common errors: Tag on landing page instead of thank-you page; tag firing on every page view; tag firing on page refresh (double-counting)

**Check 3: Tag Placement Consistency**
- Pass: Tags are consistently implemented across all conversion points (all forms, all checkout flows)
- Fail: Some conversion points tracked, others not (partial tracking)
- Scoring: 4 points

**Check 4: Consent Mode Implementation**
- Pass: Consent Mode v2 implemented for GDPR/CCPA compliance; consent-aware tags configured
- Fail: No consent mode despite operating in regulated markets (EU, California)
- Scoring: 3 points
- Note: Consent Mode also enables conversion modeling for opted-out users (recovers 5-15% of conversion data)

### Conversion Action Configuration (5 checks)

**Check 5: Conversion Counting Method**
- Pass: Lead gen uses "One" counting (one conversion per click); e-commerce uses "Every" counting (every transaction)
- Fail: Lead gen set to "Every" (inflates conversions — same user submitting form twice counts as 2 conversions) or e-commerce set to "One" (misses repeat purchases)
- Scoring: 7 points
- This is one of the most common tracking errors in Google Ads

**Check 6: Conversion Value Assignment**
- Pass: Conversion values are set meaningfully — either dynamic values (e-commerce revenue) or static values reflecting lead quality tiers
- Fail: All conversions set to $0 or $1 (no value differentiation for VBB)
- Scoring: 5 points
- Best practice for lead gen: Assign different values to different conversion actions (e.g., phone call = $50, form submit = $30, chat = $20) based on close rates

**Check 7: Conversion Window Settings**
- Pass: Click-through window matches typical sales cycle (30 days default; longer for B2B/high-consideration)
- Fail: Window too short (missing delayed conversions) or too long (attributing stale conversions)
- Scoring: 3 points
- Benchmarks: E-commerce: 7-30 days | Lead gen: 30-60 days | B2B SaaS: 60-90 days | View-through: 1-3 days

**Check 8: Primary vs Secondary Conversion Actions**
- Pass: Only true business outcomes are set as "Primary" (included in bidding); micro-conversions set as "Secondary" (observation only)
- Fail: Multiple redundant primary conversions (e.g., both "page view" and "form submit" as primary — inflates conversion volume and corrupts smart bidding)
- Scoring: 7 points
- Critical: Smart bidding optimizes toward ALL primary conversion actions — having a page view as primary will skew bidding away from real leads

**Check 9: Conversion Action Naming & Organization**
- Pass: Conversion actions have clear, descriptive names; old/unused actions removed or set to secondary
- Fail: Duplicate conversion actions, confusing names like "Conversion 1", or legacy actions still counting
- Scoring: 2 points

### Enhanced Conversions (4 checks)

**Check 10: Enhanced Conversions for Web (EC4W)**
- Pass: Enhanced Conversions for Web is enabled and sending hashed first-party data (email, phone, name, address)
- Fail: EC4W not implemented despite having form submissions
- Scoring: 5 points
- Impact: Recovers 5-17% of otherwise unmeasured conversions by matching user data to signed-in Google accounts
- Implementation: Via gtag.js, GTM, or Google Ads API

**Check 11: EC4W Data Quality**
- Pass: Enhanced Conversion data match rate is 50%+ (visible in conversion action diagnostics)
- Fail: Match rate below 30% (poor data quality — check hashing implementation and data fields)
- Scoring: 3 points

**Check 12: Enhanced Conversions for Leads (EC4L)**
- Pass: EC4L implemented for lead gen businesses — user-provided data (email/phone) captured at form submission, matched to conversion event when lead converts offline
- Fail: Lead gen business without EC4L (missing offline conversion signal)
- Scoring: 5 points
- How EC4L works: 1) Capture GCLID + user email at form submit, 2) Store in CRM, 3) When lead closes, upload conversion with email → Google matches to original click
- Impact: Enables true ROAS measurement for lead gen; dramatically improves smart bidding quality

**Check 13: EC4L Pipeline Validation**
- Pass: EC4L data pipeline verified end-to-end — from form capture to CRM storage to upload/API push
- Fail: EC4L set up but pipeline broken (data not flowing, GCLID not captured, upload failing)
- Scoring: 3 points

### Offline Conversion Import (3 checks)

**Check 14: Offline Conversion Import (OCI) Setup**
- Pass: If applicable, offline conversions (CRM-reported sales, phone calls, in-store visits) imported back to Google Ads
- Fail: Lead gen business with CRM data but no offline conversion import (smart bidding lacks downstream quality signal)
- Scoring: 5 points
- Methods: Manual CSV upload, Zapier/Make integration, Google Ads API, Salesforce/HubSpot connector
- Cadence: Daily or weekly upload recommended; conversion must occur within the conversion window

**Check 15: GCLID Capture & Storage**
- Pass: GCLID (Google Click ID) captured from URL parameters and stored with each lead in CRM
- Fail: GCLID not captured (makes offline conversion import impossible for non-EC4L methods)
- Scoring: 4 points
- Implementation: Hidden form field populated by JavaScript extracting `gclid` URL parameter

**Check 16: Offline Conversion Latency**
- Pass: Offline conversions uploaded within a reasonable timeframe (daily-weekly)
- Fail: Offline conversions uploaded monthly or less (too late for smart bidding to learn from)
- Scoring: 2 points
- Benchmark: < 24 hour upload lag = excellent; 1-3 days = good; weekly = acceptable; monthly = too slow

### Advanced Tracking (5 checks)

**Check 17: Server-Side Tracking (sGTM) Detection**
- Pass: Server-side GTM implemented for improved data accuracy, first-party tracking, and ad blocker resilience
- Fail: Client-side only tracking (vulnerable to ad blockers, ITP, cookie restrictions)
- Scoring: 3 points
- Note: sGTM is advanced — not having it is not a failure for most accounts; it's an upgrade opportunity
- Impact: sGTM typically recovers 10-20% of lost conversion data from browser privacy features

**Check 18: Cross-Domain Tracking**
- Pass: If user journey spans multiple domains (e.g., site.com → checkout.site.com → payment.com), cross-domain tracking is configured
- Fail: Multi-domain journey without cross-domain tracking (breaks attribution, inflates sessions)
- Scoring: 4 points
- Verification: Check for `linker` configuration in gtag.js or cross-domain setup in GTM

**Check 19: Attribution Model Review**
- Pass: Data-driven attribution (DDA) is used (Google's recommended default since it distributes credit across touchpoints)
- Fail: Last-click attribution still in use (overvalues bottom-funnel, undervalues awareness/consideration)
- Scoring: 4 points
- Note: Google deprecated all rule-based models except last-click in 2023, pushing DDA as default
- DDA requirement: Sufficient conversion volume (300+ conversions in 30 days recommended, but works with less)

**Check 20: Conversion Lag Analysis**
- Pass: Conversion lag (time between click and conversion) is understood and accounted for in reporting
- Fail: Recent performance judged without accounting for conversion lag (last 7 days always looks worse than it is)
- Scoring: 3 points
- Method: Compare conversion counts for a date range at different reporting delays (e.g., last 7 days vs same 7 days viewed 14 days later)
- Benchmark: E-commerce: 0-3 day lag typical | Lead gen: 1-7 day lag | B2B: 7-30 day lag

**Check 21: Tag Firing Validation (Debug Check)**
- Pass: Conversion tags verified as firing correctly using Tag Assistant, GTM Preview, or real-time conversion report
- Fail: Tags not recently validated (could be silently broken)
- Scoring: 3 points

### Conversion Data Quality (4 checks)

**Check 22: Conversion Rate Reasonableness**
- Pass: Conversion rates are within industry benchmarks (not suspiciously high or low)
- Fail: Conversion rate > 20% on non-brand Search (likely tracking error) or < 0.5% (likely missing conversions)
- Scoring: 4 points
- Benchmarks: Search avg: 3-5% | Brand: 5-15% | Display: 0.5-1% | Shopping: 1-3%

**Check 23: Duplicate Conversion Detection**
- Pass: No evidence of double-counting (conversion count doesn't spike on tag changes, reasonable ratio of clicks to conversions)
- Fail: Suspicious conversion patterns suggesting double-counting (tag firing on page load + form submit, for example)
- Scoring: 4 points

**Check 24: GA4 ↔ Google Ads Conversion Parity**
- Pass: Conversion counts in Google Ads and GA4 are within 15% of each other (some variance is expected due to attribution differences)
- Fail: > 30% discrepancy between GA4 and Google Ads conversion counts (indicates tracking issues)
- Scoring: 3 points

**Check 25: Conversion Action Audit Log**
- Pass: All changes to conversion actions are documented; no unauthorized modifications
- Fail: Conversion action settings changed without documentation (can silently corrupt data)
- Scoring: 2 points

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Best-in-class tracking; data is highly reliable |
| 75-89 | Good | Solid tracking with minor gaps or improvement opportunities |
| 60-74 | Average | Core tracking works but missing advanced features; some data quality concerns |
| 40-59 | Below Average | Significant tracking issues undermining optimization |
| 0-39 | Poor | Tracking is fundamentally broken; all performance data suspect |

**Total possible points: 105** (normalized to 100-point scale)

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Conversion data accuracy | > 95% | 85-95% | 70-85% | < 70% |
| Enhanced Conversion match rate | > 60% | 40-60% | 20-40% | < 20% |
| Offline conversion import lag | < 24 hrs | 1-3 days | 3-7 days | > 7 days |
| GA4 vs Google Ads parity | < 10% diff | 10-20% | 20-30% | > 30% |
| Primary conversion actions (correct) | 100% | 90%+ | 70-90% | < 70% |

## Output Format

```markdown
## Conversion Tracking Audit Results

**Overall Score: [X]/100 — [Rating]**
**DATA RELIABILITY RATING: [High/Medium/Low/Critical]**

### Tracking Infrastructure
| Component | Status | Details |
|-----------|--------|---------|
| Google Tag | Present/Missing | gtag / GTM / Google Tag |
| Enhanced Conversions (Web) | Active/Inactive | Match rate: X% |
| Enhanced Conversions (Leads) | Active/Inactive/N/A | Pipeline: Verified/Broken |
| Offline Conversion Import | Active/Inactive/N/A | Cadence: Daily/Weekly/None |
| Server-Side Tracking | Active/Inactive | sGTM / Client-side only |
| Cross-Domain Tracking | Active/Inactive/N/A | Domains: ... |
| Attribution Model | DDA/Last Click | ... |
| Consent Mode | v2/v1/None | ... |

### Conversion Action Audit
| Action Name | Type | Counting | Value | Window | Primary/Secondary | Status |
|-------------|------|----------|-------|--------|-------------------|--------|
| ... | ... | ... | ... | ... | ... | OK/Issue |

### Critical Issues
1. [Tracking problems that undermine all data]

### Data Quality Score
- Estimated conversion data accuracy: [X]%
- Estimated missed conversions: [X]%

### Recommendations
1. [Fix critical tracking issues first]
2. [Implement enhanced conversions]
3. [Optimize configuration]
```
