# Track LinkedIn Insight — Sub-Skill

## Command
`/track linkedin`

## Description
Validates LinkedIn Insight Tag installation, conversion tracking configuration, and LinkedIn Conversions API (CAPI) setup. LinkedIn advertising is particularly important for B2B lead generation, and accurate conversion tracking is what separates "we think LinkedIn works" from "we know LinkedIn generates $X in pipeline." This skill validates every component of LinkedIn's tracking infrastructure.

---

## LinkedIn Insight Tag

### What It Does
The Insight Tag is a lightweight JavaScript snippet that enables:
- Conversion tracking (form submissions, page visits, sign-ups)
- Website audience building (retargeting pools)
- Website demographics reporting (company, industry, job function of visitors)

### Base Tag Code
```html
<script type="text/javascript">
_linkedin_partner_id = "YOUR_PARTNER_ID";
window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
window._linkedin_data_partner_ids.push(_linkedin_partner_id);
</script>
<script type="text/javascript">
(function(l) {
if (!l){window.lintrk = function(a,b){window.lintrk.q.push([a,b])};
window.lintrk.q=[]}
var s = document.getElementsByTagName("script")[0];
var b = document.createElement("script");
b.type = "text/javascript";b.async = true;
b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
s.parentNode.insertBefore(b, s);})(window.lintrk);
</script>
<noscript>
<img height="1" width="1" style="display:none;" alt=""
src="https://px.ads.linkedin.com/collect/?pid=YOUR_PARTNER_ID&fmt=gif" />
</noscript>
```

### Installation Validation

**Presence Check:**
- Insight Tag present on every page of the website
- Partner ID matches the LinkedIn Campaign Manager account
- Tag loads asynchronously (has `async` attribute)
- noscript fallback present

**Verification Methods:**
1. **LinkedIn Tag Validator** — Chrome extension by LinkedIn
2. **Browser DevTools** — Network tab, filter for `snap.licdn.com` or `px.ads.linkedin.com`
3. **Campaign Manager** — Analyze > Insight Tag > shows domains where tag is detected
4. **GTM Preview Mode** — If implemented via GTM, verify tag fires in preview

**Common Issues:**
- Tag not on all pages (missing from landing pages, thank you pages)
- Wrong Partner ID (testing vs production account)
- Tag blocked by consent management platform
- Tag conflicts with other LinkedIn tags (old deprecated versions)
- SPA not re-triggering tag on navigation

---

## Conversion Tracking Setup

### Event-Specific Conversions (Recommended)

LinkedIn's event-specific tracking uses the `lintrk` function to fire conversion events on specific actions:

```javascript
// Fire on form submission
lintrk('track', { conversion_id: 12345678 });
```

**Setup:**
1. Create conversion action in Campaign Manager > Analyze > Conversion Tracking
2. Choose "Online Conversion" and select event type
3. Set attribution window (1, 7, 30, or 90 days post-click; 1 or 7 days view-through)
4. Get the conversion ID
5. Add `lintrk('track')` call to your website at the conversion point

**Event Types:**
- Add to Cart
- Download
- Install
- Key Page View
- Lead
- Purchase
- Sign Up
- Other

### URL-Based Conversions

Track conversions by matching thank you page URLs:

**Setup:**
1. Create conversion in Campaign Manager
2. Choose "URL/Page" based
3. Define URL rules:
   - **Equals** — Exact URL match
   - **Starts with** — URL prefix match
   - **Contains** — Substring match

**Example Rules:**
- Page URL equals `https://example.com/thank-you`
- Page URL contains `/confirmation`
- Page URL starts with `https://example.com/success/`

**Pros vs Cons:**
- Pros: No additional code needed beyond Insight Tag, easy to set up
- Cons: Less precise (anyone visiting the URL counts), doesn't work for SPAs without URL changes, no custom value passing

### Validation Checklist

1. **Conversion actions created**
   - At least one conversion action per campaign objective
   - Lead gen campaigns: Lead or Sign Up event
   - E-commerce: Purchase event with value

2. **Attribution windows set correctly**
   - B2B recommended: 30-day click-through, 7-day view-through
   - Shorter windows = fewer attributed conversions but higher confidence
   - Match with your sales cycle length

3. **Conversion firing correctly**
   - Trigger a test conversion and check Campaign Manager
   - Allow 24 hours for data to appear
   - Verify conversion count matches actual form submissions

4. **Campaign association**
   - Conversion actions associated with the correct campaigns
   - "Include in reporting" enabled for primary conversions

---

## LinkedIn Conversions API (CAPI)

### Overview
LinkedIn CAPI sends conversion events server-to-server, similar to Meta CAPI. It provides more reliable tracking that is not affected by ad blockers or browser cookie restrictions.

### Setup Requirements
- LinkedIn Campaign Manager account with API access
- OAuth 2.0 access token with `r_conversions` and `w_conversions` permissions
- Server-side code to send HTTP POST requests to LinkedIn's API

### API Endpoint
```
POST https://api.linkedin.com/rest/conversionEvents
```

### Event Payload
```json
{
  "conversion": "urn:lla:llaPartnerConversion:CONVERSION_ID",
  "conversionHappenedAt": 1710300000000,
  "conversionValue": {
    "currencyCode": "USD",
    "amount": "500.00"
  },
  "user": {
    "userIds": [
      {
        "idType": "SHA256_EMAIL",
        "idValue": "<sha256_hash_of_email>"
      },
      {
        "idType": "LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID",
        "idValue": "<li_fat_id_value>"
      }
    ],
    "userInfo": {
      "firstName": "<sha256_hash>",
      "lastName": "<sha256_hash>",
      "companyName": "<sha256_hash>",
      "title": "<sha256_hash>",
      "countryCode": "US"
    }
  },
  "eventId": "unique_event_id_for_dedup"
}
```

### Key Parameters
- **li_fat_id** — LinkedIn First-Party Ad Tracking ID, similar to GCLID. Captured from URL parameter or cookie. Critical for matching.
- **SHA256_EMAIL** — Hashed email, primary matching key
- **eventId** — For deduplication between Insight Tag and CAPI events
- **conversionHappenedAt** — Epoch timestamp in milliseconds

### CAPI Validation
1. API credentials valid and not expired
2. Conversion events appearing in Campaign Manager
3. Event match rate visible (higher = better)
4. Deduplication working (not double-counting with Insight Tag)
5. `li_fat_id` captured and stored from landing page URL

---

## Scoring Contribution

This sub-skill contributes to the overall Tracking Health Score:

- Insight Tag installed on all pages: 3 points
- Conversion actions configured: 3 points
- Event-specific tracking (not just URL): 2 points
- LinkedIn CAPI active: 2 points

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| Insight Tag not installed | Critical | No LinkedIn tracking at all |
| No conversion actions created | Critical | Can't measure campaign ROI |
| Wrong Partner ID | Critical | Data going to wrong account |
| URL-based only (no event tracking) | Medium | Less precise conversion data |
| No CAPI setup | Medium | Missing ad-blocked conversions |
| Attribution window too short | Medium | Underreported conversions |
| li_fat_id not captured | Medium | Lower CAPI match rate |
| Tag not on all pages | High | Incomplete retargeting audiences |
