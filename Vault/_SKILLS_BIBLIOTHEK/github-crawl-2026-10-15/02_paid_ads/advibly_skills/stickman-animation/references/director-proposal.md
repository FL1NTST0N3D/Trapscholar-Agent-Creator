# Director's proposal (Phase 2)

Plan the whole video in text before any credit is spent. The proposal is the approval gate: the
user reads it, edits it, and approves the current version. Nothing renders before that.

## 1. Find the idea

Pull from the brand brief, dossier, the product, or the user's copy. Answer in one sentence each:

- What single thing should the viewer feel or realize by the end?
- What is the hook in the first three seconds? A stick-figure video lives or dies on its opening.
- What is the most literal, surprising, or funny way to draw that idea with line art?

If the idea does not fit in one sentence, it is not sharp enough yet.

**Source fidelity.** Keep the source's core claim, names, and numbers. Strengthen a weak opening,
cut repetition and side branches from long sources, and expand a thin source with an example, a
progression, or a callback. Never invent statistics, quotes, research, or product claims.

## 2. Pick a narrative pattern

Choose the one that fits; do not force it.

- **Commercial**: pain point, consequence, product reveal, how it works, proof or use case,
  benefit and CTA.
- **Educational**: surprising hook, setup, mechanism, consequence, practical meaning, takeaway.
- **Motivational**: hook, recognition, escalation, reframe, action, payoff.
- **Gag**: setup, escalation, punchline that is the product (3 clips suit this).

Every clip gets a **different narrative job**. The last clip calls back to the opening image or
idea.

## 3. Build each clip from three timed beats

| Beat | Job |
|---|---|
| `0-3s` | Establish, or inherit the previous clip's landing state. |
| `3-7s` | Transform, escalate, or explain the metaphor. |
| `7-10s` | Climax, then form the landing state the next clip inherits. |

Require a perceptible visual change every two to three seconds. Use at least **four** devices per
clip from this menu, every one serving the spoken idea:

- expressive figure action (a fall, a sprint, a push, a collapse, a leap)
- environmental transformation (the floor becomes a treadmill, a wall folds into a road)
- a concrete metaphor made literal (a thought becomes a tangle, fear becomes a cage)
- an icon-only diagram, arrow, or symbol (no letters or numbers)
- particles, energy, fluid, explosion, or light
- a camera move: push, pull, pan, orbit, tilt, shake, or tracking
- a foreground wipe or an object crossing the lens
- a match cut, shape morph, or motion-matched transition
- interaction with a second figure or an oversized object (a giant gavel, a towering phone)

**Scale is the cheapest density.** Tiny figures against huge graphic objects (columns, frames,
tools, devices) give line art cinematic weight. Solid black or white silhouettes of big objects
are allowed; shading is not.

Sparse clip: add a metaphor, an interaction, or a transformation. Overloaded clip: cut simultaneous
events, keep the three beats.

## 4. Name every transition interface

Each clip ends on a visible state the next clip starts from. Name both sides in the proposal:

- a shape that fills the frame (lines, a color flood, a glass fragment across the lens)
- an object in motion (a beam, a ball, a paper plane) that continues
- a pose (a raised foot that lands in the next clip)
- a travel direction (running right, the camera keeps tracking right)
- a shape morph (bars that become vines, a sun that becomes a coin)

The landing state of clip N is drawn once, as the opening still of clip N+1. Mark a seam as a
**hard cut** only when the story wants a jolt; that clip gets no end frame.

## 5. Composition by aspect ratio

- `16:9`: stage across left, center, and right; lateral tracking; horizontal match cuts;
  deliberate negative space, reserved where an overlay will sit.
- `9:16`: foreground and background depth, vertical reveals, stacked motion, foreground passes;
  keep key action out of the top 10 percent and bottom 20 percent (platform UI).
- `1:1`: generated as 9:16 and cropped to the center square, so every important event stays in the
  middle square. Compact staging, short travel, radial motion.

Changing the ratio means new staging, camera paths, transition geometry, and overlay placement.

## 6. Theme and palette

- **Light**: flat, uniform, pure white canvas; black figures and line art.
- **Dark**: flat, uniform, pure black canvas; white figures and line art.

Up to three saturated accents across the video, each with one meaning, named in plain words:
"vivid red for rejection", "electric blue for insight", "warm gold for action". For a brand ad,
translate the brand's primary hex into its nearest plain color name ("the brand's #1FA971" becomes
"emerald green") and assign it the product and the payoff. Generally one dominant accent per clip.
Never write a color code in the proposal's prompts or any generation prompt.

## 7. Text and product

- Generations carry **no visible words, letters, or numbers**. Icon-only bubbles, cards, clocks,
  meters, and notifications.
- Optional overlays: two to five words each, listed after the table with the clip, the time, and
  the position. They become `texts` in the final composition.
- The product, when featured, is a flat line-art prop in the brand accent with its logo copied
  from the photo. Keep it large (30 to 40 percent of frame) on the clips that show it.

## 8. Narration and voice

- English by default, ~2.3 to 2.5 words per second: 20 to 25 words per 10 second clip, 130 to 150
  words for a 60 second video. Simplify wording before asking for faster delivery.
- Break lines at natural sentence boundaries per clip. Read straight through, the lines are one
  script.
- Voices: `leo` (deep announcer), `rex` (confident, punchy CTA), `ara` (warm), `sal` (smooth,
  calm), `eve` (bright, energetic). Default `eve` for explainers and motivational pieces, `leo` for
  a hard-sell ad. One voice for the whole video.

## 9. The proposal format

Present in this order, in the user's language:

1. **Title** (and reference-language title if the user writes in another language)
2. **Core message** and **hook**
3. **Format**: theme, aspect ratio, composition strategy in one line
4. **Narrator**: voice, delivery, word count, estimated duration
5. **Accents**: up to three plain color names with meanings
6. **Music**: mood, the emotional turn and its timestamp; **cadence**: on_twos or smooth, with why
7. **Clip table**:

| Time | Purpose | Beats (0-3 / 3-7 / 7-10) | Devices and camera | Narration | SFX | Interface to next clip |
|---|---|---|---|---|---|---|

Add a `Translation` column after Narration when the user writes in another language.

8. **Optional overlays** (clip, time, position, exact words)
9. **Credit estimate**
10. **Next step**: approve and render; revise a named clip or line; or change a global setting.

## 10. Cost shape

Per video: one gpt-image-2 still per clip, one Omni 1.1 clip per clip (10s at 720p), one short
voiceover per clip (~0.03 credits per 1000 characters), one or two music beds (~0.3 credits each),
one composition (0.4 credits). Check current per-call prices in the tool responses and present the
total for this clip count before the user approves. Re-rolls cost extra; say so.

## Proposal checks (repair before sending)

- Source, theme, and aspect ratio are known; nothing was silently defaulted.
- Narration word count matches the length (20 to 25 words per clip).
- Every clip has a distinct purpose, three timed beats, and at least four relevant devices.
- A visible change roughly every two to three seconds.
- No more than three accents, all in plain color names; no color codes anywhere.
- No visible text planned inside any generation; overlays listed separately.
- Every adjacent pair has a named interface or a deliberate hard cut.
- The last clip returns to the central message.
- No unsupported facts, statistics, quotes, or claims were added.
- The proposal ends by asking for approval and contains no generation prompts.
