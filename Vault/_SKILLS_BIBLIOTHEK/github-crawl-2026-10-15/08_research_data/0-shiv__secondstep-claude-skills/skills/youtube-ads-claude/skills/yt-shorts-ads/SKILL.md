# YouTube Shorts Ads Skill

**Command:** `/yt shorts`

## Purpose

Evaluates and optimizes YouTube Shorts ad campaigns. Shorts is YouTube's fastest-growing format, now accounting for 22% of total YouTube ad revenue and growing rapidly. With 70 billion daily views, Shorts represents the largest untapped opportunity in YouTube advertising for most brands. This skill assesses Shorts-specific creative requirements, audience strategy, and performance optimization.

## Shorts Ads Landscape (2026)

### Key Statistics
- **70 billion daily Shorts views** globally
- **22% of YouTube ad revenue** now comes from Shorts (up from 0% in 2023)
- **Shorts CPM averages ~$4** — significantly cheaper than In-Stream ($6-$12)
- **2 billion+ logged-in users** watch Shorts monthly
- **60% of Shorts viewers** are under 35
- **Shorts viewers spend 25% more time** on YouTube overall
- **Mobile accounts for 89%** of Shorts consumption

### Shorts Ad Formats
- **Shorts ads:** Appear between organic Shorts in the Shorts feed. Users can swipe past them.
- **Billing:** CPM-based (cost per 1,000 impressions)
- **Length:** 15-60 seconds (vertical, 9:16 aspect ratio)
- **Interaction:** Users swipe up to skip, tap to pause, or engage with CTA button

## Shorts Creative Requirements

### Technical Specifications

| Spec | Requirement |
|------|-------------|
| Aspect Ratio | 9:16 (vertical) — MANDATORY |
| Resolution | 1080x1920 minimum |
| Length | 15-60 seconds |
| File Size | Max 256MB |
| Audio | Required (95%+ watch with sound) |
| Captions | Strongly recommended (burned in) |
| Safe Zones | Keep key elements within center 80% (avoid top/bottom UI overlap) |

### The Native Feel Imperative

The single most important factor in Shorts ad performance is whether the ad feels native to the Shorts feed. Ads that look like traditional commercials get swiped past immediately. Ads that feel like organic Shorts content get watched.

**Native Feel Scoring (0-25 points):**

| Element | Points | Criteria |
|---------|--------|----------|
| Vertical Format | 0-5 | Shot natively in vertical? Or cropped from horizontal? Cropped ads lose 40% of the frame and feel obviously repurposed. |
| Visual Style | 0-7 | Does it match the aesthetic of organic Shorts? Handheld/selfie-style, quick cuts, text overlays, reaction-style content. Professional studio lighting and cinematic cameras feel out of place. |
| Pacing | 0-7 | Is the pacing fast enough for the Shorts feed? Average cut every 2-3 seconds. Static shots longer than 4 seconds cause drop-off. |
| Audio/Music | 0-6 | Is the audio/music trending or contemporary? Using trending sounds increases engagement 3x. Background music should be energetic and match Shorts culture. |

### Hook Urgency (First 1-2 Seconds)

In the Shorts feed, users decide to watch or swipe in under 2 seconds — even faster than the 5-second window on In-Stream ads:

**Shorts Hook Scoring (0-25 points):**

| Element | Points | Criteria |
|---------|--------|----------|
| First Frame Impact | 0-10 | Is the first frame visually arresting? Bold text overlay, surprising visual, or face with strong expression. The thumbnail IS the first frame in Shorts. |
| Immediate Value Signal | 0-8 | Does the viewer instantly know what they will get? "3 ways to..." "Watch what happens when..." "You need to know this..." |
| No Wasted Frames | 0-7 | Does content start immediately? No fade-ins, no title cards, no "hey guys welcome back" intros. Every millisecond counts. |

### Content Strategy for Shorts Ads

**What Works on Shorts:**
- Before/after transformations (product demos, makeovers, cleaning)
- Quick tips and hacks (numbered lists, "did you know" reveals)
- Reaction-style content (reacting to a common problem, then showing solution)
- UGC/testimonial style (real customers, unscripted feel)
- Unboxing and first impressions
- Behind-the-scenes/process reveals
- Challenge or trend participation with product integration

**What Fails on Shorts:**
- Repurposed TV commercials cropped to vertical
- Long brand intros or logo animations
- Slow-paced storytelling (save for In-Stream)
- Heavy text-on-screen without voiceover
- Product spec dumps without context
- Celebrity endorsements that feel inauthentic to the platform

### CTA Strategy for Shorts (0-25 points)

| Element | Points | Criteria |
|---------|--------|----------|
| CTA Integration | 0-8 | Is the CTA woven into the content or slapped on at the end? Integrated CTAs ("I got mine at [brand].com") outperform end cards. |
| CTA Button Usage | 0-7 | Is the Google Ads CTA button configured? (Shop Now, Learn More, Sign Up). Button CTR averages 0.8-1.2% on Shorts. |
| CTA Timing | 0-5 | Does the CTA appear multiple times? Best practice: mention once at 3-5 seconds, reinforce at the end. |
| Landing Page Mobile | 0-5 | Does the CTA lead to a mobile-optimized page? 89% of Shorts viewers are on mobile. Non-mobile-friendly landing pages kill conversions. |

## Shorts Campaign Configuration

### Bidding Strategy
- **CPM bidding** is standard for Shorts (impression-based)
- **Target CPM** of $3-$6 for most verticals
- **Maximize Conversions** available but requires sufficient conversion data (30+ per month)
- Start with Manual CPM to establish benchmarks, then shift to automated bidding

### Audience Strategy for Shorts
- **Age:** Skew younger targeting (18-34 primary, 35-54 secondary)
- **Device:** Mobile-only targeting recommended (exclude desktop/tablet/TV)
- **Placement:** Shorts-specific placement available via "YouTube Shorts" placement
- **Custom Intent:** Still works for Shorts — users who searched relevant terms on Google then see Shorts ads
- **Remarketing:** Shorts remarketing lists build quickly due to high impression volume

### Budget Recommendations
- **Minimum:** $20/day per Shorts campaign (need volume for CPM optimization)
- **Ideal:** $50-$100/day for sufficient learning phase data
- **Creative testing budget:** 20% of Shorts budget allocated to testing new creatives weekly
- **Refresh cycle:** Shorts creatives fatigue 2x faster than In-Stream. Refresh every 2-3 weeks.

## Shorts Readiness Assessment

### Composite Score (0-100)

```
Shorts Score = Native Feel (25) + Hook Quality (25) + CTA Strategy (25) +
               Campaign Config (25, from bidding + audience + budget assessment)
```

## Output Format

```
## Shorts Ads Assessment: [Score]/100

### Shorts Readiness
| Dimension | Score | Finding |
|-----------|-------|---------|
| Native Feel | /25 | |
| Hook Quality | /25 | |
| CTA Strategy | /25 | |
| Campaign Config | /25 | |

### Creative Audit
- Format: Vertical native / Cropped horizontal
- Pacing: Fast / Adequate / Too slow
- Audio: Trending / Professional / Missing
- Captions: Present / Missing

### Top Recommendations
1. [Highest impact]
2. [Second priority]
3. [Quick win]

### Shorts Creative Brief
[Provide a 60-second Shorts ad script based on the brand/product]
```
