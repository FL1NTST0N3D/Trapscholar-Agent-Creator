---
name: blender-ad-pipeline
description: Build 100% 3D vertical video ads in Blender with free tools only. Covers headless EEVEE renders, realistic human figures (MakeHuman via MPFB) that pose, talk, react and actually hold phones and cards, constant-speed coin and particle flows, product UI as native geometry, captions and final edit in the Blender VSE, and parallel rendering. Use when an ad must be rendered in Blender or needs real 3D people. Uses the kit in kit/blender/.
---

# Blender ad pipeline

Everything is rendered in Blender, including captions (VSE text strips), the end card and the final edit. It needs no API keys and no paid generators.

## Setup

- **Blender:** 4.2 or later (tested on 5.2), EEVEE, headless: `blender -b -P shot.py`.
- **Humans:** install the MPFB extension (Blender Extensions → "MPFB"). Download the MakeHuman CC0 asset packs from static.makehumancommunity.org: system assets, hair, shirts, pants, shoes, skins, suits and faceunits. Unzip them into `~/Library/Application Support/Blender/<ver>/extensions/.user/blender_org/mpfb/data` (Linux: `~/.config/blender/<ver>/…`). Scripts that use humans must run **without** `--factory-startup`, or the add-on won't load.
- **Fonts:** put `Figtree-Black.ttf` and `Figtree-Bold.ttf` (OFL, Google Fonts) in `kit/blender/fonts/`.
- **Project layout:** set `AMV_PROJECT=/path/to/project`.
  - `shots/<ad>/<shot>.py`: shot scripts.
  - `shots/<ad>/edit_<ad>.py`: final assembly.
  - `audio/`: `<ad>-vo.json`, `<ad>-mix.wav`.
  - `sfx/`
  - `out/shots/<ad>/*.mp4`
- **Render:**
  - Preview: `kit/blender/render_shot.sh <ad> <shot> preview 1,40,90`.
  - Full: `render_shot.sh <ad> <shot>`. It takes a slot from `locked.sh` (`AMV_SLOTS`, default 2; renders are memory-bound).

A shot script starts with:
```python
import sys; sys.path.insert(0, "/path/to/ai-marketing-videos/kit/blender")
import k6, human, props
from k6 import *
reset(frames=150, samples=64)          # 1080x1920 @30
```

## Kit reference

- **`k6`:**
  - Scene: `reset`, `world_gradient(top, bottom, amb, amb_strength)`, `bloom`, `out`, `preview(path, frames, pct)`.
  - Materials: `soft`, `glow`, `flat`, `image_mat`.
  - Primitives: `sphere`, `box`, `cyl`, `text` (extruded 3D text).
  - Lights and camera: `area`, `sun`, `rig(target, key, fill, rim)`, `camera(loc, target, lens)`, `dof`.
  - Keys: `key(obj, frame, **props)`, `show(obj, frame, visible)`.
  - `wobble(obj, path, index, amp, period)`: an F-curve sine generator for idle motion; works headless.
  - `ease_all()`: Bezier easing everywhere, except objects with `obj["linear"]=1`, which stay LINEAR.
  - `PAL`: palettes by mood.
- **`props`:**
  - `phone(scale)`: screen on local −Y. `scale=0.10` is real phone size.
  - `coin`, `coin_stack`, `chip`, `rack`, `beam`, `pill`, `bubble`, `arrow`, `chart_line` + `draw_on`, `staircase`.
  - `flow(name, pts, n, f0, f1, r, pipe, travel, spin, ride)`: objects travel a smooth path at constant speed, sampled by arc length, evenly spaced, rolling with faces to camera.
- **`human`:** see the next section.
- **`edit.build(ad, shots, out_path, sfx, …)`:** VSE assembly with crossfades, whisper-timed caption chunks (`cue(vo, line, word)` gives the frame of a word), the VO/music mix and SFX. It reads `audio/<ad>-vo.json` from `kit/audio/vo.py`.

## Real humans (`kit/blender/human.py`)

```python
h = human.Human("Maya", "young_woman", loc=(0, 0, 0), rot_z=0, seed=3)   # idle=True by default
h.pose(1, "think"); h.face(1, "smile"); h.talk(20, 80); h.gesture(20, 80); h.react(90, "surprised", "grin")
ph, screen = props.phone("Phone", scale=0.10)
h.grip(ph, 1, "R", pose="phone")            # phone in hand, screen to her face
h.grip(ph, 60, "R", pose="rest")            # later: re-grip at another pose (offsets are keyed per call)
card = ...                                    # any object whose face is local -Y
h.between_hands(card, 1, "hold", face_to=cam) # held by the side edges, face to camera
human.realistic_look()                        # AgX colour management for skin
```

- **Presets:** young_man, young_woman, black_man, asian_woman, suit_man, older_woman. Override outfits with `overrides={"clothes": [...]}`.
- **Poses** are armature-space aim directions per arm (the character faces −Y; its left is +X), not Euler angles. MakeHuman bone axes are unintuitive, so aiming is the reliable way.
  - Built in: rest, phone, hold, wave, point, cheer, think, arms_crossed, present, shrug.
  - Add your own to `human.POSES` in a per-ad `lib.py`.
- **Faces:** ARKit face-unit shape keys drive neutral, smile, grin, surprised, worried and focused, plus eye look and jaw for `talk`.
- **Idle is on by default:** breathing, weight shift, head drift, eye darts, blinks and relaxed fingers.
  - Vary the `seed` per person, and give crowds different poses, staggered timing and some talking. Identical crowds read as "zombies".
  - Don't add your own blink calls on top.
- **`grip`:**
  - Turns the palm to the head (or to `face_to`, e.g. the camera for show-and-tell), with the fingers across the body.
  - Seats the object portrait with its back on the palm, offset toward the wrist so the fingers wrap the far edge (`edge_in`).
  - Solves each finger segment and the thumb so nothing penetrates.
  - Don't re-pose that arm or call `hand()` on that side while the object is held.
- **`between_hands`:** `mode="sides"` puts the palms on the side edges with the fingers behind. `fit=True` scales the card to the palm span; widen the pose rather than shrinking the card.
- **Look:**
  - AgX suits skin but dulls flat UI and glows, so keep UI close-ups and end cards on Standard.
  - Small area lights near a face blow out the subsurface skin and make it look chalky. Warm the key light instead.
- **Clothing:**
  - Women get nipple and breast-point reduction targets so tight tops read clean.
  - Knit sweaters shimmer at distance.
  - Hide body verts under clothes (Mask modifier) if skin pokes through.

## Money, coins and particle motion

- **Speed and spacing:** constant speed and even spacing via `props.flow`. A Bezier-eased path `offset_factor` accelerates and reads as sloppy.
- **Density:** keep objects sparse, at least 2.5 diameters apart and about 5 visible per lane. Dense columns read as "beads" or "chains".
- **Direction:** faces to camera. Lanes cross the frame diagonally or horizontally, not straight down at the viewer.
- **Falls:** a gravity arc with spin about one axis that lands flat. Nothing interpenetrates signs or logos.

## Product UI as geometry

- **Build real surfaces:** report cards, pick or plan cards, lesson lists, chat screens. Use panels, extruded text, icons and geometry check marks, never a "^" glyph.
- **Rounded corners:** bevels are capped by thin slab depth, so build a real rounded-rect mesh for panels.
- **Chat screens** need a real input field with typed text, a blinking caret and a geometry send arrow, plus a keyboard so half the screen isn't empty.
- **Sheen:** a narrow bright strip clipped to the card face, never a translucent slab sweeping across.
- **Big numerals** need a dark plate behind them to read.
- **No PNGs:** don't import textures rendered elsewhere if the brief says 100% Blender.

## Pitfalls

- Never call `read_factory_settings` from an MCP or live session; it unloads add-ons.
- `transform_apply(location=False)`.
- Use `filter_size`, not `film_filter_size`.
- VSE strips: `scene.sequence_editor.strips`.
- Live MCP sessions cache Python modules, so rename a kit module rather than reloading it.
- The render dir must be recreated each run (`rm -rf` then `mkdir`) to avoid empty-glob and stale-frame bugs.
- Tiny humans in wide shots, cut-off signs, and anything in the caption band all get flagged. Check with `render-precheck`.
