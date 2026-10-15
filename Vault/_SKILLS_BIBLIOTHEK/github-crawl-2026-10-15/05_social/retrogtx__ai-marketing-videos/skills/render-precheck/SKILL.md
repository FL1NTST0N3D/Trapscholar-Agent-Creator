---
name: render-precheck
description: Review loop for AI-built video ads. Check each shot in the tool before the full render, using low-sample stills with safe-zone and caption-band overlays plus 100% close-ups of hands, held objects, faces and clothing. Then review the final mp4 the same way. Use before every full render and before telling the user an ad is done. Uses kit/blender/precheck/.
---

# Precheck before render

Signing off from small contact sheets let these reach the client: fingers through cards, phones floating beside hands, phones lying on flat palms, nipples through tight tops, skin showing through a sweater, chalky faces, captions over the product, and coins that looked like beads. Every one would have shown up in a 10-second preview still. **Check in the tool before rendering, and review at 100%.**

## Blender precheck

```
AMV_PROJECT=/path/to/project kit/blender/precheck/run.sh <ad> <shot> "1,24,60,110" \
  "hand@24@Maya:wrist.R, face@24@Maya:head@0.5, top@24@Maya:spine03, phone@60@Phone"
```

This writes `/tmp/amv/<ad>/precheck/<shot>-precheck.png`:
- **Top row:** main-camera stills at 16 samples and 40% scale, with the safe zone (green) and caption band (yellow) drawn on.
- **Bottom row:** 600px close-ups from a temporary camera aimed at each `Rig:bone` or object at the given frame. The optional last number is the camera distance.

In Remotion, render `npx remotion still` at the same key frames and draw the same overlays with ffmpeg `drawbox`.

## What to check (at 100%)

- **Held objects:**
  - Phones sit in the hand, with the fingers wrapping an edge and the thumb off the screen.
  - Cards are held by their edges, with no fingers through them or over the text.
  - Check a front and a side angle, at every frame where a grip or pose changes.
- **Framing:**
  - Product surfaces, faces, numbers and speech bubbles sit inside the safe zone.
  - Nothing important is in the caption band.
  - Nothing is cut off at the frame edge, and no tiny unreadable humans or cards.
- **People:**
  - Alive and varied: different poses, staggered timing, some talking and reacting.
  - Faces lit warm, not chalky. Clothing clean.
- **Motion:** constant-speed, sparse, correctly oriented objects. Nothing clips through signs. Add mid-motion stills.
- **UI:** readable at phone size. Inputs look real: text, caret, send icon. No placeholder glyphs.
- **Compliance:** no unsubstantiated claims, no stray price, correct disclaimer on the end card.

## Workflow with builder agents

1. The builder sends precheck sheet paths and waits.
2. The coordinator views every sheet at full size and approves or sends specific fixes: what is wrong, where, and the likely cause.
3. Repeat until clean. Only then run the full render through the render-slot lock.
4. After assembly, the builder sends overlay contact sheets and 100% crops of every held object and face, pulled from the final mp4.
5. The coordinator reviews them before reporting to the user, and states any known compromise plainly.

When the shared kit changes behaviour (defaults, parameter meaning), tell every builder immediately. Stale assumptions cause silent regressions.
