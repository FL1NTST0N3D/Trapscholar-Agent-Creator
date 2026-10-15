# Opening stills (Phase 3)

One still per clip, made with `advibly_generate_image` (`model: "gpt-image-2"`,
`quality: "high"`, `on_brand: false`, `aspect_ratio` `"9:16"` or `"16:9"`, `brand_id`,
`project_id`). Each still is the **first frame of its clip** and the **landing frame of the clip
before it**, so draw exactly the state the proposal's transition interface names.

`on_brand: false` always: the brand kit would recolor the scene and stamp a logo. The brand shows
up through the accent color and the product prop.

## Prompt structure

```
[STYLE LOCK]   theme-aware, verbatim every still
[FRAME]        composition, figure placement and pose, objects, accents, camera framing
[PALETTE]      the accents in plain color names and where each appears in THIS frame
[NEGATIVE]     verbatim every still
```

Stay under 2000 characters. Never write a color code anywhere in the prompt.

### STYLE LOCK: light theme (verbatim)

```
Flat 2D minimalist line-art motion-graphics frame. A completely flat, uniform, digitally pure white
canvas with no gray or off-white tint, no paper texture, no grain, no gradient, no vignette, no
shadows, no lighting. Stick figures and objects are drawn in clean black lines of one uniform
medium weight. Each stick figure has a hollow circular head with no face, no hair, no clothing, a
single-line torso and single-line limbs, and stable human proportions. Large objects may be solid
flat black silhouettes or black line art. Perspective comes only from lines and scale, never from
shading.
```

### STYLE LOCK: dark theme (verbatim)

```
Flat 2D minimalist line-art motion-graphics frame. A completely flat, uniform, pure black canvas
with no gray lift, no texture, no grain, no gradient, no vignette, no glow haze, no lighting. Stick
figures and objects are drawn in clean white lines of one uniform medium weight. Each stick figure
has a hollow circular head with no face, no hair, no clothing, a single-line torso and single-line
limbs, and stable human proportions. Large objects may be solid flat white silhouettes or white
line art. Perspective comes only from lines and scale, never from shading.
```

If the proposal locked a dot-eyes face, replace "with no face" with "with two small dot eyes and a
simple line mouth" in both the still and clip locks, for every clip.

### PALETTE (fill per still)

```
Accent colors are only {ACCENT 1} for {meaning}, {ACCENT 2} for {meaning}, and {ACCENT 3} for
{meaning}, used as flat solid color with no gradients. In this frame {which accent appears on
which object}. Everything else is {black on white | white on black}.
```

Drop unused accents from the sentence rather than writing "none".

### NEGATIVE (verbatim)

```
No words, letters, numbers, captions, labels, signs, interface text, color codes, logos, or
watermarks. Speech bubbles, cards, screens, clocks, and meters are icon-only. No 3D rendering, no
shading, no cel-shading, no gradients, no drop shadows, no cross-hatching, no texture, no
photographic elements, no realistic anatomy, no faces, no hair, no clothing, no sketchy or double
lines, no motion blur.
```

For a product frame, change the first sentence to "No words, letters, or numbers except the
product's own logo copied exactly from the reference."

## FRAME: what to write

Write what the clip's first frame shows, as the proposal's interface describes it:

- **Composition for the ratio**: where the figure stands (left third, center low), what fills the
  rest, where the negative space is. For `1:1` output, keep everything important inside the
  centered square of the 9:16 frame.
- **The figure's pose**, specific enough to read in one glance ("crouched with both hands over the
  head", "mid-stride running right, right foot raised").
- **Objects and scale**: the metaphor objects and how big they are relative to the figure.
- **Camera framing**: wide, medium, low angle, looking down a corridor of columns.
- **A frame-filling interface** (a tangle of lines, a color flood, a fragment across the lens) is
  drawn as that fill, with the figure hidden or barely visible if the interface says so.

One readable idea per frame. The clip adds the motion; the still does not need to show everything
that happens.

## Product prop

On clips that show the product, attach its photo in `reference_image_urls` after the style plate
and describe it as: "the product from the reference, redrawn as a flat 2D line-art icon in
{BRAND ACCENT} with a uniform {black | white} outline, its logo copied exactly, simple flat
silhouette, no photographic shading, large in frame." Never pass `product_id` (it switches to
editing the raw photo). Clips without the product get no product reference.

## Reference chain

1. Clip 1's still is the **style plate**. Render it alone, show it, get a yes.
2. Every other still attaches the style plate URL first in `reference_image_urls` and adds "Match
   the line weight, head size, and figure proportions of the first reference image exactly."
3. Render stills 2 onward in parallel.
4. A user-supplied stick figure or brand character replaces the style plate as the first
   reference.

## Still QA checklist

- [ ] Canvas is flat pure white (light) or pure black (dark): no tint, gradient, vignette, texture.
- [ ] Figures: hollow circle head, no face (unless locked), single-line limbs, same proportions as
      the style plate.
- [ ] One uniform line weight; no sketchy, double, or tapered lines.
- [ ] No shading, gradients, or 3D volume anywhere.
- [ ] Accents appear only on their assigned meanings; no stray colors.
- [ ] No visible words, letters, or numbers (product logo excepted).
- [ ] The frame matches the proposal's interface state for this clip.
- [ ] Correct aspect; key action inside the platform-safe area (and the center square for `1:1`).

Two re-rolls per still. If shading persists, try that one still on `nano-banana-2` with
`resolution: "2K"`, re-anchored on the style plate.
