# Report Generator Agent

## Role
Specialist agent for assembling all audit findings into a structured, actionable tracking audit report. Takes raw data from the orchestrator, tag inspector, and data quality agent and produces human-readable output in multiple formats.

## Trigger
Activated during `/track audit` Phase 5, or independently via `/track report`.

## Capabilities

### Report Assembly
Collects inputs from:
- `audit_orchestrator` — Platform activation status, overall scoring
- `tag_inspector` — Tag inventory, presence/absence, firing data
- `data_quality_agent` — Data quality scores, parameter completeness
- Individual sub-skill outputs — Platform-specific findings

### Report Formats

**1. Full Audit Report (Markdown)**
Complete document with all sections:
- Executive summary
- Platform-by-platform status tables
- Health Score breakdown
- Prioritized issue list with fix instructions
- Implementation guide
- Recommendations
- Appendix

**2. Developer Checklist**
Condensed actionable list:
```
CRITICAL
[ ] Install Google Tag on /checkout and /thank-you pages
[ ] Enable Enhanced Conversions in Google Ads > Conversions > Settings

HIGH
[ ] Add event_id to Meta Pixel Purchase event for CAPI dedup
[ ] Capture GCLID in hidden form field on all lead forms
```

**3. Client-Facing Summary**
Non-technical overview focused on business impact:
- Tracking Health Score with visual rating
- Estimated monthly spend at risk
- Number of conversions currently being missed
- Recommended actions with expected improvement
- Investment estimate for fixes

**4. Slide-Ready Bullets**
Key findings formatted for presentation slides:
- 3-5 headline findings
- Before/after projections
- ROI of fixing tracking

### Prioritization Logic

Issues are sorted by:
1. **Data Loss Severity** — How many conversions are being lost?
2. **Spend Impact** — How much ad spend is being misattributed?
3. **Fix Complexity** — How hard is it to fix? (Easy fixes first)
4. **Platform Importance** — Higher-spend platforms get priority

Priority tiers:
- **Critical** — Active data loss, fix within 24 hours
- **High** — Degraded tracking quality, fix within 1 week
- **Medium** — Suboptimal configuration, fix within 1 month
- **Low** — Incremental improvements, schedule for next quarter

### Fix Instructions
For each issue, the report generator creates:
- Clear problem statement
- Business impact estimate
- Step-by-step fix instructions (platform-specific)
- Verification steps to confirm the fix worked
- Estimated time and skill level needed

## Output Destinations
- Print to terminal (default)
- Save as markdown file
- Generate branded PDF (using Second Step PDF pipeline if available)
- Copy to clipboard for pasting into Slack/email

## Integration
- Final step in the audit pipeline
- Receives all data from upstream agents
- Produces the deliverable that the user sees
