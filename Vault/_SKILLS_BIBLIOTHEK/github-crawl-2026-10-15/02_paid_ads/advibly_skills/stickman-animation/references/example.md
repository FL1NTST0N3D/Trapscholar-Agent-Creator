# Worked example (ILLUSTRATION ONLY)

Load only when a concrete example resolves ambiguity. Reuse the method and the level of detail.
Never reuse the topic, the metaphors, the palette, or the wording.

The method is adapted from the open-source Stickman Video Director skill by kaomei (MIT):
three timed beats per ~10 second clip, named interfaces between clips, plain color names, and no
text inside generations.

## Kickoff

Brand: a personal budgeting app (fictional), primary color #16A34A. User: "stickman ad about
losing track of subscriptions". Assistant asked for theme, ratio, and length in one message. User:
"light, 9:16, 30 seconds".

## Proposal excerpt

- **Title:** The Subscription Swarm
- **Core message:** Small forgotten subscriptions add up; the app finds them and cancels them in
  one place.
- **Hook:** a single coin rolls away from the figure and multiplies into a swarm.
- **Format:** light theme, 9:16, depth and vertical reveals, key action in the middle 70 percent.
- **Narrator:** `eve`, bright and quick, 62 words, ~28 seconds.
- **Accents:** vivid red for money leaking away; emerald green for the app and control.
- **Music:** light ticking pizzicato, tense; lifts into a bouncy beat at 20s. **Cadence:** on_twos
  (pose-driven comic action, short camera travel).

| Time | Purpose | Beats (0-3 / 3-7 / 7-10) | Devices and camera | Narration | SFX | Interface to next clip |
|---|---|---|---|---|---|---|
| 0-10s | Hook, recognition | Figure drops one red coin, it rolls down / the coin splits into dozens of small red coins with tiny wings, circling the figure / the swarm rises and blocks the frame | metaphor made literal, particles, figure action, push-in then tilt up, frame fill | "Ever check your bank app and wonder where it all went? It's not one big purchase. It's a dozen tiny ones you forgot." | coin drop, jingle multiplying, wing flutter | red coin swarm fills the whole frame |
| 10-20s | Escalation | Inside the swarm the coins form a giant red conveyor belt / the figure runs up it but slides back as icon-only cards drop onto it / the belt tips toward camera, the figure falls, an emerald phone icon catches them | environment transformation, oversized object, interaction, lateral track, shake | "Streaming, apps, trials that never ended. Each one quietly takes a little more, every single month." | conveyor rumble, card thuds, slip whoosh, soft catch | emerald phone icon held large in the figure's arms, center |
| 20-30s | Payoff and CTA | Phone screen shows icon-only cards / the figure swipes, each card pops into an emerald check and coins fly back into a jar / pull back to a calm figure beside a full jar | shape morph, particles, match cut card to check, pull-out, negative space top | "See every subscription in one place, cancel what you don't use in a tap, and keep your money yours." | swipe, pop, coins landing, bright chime | final hold, overlay space top |

**Overlays:** "Where did it go?" clip 1, 1.5s to 4s, top. "Keep your money." clip 3, 7s to 10s,
top, white on emerald pill.

## Still for clip 2 (the landing frame of clip 1)

```
{STYLE LOCK: light theme}

Vertical 9:16 frame. The entire frame is filled edge to edge with a dense swarm of small flat
vivid red coins, each a simple circle with a black outline and two tiny black line wings, angled in
many directions as if flying. Through a small gap in the center, a black stick figure is barely
visible, arms raised to shield the head. No floor visible.

Accent colors are only vivid red for money leaking away, used as flat solid color with no
gradients. In this frame vivid red is on the coins only. Everything else is black on white.

{NEGATIVE}
```

Attached: `reference_image_urls: [<clip 1 still = style plate>]`, plus "Match the line weight,
head size, and figure proportions of the first reference image exactly."

## Clip 1 prompt (start = still 1, end = still 2)

```
The first frame is the start image exactly: keep its composition, line weight, figure design, and
colors, then animate.

Flat 2D line animation on a flat, uniform, pure white canvas with no gray tint, texture, gradient,
shadow, or lighting at any moment. Stick figures in clean black lines of one uniform medium weight:
hollow circle head with no face, no hair, no clothing, single-line limbs, fixed proportions.
Accents only vivid red (money leaking away), as flat solid color.

Rapid scene changes and kinetic motion-graphics transformations while preserving an identical stick
figure design, constant line weight, and strict temporal consistency.

[0-3s] The figure stands center low. A single vivid red coin slips from its hand, bounces once and
rolls toward the lower right. Slow push toward the figure.
[3-7s] The coin splits into two, four, then dozens of small red coins that sprout tiny line wings
and circle the figure faster and faster. The figure turns, reaching for them. Camera tilts up with
the swarm.
[7-10s] The swarm surges upward and toward the lens until red coins fill the entire frame edge to
edge, the figure barely visible through a small central gap with arms raised.

Audio: synchronized sound effects only, a single coin drop and bounce, a rising multiplying jingle,
fluttering wings, a whoosh as the swarm fills the frame. No narration, no dialogue, no singing, no
music.

No words, letters, numbers, captions, subtitles, color codes, logos, or watermarks. No 3D, no
shading, no gradients, no shadows, no photorealism, no faces, no hair, no clothing, no extra limbs,
no changing proportions or line weight, no line flicker or boiling, no inverted theme colors, no
unexplained colors, no unintended characters.
```

## Clip 2 prompt (start = still 2, end = still 3)

```
The first frame is the start image exactly: keep its composition, line weight, figure design, and
colors, then animate.

Flat 2D line animation on a flat, uniform, pure white canvas with no gray tint, texture, gradient,
shadow, or lighting at any moment. Stick figures in clean black lines of one uniform medium weight:
hollow circle head with no face, no hair, no clothing, single-line limbs, fixed proportions.
Accents only vivid red (money leaking away), emerald green (the app and control), as flat solid
color.

Rapid scene changes and kinetic motion-graphics transformations while preserving an identical stick
figure design, constant line weight, and strict temporal consistency.

[0-3s] The red coin swarm streams apart and locks into a giant red conveyor belt rising diagonally
from lower left to upper right. The figure lands on it running uphill. Lateral track right.
[3-7s] Icon-only blank cards drop onto the belt one after another. The figure runs harder but
slides backward. Each card thud adds a short camera shake.
[7-10s] The belt tips toward the camera, the figure tumbles off, and a large emerald green phone
icon swings in from the right and catches the figure. End with the figure holding the emerald phone
large and centered.

Audio: synchronized sound effects only, a heavy conveyor rumble, card thuds, a slipping whoosh, a
soft cushioned catch. No narration, no dialogue, no singing, no music.

No words, letters, numbers, captions, subtitles, color codes, logos, or watermarks. No 3D, no
shading, no gradients, no shadows, no photorealism, no faces, no hair, no clothing, no extra limbs,
no changing proportions or line weight, no line flicker or boiling, no inverted theme colors, no
unexplained colors, no unintended characters.
```

Clip 3 has `start_image_url` = still 3 and no `end_image_url`.

## Composition call

```
advibly_render_composition
  aspect_ratio: "9:16"
  scenes: [ {source: clip1, volume: 0.25}, {source: clip2, volume: 0.25},
            {source: clip3, volume: 0.25} ]
  voiceovers: [ {source: vo1, start_seconds: 0}, {source: vo2, start_seconds: 10},
                {source: vo3, start_seconds: 20} ]
  music: <music id>
  keep_scene_audio: true
  frame_cadence: "on_twos"
  texts: [ {content: "Where did it go?", start_seconds: 1.5, duration_seconds: 2.5,
            position: "top", size: "lg", color: "black"},
           {content: "Keep your money.", start_seconds: 27, duration_seconds: 3,
            position: "top", size: "lg", color: "white", background_color: "#16A34A"} ]
  brand_id, project_id
```

The overlay pill's CSS color is a composition parameter, not a generation prompt, so a code is
fine there.
