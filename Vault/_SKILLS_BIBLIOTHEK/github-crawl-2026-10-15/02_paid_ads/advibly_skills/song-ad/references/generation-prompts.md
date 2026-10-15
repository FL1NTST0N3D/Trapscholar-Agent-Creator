# Generation prompts

Every prompt here is written for a stylized animated register (default: polished feature-film 3D animation with an original character). If the user picks another style (claymation, 2D cel, paper-craft), swap the style sentence everywhere and keep the rest.

## Character sheet (Stage 2)

One image, generated once, attached to every canvas and every batch.

```text
advibly_generate_image
  model: gpt-image-2, quality: high, aspect_ratio: "16:9", on_brand: false
  prompt:
    Character reference sheet for an original animated character, polished
    feature-film 3D animation style, soft even studio lighting on a plain white
    background. The character: <age, build, face shape, hair with one distinctive
    detail, skin tone, eye colour, one accessory, outfit with exact colours>.
    Left to right: full body front view, full body side view, full body back
    view, then three head-and-shoulders close-ups: neutral with mouth closed,
    singing with mouth open mid-note, warm smile. Same character, same outfit,
    same proportions in every view. Evenly spaced, nothing overlapping. No text,
    no labels, no logos.
```

Give the character one or two memorable details (a silver streak in the hair, tortoiseshell glasses, a terracotta blouse) and repeat them word for word in every later prompt: they are what the model latches onto. Design for the persona, not for the product.

Objects with faces (a grumpy mattress, a tired old serum bottle) are cast the same way: a one-image sheet, front plus three expressions, attached wherever they appear.

## Product

Attach the real product photo (catalog hero from `advibly_get_products`, or an uploaded asset). Describe it only as "the product in the attached photo, rendered exactly as photographed, its label unchanged". Never ask the model to write or restyle the label.

## Storyboard canvas (Stage 3, one per batch)

A canvas holds every shot of one batch as panels, so one video generation can move through the whole sequence in order. Panels are vertical (9:16) because the ad is.

| Shots in the batch | Layout                              | `aspect_ratio` |
| ------------------ | ----------------------------------- | -------------- |
| 2                  | two vertical panels side by side    | `1:1`          |
| 3                  | three vertical panels in one row    | `16:9`         |
| 4                  | two rows of two vertical panels     | `9:16`         |
| 5 to 6             | two rows of three vertical panels   | `4:5`          |

(Nine-by-sixteen panels tile to roughly these ratios; the nearest supported one is used.)

```text
advibly_generate_image
  model: gpt-image-2, quality: high, aspect_ratio: <from the table>, on_brand: false
  reference_image_urls: [<character sheet>, <product photo if in batch>, <locked set if any>]
  prompt:
    A storyboard sheet of <N> vertical 9:16 panels, <layout>, separated by thin
    white gutters, read left to right, top to bottom. Polished feature-film 3D
    animation style, every panel fully rendered, consistent lighting. The woman
    is exactly the character in the first attached image: <her memorable details>.
    Panel 1: <shot 1: framing, action, setting, camera>.
    Panel 2: <shot 2 ...>.
    ...
    Every panel is a finished frame, not a sketch. No text, no numbers, no
    captions, no speech bubbles, no panel labels anywhere.
```

Write each panel as a finished frame: framing (close-up, medium, wide), the one action, the setting, the camera angle. Vary framing across B-roll panels. In a sung panel the lead faces the camera, face large and unobstructed. The outro's last panel is the product end card: the product on a clean pedestal or surface with generous empty space above it for a headline added later.

## Batch video prompt (Stage 3)

```text
advibly_generate_video
  model: minimax-h3-max
  reference_image_urls: [<canvas>, <character sheet>, <product photo if in batch>]
  reference_audio_urls: [<slice url>]
  duration: <ceil(slice length), 5-15>
  aspect_ratio: "9:16", resolution: "768P"
  brand_id, project_id
  prompt:
    Vertical polished 3D feature-animation sequence with <N> connected shots.
    Image 1 is the storyboard canvas: play its panels in order, left to right,
    top to bottom, one panel per shot. Image 2 is the exact recurring hero
    character: keep her <memorable details>, outfit and proportions identical in
    every shot. <Image 3 is the product: render it exactly as photographed.>
    Audio 1 is the song for this section and the only timing source.
    Shot <k> is the only on-camera singing shot: she faces the camera and
    lip-syncs Audio 1's lyrics clearly, on the beat. Every other shot is silent
    picture over the music: no mouth movement, no talking.
    Shot 1 (<in>-<out>s): <action and camera move>.
    Shot 2 (<in>-<out>s): <action and camera move>.
    ...
    Cut between shots on the musical beat. No added music, no extra dialogue,
    no sound effects over the vocal, no captions, no on-screen text.
```

The per-shot times come from the storyboard, relative to the start of the slice. When the batch has no sung shot (an instrumental outro, a montage), replace the singing sentence with "No shot contains singing or talking; every character's mouth stays closed" and still attach the slice, so the cuts ride the music.

`minimax-h3-max` reads the references positionally, so the order of `reference_image_urls` must match "Image 1, Image 2, Image 3" in the prompt. Keep the prompt detailed: a detailed prompt is passed through verbatim, a thin one gets rewritten by the provider.

## Checking a clip

Accept a clip only when all three hold:

1. **On the beat**: the sung shot's mouth shapes land on the words of the slice, starting where the line starts.
2. **Same lead**: face, hair detail, glasses, outfit match the sheet in every shot.
3. **Silent B-roll**: no mouth moves in a shot not marked SUNG.

Retry fixes (tighten the named failure, never add quality adjectives):

| Failure                                | Fix in the retry prompt                                                   |
| -------------------------------------- | ------------------------------------------------------------------------- |
| Lip sync drifts or mumbles             | Move the sung shot to shot 1, make it a close-up, name the first lyric    |
| B-roll character mouths the song       | Add "in shots <list> her mouth is closed" and make those shots wider      |
| Lead drifts off-model                  | Repeat the memorable details in each shot line, put the sheet first if the canvas drifts less |
| Panels skipped or reordered            | Fewer panels per batch (3), state the shot count twice                    |
| Model invents text or labels           | Repeat "no text" and describe the product as "exactly as photographed"    |

Up to two retries per batch; after that, redraw the batch's canvas.

## Credit quote

`minimax-h3-max` at 768P bills per second of output plus a small charge for the attached references. Quote roughly **2 credits per 10-second batch**, so about 6 to 8 credits for a 30 to 40 second song, plus the stills (character sheet and one canvas per batch, gpt-image-2 high) and one composition render (0.4). The song itself costs a few hundredths of a credit per take. Budget one retry per batch in the quote.

## Composition

```text
advibly_render_composition
  scenes: [
    { source: <batch 1 generation id>, trim_end_seconds: 10.35 },
    { source: <batch 2 generation id>, trim_end_seconds: 11.45 },
    { source: <batch 3 generation id>, trim_end_seconds: 14.60 }
  ]
  keep_scene_audio: false
  music: <locked song url>
  music_volume: 1
  aspect_ratio: "9:16"
  texts: [ { content: "<headline>", start_seconds: <outro start>, position: "top", size: "lg" } ]   # optional end card
  brand_id, project_id
```

The trims are the slice lengths from the slice table, never rounded. `keep_scene_audio: false` is mandatory: each clip carries its own model-generated audio, and only the master song may play.
