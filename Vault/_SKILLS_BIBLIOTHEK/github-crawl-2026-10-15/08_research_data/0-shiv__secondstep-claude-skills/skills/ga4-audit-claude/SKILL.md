# GA4 Audit — Main Skill

## Command Routing

This is the master skill file for the GA4 Audit Claude Code skill. It routes `/ga4` commands to the appropriate sub-skill.

### Available Commands

| Command | Sub-skill | Description |
|---------|-----------|-------------|
| `/ga4 audit` | All sub-skills | Full property audit across all dimensions |
| `/ga4 streams` | `ga4-data-streams` | Audit data stream configuration |
| `/ga4 events` | `ga4-events` | Audit event implementation |
| `/ga4 conversions` | `ga4-conversions` | Audit conversion setup |
| `/ga4 audiences` | `ga4-audiences` | Audit audience configuration |
| `/ga4 attribution` | `ga4-attribution` | Audit attribution settings |
| `/ga4 ecommerce` | `ga4-ecommerce` | Audit e-commerce tracking |
| `/ga4 dimensions` | `ga4-custom-dimensions` | Audit custom dimensions |
| `/ga4 reporting` | `ga4-reporting` | Audit reports and explorations |
| `/ga4 integrations` | `ga4-integrations` | Audit Google product links |
| `/ga4 report` | `ga4-report` | Generate final audit report |

## GA4 Fundamentals

Before running any audit, understand the core GA4 data model.

### Event-Based Model

GA4 uses an event-based data model, replacing the session/pageview model from Universal Analytics. Everything is an event.

**Four event categories:**
1. **Automatically collected events** — `first_visit`, `session_start`, `page_view` (web), `screen_view` (app), `user_engagement`
2. **Enhanced measurement events** — `scroll`, `click` (outbound), `view_search_results`, `video_start`, `video_progress`, `video_complete`, `file_download`
3. **Recommended events** — Google-defined names with expected parameters (e.g., `purchase`, `sign_up`, `generate_lead`)
4. **Custom events** — User-defined events for business-specific actions

### Sessions

A session begins with `session_start` and ends after 30 minutes of inactivity (configurable). Unlike UA, sessions do NOT restart at midnight or on new campaign parameters by default.

**Key session metrics:**
- `session_start` — Fires once per session
- `engagement_time_msec` — Accumulated active time
- `engaged_sessions` — Sessions lasting >10 seconds, with a conversion, or with 2+ page/screen views
- `engagement_rate` — `engaged_sessions / sessions`

### Users

GA4 tracks three user identity spaces:
1. **User ID** — Your authenticated user identifier (most accurate)
2. **Google Signals** — Cross-device tracking for signed-in Google users
3. **Device ID** — Client ID from `_ga` cookie (least accurate)

**Reporting identity hierarchy** (configurable):
- Blended: User ID > Google Signals > Device ID > Modeling
- Observed: User ID > Google Signals > Device ID
- Device-based: Device ID only

### Engagement

GA4 replaces bounce rate with engagement metrics:
- **Engaged session**: >10 seconds OR conversion event OR 2+ page views
- **Engagement rate**: Percentage of engaged sessions (replaces inverse bounce rate)
- **Average engagement time**: Mean active time per session

### Recommended Events Reference

**All business types:**
- `login`, `sign_up`, `share`, `search`, `select_content`

**E-commerce:**
- `view_item_list`, `select_item`, `view_item`, `add_to_wishlist`
- `add_to_cart`, `remove_from_cart`, `view_cart`
- `begin_checkout`, `add_shipping_info`, `add_payment_info`
- `purchase`, `refund`
- `view_promotion`, `select_promotion`

**Lead generation:**
- `generate_lead`, `form_submit`, `qualify_lead`

**SaaS / Apps:**
- `sign_up`, `tutorial_begin`, `tutorial_complete`
- `spend_virtual_currency`, `earn_virtual_currency`
- `level_start`, `level_end`, `level_up`
- `unlock_achievement`, `post_score`

**Content / Media:**
- `page_view`, `scroll`, `video_start`, `video_progress`, `video_complete`
- `file_download`, `click`

**Travel:**
- `search`, `view_item`, `begin_checkout`, `purchase`

### Event Naming Rules

- Snake_case only (e.g., `add_to_cart`, NOT `AddToCart`)
- Maximum 40 characters
- Must start with a letter
- No reserved prefixes (`firebase_`, `ga_`, `google_`, `gtag.`)
- Maximum 500 distinct event names per property
- Maximum 25 custom parameters per event
- Parameter names: max 40 characters
- Parameter values: max 100 characters

## Orchestration

### Full Audit Flow (`/ga4 audit`)

When running a full audit, execute sub-skills in this order:

1. **Data Streams** — Foundation check (stream config, filters, retention)
2. **Events** — Event coverage and quality
3. **Conversions** — Conversion event setup
4. **E-commerce** — E-commerce funnel (if applicable)
5. **Custom Dimensions** — Dimension registration
6. **Audiences** — Audience configuration
7. **Attribution** — Attribution model settings
8. **Reporting** — Report and exploration setup
9. **Integrations** — Google product linking
10. **Report** — Compile findings into scored report

### Audit Input Requirements

For each audit, you need:
- GA4 Property ID (format: `properties/XXXXXXXX`)
- Business type (e-commerce, lead gen, SaaS, content, travel)
- Website URL
- GTM container ID (optional but recommended)
- Google Ads account ID (if running paid traffic)

### Health Score Calculation

```
Health Score = (
    streams_score * 0.10 +
    events_score * 0.20 +
    conversions_score * 0.15 +
    audiences_score * 0.10 +
    attribution_score * 0.10 +
    ecommerce_score * 0.15 +
    dimensions_score * 0.10 +
    integrations_score * 0.10
) * 100
```

Each dimension score is 0.0 to 1.0 based on checklist completion percentage.

### Output Format

All audit findings follow this structure:

```
## [Dimension Name] Audit

**Score: XX/100**

### Passed Checks
- [x] Check description

### Failed Checks
- [ ] Check description
  - **Impact**: High/Medium/Low
  - **Current**: What is currently configured
  - **Recommended**: What should be configured
  - **Fix**: Step-by-step instructions

### Warnings
- [!] Warning description
```
