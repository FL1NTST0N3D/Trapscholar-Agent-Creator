# YouTube Remarketing Skill

**Command:** `/yt remarketing`

## Purpose

Analyzes and optimizes YouTube remarketing strategy across video engagement, website visitors, and customer lists. YouTube remarketing is uniquely powerful because video engagement signals are far richer than page views — a user who watched 75% of your 2-minute product demo is categorically more interested than someone who bounced from your homepage in 3 seconds. This skill evaluates remarketing list strategy, sequential messaging, and cross-platform integration.

## YouTube Remarketing List Types

### 1. Video Viewer Lists

YouTube automatically creates engagement-based audiences from your video content. These are the richest remarketing signals available:

| List Type | Signal Strength | Typical Size | Best Use |
|-----------|----------------|--------------|----------|
| Watched any video (as ad) | Low | Large | Broad retargeting awareness |
| Watched specific video(s) | Medium | Medium | Content-specific follow-up |
| Watched 25% of video | Low-Medium | Large | Light engagement, show more content |
| Watched 50% of video | Medium | Medium | Moderate interest, deeper messaging |
| Watched 75% of video | High | Smaller | Strong interest, push toward conversion |
| Watched 100% of video | Very High | Smallest | Highest intent, direct CTA |
| Liked a video | High | Small | Brand advocates, upsell/cross-sell |
| Commented on a video | Very High | Very Small | Super-engaged, invite to community |
| Shared a video | Very High | Very Small | Potential brand ambassadors |

**Best Practices:**
- Create separate lists for 25%, 50%, 75%, and 100% completion
- Use 75%+ completion as your primary high-intent remarketing list
- Set membership duration to 30-90 days (match your sales cycle)
- For long sales cycles (B2B), extend to 180 days
- Exclude converters from all remarketing lists to avoid wasting budget

**Scoring (0-25 points):**
- 4+ tiered video viewer lists with appropriate durations: 25 points
- 1-2 basic video viewer lists: 12 points
- No video viewer remarketing: 0 points

### 2. Channel Subscriber Lists

Subscribers are your most loyal YouTube audience. Remarketing to them is cheap (high relevance score) and effective:

**Strategy:**
- Promote new products/features to existing subscribers
- Use subscriber lists as a seed for Similar Audiences
- Exclude subscribers from brand awareness campaigns (they already know you)
- Create subscriber-exclusive offers to reward loyalty and drive conversion

**Scoring (0-10 points):**
- Subscriber list active with dedicated campaigns: 10 points
- Subscriber list exists but unused: 5 points
- Not utilizing subscriber data: 0 points

### 3. Website Visitor Lists (Google Ads Tag)

Combine YouTube remarketing with website visitor data for powerful cross-platform retargeting:

| List | Duration | Strategy |
|------|----------|----------|
| All website visitors | 30 days | Show brand reinforcement bumpers |
| Product page viewers | 60 days | Show product demo in-stream ads |
| Cart abandoners | 14 days | Show urgency-driven short ads |
| Blog readers | 90 days | Show thought leadership content |
| Pricing page visitors | 30 days | Show case studies and testimonials |
| Converters | 180 days | Exclude from acquisition, show upsell |

**Scoring (0-20 points):**
- 3+ segmented website lists with YouTube campaigns: 20 points
- Basic "all visitors" list only: 8 points
- No website remarketing integration: 0 points

### 4. Customer Match Lists

Upload your CRM email lists to Google Ads for direct customer targeting on YouTube:

**High-Value Lists:**
- Paying customers (upsell/cross-sell campaigns)
- Trial users who did not convert (conversion recovery)
- Newsletter subscribers (nurture with video content)
- Event attendees (post-event follow-up)
- Lapsed customers (win-back campaigns)

**Requirements:**
- Minimum list size: 1,000 matched emails for YouTube targeting
- Match rate: Typically 30-60% (Gmail users match highest)
- Refresh lists monthly for accuracy
- Hash emails before upload (Google Ads does this automatically)

**Scoring (0-15 points):**
- Customer Match active with 2+ segmented lists: 15 points
- One Customer Match list uploaded: 8 points
- No Customer Match: 0 points

### 5. Similar/Lookalike Audiences

Google can create audiences similar to your remarketing lists and customer lists:

**Best Seed Lists for Similar Audiences:**
1. Converters (highest quality signal)
2. 75%+ video completion viewers
3. Customer Match — high-LTV customers
4. Pricing page visitors

**Best Practices:**
- Only use Similar Audiences in prospecting campaigns (not remarketing)
- Layer with demographic and geographic filters
- Monitor performance closely — Similar Audiences can be broad
- Minimum seed list size: 1,000 users

**Scoring (0-10 points):**
- Similar Audiences active from high-quality seed lists: 10 points
- Not utilizing Similar Audiences: 3 points

## Sequential Messaging Strategy

Sequential messaging shows different ads to users based on their previous interactions. This is the most sophisticated YouTube remarketing tactic:

### Funnel-Based Sequencing

```
Stage 1: Cold Audience (No previous interaction)
  Ad: 60-second brand story / problem-aware content
  Format: Skippable In-Stream
  Goal: Generate video views and build remarketing lists

Stage 2: Warm Audience (Watched 50%+ of Stage 1 ad)
  Ad: 30-second product demo / solution-aware content
  Format: Skippable In-Stream or In-Feed
  Goal: Drive website visits and product consideration

Stage 3: Hot Audience (Visited website after Stage 2)
  Ad: 15-second testimonial / social proof
  Format: Non-Skippable or Bumper sequence
  Goal: Build trust and reduce objections

Stage 4: Ready to Convert (Pricing page visitor / cart abandoner)
  Ad: 6-second bumper with offer + urgency
  Format: Bumper
  Goal: Drive conversion with final push

Stage 5: Customer (Converted)
  Ad: Upsell/cross-sell or referral request
  Format: In-Feed or Shorts
  Goal: Increase LTV and generate referrals
```

### Sequential Setup in Google Ads

1. Create Video Ad Sequencing campaign
2. Define audience entry point (cold or warm)
3. Set sequence steps with specific creatives per step
4. Configure impression-based advancement (user must see step N before step N+1)
5. Set frequency caps between steps (48-72 hours recommended)
6. Exclude users who converted at any stage

### Cross-Platform Remarketing Integration

YouTube remarketing becomes most powerful when combined with other Google properties:

**YouTube + Google Search Remarketing:**
- Show search ads to users who watched your YouTube ads (RLSA)
- Bid 30-50% higher on search for YouTube viewers (they already know your brand)
- This combination consistently delivers 20-40% lower CPA than search-only

**YouTube + Display Remarketing:**
- Show display ads as a reminder between YouTube ad exposures
- Use display for frequency fill between YouTube sequence steps
- Display CPMs are lower than YouTube — efficient for maintaining presence

**YouTube + Gmail Ads:**
- Target video viewers with Gmail sponsored promotions
- Effective for B2B where decision-makers check email frequently

## Remarketing Budget Allocation

**Rule of Thumb:**
- 15-25% of total YouTube budget should go to remarketing campaigns
- Remarketing CPA is typically 40-60% lower than prospecting CPA
- Over-investing in remarketing limits new audience growth (diminishing returns above 30% of budget)

## Composite Remarketing Score

```
Remarketing Score = Video Viewer Lists (25) + Subscriber Lists (10) +
                    Website Lists (20) + Customer Match (15) +
                    Similar Audiences (10) + Sequential Strategy (10) +
                    Cross-Platform Integration (10)
Maximum: 100 points
```

## Output Format

```
## Remarketing Analysis: [Score]/100

### Remarketing List Inventory
| List Type | Status | Size | Duration | Campaign Active |
|-----------|--------|------|----------|----------------|
| Video 75%+ viewers | | | | |
| Website visitors | | | | |
| Customer Match | | | | |
| Subscribers | | | | |

### Sequential Messaging Assessment
- Current: [Describe current approach]
- Funnel stages covered: [X of 5]
- Gap: [Missing stages]

### Cross-Platform Integration
- Search RLSA: Active / Missing
- Display remarketing: Active / Missing
- Gmail ads: Active / Missing

### Recommendations
1. [List creation priorities]
2. [Sequential messaging plan]
3. [Cross-platform integration steps]
4. [Budget reallocation]
```
