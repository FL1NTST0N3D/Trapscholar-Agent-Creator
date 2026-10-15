# Meta Placements Audit

## Command
`/meta placements`

## Description
Analyzes placement performance across Meta's ad network, evaluates Advantage+ Placements vs manual placement selection, reviews Feed vs Stories vs Reels vs Audience Network distribution, and validates placement-specific creative optimization. Proper placement strategy ensures budget flows to where it performs best while maintaining creative quality across surfaces.

## Why Placement Analysis Matters

Meta offers 15+ placement surfaces across Facebook, Instagram, Messenger, and Audience Network. Performance varies dramatically by placement:

- **CPM variance**: 3-5x difference between cheapest and most expensive placements
- **CTR variance**: 2-4x difference across placements for the same creative
- **Conversion quality**: Some placements drive clicks but not conversions (especially Audience Network)
- **Creative fit**: A 1:1 image looks great in Feed but poor in Stories (9:16 needed)
- **Brand safety**: Audience Network placements appear on third-party apps/sites with less brand control

## Audit Checklist (25 Points)

### 1. Advantage+ Placements vs Manual (5 points)

Meta recommends Advantage+ Placements (formerly Automatic Placements) for most campaigns. It lets Meta's algorithm distribute spend across placements for best results.

| Approach | Pros | Cons |
|----------|------|------|
| Advantage+ Placements | Lower CPMs, broader reach, algorithmic optimization | Less control, budget may go to low-quality placements |
| Manual Placements | Full control, brand safety, placement-specific creative | Higher CPMs, limited reach, may miss opportunities |

- [ ] **Placement Setting**: Document which campaigns use Advantage+ vs Manual
- [ ] **Advantage+ Justification**: If using Advantage+, verify creative works across all placements
- [ ] **Manual Justification**: If manual, verify there is a data-driven reason for excluded placements
- [ ] **Hybrid Approach**: Are some campaigns using Advantage+ for scale and others manual for testing?
- [ ] **Placement Performance Review**: Regardless of setting, review performance breakdown by placement

### 2. Placement Performance Analysis (8 points)

Pull placement-level data and analyze:

**Meta Placement Network:**

| Platform | Placement | Typical CPM | Best For |
|----------|-----------|------------|----------|
| Facebook | Feed | $10-15 | Awareness, conversions, all objectives |
| Facebook | Stories | $6-10 | Full-screen engagement, younger demo |
| Facebook | Reels | $5-9 | Video views, younger demo, UGC-style |
| Facebook | In-Stream Video | $7-12 | Video views, mid-roll attention |
| Facebook | Right Column | $2-5 | Retargeting (desktop only) |
| Facebook | Search Results | $4-8 | Intent-based queries |
| Facebook | Marketplace | $5-9 | E-commerce, local commerce |
| Instagram | Feed | $8-14 | Visual products, lifestyle brands |
| Instagram | Stories | $5-10 | Full-screen, swipe-up actions |
| Instagram | Reels | $4-8 | Short-form video, discovery |
| Instagram | Explore | $6-11 | Discovery, new audience reach |
| Messenger | Inbox | $5-8 | Retargeting, re-engagement |
| Messenger | Stories | $4-7 | Casual engagement |
| Audience Network | Banner/Interstitial | $2-5 | Cheap reach, low quality |
| Audience Network | Rewarded Video | $3-6 | Video views (gaming apps) |

- [ ] **CPM by Placement**: Identify most/least expensive placements
- [ ] **CTR by Placement**: Identify highest/lowest performing placements
- [ ] **Conversion Rate by Placement**: Flag placements with clicks but no conversions
- [ ] **Cost Per Conversion by Placement**: The true efficiency metric
- [ ] **Spend Distribution**: What % of budget goes to each placement?
- [ ] **Audience Network Evaluation**: Is Audience Network producing quality traffic or just cheap impressions?
- [ ] **Stories vs Feed Performance**: Compare KPIs between these two highest-volume placements
- [ ] **Reels Performance**: Are Reels placements being utilized? What is the performance?

### 3. Placement-Specific Creative (7 points)

Different placements require different creative specifications:

| Placement | Aspect Ratio | Max Duration | Text Overlay |
|-----------|-------------|-------------|-------------|
| Feed | 1:1 or 4:5 | 240 min | Keep < 20% |
| Stories/Reels | 9:16 | 15-60 sec | Include, overlay-style |
| Right Column | 1:1 | Image only | Minimal |
| In-Stream | 16:9 | 5-15 sec | Not applicable |
| Marketplace | 1:1 | 240 min | Product-focused |

- [ ] **Aspect Ratio Coverage**: Are 1:1, 4:5, and 9:16 versions of creative available?
- [ ] **Stories/Reels Creative**: Dedicated 9:16 creative exists (not cropped from Feed)
- [ ] **Video Length by Placement**: Stories videos < 15 sec, Reels < 30 sec, Feed flexible
- [ ] **Safe Zones**: Text and key elements within safe zones (UI elements cover edges in Stories/Reels)
- [ ] **Sound Design**: Videos have captions/text overlays for sound-off viewing (85% watch without sound)
- [ ] **Creative Preview**: Ads previewed in each placement to verify visual quality
- [ ] **Asset Customization**: Using Meta's placement asset customization feature to serve different creative per placement

### 4. Audience Network Assessment (5 points)

Audience Network extends Meta ads to third-party apps and websites. It can provide cheap reach but often lower quality.

- [ ] **AN Enabled/Disabled**: Document whether Audience Network is active
- [ ] **AN Spend %**: What percentage of budget goes to Audience Network?
- [ ] **AN Conversion Quality**: Compare AN conversion rate to Facebook/Instagram
- [ ] **AN Brand Safety**: Review where ads are appearing (publisher report)
- [ ] **AN Block Lists**: Is a publisher block list configured to exclude low-quality apps/sites?

**When to Use Audience Network:**
| Scenario | Recommendation |
|----------|---------------|
| Awareness/Reach campaigns | Enable — cheap impressions expand reach |
| Video view campaigns | Enable rewarded video — high completion rates |
| Conversion campaigns | Test, but monitor closely — often low quality |
| Brand-sensitive advertisers | Disable — limited control over placement context |
| E-commerce/Direct Response | Usually disable — low conversion quality |

## Placement Optimization Score

| Score Range | Grade | Interpretation |
|-------------|-------|---------------|
| 90-100 | A+ | Optimal placement strategy with creative for each surface |
| 80-89 | A | Good strategy, minor creative gaps |
| 70-79 | B | Decent placement mix, creative not optimized per placement |
| 60-69 | C | Over-reliance on one placement or missing creative sizes |
| 40-59 | D | Significant placement issues — budget flowing to poor performers |
| 0-39 | F | No placement strategy — default settings with no optimization |

## Common Issues & Fixes

### Issue: 80% of Budget Going to Facebook Feed
**Symptom**: Feed dominates spend, Stories and Reels get minimal budget
**Root Cause**: Creative only available in 1:1/4:5 — Stories/Reels require 9:16
**Fix**: Create dedicated 9:16 creative for Stories/Reels. Use asset customization to serve format-appropriate creative per placement.

### Issue: Audience Network Draining Budget with No Conversions
**Symptom**: AN gets 25% of budget, 0 conversions, low CPC but high bounce rate
**Root Cause**: Advantage+ Placements enabled with no placement-level performance review
**Fix**: Either exclude Audience Network from conversion campaigns or add publisher block list. Keep AN only for awareness.

### Issue: Stories Ads Using Feed Creative (Cropped)
**Symptom**: Stories ads show cropped 1:1 image with black bars — poor user experience
**Root Cause**: No 9:16 creative uploaded, Meta auto-crops the Feed creative
**Fix**: Upload dedicated 9:16 Stories creative. Use Meta's creative tools to create Stories versions.

### Issue: No Reels Presence
**Symptom**: Zero spend on Reels despite growing user base and lower CPMs
**Root Cause**: No short-form vertical video in the creative library
**Fix**: Create 15-30 second vertical videos. UGC-style content performs best on Reels.

## Output Format

```
## Placement Audit Results

**Score: XX/100** (Grade: X)
**Active Placements: X/15+**
**Placement Strategy: [Advantage+ / Manual / Mixed]**
**Creative Coverage: X/3 aspect ratios**

### Performance by Placement
| Placement | Spend % | CPM | CTR | Conv Rate | CPA | Grade |
|-----------|---------|-----|-----|-----------|-----|-------|
| FB Feed | 45% | $12.30 | 1.4% | 3.2% | $18 | A |
| IG Stories | 20% | $7.50 | 0.9% | 2.8% | $22 | B |
| IG Reels | 5% | $5.20 | 1.8% | 1.5% | $35 | C |
| Audience Network | 15% | $2.80 | 2.1% | 0.2% | $140 | F |

### Critical Findings (P0)
- [e.g., Audience Network consuming 15% budget with $140 CPA vs $18 Feed CPA]

### Recommendations
1. [Action item — e.g., Exclude Audience Network from conversion campaigns]
2. [Action item — e.g., Create 9:16 creative for Stories/Reels]
```
