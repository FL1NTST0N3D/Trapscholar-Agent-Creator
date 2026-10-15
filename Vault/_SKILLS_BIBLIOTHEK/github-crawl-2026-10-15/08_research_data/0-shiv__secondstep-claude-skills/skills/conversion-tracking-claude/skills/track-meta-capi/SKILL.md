# Track Meta CAPI — Sub-Skill

## Command
`/track capi`

## Description
Validates Meta Conversions API (CAPI) setup, server event configuration, Event Match Quality (EMQ) scoring, required customer information parameters, and integration method. CAPI sends conversion events from your server to Meta's servers, bypassing browser limitations. With Safari ITP blocking cookies and ad blockers filtering client-side tags, CAPI is now essential — not optional — for accurate Meta Ads measurement. Meta reports that advertisers using both Pixel + CAPI see a 19% average improvement in cost per action.

---

## How CAPI Works

```
User converts on website
        |
        v
Your Web Server captures event data
        |
        v
Server sends HTTPS POST to:
https://graph.facebook.com/v18.0/{PIXEL_ID}/events
        |
        v
Meta receives server event
        |
        ├── Matches with Pixel event (deduplication via event_id)
        └── Attributes conversion to ad click/view
```

### CAPI vs Pixel

| Aspect | Pixel (Client-Side) | CAPI (Server-Side) |
|--------|---------------------|---------------------|
| Fires from | User's browser | Your server |
| Ad blocker resistant | No | Yes |
| Cookie dependent | Yes | No |
| Data quality | Degrading | Stable |
| Setup complexity | Low | Medium-High |
| Real-time | Yes | Near real-time |
| Required for | Basic tracking | Reliable tracking |

---

## Integration Methods

### 1. Conversions API Gateway (Recommended for Most)
- Managed by Meta, deployed on your cloud (AWS/GCP)
- Minimal code — configure via Events Manager UI
- Automatically captures events from Pixel and forwards via CAPI
- Handles deduplication automatically
- Cost: cloud hosting fees ($50-200/mo depending on traffic)

### 2. Partner Integrations
- Shopify, WooCommerce, WordPress plugins with built-in CAPI
- GTM server-side container with Meta CAPI tag template
- Stape.io with Meta CAPI integration
- Zapier/Make for simple event forwarding

### 3. Direct API Integration
- Custom code sends events to Graph API
- Maximum control and flexibility
- Requires developer resources
- Best for: custom platforms, complex event logic

---

## Event Match Quality (EMQ) Scoring

### What Is EMQ?
EMQ is Meta's score (1.0 to 10.0) that measures how well your server events can be matched to Meta user accounts. Higher EMQ = more conversions attributed = better ad optimization.

**Target: EMQ 6.0 or higher.** Below 6.0 means you are sending insufficient customer information parameters (CIPs).

### How to Check EMQ
1. Events Manager > select your Pixel
2. Click on a specific event (e.g., Purchase)
3. Look at "Event Match Quality" score
4. Click to see parameter-level breakdown

### Customer Information Parameters (CIPs)

These are the user data fields you send with each CAPI event. More fields = higher match rate = higher EMQ:

| Parameter | API Key | Required? | Impact on EMQ |
|-----------|---------|-----------|---------------|
| Email | `em` | Strongly recommended | Very High |
| Phone | `ph` | Strongly recommended | Very High |
| First Name | `fn` | Recommended | High |
| Last Name | `ln` | Recommended | High |
| City | `ct` | Recommended | Medium |
| State | `st` | Recommended | Medium |
| Zip Code | `zp` | Recommended | Medium |
| Country | `country` | Recommended | Medium |
| External ID | `external_id` | Recommended | High |
| Client IP Address | `client_ip_address` | Required | High |
| Client User Agent | `client_user_agent` | Required | High |
| Facebook Click ID | `fbc` | Strongly recommended | Very High |
| Facebook Browser ID | `fbp` | Strongly recommended | Very High |

### Hashing Requirements
All user data parameters must be SHA-256 hashed before sending (except `fbc`, `fbp`, `client_ip_address`, `client_user_agent`):

```python
import hashlib

def hash_value(value):
    """Hash a value using SHA-256 for Meta CAPI."""
    if not value:
        return None
    normalized = str(value).strip().lower()
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

# Email: lowercase, trim
hash_value("John.Doe@Example.com")  # hash of "john.doe@example.com"

# Phone: digits only, E.164 without +
hash_value("+1-212-555-1234")  # hash of "12125551234"

# Name: lowercase, trim
hash_value(" John ")  # hash of "john"
```

---

## Validation Checklist

### 1. CAPI Active and Sending Events
- Events Manager shows both "Browser" and "Server" sources for events
- Server events appearing within expected latency (< 1 hour)
- Event volume from server roughly matches browser (accounting for ad blockers)
- No error responses from Graph API (check server logs)

### 2. EMQ Score Check
- **Per-event EMQ:** Check each conversion event separately
- **Target:** 6.0+ for all primary conversion events
- **Common low-EMQ causes:**
  - Missing `fbc` and `fbp` cookies (not forwarded from client)
  - No email or phone in server events
  - IP address and user agent not captured
  - Country/state/zip not included

### 3. Event Deduplication
- Every event has a unique `event_id`
- Same `event_id` sent from both Pixel and CAPI
- Events Manager shows deduplication percentage
- Total events should NOT be Pixel + CAPI (that means no dedup)

### 4. Required Event Parameters
For each conversion event, verify these are present:

**Purchase:**
```json
{
  "event_name": "Purchase",
  "event_time": 1710300000,
  "event_id": "order_abc123",
  "event_source_url": "https://example.com/thank-you",
  "action_source": "website",
  "user_data": {
    "em": ["<sha256_hash>"],
    "ph": ["<sha256_hash>"],
    "fn": ["<sha256_hash>"],
    "ln": ["<sha256_hash>"],
    "ct": ["<sha256_hash>"],
    "st": ["<sha256_hash>"],
    "zp": ["<sha256_hash>"],
    "country": ["<sha256_hash>"],
    "external_id": ["<sha256_hash>"],
    "client_ip_address": "203.0.113.1",
    "client_user_agent": "Mozilla/5.0...",
    "fbc": "fb.1.1610000000.AbCdEf",
    "fbp": "fb.1.1610000000.1234567890"
  },
  "custom_data": {
    "value": 149.99,
    "currency": "USD",
    "content_ids": ["SKU123"],
    "content_type": "product",
    "num_items": 1
  }
}
```

### 5. Test Events
- Use Events Manager > Test Events to send test server events
- Verify test events appear in the Test Events tab
- Check for error messages or warnings
- Use `test_event_code` parameter during testing

---

## Improving EMQ Score

**From 3.0 to 6.0+ roadmap:**

1. **Add client_ip_address and client_user_agent** — Capture from HTTP request headers on your server (+1.0-1.5 EMQ)
2. **Forward fbc and fbp cookies** — Read `_fbc` and `_fbp` cookies from the request and include in CAPI event (+1.0-2.0 EMQ)
3. **Include email** — Hash and send the user's email from form submission or account (+1.0-1.5 EMQ)
4. **Include phone** — Hash and send phone number if available (+0.5-1.0 EMQ)
5. **Add name and address fields** — First name, last name, city, state, zip, country (+0.5-1.0 EMQ)
6. **Include external_id** — Your internal user/customer ID, hashed (+0.5 EMQ)

---

## Scoring Contribution

This sub-skill contributes to the **15 points** for Enhanced Conversions / Matching:

- CAPI active and sending events: 4 points
- EMQ score 6.0+: 4 points
- Event deduplication working: 4 points
- All required CIPs present: 3 points

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| No CAPI at all | Critical | Missing 25-40% of conversions (ad-blocked users) |
| EMQ below 4.0 | Critical | Very low match rate, poor attribution |
| No event deduplication | High | Double-counted conversions |
| Missing fbc/fbp parameters | High | Significant EMQ reduction |
| Missing email/phone | High | Cannot match users to Meta accounts |
| EMQ 4.0-5.9 | Medium | Room for improvement in matching |
| Missing address fields | Low | Incremental EMQ improvement |
| Test events not validated | Low | May have undetected issues |
