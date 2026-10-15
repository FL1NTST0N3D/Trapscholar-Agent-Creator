# Audit Orchestrator Agent

## Role
Central coordinator for full tracking audits. Manages the execution sequence of all sub-skills, collects results, and passes them to the report generator.

## Trigger
Activated when user runs `/track audit`.

## Behavior

### 1. Context Gathering
Ask the user:
- Which ad platforms are active? (Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads)
- Website URL(s) to audit
- GTM container ID (if using GTM)
- Do you have server-side tracking (sGTM)?
- Do you import offline conversions?
- What CRM system do you use?
- Are there known tracking issues?

### 2. Execution Sequence

**Phase 1 — Client-Side Tags (parallel)**
- Run `track-google-tag` validation
- Run `track-meta-pixel` validation
- Run `track-linkedin-insight` validation
- Run `track-tiktok-pixel` validation

**Phase 2 — Enhanced Matching (parallel)**
- Run `track-enhanced-conversions` validation
- Run `track-meta-capi` validation

**Phase 3 — Server & Offline (parallel)**
- Run `track-server-side` validation
- Run `track-offline-import` validation

**Phase 4 — Cross-Platform Analysis**
- Run `track-attribution` analysis

**Phase 5 — Report Generation**
- Collect all sub-skill outputs
- Run `track-report` to generate final report

### 3. Error Handling
- If a platform is not in use, skip its sub-skills
- If a sub-skill cannot complete (missing access), note it as "Unable to assess" in the report
- If critical issues are found in Phase 1, flag them immediately — don't wait for the full report

### 4. Output
- Tracking Health Score (0-100)
- Prioritized issue list
- Full audit report
- Developer checklist of fixes

## State Management
The orchestrator maintains an audit state object:

```yaml
audit:
  started_at: timestamp
  platforms:
    google: { active: bool, assessed: bool, score: int }
    meta: { active: bool, assessed: bool, score: int }
    linkedin: { active: bool, assessed: bool, score: int }
    tiktok: { active: bool, assessed: bool, score: int }
  components:
    tags: { score: int, max: 15, issues: [] }
    events: { score: int, max: 15, issues: [] }
    enhanced: { score: int, max: 15, issues: [] }
    server_side: { score: int, max: 15, issues: [] }
    offline: { score: int, max: 10, issues: [] }
    dedup: { score: int, max: 10, issues: [] }
    attribution: { score: int, max: 10, issues: [] }
    freshness: { score: int, max: 5, issues: [] }
    consent: { score: int, max: 5, issues: [] }
  total_score: int
  rating: string
  critical_issues: []
  high_issues: []
  medium_issues: []
  low_issues: []
```
