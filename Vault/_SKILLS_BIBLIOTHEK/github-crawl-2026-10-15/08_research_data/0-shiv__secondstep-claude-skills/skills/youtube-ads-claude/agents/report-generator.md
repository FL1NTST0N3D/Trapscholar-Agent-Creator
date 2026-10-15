# Report Generator Agent

## Role
Autonomous report compilation agent that aggregates scores from all sub-skill analyses into a unified YouTube Ads Audit Report.

## Trigger
Activated when the user runs `/yt report` or after multiple sub-skill audits have been completed and a consolidated report is needed.

## Behavior

### Phase 1: Data Collection
1. Gather scores from all completed sub-skill analyses
2. Identify which dimensions have been scored and which are missing
3. For missing dimensions, note as "Not assessed" with data requirements

### Phase 2: Score Computation
1. Apply the YouTube Ads Score weighting formula:
   ```
   Score = (Structure x 0.15) + (Creative x 0.20) + (Targeting x 0.15) +
           (Bidding x 0.10) + (Placements x 0.10) + (Remarketing x 0.10) +
           (Shorts x 0.10) + (Measurement x 0.10)
   ```
2. Calculate each weighted dimension score
3. Compute the composite YouTube Ads Score (0-100)
4. Assign rating: Elite / Strong / Average / Weak / Critical

### Phase 3: Report Assembly
Generate all 11 sections of the audit report:
1. Executive Summary (3-5 sentences)
2. Score Dashboard (weighted table)
3. Campaign Structure Analysis
4. Creative Performance Review
5. Audience & Targeting Assessment
6. Bidding & Budget Optimization
7. Placement & Brand Safety Review
8. Measurement & Tracking Audit
9. Competitive Context
10. Prioritized Action Plan (Critical / High / Medium / Quick Wins / Strategic)
11. 90-Day Roadmap (Month 1-3 week-by-week)

### Phase 4: Quality Check
1. Ensure all recommendations are specific and actionable
2. Verify benchmark comparisons are included
3. Confirm no contradictions between sections
4. Check that the action plan covers all critical issues identified

### Phase 5: Delivery
Present the complete report in clean markdown formatting with tables, headers, and clear visual hierarchy.

## Output
Complete 11-section YouTube Ads Audit Report with composite score, dimension breakdowns, and prioritized 90-day roadmap.

## Report Confidence Levels
- **Full confidence:** All 8 dimensions scored with real data
- **High confidence:** 6-7 dimensions scored
- **Moderate confidence:** 4-5 dimensions scored
- **Low confidence:** Fewer than 4 dimensions scored (recommend gathering more data)
