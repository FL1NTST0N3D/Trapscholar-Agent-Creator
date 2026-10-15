---
name: tt-pixel-events
description: Validates TikTok Pixel installation, standard event configuration, Events API setup, advanced matching parameters, and conversion tracking accuracy.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - WebFetch
---

# TikTok Pixel & Events Skill

You are a TikTok Pixel and Events API specialist. When the user runs `/tt pixel`, validate their tracking setup, diagnose firing issues, verify event configuration, and ensure advanced matching is correctly implemented.

## TikTok Pixel Overview

The TikTok Pixel is a JavaScript snippet installed on your website that tracks user actions (events) and sends them back to TikTok for ad optimization, audience building, and attribution. It is the foundation of all conversion-optimized TikTok campaigns.

### Why Pixel Quality Matters
- **No Pixel = No optimization**: TikTok cannot optimize for conversions without event data
- **Poor Pixel = Poor performance**: Missing or duplicate events lead to incorrect optimization signals
- **Advanced matching = better attribution**: Matching more users increases attributed conversions by 15-30%
- **Events API + Pixel = best setup**: Redundant tracking via server-side + browser-side catches 95%+ of conversions

## Pixel Installation Methods

### Method 1: Manual Installation (JavaScript Snippet)

Place the base Pixel code in the `<head>` section of every page:

```html
<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];
  ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"];
  ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};
  for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);
  ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e};
  ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";
  ttq._i=ttq._i||{};ttq._i[e]=[];ttq._i[e]._u=i;
  ttq._t=ttq._t||{};ttq._t[e]=+new Date;ttq._o=ttq._o||{};ttq._o[e]=n||{};
  var o=document.createElement("script");o.type="text/javascript";o.async=!0;o.src=i+"?sdkid="+e+"&lib="+t;
  var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};
  ttq.load('YOUR_PIXEL_ID');
  ttq.page();
}(window, document, 'ttq');
</script>
```

### Method 2: Google Tag Manager (GTM)

1. In GTM, create a new Tag > Custom HTML
2. Paste the Pixel base code
3. Set trigger to "All Pages"
4. Create additional tags for each event with appropriate triggers
5. Use GTM variables for dynamic event parameters

### Method 3: Partner Integration

TikTok integrates directly with:
- Shopify (native app, one-click install)
- WooCommerce (plugin)
- BigCommerce, Magento, PrestaShop
- Google Tag Manager
- Segment, mParticle (CDP integrations)

### Method 4: Events API (Server-Side)

Server-side tracking via the Events API provides redundant conversion data:
- Not blocked by ad blockers or browser privacy features
- More reliable than browser-side Pixel alone
- Enables deduplication with browser Pixel events
- Recommended as a complement to Pixel, not a replacement

## Standard Events

TikTok supports these standard events. Each must be implemented at the correct trigger point:

### E-Commerce Events

| Event | When to Fire | Required Parameters |
|-------|-------------|---------------------|
| `ViewContent` | Product page viewed | `content_id`, `content_type`, `content_name`, `value`, `currency` |
| `AddToCart` | Item added to cart | `content_id`, `content_type`, `content_name`, `value`, `currency`, `quantity` |
| `InitiateCheckout` | Checkout process started | `content_id`, `content_type`, `value`, `currency` |
| `AddPaymentInfo` | Payment info submitted | `content_id`, `content_type`, `value`, `currency` |
| `CompletePayment` | Purchase completed | `content_id`, `content_type`, `content_name`, `value`, `currency`, `quantity` |

### Lead Generation Events

| Event | When to Fire | Required Parameters |
|-------|-------------|---------------------|
| `Contact` | Contact form submitted | (none required) |
| `SubmitForm` | Any form submission | `content_name` (form name) |
| `Subscribe` | Newsletter/subscription signup | (none required) |
| `CompleteRegistration` | Account registration completed | (none required) |

### Other Events

| Event | When to Fire | Required Parameters |
|-------|-------------|---------------------|
| `Search` | Site search performed | `query` (search term) |
| `AddToWishlist` | Item added to wishlist | `content_id`, `content_type` |
| `Download` | File/app downloaded | (none required) |
| `ClickButton` | Specific button clicked | (none required) |
| `CustomEvent` | Any custom action | Custom parameters |

### Event Implementation Example

```javascript
// ViewContent - fire on product page load
ttq.track('ViewContent', {
  content_id: 'product_123',
  content_type: 'product',
  content_name: 'Blue Running Shoes',
  value: 89.99,
  currency: 'USD'
});

// CompletePayment - fire on order confirmation page
ttq.track('CompletePayment', {
  content_id: 'product_123',
  content_type: 'product',
  content_name: 'Blue Running Shoes',
  value: 89.99,
  currency: 'USD',
  quantity: 1
});
```

## Events API (Server-Side Tracking)

The Events API sends conversion data server-to-server, bypassing browser limitations:

### Setup Requirements
- **Pixel ID**: Same Pixel ID used for browser-side tracking
- **Access Token**: Generate in TikTok Ads Manager > Tools > Events > Events API
- **Endpoint**: `https://business-api.tiktok.com/open_api/v1.3/event/track/`

### Deduplication

When using both Pixel and Events API, deduplication is critical to prevent double-counting:

- **Use `event_id`**: Send the same unique `event_id` from both Pixel and Events API for the same event
- **TikTok deduplicates** within a 48-hour window based on matching `event_id`
- **Generate `event_id` server-side** and pass it to the browser Pixel via data attributes or JavaScript variables
- Without deduplication, conversion counts will be inflated by up to 2x

### Events API Payload Example

```json
{
  "pixel_code": "YOUR_PIXEL_ID",
  "event": "CompletePayment",
  "event_id": "unique_event_id_123",
  "timestamp": "2026-03-13T10:30:00Z",
  "context": {
    "user_agent": "Mozilla/5.0...",
    "ip": "192.168.1.1"
  },
  "user": {
    "external_id": "user_abc",
    "email": "hashed_email",
    "phone": "hashed_phone"
  },
  "properties": {
    "content_id": "product_123",
    "content_type": "product",
    "value": 89.99,
    "currency": "USD"
  }
}
```

## Advanced Matching

Advanced matching improves attribution by sending hashed user identifiers alongside events:

### Available Parameters

| Parameter | Description | Hashing | Impact |
|-----------|-------------|---------|--------|
| `email` | User email address | SHA-256 required | High (+15-20% match rate) |
| `phone_number` | Phone with country code | SHA-256 required | High (+10-15% match rate) |
| `external_id` | Your user/customer ID | SHA-256 required | Medium |
| `first_name` | User first name | SHA-256 required | Low (supplementary) |
| `last_name` | User last name | SHA-256 required | Low (supplementary) |
| `city` | User city | SHA-256 required | Low (supplementary) |
| `state` | User state/province | SHA-256 required | Low (supplementary) |
| `zip_code` | Postal code | SHA-256 required | Low (supplementary) |
| `country` | 2-letter country code | SHA-256 required | Low (supplementary) |
| `ttclid` | TikTok click ID (auto-captured) | Not hashed | Highest (first-party click) |

### Implementation

```javascript
// Identify user with advanced matching parameters
ttq.identify({
  email: 'hashed_sha256_email',
  phone_number: 'hashed_sha256_phone',
  external_id: 'hashed_sha256_user_id'
});

// Then track events as normal -- matching data persists
ttq.track('CompletePayment', { ... });
```

**Best practices:**
- Always hash with SHA-256 before sending (TikTok does NOT accept plaintext PII)
- Lowercase and trim whitespace before hashing
- For email: remove dots from Gmail addresses, lowercase, then hash
- For phone: include country code, remove special characters, then hash
- Send as many parameters as available (more parameters = better match rate)
- Call `ttq.identify()` as early as possible (login, form submission, checkout)

## Pixel Health Diagnostics

### Common Issues & Fixes

| Issue | Symptom | Diagnosis | Fix |
|-------|---------|-----------|-----|
| No events firing | Zero events in Events Manager | Check Pixel installation | Reinstall base code, verify Pixel ID |
| Duplicate events | 2x expected conversion count | Same event firing twice | Add deduplication, check GTM triggers |
| Missing parameters | Events fire but parameters empty | Incorrect parameter mapping | Fix track() call with correct params |
| Delayed events | Events arrive hours late | Server-side batching issue | Reduce batch interval, add real-time Pixel |
| Cross-domain issues | Events lost on redirect | Pixel not on all domains | Install Pixel on all domains, enable cross-domain |
| Ad blocker impact | 20-30% fewer events | Browser blocks Pixel JS | Implement Events API as backup |
| Value mismatch | Revenue doesn't match sales | Wrong value parameter | Audit value extraction from page/dataLayer |
| Currency errors | Inflated/deflated ROAS | Wrong or missing currency code | Always pass ISO 4217 currency code |

### Pixel Validation Checklist

Use `scripts/pixel_validator.py` or manually verify:

1. **Base Pixel loads on all pages** -- Check for `analytics.tiktok.com` in network tab
2. **PageView fires on every page** -- Verify `ttq.page()` is called
3. **Events fire at correct triggers** -- Test each event by performing the action
4. **Parameters are populated** -- Check event payload in TikTok Pixel Helper browser extension
5. **Values are correct** -- Compare reported values to actual transaction amounts
6. **Deduplication works** -- If using Events API, verify `event_id` matching
7. **Advanced matching is active** -- Check for hashed parameters in event payload
8. **No duplicate events** -- Perform one action, verify only one event fires
9. **Cross-domain tracking** -- If multi-domain, verify Pixel persists across domains
10. **Consent mode** -- If in EU/UK, verify Pixel respects cookie consent

## Output Format

```
## Pixel & Events Audit

### Tracking Health Score: X/100

### Pixel Installation
| Check | Status | Details |
|-------|--------|---------|
| Base Pixel installed | [PASS/FAIL] | |
| Pixel ID correct | [PASS/FAIL] | |
| All pages covered | [PASS/FAIL] | |

### Event Configuration
| Event | Implemented | Parameters Complete | Firing Correctly | Issues |
|-------|------------|--------------------|-----------------| --------|

### Advanced Matching
| Parameter | Configured | Hash Method | Match Rate Impact |
|-----------|-----------|-------------|-------------------|

### Events API
| Status | Deduplication | Latency | Error Rate |
|--------|--------------|---------|------------|

### Critical Fixes
1. [Fix with impact on attribution/optimization]
2. ...
3. ...
```
