# YouTube Ads Audit & Optimization Skill

## Command Router

This skill provides 9 specialized commands for YouTube advertising audit and optimization. Each command routes to a dedicated sub-skill with deep domain expertise.

### Command Reference

| Command | Sub-Skill | Description |
|---------|-----------|-------------|
| `/yt audit` | `yt-campaign-audit` | Full campaign audit across all dimensions |
| `/yt creative` | `yt-creative-scoring` | Video ad creative scoring with ABCD framework |
| `/yt targeting` | `yt-targeting-strategy` | Targeting strategy analysis and recommendations |
| `/yt shorts` | `yt-shorts-ads` | Shorts ad readiness and optimization |
| `/yt bumper` | `yt-bumper-ads` | 6-second bumper ad strategy |
| `/yt bidding` | `yt-bidding` | Bidding strategy analysis by objective |
| `/yt placements` | `yt-placements` | Placement hygiene and brand safety audit |
| `/yt remarketing` | `yt-remarketing` | Remarketing funnel and sequential messaging |
| `/yt report` | `yt-report` | Generate full audit report with scores |

## YouTube Campaign Type Reference

Understanding YouTube ad formats is foundational to any audit. Each format serves a different purpose and has different billing mechanics, creative requirements, and benchmarks.

| Type | Format | Billing | Max Length | Best For |
|------|--------|---------|------------|----------|
| Skippable In-Stream | Horizontal, skip after 5s | CPV | 15s - 3min (recommended) | Awareness + consideration |
| Non-Skippable In-Stream | Horizontal, no skip | CPM | 15s max | Guaranteed views, brand lift |
| Bumper | Horizontal, no skip | CPM | 6s max | Reach / frequency |
| Shorts | Vertical 9:16, swipeable | CPM | 15-60s | Mobile-first audiences |
| In-Feed (Discovery) | Thumbnail + text | CPC | Any length | Discovery / search intent |
| Demand Gen | Multi-format auto | CPA / tROAS | Varies | Conversions / ROAS |

### Format Selection Decision Tree

```
What is the primary objective?
├── Brand Awareness / Reach
│   ├── Need guaranteed views? → Non-Skippable In-Stream
│   ├── Need frequency at scale? → Bumper Ads
│   └── Targeting mobile-first? → Shorts Ads
├── Consideration / Engagement
│   ├── Want qualified viewers only? → Skippable In-Stream (CPV)
│   └── Want search/browse discovery? → In-Feed Ads
└── Conversions / Revenue
    ├── Have 30+ conversions/month? → Demand Gen (tCPA/tROAS)
    └── Building conversion data? → Skippable In-Stream + Max Conversions
```

### Campaign Structure Best Practices

**Naming Convention:**
```
[Client]_[Objective]_[Format]_[Audience]_[Creative]_[Date]
Example: AcmeCo_Awareness_Bumper_InMarket-SaaS_ProductDemo_2026Q1
```

**Budget Distribution by Objective:**
- **Awareness:** 60% Bumper/Non-Skip + 25% Shorts + 15% Skippable
- **Consideration:** 50% Skippable In-Stream + 30% In-Feed + 20% Shorts
- **Conversion:** 70% Demand Gen + 20% Skippable + 10% Remarketing

**Frequency Caps (Recommended):**
- Skippable In-Stream: 3-5 impressions per user per week
- Non-Skippable: 2-3 impressions per user per week
- Bumper: 5-7 impressions per user per week (they are short)
- Shorts: 3-4 impressions per user per week

### Audience Strategy Overview

YouTube offers the richest audience targeting in Google's ecosystem because it combines search intent data with viewing behavior:

1. **Custom Intent** — Target users based on their Google Search keywords. The most powerful YouTube audience type. Create audiences from keywords people searched on Google in the last 7-14 days.

2. **Affinity Segments** — Broad interest-based audiences. Good for awareness campaigns. Examples: "Tech Enthusiasts," "Cooking Enthusiasts," "Fitness Buffs."

3. **In-Market Segments** — Users actively researching or comparing products. High purchase intent. Examples: "In-Market for CRM Software," "In-Market for Travel."

4. **Life Events** — Major life changes trigger buying behavior. Examples: "Recently Moved," "Getting Married," "Starting a Business."

5. **Custom Segments** — Combine URLs, apps, and keywords to build hyper-specific audiences. Target users who visit competitor websites or use competitor apps.

6. **Remarketing** — Re-engage users who watched your videos, visited your channel, or interacted with your website.

7. **Similar/Lookalike** — Expand reach by targeting users similar to your converters or remarketing lists.

### Conversion Tracking Requirements

For any conversion-focused YouTube campaign, ensure:
- Google Ads conversion tracking is active (not just GA4 goals)
- View-through conversion window is set (recommended: 30 days for YouTube)
- Enhanced conversions are enabled for accurate attribution
- Consent mode v2 is implemented for EU traffic
- Offline conversion import is configured for lead gen businesses

### YouTube Ads Score Methodology

The YouTube Ads Score (0-100) is computed by auditing 8 weighted dimensions:

```
Score = (Structure × 0.15) + (Creative × 0.20) + (Targeting × 0.15) +
        (Bidding × 0.10) + (Placements × 0.10) + (Remarketing × 0.10) +
        (Shorts × 0.10) + (Measurement × 0.10)
```

Each dimension is scored 0-100 individually, then weighted. The sub-skills provide detailed scoring rubrics for each dimension.

### Data Requirements

To perform a full audit, request the following exports from Google Ads:

1. **Campaign Report** — Campaigns > Filter: Video > Columns: Campaign, Type, Status, Budget, Bid Strategy, Impressions, Views, View Rate, CPV, Clicks, CTR, Conversions, Cost/Conv, Cost
2. **Ad Group Report** — Ad Groups > Same columns + Audience segments
3. **Video Report** — Videos > Video title, Views, View Rate, Watch Time, Quartile metrics (25/50/75/100%)
4. **Audience Report** — Audiences > Segment name, Impressions, Views, View Rate, Conversions
5. **Placement Report** — Placements > Where ads showed > URL, Channel, Impressions, Cost
6. **Geographic Report** — Locations > Country/Region, Impressions, Views, Conversions
7. **Device Report** — Devices > Device type, Impressions, Views, View Rate, Conversions
