# Link Checker Scripts

## Command: `/script links`

## Overview

Broken landing pages are one of the most expensive and preventable problems in Google Ads. When a user clicks your ad and lands on a 404 error page, you pay for the click but get zero chance of conversion. Worse, Google will eventually lower your Quality Score for that keyword, increasing your CPCs across the board.

Link checker scripts proactively validate every URL in your Google Ads account — ad final URLs, sitelink extensions, keyword-level destination URLs, and display URLs. They use `UrlFetchApp.fetch()` to make HTTP requests and check for non-200 status codes, then compile a report of broken links and email it to your team.

Google Ads Scripts are limited to 50 URL fetch calls per execution, so these scripts use batching strategies to check large accounts across multiple runs.

## Script Templates

### 1. Ad URL Validator
Checks the final URL of every enabled ad in the account. Flags URLs returning 404, 500, 503, or any non-200 status code. Handles redirects gracefully — a 301/302 that resolves to a 200 is considered valid.

**Key Configuration:**
- `ALERT_EMAIL` — Email to receive broken link reports
- `TIMEOUT_MS` — HTTP request timeout in milliseconds (default: 10000)
- `CHECK_LIMIT` — Maximum URLs to check per execution (default: 45, leaving buffer under the 50 limit)
- `SPREADSHEET_URL` — Optional: log all results to a Google Sheet

**How it works:**
1. Queries all enabled ads and extracts unique final URLs
2. Checks up to CHECK_LIMIT URLs per run using UrlFetchApp.fetch()
3. Tracks which URLs have been checked in a Google Sheet to avoid re-checking
4. For each URL, records: status code, response time, redirect chain
5. Compiles broken URLs into an HTML email report with campaign/ad group context

### 2. Sitelink URL Checker
Validates all sitelink extension URLs. Sitelinks are often forgotten when landing pages change, making them a common source of broken links.

**Key Configuration:**
- `ALERT_EMAIL` — Email for broken sitelink reports
- `INCLUDE_CAMPAIGN_SITELINKS` — Check campaign-level sitelinks (default: true)
- `INCLUDE_ACCOUNT_SITELINKS` — Check account-level sitelinks (default: true)

**How it works:**
1. Iterates through all sitelink extensions using `AdsApp.extensions().sitelinks()`
2. Extracts the final URL from each sitelink
3. Validates each URL and logs the result
4. Emails a report of any broken sitelinks with their associated campaigns

### 3. Keyword Destination URL Audit
Checks keyword-level final URLs (when set, overriding the ad-level URL). Keywords with custom URLs are easy to overlook and frequently break.

**Key Configuration:**
- `ALERT_EMAIL` — Email for the report
- `ONLY_CUSTOM_URLS` — Only check keywords with non-default URLs (default: true)

### 4. Comprehensive Broken Links Report
Combines all three checks (ads, sitelinks, keywords) into a single weekly report. Prioritizes URLs by spend — broken URLs on high-spend keywords are flagged as critical.

**Key Configuration:**
- `ALERT_EMAIL` — Email recipients
- `SPREADSHEET_URL` — Historical log of all checks
- `SEVERITY_THRESHOLD` — Spend level for "critical" classification (default: $100/month)

## Best Practices

- **Run weekly, not daily**: URL statuses rarely change daily, and the 50 URL fetch limit means daily runs only cover a fraction of large accounts.
- **Use a tracking spreadsheet**: Store checked URLs with timestamps so you do not re-check the same URL every run. Only re-check URLs older than 7 days.
- **Handle timeouts gracefully**: A timeout is not necessarily a broken page — it could be a slow server. Retry timed-out URLs once before flagging them.
- **Check from the right location**: UrlFetchApp runs from Google's servers (typically US-based). Geo-restricted pages may return false positives.
- **Batch and prioritize**: Check high-spend URLs first. A broken URL on a $50/day keyword is more urgent than one on a $1/day keyword.
- **Exclude known patterns**: Some sites use JavaScript rendering and return a 200 status code even for "not found" pages. Add pattern matching for known soft-404 strings.
- **Monitor response times**: Pages that take 5+ seconds to load hurt conversion rates even if they return 200. Flag slow pages in your report.

## Common Pitfalls

1. **50 URL fetch limit**: This is per script execution, not per day. For large accounts, you must batch across multiple scheduled runs.
2. **Bot detection**: Some sites block requests from Google's servers. Use `muteHttpExceptions: true` in fetch options to handle this.
3. **Redirect chains**: A URL that 301-redirects to another URL that 302-redirects to a 200 page is technically working. Follow redirects (default behavior) and check the final status.
4. **HTTPS certificate errors**: UrlFetchApp will fail on invalid SSL certificates. Use `validateHttpsCertificates: false` for internal staging URLs.
5. **Soft 404s**: Some sites return a 200 status code but display a "page not found" message. These require content inspection to detect.

## GAQL Queries Used

```sql
-- Ad URLs
SELECT ad_group_ad.ad.final_urls, campaign.name, ad_group.name,
       metrics.cost_micros
FROM ad_group_ad
WHERE ad_group_ad.status = 'ENABLED'
AND campaign.status = 'ENABLED'

-- Keyword URLs (custom destinations only)
SELECT ad_group_criterion.keyword.text, ad_group_criterion.final_urls,
       campaign.name, metrics.cost_micros
FROM keyword_view
WHERE ad_group_criterion.status = 'ENABLED'
AND ad_group_criterion.final_urls IS NOT NULL
```

## Template Reference

See `templates/link-checker.js` for the complete ad URL validation script with email reporting.
