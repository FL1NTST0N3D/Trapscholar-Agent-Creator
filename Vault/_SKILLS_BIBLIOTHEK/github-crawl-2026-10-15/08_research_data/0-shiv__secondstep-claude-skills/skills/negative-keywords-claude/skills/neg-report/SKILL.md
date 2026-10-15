# Negative Keyword Audit Report Generator

## Command: /negatives report

Generate a comprehensive negative keyword audit report combining coverage scoring, top recommendations, conflict detection, industry list matching, and estimated savings into a single actionable document. This is the master output that ties all sub-skills together.

## What the Report Contains

The negative keyword audit report is a complete diagnostic of an account's negative keyword health. It is designed to be shared with clients, stakeholders, or used internally as an optimization roadmap. Every finding includes specific actions with estimated impact.

## Report Structure

### Section 1: Executive Summary
A 3-sentence overview for stakeholders who won't read the full report:
- Current state (coverage score + rating)
- Key finding (biggest waste area)
- Bottom line (monthly savings opportunity)

Example:
> "This account has a Negative Keyword Coverage Score of 38/100 (Poor). The primary waste driver is irrelevant informational queries consuming 18% of budget with zero conversions. Implementing the recommended negatives will save an estimated $3,200/month ($38,400/year)."

### Section 2: Negative Keyword Coverage Score

The overall health metric scored 0-100:

**Scoring Components:**

| Component | Weight | What It Measures | How It's Scored |
|-----------|--------|-----------------|-----------------|
| Search Term Relevance Rate | 30% | % of search terms classified as Relevant | 90%+ relevant = 100 points, linear scale down |
| N-Gram Coverage | 25% | % of high-waste N-grams already covered by existing negatives | Each uncovered high-waste N-gram reduces score |
| Conflict Absence | 15% | No negative-positive keyword conflicts exist | Each conflict reduces score by severity |
| Industry List Coverage | 15% | % of applicable industry negatives already in the account | Compare account negatives vs industry list |
| Match Type Accuracy | 15% | Existing negatives use appropriate match types | Each match type error reduces score |

**Score Interpretation:**
```
90-100  EXCELLENT  — Tight coverage, minimal waste. Maintain quarterly reviews.
70-89   GOOD       — Solid foundation. Address identified gaps within 2 weeks.
50-69   FAIR       — Significant waste. Prioritize top 20 negatives immediately.
30-49   POOR       — Major leakage. Expect 20-30% improvement from optimization.
0-29    CRITICAL   — Emergency intervention. Account is hemorrhaging budget.
```

### Section 3: Current Negative Keyword Inventory
Overview of what's already in the account:
- Total negative keywords count
- Breakdown by match type (broad/phrase/exact)
- Breakdown by level (account/campaign/ad group/shared list)
- Shared negative keyword lists and their campaign associations
- Date of last negative keyword addition (staleness indicator)

### Section 4: Top 50 Recommended Negatives

The most impactful negative keywords to add, prioritized by estimated monthly savings:

```
| Rank | Negative Keyword | Match Type | Monthly Waste | Search Terms Affected | Confidence |
|------|-----------------|------------|---------------|----------------------|------------|
| 1    | free            | Broad      | $340.20       | 47                   | HIGH       |
| 2    | jobs            | Broad      | $234.50       | 31                   | HIGH       |
| 3    | "how to"        | Phrase     | $189.30       | 23                   | HIGH       |
| 4    | salary          | Broad      | $156.80       | 18                   | HIGH       |
| 5    | "near me"       | Phrase     | $134.20       | 15                   | MEDIUM     |
| ...  | ...             | ...        | ...           | ...                  | ...        |
| 50   | certification   | Broad      | $12.40        | 3                    | MEDIUM     |
```

Each recommendation includes:
- The negative keyword to add
- Recommended match type with rationale
- Which campaigns/ad groups to apply it to
- Monthly waste this negative would eliminate
- Number of search terms it covers
- Confidence level (HIGH/MEDIUM/LOW)

### Section 5: Conflict Report

All detected negative-positive keyword conflicts:

- CRITICAL conflicts (blocking converting keywords) — listed first
- HIGH conflicts (blocking active keywords with impression/click history)
- MEDIUM conflicts (potential blocks based on keyword overlap)
- Resolution recommendation for each conflict

### Section 6: Industry List Recommendations

Based on the detected industry of the account:
- Matched industry: [Industry name]
- Industry list terms already in account: X of Y (Z%)
- Missing industry terms recommended for addition
- Universal negative coverage: X of 50 (Z%)

### Section 7: Cross-Campaign Analysis

Campaign structure assessment:
- Brand vs non-brand separation status
- Geographic campaign isolation status
- Funnel-stage separation status
- Cross-campaign cannibalization waste estimate

### Section 8: Waste Summary

Dollar-amount waste breakdown from `/negatives waste`:
- By category (irrelevant, competitor, informational, geographic, job seeker, cannibalization)
- Monthly total
- Annual projection
- Savings projection with recovery rate

### Section 9: Action Plan

Prioritized implementation roadmap:

```
WEEK 1 (Immediate — highest impact):
□ Add top 20 negative keywords (est. savings: $2,100/mo)
□ Resolve 3 CRITICAL conflicts
□ Apply universal negative list

WEEK 2 (High priority):
□ Add negatives #21-50 (est. savings: $780/mo)
□ Apply industry-specific negative list
□ Implement brand vs non-brand separation negatives

WEEK 3 (Optimization):
□ Resolve remaining conflicts
□ Set up cross-campaign negatives
□ Correct match type errors on existing negatives

ONGOING (Monthly maintenance):
□ Review search term report weekly for first month, then bi-weekly
□ Run /negatives ngram monthly on new search term data
□ Run /negatives conflicts quarterly
□ Update industry lists quarterly
```

### Section 10: Appendix

Raw data tables:
- Full N-gram analysis output
- Complete search term classification
- All conflicts with details
- Industry list gap analysis
- Match type audit results

## Report Generation Process

1. **Data Collection**: Gather search term reports, keyword lists, negative keyword lists, campaign structure
2. **Mining**: Run `/negatives mine` to classify all search terms
3. **N-Gram Analysis**: Run `/negatives ngram` to find waste patterns
4. **Conflict Detection**: Run `/negatives conflicts` to find blocks
5. **Industry Matching**: Run `/negatives lists` to identify industry and gaps
6. **Cross-Campaign**: Run `/negatives cross-campaign` to check structure
7. **Match Types**: Run `/negatives match-types` to audit existing negatives
8. **Waste Calculation**: Run `/negatives waste` to quantify everything
9. **Scoring**: Calculate Negative Keyword Coverage Score
10. **Assembly**: Compile all findings into the report format

## Usage

```bash
# Generate full audit report
/negatives report

# Generate report from CSV data
/negatives report path/to/search-terms.csv

# Generate report for specific date range
/negatives report --days 90

# Generate report for specific industry
/negatives report --industry saas

# Export report to file
/negatives report --output audit-report.md

# Generate report with competitor list
/negatives report --competitors "salesforce,hubspot,zoho"

# Quick report (skip cross-campaign analysis)
/negatives report --quick
```

## Report Delivery Formats

- **Markdown** — Default. Formatted for terminal or documentation.
- **CSV** — Negative keyword list only, ready for Google Ads upload.
- **PDF** — Formatted for client presentation (requires external PDF generation).
- **Google Sheets** — Structured for collaborative review with clients.

## Integration with All Skills

This report is the culmination of all sub-skills:
- `/negatives mine` provides search term classifications
- `/negatives ngram` provides waste patterns and N-gram tables
- `/negatives conflicts` provides conflict detection and resolution
- `/negatives lists` provides industry list matching and gap analysis
- `/negatives cross-campaign` provides campaign structure assessment
- `/negatives match-types` provides match type accuracy audit
- `/negatives waste` provides dollar-amount waste calculations
