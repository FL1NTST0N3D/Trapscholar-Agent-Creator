# Track TikTok Pixel — Sub-Skill

## Command
`/track tiktok`

## Description
Audits TikTok Pixel installation, standard event configuration, Events API setup, and advanced matching parameters. TikTok is increasingly important for e-commerce and D2C brands, and its tracking ecosystem mirrors Meta's Pixel + CAPI model. This skill validates that your TikTok tracking stack captures every conversion accurately and provides sufficient user data for the TikTok algorithm to optimize effectively.

---

## TikTok Pixel

### Base Pixel Code
```html
<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e};ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};
  ttq.load('YOUR_PIXEL_ID');
  ttq.page();
}(window, document, 'ttq');
</script>
```

### Installation Validation

**Presence Check:**
- TikTok Pixel code present on all pages
- `ttq.load('PIXEL_ID')` called with correct Pixel ID
- `ttq.page()` fires on every page load (equivalent to PageView)
- Pixel loads asynchronously

**Verification Methods:**
1. **TikTok Pixel Helper** — Chrome extension, shows events firing and parameters
2. **Browser DevTools** — Network tab, filter for `analytics.tiktok.com`
3. **TikTok Events Manager** — Check event activity and diagnostics
4. **GTM Preview** — If implemented via GTM

**Common Issues:**
- Pixel missing from key pages (checkout, thank you)
- Duplicate Pixel installations (direct + GTM)
- Pixel blocked by ad blockers (mitigate with Events API)
- SPA not calling `ttq.page()` on route changes
- Consent platform preventing Pixel from loading

---

## Standard Events

TikTok supports these standard events for optimization:

| Event | Method | When to Fire |
|-------|--------|-------------|
| `ViewContent` | `ttq.track('ViewContent', {...})` | Product/service page viewed |
| `ClickButton` | `ttq.track('ClickButton', {...})` | Important button clicked |
| `Search` | `ttq.track('Search', {...})` | Search performed |
| `AddToWishlist` | `ttq.track('AddToWishlist', {...})` | Item wishlisted |
| `AddToCart` | `ttq.track('AddToCart', {...})` | Item added to cart |
| `InitiateCheckout` | `ttq.track('InitiateCheckout', {...})` | Checkout started |
| `AddPaymentInfo` | `ttq.track('AddPaymentInfo', {...})` | Payment info entered |
| `CompletePayment` | `ttq.track('CompletePayment', {...})` | Purchase completed |
| `PlaceAnOrder` | `ttq.track('PlaceAnOrder', {...})` | Order placed |
| `Contact` | `ttq.track('Contact', {...})` | Contact form submitted |
| `Download` | `ttq.track('Download', {...})` | File/app downloaded |
| `SubmitForm` | `ttq.track('SubmitForm', {...})` | Form submitted |
| `CompleteRegistration` | `ttq.track('CompleteRegistration', {...})` | Registration completed |
| `Subscribe` | `ttq.track('Subscribe', {...})` | Newsletter/service subscribed |

**Event Parameters:**
```javascript
ttq.track('CompletePayment', {
  content_id: 'SKU123',
  content_type: 'product',
  content_name: 'Blue Widget',
  quantity: 2,
  price: 49.99,
  value: 99.98,
  currency: 'USD'
});
```

**Validation for Each Event:**
- Event fires at the correct moment (not too early, not too late)
- Parameters populated with correct values (not null, undefined, or placeholder)
- Value and currency present for monetary events (CompletePayment, AddToCart)
- content_id matches product catalog IDs (for dynamic product ads)
- No duplicate event fires on the same action

---

## Advanced Matching

Advanced matching sends hashed user data alongside Pixel events, improving match rates similar to Meta's Advanced Matching and Google's Enhanced Conversions.

### Automatic Advanced Matching
Enable in TikTok Events Manager — TikTok automatically scans page forms for identifiable fields.

### Manual Advanced Matching
```javascript
ttq.identify({
  email: 'user@example.com',           // hashed automatically by SDK
  phone_number: '+12125551234',         // E.164 format
  external_id: 'customer_12345'         // your internal ID
});
```

**Supported Parameters:**
| Parameter | Key | Format |
|-----------|-----|--------|
| Email | `email` | Plain text (SDK hashes) or SHA-256 |
| Phone | `phone_number` | E.164 format |
| External ID | `external_id` | Your internal user/customer ID |

**Validation:**
- `ttq.identify()` called before or alongside conversion events
- At least email provided (phone and external_id add incremental value)
- Data format correct (email lowercase, phone E.164)
- Check Events Manager for match rate percentage

---

## TikTok Events API

### Overview
TikTok Events API is the server-side equivalent of the Pixel, similar to Meta's Conversions API. It sends events from your server to TikTok, ensuring tracking works even when the Pixel is blocked.

### API Endpoint
```
POST https://business-api.tiktok.com/open_api/v1.3/event/track/
```

### Event Payload
```json
{
  "pixel_code": "YOUR_PIXEL_ID",
  "event": "CompletePayment",
  "event_id": "unique_order_id_123",
  "timestamp": "2026-03-13T10:30:00-05:00",
  "context": {
    "ad": {
      "callback": "ttclid_value"
    },
    "page": {
      "url": "https://example.com/thank-you",
      "referrer": "https://example.com/checkout"
    },
    "user": {
      "external_id": "sha256_hash",
      "email": "sha256_hash",
      "phone": "sha256_hash",
      "ip": "203.0.113.1",
      "user_agent": "Mozilla/5.0..."
    }
  },
  "properties": {
    "contents": [
      {
        "content_id": "SKU123",
        "content_type": "product",
        "content_name": "Blue Widget",
        "quantity": 2,
        "price": 49.99
      }
    ],
    "value": 99.98,
    "currency": "USD"
  }
}
```

### Key Parameters
- **ttclid** — TikTok Click ID, appended to landing page URL on ad click. Equivalent to GCLID/fbclid.
- **event_id** — Unique event identifier for deduplication between Pixel and Events API
- **User data** — Email, phone, external_id (SHA-256 hashed), plus IP and user agent

### Events API Validation
1. API access token valid and scoped correctly
2. Events appearing in Events Manager from "Server" source
3. Event deduplication with Pixel working (matching event_id)
4. ttclid captured from landing page URL and stored
5. User data parameters sending correctly (check match quality)
6. No API error responses (check server logs)

---

## Scoring Contribution

This sub-skill contributes to the overall Tracking Health Score:

- Pixel installed on all pages: 3 points
- Standard events configured correctly: 3 points
- Advanced matching active: 2 points
- Events API active with deduplication: 2 points

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| Pixel not installed | Critical | No TikTok conversion data |
| CompletePayment/SubmitForm missing | Critical | Can't optimize for conversions |
| No event values | High | Value optimization impossible |
| No advanced matching | High | Low match rate, poor attribution |
| No Events API | Medium | Missing ad-blocked conversions |
| ttclid not captured | Medium | Lower Events API match rate |
| Duplicate event fires | Medium | Over-reported conversions |
| Missing content_id | Low | Dynamic product ads won't work |
