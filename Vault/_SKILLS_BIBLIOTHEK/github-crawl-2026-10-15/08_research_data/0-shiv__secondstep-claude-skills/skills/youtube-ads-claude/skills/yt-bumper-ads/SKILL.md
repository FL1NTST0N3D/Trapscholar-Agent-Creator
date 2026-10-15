# YouTube Bumper Ads Skill

**Command:** `/yt bumper`

## Purpose

Develops and optimizes 6-second bumper ad strategy for YouTube. Bumper ads are YouTube's most efficient format for building reach and frequency at scale. Despite being only 6 seconds, well-crafted bumpers deliver brand recall rates comparable to 30-second ads at a fraction of the cost. This skill covers single-message strategy, sequential bumper campaigns, and frequency optimization.

## Bumper Ad Fundamentals

### Format Specifications

| Spec | Requirement |
|------|-------------|
| Duration | 6 seconds maximum (non-skippable) |
| Aspect Ratio | 16:9 (horizontal) |
| Billing | CPM (cost per 1,000 impressions) |
| Average CPM | $2.00 - $6.00 |
| Skip Option | None — viewer must watch all 6 seconds |
| Companion Banner | Optional 300x60 display banner |
| Resolution | 1080p recommended |

### Why Bumpers Work

Google's research shows bumper ads deliver:
- **9 out of 10 bumper campaigns** drive significant ad recall lift
- **Average ad recall lift of 38%** (comparable to 30-second ads)
- **Average brand awareness lift of 13%**
- **Average purchase intent lift of 4%**
- **CPM 40-60% lower** than non-skippable in-stream

The constraint of 6 seconds forces creative clarity. One message. One visual. One feeling. No filler.

## Single Message Strategy

### The Golden Rule: One Message Per Bumper

Six seconds allows exactly ONE clear message. Attempting to communicate multiple ideas in 6 seconds results in zero recall. Every bumper must have a singular focus:

**Acceptable Single Messages:**
- Product name + one benefit ("AcmeCRM: Close deals 3x faster")
- Brand moment (logo + sonic signature + emotion)
- Single offer ("50% off this weekend only")
- Feature spotlight (one feature demonstrated in action)
- Social proof ("Trusted by 10,000+ companies")
- Problem statement ("Tired of losing leads?")

**Message Scoring (0-30 points):**

| Element | Points | Criteria |
|---------|--------|----------|
| Message Clarity | 0-10 | Can a viewer state the message after one viewing? If not, it is too complex for 6 seconds. |
| Message Singularity | 0-10 | Is there exactly ONE takeaway? Multiple messages in 6 seconds = zero retention. |
| Message Relevance | 0-10 | Does the message matter to the target audience? Is it tied to a real pain point or desire? |

### Visual Storytelling (0-25 points)

With only 6 seconds, visuals must do most of the heavy lifting:

| Element | Points | Criteria |
|---------|--------|----------|
| Visual Clarity | 0-8 | Is the visual immediately understandable? No complex scenes, no multiple characters, no detailed environments. |
| Product Visibility | 0-7 | Is the product or brand mark visible for at least 3 of the 6 seconds? |
| Motion & Energy | 0-5 | Does the visual have movement? Static images feel like display ads, not video. |
| Color & Contrast | 0-5 | Does the bumper stand out from typical YouTube content? Bold colors and high contrast improve attention. |

### Audio Strategy (0-20 points)

Audio is critical in bumpers because the viewer cannot skip — they hear everything:

| Element | Points | Criteria |
|---------|--------|----------|
| Voiceover Efficiency | 0-7 | Maximum 8-10 words spoken in 6 seconds. More than that sounds rushed and desperate. Ideally 5-7 words. |
| Sonic Branding | 0-7 | Does the brand have a recognizable sound? Intel bong, Netflix "ta-dum," McDonald's "ba da ba ba ba." Sonic branding increases recall 8x. |
| Music/SFX | 0-6 | Is there a musical or sound effect element that reinforces the message? Sound effects can replace words and communicate faster. |

### Brand Recall Optimization (0-25 points)

| Element | Points | Criteria |
|---------|--------|----------|
| Brand Appearance | 0-10 | Is the brand name/logo visible for at least 50% of the bumper (3+ seconds)? |
| Brand Audio | 0-8 | Is the brand name spoken aloud? Dual encoding (visual + audio) doubles recall. |
| End Frame | 0-7 | Does the final frame show brand + CTA? The last frame lingers in memory. |

## Sequential Bumper Strategy

Sequential bumpers are a series of 6-second ads shown in a specific order to the same user over time. This is one of the most sophisticated YouTube ad tactics and creates a narrative arc across multiple micro-moments.

### Sequence Structures

**3-Part Sequence (Most Common):**
1. **Tease:** Introduce the problem or create curiosity (Day 1)
2. **Reveal:** Show the product/solution (Day 3-5)
3. **Reinforce:** Drive the CTA with urgency (Day 7-10)

**5-Part Sequence (For Product Launches):**
1. **Problem:** "Are you struggling with X?"
2. **Agitate:** "It costs you Y every month"
3. **Solution:** "Introducing [Product]"
4. **Proof:** "Join 10,000+ customers"
5. **Action:** "Try free for 14 days"

**Ongoing Series (For Brand Building):**
- Weekly new bumper featuring a different product feature, customer story, or use case
- Each bumper is self-contained but builds brand familiarity over time
- Recommended frequency: 1 new bumper every 2 weeks, rotated for 4-6 weeks

### Sequential Campaign Setup

In Google Ads, set up sequential bumpers using Video Ad Sequencing campaigns:
- Select "Video" campaign type > "Ad sequence" subtype
- Define sequence steps with specific bumper creatives
- Set impression-based sequencing (show step 2 only after step 1)
- Set frequency caps between steps (2-4 days between each step)
- Minimum audience size: 100,000 for effective sequencing

## Frequency Management for Bumpers

Bumpers are short and non-intrusive, so they tolerate higher frequency than other formats:

**Recommended Frequency Caps:**
- Single bumper campaign: 5-7 impressions per user per week
- Sequential campaign: 1 impression per step, with 2-4 day gaps
- Brand awareness burst: Up to 10 impressions per week for 2-week flights
- Always-on brand building: 3-4 impressions per week

**Over-Frequency Indicators:**
- View-through rate declining over time
- Audience overlap report showing >30% overlap between campaigns
- Brand lift study showing declining incremental recall

## Bumper Creative Testing

Test bumpers in groups of 3-5 variants. Key variables to test:

1. **Message type:** Benefit-led vs. problem-led vs. social proof
2. **Visual style:** Product demo vs. lifestyle vs. graphic/animated
3. **Audio approach:** Voiceover vs. music-only vs. sound effects
4. **Brand placement:** Logo throughout vs. end-frame only
5. **CTA type:** URL vs. "Search for [brand]" vs. no CTA

## Composite Bumper Score

```
Bumper Score = Message (30) + Visual (25) + Audio (20) + Brand Recall (25)
Maximum: 100 points
```

## Output Format

```
## Bumper Strategy Assessment: [Score]/100

### Bumper Creative Scores
| Bumper | Message | Visual | Audio | Brand | Total |
|--------|---------|--------|-------|-------|-------|
| Bumper 1 | /30 | /25 | /20 | /25 | /100 |
| Bumper 2 | /30 | /25 | /20 | /25 | /100 |

### Sequential Strategy
- Current: [Describe current approach]
- Recommended: [Sequence structure]
- Estimated reach improvement: [X%]

### Frequency Analysis
- Current frequency: [X impressions/user/week]
- Recommended cap: [X impressions/user/week]
- Estimated waste from over-frequency: [$X]

### Bumper Script Templates
[Provide 3 scripted bumper concepts tailored to the brand]
```
