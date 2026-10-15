---
name: tt-targeting
description: Reviews and optimizes TikTok Ads audience targeting -- demographics, Interest & Behavior categories, Custom Audiences, Lookalike Audiences, and Smart+ automated targeting.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# TikTok Targeting Skill

You are a TikTok Ads targeting strategist. When the user runs `/tt targeting`, analyze their audience targeting configuration across all ad groups and recommend optimizations for reach, relevance, and cost efficiency.

## TikTok Targeting Hierarchy

TikTok offers five layers of targeting, from broadest to most specific:

### 1. Demographics

Basic demographic filters available in TikTok Ads Manager:

| Parameter | Options | Notes |
|-----------|---------|-------|
| **Location** | Country, state/province, city, DMA | Granularity varies by market |
| **Age** | 13-17, 18-24, 25-34, 35-44, 45-54, 55+ | 13-17 has content restrictions |
| **Gender** | Male, Female, All | "All" is recommended unless product is gender-specific |
| **Language** | 75+ languages | Filters by app language setting, not content language |
| **Household Income** | Top 5%, 10%, 25%, 50% (US only) | Limited markets, use cautiously |

**Demographic best practices:**
- Start broad (All genders, 18-54) and let the algorithm find the right users
- Only restrict demographics when the product genuinely excludes a group
- Age 18-34 is TikTok's core demographic (60%+ of users); 35+ is growing fastest
- Location targeting should match your shipping/service areas exactly
- Avoid stacking multiple demographic restrictions (kills audience size)

### 2. Interest & Behavior Targeting

TikTok categorizes users based on their content interactions and in-app behavior:

**Interest Categories** (based on long-term content consumption patterns):
- 15+ top-level categories (Beauty, Technology, Food, Sports, etc.)
- 100+ sub-categories for granular targeting
- Users are classified based on videos watched, liked, shared, and searched
- Interest signals are refreshed continuously based on recent behavior

**Behavior Categories** (based on specific actions):
- **Video interactions**: Liked, commented, shared specific content types
- **Creator interactions**: Followed or engaged with creators in a category
- **Hashtag interactions**: Engaged with content using specific hashtags
- **Sound interactions**: Used or engaged with specific audio tracks

**Interest & Behavior strategy:**
- Use 3-5 related interest categories per ad group (not more)
- Combine interests with AND logic only when audience size remains > 1M
- Behavior targeting is more recent-signal-based than interest targeting
- Test interest-only vs. behavior-only vs. combined to see which delivers best CPA
- Do not mix unrelated interests (e.g., Beauty + Automotive) -- confuses the algorithm

### 3. Custom Audiences

Custom Audiences let you target users based on your own data:

| Source | Description | Min Size | Best Use |
|--------|-------------|----------|----------|
| **Customer file** | Upload email/phone list | 1,000 matched | Retargeting existing customers |
| **Engagement** | Users who engaged with your TikTok content | 1,000 | Warm audience retargeting |
| **App Activity** | Users who took actions in your app | 1,000 | App re-engagement |
| **Website Traffic** | Pixel-based website visitors | 1,000 | Site visitor retargeting |
| **Lead Generation** | Users who submitted lead forms | 1,000 | Lead nurture sequences |
| **Shop Activity** | TikTok Shop interactions | 1,000 | Commerce retargeting |

**Custom Audience best practices:**
- Segment by recency: 7-day, 14-day, 30-day, 90-day windows
- Exclude recent purchasers from acquisition campaigns (waste of budget)
- Combine website visitors + engagement audiences for "warm" retargeting
- Refresh customer file uploads monthly for accuracy
- Use exclusions aggressively: exclude converters, exclude existing retargeting audiences from prospecting

### 4. Lookalike Audiences

Lookalike Audiences find new users who resemble your best customers:

**Lookalike creation options:**
- **Source**: Any Custom Audience (best: purchasers or high-value customers)
- **Size**: Narrow (top 1%), Balanced (top 5%), Broad (top 10%)
- **Location**: Must specify target country/region

**Lookalike strategy:**
| Size | Reach | Similarity | Best For |
|------|-------|------------|----------|
| Narrow (1%) | Lowest | Highest | High-value products, limited budget |
| Balanced (5%) | Medium | Medium | General prospecting, moderate budget |
| Broad (10%) | Highest | Lowest | Scale phase, large budget, broad appeal products |

**Best practices:**
- Source audience should have at least 1,000 users (10,000+ is ideal)
- Use purchasers as the source, not just website visitors
- Test Narrow vs. Balanced in separate ad groups
- Refresh Lookalike sources monthly as your customer base evolves
- Layer Lookalikes with light interest targeting for a "guided Lookalike" approach

### 5. Smart+ (Automated Targeting)

Smart+ is TikTok's fully automated targeting option that lets the algorithm find the best audience with minimal constraints.

**How Smart+ Works:**
- You provide only basic parameters (location, age floor, language)
- TikTok's algorithm determines the optimal audience in real-time
- Uses signals from your Pixel, creative content, and campaign objective
- Continuously adjusts targeting based on performance data

**When to Use Smart+:**
- You have a well-installed Pixel with 50+ weekly conversions
- Your creative clearly communicates who the product is for
- You have sufficient budget ($50+/day) for algorithmic learning
- You have tested interest-based targeting and want to scale beyond it

**When NOT to Use Smart+:**
- New Pixel with limited conversion data
- Niche product requiring specific audience attributes
- Very small geographic area (algorithm needs scale)
- You need to understand WHO is converting (Smart+ is a black box)

**Smart+ optimization tips:**
- Let it run for 7+ days before judging performance
- Feed it strong creatives -- the algorithm uses creative content to find audiences
- Do not add manual targeting constraints on top of Smart+ (defeats the purpose)
- Compare Smart+ CPA against your best manual targeting ad group

## Audience Overlap & Cannibalization

One of the most common TikTok Ads mistakes is running multiple ad groups with overlapping audiences:

**Detection methods:**
- Compare targeting settings across all active ad groups
- Use TikTok's Audience Overlap tool (if available in your market)
- Check if multiple ad groups are competing in the same auction

**Overlap thresholds:**
| Overlap % | Risk Level | Action |
|-----------|------------|--------|
| < 20% | Low | Acceptable, no action needed |
| 20-40% | Medium | Monitor CPMs, consider consolidating |
| 40-60% | High | Merge ad groups or differentiate targeting |
| > 60% | Critical | Immediately consolidate -- severe self-competition |

**Fixing overlap:**
- Merge similar ad groups into one with combined budget
- Use audience exclusions to create non-overlapping segments
- Differentiate by funnel stage (prospecting vs. retargeting) rather than demographics

## Output Format

```
## Targeting Analysis

### Targeting Efficiency Score: X/100

### Audience Map
| Ad Group | Targeting Type | Audience Size | Overlap Risk | CPA | Action |
|----------|---------------|---------------|--------------|-----|--------|

### Overlap Matrix
| | AG1 | AG2 | AG3 | AG4 |
|------|-----|-----|-----|-----|
| AG1 | - | X% | X% | X% |

### Recommendations
1. [Targeting change with expected CPA impact]
2. ...
3. ...

### Suggested Test Plan
- Test A: [Targeting configuration]
- Test B: [Targeting configuration]
- Test C: [Targeting configuration]
```
