---
name: audit-pmax
description: Audits Performance Max campaigns including asset group completeness, audience signal quality, URL expansion settings, PMax vs Search cannibalization, asset performance ratings, search themes, brand exclusions, and budget allocation recommendations.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Performance Max (PMax) Audit

## Overview

Performance Max is Google's AI-driven campaign type that runs across all Google inventory (Search, Display, YouTube, Gmail, Discover, Maps, Shopping). It replaces Smart Shopping and Local campaigns and uses machine learning to optimize across channels automatically.

PMax is powerful but opaque — it provides limited visibility into where budget is spent, which search terms trigger ads, and how the algorithm allocates across networks. This audit examines the controllable inputs (assets, audiences, settings) and analyzes available performance signals to ensure PMax is delivering incremental value.

**Key PMax truths:**
- PMax cannibalizes brand Search traffic by default (unless brand exclusions are set)
- PMax prioritizes easy conversions first (brand, remarketing) before prospecting
- Asset quality directly impacts which inventory PMax can access
- Audience signals are "suggestions" not "targeting" — PMax will go beyond them
- URL expansion is ON by default and can send traffic to irrelevant pages

## Audit Checks (20 Total)

### Asset Group Completeness (5 checks)

**Check 1: Text Asset Completeness**
- Pass: Each asset group has maximum text assets — 5 headlines (30 chars), 5 long headlines (90 chars), 5 descriptions (90 chars), 1 short description (60 chars), business name, call-to-action selection
- Fail: Asset groups with fewer than the recommended minimums (3 headlines, 2 long headlines, 2 descriptions)
- Scoring: 7 points
- Best practice: Fill all available text slots to give PMax maximum creative flexibility

**Check 2: Image Asset Completeness**
- Pass: Each asset group has required image assets — landscape (1.91:1, min 600x314), square (1:1, min 300x300), portrait (4:5, min 480x600); recommended 5+ of each ratio
- Fail: Missing image ratios or fewer than 3 images total
- Scoring: 6 points
- Impact: Missing landscape images blocks YouTube and Discover inventory; missing portrait blocks some Display placements

**Check 3: Video Asset Presence**
- Pass: Each asset group has at least one video asset (recommended: 1 horizontal, 1 vertical, 1 square; each 10+ seconds)
- Fail: No video assets (Google will auto-generate low-quality videos from images and text)
- Scoring: 6 points
- Critical: Auto-generated PMax videos are typically poor quality and can harm brand perception. Providing your own videos is strongly recommended.
- Minimum video specs: 10 seconds minimum, 15-30 seconds ideal, vertical (9:16) + horizontal (16:9) + square (1:1)

**Check 4: Logo Assets**
- Pass: Logo provided in both square (1:1, min 128x128) and landscape (4:1, min 512x128) formats
- Fail: Missing logo assets (reduces ad branding across Display and Video placements)
- Scoring: 3 points

**Check 5: Asset Group Count & Organization**
- Pass: Multiple asset groups organized by theme/product/service (not one catch-all asset group)
- Fail: Single asset group for the entire business (limits relevance scoring and optimization)
- Scoring: 5 points
- Best practice: Create asset groups similar to how you'd create ad groups — one per product category, service type, or audience segment
- Benchmark: 3-7 asset groups per PMax campaign for most businesses

### Audience Signal Quality (4 checks)

**Check 6: Custom Segments Setup**
- Pass: Custom segments configured with relevant search terms, competitor URLs, and app users
- Fail: No custom segments (PMax has zero guidance on ideal audience)
- Scoring: 6 points
- Custom segment types:
  1. Search-term based: Add your top-performing keywords and search terms
  2. URL-based: Add competitor websites, industry publications, relevant URLs
  3. App-based: Users of related apps
- Impact: Custom segments are the strongest audience signal — they tell PMax "find people like this"

**Check 7: First-Party Data (Your Data) Signals**
- Pass: Customer match lists (email lists), website visitors (remarketing), and converters uploaded as audience signals
- Fail: No first-party data signals (PMax can't learn from your best customers)
- Scoring: 5 points
- Best practice: Upload your customer list (even if small) — PMax uses it to find similar users, not just remarket

**Check 8: Interest & Demographic Signals**
- Pass: Relevant in-market audiences and demographic targeting applied as signals
- Fail: No interest-based signals or overly broad demographic targeting
- Scoring: 3 points
- Note: These are weaker signals than custom segments and customer data but still help guide initial optimization

**Check 9: Audience Signal Breadth**
- Pass: Multiple signal types combined (custom segments + your data + interests) for robust guidance
- Fail: Only one signal type or no signals at all
- Scoring: 3 points
- Rule: More signal types = faster PMax learning; fewer signals = more wasted spend during ramp-up

### URL Expansion & Search Themes (3 checks)

**Check 10: URL Expansion Setting**
- Pass: URL expansion is deliberately configured — either ON (for e-commerce with many product pages) or OFF (for lead gen with specific landing pages)
- Fail: URL expansion left at default (ON) for lead gen businesses, sending traffic to blog posts, about pages, or other non-conversion pages
- Scoring: 6 points
- Lead gen: Almost always turn URL expansion OFF and specify final URLs
- E-commerce: URL expansion ON can be beneficial for product discovery
- Check: Review the "landing page" report to see if PMax is sending traffic to unexpected URLs

**Check 11: Final URL Specifications**
- Pass: If URL expansion is OFF, specific final URLs are set for each asset group, matching the theme
- Fail: Generic homepage URL for all asset groups (misses relevance opportunity)
- Scoring: 4 points

**Check 12: Search Themes Configuration**
- Pass: Search themes (introduced 2023) are set with relevant keywords/topics to guide PMax's Search inventory behavior
- Fail: No search themes configured (PMax guesses what queries to target)
- Scoring: 4 points
- Limit: Up to 25 search themes per asset group
- Best practice: Use your top-performing Search campaign keywords as search themes

### PMax vs Search Cannibalization (3 checks)

**Check 13: Brand Exclusions**
- Pass: Brand terms excluded from PMax (using account-level brand exclusions or brand list) to prevent PMax from cannibalizing brand Search campaigns
- Fail: No brand exclusions — PMax likely capturing 30-60% of brand traffic and claiming credit for conversions that would happen anyway
- Scoring: 7 points
- This is the single most important PMax setting for accounts with brand Search campaigns
- How to check: Look at PMax insights → search categories for brand term presence; compare brand Search impression share before/after PMax launch

**Check 14: Incremental Conversion Analysis**
- Pass: Analysis performed to determine if PMax conversions are truly incremental (new customers) vs cannibalized from other campaigns
- Fail: PMax conversion volume taken at face value without incrementality assessment
- Scoring: 5 points
- Methods: Geographic lift test, holdback test, pre/post analysis of total account conversions after PMax launch
- Red flags: Total account conversions didn't increase after PMax launch, Search campaign performance declined

**Check 15: Search Campaign Performance Impact**
- Pass: Search campaign metrics (impressions, clicks, conversions) monitored before/after PMax launch
- Fail: No comparison — unable to assess cannibalization
- Scoring: 3 points
- Check: If Search impression share dropped after PMax launch without budget changes, PMax is likely cannibalizing

### Asset Performance & Optimization (3 checks)

**Check 16: Asset Performance Rating Review**
- Pass: Asset performance ratings (Best, Good, Low) reviewed and low-performing assets replaced or improved
- Fail: No performance review of individual assets; running same assets since launch
- Scoring: 5 points
- Action framework:
  - "Best" → Keep, create similar variations
  - "Good" → Keep, test improvements
  - "Low" → Replace with new creative
  - "Pending" → Needs more data (2-4 weeks typically)

**Check 17: Asset Group Performance Comparison**
- Pass: Performance compared across asset groups; underperformers optimized or restructured
- Fail: No asset-group-level performance analysis
- Scoring: 3 points

**Check 18: PMax Insights Review**
- Pass: PMax Insights tab reviewed regularly (search categories, audience segments, top-performing creatives)
- Fail: PMax running on autopilot with no insights review
- Scoring: 3 points
- Key insights to review: Search term categories (what queries PMax is matching), audience segment insights (who's converting), top combinations (which creative combos work)

### Budget & Performance (2 checks)

**Check 19: PMax Budget Allocation**
- Pass: PMax budget is appropriate relative to Search — typically 30-40% PMax / 60-70% Search for lead gen; varies for e-commerce
- Fail: PMax consuming majority of budget at worse CPA than Search (common when PMax cannibalizes brand)
- Scoring: 5 points
- Benchmark:
  - Lead gen starting point: 20-30% of total budget in PMax
  - E-commerce with feed: 40-60% in PMax (replaces Smart Shopping)
  - Scale as incrementality is proven

**Check 20: PMax CPA/ROAS vs Search Comparison**
- Pass: PMax CPA is within 20% of non-brand Search CPA (apples-to-apples, excluding brand)
- Fail: PMax CPA significantly better than Search (suspicious — likely capturing brand) or significantly worse (not optimizing well)
- Scoring: 4 points
- Warning: PMax CPA looks artificially good when it's capturing brand conversions at low cost — always compare to non-brand Search only

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | PMax fully optimized and driving incremental growth |
| 75-89 | Good | Well-configured PMax with specific improvement areas |
| 60-74 | Average | PMax running but potentially cannibalizing or underperforming |
| 40-59 | Below Average | Significant PMax configuration issues |
| 0-39 | Poor | PMax needs fundamental restructuring or may not be appropriate |

**Total possible points: 100**

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Asset completeness (all slots filled) | 100% | 80%+ | 60-80% | < 60% |
| Asset performance: "Best" rated | > 30% | 20-30% | 10-20% | < 10% |
| PMax incremental conversion % | > 70% | 50-70% | 30-50% | < 30% |
| PMax CPA vs non-brand Search | Within 20% | 20-40% higher | 40-60% higher | > 60% higher |
| Audience signals configured | 3+ types | 2 types | 1 type | 0 |
| Video assets provided | Yes (3 formats) | Yes (1 format) | Auto-generated | None |

## Output Format

```markdown
## Performance Max Audit Results

**Overall Score: [X]/100 — [Rating]**

### Asset Group Completeness
| Asset Group | Text | Images | Videos | Logos | Overall |
|-------------|------|--------|--------|-------|---------|
| Group 1 | 15/15 | 10/15 | 3/3 | 2/2 | 95% |
| ... | ... | ... | ... | ... | ... |

### Audience Signals
| Signal Type | Configured | Details |
|-------------|-----------|---------|
| Custom Segments | Yes/No | X segments, Y terms/URLs |
| Customer Match | Yes/No | X list size |
| Website Visitors | Yes/No | X list size |
| In-Market | Yes/No | X audiences |
| Demographics | Yes/No | ... |

### Cannibalization Assessment
- Brand exclusions: Active/Missing
- PMax brand traffic estimate: X%
- Search campaign IS change since PMax launch: +/-X%
- Incremental conversion estimate: X%

### Settings Review
| Setting | Current | Recommended |
|---------|---------|-------------|
| URL Expansion | ON/OFF | ... |
| Search Themes | X configured | ... |
| Brand Exclusions | Yes/No | ... |
| Final URLs | Specific/Homepage | ... |

### Budget Recommendation
- Current PMax budget: $X (Y% of total)
- Recommended: $X (Y% of total)
- Rationale: ...

### Recommendations
1. [Add brand exclusions]
2. [Provide video assets]
3. [Configure audience signals]
4. [Turn off URL expansion for lead gen]
```
