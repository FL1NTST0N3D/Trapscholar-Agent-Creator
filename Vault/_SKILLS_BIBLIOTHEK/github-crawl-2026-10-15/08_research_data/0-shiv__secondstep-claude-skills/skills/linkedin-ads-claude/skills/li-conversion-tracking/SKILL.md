# Conversion Tracking Sub-Skill

## Purpose

Audit and optimize LinkedIn conversion tracking infrastructure. Verify Insight Tag installation, evaluate conversion event configuration, review LinkedIn Conversions API (CAPI) setup, and assess attribution window settings.

## LinkedIn Insight Tag

### What It Does
The Insight Tag is a lightweight JavaScript snippet that enables conversion tracking, website retargeting, and website demographics reporting. It is the foundation of all LinkedIn measurement.

### Installation Methods

| Method | Complexity | Best For |
|--------|-----------|----------|
| Direct JavaScript | Low | Simple websites |
| Google Tag Manager | Medium | Most common, recommended |
| Tag management platform | Medium | Enterprise (Tealium, Segment) |
| LinkedIn Partner Integration | Low | HubSpot, WordPress plugins |

### Verification Checklist

1. **Tag Presence** -- Insight Tag must fire on every page of your website
2. **Tag ID Match** -- Verify the partner/account ID matches your LinkedIn ad account
3. **Fire Timing** -- Tag should fire on page load, not deferred/lazy-loaded
4. **Cross-Domain** -- If your site spans multiple domains, tag must be on all
5. **SPA Compatibility** -- Single Page Apps need event-based firing (not just page load)
6. **Cookie Consent** -- Tag must respect GDPR/CCPA consent; deferred firing if no consent

### Testing the Insight Tag
- Use LinkedIn Insight Tag Helper Chrome extension
- Check Tag Assistant (Google) for GTM-based installations
- Verify in Campaign Manager: Account Assets > Insight Tag > "Tracking" status should be "Active"
- Check Website Demographics report -- if data appears, tag is working

## Conversion Events

### Event Types

| Type | How It Works | Best For |
|------|-------------|----------|
| URL-based | Fires when user visits a specific URL | Thank-you pages, confirmation pages |
| Event-specific | Fires on custom JavaScript events | Button clicks, form submissions, video plays |
| LinkedIn-native | Tracked automatically by LinkedIn | Lead Gen Form submissions, video views |

### Recommended Conversion Events

| Event Name | Type | Funnel Stage | Attribution |
|------------|------|-------------|------------|
| Page View | URL | All | Engagement |
| Content Download | Event-specific | MOFU | Lead |
| Pricing Page View | URL | BOFU | Intent signal |
| Demo Request | Event-specific or URL | BOFU | Lead (high value) |
| Contact Form Submit | Event-specific | BOFU | Lead |
| Purchase/Sign-up | URL or Event | BOFU | Revenue |
| Lead Gen Form Submit | LinkedIn-native | All | Lead |
| Free Trial Start | Event-specific or URL | BOFU | Lead (high value) |

### Conversion Event Setup Best Practices

1. **Name conversions clearly**: Use a naming convention like `[Stage]_[Action]_[Source]`
   - Example: `BOFU_DemoRequest_Website`, `MOFU_WhitepaperDownload_LGF`

2. **Assign conversion values**: Even estimated values help LinkedIn optimize
   - Demo Request: $500 (estimated pipeline value * win rate)
   - Content Download: $50 (estimated downstream value)
   - Free Trial: $200 (estimated conversion value)

3. **Set counting method**:
   - **Every conversion**: For purchases (count each transaction)
   - **One conversion per member**: For leads (deduplicate form submissions)

4. **Configure attribution window** appropriately (see section below)

## LinkedIn Conversions API (CAPI)

### What Is CAPI?
LinkedIn CAPI is a server-side tracking solution that sends conversion data directly from your server to LinkedIn, bypassing browser-based tracking limitations (ad blockers, cookie restrictions, iOS privacy changes).

### Why CAPI Matters
- Browser-based tracking captures only 60-70% of conversions (due to ad blockers, cookie consent)
- CAPI recovers 20-30% of lost conversions
- Combined Insight Tag + CAPI provides the most accurate measurement
- Required for accurate Offline Conversions tracking

### CAPI Implementation

| Method | Complexity | Best For |
|--------|-----------|----------|
| Direct API Integration | High | Engineering teams, custom CRM |
| HubSpot Native | Low | HubSpot CRM users |
| Salesforce Integration | Medium | Salesforce CRM users |
| Zapier/Make | Medium | No-code teams |
| Partner integrations | Varies | LeadsBridge, Fivetran, etc. |

### CAPI Data Requirements

**Required Fields:**
| Field | Description |
|-------|-------------|
| Conversion Rule ID | LinkedIn conversion event ID |
| Conversion Timestamp | When the conversion occurred |
| User Identifier | Email (SHA256 hashed) or LinkedIn First Party Ad Tracking UUID |

**Recommended Fields:**
| Field | Description |
|-------|-------------|
| Conversion Value | Revenue or estimated value |
| Currency Code | USD, EUR, etc. |
| Event ID | Deduplication key (must match browser event) |

### CAPI + Insight Tag Deduplication
When running both CAPI and Insight Tag, use the same `event_id` for both to prevent double-counting. LinkedIn deduplicates based on:
- Same conversion rule ID
- Same user identifier
- Same event ID
- Within the same attribution window

## Attribution Windows

### Available Attribution Windows

| Window Type | Options | Default |
|------------|---------|---------|
| Click-through | 1, 7, 30, 90 days | 30 days |
| View-through | 1, 7, 30, 90 days | 7 days |

### Attribution Window Recommendations

| Campaign Type | Click Window | View Window | Rationale |
|--------------|-------------|-------------|-----------|
| TOFU Awareness | 90 days | 30 days | Long consideration cycles |
| MOFU Content | 30 days | 7 days | Balanced measurement |
| BOFU Lead Gen | 30 days | 7 days | Standard B2B window |
| ABM Campaigns | 90 days | 30 days | Enterprise sales cycles are long |
| Retargeting | 7 days | 1 day | Closer to conversion, shorter window |

### Attribution Models
LinkedIn currently supports:
- **Last Touch - Last Campaign**: Credit goes to the last LinkedIn campaign that was clicked/viewed before conversion
- **Each Campaign**: Credit distributed across all LinkedIn campaigns that contributed (available in Campaign Manager reporting)

**Important:** LinkedIn attribution is LinkedIn-only. It does not account for other channels. Always cross-reference with your CRM and multi-touch attribution tool for true channel mix analysis.

## Offline Conversions

### What They Are
Offline conversions let you upload CRM data (closed deals, qualified leads, revenue) back to LinkedIn to measure downstream impact of ads.

### Upload Methods
- CSV upload in Campaign Manager
- CAPI (server-side, automated)
- CRM integration (HubSpot, Salesforce)

### Recommended Offline Events
| Event | When to Upload | Value |
|-------|---------------|-------|
| MQL | When lead qualifies | Estimated MQL value |
| SQL | When sales accepts | Estimated SQL value |
| Opportunity Created | CRM opportunity stage | Pipeline value |
| Closed Won | Deal closes | Revenue |
| Closed Lost | Deal lost | $0 (still valuable for optimization) |

## Audit Checklist

1. **Insight Tag Installation** (3 pts)
   - Is the Insight Tag active and firing on all website pages?
   - Does the tag ID match the correct LinkedIn ad account?
   - Is the tag compatible with SPA architecture (if applicable)?

2. **Conversion Event Setup** (3 pts)
   - Are conversion events configured for each funnel stage (TOFU/MOFU/BOFU)?
   - Are conversion values assigned (even estimated)?
   - Is the counting method appropriate (one per member for leads, every for revenue)?

3. **CAPI Implementation** (2 pts)
   - Is LinkedIn CAPI set up alongside the Insight Tag?
   - Is deduplication configured (same event_id for browser and server events)?

4. **Attribution Configuration** (2 pts)
   - Are attribution windows set appropriately per campaign type?
   - Is offline conversion data being uploaded from CRM?

## Scoring

| Score | Rating | Meaning |
|-------|--------|---------|
| 9-10 | Elite | Full Insight Tag + CAPI + offline conversions + proper attribution |
| 7-8 | Strong | Good tracking with Insight Tag, minor CAPI or attribution gaps |
| 5-6 | Average | Insight Tag active but limited conversion events |
| 3-4 | Weak | Insight Tag present but misconfigured or partial |
| 0-2 | Critical | No Insight Tag or broken tracking |

## Common Conversion Tracking Mistakes

1. **Insight Tag not on all pages** -- retargeting and demographics only work where the tag fires
2. **No conversion events** -- running campaigns with no success metrics defined
3. **No conversion values** -- LinkedIn cannot optimize for value without revenue signals
4. **Missing CAPI** -- losing 20-30% of conversion visibility to ad blockers
5. **Wrong attribution window** -- 1-day click for enterprise B2B misses the 30-60 day sales cycle
6. **No offline conversions** -- LinkedIn optimization stops at form submit; CRM feedback closes the loop
7. **Double-counting** -- CAPI and Insight Tag both firing without deduplication event_id
8. **Not testing the tag** -- assuming the tag works without verifying via LinkedIn Tag Helper
