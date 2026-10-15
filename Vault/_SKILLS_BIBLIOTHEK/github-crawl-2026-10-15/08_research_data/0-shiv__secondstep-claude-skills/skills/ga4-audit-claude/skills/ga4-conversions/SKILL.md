# GA4 Conversions Audit

## Command
`/ga4 conversions`

## Purpose
Audit conversion event configuration in GA4. Conversions are the most critical events in your property — they define what "success" means for your business and directly impact Google Ads bidding, audience creation, and ROI reporting. A misconfigured conversion setup leads to bad bidding signals and wasted ad spend.

## GA4 Conversion Model

In GA4, any event can be marked as a conversion (called "Key Events" in the latest GA4 UI update, though the API still uses "conversions"). There is no separate goal system like Universal Analytics.

**Key differences from UA:**
- No goal slots (UA had 20 goals per view) — GA4 allows up to 30 conversion events
- No goal funnels — Use Funnel Exploration instead
- Counting method is configurable per conversion event
- Conversion value can be set at the event level or via Google Ads

## Audit Checklist

### 1. Conversion Event Configuration

**Basic setup:**
- [ ] At least one conversion event is configured
- [ ] Conversion events match actual business objectives (not vanity metrics)
- [ ] Total conversion events are under the 30 limit
- [ ] No automatically collected events are marked as conversions unless intentional (e.g., `first_visit` is rarely a true conversion)
- [ ] All conversion events are actively firing (check last 28 days of data)
- [ ] No test or debug conversion events are active in production

**By business type — required conversions:**

*E-commerce:*
- [ ] `purchase` is marked as a conversion
- [ ] `begin_checkout` is marked as a conversion (micro-conversion)
- [ ] `add_to_cart` is optionally a conversion (depends on business)
- [ ] `purchase` has `value` and `currency` parameters

*Lead generation:*
- [ ] `generate_lead` or equivalent form submission is a conversion
- [ ] Phone call events are conversions (if phone is a channel)
- [ ] Chat initiation events are conversions (if chat is a channel)
- [ ] Conversion values are assigned (even estimated values for leads)

*SaaS:*
- [ ] `sign_up` is marked as a conversion
- [ ] Trial start / subscription events are conversions
- [ ] Key activation events are conversions (e.g., first feature use)
- [ ] Upgrade / plan change events are conversions

### 2. Counting Method

Each conversion event has a counting method that determines how conversions are counted within a single session.

**Options:**
- **Once per session** — Counts maximum one conversion per session per event. Best for lead gen forms, sign-ups.
- **Every time** (default for `purchase`) — Counts every event instance. Best for e-commerce purchases, repeat actions.

**Audit checks:**
- [ ] `purchase` events use "Every time" counting (multiple purchases per session should all count)
- [ ] Lead form submissions use "Once per session" counting (prevents duplicate leads from page refreshes)
- [ ] Sign-up events use "Once per session" counting
- [ ] Download events use appropriate counting based on business need
- [ ] No conversion events have mismatched counting methods that inflate or deflate numbers

### 3. Conversion Value Assignment

Conversion values enable value-based bidding in Google Ads and ROI reporting.

- [ ] Revenue-generating events have dynamic values from the data layer (`value` parameter)
- [ ] Non-revenue conversions have estimated static values assigned
- [ ] Currency is set correctly for all valued conversions
- [ ] Values are in the correct unit (not in cents when expecting dollars)
- [ ] No negative conversion values (except refund events)
- [ ] Values are realistic (no $0 purchases, no $999999 test values in production)

**Value assignment best practices:**
- Lead form: Assign average customer value * close rate (e.g., $5,000 avg deal * 10% close = $500)
- Phone call: Assign value based on call-to-customer conversion rate
- Newsletter signup: Assign lifetime value of email subscriber
- Free trial: Assign trial-to-paid conversion rate * subscription value

### 4. Google Ads Import

If running Google Ads, conversion import is critical for Smart Bidding to work correctly.

- [ ] GA4 property is linked to Google Ads account
- [ ] Key conversion events are imported into Google Ads
- [ ] Imported conversions are set as "Primary" in Google Ads (used for bidding)
- [ ] Secondary conversions are correctly marked as "Secondary" (observation only)
- [ ] No duplicate conversions (same action tracked by both GA4 import AND Google Ads native tag)
- [ ] Conversion action categories are correctly set in Google Ads (Purchase, Lead, etc.)
- [ ] Conversion window matches business buying cycle (default 30 days, range 1-90 days)
- [ ] View-through conversion window is configured (default 1 day, range 1-30 days)
- [ ] Attribution model in Google Ads aligns with GA4 attribution settings
- [ ] Conversion value is passing through correctly from GA4 to Google Ads
- [ ] Enhanced conversions are configured for improved match rates

### 5. Conversion Linker Tag

- [ ] Conversion linker tag is present in GTM (fires on all pages)
- [ ] Conversion linker is not blocking GCLID parameter
- [ ] GCLID auto-tagging is enabled in Google Ads
- [ ] GCLID is not being stripped by redirects or server-side processing
- [ ] UTM parameters and GCLID coexist without conflict

### 6. Cross-Platform Conversion Deduplication

If tracking conversions from multiple sources, deduplication is critical.

- [ ] Transaction IDs are unique and consistent across platforms
- [ ] Server-side conversion tracking (if used) does not duplicate client-side tracking
- [ ] Google Ads native conversion tag and GA4 import are not both counting as primary
- [ ] Facebook/Meta CAPI does not duplicate pixel conversions (separate concern but related pattern)
- [ ] Offline conversion imports have proper deduplication against online conversions

### 7. Conversion Path Validation

- [ ] Test the full conversion path in GA4 DebugView
- [ ] Conversion appears in Realtime > Conversions within 30 seconds
- [ ] Conversion appears in standard Conversions report within 24-48 hours
- [ ] Conversion count in GA4 approximately matches server-side records (within 10-15% due to consent/blocking)
- [ ] Conversion value total in GA4 matches transaction system records

## Common Issues Found

1. **No conversion events configured** — Property collecting data but nothing marked as a conversion. Google Ads has no signal to optimize.
2. **Page_view marked as conversion** — Inflates conversion count, sends garbage signals to Google Ads bidding.
3. **Wrong counting method** — Lead form using "Every time" counting means a page refresh creates duplicate conversions.
4. **Missing conversion values** — Google Ads cannot use value-based bidding (tROAS) without conversion values.
5. **Duplicate Google Ads conversions** — Same purchase tracked by GA4 import AND Google Ads tag, doubling reported conversions.
6. **Stale conversions** — Events marked as conversions that no longer fire (deprecated pages, old features).
7. **Missing transaction_id on purchase** — Without transaction_id, Google Ads cannot deduplicate purchases from users who refresh the confirmation page.
8. **Conversion value in wrong currency** — Property in USD but values sent in cents or in a different currency, causing 100x over/under-reporting.

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Conversion setup | 25 | 25% |
| Counting method | 15 | 15% |
| Value assignment | 20 | 20% |
| Google Ads import | 25 | 25% |
| Deduplication | 15 | 15% |

**Score = (passed_points / total_applicable_points) * 100**

## Output Format

```
## Conversions Audit

**Score: XX/100**

### Conversion Events
| Event Name | Status | Counting | Value | Ads Import |
|-----------|--------|----------|-------|------------|
| purchase | Active | Every time | Dynamic | Primary |
| generate_lead | Active | Once/session | $500 | Primary |

### Google Ads Integration
- Linked: Yes/No
- Account ID: XXX-XXX-XXXX
- Imported conversions: [count]
- Primary: [list]
- Secondary: [list]

### Findings
[Passed/Failed/Warning items with fix instructions]
```
