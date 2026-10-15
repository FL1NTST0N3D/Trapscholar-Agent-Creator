# QS Optimizer — Actionable Optimization Playbook

## Command
`/qs optimize`

## Purpose

Produce a comprehensive, prioritized optimization playbook that takes an account from its current Quality Score state to the target state. This is the action plan that ties together findings from all other QS sub-skills into a sequenced execution roadmap.

## Optimization Philosophy

Quality Score optimization follows a strict priority order based on impact-per-effort:

1. **Fix landing pages first** — One landing page fix can improve QS for dozens of keywords simultaneously. Highest leverage.
2. **Restructure ad groups second** — Tighter themes improve both Ad Relevance and Expected CTR. Structural foundation.
3. **Rewrite ad copy third** — Targeted ad rewrites improve Ad Relevance and CTR. Lower effort per keyword.
4. **Add extensions fourth** — Extensions improve Expected CTR with minimal effort. Often overlooked.
5. **Clean up match types fifth** — Negative keywords and match type tightening improve CTR by eliminating irrelevant impressions.
6. **Monitor and iterate** — QS changes take 2-4 weeks to materialize. Patience is part of the strategy.

## The 30-60-90 Day Plan

### Days 1-30: Foundation Fixes

**Week 1: Landing Page Speed**
- Run PageSpeed Insights on all unique landing pages
- Prioritize pages with LCP > 4 seconds (critical) and > 2.5 seconds (needs improvement)
- Common quick fixes:
  - Compress and convert images to WebP format
  - Enable gzip/brotli compression on server
  - Defer non-critical JavaScript
  - Remove unused CSS
  - Set up browser caching headers
  - Enable CDN if not already active
- Expected impact: 1-2 QS point improvement on keywords with Below Average Landing Page Experience
- Timeline for QS update: 2-4 weeks after page speed improvements go live

**Week 2: Landing Page Content and Mobile**
- Audit landing pages for content relevance to their keyword groups
- Ensure each major keyword theme has a dedicated landing page (not all traffic to homepage)
- Check mobile responsiveness on top 5 landing pages
- Add trust signals: reviews, certifications, contact information, privacy policy links
- Fix any broken forms, dead links, or navigation issues

**Week 3: Ad Group Restructuring**
- Identify ad groups with 15+ keywords — these are restructuring candidates
- For each oversized ad group:
  - Export all keywords
  - Cluster by semantic theme (3-8 keywords per new ad group)
  - Create new ad groups with theme-specific names
  - Write dedicated ads for each new ad group (keyword in Headline 1)
  - Add cross-negatives between related ad groups
  - Pause (do not delete) the original ad group
- Start with the top 5 ad groups by spend

**Week 4: Ad Copy Optimization**
- For all ad groups with Below Average Ad Relevance:
  - Ensure the primary keyword appears in Headline 1
  - Ensure the keyword theme appears in at least one description
  - For RSAs: aim for 12-15 headlines with good keyword coverage
  - Pin the best keyword-containing headline to Position 1
  - Add at least 4 unique description lines

### Days 31-60: Performance Optimization

**Week 5-6: Extension Buildout**
- Audit extension coverage across all campaigns:
  - Sitelinks: 4-6 per campaign, relevant to the campaign's theme
  - Callouts: 4-6 highlighting unique selling points
  - Structured Snippets: 2-3 with relevant categories
  - Call extensions: for all campaigns where phone calls are valuable
  - Location extensions: for all local service campaigns
  - Price extensions: where pricing is competitive
  - Image extensions: add product or service images where available
- Extensions should be set at the campaign level, with ad group overrides for key groups

**Week 7-8: Match Type and Negative Keyword Cleanup**
- Review Search Terms report for last 90 days
- Identify irrelevant search terms triggering your ads (CTR killers)
- Add negative keywords at campaign and ad group level
- Consider tightening match types:
  - Move high-spend broad match keywords to phrase or exact match
  - Keep broad match only with robust negative keyword lists
  - Create separate campaigns for broad match with tighter budget controls
- Expected impact: Improved CTR by eliminating low-quality impressions

### Days 61-90: Fine-Tuning and Scaling

**Week 9-10: Device and Geographic Optimization**
- Analyze CTR by device type (desktop, mobile, tablet)
- Set bid adjustments for underperforming devices
- Create device-specific ad copy where significant CTR differences exist
- Analyze CTR by geographic region
- Adjust geo bid modifiers for regions with lower CTR
- Consider dedicated campaigns for high-volume geographic areas

**Week 11-12: Testing and Monitoring**
- Review QS changes from Days 1-30 fixes (should be visible by now)
- A/B test new ad copy against current best performers
- Test new headline angles: questions, numbers, urgency, social proof, authority
- Set up automated QS tracking (weekly export or Google Ads script)
- Document QS changes and correlate with specific actions taken
- Identify next wave of optimization targets

## Optimization Tactics Reference

### For Below Average Expected CTR

| Tactic | Effort | Impact | Timeline |
|:--|:--:|:--:|:--|
| Add missing extensions | Low | Medium | 1-2 days |
| Add negative keywords from search terms | Low | Medium | 1-2 days |
| Rewrite ad headlines with stronger hooks | Medium | High | 3-5 days |
| Pin best headline to Position 1 in RSAs | Low | Low-Medium | 1 day |
| Create device-specific ad variations | Medium | Medium | 3-5 days |
| Tighten match types | Medium | Medium | 1-2 weeks |
| Restructure ad groups for tighter themes | High | High | 2-3 weeks |

### For Below Average Ad Relevance

| Tactic | Effort | Impact | Timeline |
|:--|:--:|:--:|:--|
| Add keyword to Headline 1 | Low | High | 1 day |
| Add keyword to Description 1 | Low | Medium | 1 day |
| Split oversized ad groups into STAGs | Medium | Very High | 1-2 weeks |
| Use DKI for ad groups with 3-5 similar keywords | Low | Medium | 1 day |
| Write dedicated ads per ad group | Medium | High | 3-5 days |
| Cross-negative between related ad groups | Low | Medium | 1-2 days |

### For Below Average Landing Page Experience

| Tactic | Effort | Impact | Timeline |
|:--|:--:|:--:|:--|
| Compress images, enable caching | Low | High | 1-2 days |
| Fix mobile responsiveness issues | Medium | High | 3-5 days |
| Add H1 heading with keyword | Low | Medium | 1 day |
| Add substantive content (500+ words) | Medium | High | 3-5 days |
| Add trust signals (reviews, certifications) | Low | Medium | 1-2 days |
| Create dedicated landing pages per theme | High | Very High | 2-4 weeks |
| Enable CDN | Low | Medium | 1 day |
| Fix redirect chains | Low | Low-Medium | 1 day |

## The Keyword Triage Decision Tree

For every keyword with QS below 7, follow this decision tree:

```
Is the keyword converting profitably?
├── YES → Optimize: Improve QS to reduce CPC and increase profit margin
│   ├── QS 5-6 → Incremental fixes (ad copy, extensions, minor LP improvements)
│   ├── QS 3-4 → Structural fixes (ad group restructure, new landing page)
│   └── QS 1-2 → Major rebuild (new ad group, new ads, dedicated LP) or...
│               └── Consider pausing and recreating to reset QS history
│
└── NO → Is the keyword strategically important?
    ├── YES → Optimize aggressively: this keyword needs to work
    │   └── Full treatment: new ad group, new ads, new landing page
    └── NO → Pause the keyword
        └── Reallocate budget to high-QS, converting keywords
```

## Tracking Optimization Progress

Set up a weekly tracking spreadsheet:

| Metric | Baseline (Day 0) | Week 2 | Week 4 | Week 8 | Week 12 |
|:--|:--:|:--:|:--:|:--:|:--:|
| Weighted Avg QS | | | | | |
| % Keywords QS 7+ | | | | | |
| % Keywords QS 1-4 | | | | | |
| Monthly QS waste ($) | | | | | |
| Avg CPC | | | | | |
| Total conversions | | | | | |
| Cost per conversion | | | | | |

## Output Format

1. **Current State Summary** — Where the account stands today
2. **Target State** — Where it should be in 90 days
3. **30-60-90 Day Action Plan** — Sequenced, specific tasks with owners and deadlines
4. **Quick Wins List** — Actions that can be completed this week
5. **Resource Requirements** — What is needed (developer time, copywriter, landing page builder)
6. **Expected Impact Timeline** — When QS improvements should start appearing
7. **Risk Factors** — What could prevent improvements (competitor activity, seasonal changes, budget constraints)
