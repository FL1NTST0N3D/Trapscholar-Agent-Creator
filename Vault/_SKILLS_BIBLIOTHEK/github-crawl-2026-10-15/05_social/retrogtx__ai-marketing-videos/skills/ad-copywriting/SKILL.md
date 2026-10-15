---
name: ad-copywriting
description: Write short-form video ad scripts, hooks, storylines, captions and CTAs for any app or product, and keep them inside platform ad policy (Meta, TikTok, YouTube). Includes safe-zone and caption specs for 1080x1920. Use when drafting or reviewing ad copy, VO scripts, on-screen text or end cards.
---

# Ad copywriting

## Storylines

Draft 4–6 storylines before writing any script. For each one, give:
- a title,
- a one-line angle,
- the psychology it uses (curiosity gap, insider knowledge, pattern interrupt, identity or aspiration, before/after, goal gradient),
- the proof it rests on.

Let the user choose. Expect some to be replaced; don't argue for rejected ones.

Angles that tend to work:
- **Borrowed attention:** build around well-known, trendy companies or events the audience already cares about. Use real names and facts as story facts, sourced from your own content.
- **The money or cause trail:** "You can't buy X. But you can own/use/learn what powers it."
- **The overlooked signal:** "Everyone watches X. Almost nobody watched Y."
- **Identity outcome:** "Six months from now, you could be the one your friends ask."

## Script shape (30–40s, about 170–190 wpm)

1. **Hook (0–2s):** topic plus outcome, instantly clear. A pattern interrupt or a concrete fact.
2. **Tension:** what most people miss, or the pain.
3. **Insight or payoff:** the story's reveal.
4. **What you get:** "[Product] is a [category] that [does X], with [concrete thing 1] and [concrete thing 2]." Say it plainly and show it on the real UI.
5. **Secondary value**, e.g. "Plus a course so you can do it yourself."
6. **CTA line:** one verb plus the brand plus the outcome. "Join X. Become the one who knows."

Store scripts as JSON, one object per line: `{id, text, pause}`. Keep a markdown doc next to it with the approved scripts, a source per factual claim, and a compliance note.

## Hooks

- The first 2 seconds must say what this is about and why the viewer should care.
- Shapes that work: specific receipt, myth-bust, stop-doing, curiosity gap, POV.
- The first frame must be visually distinct. Use at least 2 cuts in the first 3 seconds, and never open on a logo.
- Curiosity hooks suit cold traffic; problem/solution suits retargeting.
- Measure hook rate as 3-second views ÷ impressions. Under 25% means the hook is failing.

## Never

- Deny a real part of the offer to sound humble. If the product gives recommendations, say so.
- Make performance, income, health or results claims you can't substantiate, or guarantees. Performance claims are also a platform-policy problem.
- Put a price on creative unless the landing page matches exactly and the user wants it.
- Pitch free tiers or trials unless the user asks.
- Show jargon labels, internal feature names, or on-screen sentences that duplicate the VO.
- Use competitor brand marks, or public figures without a clear right to.

## Regulated categories (finance, health, credit, housing, employment)

- Frame the product as research or education, not advice. Put a disclaimer on the end card, e.g. "Research and education. Not investment advice."
- Platforms review the landing page too, so the ad and the page must agree.
- Don't imply past results predict future ones, or that a regulator endorses you.
- Declare a special ad category when it applies.

## Captions and safe zone (1080x1920, Meta Reels/Stories 2026)

- **Top:** keep the top 14% clear (y < 269), for the name and "Sponsored" label.
- **Bottom:** keep the bottom 35% clear (y > 1248), for the CTA button and caption. A disclaimer pushes this to 40%.
- **Sides:** keep 6% clear on each side (x < 65, x > 1015). The right rail icons go deeper, so keep x > 960 empty below mid-screen.
- **Key visuals** go inside x 65–1015, y 250–1150. The caption band is about y 1170–1310, and nothing important sits under it.
- **Caption style:** 2–4 words per chunk, bold sans, white with a stroke or dark plate, 56–80px. Keep one fixed anchor for the whole ad and make sure the caption text never duplicates on-screen titles.
- **Whisper spelling fixes:** fix only real mis-hearings of brand names. Over-eager rules break normal words (e.g. "everyone" became "every one").
