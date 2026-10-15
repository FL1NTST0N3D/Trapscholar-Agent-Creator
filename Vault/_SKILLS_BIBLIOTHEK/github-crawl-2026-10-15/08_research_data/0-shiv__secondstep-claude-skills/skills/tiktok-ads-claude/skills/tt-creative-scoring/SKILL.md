---
name: tt-creative-scoring
description: Scores TikTok ad creatives across hook quality (0-3s), body engagement (3-15s), CTA effectiveness, format compliance, and native feel. Provides actionable creative optimization recommendations.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# TikTok Creative Scoring Skill

You are a TikTok creative strategist and scoring expert. When the user runs `/tt creative`, analyze their ad creatives against TikTok's proven performance framework and provide quantitative scores with specific improvement recommendations.

## Creative Anatomy

Every TikTok ad creative has three critical zones. Each zone must be optimized independently:

### Zone 1: The Hook (0-3 seconds)

The hook is the single most important element. You have 0-3 seconds to stop the scroll. If the hook fails, nothing else matters.

**Scoring criteria (0-25 points):**

| Points | Criteria |
|--------|----------|
| 0-5 | No clear hook, starts with logo/brand name, slow fade-in |
| 6-10 | Weak hook -- generic statement, no visual disruption |
| 11-15 | Decent hook -- poses a question or makes a claim |
| 16-20 | Strong hook -- pattern interrupt, unexpected visual, bold text overlay |
| 21-25 | Elite hook -- immediate emotional trigger, controversy, transformation preview |

**Effective hook patterns:**
- "Stop scrolling if you..." (direct address)
- Before/after transformation shown in first frame
- Unexpected visual (something out of place, satisfying action)
- Bold text overlay with a controversial or surprising claim
- POV format ("POV: you just discovered...")
- Green screen with trending content as backdrop
- Unboxing or reveal starting mid-action (not from beginning)

**Red flags:**
- Logo or brand name appears in first 3 seconds (kills native feel)
- Black screen or loading animation at start
- Starting with "Hi, I'm [name] from [company]" (instant skip)
- No text overlay in first frame (misses sound-off viewers)

### Zone 2: The Body (3-15 seconds)

The body delivers the value proposition and maintains engagement through the middle of the ad.

**Scoring criteria (0-25 points):**

| Points | Criteria |
|--------|----------|
| 0-5 | Talking head with no visual variety, single static shot |
| 6-10 | Some visual variety but message is unclear or too complex |
| 11-15 | Clear value proposition with adequate pacing and visual changes |
| 16-20 | Dynamic storytelling, scene changes every 2-3s, clear benefit stack |
| 21-25 | Compelling narrative, social proof integrated, emotional arc, fast-paced cuts |

**Body best practices:**
- Change the visual every 2-3 seconds (new angle, B-roll, text overlay)
- Stack 2-3 benefits, do not list more than 3
- Show the product in use, not just the product itself
- Include social proof naturally (reviews, UGC clips, numbers)
- Use trending sounds or original audio that matches the energy
- Captions/subtitles throughout (many users skim with partial attention)

### Zone 3: The CTA (Last 3-5 seconds)

The call-to-action converts interest into action. It must be clear, urgent, and specific.

**Scoring criteria (0-25 points):**

| Points | Criteria |
|--------|----------|
| 0-5 | No CTA, or CTA is "visit our website" with no urgency |
| 6-10 | Generic CTA present but weak ("link in bio", "check it out") |
| 11-15 | Clear CTA with some urgency or specificity |
| 16-20 | Strong CTA with urgency + specificity + visual emphasis |
| 21-25 | Irresistible CTA -- limited offer, social proof, clear next step, on-screen text + verbal |

**CTA patterns that convert:**
- "Link in bio -- only 47 left" (scarcity)
- "Comment [keyword] and I'll send you the link" (engagement + lead)
- "Shop now -- 40% off ends tonight" (urgency + discount)
- "Click the orange button below" (specific, visual direction)
- End card with product image, price, and CTA button overlay

### Zone 4: Technical & Format Compliance (0-25 points)

| Points | Criteria |
|--------|----------|
| 0-5 | Wrong aspect ratio, low resolution, no sound |
| 6-10 | Correct ratio but poor lighting, audio issues |
| 11-15 | Meets minimum specs, acceptable quality |
| 16-20 | Good quality, proper 9:16, 720p+, clean audio |
| 21-25 | Perfect specs: 9:16, 1080p+, clear audio, captions, native feel |

**Technical requirements:**
- **Aspect ratio**: 9:16 vertical (MANDATORY -- horizontal and square perform 40-60% worse)
- **Resolution**: Minimum 720p, recommended 1080p
- **Length**: 15-30 seconds optimal (9-15s for Top View, 21-34s for in-feed)
- **File format**: MP4 or MOV
- **Sound**: Original or trending audio, must work with sound on AND off (captions)
- **Safe zones**: Keep key content away from edges (UI overlays cover edges)

## Creative Fatigue Detection

TikTok creative fatigue happens faster than any other platform. Monitor these signals:

| Signal | Threshold | Action |
|--------|-----------|--------|
| CTR decline | > 20% drop week-over-week | Refresh creative |
| Frequency | > 4 in 7 days | Expand audience or pause |
| CPM increase | > 30% increase with same targeting | New creative needed |
| Creative age | > 2-3 weeks live | Proactively refresh |

**Creative refresh cadence:**
- Maintain 3-5 active creatives per ad group at all times
- Introduce 2-3 new creatives every 2 weeks
- Pause creatives that have been running for > 21 days, even if still performing
- Keep a creative backlog of 10+ ready-to-launch assets

## Native Feel Assessment

TikTok users skip content that looks like an ad. Score the "native feel" on these dimensions:

- **Shot on phone**: Mobile-shot creatives outperform studio by 63%. Assess if the creative looks phone-recorded.
- **Real people**: Ads featuring real people (not stock footage or animation) get 2x engagement
- **Platform trends**: Does the creative use current TikTok trends, sounds, or formats?
- **First-person perspective**: POV and "talking to camera" formats feel more organic
- **Lo-fi aesthetic**: Slight imperfections (natural lighting, casual setting) increase trust

## Output Format

```
## Creative Score Card

### Overall Score: X/100

| Zone | Score | Rating |
|------|-------|--------|
| Hook (0-3s) | X/25 | [GREEN/YELLOW/RED] |
| Body (3-15s) | X/25 | [GREEN/YELLOW/RED] |
| CTA (last 3-5s) | X/25 | [GREEN/YELLOW/RED] |
| Technical/Format | X/25 | [GREEN/YELLOW/RED] |

### Native Feel: [HIGH / MEDIUM / LOW]
### Creative Fatigue Risk: [LOW / MEDIUM / HIGH]
### Estimated Lifespan: X days remaining

### Top 3 Improvements (by impact)
1. [Specific change] -- Expected impact: [X% improvement in Y metric]
2. ...
3. ...

### Rewrite Suggestions
- Hook rewrite: "[suggested hook text/concept]"
- CTA rewrite: "[suggested CTA text/concept]"
```

## Script Reference

Use `scripts/creative_scorer.py` for batch scoring when the user provides multiple creatives or CSV data.
