# Comprehensive Brand Social Media Skill

**Triggers:**
- `/social-calendar [BrandName] [Month Year]` — build monthly content calendar
- `/social-audit [BrandName]` — audit brand's social channels
- `/competitor-audit [BrandName]` — competitor intelligence + gap analysis
- `/social-suite [BrandName] [Month Year]` — run all three modes end to end
- "create social media calendar", "build the calendar", "audit my social media",
  "analyse my competitors", "do a full social media analysis"

---

## Overview

This skill is a complete social media intelligence and content production system. It operates in three modes — run individually or combined:

| Mode | Command | What it does |
|------|---------|--------------|
| **A — Calendar** | `/social-calendar` | Research → narrative brief → full monthly content calendar for selected platforms |
| **B — Audit** | `/social-audit` | Analyses brand's own social channels, scores performance, outputs recommendations |
| **C — Competitor Intel** | `/competitor-audit` | Studies competitor channels, builds comparison matrix, identifies gaps and whitespace |
| **Full Suite** | `/social-suite` | Runs B + C first, uses findings to inform A — the most comprehensive output |

**The only mandatory pause in any mode is after the narrative brief in Mode A (Phase 4).** Everything else runs sequentially without asking for confirmation.

---

## Step 0 — Mode Selection and Brand Context

### 0a: Identify the Mode

If the user's message is ambiguous (e.g. just "help with social media"), ask:

> "What would you like to do?
> 1. Build a monthly content calendar
> 2. Audit our existing social channels
> 3. Analyse competitors and find content gaps
> 4. All of the above (full suite — recommended)"

### 0b: Gather Brand Context

Extract from the user's message or ask for anything missing:

```
BRAND_NAME      = [brand name, e.g. "Stripe"]
BRAND_URL       = [primary website URL — required for all modes]
TARGET_MONTH    = [Month Year — required for Mode A only, e.g. "June 2026"]
ICP_HINT        = [optional — who they sell to, e.g. "CTOs at mid-market SaaS"]
COMPETITORS     = [list of competitor names/URLs — required for Mode C; discover if not provided]
OUTPUT_DIR      = [save path — default: ~/Documents/[BRAND_NAME]/social/]
```

### 0c: Channel Selection (Mode A — Calendar)

Ask the user which platforms they want content for:

> "Which platforms do you want content for this month? Select all that apply:
> 1. LinkedIn
> 2. X (Twitter)
> 3. Instagram (Feed + Reels)
> 4. Instagram Stories
> 5. Facebook
> 6. TikTok
> 7. YouTube Shorts
> 8. YouTube (Long-form)
> 9. Threads
> 10. Pinterest
> 11. Reddit (community engagement)
> 12. All major platforms (LinkedIn, X, Instagram, Facebook, TikTok, YouTube Shorts)"

Store as: `ACTIVE_CHANNELS = [list of selected platforms]`

If the user says "all" or doesn't specify, default to: LinkedIn, X, Instagram (Feed + Reels), Facebook, TikTok, YouTube Shorts.

For Mode B and C, discover which channels the brand is active on automatically (Phase B1 / C1).

---

## PLATFORM PROFILES

> This section is the canonical reference for all content decisions. Every caption, script, hook, and format must follow the rules for its platform. Content is not platform-native if it's just a shorter or longer version of the same sentence.

### LinkedIn

**What it is:** Professional network. Primary B2B content platform. High-intent audience — people are in a work mindset.

**Audience:** Decision-makers, practitioners, industry professionals. Skews 25–54.

**What performs:**
- Bold data-led hooks (first line is everything — only first 2 lines visible before "see more")
- Carousel documents (native PDF format — high saves and shares)
- Short-form video (under 60 sec, captions on, no sound required)
- Provocative opinions / contrarian takes
- Founder/executive personal posts (far higher reach than company pages)
- Behind-the-scenes / team culture content

**What doesn't perform:**
- Generic promotional content ("We're excited to announce...")
- Long unbroken paragraphs
- Stock photography
- External links in the post body (put links in comments — the algorithm suppresses them)

**Caption rules:**
- Static: max 3 lines before "see more". First line = hook. Second = context. Third = CTA or question.
- Carousel: max 2 lines + "Swipe →" or similar.
- Video: 1–2 lines + what the video is about.
- Hashtags: 2–3, placed at the very end. Use specific ones (#DevSecOps not #Tech).
- Never put URLs in the post body. Always in first comment.

**Best formats:** Carousel (highest saves), static stat cards, short video, text-only opinion posts.

**Optimal posting:** 3–5x per week. Tue–Thu, 8–10am and 12–2pm local.

---

### X (Twitter)

**What it is:** Real-time conversation platform. Audience skews technical, opinionated, media-forward. Organic reach is declining but engagement from the right accounts drives outsized distribution.

**Audience:** Journalists, developers, founders, investors, power users. High signal-to-noise when done right.

**What performs:**
- Very short, punchy takes (1–2 sentences)
- Threads that teach something (numbered lists as connected tweets)
- Contrarian opinions with receipts
- Genuine reactions to breaking news / industry moments
- Quote-tweeting with a strong take
- Polls
- Images with bold text overlay (no caption needed — the image IS the content)

**What doesn't perform:**
- Long blocks of text in a single tweet
- Too many hashtags (0–1 is ideal for reach; branded hashtags only for campaigns)
- Automated cross-posts from LinkedIn (tone is completely different)
- Formal brand-speak

**Caption rules:**
- Max 280 characters (hard limit).
- Aim for under 200 characters — leave room for quote-tweeting.
- Hashtags: 0–1. Only if genuinely trending or campaign-specific.
- End with a question or provocative statement to drive replies.
- For threads: first tweet = standalone hook. Each subsequent tweet = one idea.

**Best formats:** Short text takes, threads, images with text, video clips (first 3 sec matters).

**Optimal posting:** 1–3x per day. Weekdays, 9am–12pm and 5–7pm.

---

### Instagram Feed

**What it is:** Visual-first platform. Discovery via Explore and hashtags. Community via comments and DMs.

**Audience:** Broad consumer and prosumer. B2B brands can work here if the visual output is high quality.

**What performs:**
- High-quality visuals (dark/minimal or bold/colourful — consistency matters more than style)
- Carousel posts (algorithm pushes them because they increase dwell time)
- Behind-the-scenes / authentic content
- Data visualisations as carousels
- Relatable content (memes, workplace humour for B2B)
- Strong first frame on carousels — must compel the swipe

**What doesn't perform:**
- Low-quality images
- Too much text on a static image
- Pure product photography without context
- Inconsistent visual style

**Caption rules:**
- Max 2 lines visible before "more". First line = hook.
- Hashtags: 5–8, placed on a new line below the caption (or in the first comment for cleaner look).
- Use a mix of niche (#DevSecOps 50K), mid-size (#CyberSecurity 2M), and broad (#Tech 100M).
- Alt text: always fill it in (accessibility + SEO).

**Best formats:** Carousel (highest reach), strong static images, Reels.

**Optimal posting:** 4–7x per week (feed). Daily for Stories.

---

### Instagram Reels

**What it is:** Short-form video tab. Highest organic reach on the platform. Algorithm serves Reels to non-followers aggressively.

**Audience:** Broader than feed — Reels reach new audiences who don't follow the account.

**What performs:**
- Hook in first 1–3 seconds (text on screen, bold statement, or surprising visual)
- Trending audio (boosts algorithmic distribution)
- Text-on-screen captions (most watched without sound)
- Under 30 seconds performs better for most brands
- Educational content that delivers value fast ("3 things your team doesn't know about X")
- B-roll with voiceover is fine — doesn't need to be face-to-camera

**What doesn't perform:**
- Slow intros (any brand logo or "Hi guys" opening)
- Repurposed horizontal video
- Low-quality audio (if doing voiceover)
- Not using text overlays (most views are sound-off)

**Caption rules:**
- More relaxed than feed. Can be slightly longer (2–3 lines).
- Hashtags: 3–5, in caption or first comment.
- Include a CTA: "Save this", "Share with your team", "Comment X if you want the full list".

**Best formats:** Text-on-screen + voiceover, B-roll montage with VO, talking head with captions.

**Optimal posting:** 4–7x per week. Evenings and weekends perform well.

---

### Instagram Stories

**What it is:** Ephemeral 24-hour content. Shown only to followers. High intimacy, low pressure.

**Audience:** Existing community — people who already follow the account.

**What performs:**
- Interactive stickers (polls, questions, quizzes, sliders)
- Behind-the-scenes
- Countdown timers (product launches, events)
- Reposts of feed content with a "new post" sticker
- Link stickers (now available to all accounts)
- Quick polls ("Hot take: X or Y?")
- Q&A sessions

**What doesn't perform:**
- Static promotional graphics with no interactivity
- Stories that are clearly an afterthought
- Text-heavy slides

**Content rules:**
- Each story frame = one idea. Max 7 frames per story series before drop-off.
- Always use at least one interactive element.
- Link stickers: use for every story that references external content.
- Produce 3–5 Stories per day (separate from feed).
- Stories content should feel more spontaneous than feed content.

**Format notes:** 9:16 vertical (1080×1920px). Text in the safe zone (middle 60% of screen — top and bottom may be cut by UI).

---

### Facebook

**What it is:** Largest platform by MAU globally. Organic reach for brand pages is very low (1–5%), but paid amplification is highly effective. Also important for community (Groups) and events.

**Audience:** Skews older than other platforms (35–65). High use in international markets. Strong for B2C brands and local businesses.

**What performs:**
- Native video (Facebook prioritises video that keeps people on platform)
- Long-form posts when storytelling (Facebook's audience reads more than X's)
- Events and local content
- Facebook Groups engagement
- Shared articles (with strong comment hooks)
- Facebook-native polls

**What doesn't perform:**
- Short punchy posts that work on X (too terse for Facebook's audience)
- Excessive external links (deprioritised in feed)
- Purely promotional content without narrative

**Caption rules:**
- Can be longer than other platforms — 3–5 sentences is fine.
- Conversational, slightly warmer tone than LinkedIn.
- Questions at the end drive comments.
- Hashtags: 1–2 max (Facebook hashtags have minimal SEO value).
- Emojis: fine to use sparingly, more than LinkedIn.

**Best formats:** Native video, long-form storytelling posts, event posts, Group content.

**Optimal posting:** 1–2x per day. Weekdays 1–4pm.

---

### TikTok

**What it is:** Short-form video-first platform with the most powerful discovery algorithm of any social network. A video can reach millions of non-followers. The algorithm rewards watch time, completion rate, and saves — not follower count.

**Audience:** Skews 18–34 but expanding to 35–54. Highly engaged. B2B brands are growing fast here — the "TikTok for business" audience is real.

**What performs:**
- Hook in the FIRST 1–2 SECONDS — text on screen or a bold opening visual
- Native TikTok formats: POV, "I tried X so you don't have to", "Things nobody tells you about X", "Day in the life of a [role]", "What it's actually like to [experience]"
- Trending sounds + original audio
- Creator-style authentic feel (not polished corporate video)
- Stitches and Duets (engaging with other creators' content)
- Educational content that moves fast ("3 facts in 30 seconds")
- Voiceover-style explanation over text cards
- Jump-cut editing (cut every 1–2 seconds to maintain attention)

**What doesn't perform:**
- Horizontal video (never)
- Slow intros
- Heavily produced corporate-feel content
- Repurposed LinkedIn videos (wrong energy entirely)
- Long setup before getting to the point

**Caption rules:**
- 1–2 lines max. The video IS the content — the caption is a supplement.
- 3–5 hashtags: 1 broad (#Marketing), 1 niche (#B2BSaaS), 1 trending (check weekly).
- Often ends with a question to drive comments.
- Strong CTA: "Follow for more", "Comment if you want part 2", "Save this for your next meeting".

**Script rules (TikTok-specific):**
- ON-SCREEN TEXT must appear within the first 1 second (not 3 seconds like other formats)
- First spoken word must be at second 0 — no silent intros
- Format hook: "Here's what [X] actually means for [ICP role]..." or "Nobody in [industry] talks about this, but..."
- Optimal length: 15–45 seconds (sweet spot for B2B)
- Trending audio: note where to add trending sound (Claude will indicate the scene — user/editor selects actual trending audio at time of production)
- Duet/Stitch potential: flag if a competitor or industry post would be a good Stitch candidate

**Best formats:** Text-on-screen + VO, creator-style explainer, B-roll with VO, reaction/commentary.

**Optimal posting:** 1–4x per day (higher frequency than other platforms). Any time — algorithm matters more than posting time.

---

### YouTube Shorts

**What it is:** YouTube's short-form vertical video format (<60 seconds). Shown in the Shorts feed and also discoverable via search. The SEO element is stronger than TikTok — YouTube Shorts can rank in Google Search.

**Audience:** Broader age range than TikTok. High intent (people search for things). Strong for tutorial and educational content.

**What performs:**
- Educational explainers
- "Quick tip" format
- Repurposed long-form highlights
- Step-by-step "how to" content
- Strong hook in first 3 seconds
- Visuals that loop well (the video replays automatically)

**What doesn't perform:**
- Content without a clear payoff
- Slow intros
- Horizontal video
- Content that only makes sense in context of a longer video without that context provided

**Content rules:**
- Title is critical for searchability — include the keyword people would search for.
- Description: first 2 lines visible in feed. Include target keyword and CTA.
- Unlike TikTok, YouTube Shorts benefits from a SEO-optimised title (not just a hook).
- If related to a long-form video on the channel, include a link in description.

**Script rules:**
- Same structure as regular video scripts but faster paced.
- First 3 seconds = hook text on screen + VO simultaneously.
- Aim for a conclusion or "payoff" at the 45-second mark, leaving time for CTA.

**Optimal posting:** 2–5x per week. Consistency matters more than frequency here.

---

### YouTube Long-Form

**What it is:** The world's second-largest search engine. Long-form video content that ranks in both YouTube and Google Search. High trust, high intent, long shelf life.

**Audience:** Research-mode audience. Willing to invest 5–20 minutes for depth. Strong for tutorial, case study, interview, and documentary-style content.

**What performs:**
- Tutorial / how-to content (evergreen)
- Case studies and customer stories
- Expert interviews and panel discussions
- Thought leadership series
- Product walkthroughs
- Industry analysis and commentary

**What doesn't perform:**
- Poorly structured content with no chapters
- Bad audio (this is the single biggest drop-off driver)
- Videos without a compelling thumbnail
- Titles that don't match search intent

**Content spec (for each YouTube long-form video):**
- **Title:** SEO-optimised. Include primary keyword. Under 60 characters. Pattern: "[What they'll learn] | [Context]"
- **Thumbnail brief:** What should appear — person, text overlay, brand element. High contrast. Single focal point.
- **Description:** Lines 1–2 visible in search. Include hook + keyword. Full description below fold: what's covered, chapters, links, CTA.
- **Chapters:** Always include timestamps. Format: 0:00 Intro, 1:30 [Topic 1], etc.
- **Tags:** 5–10 keyword tags.
- **End screen:** What CTA should appear — subscribe, watch next, visit website.
- **Cards:** Where to place mid-video cards pointing to related content.

**Optimal posting:** 1–2x per week (consistency over volume).

---

### Threads

**What it is:** Meta's text-based platform (launched 2023). Most brand-safe of the Twitter alternatives. Casual, conversational, discovery-oriented. Cross-posts easily from Instagram.

**Audience:** Instagram's existing users (so skews similar to IG). Early-adopter brands are getting outsized reach now while competition is low.

**What performs:**
- Opinions and hot takes (more casual than LinkedIn)
- Questions that spark conversation
- Behind-the-scenes and authentic moments
- Short threads (3–5 connected posts)
- Reposts with commentary
- Genuine humour (brands that are too corporate don't work here)

**What doesn't perform:**
- Formal press-release tone
- Heavy promotional content
- Too many posts (algorithm still establishing itself)

**Caption rules:**
- Conversational, first-person tone.
- No established hashtag culture — skip hashtags for now.
- 2–4 lines max for a single post.
- For threads: each post = one idea. Keep each under 3 lines.

**Optimal posting:** 2–4x per week. Building slowly is fine — the platform is still maturing.

---

### Pinterest

**What it is:** A visual search engine, not a social network. People use Pinterest to plan and discover — they're in a high-intent, aspirational mindset. SEO matters far more than social strategy here.

**Audience:** Skews female, 25–45 globally. Strong for lifestyle, home, food, fashion, wedding, travel. Growing B2B presence for infographics, marketing tips, design inspiration, and tools.

**What performs:**
- Vertical images (2:3 ratio — 1000×1500px ideal)
- Infographics and data visualisations
- Step-by-step process content ("How to X in 5 steps")
- Listicles as visual assets
- Product inspiration (not just product shots — lifestyle context)
- Bold text overlay with minimal background

**What doesn't perform:**
- Horizontal images
- Images without text overlay (hard to understand out of context)
- Content without a keyword-rich description
- Pinning without board strategy

**Content spec:**
- **Pin title:** 60–100 characters. Include the primary keyword naturally.
- **Pin description:** 100–300 characters. Keyword-rich. What the content is, who it's for, what they'll learn or find.
- **Board:** Which board this pin belongs to (each board = a category/topic).
- **Link:** Every pin should link somewhere — blog post, product page, landing page.

**Optimal posting:** 5–15 pins per day (Pinterest rewards volume unlike other platforms). Use scheduling tools.

---

### Reddit

**What it is:** Community-based discussion platform. Extremely high-quality audience with near-zero tolerance for promotional content. The highest-trust community engagement channel available to brands — if done right.

**Audience:** Highly specific per subreddit. Generally skews male, 25–40, technically literate. Will immediately call out inauthenticity.

**What performs:**
- Genuine value-first posts that contribute to the community's conversation
- Data, research, and original findings (communities love original data)
- Honest questions from practitioners
- AMAs (Ask Me Anything) from credible experts
- Sharing genuinely useful resources without asking for anything in return
- Commenting on existing threads with expertise, not promotion

**What doesn't perform:**
- Anything that sounds like marketing copy
- Posts that mention the brand prominently
- Self-promotion without genuine value added
- Cross-posting the same content across multiple subreddits simultaneously

**Content rules:**
- Reddit is a community engagement channel, not a publishing channel.
- Never post promotional content as a top-level post.
- Brand mention: only if directly relevant and only in comments, never in the post title.
- Write like a practitioner who happens to work at the brand — not a marketer.
- Identify the right subreddit per post (each post belongs to one specific community).
- For AMAs: plan in advance, get subreddit mod approval, prepare 10–15 pre-answered questions.

---

## MODE A — Monthly Calendar Build

### Phase 1 — Study the Brand

**WebFetch** BRAND_URL (homepage) and up to 5 sub-pages — prioritise: product, solutions, platform, pricing, about.

Extract and store as `BRAND_PROFILE`:

**Core identity:**
- USPs — what makes this brand genuinely different
- Product/service pillars — main categories of what they offer
- Key terminology — specific phrases, coined terms, product names the brand owns
- ICP — who they sell to, pain points addressed, job titles in copy

**Tone of voice:**
- Register: assertive / technical / empathetic / conversational / executive-facing
- What they avoid: hype / jargon / overly salesy language
- Distinctive voice patterns

**Social presence (study each platform in ACTIVE_CHANNELS):**

For each active platform, WebFetch the profile and study the last 10–15 posts. Document:
- Follower/subscriber count
- Posting frequency
- Content formats in use
- Hook style and opening patterns
- Caption length and structure
- Hashtag strategy
- Engagement pattern (relative to following — high/medium/low)
- What's performing (high engagement)
- What's not (low engagement, ignored formats)
- Visual consistency and brand aesthetic
- Whether content is truly platform-native or cross-posted from another channel

Store observations per platform within `BRAND_PROFILE`.

### Phase 2 — Extract Keywords and Research Targets

From BRAND_PROFILE, extract and store as `RESEARCH_KEYWORDS`:

- **Primary keywords** (3–5): the brand's core product/category terms
- **Pain point keywords** (3–5): problems the brand solves, in the ICP's own language
- **Competitor keywords** (3–5): named competitors and alternative approaches
- **ICP role keywords** (3–5): job titles and personas the brand targets

If ICP_HINT was provided, use it to refine extraction.

### Phase 3 — Community Research (Last 30 Days)

Run `/last30days` with a 4-query plan:

| Query | Focus |
|-------|-------|
| Query 1 | Top 3–4 primary keywords |
| Query 2 | Pain point keywords — what the ICP is actively struggling with |
| Query 3 | Category/industry trends — what's shifting in their space this month |
| Query 4 | Competitor brand mentions — sentiment, claims, community reactions |

Supplement with WebSearch for:
- Platform-specific trending content in each ACTIVE_CHANNEL this month
- Industry news relevant to the ICP in TARGET_MONTH
- Trending formats and sounds on TikTok/Reels if those channels are active
- Any viral content in the brand's category this month

Store as: `RESEARCH_OUTPUT`

### Phase 4 — Narrative Brief (APPROVAL GATE)

Synthesize BRAND_PROFILE + RESEARCH_OUTPUT into:

```
# [BRAND_NAME] — [TARGET_MONTH] Social Media Narrative Brief

## What the Community Is Talking About
[3–5 bullet points — most discussed topics, with platform source cited]

## Key Pain Points and Blockers Surfaced
[3–5 specific frustrations from real posts/threads — cite subreddit or platform]

## Landscape Signals
[What's trending, what competitors are doing, what the ICP is worried about]

## How [BRAND_NAME] Addresses This
[For each pain point — one sentence on how the brand responds]

## Recommended Monthly Narrative
[1–2 sentence theme that runs through all content this month]

## Narrative Pillars (3–4 content themes)
1. [Pillar name] — [one line]
2. [Pillar name] — [one line]
3. [Pillar name] — [one line]
4. [Pillar name] — [one line]

## Tone of Voice for This Month
[Specific guidance — assertive? data-led? empathetic? provocative? why?]

## Platform Strategy Notes
[Any platform-specific angle or opportunity this month — e.g. "TikTok: the [trending sound] is relevant to Pillar 2"]

## Suggested Content Mix
[By platform and format — e.g. "LinkedIn: 60% carousel, 40% static | TikTok: daily short-form, mix of POV and explainer"]
```

**PAUSE HERE.** Present the brief and ask for approval before proceeding.

### Phase 5 — Build the Full Calendar

**Only run after narrative brief is approved.**

#### 5a: Post Structure

Create content for each ACTIVE_CHANNEL based on the approved brief.

**Base volume:** 20 social posts + 4 video reels per month (one video per week). Scale per platform as follows:

| Platform | Monthly volume guidance |
|----------|------------------------|
| LinkedIn | 20 posts (5/week) |
| X | 25–30 posts (6–7/week, includes thread openers) |
| Instagram Feed | 12–16 posts (3–4/week) |
| Instagram Reels | 8–12 Reels (2–3/week) |
| Instagram Stories | Daily (5–7 frames/day — plan themes not individual frames) |
| Facebook | 12–16 posts (3–4/week) |
| TikTok | 20–30 videos (daily or near-daily) |
| YouTube Shorts | 8–12 Shorts (2–3/week) |
| YouTube Long-form | 2–4 videos (1/week or bi-weekly) |
| Threads | 10–15 posts (3–4/week) |
| Pinterest | 20–40 pins (5–10/week, can repurpose from other channels) |
| Reddit | 4–8 posts (1–2/week, value-first) |

For the Excel calendar, organise content by week, with each row = one piece of content on one platform. Group by week, then by platform within each week.

#### 5b: Post Data Structure

For each content piece, define all applicable fields:

```python
{
  "num": int,
  "week": int,                 # 1–4
  "pillar": str,               # narrative pillar
  "date": str,                 # "Mon 1 Jun"
  "platform": str,             # which platform this piece is for
  "topic": str,                # what this post is about
  "format": str,               # format specific to that platform (see Platform Profiles)
  "hook": str,                 # scroll-stopping opening — never starts with brand name
  "post_copy": str,            # creative copy — what goes ON the image/slide/screen
  "carousel_slides": str,      # slide-by-slide content if carousel (LinkedIn, IG)
  "video_script": str,         # production script if video/reel/Short
  "tiktok_script": str,        # TikTok-specific script (distinct format — see TikTok rules)
  "youtube_spec": str,         # YouTube-specific: title, thumbnail brief, description, chapters
  "stories_plan": str,         # Instagram/Facebook Stories frame plan
  "pinterest_spec": str,       # Pinterest: pin title, description, board, link target
  "visual": str,               # visual direction brief for the designer
  "meme_concept": str,         # meme format + panel descriptions (if applicable)
  "caption": str,              # platform-native caption (written per platform's rules above)
  "hashtags": str,             # hashtags for platforms that use them
  "cta": str,                  # specific CTA for this post
  "reddit_sub": str,           # target subreddit (Reddit posts only)
  "trending_audio_note": str,  # TikTok/Reels: note where trending audio should go
  "best_time": str,            # optimal posting time for this platform
}
```

#### 5c: Content Rules

**Universal rules (apply to every piece, every platform):**
1. Hooks never start with "We", "Our", or the brand name.
2. Every piece of content must make the ICP feel seen before the brand appears.
3. Week 1 = plant the problem. Week 2 = insight. Week 3 = proof. Week 4 = authority + action.
4. Never use: "leverage", "synergy", "excited to announce", "game-changing", "seamless", "robust".
5. Each post must have one clear idea. One hook. One CTA. No trying to do multiple things.

**Platform-native rules (apply per platform):**
- Follow every rule defined in the Platform Profiles section above.
- If content for a platform is just a shorter version of another platform's content, rewrite it — it's not platform-native.
- TikTok scripts must feel like TikTok. LinkedIn carousels must feel like LinkedIn. They are different products for different audience mindsets.

**Meme concept rules:**
Use meme formats where they would amplify the message:

| Post type | Best format |
|-----------|-------------|
| Ironic stat or data gap | Gru's Plan, This is Fine dog |
| Before/after contrast | Drake Pointing, Distracted Boyfriend |
| Challenging market assumption | Change My Mind, Always Has Been |
| Impossible choice | Two Buttons |
| Perception vs reality | Anakin / Padme |
| Escalating insight | Expanding Brain |
| Single impossible-sounding task | One Does Not Simply |

Each meme_concept must include: FORMAT name, panel-by-panel description, Caption line, STYLE notes.

**TikTok-specific script rules:**
- ON-SCREEN TEXT must appear at second 0 (not 3, not 5 — zero)
- First spoken word at second 0 — no silent intros
- Format hook: "Nobody in [industry] talks about this, but..." / "Here's what [X] actually means for [role]..." / "POV: you're a [ICP role] and..."
- Mark where trending audio should be added (editor decides actual track at production time)
- Flag Duet/Stitch opportunities where relevant
- Every TikTok script ends with a comment bait line: "Comment [word] if you want the full breakdown"

**Video script rules (non-TikTok):**
```
DURATION: ~[N] sec
FORMAT: [e.g. Text-on-screen + AI voiceover / Talking head / B-roll + VO]
STYLE: [visual aesthetic]
TONE: [tone guidance]
MUSIC: [music direction]

[0:00–0:XX] SECTION
VISUAL: [what's on screen]
ON-SCREEN: [text overlays]
VO: [voiceover]
```

Story arc: Hook (0–7s) → Problem (7–25s) → Reframe (25–40s) → Answer (40–52s) → CTA (52–60s).

**YouTube long-form spec format:**
```
TITLE: [SEO-optimised, under 60 chars, includes keyword]
THUMBNAIL BRIEF: [what appears — person, text overlay, brand element, contrast notes]
DESCRIPTION LINE 1: [hook + keyword — visible in search]
DESCRIPTION LINE 2: [what they'll learn / why to watch]
CHAPTERS:
  0:00 Introduction
  [1:30] [Chapter 1 name]
  [N:NN] [Chapter N name]
TAGS: [keyword1, keyword2, keyword3, keyword4, keyword5]
END SCREEN CTA: [subscribe / watch next video / visit website]
CARDS: [timestamps where to place mid-video cards + what they point to]
```

#### 5d: Generate and Run the Python Build Script

Write `build_calendar.py` tailored to ACTIVE_CHANNELS. The script:

1. Defines all content data as a list of dicts (per structure above)
2. Uses `openpyxl` to generate a styled Excel workbook
3. Creates sheets dynamically based on ACTIVE_CHANNELS:
   - **Overview** — narrative summary, platform breakdown, legend
   - **Full Calendar** — all posts across all platforms
   - **[Platform] Sheet** — one sheet per ACTIVE_CHANNEL with that platform's content in full
   - **Videos** — all video/reel scripts in wide-format
   - **Week 1–4** — content per week across all platforms
4. Columns shown vary by platform — LinkedIn posts show carousel slide column, TikTok posts show TikTok script column, YouTube posts show the full YouTube spec column
5. Applies colour coding by platform (each platform gets a distinct colour)
6. Saves to: `OUTPUT_DIR/[MONTH-YEAR]-[BRAND_NAME]-Social-Calendar.xlsx`

Run:
```bash
PYTHONUTF8=1 python3 build_calendar.py
```

---

## MODE B — Social Media Audit

**Trigger:** `/social-audit [BrandName]` or "audit my social media"

This mode produces a comprehensive audit report of the brand's existing social channels. It works from publicly available data (post performance signals, profile completeness, content patterns) and outputs a scored, actionable report.

### Phase B1 — Channel Discovery

If ACTIVE_CHANNELS is not specified, discover which platforms the brand is on:

1. WebSearch: `[BRAND_NAME] site:linkedin.com/company`
2. WebSearch: `[BRAND_NAME] site:x.com OR twitter.com`
3. WebSearch: `[BRAND_NAME] site:instagram.com`
4. WebSearch: `[BRAND_NAME] site:tiktok.com`
5. WebSearch: `[BRAND_NAME] site:youtube.com`
6. WebSearch: `[BRAND_NAME] site:facebook.com`
7. WebSearch: `[BRAND_NAME] site:pinterest.com`
8. WebSearch: `[BRAND_NAME] site:threads.net`

For each platform found, WebFetch the profile. Store as: `DISCOVERED_CHANNELS = [list with URLs]`

Present the list to the user and confirm: "I found [Brand Name] on [platforms]. Shall I audit all of these?"

### Phase B2 — Per-Platform Audit

For each channel in DISCOVERED_CHANNELS, assess:

**Profile Completeness (score /10):**
- Profile photo / logo: present and high quality? (2pts)
- Header / banner: present, on-brand, updated? (2pts)
- Bio / description: clear, includes keywords, includes CTA or link? (3pts)
- Contact info / website link: present and correct? (1pt)
- Pinned post / highlight: effectively used? (2pts)

**Content Performance Assessment (study last 20–30 posts):**
- Posting frequency: actual vs recommended for this platform
- Content mix: breakdown of formats (static / carousel / video / text / stories)
- Engagement rate: estimate from visible likes + comments relative to follower count
  - Excellent: >5% | Good: 2–5% | Average: 0.5–2% | Poor: <0.5%
- Best performing content: top 3 posts by engagement — what do they have in common?
- Worst performing content: bottom 3 by engagement — what patterns emerge?
- Hook quality: are first lines/frames strong? Rate: Strong / Weak / Absent
- CTA usage: are posts asking for something? Rate: Consistent / Occasional / Never
- Hashtag strategy: present? relevant? over/under-used?
- Visual consistency: consistent brand aesthetic? Rate: Strong / Moderate / Inconsistent
- Brand voice: consistent with the brand's tone? Rate: Consistent / Varies / Off-brand
- Cross-posting: is this platform getting original content or copy-paste from another? Rate: Original / Mixed / Cross-posted

**Audience Signals:**
- Follower count (note if growing, flat, or declining based on visible signals)
- Comment quality: are comments substantive or just emojis?
- Response rate: does the brand reply to comments?
- Community engagement: does the brand engage with others' content?

### Phase B3 — Audit Report Output

Generate a structured audit report:

```
# [BRAND_NAME] — Social Media Audit Report
Audit Date: [date]
Channels Audited: [list]

---

## Executive Summary

**Overall Social Health Score: [X/100]**

[3–5 sentence summary of the brand's overall social media health — what's working,
what's broken, and the #1 priority to fix]

**Top 3 Wins:**
1. [Specific thing that's working well]
2. [Specific thing that's working well]
3. [Specific thing that's working well]

**Top 3 Critical Issues:**
1. [Specific thing that needs fixing, with impact]
2. [Specific thing that needs fixing, with impact]
3. [Specific thing that needs fixing, with impact]

---

## Platform-by-Platform Audit

### [Platform Name] — Score: [X/100]

**Profile Health:** [X/10]
[Bullet list of what's complete / missing / needs updating]

**Content Performance:**
- Posting frequency: [X/week] vs recommended [Y/week]
- Content mix: [% by format]
- Estimated engagement rate: [%] — [Excellent / Good / Average / Poor]
- Hook quality: [Strong / Weak / Absent]
- CTA usage: [Consistent / Occasional / Never]
- Visual consistency: [Strong / Moderate / Inconsistent]
- Original vs cross-posted: [%/%]

**Best Performing Content Patterns:**
[What the top 3 posts have in common — format, topic, tone, hook style]

**What's Not Working:**
[What the lowest-engagement posts have in common]

**Platform-Specific Observations:**
[Anything unique to this platform's audit — e.g. "LinkedIn posts are burying the hook in line 3"
or "TikTok videos have no on-screen text — most views are sound-off"]

**Recommendations for [Platform]:**
1. [Priority 1 — specific, actionable, measurable]
2. [Priority 2]
3. [Priority 3]

[Repeat for each platform audited]

---

## Cross-Platform Analysis

**Brand Voice Consistency:** [Consistent / Varies / Fragmented]
[Observation on whether the brand sounds the same across platforms]

**Visual Consistency:** [Strong / Moderate / Inconsistent]
[Observation on whether the brand looks the same across platforms]

**Content Repurposing:** [Strategic / Ad hoc / None]
[Is the brand smartly adapting content or just copy-pasting?]

**Platform Prioritisation:** [Assessment of whether effort matches platform opportunity]

---

## Priority Action Plan

| Priority | Action | Platform | Expected Impact | Effort |
|----------|--------|----------|-----------------|--------|
| 1 | [Action] | [Platform] | [Impact] | Low/Med/High |
| 2 | [Action] | [Platform] | [Impact] | Low/Med/High |
| 3 | [Action] | [Platform] | [Impact] | Low/Med/High |
| 4 | [Action] | [Platform] | [Impact] | Low/Med/High |
| 5 | [Action] | [Platform] | [Impact] | Low/Med/High |
```

Save the audit report to: `OUTPUT_DIR/[BRAND_NAME]-Social-Audit-[DATE].md`

---

## MODE C — Competitor Intelligence and Gap Analysis

**Trigger:** `/competitor-audit [BrandName]` or "analyse my competitors"

This mode studies competitor social channels, builds a comparison matrix, and identifies content gaps and whitespace opportunities the brand can own.

### Phase C1 — Competitor Discovery

If COMPETITORS list is not provided, discover them:

1. WebSearch: `[BRAND_NAME] competitors alternatives [year]`
2. WebSearch: `best [brand's product category] tools [year]`
3. WebSearch: `[BRAND_NAME] vs [category] comparison`
4. Check G2, Capterra, or relevant comparison sites for the category

From results, identify 3–6 direct competitors. Present the list to the user for confirmation before proceeding.

Store as: `COMPETITOR_LIST = [name, website, social handles per platform]`

### Phase C2 — Competitor Channel Analysis

For each competitor in COMPETITOR_LIST, for each relevant platform:

**WebFetch** their social profiles and study the last 20–30 posts. For each, document:

- Follower count and estimated growth trajectory
- Posting frequency
- Primary content formats
- Top-performing content (topics, formats, hooks)
- Tone and brand voice
- Hashtag strategy
- Engagement rate estimate
- Notable campaigns or content series
- What they're NOT doing (gaps in their strategy)
- Any viral moments or breakout content in the last 30 days

Store as: `COMPETITOR_PROFILES = {competitor_name: {platform: data}}`

### Phase C3 — Gap Analysis

Compare BRAND_PROFILE + audit data (if Mode B was run) against COMPETITOR_PROFILES to identify:

**Content angle gaps:**
- Topics the ICP cares about that nobody is covering
- Questions the community is asking that no brand is answering
- Pain points surfaced in research (from RESEARCH_OUTPUT if available) that competitors are ignoring

**Format gaps:**
- Formats nobody in the space is using (e.g. no one is doing LinkedIn carousels, or no one is on TikTok)
- Format experiments that are working for adjacent categories but haven't been adopted here

**Tone gaps:**
- Is everyone too corporate? Is there room for a more human voice?
- Is everyone too casual? Is there room for a more authoritative, data-led tone?
- Is anyone doing humour? Memes? Educational content?

**Platform gaps:**
- Platforms the brand is absent from that competitors are growing on
- Platforms competitors are absent from that the brand could own early

**Engagement gaps:**
- Are competitors responding to comments? (If not, the brand can win on community)
- Are competitors engaging in Reddit / communities? (If not, whitespace opportunity)

**Narrative gaps:**
- Is there a story nobody is telling in the space?
- Is there a category position nobody is owning?

### Phase C4 — Competitive Intelligence Report

Generate:

```
# [BRAND_NAME] — Competitor Intelligence Report
Date: [date]
Competitors Analysed: [list]

---

## Executive Summary

[3–5 sentences on the competitive social media landscape — who's winning, why,
and where the biggest opportunity for the brand lies]

---

## Competitor Comparison Matrix

### LinkedIn
| Metric | [Brand] | [Comp A] | [Comp B] | [Comp C] |
|--------|---------|----------|----------|----------|
| Followers | | | | |
| Posts/week | | | | |
| Est. engagement rate | | | | |
| Primary format | | | | |
| Tone | | | | |
| Top content topics | | | | |
| Hashtag strategy | | | | |

[Repeat matrix for each platform where 2+ competitors are active]

---

## What's Working for Competitors

### [Competitor A]
**Platform:** [Platform] | **Format:** [Format] | **Why it works:** [Observation]
[Specific example of their best-performing content type and why it resonates]

### [Competitor B]
[Same structure]

---

## What's Not Working for Competitors

[Common failures or missed opportunities across multiple competitors]
- [Observation 1 — e.g. "All competitors have weak hooks — first line is always the brand name"]
- [Observation 2]
- [Observation 3]

---

## Whitespace Opportunities

### High-Impact Gaps (own these first)

1. **[Gap name]**
   - What it is: [Description]
   - Why nobody is doing it: [Reason]
   - How to own it: [Specific approach]
   - Platforms: [Where to execute]
   - Effort: Low / Medium / High

2. **[Gap name]**
   [Same structure]

### Medium-Impact Gaps (build toward these)

[2–3 more opportunities, lower urgency]

### Emerging Opportunities (monitor these)

[1–2 signals that aren't proven yet but worth watching]

---

## Recommended Competitive Positioning

**Content positioning:** [How the brand should position its content vs competitors]
**Tone positioning:** [The voice the brand should own that nobody else has]
**Platform positioning:** [Which platforms to prioritise and why]
**Format positioning:** [The formats the brand should lead with]

---

## 30-Day Competitive Action Plan

| Week | Action | Platform | Goal |
|------|--------|----------|------|
| Week 1 | [Action] | [Platform] | [Goal] |
| Week 2 | [Action] | [Platform] | [Goal] |
| Week 3 | [Action] | [Platform] | [Goal] |
| Week 4 | [Action] | [Platform] | [Goal] |
```

Save to: `OUTPUT_DIR/[BRAND_NAME]-Competitor-Intel-[DATE].md`

---

## MODE D — Full Suite

**Trigger:** `/social-suite [BrandName] [Month Year]`

Runs all three modes in sequence, using findings from each to inform the next:

1. **Mode B (Audit)** — understand the brand's current baseline
2. **Mode C (Competitor Intel)** — understand the competitive landscape
3. **Mode A (Calendar)** — build the calendar informed by both the audit findings and competitive gaps

The narrative brief in Phase 4 of Mode A explicitly incorporates:
- Weaknesses identified in the audit → areas to improve this month
- Gaps identified from competitors → angles to own this month
- Best-performing formats from the audit → double down this month

This is the most powerful way to run the skill — the calendar is not just research-informed, it's also audit-informed and competition-aware.

---

## Output Files

| Mode | Output file |
|------|-------------|
| Mode A | `OUTPUT_DIR/[MONTH-YEAR]-[BRAND]-Social-Calendar.xlsx` |
| Mode B | `OUTPUT_DIR/[BRAND]-Social-Audit-[DATE].md` |
| Mode C | `OUTPUT_DIR/[BRAND]-Competitor-Intel-[DATE].md` |
| Mode D | All three files above |

---

## Important Notes

- **BRAND_URL is required** for all modes. If not provided, ask before starting.
- **Mode A approval gate:** The narrative brief in Phase 4 is the only mandatory pause. Do not ask for approval at any other point.
- **Audit limitations:** This skill works from publicly visible data only. For impression counts, reach, click-through rates, and follower growth trends, the user should pull their native analytics from each platform's dashboard. The audit assesses what can be observed from public profiles.
- **Competitor discovery:** Always confirm the competitor list with the user before running Phase C2. Don't assume — the user may have strategic reasons to exclude certain competitors.
- **Reddit engagement:** Reddit is a community engagement channel, not a publishing channel. Never instruct the brand to post promotional content on Reddit. Value-first, practitioner-tone always.
- **TikTok audio:** Claude cannot select trending audio. Flag in the script where trending audio should be placed — the social media manager selects the actual track at time of production based on what's trending that week.
- **Requires:** Python 3.8+, `openpyxl` (`pip install openpyxl`), `/last30days` skill (optional but strongly recommended for Mode A Phase 3).
