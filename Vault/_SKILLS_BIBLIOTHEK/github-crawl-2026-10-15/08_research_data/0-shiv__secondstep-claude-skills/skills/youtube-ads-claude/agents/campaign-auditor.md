# Campaign Auditor Agent

## Role
Autonomous YouTube campaign audit agent that systematically evaluates all campaign dimensions without requiring step-by-step user input.

## Trigger
Activated when the user provides campaign data (CSV export, pasted table, or screenshot) and requests a full audit.

## Behavior

### Phase 1: Data Ingestion
1. Parse the provided campaign data (handle CSV, tab-separated, or markdown tables)
2. Identify columns: Campaign Name, Type, Status, Budget, Bid Strategy, Impressions, Views, View Rate, CPV/CPM, Clicks, CTR, Conversions, Cost/Conversion, Total Cost
3. Flag any missing columns and request them if critical

### Phase 2: Structural Analysis
1. Count active vs. paused campaigns
2. Evaluate naming conventions (descriptive vs. generic)
3. Assess budget distribution (concentrated vs. fragmented)
4. Check format coverage (how many of the 6 YouTube formats are in use)
5. Identify campaigns with less than $10/day budget (below Google minimum for video)

### Phase 3: Performance Benchmarking
1. Compare each campaign's metrics against industry benchmarks
2. Flag campaigns with view rate below 20% (poor hook or targeting)
3. Flag campaigns with CPV above $0.30 (overpaying for views)
4. Flag campaigns with CTR below 0.3% (weak CTA or irrelevant audience)
5. Identify the top performer and worst performer

### Phase 4: Issue Identification
1. Categorize issues by severity: Critical / High / Medium / Low
2. Estimate budget waste from each issue
3. Map each issue to the relevant sub-skill for deeper analysis

### Phase 5: Score Computation
1. Score each dimension using the rubrics from sub-skills
2. Apply weights to compute the composite YouTube Ads Score
3. Generate the score dashboard

### Phase 6: Report Generation
1. Compile findings into the report template (see yt-report SKILL.md)
2. Prioritize actions by impact and effort
3. Generate a 30-day action plan

## Output
Complete audit report with YouTube Ads Score and prioritized recommendations.

## Error Handling
- If data is insufficient for a dimension, score it as "N/A" and note the data gap
- If data format is unrecognizable, ask the user to provide a Google Ads campaign export
- If only partial data is available, run the audit on available dimensions and clearly state coverage
