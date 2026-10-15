# Google Ads Scripts — Master Skill Reference

## Overview

Google Ads Scripts are JavaScript-based automations that run directly within the Google Ads platform. They provide programmatic access to campaigns, ad groups, keywords, ads, extensions, reports, and more — without requiring an external server, OAuth setup, or API credentials.

Scripts are the most underutilized power feature in Google Ads. Only about 15% of advertisers use them, yet they can save 10-20 hours per month of repetitive manual work and improve ROAS by an average of 18% through automated bid management.

## How Google Ads Scripts Work

### Execution Environment
- **Language**: JavaScript (ES5 baseline, partial ES6 support — `let`, `const`, arrow functions work; `async/await` does not)
- **Runtime**: Google's servers — no hosting, no deployment, no infrastructure
- **Entry Point**: Every script must have a `function main() {}` — this is what Google Ads calls
- **Scheduling**: Scripts can run hourly, daily, weekly, or monthly via the Scripts UI
- **Trigger**: Manual run from the UI, or scheduled automatic execution

### API Access
- **Current API Version**: Google Ads Scripts use a simplified wrapper around the Google Ads API (v15+)
- **Primary Object**: `AdsApp` — the global entry point for all account data
- **Report Queries**: Use GAQL (Google Ads Query Language) via `AdsApp.report(query)`
- **External Services**: `UrlFetchApp.fetch()` for HTTP calls, `SpreadsheetApp` for Google Sheets, `MailApp` for emails

### Execution Limits
| Limit | Value |
|-------|-------|
| Maximum runtime | 30 minutes per execution |
| API calls | 250,000 per execution |
| Entities modified | 250,000 per execution |
| URL fetches | 50 per execution (UrlFetchApp) |
| Email sends | 200 per day (MailApp) |
| Script size | 250 KB max |
| Spreadsheet writes | 500,000 cells per execution |
| MCC script accounts | Process up to 50 accounts per execution |

### Key AdsApp Methods
```javascript
// Selectors (return iterators)
AdsApp.campaigns()
AdsApp.adGroups()
AdsApp.keywords()
AdsApp.ads()
AdsApp.extensions().sitelinks()

// Filtering
.withCondition("Cost > 100")
.withCondition("metrics.clicks > 50")
.forDateRange("LAST_30_DAYS")
.orderBy("metrics.cost_micros DESC")
.withLimit(100)

// Reports (GAQL)
AdsApp.report(
  "SELECT campaign.name, metrics.cost_micros " +
  "FROM campaign " +
  "WHERE segments.date DURING LAST_7_DAYS"
);

// External services
MailApp.sendEmail("you@example.com", "Subject", "Body");
SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/...");
UrlFetchApp.fetch("https://api.example.com/data");
```

## Script Categories

This skill set covers 10 categories of Google Ads Scripts:

### 1. Budget Alerts (`/script budget`)
Monitor spend pacing against targets. Pause campaigns at budget thresholds. Send email alerts for over/under-pacing. Track shared budgets.

### 2. Bid Management (`/script bids`)
Automate bid adjustments by hour, device, geography, and performance. ROAS-based bidding rules. Keyword-level bid optimization.

### 3. Reporting (`/script report`)
Automated performance reports via email and Google Sheets. Daily summaries, weekly trends, MCC cross-account dashboards.

### 4. Link Checker (`/script links`)
Validate all ad URLs, sitelink destinations, and keyword landing pages. Email reports of broken links (404, 500, timeout).

### 5. Quality Score (`/script qs`)
Track Quality Score changes over time. Log to Google Sheets daily. Alert on QS drops. Component-level tracking (Expected CTR, Ad Relevance, Landing Page).

### 6. Search Terms (`/script search-terms`)
Mine search term reports for keyword additions and negative keywords. N-gram analysis to find patterns. Cost analysis for non-converting terms.

### 7. Anomaly Detection (`/script anomaly`)
Compare current metrics against historical averages. Flag significant deviations in spend, CPA, CTR, and conversions. Configurable alert thresholds.

### 8. Labeling (`/script labels`)
Automatically label campaigns, ad groups, and keywords by performance tier. Dynamic label refresh on schedule. Custom label taxonomies.

### 9. Script Generator (`/script generate`)
Describe your automation need in plain English. The skill generates complete, runnable Google Ads Script code with error handling and logging.

### 10. Script Audit (`/script audit`)
Inventory of running scripts, execution history analysis, error log parsing, and optimization recommendations.

## Common Script Patterns

### Iterator Pattern
```javascript
var campaignIterator = AdsApp.campaigns()
  .withCondition("Status = ENABLED")
  .get();
while (campaignIterator.hasNext()) {
  var campaign = campaignIterator.next();
  Logger.log(campaign.getName() + ": " + campaign.getStatsFor("LAST_30_DAYS").getCost());
}
```

### Report Pattern
```javascript
var report = AdsApp.report(
  "SELECT campaign.name, metrics.cost_micros, metrics.conversions " +
  "FROM campaign " +
  "WHERE segments.date DURING LAST_7_DAYS " +
  "AND campaign.status = 'ENABLED'"
);
var rows = report.rows();
while (rows.hasNext()) {
  var row = rows.next();
  Logger.log(row['campaign.name'] + " - Cost: " + (row['metrics.cost_micros'] / 1e6));
}
```

### Google Sheets Pattern
```javascript
var ss = SpreadsheetApp.openByUrl(SPREADSHEET_URL);
var sheet = ss.getSheetByName("Data") || ss.insertSheet("Data");
sheet.appendRow([new Date(), campaignName, cost, conversions, cpa]);
```

### Email Alert Pattern
```javascript
if (anomalyDetected) {
  MailApp.sendEmail({
    to: ALERT_EMAIL,
    subject: "Google Ads Alert: " + alertType,
    htmlBody: buildEmailHtml(alertData)
  });
}
```

## Usage in Claude Code

When a user invokes any `/script` command, the relevant sub-skill is loaded. The sub-skill provides:
1. Context about the script category
2. Ready-to-use JavaScript code templates
3. Customization guidance for the user's specific account
4. Best practices and gotchas for that script type

The skill always generates complete, runnable scripts — not pseudocode. Every script includes:
- Configuration section at the top (emails, thresholds, URLs)
- Error handling with try/catch blocks
- Logging via `Logger.log()` for debugging
- Comments explaining each section
