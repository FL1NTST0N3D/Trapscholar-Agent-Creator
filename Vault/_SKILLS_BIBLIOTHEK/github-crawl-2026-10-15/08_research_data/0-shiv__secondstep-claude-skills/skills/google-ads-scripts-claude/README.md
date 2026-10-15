# Google Ads Scripts Claude

**50+ ready-to-use Google Ads Scripts. Budget alerts, bid rules, performance reports, broken link detection, anomaly alerts & more — all generated inside Claude Code.**

---

## Why Google Ads Scripts?

| Stat | Detail |
|------|--------|
| **Only 15%** of advertisers use Google Ads Scripts | Massive competitive advantage for those who do |
| **10-20 hours/month** saved | Automating repetitive account management tasks |
| **18% avg ROAS improvement** | From automated bid rules vs manual bidding |

Google Ads Scripts are JavaScript-based automations that run directly inside your Google Ads account. They can read and modify campaigns, ad groups, keywords, ads, and more — on a schedule or on-demand. No external server needed.

---

## Quick Start

Install the skill in Claude Code:

```bash
claude install-skill google-ads-scripts-claude
```

Then use any of these commands:

| Command | What It Does |
|---------|-------------|
| `/script generate` | Describe what you want in plain English, get a working script |
| `/script budget` | Budget pacing alerts, monthly limiters, pause at threshold |
| `/script bids` | Hourly bidding, device bid rules, geo bid adjustments |
| `/script report` | Daily email reports, weekly Sheets summaries, MCC reports |
| `/script links` | Check all ad/sitelink/keyword URLs for broken links |
| `/script qs` | Track Quality Score changes, alert on drops, trend analysis |
| `/script search-terms` | Mine search terms, flag negatives, N-gram analysis |
| `/script anomaly` | Detect performance anomalies vs 7-day averages |
| `/script labels` | Auto-label campaigns/ad groups by performance tier |
| `/script audit` | Audit running scripts, execution history, error logs |

---

## Script Categories

### 1. Budget Management
- **Budget Pacing** — Compare daily spend vs target, email alerts when over/under pacing
- **Monthly Budget Limiter** — Pause campaigns when monthly budget is exhausted
- **Campaign Pause at Threshold** — Emergency stop when spend exceeds configurable limit
- **Shared Budget Monitor** — Track shared budgets across campaigns

### 2. Bid Management
- **Hourly Bid Adjustments** — Modify bids based on time-of-day performance
- **Device Bid Rules** — Adjust bids per device type using conversion data
- **Geo Bid Adjustments** — Optimize location bid modifiers from conversion data
- **ROAS-Based Bidding** — Raise bids on high-ROAS keywords, lower on poor performers

### 3. Reporting
- **Daily Performance Email** — Key metrics delivered to your inbox every morning
- **Weekly Google Sheets Summary** — Auto-populated spreadsheet with weekly trends
- **MCC Cross-Account Report** — Aggregate performance across all managed accounts
- **Custom KPI Dashboard** — Track your chosen KPIs in a live Google Sheet

### 4. Link Checking
- **Ad URL Validator** — Check all final URLs for 404/500 errors
- **Sitelink URL Checker** — Validate every sitelink destination
- **Keyword URL Audit** — Find keywords pointing to broken landing pages
- **Broken Links Email Report** — Summary of all broken URLs with fix recommendations

### 5. Quality Score
- **QS Daily Logger** — Record Quality Score to Google Sheets daily
- **QS Drop Alerts** — Email notification when QS falls below threshold
- **Historical QS Trends** — Visualize QS changes over time in Sheets
- **QS Component Tracker** — Track Expected CTR, Ad Relevance, Landing Page Experience

### 6. Search Terms
- **High-Performer Mining** — Identify search terms to add as exact match keywords
- **Negative Keyword Flagger** — Flag irrelevant terms for negative keyword lists
- **N-Gram Analysis** — Break search terms into n-grams to find patterns
- **Search Term Cost Analysis** — Find expensive terms with no conversions

### 7. Anomaly Detection
- **Spend Anomaly Alerts** — Flag days where spend deviates >2x from 7-day avg
- **CPA Spike Detection** — Alert when cost per acquisition jumps abnormally
- **CTR Drop Monitor** — Detect sudden CTR decreases across campaigns
- **Conversion Volume Alerts** — Notify when conversions drop below expected range

### 8. Labeling
- **Performance Tier Labels** — Top Performer, Average, Underperformer, Watch List
- **Budget Tier Labels** — High Spend, Medium Spend, Low Spend
- **Conversion Labels** — Converting, Non-Converting, New Converter
- **Dynamic Label Refresh** — Auto-update labels on schedule

### 9. Script Generator
- **Plain English to Script** — Describe automation needs, get working code
- **Template Customizer** — Start from a template, customize with your parameters
- **Script Combiner** — Merge multiple scripts into one scheduled runner
- **Error Handler Wrapper** — Add robust error handling to any script

### 10. Script Audit
- **Running Scripts Inventory** — List all active scripts and their schedules
- **Execution History Report** — Track success/failure rates over time
- **Error Log Analyzer** — Parse error patterns and suggest fixes
- **Optimization Recommendations** — Suggest script improvements and new automations

---

## Google Ads Scripts Fundamentals

### How Scripts Work
- **Language**: JavaScript (ES5-compatible, some ES6 features)
- **Runtime**: Executes inside Google Ads servers — no external hosting needed
- **API Version**: Google Ads API v15+ (scripts use a simplified wrapper)
- **Execution Limit**: 30 minutes max runtime per execution
- **API Call Limit**: 250,000 API calls per execution
- **Scheduling**: Hourly, daily, weekly, or monthly

### Key Objects
```javascript
AdsApp.campaigns()          // Access campaigns
AdsApp.adGroups()           // Access ad groups
AdsApp.keywords()           // Access keywords
AdsApp.ads()                // Access ads
AdsApp.report()             // Run GAQL reports
MailApp.sendEmail()          // Send email alerts
SpreadsheetApp.openByUrl()   // Write to Google Sheets
UrlFetchApp.fetch()          // Make HTTP requests
```

### Script Structure
```javascript
function main() {
  // 1. Query data
  // 2. Process & analyze
  // 3. Take action (modify bids, pause, label)
  // 4. Report results (email, Sheets)
}
```

---

## Project Structure

```
google-ads-scripts-claude/
├── README.md
├── SKILL.md                      # Main skill reference
├── CLAUDE.md                     # Claude Code configuration
├── .claudeignore                 # Files to ignore
├── scripts-skill/
│   └── SKILL.md                  # Script skill entry point
├── skills/
│   ├── script-budget-alerts/     # Budget pacing & alerts
│   ├── script-bid-management/    # Bid adjustment scripts
│   ├── script-reporting/         # Automated reporting
│   ├── script-link-checker/      # URL validation
│   ├── script-quality-score/     # QS tracking
│   ├── script-search-terms/      # Search term mining
│   ├── script-anomaly-detection/ # Performance anomalies
│   ├── script-labeling/          # Auto-labeling
│   ├── script-generator/         # Custom script generator
│   └── script-report/            # Script audit
├── agents/
│   ├── script-builder.md         # Script generation agent
│   ├── script-debugger.md        # Script debugging agent
│   └── script-optimizer.md       # Script optimization agent
├── scripts/
│   ├── validate-script.py        # Validate script syntax
│   └── template-renderer.py      # Render templates with config
├── templates/
│   ├── budget-pacing.js          # Budget pacing template
│   ├── bid-adjustments.js        # Bid adjustment template
│   ├── daily-report.js           # Daily report template
│   ├── link-checker.js           # Link checker template
│   ├── qs-tracker.js             # Quality Score tracker
│   ├── search-term-miner.js      # Search term mining
│   ├── anomaly-alert.js          # Anomaly detection
│   └── auto-labeler.js           # Auto-labeling template
├── docs/
│   ├── google-ads-scripts-api.md # API reference
│   ├── execution-limits.md       # Limits & quotas
│   ├── troubleshooting.md        # Common errors & fixes
│   └── best-practices.md         # Script best practices
└── assets/
    └── .gitkeep
```

---

## Requirements

- Google Ads account with script access (standard or MCC)
- Google Sheets (for reporting scripts)
- Email address for alert scripts
- Claude Code CLI installed

---

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))
Second Step Digital Marketing | [getsecondstep.com](https://getsecondstep.com)

---

## License

MIT License. Use these scripts freely in your Google Ads accounts.
