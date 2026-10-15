# Track Meta Pixel — Sub-Skill

## Command
`/track meta-pixel`

## Description
Audits Meta Pixel installation, standard event configuration, custom events, parameter accuracy, and event deduplication. The Meta Pixel is the client-side tracking foundation for Facebook and Instagram advertising. A misconfigured Pixel leads to poor audience building, broken optimization, and wasted ad spend. This skill validates every layer of the Pixel implementation.

---

## Meta Pixel Architecture

### How It Works
The Meta Pixel is a JavaScript snippet that fires HTTP requests to Facebook's servers when users take actions on your website. Each request carries event data (what happened), user data (who did it, for matching), and context data (page URL, referrer, device).

### Base Pixel Code
```html
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"/></noscript>
```

---

## Validation Checklist

### 1. Pixel Installation

**Presence Check:**
- Pixel code in `<head>` of every page (or loaded via GTM)
- `fbq('init', 'PIXEL_ID')` called with correct Pixel ID
- `fbq('track', 'PageView')` fires on every page load
- noscript fallback image tag present

**Common Installation Issues:**
- Pixel only on homepage, missing from inner pages
- Wrong Pixel ID (staging vs production, old vs new)
- Multiple `fbq('init')` calls with different IDs (causes double-counting)
- Pixel loaded after consent but PageView not fired post-consent
- SPA not re-firing PageView on route changes
- Pixel blocked by ad blockers (use CAPI as redundancy)

### 2. Standard Events

Meta defines 17 standard events. Validate each relevant event fires with correct parameters:

| Event | When to Fire | Key Parameters |
|-------|-------------|----------------|
| `PageView` | Every page load | (none required) |
| `ViewContent` | Product/service page viewed | content_name, content_ids, content_type, value, currency |
| `AddToCart` | Item added to cart | content_ids, content_type, value, currency |
| `InitiateCheckout` | Checkout started | content_ids, num_items, value, currency |
| `AddPaymentInfo` | Payment info entered | content_category, value, currency |
| `Purchase` | Transaction completed | content_ids, content_type, value, currency, num_items |
| `Lead` | Lead form submitted | content_name, value, currency |
| `CompleteRegistration` | Sign-up completed | content_name, value, currency, status |
| `Search` | Search performed | search_string, content_category |
| `AddToWishlist` | Item wishlisted | content_ids, content_type, value, currency |
| `Contact` | Contact initiated | (none required) |
| `CustomizeProduct` | Product customized | content_ids, content_type |
| `Donate` | Donation made | value, currency |
| `FindLocation` | Location searched | (none required) |
| `Schedule` | Appointment scheduled | (none required) |
| `StartTrial` | Trial started | value, currency, predicted_ltv |
| `SubmitApplication` | Application submitted | (none required) |

**Implementation Example:**
```javascript
// Purchase event
fbq('track', 'Purchase', {
  content_ids: ['SKU123', 'SKU456'],
  content_type: 'product',
  value: 149.99,
  currency: 'USD',
  num_items: 2
});
```

### 3. Custom Events

For actions not covered by standard events:
```javascript
fbq('trackCustom', 'QualifiedLead', {
  lead_score: 85,
  source: 'contact_form'
});
```

**Validation:**
- Custom event names are descriptive and consistent
- Parameters provide useful data for optimization
- Custom events are mapped to custom conversions in Events Manager
- Not duplicating a standard event with a custom event name

### 4. Pixel Helper Diagnostics

**Using Meta Pixel Helper (Chrome Extension):**
- Install from Chrome Web Store
- Visit each page type and check:
  - Green checkmark: Pixel firing correctly
  - Yellow warning: Pixel active but issues detected
  - Red error: Pixel not found or broken
  - Event count matches expected (no duplicates)
  - Parameters present and correctly formatted

**Common Pixel Helper Warnings:**
- "Pixel activated multiple times" — duplicate init calls
- "Event received after long delay" — tag firing too late
- "Missing required parameter" — value or currency missing from Purchase
- "Pixel ID mismatch" — wrong ID configured

### 5. Event Deduplication

**Why It Matters:**
If you use both Meta Pixel (client-side) and Conversions API (server-side), the same event can be counted twice. Deduplication ensures each conversion is counted only once.

**How to Deduplicate:**
- Assign a unique `event_id` to each event
- Send the same `event_id` from both Pixel and CAPI
- Meta deduplicates events with matching `event_id` within a 48-hour window

```javascript
// Client-side: Pixel with event_id
var eventID = 'order_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
fbq('track', 'Purchase', {value: 99.99, currency: 'USD'}, {eventID: eventID});

// Server-side: CAPI with same event_id
// Send eventID as event_id parameter in CAPI request
```

**Deduplication Validation:**
- Check Events Manager > event_id coverage percentage
- Compare Pixel-only events vs CAPI events vs deduplicated total
- If deduplicated count equals Pixel count, CAPI events are being dropped (dedup working)
- If total is Pixel + CAPI combined, deduplication is NOT working (double-counting)

---

## Diagnostic Queries

1. What is your Meta Pixel ID?
2. How is the Pixel installed (direct, GTM, partner integration)?
3. Which standard events should be firing?
4. Are you using Conversions API alongside the Pixel?
5. What does Meta Events Manager show for event activity?

---

## Scoring Contribution

This sub-skill contributes to the **15 points** for Event Configuration:

- Pixel present on all pages: 4 points
- Standard events configured correctly: 4 points
- Parameters complete (value, currency, content_ids): 3 points
- Event deduplication with CAPI: 2 points
- No duplicate Pixel init or double-firing: 2 points

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| Pixel not installed | Critical | Zero Meta conversion data |
| Purchase/Lead event missing | Critical | Can't optimize for conversions |
| Wrong Pixel ID | Critical | Data going to wrong account |
| No event deduplication | High | Double-counted conversions, inflated ROAS |
| Missing value/currency on Purchase | High | Can't use value optimization |
| Duplicate Pixel init | Medium | Over-reported PageViews |
| Missing ViewContent/AddToCart | Medium | Incomplete funnel data |
| No custom events for key actions | Low | Less optimization signal |
