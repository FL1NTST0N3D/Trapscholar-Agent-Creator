# Quality Score Tracking Scripts

## Command: `/script qs`

## Overview

Quality Score (QS) is Google's 1-10 rating of keyword quality. It directly impacts your ad rank and cost per click — a QS of 10 can reduce your CPC by up to 50% compared to a QS of 5. Yet Google Ads does not provide historical Quality Score data. Once QS changes, the old value is gone forever.

Quality Score tracking scripts solve this by logging QS values daily to a Google Sheet, creating a permanent historical record. This allows you to correlate QS changes with specific actions (ad copy changes, landing page updates, bid strategy switches) and identify trends before they become problems.

QS is composed of three components, each rated Above Average, Average, or Below Average:
- **Expected CTR** — How likely your ad is to be clicked
- **Ad Relevance** — How closely your ad matches the search intent
- **Landing Page Experience** — How relevant and useful your landing page is

## Script Templates

### 1. Daily QS Logger
Records the Quality Score and its three components for every active keyword in the account to a Google Sheet, once per day.

**Key Configuration:**
- `SPREADSHEET_URL` — Google Sheet URL for QS data storage
- `SHEET_NAME` — Tab name (default: "QS History")
- `MIN_IMPRESSIONS` — Only track keywords with this many impressions (default: 10)
- `CAMPAIGN_FILTER` — Optional: only track specific campaigns

**How it works:**
1. Queries all enabled keywords with their QS and component ratings
2. Opens the target Google Sheet
3. For each keyword, appends a row: Date, Campaign, Ad Group, Keyword, Match Type, QS, Expected CTR, Ad Relevance, Landing Page Experience
4. Skips keywords with no impressions (QS is often null/0 for inactive keywords)
5. Logs the total number of keywords tracked

### 2. QS Drop Alert
Compares today's Quality Score to the most recent logged value and sends an email alert when any keyword's QS drops by 2 or more points.

**Key Configuration:**
- `ALERT_EMAIL` — Email address for QS drop alerts
- `DROP_THRESHOLD` — Minimum QS point drop to trigger alert (default: 2)
- `SPREADSHEET_URL` — Same sheet used by the Daily QS Logger
- `MIN_COST` — Only alert on keywords spending above this amount (to avoid noise from low-spend keywords)

**How it works:**
1. Reads the most recent QS data from the Google Sheet
2. Queries current QS from the Google Ads API
3. Compares current vs logged QS for each keyword
4. Filters for drops >= DROP_THRESHOLD on keywords spending >= MIN_COST
5. Sends an HTML email listing affected keywords with campaign context

### 3. QS Trend Visualization
Reads the historical QS data from Google Sheets and creates a summary tab with average QS over time, QS distribution charts, and a breakdown of component ratings.

**Key Configuration:**
- `SPREADSHEET_URL` — QS history spreadsheet
- `SUMMARY_SHEET_NAME` — Tab for the summary (default: "QS Summary")
- `TREND_PERIOD_DAYS` — Number of days to include in trend (default: 90)

### 4. QS Component Deep Dive
Focuses specifically on the three QS components. Identifies keywords where a single component is dragging down overall QS and provides actionable recommendations.

**Key Configuration:**
- `ALERT_EMAIL` — Email for the recommendations report
- `FOCUS_COMPONENT` — "ALL", "EXPECTED_CTR", "AD_RELEVANCE", or "LANDING_PAGE"

## Best Practices

- **Run the QS logger daily at the same time**: Consistency matters for trend accuracy. Schedule for early morning before daily spend accrues.
- **Track components, not just the number**: The overall QS number is a composite. Knowing which component dropped tells you exactly what to fix (ad copy vs landing page vs keyword relevance).
- **Focus on high-spend keywords**: QS fluctuations on keywords spending $0.50/month are noise. Filter your alerts to keywords spending at least $50/month.
- **Correlate with changes**: When you see a QS drop, check your change history — was there an ad copy update, landing page change, or bid strategy switch around that date?
- **Do not chase QS obsessively**: QS is an input metric, not a goal. A keyword with QS 6 and strong conversion rate is more valuable than a keyword with QS 10 and zero conversions.
- **Archive old data**: After 6 months, move older rows to an archive sheet to keep the main sheet performant.
- **Separate branded vs non-branded**: Brand keywords typically have QS 8-10 and inflate your averages. Track them separately.

## Common Pitfalls

1. **Null QS values**: Keywords with very few impressions often have QS = 0 or null. Filter these out to avoid polluting your data.
2. **QS caching**: Google does not recalculate QS in real-time. Changes may take 24-48 hours to reflect. Do not over-react to single-day fluctuations.
3. **Sheet row limits**: Google Sheets has a 10 million cell limit. An account with 5,000 keywords logging daily will hit ~35 million cells per year. Archive regularly.
4. **Component text values**: QS components return text strings ("ABOVE_AVERAGE", "AVERAGE", "BELOW_AVERAGE"), not numbers. Map these to numeric values (3, 2, 1) for calculations.
5. **Match type matters**: The same keyword in exact and broad match can have different Quality Scores. Track them separately.

## GAQL Queries Used

```sql
-- Keyword Quality Score with components
SELECT ad_group_criterion.keyword.text,
       ad_group_criterion.keyword.match_type,
       ad_group_criterion.quality_info.quality_score,
       ad_group_criterion.quality_info.creative_quality_score,
       ad_group_criterion.quality_info.search_predicted_ctr,
       ad_group_criterion.quality_info.post_click_quality_score,
       campaign.name, ad_group.name, metrics.cost_micros,
       metrics.impressions
FROM keyword_view
WHERE ad_group_criterion.status = 'ENABLED'
AND campaign.status = 'ENABLED'
AND metrics.impressions > 0
```

## Template Reference

See `templates/qs-tracker.js` for the complete Quality Score daily logging script.
