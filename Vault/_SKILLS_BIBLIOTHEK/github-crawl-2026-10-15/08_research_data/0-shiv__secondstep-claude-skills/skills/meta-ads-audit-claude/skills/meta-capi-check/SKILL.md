# Meta Conversions API (CAPI) Audit

## Command
`/meta capi`

## Description
Deep validation of Meta Conversions API implementation, server event matching, Event Match Quality (EMQ) scoring, parameter completeness, and deduplication with browser Pixel events. CAPI is Meta's server-side tracking solution that bypasses browser limitations like ad blockers, ITP, and cookie restrictions.

## Why CAPI Matters

Since iOS 14.5 and increasing browser privacy restrictions, browser-side Pixel tracking alone captures only 60-70% of conversion events. CAPI fills the gap by sending events server-to-server:

- **Ad blocker bypass**: 30-40% of users run ad blockers that block Pixel
- **iOS ATT compliance**: CAPI works regardless of ATT opt-in status
- **Improved signal quality**: Server events include richer customer data
- **Better optimization**: More complete data = better delivery optimization
- **Higher EMQ scores**: CAPI + Pixel together typically achieve EMQ 7.0+ vs 4.0 Pixel-only

Accounts with properly configured CAPI see an average **13% reduction in cost per acquisition** compared to Pixel-only tracking.

## Audit Checklist (30 Points)

### 1. CAPI Implementation Verification (8 points)

- [ ] **CAPI Active**: Verify server events are being received in Events Manager
- [ ] **Integration Method**: Document implementation method:
  - Direct API integration (custom server code)
  - Partner integration (Shopify, WordPress, etc.)
  - Google Tag Manager Server-Side
  - Zapier/Make.com webhook relay
  - Meta's Conversions API Gateway
- [ ] **Access Token Valid**: Confirm API access token is active and has correct permissions
- [ ] **Pixel ID Linked**: CAPI events are sent to the correct Pixel ID
- [ ] **SSL/TLS**: Server endpoint uses HTTPS (required by Meta)
- [ ] **Event Delivery Latency**: Events should arrive within 1 hour of occurrence (ideally < 5 minutes)
- [ ] **Error Rate**: Check API error responses (target: < 1% error rate)
- [ ] **Rate Limiting**: Verify batch size and frequency are within Meta's limits (1,000 events per batch, 2,000 batches/hour)

### 2. Event Match Quality (EMQ) Scoring (7 points)

EMQ measures how well Meta can match server events to Facebook users. Scale: 0-10.

| EMQ Score | Rating | Meaning |
|-----------|--------|---------|
| 8.0-10.0 | Excellent | Maximum match rate, optimal optimization |
| 6.0-7.9 | Good | Strong matching, minor improvements possible |
| 4.0-5.9 | Fair | Moderate matching, significant room for improvement |
| 2.0-3.9 | Poor | Low match rate, optimization severely impacted |
| 0-1.9 | Critical | Almost no matching, CAPI is essentially non-functional |

**EMQ Improvement Checklist:**
- [ ] **EMQ Score Retrieved**: Pull current EMQ from Events Manager for each event type
- [ ] **Email Parameter**: Hashed email (`em`) sent with events (highest impact parameter)
- [ ] **Phone Parameter**: Hashed phone number (`ph`) sent with events
- [ ] **First/Last Name**: Hashed `fn` and `ln` parameters included
- [ ] **External ID**: `external_id` parameter maps to your CRM/user ID
- [ ] **fbp Cookie**: First-party `_fbp` cookie value passed from browser to server
- [ ] **fbc Parameter**: Click ID (`_fbc`) captured from URL and passed in events

### 3. Parameter Completeness (6 points)

Every CAPI event should include these parameter categories:

**Required Parameters:**
- [ ] `event_name` — Standard or custom event name
- [ ] `event_time` — Unix timestamp of the event
- [ ] `action_source` — Where the event occurred (website, app, email, etc.)
- [ ] `event_source_url` — URL where the event happened
- [ ] `user_data` — At minimum: hashed email OR phone number

**Recommended Parameters:**
- [ ] `custom_data` — Event-specific data (value, currency, content_ids, etc.)
- [ ] `event_id` — Unique ID for deduplication with Pixel events
- [ ] `opt_out` — Respect user privacy preferences
- [ ] `data_processing_options` — LDU compliance for California/other jurisdictions

**Customer Information Parameters (for EMQ):**
| Parameter | Field | Impact on EMQ |
|-----------|-------|---------------|
| `em` | Email (SHA256) | Very High |
| `ph` | Phone (SHA256) | High |
| `fn` | First Name (SHA256) | Medium |
| `ln` | Last Name (SHA256) | Medium |
| `ct` | City (SHA256) | Low |
| `st` | State (SHA256) | Low |
| `zp` | Zip Code (SHA256) | Low |
| `country` | Country Code (SHA256) | Low |
| `external_id` | CRM User ID (SHA256) | High |
| `fbp` | Facebook Pixel cookie | Very High |
| `fbc` | Facebook Click ID | Very High |
| `client_ip_address` | User IP | Medium |
| `client_user_agent` | Browser UA string | Medium |

### 4. Deduplication with Pixel Events (5 points)

When both Pixel and CAPI send the same event, deduplication prevents double-counting.

- [ ] **Event ID Matching**: Same `event_id` used in both Pixel `fbq()` call and CAPI request
- [ ] **Event Name Matching**: `event_name` is identical in both Pixel and CAPI (case-sensitive)
- [ ] **Dedup Window Compliance**: Both events arrive within 48 hours of each other
- [ ] **Dedup Rate in Events Manager**: Check the "Browser & Server" overlap percentage
- [ ] **No Over-Dedup**: Verify legitimate separate events are not being incorrectly deduplicated

**Dedup Validation Process:**
1. Fire a test event on the website with a known `event_id`
2. Verify the same `event_id` appears in both Pixel Helper and server logs
3. Check Events Manager — the event should show as "Browser & Server" (not counted twice)

### 5. CAPI Event Coverage (4 points)

- [ ] **All Standard Events Covered**: Every Pixel standard event also has a CAPI counterpart
- [ ] **Key Conversion Events**: At minimum, Purchase/Lead events are sent via CAPI
- [ ] **Mid-Funnel Events**: AddToCart, InitiateCheckout also sent via CAPI
- [ ] **Offline Events**: If applicable, offline conversions (phone calls, in-store) sent via CAPI

## Common CAPI Issues & Fixes

### Issue: EMQ Score Below 4.0
**Symptom**: Poor event matching, optimization not improving
**Root Cause**: Missing customer information parameters
**Fix**: Add hashed email, phone, and `fbp`/`fbc` cookies to all CAPI events. The `fbp` cookie is especially impactful — capture it from the browser's `_fbp` cookie and pass it to your server.

### Issue: Duplicate Conversions
**Symptom**: Conversion count is approximately 2x actual conversions
**Root Cause**: `event_id` not implemented or not matching between Pixel and CAPI
**Fix**: Generate a unique ID (UUID or transaction ID) at event time, pass it in both `fbq('track', 'Purchase', data, {eventID: 'xxx'})` and the CAPI `event_id` field.

### Issue: CAPI Events Delayed > 1 Hour
**Symptom**: Events Manager shows events arriving late, optimization is sluggish
**Root Cause**: Server processing queue is backed up, or using batch mode with long intervals
**Fix**: Send events in near real-time. If batching, send batches every 5-15 minutes maximum.

### Issue: 403/401 API Errors
**Symptom**: Events Manager shows no CAPI events, server logs show auth errors
**Root Cause**: Expired or invalid access token
**Fix**: Generate a new System User token in Business Manager > Business Settings > System Users. Set token to never expire.

### Issue: Missing fbp/fbc Parameters
**Symptom**: EMQ score stuck at 4-5 despite having email/phone
**Root Cause**: First-party cookies not being captured from browser and sent to server
**Fix**: On form submission, read `document.cookie` for `_fbp` and URL params for `fbclid`. Send these values to your server alongside form data, then include in CAPI events.

## Data Requirements

To run this audit, provide one or more of:
1. **Events Manager CAPI tab screenshot** — Shows event volume, EMQ, error rate
2. **Server-side code/configuration** — Implementation details (GTM SS container, custom code, etc.)
3. **API response logs** — Sample CAPI request/response pairs
4. **Partner integration settings** — Shopify/WordPress CAPI plugin configuration
5. **Meta Business Manager access** — For live API validation

## Output Format

```
## Conversions API Audit Results

**Score: XX/100** (Grade: X)
**EMQ Score: X.X/10**
**CAPI Events Active: X/9 standard events**
**Dedup Status: [Active/Inactive/Partial]**
**API Error Rate: X.X%**

### Critical Findings (P0)
- [e.g., CAPI not sending Purchase events — 40% of conversions lost]

### High Priority (P1)
- [e.g., EMQ at 3.2 — missing email and fbp parameters]

### Medium Priority (P2)
- [e.g., No offline conversion events configured]

### EMQ Parameter Coverage
| Parameter | Status | Impact |
|-----------|--------|--------|
| Email (em) | Sent | Very High |
| Phone (ph) | Missing | High |
| fbp | Missing | Very High |
| fbc | Sent | Very High |
| external_id | Missing | High |

### Recommendations
1. [Action item with expected EMQ improvement]
```
