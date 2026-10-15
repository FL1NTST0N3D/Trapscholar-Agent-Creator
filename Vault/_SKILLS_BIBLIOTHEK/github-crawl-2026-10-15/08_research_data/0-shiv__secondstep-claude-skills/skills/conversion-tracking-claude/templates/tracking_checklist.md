# Tracking Implementation Checklist

## Google Ads

### Google Tag (gtag.js)
- [ ] Google Tag present in `<head>` on ALL page templates
- [ ] Tag has `async` attribute
- [ ] Correct Conversion ID (AW-XXXXXXXXXX)
- [ ] gtag('config') fires on every page load
- [ ] SPA: gtag re-fires on route changes
- [ ] No duplicate Google Tags
- [ ] Tag not blocked by consent management platform (or consent mode configured)

### Conversion Actions
- [ ] All conversion actions created in Google Ads
- [ ] Counting method correct: One (leads) or Every (purchases)
- [ ] Conversion value assigned (static or dynamic)
- [ ] Conversion window appropriate (30/60/90 days)
- [ ] Attribution model set to data-driven (if eligible)
- [ ] Primary conversions: "Include in Conversions" = Yes
- [ ] Secondary conversions: "Include in Conversions" = No

### Enhanced Conversions for Web
- [ ] EC enabled in Google Ads settings
- [ ] Terms of service accepted
- [ ] User data sent via gtag API or GTM
- [ ] At minimum: email hashed and sent
- [ ] Ideally: email + phone + name + address
- [ ] Data normalized (lowercase, trimmed) before hashing
- [ ] EC diagnostics show "Recording enhanced conversions"

### Enhanced Conversions for Leads (EC4L)
- [ ] EC4L enabled in Google Ads settings
- [ ] GCLID captured from URL on landing page
- [ ] GCLID stored in hidden form field
- [ ] GCLID stored in cookie (for multi-page journeys)
- [ ] GCLID submitted with lead form
- [ ] CRM stores GCLID in dedicated field
- [ ] WBRAID/GBRAID also captured (iOS support)

### Server-Side GTM
- [ ] sGTM container deployed (Stape or GCP)
- [ ] Container URL on your subdomain (sgtm.yourdomain.com)
- [ ] DNS CNAME configured
- [ ] SSL certificate valid
- [ ] Transport URL set in client-side config
- [ ] Google Ads conversion tag in server container
- [ ] First-party cookies set by server
- [ ] Proxy mode enabled (ad blocker bypass)

### Offline Conversion Import
- [ ] Upload process exists (manual CSV or automated API)
- [ ] Upload frequency: daily or weekly
- [ ] Conversion action name matches exactly
- [ ] GCLID included in upload
- [ ] Conversion time in correct format
- [ ] Conversion value included
- [ ] Upload errors < 5%

---

## Meta Ads

### Meta Pixel
- [ ] Pixel base code in `<head>` on all pages
- [ ] Correct Pixel ID
- [ ] fbq('init') called once per page
- [ ] fbq('track', 'PageView') fires on every page
- [ ] noscript fallback present
- [ ] No duplicate Pixel initializations

### Standard Events
- [ ] Purchase event fires on order confirmation
- [ ] Purchase includes: value, currency, content_ids
- [ ] Lead event fires on form submission
- [ ] ViewContent fires on product/service pages
- [ ] AddToCart fires on cart addition (if e-commerce)
- [ ] InitiateCheckout fires at checkout start
- [ ] CompleteRegistration fires on sign-up

### Conversions API (CAPI)
- [ ] CAPI active and sending server events
- [ ] EMQ score 6.0+ for primary events
- [ ] client_ip_address included
- [ ] client_user_agent included
- [ ] fbc cookie forwarded
- [ ] fbp cookie forwarded
- [ ] Hashed email included
- [ ] Hashed phone included
- [ ] event_id sent for deduplication
- [ ] Same event_id used in both Pixel and CAPI

---

## LinkedIn Ads

### Insight Tag
- [ ] Insight Tag on all pages
- [ ] Correct Partner ID
- [ ] Tag loads asynchronously
- [ ] noscript fallback present

### Conversion Tracking
- [ ] At least one conversion action created
- [ ] Event-specific tracking preferred over URL-based
- [ ] Attribution window set (30-day click recommended for B2B)
- [ ] li_fat_id captured from URL (for CAPI)

---

## TikTok Ads

### TikTok Pixel
- [ ] Pixel on all pages
- [ ] Correct Pixel ID
- [ ] ttq.page() fires on every page
- [ ] No duplicate installations

### Events & Matching
- [ ] CompletePayment/SubmitForm event configured
- [ ] Value and currency included on monetary events
- [ ] ttq.identify() called with email/phone
- [ ] ttclid captured from URL (for Events API)

---

## Cross-Platform

### Attribution
- [ ] Attribution models documented per platform
- [ ] Data-driven used where eligible
- [ ] Conversion windows documented
- [ ] Cross-platform overlap ratio < 1.3

### Deduplication
- [ ] Pixel + CAPI deduplication (Meta)
- [ ] Client + server deduplication (Google sGTM)
- [ ] No duplicate conversion counting across platforms

### Consent
- [ ] Consent management platform in place (if required)
- [ ] Google Consent Mode v2 configured
- [ ] Tags fire appropriately based on consent state
- [ ] Modeled conversions enabled for consent-denied users
