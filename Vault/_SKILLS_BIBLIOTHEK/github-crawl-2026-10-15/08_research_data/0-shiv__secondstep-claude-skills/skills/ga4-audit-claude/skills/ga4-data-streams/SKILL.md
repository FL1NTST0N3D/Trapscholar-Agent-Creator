# GA4 Data Streams Audit

## Command
`/ga4 streams`

## Purpose
Audit the web and app data stream configuration for a GA4 property. Data streams are the foundation of GA4 data collection — misconfigured streams mean every downstream report is compromised.

## Audit Checklist

### 1. Web Stream Configuration

**Stream basics:**
- [ ] Web stream exists and is active
- [ ] Stream URL matches the production website (not staging/dev)
- [ ] Measurement ID (G-XXXXXXX) is correctly deployed on all pages
- [ ] Stream name is descriptive (not default "Web stream")
- [ ] Only ONE web stream per website (multiple streams = duplicate data)

**Measurement ID deployment:**
- [ ] G-tag is present in `<head>` section (not `<body>`)
- [ ] G-tag fires on every page (check for missing pages)
- [ ] G-tag is deployed via Google Tag Manager (preferred) or gtag.js
- [ ] No duplicate G-tags on the same page
- [ ] G-tag loads before other scripts that depend on it

### 2. Enhanced Measurement Settings

Enhanced Measurement provides automatic event tracking without additional code. Each toggle should be evaluated for the specific site.

**Page views (`page_view`):**
- [ ] Enabled (should almost always be ON)
- [ ] "Page changes based on browser history events" — Enable for SPAs (React, Angular, Vue), disable for traditional multi-page sites to avoid duplicate page_views
- [ ] Verify page_view fires exactly once per page load (check for duplicates)

**Scrolls (`scroll`):**
- [ ] Enabled — fires when user scrolls past 90% of page height
- [ ] Note: Only tracks 90% threshold. For granular scroll tracking (25%, 50%, 75%, 90%), implement custom scroll events via GTM
- [ ] Consider disabling if custom scroll tracking is implemented (prevents duplicate events)

**Outbound clicks (`click` with `outbound` parameter):**
- [ ] Enabled — tracks clicks to external domains
- [ ] Verify outbound click definition matches business needs
- [ ] Cross-domain linked domains should NOT trigger outbound clicks
- [ ] Affiliate and partner links are being tracked

**Site search (`view_search_results`):**
- [ ] Enabled if site has search functionality
- [ ] Search term parameter is correctly configured (default: `q`, `s`, `search`, `query`, `keyword`)
- [ ] Custom search parameters added if site uses non-standard parameter names
- [ ] Disabled if site has no search functionality (prevents noise)

**Video engagement (`video_start`, `video_progress`, `video_complete`):**
- [ ] Enabled if site has embedded YouTube videos
- [ ] JS API support is enabled on YouTube embeds (`enablejsapi=1`)
- [ ] Note: Only works with YouTube embeds, not Vimeo/Wistia/custom players
- [ ] For non-YouTube video, custom events should be implemented via GTM

**File downloads (`file_download`):**
- [ ] Enabled — tracks clicks on links to files (pdf, xlsx, docx, csv, txt, rtf, exe, zip, etc.)
- [ ] Verify file extensions list matches business needs
- [ ] Custom file types added if business uses non-standard formats

**Form interactions (`form_start`, `form_submit`):**
- [ ] Enabled if using native HTML forms
- [ ] Note: May not work with JavaScript-based forms (React forms, AJAX submissions)
- [ ] For JS forms, custom form tracking via GTM is recommended
- [ ] Verify form_submit fires on actual submission, not just button click

### 3. Cross-Domain Tracking

Cross-domain tracking ensures users navigating between your domains are counted as a single session.

- [ ] Cross-domain conditions configured if business operates multiple domains
- [ ] All owned domains are included in the cross-domain list
- [ ] Domains are added using exact match or contains/regex as appropriate
- [ ] `_gl` parameter is being appended to cross-domain links
- [ ] Landing pages on secondary domains accept and process `_gl` parameter
- [ ] Test: Navigate between domains and verify session continuity in Realtime report
- [ ] Subdomain tracking works automatically (no cross-domain config needed for same root domain)

### 4. Internal Traffic Filters

Internal traffic filters prevent employee/team visits from polluting data.

- [ ] Internal traffic rule is defined (Admin > Data Streams > Configure tag settings > Define internal traffic)
- [ ] Office IP addresses are included
- [ ] VPN IP ranges are included (if team uses VPN)
- [ ] Remote worker IPs are addressed (consider dynamic IP solution)
- [ ] Data filter is created in Admin > Data Settings > Data Filters
- [ ] Data filter is set to ACTIVE (not just Testing) — many audits find filters stuck in Testing mode
- [ ] Developer traffic filter is also configured if applicable
- [ ] Filter is using `traffic_type` parameter with correct value

### 5. Referral Exclusions (Unwanted Referrals)

Unwanted referral traffic creates false sessions and breaks attribution.

- [ ] Payment gateways are excluded (PayPal, Stripe checkout, Square, etc.)
- [ ] Authentication providers are excluded (Auth0, Okta, login pages)
- [ ] Cross-domain sites are handled via cross-domain tracking, NOT referral exclusion
- [ ] CDN domains are not triggering self-referrals
- [ ] Third-party booking/scheduling tools are excluded if they redirect back to site
- [ ] Own domain is NOT in the unwanted referrals list (this is handled automatically)

### 6. Data Retention Settings

Data retention affects how long user-level and event-level data is available in Explorations.

- [ ] Data retention is set to **14 months** (maximum for standard properties)
- [ ] Note: Default is 2 months — this is almost always insufficient
- [ ] "Reset user data on new activity" is ENABLED (extends retention for active users)
- [ ] For GA4 360 properties, 26/38/50-month options are available
- [ ] Understand: Standard reports (not Explorations) use aggregated data that is NOT affected by retention settings

### 7. Google Signals and Data Collection

- [ ] Google Signals is enabled (Admin > Data Collection)
- [ ] Understand impact: Enables cross-device reporting, remarketing audiences
- [ ] Thresholding may apply to reports when Signals is enabled (data may be hidden for small sample sizes)
- [ ] Data collection acknowledgment is accepted
- [ ] Granular location and device data collection is enabled (if needed)

### 8. Consent Mode

- [ ] Consent Mode is implemented if operating in regions requiring consent (EU, UK, California)
- [ ] Default consent state is set correctly (`denied` for EU users)
- [ ] Consent state updates when user grants/denies consent
- [ ] Google tags respect consent state (analytics_storage, ad_storage)
- [ ] Consent Mode v2 is implemented (required for EU data collection after March 2024)
- [ ] Behavioral modeling is enabled to recover data from non-consenting users

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Stream config | 15 | 15% |
| Enhanced Measurement | 25 | 25% |
| Cross-domain | 15 | 15% |
| Internal traffic | 15 | 15% |
| Referral exclusions | 10 | 10% |
| Data retention | 10 | 10% |
| Consent Mode | 10 | 10% |

**Score = (passed_points / total_applicable_points) * 100**

## Common Issues Found

1. **Data retention at 2 months** — The #1 most common misconfiguration. Change to 14 months immediately.
2. **Duplicate page_views on SPAs** — History change tracking enabled on traditional sites, or custom page_view firing alongside enhanced measurement.
3. **Internal traffic filter in Testing mode** — Filter created but never activated, polluting data for months.
4. **Missing cross-domain tracking** — Users counted as new sessions when navigating between owned domains.
5. **Payment gateway referrals** — PayPal/Stripe checkout creates false referral sessions, breaking attribution.
6. **Multiple web streams for same site** — Causes duplicate event collection and inflated metrics.
7. **Enhanced Measurement all toggles ON** — Video engagement enabled on sites with no videos creates unnecessary processing.
8. **Consent Mode not implemented** — EU traffic either not collected at all or collected non-compliantly.

## Output Format

```
## Data Streams Audit

**Score: XX/100**

### Stream Overview
- Property ID: [ID]
- Web Streams: [count]
- App Streams: [count]
- Measurement ID: [G-XXXXXXX]

### Enhanced Measurement Status
| Setting | Status | Recommendation |
|---------|--------|---------------|
| Page views | ON/OFF | ... |
| Scrolls | ON/OFF | ... |
| Outbound clicks | ON/OFF | ... |
| Site search | ON/OFF | ... |
| Video engagement | ON/OFF | ... |
| File downloads | ON/OFF | ... |
| Form interactions | ON/OFF | ... |

### Findings
[Passed/Failed/Warning items with fix instructions]
```
