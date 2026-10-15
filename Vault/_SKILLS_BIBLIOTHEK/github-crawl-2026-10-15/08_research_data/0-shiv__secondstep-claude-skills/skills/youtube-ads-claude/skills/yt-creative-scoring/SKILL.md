# YouTube Creative Scoring Skill

**Command:** `/yt creative`

## Purpose

Scores YouTube video ad creatives using Google's ABCD framework and proprietary hook-quality analysis. Creative is the single most impactful lever in YouTube advertising — Google's own research shows that creative quality accounts for 70% of ad performance on YouTube, far exceeding targeting or bidding optimizations.

## The ABCD Framework

Google's research-backed framework for effective YouTube ads. Each letter represents a critical creative element:

### A — Attract (First 5 Seconds)

The hook is everything on YouTube. For skippable ads, you have exactly 5 seconds before the skip button appears. For Shorts, you have about 1 second before the user swipes away. Score the opening:

**Hook Quality Scoring (0-25 points):**

| Element | Points | Criteria |
|---------|--------|----------|
| Pattern Interrupt | 0-7 | Does the first frame break the viewer's scroll/watch pattern? Unexpected visual, bold statement, or surprising action. |
| Relevance Signal | 0-6 | Does the hook immediately signal who this ad is for? "If you're a [target audience]..." or visual cue that filters the right viewer. |
| Curiosity Gap | 0-6 | Does it create an open loop the viewer wants to close? A question, partial reveal, or before/after tease. |
| Emotional Trigger | 0-6 | Does it provoke an emotion in the first 3 seconds? Fear, excitement, humor, empathy, surprise. |

**Red Flags (deduct points):**
- Logo animation as the first frame (-5 points): Viewers associate logos-first with ads and skip immediately.
- Slow fade-in or title card (-3 points): Dead time kills retention.
- Generic stock footage opener (-3 points): Feels inauthentic, low engagement.
- No human face in first 2 seconds (-2 points): Faces increase attention by 30%.

### B — Brand (Appearance & Integration)

Brand visibility matters, but timing and integration style affect recall and sentiment differently:

**Brand Scoring (0-25 points):**

| Element | Points | Criteria |
|---------|--------|----------|
| Brand Mention Timing | 0-8 | For awareness: Brand in first 5 seconds. For consideration: Brand within first 10 seconds. For conversion: Brand can appear later but must be prominent at CTA. |
| Visual Brand Presence | 0-6 | Logo, brand colors, or product visible on screen. Persistent watermark vs. occasional flash. |
| Audio Brand Mention | 0-5 | Brand name spoken aloud. Sonic branding (jingle, sound logo). Audio mention increases recall 20%. |
| Brand Integration | 0-6 | Is the brand naturally woven into the story, or awkwardly inserted? Native integration scores higher than overlay graphics. |

**Benchmarks:**
- Ads with brand mention in first 5 seconds: 30% higher ad recall
- Ads with both audio and visual branding: 2x recall vs. visual only
- Persistent logo watermark: Increases unaided brand recall by 15%

### C — Connect (Storytelling & Emotion)

The viewer must feel something to remember the ad and take action:

**Connection Scoring (0-25 points):**

| Element | Points | Criteria |
|---------|--------|----------|
| Storytelling Structure | 0-7 | Does the ad tell a story with setup/conflict/resolution? Or is it just a product feature list? |
| Emotional Resonance | 0-6 | Does the ad make the viewer feel something? Humor, inspiration, empathy, aspiration, fear of missing out. |
| Audience Mirroring | 0-6 | Does the ad feature people who look/sound/live like the target audience? Representation increases connection. |
| Pacing & Music | 0-6 | Does the pacing match the platform? Fast cuts for Shorts/Bumpers, story arc for In-Stream. Is music enhancing the mood? |

**Audio Quality Check:**
- 95% of YouTube is watched with sound on (unlike social feeds)
- Audio quality must be professional: clear voiceover, balanced music, no distortion
- Captions/subtitles present for accessibility (also helps in sound-off scenarios)
- Caption usage increases view time by 12% on average

### D — Direct (Call to Action)

The CTA must be clear, specific, and visually prominent:

**CTA Scoring (0-25 points):**

| Element | Points | Criteria |
|---------|--------|----------|
| CTA Clarity | 0-8 | Is there a single, clear action the viewer should take? "Shop Now," "Get a Free Quote," "Download the App." Vague CTAs like "Learn More" score lower. |
| CTA Timing | 0-6 | For skippable: CTA before the 5-second mark AND at the end. For non-skip/bumper: CTA in final 2 seconds. For Shorts: CTA overlaid throughout. |
| Visual CTA | 0-5 | Is the CTA reinforced visually? End card, overlay, product shot with URL. |
| Urgency Element | 0-6 | Does the CTA include urgency? Limited time, scarcity, exclusive offer. Urgency increases CTR by 30%. |

## Composite Creative Score

```
Creative Score = Attract + Brand + Connect + Direct
Maximum: 100 points

90-100: Elite creative. Top-performing ad.
70-89:  Strong creative. Minor refinements needed.
50-69:  Average. Significant improvement opportunities in weak areas.
30-49:  Below average. Major rework recommended.
0-29:   Poor. Creative is likely hurting campaign performance.
```

## Creative Analysis Process

When the user provides video ad details (URL, script, or description):

1. **Score each ABCD dimension** using the rubrics above
2. **Identify the weakest dimension** — this is where improvement will have the biggest impact
3. **Provide specific rewrite suggestions** for the hook (first 5 seconds)
4. **Check format-specific requirements:**
   - Skippable In-Stream: Does the ad work if the viewer skips at 5 seconds? (Brand/message delivered pre-skip?)
   - Bumper: Is the message singular and clear in 6 seconds?
   - Shorts: Does it feel native to the Shorts feed? Vertical format? Fast-paced?
   - Non-Skip: Is 15 seconds used efficiently without filler?
5. **Compare to category benchmarks** for view rate and engagement
6. **Recommend A/B test variants** — always suggest testing the hook first, then CTA

## Creative Testing Framework

Recommend the user test creatives in this priority order:

1. **Hook variations** (highest impact): Test 3-5 different opening 5 seconds
2. **CTA variations**: Test action verb, urgency, and offer
3. **Length variations**: Test 15s vs 30s vs 60s of the same concept
4. **Format variations**: Same message adapted for In-Stream vs Shorts vs Bumper
5. **Talent/presenter variations**: Different faces, voices, demographics

## Output Format

```
## Creative Score: [X]/100

### ABCD Breakdown
| Dimension | Score | Key Finding |
|-----------|-------|-------------|
| A - Attract | /25 | |
| B - Brand | /25 | |
| C - Connect | /25 | |
| D - Direct | /25 | |

### Hook Analysis (First 5 Seconds)
Current hook: [describe]
Effectiveness: [score/10]
Suggested rewrite: [provide alternative]

### Top 3 Improvements
1. [Highest impact change]
2. [Second priority]
3. [Quick win]

### A/B Test Recommendations
Test 1: [Hook variant]
Test 2: [CTA variant]
Test 3: [Format variant]
```
