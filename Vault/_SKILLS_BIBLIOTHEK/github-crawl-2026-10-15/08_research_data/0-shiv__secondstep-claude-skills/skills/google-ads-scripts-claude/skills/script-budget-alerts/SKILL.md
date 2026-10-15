# Budget Alerts & Pacing Scripts

## Command: `/script budget`

## Overview

Budget management is the most critical automation in Google Ads. Overspending wastes money; underspending misses opportunity. These scripts monitor spend pacing against targets and take action — sending alerts, pausing campaigns, or adjusting budgets — before problems compound.

Budget pacing scripts compare your actual daily or monthly spend against a target trajectory. For example, if your monthly budget is $10,000 and you are 15 days into the month, you should have spent roughly $5,000. If you have spent $7,000, you are over-pacing by 40% and the script sends an alert or pauses campaigns.

## Script Templates

### 1. Budget Pacing Alert
Compares cumulative spend vs expected spend for the month. Sends an email alert if spend is more than 10% over or under the linear pacing target. Runs daily.

**Key Configuration:**
- `MONTHLY_BUDGET` — Target monthly spend in account currency
- `ALERT_EMAIL` — Email address to receive pacing alerts
- `OVER_PACE_THRESHOLD` — Percentage over target to trigger alert (default: 1.10 = 10% over)
- `UNDER_PACE_THRESHOLD` — Percentage under target to trigger alert (default: 0.80 = 20% under)

**How it works:**
1. Gets the current day of the month and total days in the month
2. Calculates expected spend: `(MONTHLY_BUDGET / totalDays) * currentDay`
3. Queries actual spend for the month so far using GAQL
4. Compares actual vs expected and sends email if thresholds are breached

### 2. Monthly Budget Limiter
Pauses all enabled campaigns when cumulative monthly spend reaches a configurable threshold (e.g., 95% of monthly budget). Re-enables campaigns on the 1st of each month.

**Key Configuration:**
- `MONTHLY_BUDGET` — The hard monthly budget cap
- `PAUSE_THRESHOLD` — Percentage of budget to trigger pause (default: 0.95 = 95%)
- `LABEL_NAME` — Label applied to paused campaigns so the script knows which to re-enable

**How it works:**
1. Queries total account spend for the current month
2. If spend >= MONTHLY_BUDGET * PAUSE_THRESHOLD, pauses all enabled campaigns and labels them
3. On the 1st of the month, re-enables labeled campaigns and removes the label

### 3. Campaign-Level Budget Monitor
Tracks individual campaign spend against per-campaign budget targets defined in a Google Sheet. Alerts when any campaign deviates from its target.

**Key Configuration:**
- `SPREADSHEET_URL` — Google Sheet with columns: Campaign Name, Monthly Budget, Alert Email
- `THRESHOLD_PERCENT` — Deviation threshold for alerts

### 4. Shared Budget Tracker
Monitors Google Ads shared budgets and logs daily utilization to a Google Sheet. Alerts when shared budgets are consistently hitting their daily limit (indicating budget-constrained campaigns).

## Best Practices

- **Run budget pacing scripts daily**, ideally in the morning so you can react during business hours
- **Set conservative thresholds** — a 10% over-pace alert gives you time to react before overspending significantly
- **Use labels for pause/resume** — never just pause everything; label what the script paused so it can selectively re-enable
- **Account for weekends** — spending patterns differ on weekends; consider a weighted pacing model instead of linear
- **Monitor at campaign level** — account-level pacing can mask individual campaign issues (one campaign overspending while another underspends)
- **Log to Google Sheets** — keep a daily spend log for trend analysis and auditing
- **Test with alerts first** — start with email-only alerts before enabling auto-pause functionality

## Common Pitfalls

1. **Forgetting micros conversion**: Google Ads API returns cost in micros (1,000,000 = $1.00). Always divide by 1e6.
2. **Timezone mismatch**: Script timezone vs account timezone can cause off-by-one-day errors in spend calculations.
3. **Shared budgets**: Campaign-level budget queries do not work correctly with shared budgets; use shared budget reporting instead.
4. **Month boundaries**: Be careful with date ranges around month-end; `THIS_MONTH` resets on the 1st.
5. **Paused campaign re-enabling**: Never blindly re-enable all paused campaigns — some may have been manually paused for other reasons.

## Template Reference

See `templates/budget-pacing.js` for the complete, ready-to-use budget pacing script with email alerts.

## GAQL Queries Used

```sql
-- Account-level spend for current month
SELECT metrics.cost_micros
FROM customer
WHERE segments.date DURING THIS_MONTH

-- Campaign-level spend
SELECT campaign.name, campaign.status, metrics.cost_micros
FROM campaign
WHERE segments.date DURING THIS_MONTH
AND campaign.status = 'ENABLED'
```
