# Automated Reporting Scripts

## Command: `/script report`

## Overview

Reporting is the most common use case for Google Ads Scripts. Instead of manually pulling data from the Google Ads UI every morning, scripts can automatically compile performance metrics and deliver them via email or push them to Google Sheets on a schedule. This ensures stakeholders always have fresh data without anyone needing to log into the platform.

Reporting scripts are typically read-only — they query data but do not modify campaigns. This makes them the safest category of scripts and an excellent starting point for advertisers new to Google Ads Scripts.

## Script Templates

### 1. Daily Performance Email
Sends a morning email with yesterday's key metrics: spend, clicks, impressions, CTR, CPC, conversions, CPA, and conversion value. Includes comparison to the same day last week.

**Key Configuration:**
- `ALERT_EMAILS` — Comma-separated list of email recipients
- `INCLUDE_CAMPAIGN_BREAKDOWN` — Whether to include per-campaign rows (default: true)
- `CURRENCY_SYMBOL` — Currency symbol for formatting (default: "$")
- `COMPARISON_PERIOD` — "LAST_WEEK" or "LAST_MONTH" for delta comparison

**How it works:**
1. Queries account-level metrics for YESTERDAY using GAQL
2. Queries the same metrics for the comparison day (7 days ago)
3. Calculates deltas (% change) for each metric
4. Builds an HTML email table with conditional formatting (green for improvements, red for declines)
5. Sends via MailApp.sendEmail()

### 2. Weekly Google Sheets Summary
Appends a new row to a Google Sheet every week with account-level performance. Over time, this builds a historical trend dataset perfect for charts and dashboards.

**Key Configuration:**
- `SPREADSHEET_URL` — URL of the target Google Sheet
- `SHEET_NAME` — Tab name to write to (default: "Weekly Summary")
- `DATE_RANGE` — Report period (default: "LAST_7_DAYS")

**How it works:**
1. Opens the target Google Sheet via SpreadsheetApp
2. Queries account-level metrics for the date range
3. If the header row does not exist, creates it
4. Appends a new row with: Date, Spend, Clicks, Impressions, CTR, CPC, Conversions, CPA, Conv Value, ROAS
5. Optionally auto-creates charts from the data

### 3. MCC Cross-Account Report
For agencies managing multiple accounts under an MCC (My Client Center), this script iterates through all child accounts, collects performance data, and compiles a single summary spreadsheet.

**Key Configuration:**
- `SPREADSHEET_URL` — Shared Google Sheet for the report
- `ACCOUNT_IDS` — List of account IDs to include (or "ALL" for every account under MCC)
- `DATE_RANGE` — Reporting period
- `METRICS` — Which metrics to pull

**How it works:**
1. Uses `MccApp.accounts()` to iterate through managed accounts
2. For each account, switches context with `MccApp.select(account)`
3. Runs the standard performance query
4. Writes each account's data as a row in the Google Sheet
5. Adds a summary row at the bottom with totals

### 4. Custom KPI Dashboard
Builds a live-updating dashboard in Google Sheets with custom KPIs. Supports calculated fields like ROAS, profit margin, and cost per lead by lead type.

**Key Configuration:**
- `SPREADSHEET_URL` — Dashboard Google Sheet
- `KPI_DEFINITIONS` — Array of custom KPI objects with name, query, and formula
- `REFRESH_SCHEDULE` — How often to update (matches script scheduling)

## Best Practices

- **Schedule reports before business hours**: Set daily reports to run at 6-7 AM so data is ready when the team starts work.
- **Use HTML emails for readability**: Plain text emails are hard to scan. Use HTML tables with inline CSS for clean formatting.
- **Include period-over-period comparison**: Raw numbers without context are meaningless. Always show the delta vs previous period.
- **Keep MCC reports under 50 accounts per run**: Google Ads Scripts limit MCC iterations to 50 accounts. For larger MCCs, split into multiple script executions.
- **Add conditional formatting**: Color-code metrics — green for improvements, red for declines, yellow for neutral — to enable quick scanning.
- **Archive old data**: Google Sheets has a 10 million cell limit. For long-running reports, periodically archive older data to a separate sheet.
- **Use named ranges in Sheets**: Makes it easier to build charts and dashboards on top of the raw data.

## Common Pitfalls

1. **MailApp daily limits**: Google Ads Scripts can send 200 emails per day. If you have many scripts sending alerts, you can hit this limit.
2. **Spreadsheet access permissions**: The Google Ads account owner must have edit access to the target Google Sheet. Share the sheet with the account's login email.
3. **Date range confusion**: "YESTERDAY" and "LAST_7_DAYS" exclude today. "TODAY" includes partial data. For complete-day reporting, use "YESTERDAY".
4. **MCC context switching**: After `MccApp.select(account)`, all AdsApp calls operate on that child account. Do not forget to switch context.
5. **Large reports timing out**: Reports with many campaigns and long date ranges can exceed the 30-minute limit. Use filters and shorter date ranges.

## GAQL Queries Used

```sql
-- Account-level daily summary
SELECT metrics.cost_micros, metrics.clicks, metrics.impressions,
       metrics.conversions, metrics.conversions_value
FROM customer
WHERE segments.date = 'YYYY-MM-DD'

-- Campaign-level breakdown
SELECT campaign.name, campaign.status, metrics.cost_micros, metrics.clicks,
       metrics.impressions, metrics.conversions, metrics.conversions_value
FROM campaign
WHERE segments.date DURING LAST_7_DAYS
AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC

-- MCC account list
SELECT customer_client.client_customer, customer_client.descriptive_name
FROM customer_client
WHERE customer_client.status = 'ENABLED'
```

## Template Reference

See `templates/daily-report.js` for the complete daily performance email script.
