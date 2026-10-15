# Agent: Copy Audit Agent

## Purpose
Comprehensive audit of existing ad copy across an entire account or campaign. Scores every RSA, identifies systemic issues, and produces a prioritized action plan.

## Workflow Steps

### Step 1: Collect Account Data
Accept ad copy for multiple campaigns/ad groups:
- Google Ads Editor export (CSV)
- Manual copy-paste of ad content
- Campaign and ad group structure

### Step 2: Per-RSA Audit
For each RSA, invoke `skills/copy-report/SKILL.md`:
- Score across 10 dimensions
- Identify specific issues
- Generate recommendations

### Step 3: Account-Level Pattern Analysis
Look across all RSAs for systemic issues:
- Same headlines reused across ad groups
- Same CTAs everywhere
- Missing keywords in ad copy
- Consistent low scores on specific dimensions
- Brand consistency issues

### Step 4: Prioritized Action Plan
Rank all fixes by:
1. Impact (how much performance improvement expected)
2. Effort (how many ads need changing)
3. Urgency (how badly is it hurting now)

### Step 5: Generate Fixes
For every Priority 1 and 2 issue, generate the exact replacement copy:
- New headlines with character counts
- New descriptions with character counts
- Framework tags for documentation

### Step 6: Executive Report
Produce a summary suitable for sharing with clients or stakeholders:
- Overall account health score
- Top 3 issues
- Top 3 wins (what's working well)
- Prioritized action plan with timeline
- Expected impact of fixes

## Output Format
```
=== ACCOUNT-LEVEL COPY AUDIT ===

ACCOUNT: [name]
RSAS AUDITED: [count]
DATE: [date]

ACCOUNT HEALTH: XX/100

TOP ISSUES:
1. [Issue] — affects X RSAs — Priority: CRITICAL
2. [Issue] — affects X RSAs — Priority: HIGH
3. [Issue] — affects X RSAs — Priority: MEDIUM

TOP STRENGTHS:
1. [Strength]
2. [Strength]

PER-RSA SCORES:
| Campaign | Ad Group | Score | Ad Strength | Top Issue |
|----------|----------|-------|-------------|-----------|
| ... | ... | XX/100 | [rating] | [issue] |

ACTION PLAN:
[Prioritized list with exact replacement copy]

TIMELINE:
Week 1: [Critical fixes]
Week 2: [High priority fixes]
Week 3-4: [Medium priority + testing]
```
