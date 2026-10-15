# Conversion Tracking Claude — Main Skill

## Description
Cross-platform conversion tracking setup, validation, and audit skill. Validates tracking implementations across Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, and server-side setups. Generates a Tracking Health Score (0-100) and actionable fix recommendations.

## Command Routing

| Command | Route To | Purpose |
|---------|----------|---------|
| `/track audit` | Full orchestration | Run all sub-skills, generate Health Score |
| `/track google-tag` | `skills/track-google-tag/` | Google Tag validation |
| `/track ec` | `skills/track-enhanced-conversions/` | Enhanced Conversions audit |
| `/track server-side` | `skills/track-server-side/` | Server-side GTM validation |
| `/track offline` | `skills/track-offline-import/` | Offline conversion import check |
| `/track meta-pixel` | `skills/track-meta-pixel/` | Meta Pixel audit |
| `/track capi` | `skills/track-meta-capi/` | Meta Conversions API validation |
| `/track linkedin` | `skills/track-linkedin-insight/` | LinkedIn Insight Tag check |
| `/track tiktok` | `skills/track-tiktok-pixel/` | TikTok Pixel audit |
| `/track attribution` | `skills/track-attribution/` | Attribution model analysis |
| `/track report` | `skills/track-report/` | Generate full audit report |

---

## Tracking Fundamentals

### What Is Conversion Tracking?

Conversion tracking measures the actions users take after interacting with your ads. Without accurate tracking, every optimization decision is based on incomplete or wrong data. The tracking stack typically consists of:

1. **Client-Side Tags** — JavaScript snippets (gtag.js, Meta Pixel, etc.) that fire in the user's browser
2. **Server-Side Events** — API calls from your server to ad platforms (sGTM, Meta CAPI, LinkedIn CAPI)
3. **Offline Imports** — CRM data uploaded back to ad platforms (GCLID-based, hashed customer data)
4. **Attribution Logic** — How platforms assign credit for conversions across touchpoints

### Why Tracking Breaks

Common causes of tracking failure:

- **Tag not on all pages** — Missing from specific page templates, SPAs not re-firing on navigation
- **Consent management conflicts** — CMP blocking tags before consent, tags firing before CMP loads
- **Data layer issues** — Variables undefined, wrong data types, timing race conditions
- **GTM container conflicts** — Multiple containers, tag sequencing errors, trigger misconfiguration
- **Cookie restrictions** — ITP/ETP blocking third-party cookies, 7-day first-party cookie expiry
- **Event deduplication failures** — Same conversion counted by both Pixel and CAPI
- **GCLID loss** — Click ID not captured on landing page, lost during redirects, not stored in CRM

---

## Cross-Platform Validation Framework

### Step 1: Inventory

Catalog every tracking tag, pixel, and API integration across all platforms:

```
TRACKING INVENTORY
==================
Platform        | Tag Type       | Implementation | Status
----------------|---------------|----------------|--------
Google Ads      | gtag.js       | Direct/GTM     | ?
Google Ads      | EC for Web    | gtag API/GTM   | ?
Google Ads      | EC for Leads  | Offline Import | ?
Google Ads      | sGTM          | Stape/GCP      | ?
Meta            | Pixel         | Direct/GTM     | ?
Meta            | CAPI          | Gateway/Direct | ?
LinkedIn        | Insight Tag   | Direct/GTM     | ?
LinkedIn        | CAPI          | Direct         | ?
TikTok          | Pixel         | Direct/GTM     | ?
TikTok          | Events API    | Direct         | ?
```

### Step 2: Validate Each Platform

Run platform-specific validation using the appropriate sub-skill:

1. Check tag presence on all page types (homepage, product, checkout, thank you)
2. Verify event firing with correct parameters
3. Confirm data is received by the ad platform (check platform's diagnostics)
4. Validate conversion action configuration (counting, value, window)
5. Test Enhanced Conversions / advanced matching where available

### Step 3: Cross-Platform Checks

- **Conversion window alignment** — Ensure windows are consistent or intentionally different
- **Attribution model awareness** — Know what model each platform uses
- **Deduplication** — Prevent double-counting across Pixel + CAPI, client-side + server-side
- **Value consistency** — Same conversion value reported to all platforms
- **Latency** — Time between conversion and platform reporting

### Step 4: Score and Report

Calculate Tracking Health Score:

```
SCORING RUBRIC (100 points total)
==================================
Category                        | Max Points
-------------------------------|----------
Tag Presence (all pages)        | 15
Event Configuration             | 15
Enhanced Conversions / Matching | 15
Server-Side Implementation     | 15
Offline Import Pipeline        | 10
Event Deduplication            | 10
Attribution Setup              | 10
Data Freshness                 | 5
Consent Compliance             | 5
```

---

## Orchestration: /track audit

When `/track audit` is invoked, the skill runs this sequence:

1. **Gather context** — Ask user for:
   - Which platforms are in use (Google, Meta, LinkedIn, TikTok)
   - Website URL(s) to audit
   - GTM container ID (if applicable)
   - Access to ad platform accounts (for diagnostics)
   - CRM system (for offline import validation)

2. **Run sub-skills** — Execute each relevant sub-skill based on platforms in use

3. **Cross-reference** — Check for cross-platform issues:
   - Mismatched conversion windows
   - Missing deduplication
   - Inconsistent conversion values
   - Attribution model conflicts

4. **Score** — Calculate Tracking Health Score using the rubric above

5. **Report** — Generate the audit report via `skills/track-report/`

6. **Prioritize fixes** — Rank issues by:
   - **Critical** — Lost conversion data (broken tags, missing events)
   - **High** — Degraded data quality (no EC, no server-side)
   - **Medium** — Suboptimal configuration (wrong counting, short windows)
   - **Low** — Nice-to-have improvements (additional events, better attribution)

---

## Key Concepts Reference

### Click IDs
- **GCLID** — Google Click ID, appended to URL on Google Ads click
- **WBRAID** — Google's modeled click ID for iOS web-to-app
- **GBRAID** — Google's modeled click ID for iOS app-to-app
- **FBCLID** — Facebook/Meta Click ID
- **li_fat_id** — LinkedIn first-party ad tracking ID
- **ttclid** — TikTok Click ID

### Consent Modes
- **Google Consent Mode v2** — ad_storage, analytics_storage, ad_user_data, ad_personalization
- **Meta Limited Data Use** — LDU flag for CCPA compliance
- **IAB TCF v2.2** — Transparency and Consent Framework for GDPR

### Data Hashing
All platforms require SHA-256 hashing for user data:
- Email: lowercase, trim whitespace, then SHA-256
- Phone: E.164 format (e.g., +12125551234), then SHA-256
- Name: lowercase, trim, then SHA-256
- Address: lowercase, trim, remove special characters, then SHA-256

---

## Sub-Skills

Each sub-skill has its own `SKILL.md` with detailed validation procedures:

- [Google Tag](skills/track-google-tag/SKILL.md)
- [Enhanced Conversions](skills/track-enhanced-conversions/SKILL.md)
- [Server-Side GTM](skills/track-server-side/SKILL.md)
- [Offline Import](skills/track-offline-import/SKILL.md)
- [Meta Pixel](skills/track-meta-pixel/SKILL.md)
- [Meta CAPI](skills/track-meta-capi/SKILL.md)
- [LinkedIn Insight](skills/track-linkedin-insight/SKILL.md)
- [TikTok Pixel](skills/track-tiktok-pixel/SKILL.md)
- [Attribution](skills/track-attribution/SKILL.md)
- [Report](skills/track-report/SKILL.md)
