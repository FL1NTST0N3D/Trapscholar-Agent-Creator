# Track Enhanced Conversions — Sub-Skill

## Command
`/track ec`

## Description
Audits Enhanced Conversions for Web and Enhanced Conversions for Leads (EC4L). Enhanced Conversions recover conversion data lost to cookie restrictions, ad blockers, and cross-device journeys by sending hashed first-party user data alongside conversion tags. Google reports EC can recover 5-15% of otherwise lost conversions. With browser privacy tightening, EC is no longer optional — it is essential infrastructure.

---

## Enhanced Conversions for Web (EC Web)

### What It Does
When a user converts on your website (purchase, form submit), EC Web captures user-provided data (email, phone, name, address) from the conversion page, hashes it with SHA-256, and sends it to Google alongside the conversion tag. Google matches this hashed data against signed-in Google users to attribute the conversion even when cookies are unavailable.

### Setup Methods

**Method 1: gtag API (Recommended for direct implementations)**
```javascript
gtag('set', 'user_data', {
  "email": user_email,         // or sha256_email_address
  "phone_number": user_phone,  // E.164 format
  "first_name": user_first,
  "last_name": user_last,
  "home_address": {
    "street": user_street,
    "city": user_city,
    "region": user_state,
    "postal_code": user_zip,
    "country": user_country    // ISO 3166-1 alpha-2
  }
});
```

**Method 2: Google Tag Manager**
- Use the "User-Provided Data" variable type in GTM
- Map form fields or data layer variables to each user data field
- Attach to the conversion tag as a "User-Provided Data" setting
- GTM handles hashing automatically

**Method 3: CSS Selector / Auto-Detection**
- Google Ads UI > Enhanced Conversions settings
- Specify CSS selectors for form fields containing user data
- Least reliable method — breaks when form markup changes
- Not recommended for production

### Validation Checklist

1. **EC enabled in Google Ads**
   - Google Ads > Goals > Conversions > Settings > Enhanced conversions for web: ON
   - Terms of service accepted

2. **User data being sent**
   - Check network requests for `user_data` parameter in conversion ping
   - At least email OR phone must be present (email preferred)
   - More fields = higher match rate (email + phone + name = best)

3. **Data hashing correct**
   - Data must be lowercase and trimmed before hashing
   - Email: `john.doe@example.com` (not `John.Doe@Example.com`)
   - Phone: E.164 format `+12125551234` (not `(212) 555-1234`)
   - SHA-256 hash, not MD5 or plain text
   - If using gtag API or GTM, hashing is automatic (send plain text)

4. **Diagnostic status in Google Ads**
   - Navigate to: Conversions > select action > Diagnostics tab
   - Statuses: "Tag found and active", "Recording enhanced conversions"
   - Check match rate percentage (target: 60%+ for healthy EC)
   - Check for warnings: "No enhanced conversion data received"

5. **Testing**
   - Submit a test conversion with a known Google account email
   - Check that the conversion appears with "Enhanced" indicator in reports
   - Use Google Tag Assistant to verify user_data is included in the tag

---

## Enhanced Conversions for Leads (EC4L)

### What It Does
EC4L is for lead generation businesses where the conversion happens offline (phone call, in-person meeting, closed deal). It works by:

1. Capturing the GCLID when a user clicks a Google Ad and lands on your site
2. Storing the GCLID with the lead in your CRM
3. When the lead converts offline, uploading the conversion back to Google Ads with:
   - The original GCLID, OR
   - Hashed user data (email, phone) if GCLID was lost

### GCLID Capture

**How GCLID works:**
- Google appends `?gclid=XXXX` to the landing page URL on ad click
- Also `wbraid` (iOS web-to-app) and `gbraid` (iOS app-to-app)
- Must be captured on landing page and stored through the conversion funnel

**Capture methods:**
```javascript
// Extract GCLID from URL
function getGclid() {
  const params = new URLSearchParams(window.location.search);
  return params.get('gclid') || params.get('wbraid') || params.get('gbraid');
}

// Store in hidden form field
document.getElementById('gclid_field').value = getGclid();

// Store in cookie for multi-page journeys
document.cookie = `gclid=${getGclid()}; max-age=7776000; path=/`;
```

**Common GCLID Loss Points:**
- URL parameters stripped by redirects (301/302)
- CMS or form builder dropping query parameters
- SPA router clearing URL on navigation
- Cookie expiring before form submission
- Hidden field not included in form submission
- CRM not storing the GCLID field

### Offline Conversion Import with EC4L

**With GCLID:**
- Upload CSV or use API with: GCLID, conversion action, conversion time, value
- Most reliable method — direct click-to-conversion mapping

**With Hashed User Data (GCLID-less):**
- Upload: hashed email + hashed phone + conversion action + time + value
- Google matches against its user database
- Lower match rate than GCLID but works when GCLID is lost
- Requires EC4L to be enabled in Google Ads

### EC4L Validation Checklist

1. **EC4L enabled in Google Ads**
   - Goals > Conversions > Settings > Enhanced conversions for leads: ON

2. **GCLID capture working**
   - Click a Google Ad and verify GCLID in URL
   - Submit the form and verify GCLID stored in CRM
   - Check GCLID in hidden form field value
   - Test with wbraid/gbraid (simulate from iOS)

3. **Lead pipeline tracking**
   - CRM records have GCLID field populated
   - GCLID retention rate: % of leads with GCLID vs total leads
   - Target: 80%+ of paid leads should have GCLID

4. **Offline conversion import**
   - Import schedule: daily or weekly
   - Conversion action mapped correctly
   - Upload errors: check Google Ads import history
   - Conversion lag: import within the conversion window (default 90 days)

5. **User data hashing for GCLID-less imports**
   - Email and/or phone captured on lead form
   - Data normalized and hashed correctly
   - Included in offline import file

---

## Scoring Contribution

This sub-skill contributes up to **15 points** to the Tracking Health Score:

- EC for Web enabled and sending data: 5 points
- EC diagnostic status healthy (match rate 60%+): 3 points
- EC4L / GCLID capture working: 4 points
- Offline import pipeline active: 3 points

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| EC not enabled at all | Critical | 5-15% conversion data lost |
| GCLID not captured | Critical | Offline conversions unattributable |
| User data not hashed correctly | High | EC data rejected by Google |
| EC enabled but 0% match rate | High | Configuration error |
| Only email captured (no phone/name) | Medium | Lower match rate |
| CSS selector method used | Medium | Fragile, breaks on markup changes |
| GCLID lost in redirects | High | Offline import pipeline broken |
| Import schedule too infrequent | Medium | Delayed optimization signals |
