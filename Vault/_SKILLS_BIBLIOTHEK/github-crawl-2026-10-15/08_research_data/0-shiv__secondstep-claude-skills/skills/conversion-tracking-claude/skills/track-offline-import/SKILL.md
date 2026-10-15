# Track Offline Import — Sub-Skill

## Command
`/track offline`

## Description
Validates Google Ads offline conversion import pipeline — from GCLID/WBRAID/GBRAID capture on the landing page, through CRM storage and lead qualification, to conversion upload via CSV or API. Offline conversion import is critical for lead generation businesses where the actual conversion (sale, appointment, deal) happens outside the website. Without it, Google Ads optimizes for form fills instead of revenue.

---

## How Offline Conversion Import Works

### The Pipeline

```
1. User clicks Google Ad
   └── GCLID appended to URL: ?gclid=EAIaIQobChMI...

2. User lands on website
   └── JavaScript captures GCLID from URL
   └── GCLID stored in hidden form field + cookie

3. User submits lead form
   └── GCLID submitted with form data
   └── CRM receives lead + GCLID

4. Lead progresses through sales pipeline
   └── CRM tracks: New → Qualified → Proposal → Won/Lost

5. When lead converts (or reaches key stage):
   └── Export: GCLID + conversion action + datetime + value
   └── Upload to Google Ads via CSV or API

6. Google Ads receives offline conversion
   └── Links conversion back to the original click
   └── Smart Bidding learns which clicks lead to revenue
```

---

## Validation Checklist

### 1. GCLID Capture

**URL Parameter Extraction:**
- GCLID is in the URL as `?gclid=XXXX` or `&gclid=XXXX`
- Also check for `wbraid` (iOS web-to-app) and `gbraid` (iOS app-to-app)
- Must be captured on the first page load — cannot be retrieved later

**Storage Methods:**
- **Hidden form field** — Most reliable. Add `<input type="hidden" name="gclid" id="gclid">` to every lead form
- **Cookie** — For multi-page journeys. Set with 90-day expiry: `document.cookie = "gclid=" + gclid + ";max-age=7776000;path=/"`
- **localStorage** — Alternative to cookie, not affected by ITP but cleared if user clears browser data
- **UTM + GCLID combo** — Store both for full attribution context

**Common Capture Failures:**
- Landing page redirects strip query parameters (301/302 without parameter forwarding)
- CMS (WordPress, Webflow) drops URL parameters on form submission
- Form builder (Typeform, JotForm) doesn't include hidden fields
- SPA router clears URL on client-side navigation
- GCLID cookie expired before user returned to submit form
- Cross-domain journeys lose GCLID (e.g., landing page on domain A, form on domain B)

### 2. CRM Integration

**What to verify:**
- CRM has a dedicated field for GCLID (not stuffed into notes or comments)
- GCLID field is populated for paid leads (check a sample of recent leads)
- GCLID retention rate: `leads_with_gclid / total_paid_leads` — target 80%+
- CRM workflow doesn't overwrite or clear GCLID on lead update

**CRM-Specific Checks:**
- **Salesforce** — Custom field `GCLID__c` on Lead/Contact, mapped in web-to-lead form
- **HubSpot** — Custom property `gclid`, captured via hidden form field
- **Zoho CRM** — Custom field on Leads module
- **Pipedrive** — Custom field on Deals or Contacts
- **Google Sheets** — Column for GCLID in lead tracker

### 3. Conversion Upload Schedule

**Timing matters:**
- Google Ads conversion window default: 90 days from click
- Conversions uploaded after the window are ignored
- Recommended upload frequency: **daily** for active campaigns
- Minimum: weekly (but daily gives Smart Bidding faster signals)
- Conversion time must be the actual offline event time, not upload time

**Upload Methods:**

**CSV Upload (Manual):**
```csv
Parameters:TimeZone=America/New_York
Google Click ID,Conversion Name,Conversion Time,Conversion Value,Conversion Currency
EAIaIQobChMI...,Qualified Lead,2026-03-10 14:30:00,500,USD
```

**Google Ads API (Automated):**
- Use `UploadConversionAdjustments` for ongoing imports
- Requires API credentials (OAuth, developer token)
- Can be integrated with CRM via middleware (Zapier, Make, custom)
- Supports bulk uploads

**Salesforce Integration:**
- Google Ads Salesforce connector (native)
- Maps Salesforce opportunity stages to Google Ads conversion actions
- Automatic, near real-time upload

### 4. Conversion Value Assignment

**Static Values:**
- Assign a fixed dollar value per conversion stage
- Example: Qualified Lead = $50, Proposal = $200, Closed Won = $2,000
- Simple but doesn't reflect actual deal size variation

**Dynamic Values:**
- Pass actual deal value from CRM
- Revenue or contract value from closed deals
- Enables Value-Based Bidding (VBB) — Google optimizes for revenue, not just volume
- Much more powerful for Smart Bidding but requires clean CRM data

**Value Strategy:**
- Import multiple conversion actions at different pipeline stages
- Primary conversion action: Closed Won (or Qualified Lead if sales cycle is long)
- Secondary: intermediate stages for optimization signals
- Never import at $0 value — kills VBB capability

### 5. Import Error Troubleshooting

**Common Upload Errors:**
| Error | Cause | Fix |
|-------|-------|-----|
| Invalid GCLID | GCLID malformed or expired | Check capture code, ensure no truncation |
| Conversion action not found | Wrong conversion action name | Match exact name from Google Ads |
| Duplicate conversion | Same GCLID + action + time uploaded twice | Deduplicate before upload |
| Conversion time outside window | Event happened > 90 days after click | Upload more frequently |
| Invalid time format | Wrong datetime format | Use `yyyy-MM-dd HH:mm:ss` |
| Currency mismatch | Currency code doesn't match account | Use account's currency code |

**Debugging Steps:**
1. Check Google Ads > Tools > Conversions > Uploads > view upload history
2. Look at error details for each failed upload
3. Download the error file and cross-reference with your CRM data
4. Test with a single known-good GCLID before bulk upload

---

## Scoring Contribution

This sub-skill contributes up to **10 points** to the Tracking Health Score:

- GCLID capture working on all forms: 3 points
- CRM storing GCLID correctly: 2 points
- Regular upload schedule (daily/weekly): 2 points
- Conversion values assigned and meaningful: 2 points
- No upload errors in last 30 days: 1 point

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| GCLID not captured at all | Critical | Zero offline conversions imported |
| CRM not storing GCLID | Critical | Pipeline data disconnected from ads |
| No upload process exists | Critical | Google Ads blind to lead quality |
| Upload errors > 20% | High | Significant data loss |
| No conversion values | High | VBB impossible, Smart Bidding degraded |
| Upload frequency > weekly | Medium | Delayed optimization signals |
| Only one pipeline stage imported | Low | Less granular optimization |
