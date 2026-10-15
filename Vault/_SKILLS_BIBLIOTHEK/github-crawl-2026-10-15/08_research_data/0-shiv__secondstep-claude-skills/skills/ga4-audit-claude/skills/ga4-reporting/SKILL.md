# GA4 Reporting Audit

## Command
`/ga4 reporting`

## Purpose
Audit the reporting configuration in GA4, including default reports, custom reports, explorations, and Looker Studio integration. Reporting is where analytics data becomes actionable insight. Even a perfectly instrumented GA4 property is useless if reports are not configured to surface the right data to the right people at the right time.

## GA4 Reporting Structure

### Report Types

1. **Standard Reports** — Pre-built reports in the Reports section (Life cycle, User, Demographics)
2. **Custom Reports** — Modified or new reports added to the Reports navigation
3. **Explorations** — Advanced analysis tool (formerly Analysis Hub) with multiple techniques
4. **Looker Studio** — External dashboarding connected to GA4 data
5. **BigQuery** — Raw data export for SQL-based analysis

## Audit Checklist

### 1. Default Reports Configuration

GA4 comes with standard report collections. Verify they are properly configured.

**Life Cycle reports:**
- [ ] Acquisition > Overview — Shows user and session acquisition
- [ ] Acquisition > User acquisition — First touch attribution
- [ ] Acquisition > Traffic acquisition — Session-level attribution
- [ ] Engagement > Overview — Engagement metrics summary
- [ ] Engagement > Events — All events with counts
- [ ] Engagement > Conversions — Conversion event performance
- [ ] Engagement > Pages and screens — Page/screen performance
- [ ] Monetization > Overview — Revenue summary (e-commerce)
- [ ] Monetization > E-commerce purchases — Product performance
- [ ] Retention > Overview — User retention curves

**User reports:**
- [ ] Demographics > Overview — Age, gender, interests
- [ ] Demographics > Demographic details — Detailed breakdowns
- [ ] Tech > Overview — Browser, OS, device category
- [ ] Tech > Tech details — Detailed tech breakdowns

**Report customization:**
- [ ] Default reports have been customized to show relevant metrics (not just defaults)
- [ ] Report navigation has been reorganized to match business priorities
- [ ] Irrelevant report collections are hidden (reduce noise)
- [ ] Report comparisons are set up for key segments (e.g., mobile vs desktop)

### 2. Custom Reports

- [ ] Custom reports have been created for key business metrics
- [ ] Custom report navigation is organized logically (by team, by function, by frequency)
- [ ] Summary cards on overview pages show the most important KPIs
- [ ] Custom reports include appropriate dimensions and metrics
- [ ] Date range defaults are appropriate for each report

**Recommended custom reports by role:**
- [ ] Executive dashboard: Revenue, conversions, traffic, YoY comparison
- [ ] Marketing team: Channel performance, campaign ROI, audience insights
- [ ] Product team: Feature usage, user flows, error rates
- [ ] Content team: Page performance, engagement, content groups

### 3. Explorations

Explorations provide advanced analysis capabilities. Verify key exploration types are configured.

**Free-form exploration:**
- [ ] At least one free-form exploration exists
- [ ] Commonly used dimensions and metrics are added as variables
- [ ] Segments are defined for key user groups
- [ ] Date range is appropriate

**Funnel exploration:**
- [ ] Purchase/conversion funnel is built (critical for e-commerce)
- [ ] Funnel steps match the actual user journey
- [ ] Open vs closed funnel is set correctly:
  - Closed: Users must enter at step 1 (strict, lower volume)
  - Open: Users can enter at any step (flexible, higher volume)
- [ ] Funnel has breakdown dimension applied (device, source/medium)
- [ ] Elapsed time between steps is analyzed
- [ ] Funnel trended over time to track improvement

**Path exploration:**
- [ ] Path exploration is configured from key entry points
- [ ] Starting point is set to a meaningful event or page
- [ ] Ending point analysis shows where users drop off
- [ ] Reverse paths from conversions show what drives success

**Segment overlap:**
- [ ] Segment overlap exploration exists for key user segments
- [ ] Segments reveal actionable insights (e.g., mobile users who purchase vs desktop)
- [ ] Up to 3 segments compared simultaneously

**Cohort exploration:**
- [ ] Cohort analysis is configured for retention analysis
- [ ] Cohort type matches business need (acquisition date, conversion date)
- [ ] Return criteria is defined (any event, specific event, conversion)
- [ ] Granularity is appropriate (daily, weekly, monthly)

**User lifetime exploration:**
- [ ] LTV exploration is configured (if sufficient data)
- [ ] Lifetime metrics include: LTV, sessions, transactions, engagement time
- [ ] User acquisition source is used as a dimension
- [ ] Results inform acquisition budget allocation

### 4. Reporting Identity

- [ ] Reporting identity is set appropriately (Admin > Reporting Identity)
- [ ] Options understood:
  - Blended: Most comprehensive, includes modeling for consent gaps
  - Observed: Only includes observed data, no modeling
  - Device-based: Only uses device ID, most conservative
- [ ] Team understands that changing reporting identity changes historical data retroactively
- [ ] Thresholding behavior is understood (some data may be hidden for small sample sizes)

### 5. Comparisons and Segments

- [ ] Default comparisons are configured in reports (e.g., this period vs last period)
- [ ] Key segments are saved and reusable
- [ ] Segments use correct logic (AND vs OR, include vs exclude)
- [ ] No broken segments (referencing deleted events or dimensions)

### 6. Looker Studio Integration

- [ ] GA4 is connected to Looker Studio (if dashboarding is needed)
- [ ] Looker Studio data source uses the correct GA4 property
- [ ] Blending is configured correctly if combining GA4 with other data sources
- [ ] Dashboard refreshes at appropriate intervals
- [ ] Key stakeholder dashboards exist:
  - [ ] Executive/C-suite dashboard (high-level KPIs)
  - [ ] Marketing performance dashboard (channel/campaign detail)
  - [ ] Product/UX dashboard (user behavior, flows)
- [ ] Dashboards have appropriate access controls
- [ ] Calculated fields in Looker Studio are documented
- [ ] Dashboard date range controls work correctly
- [ ] Filter controls are available for key dimensions (source, device, country)

### 7. Alerts and Insights

- [ ] Custom insights (anomaly detection) are configured
- [ ] Alert conditions match business priorities (e.g., conversion rate drop, traffic spike)
- [ ] Alert recipients are correct (not going to an unused email)
- [ ] Automated insights are reviewed regularly (not ignored)
- [ ] At minimum, alerts exist for:
  - [ ] Significant drop in daily sessions (>30%)
  - [ ] Significant drop in conversion rate (>20%)
  - [ ] Revenue anomalies (for e-commerce)
  - [ ] Error page spikes (404/500 events if tracked)

### 8. Data Freshness and Sampling

- [ ] Standard reports show data within 24-48 hours (expected GA4 processing time)
- [ ] Realtime report is functional and showing current activity
- [ ] Explorations with large date ranges are not excessively sampled
- [ ] Sampling indicator is understood by report users
- [ ] If sampling is an issue, BigQuery export is configured for unsampled analysis
- [ ] Property-level data processing delay is within normal bounds

## Common Issues Found

1. **Default reports never customized** — Team uses only out-of-the-box reports, missing business-specific views.
2. **No funnel exploration** — E-commerce site without a purchase funnel exploration, cannot identify checkout drop-off points.
3. **No Looker Studio dashboards** — Stakeholders rely on GA4 UI directly, leading to inconsistent reporting.
4. **Broken segments** — Segments referencing events or dimensions that no longer exist, producing zero results.
5. **No alerts configured** — Tracking breaks and nobody notices for weeks because no anomaly detection is set up.
6. **Wrong reporting identity** — Device-based identity selected when User ID is implemented, losing cross-device insights.
7. **Explorations not shared** — Individual users create personal explorations that are not shared with the team.
8. **Sampled data used for decisions** — Large date range explorations are heavily sampled but users do not notice the sampling indicator.

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Default reports | 15 | 15% |
| Custom reports | 15 | 15% |
| Explorations | 25 | 25% |
| Looker Studio | 20 | 20% |
| Alerts | 15 | 15% |
| Data quality | 10 | 10% |

**Score = (passed_points / total_applicable_points) * 100**

## Output Format

```
## Reporting Audit

**Score: XX/100**

### Report Inventory
- Standard reports customized: Yes/No
- Custom reports: [count]
- Explorations: [count]
- Looker Studio dashboards: [count]
- Alerts configured: [count]

### Exploration Coverage
| Type | Status | Quality |
|------|--------|---------|
| Free-form | Present/Missing | Good/Needs work |
| Funnel | Present/Missing | Good/Needs work |
| Path | Present/Missing | Good/Needs work |
| Segment overlap | Present/Missing | Good/Needs work |
| Cohort | Present/Missing | Good/Needs work |
| User lifetime | Present/Missing | Good/Needs work |

### Findings
[Passed/Failed/Warning items with fix instructions]
```
