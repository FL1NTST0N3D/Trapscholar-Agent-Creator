# Clip prompts (Phase 4)

One `advibly_generate_video` call per clip:

```
model: "gemini-omni-flash-1.1"
aspect_ratio: "9:16" or "16:9"
duration: 10
resolution: "720p"
start_image_url: <this clip's still>
end_image_url: <next clip's still>      # omit on the last clip and on a planned hard cut
brand_id, project_id
```

No `reference_image_urls` with a start frame (it changes the mode). No `mode`. Both anchors are
stills, so all clips render in parallel.

## Why the prompt is written this way

- **Omni 1.1 treats the start frame as a suggestion** unless told to hold it. Every prompt opens by
  ordering the first frame kept exactly, then adds motion.
- **The model adds shading, gray tint, and 3D volume** to flat line art over ten seconds. The lock
  and negative blocks repeat on every clip.
- **Each prompt is standalone.** The model never sees the other clips or the proposal. Repeat the
  theme, figure, palette, and negatives every time.
- **2000 character cap.** The blocks below are compact on purpose. Spend the remaining budget on
  the three beats.

## Clip contract (write in this order)

```
1. HOLD      The first frame is the start image exactly: keep its composition, line weight, figure
             design, and colors, then animate.
2. LOCK      theme + figure + palette in one compact paragraph (below)
3. STYLE     "Rapid scene changes and kinetic motion-graphics transformations while preserving an
             identical stick figure design, constant line weight, and strict temporal consistency."
4. [0-3s]    what moves first, where, the camera
5. [3-7s]    the transformation or escalation, the camera, which accent carries meaning
6. [7-10s]   the climax, then the landing state (it must match the end image when one is attached)
7. AUDIO     synchronized SFX tied to visible events; no voice, no music
8. NEGATIVE  compact block (below)
```

### LOCK: light theme

```
Flat 2D line animation on a flat, uniform, pure white canvas with no gray tint, texture, gradient,
shadow, or lighting at any moment. Stick figures in clean black lines of one uniform medium weight:
hollow circle head with no face, no hair, no clothing, single-line limbs, fixed proportions.
Accents only {ACCENT 1} ({meaning}), {ACCENT 2} ({meaning}), as flat solid color.
```

### LOCK: dark theme

```
Flat 2D line animation on a flat, uniform, pure black canvas with no gray lift, texture, gradient,
glow haze, or lighting at any moment. Stick figures in clean white lines of one uniform medium
weight: hollow circle head with no face, no hair, no clothing, single-line limbs, fixed proportions.
Accents only {ACCENT 1} ({meaning}), {ACCENT 2} ({meaning}), as flat solid color.
```

List only the accents this clip uses. Plain color names only; never a code.

### Timed beats: how to write them

- Say **where** things start and end in frame (left third, lower right, across the full width).
- Say **what changes into what** (the bars twist into vines; the dot splits into hundreds of lines).
- Name the **camera** per beat (slow push toward the figure; lateral track right; orbit; a short
  shake on impact; a whip pan). The still owns the first composition; the beats own everything
  after.
- Keep one primary event per beat plus one or two secondary motions.
- End beat 3 by stating the landing state in the same words the next clip's still was drawn from.
- Icons stay icon-only: "an icon-only envelope", "a clock with unmarked hands".

### AUDIO

```
Audio: synchronized sound effects only, {3 to 5 specific SFX tied to the beats}. No narration, no
dialogue, no singing, no music.
```

The narrator and the music are added in the composition. Anything spoken in a clip collides with
them.

### NEGATIVE

```
No words, letters, numbers, captions, subtitles, color codes, logos, or watermarks. No 3D, no
shading, no gradients, no shadows, no photorealism, no faces, no hair, no clothing, no extra limbs,
no changing proportions or line weight, no line flicker or boiling, no inverted theme colors, no
unexplained colors, no unintended characters.
```

Product clips: "no letters except the product's logo exactly as in the start image".

## Clip QA checklist

Pull a mid frame and a late frame (`ffmpeg -ss 5 -frames:v 1`, `-ss 9`) or watch the clip.

- [ ] The first frame is the start still, not a redesign.
- [ ] Canvas stays flat white or flat black the whole clip; no tint, gradient, or vignette creeps
      in.
- [ ] No shading, 3D volume, or rendered lighting appears.
- [ ] Figures keep the style plate's design; no face, hair, or clothing grows in; no extra limbs.
- [ ] All three beats happen, with a visible change every two to three seconds; nothing idles.
- [ ] Accents stay on their meanings.
- [ ] No visible text.
- [ ] The last second lands on the next clip's still (or holds a clean state on the last clip).
- [ ] SFX only; no voice or music in the clip audio.

Fix the specific failure: redesigned start frame, strengthen HOLD and name the elements to keep;
shading, move the theme sentence to the front of LOCK and add "flat vector at every moment"; idle
middle, give beat 2 a bigger transformation. Two retries per clip. If a clip still shades, re-roll
its still on `nano-banana-2` and re-animate.

## Other models

- **User named a model**: use it for every clip and adapt only the parameters its schema supports.
  `gemini-omni-flash` (v1) takes no end frame, so seams become hard cuts or motion-matched cuts.
- **One move must run past 10 seconds**: `seedance-2.0`, `mode: "pro"`, `duration` up to 15,
  start and end stills. Ask first; it costs more per second. Seedance rejects words like
  `cinematic`, `stunning`, `8k`, `studio`; say "flat 2D line animation" instead.
