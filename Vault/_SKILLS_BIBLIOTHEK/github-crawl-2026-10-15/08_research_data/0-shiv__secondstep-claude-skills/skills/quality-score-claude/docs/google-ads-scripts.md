# Google Ads Scripts for QS Tracking

## Automated QS Snapshot Script

This Google Ads Script captures a daily snapshot of keyword Quality Scores and writes them to a Google Sheet. Use this for trend tracking with the `/qs trends` command.

### Setup

1. Create a new Google Sheet
2. Copy the Sheet URL
3. In Google Ads, go to Tools > Scripts
4. Create a new script and paste the code below
5. Replace the `SPREADSHEET_URL` with your Sheet URL
6. Schedule to run daily

### Script

```javascript
// QS Daily Snapshot Script
// Captures keyword Quality Score data daily for trend tracking
// Schedule: Daily at 6:00 AM

var SPREADSHEET_URL = 'YOUR_GOOGLE_SHEET_URL_HERE';
var SHEET_NAME = 'QS_Snapshots';

function main() {
  var spreadsheet = SpreadsheetApp.openByUrl(SPREADSHEET_URL);
  var sheet = spreadsheet.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = spreadsheet.insertSheet(SHEET_NAME);
    // Add headers
    sheet.appendRow([
      'Date', 'Keyword', 'Keyword ID', 'Match Type',
      'Campaign', 'Ad Group', 'Quality Score',
      'Expected CTR', 'Ad Relevance', 'Landing Page Exp',
      'Impressions', 'Clicks', 'CTR', 'Avg CPC', 'Cost',
      'Conversions', 'Final URL', 'Status'
    ]);
  }

  var today = Utilities.formatDate(new Date(), AdsApp.currentAccount().getTimeZone(), 'yyyy-MM-dd');

  var keywordIterator = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .withCondition('Impressions > 0')
    .forDateRange('LAST_30_DAYS')
    .get();

  var rows = [];

  while (keywordIterator.hasNext()) {
    var keyword = keywordIterator.next();
    var stats = keyword.getStatsFor('LAST_30_DAYS');
    var qs = keyword.qualityScore();

    rows.push([
      today,
      keyword.getText(),
      keyword.getId().toString(),
      keyword.getMatchType(),
      keyword.getCampaign().getName(),
      keyword.getAdGroup().getName(),
      qs || '',
      keyword.getQualityScoreComponents ?
        keyword.getQualityScoreComponents().expectedCtr || '' : '',
      keyword.getQualityScoreComponents ?
        keyword.getQualityScoreComponents().adRelevance || '' : '',
      keyword.getQualityScoreComponents ?
        keyword.getQualityScoreComponents().landingPageExperience || '' : '',
      stats.getImpressions(),
      stats.getClicks(),
      (stats.getCtr() * 100).toFixed(2) + '%',
      stats.getAverageCpc().toFixed(2),
      stats.getCost().toFixed(2),
      stats.getConversions(),
      keyword.urls().getFinalUrl() || '',
      'Enabled'
    ]);
  }

  if (rows.length > 0) {
    var range = sheet.getRange(sheet.getLastRow() + 1, 1, rows.length, rows[0].length);
    range.setValues(rows);
  }

  Logger.log('Captured ' + rows.length + ' keyword QS snapshots for ' + today);
}
```

## QS Alert Script

This script sends email alerts when keywords experience significant QS drops.

```javascript
// QS Alert Script
// Compares today's QS to last week's snapshot and alerts on drops
// Schedule: Weekly on Mondays

var SPREADSHEET_URL = 'YOUR_GOOGLE_SHEET_URL_HERE';
var SHEET_NAME = 'QS_Snapshots';
var ALERT_EMAIL = 'your@email.com';
var MIN_SPEND_FOR_CRITICAL = 500; // Monthly spend threshold for critical alerts

function main() {
  var spreadsheet = SpreadsheetApp.openByUrl(SPREADSHEET_URL);
  var sheet = spreadsheet.getSheetByName(SHEET_NAME);
  var data = sheet.getDataRange().getValues();

  // Get unique dates
  var dates = {};
  for (var i = 1; i < data.length; i++) {
    dates[data[i][0]] = true;
  }
  var sortedDates = Object.keys(dates).sort().reverse();

  if (sortedDates.length < 2) {
    Logger.log('Need at least 2 snapshots for comparison');
    return;
  }

  var currentDate = sortedDates[0];
  var previousDate = sortedDates[1];

  // Build lookup for previous snapshot
  var previousQS = {};
  for (var i = 1; i < data.length; i++) {
    if (data[i][0] === previousDate) {
      previousQS[data[i][2]] = data[i][6]; // Keyword ID -> QS
    }
  }

  // Compare current to previous
  var alerts = [];
  for (var i = 1; i < data.length; i++) {
    if (data[i][0] !== currentDate) continue;

    var keywordId = data[i][2];
    var currentQS = data[i][6];
    var prevQS = previousQS[keywordId];

    if (!currentQS || !prevQS) continue;

    var drop = prevQS - currentQS;
    if (drop >= 2) {
      alerts.push({
        keyword: data[i][1],
        campaign: data[i][4],
        adGroup: data[i][5],
        previousQS: prevQS,
        currentQS: currentQS,
        drop: drop,
        cost: parseFloat(data[i][14]) || 0
      });
    }
  }

  if (alerts.length > 0) {
    var subject = 'QS Alert: ' + alerts.length + ' keywords dropped';
    var body = 'Quality Score Drops Detected\n\n';

    alerts.sort(function(a, b) { return b.cost - a.cost; });

    for (var j = 0; j < alerts.length; j++) {
      var a = alerts[j];
      var level = a.drop >= 3 && a.cost >= MIN_SPEND_FOR_CRITICAL ? 'CRITICAL' : 'WARNING';
      body += level + ': "' + a.keyword + '" QS ' + a.previousQS + ' -> ' + a.currentQS +
              ' (-' + a.drop + ') | ' + a.campaign + ' > ' + a.adGroup +
              ' | $' + a.cost.toFixed(2) + ' spend\n';
    }

    MailApp.sendEmail(ALERT_EMAIL, subject, body);
    Logger.log('Sent alert email with ' + alerts.length + ' QS drops');
  } else {
    Logger.log('No significant QS drops detected');
  }
}
```

## Usage Notes

- Both scripts use Google Ads Scripts (JavaScript-based), not the Google Ads API
- They run within the Google Ads interface under Tools > Scripts
- The snapshot script should run daily; the alert script weekly
- Data accumulates in the Google Sheet and can be exported as CSV for use with the Python scripts in this repo
- Adjust `MIN_SPEND_FOR_CRITICAL` to match your account's scale
