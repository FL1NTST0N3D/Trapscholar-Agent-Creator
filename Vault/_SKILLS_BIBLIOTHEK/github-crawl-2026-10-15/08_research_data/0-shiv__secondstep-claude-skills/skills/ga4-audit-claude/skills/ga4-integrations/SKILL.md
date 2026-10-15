# GA4 Integrations Audit

## Command
`/ga4 integrations`

## Purpose
Audit the integration status between GA4 and other Google products. GA4 becomes exponentially more powerful when properly linked to Google Ads, Search Console, BigQuery, and other Google services. Missing integrations mean missing data, broken attribution, and underperforming campaigns. Most properties have at least one critical integration gap.

## Integration Ecosystem

GA4 can integrate with the following Google products:

| Integration | Location | Primary Benefit |
|------------|----------|----------------|
| Google Ads | Admin > Google Ads Links | Conversion import, audience sharing, campaign reporting |
| Search Console | Admin > Search Console Links | Organic search query data in GA4 |
| BigQuery | Admin > BigQuery Links | Raw event-level data export for SQL analysis |
| Firebase | Admin > Firebase Links | App analytics, A/B testing, Remote Config |
| Google Merchant Center | Admin > Merchant Center Links | Product data enrichment |
| DV360 | Admin > Display & Video 360 Links | Programmatic advertising data |
| SA360 | Admin > Search Ads 360 Links | Enterprise search campaign data |

## Audit Checklist

### 1. Google Ads Linking

The most critical integration for any property running Google Ads.

**Link status:**
- [ ] GA4 property is linked to all relevant Google Ads accounts
- [ ] Link is bidirectional (both GA4 and Google Ads show the connection)
- [ ] Multiple Ads accounts are linked if using MCC structure (link each sub-account)
- [ ] Auto-tagging is enabled in Google Ads (Settings > Account settings > Auto-tagging)
- [ ] Google Signals is enabled in GA4 (required for full cross-device Ads reporting)

**Data flowing correctly:**
- [ ] Google Ads campaign data appears in GA4 Acquisition reports
- [ ] GA4 conversions are importable in Google Ads
- [ ] Key conversions are imported and set as Primary in Google Ads
- [ ] GA4 audiences appear in Google Ads Audience Manager
- [ ] Cost data from Google Ads appears in GA4 (Acquisition > Google Ads campaigns)
- [ ] ROAS can be calculated in GA4 using Ads cost data

**Common Ads linking issues:**
- [ ] No "data mismatch" between GA4 and Google Ads conversion counts (>15% difference needs investigation)
- [ ] Click and session counts are reasonably aligned (GA4 sessions will always be lower than Ads clicks)
- [ ] GCLID parameter is not being stripped by redirects, CDNs, or server configurations
- [ ] UTM parameters and auto-tagging coexist properly (auto-tagging takes precedence in GA4)

### 2. Search Console Linking

Brings organic search performance data (queries, impressions, clicks, position) into GA4.

**Link status:**
- [ ] Search Console property is linked to GA4
- [ ] Correct Search Console property is linked (domain vs URL prefix — must match)
- [ ] User has appropriate permissions in both GA4 and Search Console

**Data flowing correctly:**
- [ ] Organic search queries appear in GA4 (Acquisition > Search Console reports)
- [ ] Search Console reports show:
  - [ ] Queries report (search terms driving traffic)
  - [ ] Google organic search traffic report (landing pages)
- [ ] Data is recent (Search Console data has 2-3 day delay)
- [ ] Landing page URLs in Search Console match GA4 page paths

**Verification:**
- [ ] Search Console queries can be combined with GA4 engagement metrics
- [ ] No "(not provided)" or "(not set)" in Search Console GA4 reports
- [ ] Multiple Search Console properties linked if managing multiple domains

### 3. BigQuery Export

Raw event-level data export enables unsampled analysis, custom ML models, and data warehousing.

**Link status:**
- [ ] BigQuery project is linked to GA4 property
- [ ] Correct GCP project is selected
- [ ] Billing is enabled on the GCP project (BigQuery export generates storage and query costs)
- [ ] Export type is configured:
  - [ ] Daily export — Batch export once per day (free for first 1M events/day)
  - [ ] Streaming export — Near real-time export (additional cost, GA4 360 feature)

**Data structure:**
- [ ] `events_YYYYMMDD` tables are being created daily
- [ ] `events_intraday_YYYYMMDD` tables exist (if streaming is enabled)
- [ ] Tables contain expected event data
- [ ] User properties are populated in export
- [ ] E-commerce item data is present in `items` RECORD field
- [ ] No export gaps (missing dates indicate failures)

**Usage and cost:**
- [ ] BigQuery costs are monitored (set up billing alerts)
- [ ] Data retention policy is configured in BigQuery (auto-delete old tables if needed)
- [ ] Queries are optimized to avoid scanning unnecessary data (use partitioned tables)
- [ ] At least one team member can write SQL queries against the export
- [ ] Scheduled queries exist for recurring analysis (if applicable)

### 4. Firebase Linking

Required for app analytics. Relevant only if the business has a mobile app.

- [ ] Firebase project is linked (if mobile app exists)
- [ ] App streams are correctly configured
- [ ] App and web data are flowing into the same GA4 property
- [ ] Cross-platform user identity is configured (User ID, Google Signals)
- [ ] App events match web events where applicable (consistent naming)
- [ ] Firebase A/B testing results are accessible in GA4
- [ ] Crashlytics data is available (if Firebase Crashlytics is used)
- [ ] Skip this section if no mobile app exists

### 5. Google Merchant Center Linking

Enriches e-commerce data with product feed information.

- [ ] Merchant Center is linked (if e-commerce with Google Shopping)
- [ ] Product data enrichment is enabled
- [ ] Product IDs in GA4 match Merchant Center product IDs
- [ ] Shopping campaign performance data appears in GA4
- [ ] Free listings performance is tracked
- [ ] Skip this section if not running Google Shopping

### 6. DV360 and SA360 Linking

Enterprise advertising platform integrations.

- [ ] DV360 is linked (if using programmatic display/video advertising)
- [ ] SA360 is linked (if using enterprise search ad management)
- [ ] Campaign data from these platforms appears in GA4 reports
- [ ] Conversions can be shared back to these platforms
- [ ] Floodlight activities are not duplicating GA4 conversions
- [ ] Skip this section if not using DV360/SA360

### 7. Google Tag Manager Integration

Not technically a GA4 "link" but critical infrastructure.

- [ ] GTM container is deployed on the site
- [ ] GA4 Configuration tag exists and fires on All Pages
- [ ] GA4 Event tags use the Configuration tag reference
- [ ] GTM container is the primary method of GA4 deployment (not hardcoded gtag.js alongside GTM)
- [ ] Server-side GTM is considered or implemented (for data quality, privacy)
- [ ] GTM workspace is not cluttered with unpublished changes
- [ ] GTM version history shows regular, documented publishes
- [ ] GTM access is limited to appropriate team members

### 8. Third-Party Integrations (Non-Google)

While not native GA4 integrations, these are commonly connected:

- [ ] CRM integration (Salesforce, HubSpot) — Offline conversion import
- [ ] Email platform (Mailchimp, Klaviyo) — UTM tracking on email links
- [ ] Heatmap tools (Hotjar, Microsoft Clarity) — Session recordings linked to GA4 data
- [ ] A/B testing tools (Optimizely, VWO) — Experiment data in GA4
- [ ] CDP (Segment, mParticle) — Data routing through CDP to GA4
- [ ] Consent management (Cookiebot, OneTrust) — Consent Mode integration

## Common Issues Found

1. **Google Ads not linked** — Property running Google Ads but GA4 is not linked, meaning no conversion import, no audience sharing, no Smart Bidding signals.
2. **Search Console wrong property** — URL prefix property linked instead of domain property (or vice versa), causing partial data.
3. **BigQuery export not enabled** — Missing out on unsampled, event-level data. Especially problematic for properties that need detailed analysis beyond GA4 UI capabilities.
4. **Auto-tagging disabled** — Google Ads clicks not properly attributed in GA4, campaign data missing from reports.
5. **GCLID stripped by redirects** — Server-side redirects or URL shorteners removing the GCLID parameter, breaking Ads attribution.
6. **Duplicate tracking** — GTM GA4 tag AND hardcoded gtag.js both firing, causing double-counted events.
7. **BigQuery costs unmonitored** — Streaming export enabled without billing alerts, resulting in unexpected charges.
8. **Firebase and web events mismatched** — App events named differently from web events, making cross-platform analysis impossible.

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Google Ads | 30 | 30% |
| Search Console | 15 | 15% |
| BigQuery | 20 | 20% |
| GTM | 15 | 15% |
| Firebase | 10 | 10% |
| Other integrations | 10 | 10% |

**Score = (passed_points / total_applicable_points) * 100**

Note: Firebase, Merchant Center, DV360, and SA360 checks are only scored if applicable to the business.

## Output Format

```
## Integrations Audit

**Score: XX/100**

### Integration Status
| Integration | Status | Data Flowing | Issues |
|------------|--------|-------------|--------|
| Google Ads | Linked/Not linked | Yes/No | [count] |
| Search Console | Linked/Not linked | Yes/No | [count] |
| BigQuery | Linked/Not linked | Yes/No | [count] |
| Firebase | Linked/N/A | Yes/No | [count] |
| Merchant Center | Linked/N/A | Yes/No | [count] |
| DV360 | Linked/N/A | Yes/No | [count] |
| SA360 | Linked/N/A | Yes/No | [count] |
| GTM | Deployed/Not deployed | Yes/No | [count] |

### Google Ads Details
- Account ID: XXX-XXX-XXXX
- Auto-tagging: Enabled/Disabled
- Imported conversions: [count]
- Shared audiences: [count]

### Findings
[Passed/Failed/Warning items with fix instructions]
```
