# Track Server-Side — Sub-Skill

## Command
`/track server-side`

## Description
Validates server-side Google Tag Manager (sGTM) setup, including container configuration, first-party cookie management, proxy mode, and tag templates. Server-side tracking is the most robust tracking method available — it moves tag execution from the user's browser to a server you control, eliminating ad blocker interference, reducing client-side JavaScript load, and enabling first-party cookie control that survives ITP/ETP restrictions.

---

## Why Server-Side Tracking Matters

### The Problem with Client-Side Only
- **Ad blockers** block 25-40% of tracking tags in some verticals
- **ITP (Safari)** caps first-party cookies at 7 days, third-party cookies blocked entirely
- **ETP (Firefox)** blocks known trackers by default
- **Chrome Privacy Sandbox** phasing out third-party cookies
- **Heavy client-side tags** slow page load by 1-3 seconds, hurting Core Web Vitals
- **Consent management** complicates client-side tag firing timing

### What sGTM Solves
- Tags fire on your server, invisible to ad blockers
- First-party cookies set by your domain (not googletagmanager.com) — survive ITP
- Reduced client-side JavaScript (one tag sends data to your server, server fans out to platforms)
- Better data control — enrich, filter, or redact data before sending to platforms
- Consent enforcement at the server level

---

## Setup Validation

### 1. Server Container Deployment

**Stape.io (Managed)**
- Verify Stape dashboard shows container running
- Check container URL: `sgtm.yourdomain.com` or similar subdomain
- Confirm DNS CNAME record points to Stape's servers
- Check container version matches latest published version
- Monitor: requests/day, error rate, latency

**Google Cloud Platform (Self-Hosted)**
- App Engine or Cloud Run deployment active
- Container URL configured with custom domain
- SSL certificate valid and not expired
- Auto-scaling configured (min 1 instance to avoid cold starts)
- Cloud Logging enabled for debugging
- Estimated cost: $30-100/mo depending on traffic volume

**Validation Steps:**
1. Visit container URL — should return GTM server container response
2. Check DNS resolution for subdomain
3. Test with Tag Assistant connected to server container
4. Verify HTTPS is working (no mixed content)

### 2. Server Container Configuration

**Transport URL:**
- Client-side GTM must be configured to send data to the server container
- `gtag('config', 'AW-XXXXX', { 'server_container_url': 'https://sgtm.yourdomain.com' });`
- Or in GTM: Google Tag > Configuration > Server Container URL

**Tag Templates:**
- Google Ads Conversion Tracking tag (server-side version)
- Google Analytics 4 tag (server-side version)
- Meta Conversions API tag (if applicable)
- Verify each tag has correct credentials (API keys, access tokens)

**Triggers:**
- Server-side triggers based on incoming event data
- Common: All Events, specific event names (purchase, lead, etc.)
- Verify triggers match the events sent from client-side

### 3. First-Party Cookies

**Why This Matters:**
When sGTM runs on your subdomain (e.g., `sgtm.yourdomain.com`), cookies set by the server container are first-party cookies from `yourdomain.com`. These survive ITP's 7-day cap because they are set via HTTP response headers (server-side), not JavaScript (client-side).

**Cookie Validation:**
- Check that `_ga`, `_gcl_aw`, and `_fbc` cookies are set by the server container
- Cookie domain should be `.yourdomain.com` (note the leading dot for subdomain access)
- Cookie expiry should be 2 years for analytics, 90 days for ad click IDs
- Verify cookies are `HttpOnly` and `Secure` flags set appropriately
- Test in Safari: cookies should persist beyond 7 days

### 4. Proxy Mode

**What It Does:**
Proxy mode routes all Google Tag requests through your server container. Instead of the browser loading `googletagmanager.com/gtag/js`, it loads from `sgtm.yourdomain.com/gtag/js`. This makes tracking completely first-party and invisible to ad blockers.

**Validation:**
- Client-side Google Tag loads from server container URL, not googletagmanager.com
- Network requests show your subdomain, not google domains
- Test with an ad blocker enabled — tags should still fire
- Verify no performance degradation (latency should be < 200ms added)

### 5. Data Flow Verification

```
Client Browser
    |
    | (single request to your subdomain)
    v
Server Container (sgtm.yourdomain.com)
    |
    |--- Google Ads (conversion + EC data)
    |--- GA4 (analytics events)
    |--- Meta CAPI (if configured)
    |--- LinkedIn CAPI (if configured)
    |
    v
Ad Platforms receive server-side events
```

**Test the full flow:**
1. Perform a conversion on the website
2. Check server container logs for incoming event
3. Verify outgoing requests to each platform
4. Confirm conversion appears in each platform's reporting
5. Check for error responses from platforms (401, 400, etc.)

---

## Common Issues

| Issue | Symptom | Fix |
|-------|---------|-----|
| DNS not configured | Container URL returns error | Add CNAME record for subdomain |
| SSL certificate expired | HTTPS errors in browser | Renew certificate, check auto-renewal |
| Transport URL not set | Client still sending to google directly | Add server_container_url to gtag config |
| Cold starts | First request after idle has 5-10s delay | Set minimum instances to 1 |
| Tag template errors | Events received but not forwarded | Check tag template configuration and credentials |
| Cookie domain wrong | Cookies not persisting | Set cookie domain to `.yourdomain.com` |
| CORS issues | Cross-origin errors in console | Configure CORS headers on server container |

---

## Scoring Contribution

This sub-skill contributes up to **15 points** to the Tracking Health Score:

- Server container deployed and running: 5 points
- First-party cookies correctly configured: 3 points
- All platform tags forwarding correctly: 4 points
- Proxy mode active (ad blocker resistant): 3 points

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| No sGTM at all | High | Missing 25-40% of Safari/Firefox conversions |
| Container down / erroring | Critical | All server-side tracking broken |
| First-party cookies not set | High | ITP still capping cookies at 7 days |
| Missing tag templates | High | Data not forwarded to platforms |
| Proxy mode not enabled | Medium | Ad blockers still blocking tags |
| Cold start latency | Low | Occasional slow first request |
