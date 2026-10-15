# Track Google Tag — Sub-Skill

## Command
`/track google-tag`

## Description
Validates Google Tag (gtag.js) installation across all pages, checks conversion action configuration, verifies tag firing order, and confirms data flow into Google Ads. This is the foundation of all Google Ads tracking — if the Google Tag is broken, everything downstream (Enhanced Conversions, offline imports, audiences) fails.

---

## Validation Checklist

### 1. Tag Presence

Check that the Google Tag is present and loading correctly on every page type:

**Pages to Check:**
- Homepage
- Category / listing pages
- Product / service detail pages
- Cart / checkout pages
- Thank you / confirmation pages
- Blog / content pages
- Landing pages (especially ad-specific LPs)
- 404 / error pages

**What to Look For:**
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-XXXXXXXXXX');
</script>
```

**Common Issues:**
- Tag only on homepage, missing from inner pages
- Tag placed in `<body>` instead of `<head>` (causes delayed firing)
- SPA (React, Vue, Angular) not re-firing gtag on route changes
- Multiple Google Tags with different IDs conflicting
- Tag blocked by ad blockers or consent management platform
- Tag loaded synchronously (missing `async` attribute) causing page speed issues

### 2. GTM Implementation Check

If using Google Tag Manager instead of direct gtag.js:

- GTM container snippet in `<head>` (JS) and `<body>` (noscript)
- GTM container ID matches the intended account
- Google Ads conversion tag configured within GTM
- Trigger set correctly (All Pages for config, specific triggers for conversions)
- No duplicate: both direct gtag.js AND GTM firing the same tag

### 3. Conversion Action Configuration

For each conversion action in Google Ads, validate:

**Counting Method:**
- **One** — Use for lead forms, sign-ups, quote requests (one conversion per click)
- **Every** — Use for purchases, transactions (every conversion counts)
- Common mistake: Purchase set to "One" (undercounts) or Lead set to "Every" (overcounts)

**Conversion Value:**
- Static value assigned (e.g., $50 per lead)
- Dynamic value passed from transaction (e.g., actual purchase amount)
- Currency code specified correctly
- Value not $0 or blank (kills Value-Based Bidding)

**Conversion Category:**
- Purchase/Sale, Lead, Page View, Sign-up, Other
- Correct category matters for Smart Bidding optimization signals

**Conversion Window:**
- Click-through: 30, 60, or 90 days (default 30)
- View-through: 1 day (default) — usually appropriate
- Engaged-view: 3 days for video campaigns
- Window too short = lost conversions, window too long = misattribution
- Recommendation: 30 days for e-commerce, 60-90 days for B2B / high-consideration

**Attribution Model:**
- Data-driven (recommended, default for new actions)
- Last click (legacy, still common)
- Check that all conversion actions use the same model for consistency

### 4. Tag Firing Verification

Methods to verify the tag is actually firing:

**Browser-Based:**
- Google Tag Assistant (Chrome extension) — shows tags found, firing status, errors
- Chrome DevTools Network tab — filter by `googletagmanager.com` or `google-analytics.com`
- Check for `gtag/js` and conversion pings in network requests
- Console: `dataLayer` variable should exist and contain events

**Platform-Based:**
- Google Ads > Tools > Conversions — check "Tracking status" column
- Statuses: Recording conversions, Tag inactive, Unverified, No recent conversions
- Google Ads > Tools > Tag diagnostics

**Tag Sequencing:**
- Google Tag (config) must fire before any conversion tags
- If using GTM: set tag sequencing so config tag fires first
- If using consent mode: `gtag('consent', 'default', {...})` must run before `gtag('config', ...)`

### 5. Conversion Import to Google Ads

Verify that conversion data is flowing into Google Ads:

- Check Conversions column in campaign reports
- Compare conversion count in Google Ads vs. actual form submissions / purchases
- Check for conversion delay (can take up to 24 hours for data to appear)
- Verify "Include in Conversions" is set to Yes for primary actions
- Secondary conversion actions (micro-conversions) should be set to No

---

## Diagnostic Queries

Ask the user these questions to gather context:

1. What is your Google Ads Conversion ID (AW-XXXXXXXXXX)?
2. How many conversion actions do you have? List them.
3. Is the tag implemented directly or via GTM?
4. What CMS / framework is the website built on?
5. Do you use a consent management platform?
6. Are you seeing conversions in Google Ads reports?
7. What is the current tracking status in Google Ads?

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| Tag missing from pages | Critical | No conversion data at all |
| Wrong counting method | High | Over/undercounting conversions |
| $0 conversion value | High | Breaks Value-Based Bidding |
| Multiple conflicting tags | High | Duplicate conversions |
| Missing async attribute | Medium | Page speed degradation |
| Wrong conversion window | Medium | Misattributed conversions |
| Tag in body not head | Low | Slightly delayed firing |

---

## Scoring Contribution

This sub-skill contributes up to **15 points** to the Tracking Health Score:

- Tag present on all pages: 5 points
- Conversion actions configured correctly: 5 points
- Tag firing verified and healthy: 3 points
- No conflicts or duplicates: 2 points
