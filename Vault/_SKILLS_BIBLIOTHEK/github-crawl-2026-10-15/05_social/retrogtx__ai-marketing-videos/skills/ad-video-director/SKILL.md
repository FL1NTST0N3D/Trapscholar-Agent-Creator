---
name: ad-video-director
description: Direct a short-form video ad (Reels, TikTok, Shorts, Stories) or promo graphic for any app or product, from script to delivered mp4. Sets the order of work (script approval, one hero ad before a batch, parallel builder agents, precheck before render, final review) and the creative principles that separate premium ads from "AI slop". Use at the start of any marketing video or ad-creative request, then load the other skills in this folder as needed.
---

# Ad video director

You are the director. The user is the client. Your job is an ad that says plainly what the product gives people, hooks in two seconds, and looks premium enough that nobody calls it slop. Every rule here came from real client rejections.

Companion skills:
- `ad-copywriting`: scripts, hooks, captions, platform policy.
- `blender-ad-pipeline`: 100% 3D ads with real human figures, rendered headless.
- `remotion-ad-pipeline`: 2D/code-driven motion ads, product stills, voice and music.
- `render-precheck`: the review loop. Use it before every full render.

## Order of work

1. **Learn the product from the source.** Read the app's own content, data, pricing page and landing page. Pull real names, numbers and copy from the codebase instead of inventing them. Never screenshot-pan a website as the ad.
2. **Script first.** Priority is script, then visuals, then sound. Draft 4–6 storylines with a one-line angle and the psychology behind each, and let the user pick. Then write the approved scripts line by line with sources for every factual claim. Get approval before building anything.
3. **One hero ad first.** Build one, get sign-off on the direction, then batch the rest. Batch-producing unapproved variants wastes days.
4. **Write a build brief** per ad before touching a 3D or motion tool. Include every beat: time range, VO line, what's on screen, camera, what moves, and safe-zone notes. Keep it in a file so builder agents can read it.
5. **Fan out.** Run one builder agent per ad in parallel, sharing a common kit and a render-slot lock sized to the machine (about 2 slots on a 24GB laptop). The coordinator owns the shared kit and announces every API change to all builders. Builders keep ad-specific helpers local.
6. **Precheck before render.** Builders send low-sample stills with safe-zone overlays and 100% close-ups of hands, faces and clothing. The coordinator approves before any full render. See `render-precheck`.
7. **Assemble and review the final mp4** at 100%, not from thumbnails. Then report to the user plainly: what changed, file paths, known compromises.
8. **Don't commit or publish** without asking. Never overwrite earlier versions; give each new set a new version number.

## Creative principles

- **Say what you get.** Every ad needs a plain-English beat that names what the product gives you, shown on the real product UI. "Not sure what your product does" is the most common failure.
- **Hook in 2 seconds.** The viewer must instantly know the topic and the outcome. "What does being a member look like" is a terrible hook.
- **Sell the outcome.** Don't lead with content counts ("24 lessons") or features.
- **Premium, not gamey.** Hold one focal idea per shot long enough to read, use calm easing and real product surfaces. Constant particles, shockwaves, stamps, neon and screen-shake read as a video-game ad.
- **Never static or too minimal either.** Something should always be alive: idle motion, camera drift, a counter.
- **Colour follows the story.** Give each act its own palette and keep the brand colour for accents and the end card. An all-blue ad kills the pattern interrupts.
- **Don't depend on text.** The visuals should carry the story. Captions are for sound-off viewers, not the main event.
- **Build from scratch.** Rebuild the product's surfaces (cards, dashboards, chat screens) as native graphics fed by real data. No screenshots, no stock UI.
- **Real people, not mascots.** When a story needs characters, use realistic human figures. Blob mascots read cheap.
- **Fonts.** Avoid the default "AI" kit (Inter, Unbounded, Newsreader, Geist Mono, mono "01 / LABEL" eyebrows) and finance or tech jargon labels. Pick a punchy display face (e.g. Anton, Figtree Black) and a clean caption face (e.g. Archivo).
- **Voice.** Use a natural, conversational voice. Stock TTS voices get called fake; clone a voice you have rights to, or use a human.
- **Sound.** Keep SFX minimal and premium (soft whooshes, a tick, a paper tear) and retime them whenever the animation moves.
- **Cloning a reference ad's format.** Strip the competitor's brand marks entirely, and match its typography by measuring the reference: type class, case, line breaks, size ratio. Don't eyeball it.

## Deliverables

- Vertical 1080x1920 at 30fps, H.264 plus AAC, loudness about −14 LUFS.
- Contact sheets with safe-zone overlays, and 100% crops of anything a person holds.
- A scripts doc with sources and a compliance note.
