# Skill: Ad Intelligence (`/comp ads`)

## Purpose
Analyze competitor advertising activity across paid channels to understand their acquisition strategy, messaging themes, audience targeting, creative patterns, and estimated spend. Ad intelligence reveals what competitors are willing to pay money to say — making it one of the most honest signals of their strategic priorities. While organic content reflects what they want to be known for, paid advertising reveals what actually drives their revenue.

## When to Use
- Planning your own paid advertising strategy and need competitive benchmarks
- Noticing increased competitive pressure in your ad auctions
- Preparing a Google Ads Auction Insights analysis for a client
- Evaluating competitor messaging to identify differentiation opportunities
- Estimating competitor customer acquisition costs and budget allocation
- Preparing a competitive paid media report for stakeholders

## Framework: Multi-Channel Ad Intelligence

### Channel 1: Google Ads Analysis

**Auction Insights Parsing** (requires access to the user's Google Ads account data):
- **Impression Share**: What percentage of eligible impressions does each competitor capture?
- **Overlap Rate**: How often do you and the competitor appear in the same auction?
- **Position Above Rate**: How often does the competitor appear above your ad?
- **Top of Page Rate**: How often does the competitor appear at the top of the page?
- **Outranking Share**: Combined measure of position advantage

Build an Auction Insights summary table:
```
| Competitor | Imp. Share | Overlap Rate | Position Above | Top of Page | Outranking |
|------------|-----------|-------------|----------------|-------------|------------|
```

Trend analysis: Compare Auction Insights month-over-month to detect:
- New competitors entering the auction
- Competitors increasing/decreasing spend
- Seasonal patterns in competitive intensity
- Impact of your bid changes on competitive dynamics

**Search Ad Copy Analysis**:
- Collect competitor ad headlines and descriptions (use Google search directly)
- Identify recurring messaging themes (speed, price, features, trust, outcomes)
- Map CTA patterns (free trial, demo, buy now, learn more, get started)
- Note use of ad extensions (sitelinks, callouts, structured snippets, seller ratings)
- Analyze landing page alignment (does the ad promise match the landing page?)

**Keyword Strategy Estimation**:
- Branded terms: Are they bidding on your brand name? Are you bidding on theirs?
- Category terms: Which high-intent category keywords are they targeting?
- Long-tail coverage: How broad or narrow is their keyword strategy?
- Negative keyword gaps: Terms where they appear but probably shouldn't

### Channel 2: Meta (Facebook/Instagram) Ad Analysis

**Meta Ad Library Methodology** (ads.facebook.com/ads/library):
- Search by competitor name or page
- Document active ads: count, creative types, run dates
- Categorize creative formats: static image, video, carousel, stories, collection
- Analyze ad copy: headlines, primary text, CTA buttons
- Note targeting signals: "About this ad" disclosure shows some targeting info
- Track creative refresh rate: How often do they launch new ads?

Build a creative inventory:
```
| Ad ID | Format | Headline | CTA | Run Date | Status | Platform |
|-------|--------|----------|-----|----------|--------|----------|
```

**Creative Pattern Analysis**:
- **Visual themes**: Product screenshots, lifestyle imagery, testimonials, data/stats, comparison
- **Copy frameworks**: Problem-agitate-solve, benefit-led, feature-led, social proof, urgency
- **Offer types**: Free trial, discount, webinar, whitepaper, demo, free tool
- **Funnel stage**: Awareness (brand/education), consideration (comparison/features), conversion (offer/CTA)

### Channel 3: LinkedIn Ads
- Check competitor LinkedIn page for sponsored content
- Note content types: sponsored posts, message ads, document ads, video ads
- Identify targeting approach: job titles, industries, company sizes
- Analyze thought leadership vs direct response ratio

### Channel 4: Display & Programmatic
- Use tools like Moat.com or AdBeat for display ad examples (when available)
- Note publisher placements: which sites do their display ads appear on?
- Identify retargeting patterns: are they running retargeting campaigns?

### Spend Estimation Framework
Estimate competitor ad spend using available signals:

**Method 1 — Auction Insights Back-Calculation**:
If you know your own spend and impression share, estimate theirs:
`Competitor Spend ≈ (Your Spend / Your Impression Share) × Competitor Impression Share`

**Method 2 — SEMrush/SpyFu Data**:
Third-party tools provide estimated monthly spend, keyword count, and CPC data.

**Method 3 — Meta Ad Library Volume**:
High ad volume with frequent creative refresh indicates significant spend.

**Method 4 — LinkedIn Ad Frequency**:
Sponsored content frequency on LinkedIn correlates with spend level.

**Always note**: Spend estimates have wide confidence intervals. Present as ranges, not precise numbers.

### Messaging Theme Extraction
Across all channels, categorize messaging into themes:

| Theme | Description | Frequency | Example |
|-------|-------------|-----------|---------|
| Speed/Performance | "Faster than X" | High/Med/Low | |
| Price/Value | "Save X%" | | |
| Ease of Use | "Simple, intuitive" | | |
| Trust/Security | "Trusted by X" | | |
| Features | "Now with X" | | |
| Outcomes | "Achieve X" | | |
| Social Proof | "X customers" | | |
| Comparison | "Unlike X, we..." | | |

## Output Template

```markdown
# Ad Intelligence Report: [Competitor Name]
**Date**: [YYYY-MM-DD]
**Channels Analyzed**: [List]
**Data Sources**: [Auction Insights, Meta Ad Library, SEMrush, etc.]

## Executive Summary
- [Estimated monthly ad spend range]
- [Primary messaging theme]
- [Key competitive insight for your ad strategy]

## Google Ads Analysis
### Auction Insights Summary
[Table]
### Search Ad Copy Themes
[Analysis]
### Keyword Strategy
[Assessment]

## Meta/Social Ads Analysis
### Active Ad Count & Formats
[Inventory]
### Creative Patterns
[Analysis]
### Messaging Themes
[Theme table]

## Spend Estimation
| Channel | Low Estimate | Mid Estimate | High Estimate | Confidence |
|---------|-------------|-------------|---------------|------------|

## CTA Pattern Analysis
| CTA Type | Frequency | Channel | Funnel Stage |
|----------|-----------|---------|--------------|

## Strategic Implications
1. [What their ad strategy reveals about their priorities]
2. [Gaps in their advertising you can exploit]
3. [Messaging angles they own vs ones you can claim]

## Recommendations for Your Paid Strategy
1. [Specific action with expected impact]
2. [Messaging angle to test based on competitor gaps]
3. [Budget allocation recommendation]

## Data Confidence Notes
- [What's confirmed from direct observation vs estimated]
```

## Best Practices
1. Check the Meta Ad Library at least monthly — it is one of the most transparent sources of competitor intelligence available and it is free
2. Screenshot competitor ads with dates for historical tracking — creative patterns evolve and you need the timeline
3. Do not confuse impression share with market share; Auction Insights only shows the auctions you are eligible for
4. Look at competitor ad copy as a signal of what messaging resonates with shared audiences — they are A/B testing too
5. Combine ad analysis with landing page analysis for a complete picture of their conversion funnel
6. Track new competitor entrants in Auction Insights monthly — the first time a new name appears, investigate immediately
7. Remember that heavy ad spend on a feature or message often means their organic/product-led approach is not working for that angle
