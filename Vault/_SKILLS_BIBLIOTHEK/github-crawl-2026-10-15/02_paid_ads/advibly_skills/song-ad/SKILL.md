---
name: song-ad
description: >
  Create an animated song ad end to end on the Advibly MCP: a micro music
  video where an original song carries the product story and one animated
  lead sings on camera in chosen beats while silent B-roll visualizes the
  lyrics in between. Writes two or three distinct song options from the
  brand's real customer and angle (genre inferred from the audience, hook in
  the first five seconds, a real song rather than a jingle), generates the
  picked song with lyrics on minimax-music-3, measures its real line-by-line
  timing with advibly_analyze_video, locks a hero character sheet
  (gpt-image-2), storyboards every second of the song into batches, draws
  each batch as one multi-panel storyboard canvas, slices the song into
  gapless 5 to 15 second pieces with ffmpeg, then renders each batch as one
  minimax-h3-max reference-to-video generation with the canvas, the character
  sheet and the song slice attached (the slice as reference audio, which is
  what puts the lip sync on the beat), and lays the untouched song back under
  the clips with advibly_render_composition.
  Trigger when the user asks for a song ad, singing ad, musical ad, music
  video ad, jingle, "sing about my product", or a Starpop-style song ad.
---

# Song ad (Advibly)

A song ad plays like a micro music video. An original song carries the story, one animated lead sings on camera in a few beats, and the rest is silent B-roll cut to the music that shows what the lyric is saying at that moment. It wins when the song is one people would actually listen to, and when its hook lands the customer's problem in the first five seconds.

**The song is the spine.** It is written and generated first, before any picture exists. Its measured timing is the clock every later decision is cut to, and it is never edited: no section is regenerated on its own, no instrumental stretch is removed, and the finished ad plays the whole track exactly as it was generated. A voiceover can be trimmed and nudged; a song cannot, so the pictures bend to it.

**The song is also an input.** The lead sings on the beat because each video generation hears its slice of the song (`reference_audio_urls` on `minimax-h3-max`). Describing timing in a prompt ("she sings the first line at 0.4s") does not work; the model mouths at whatever rhythm it likes. Attach the audio, every time a batch contains a sung shot.

Move fast: batch questions, state defaults, end every stage on its hand-off line. Speak in the user's language. No em dashes anywhere in output. No text in any generated image or video; captions and the end card live in the composition.

## Tool discovery and Advibly plumbing

Tools are deferred. Load the Advibly tool schemas with tool search before the first call each session ("advibly generate music", "advibly analyze video", "advibly generate image", "advibly generate video", "advibly create upload url", "advibly upload asset", "advibly render composition", "advibly get generation", "advibly create project") and confirm parameter names against what loads.

```text
advibly_generate_music      -> the song (minimax-music-3, lyrics + style prompt)
advibly_analyze_video       -> line-by-line timing of the finished song (it takes audio URLs)
advibly_generate_image      -> character sheet, product sheet, storyboard canvases (gpt-image-2)
advibly_create_upload_url   -> presigned PUT for each local song slice (audio/mpeg)
advibly_upload_asset        -> registers the slice, returns its public url
advibly_generate_video      -> one clip per batch (minimax-h3-max, reference-to-video)
advibly_render_composition  -> the clips over the full song, plus optional end-card text
```

**Required server capability.** The song-slice mechanic needs `reference_audio_urls` on `advibly_generate_video` and `audio/*` on `advibly_create_upload_url`. If the loaded schema lacks either, stop before Stage 3 and tell the user the connected Advibly server predates song ads; do not fall back to prompting the timing.

- **Brand and project.** Resolve the brand with `advibly_list_brands`. Create one project per run with `advibly_create_project` ("Acme song ad") and pass `brand_id` plus `project_id` on every generate call, the song and the final composition included. Continuing an earlier run: find its project with `advibly_list_projects`.
- **`on_brand: false` on every image call.** The character sheet and the canvases own the art direction.
- **Pending generations.** Call `advibly_get_generation` (`wait: true`) whenever a finished URL is needed downstream: the song, the character sheet, every canvas.
- **Local tools.** Slicing needs `ffmpeg`/`ffprobe` and `curl` on the machine running the skill. Check once (`ffmpeg -version`) at Stage 2; if missing, ask the user to install it (`brew install ffmpeg`) rather than improvising.
- **Credits.** Before Stage 3, quote the video pass (see `references/generation-prompts.md`, roughly 0.15 credits per second of song at 768P plus retries) and wait for a yes. Short on credits: `advibly_buy_credits`, share the link, never switch provider.

## Step map: resume from what this turn gives you

| They gave you...                                   | Run                                   |
| -------------------------------------------------- | ------------------------------------- |
| A product or brand, no song yet                    | **Stage 1: Song**                     |
| A picked song option                               | **Stage 1, step 4: Generate the song**|
| A finished song (ours, or their own audio file)    | **Stage 2: Plan the video**           |
| An approved storyboard                             | **Stage 3: Canvases and slices**      |
| Approved canvases                                  | **Stage 3, step 3: Render batches**   |
| All batches rendered                               | **Stage 3, step 4: Assemble**         |

A user who brings their own finished track (a Suno export, a jingle they own) skips Stage 1: upload it with the audio upload flow and go to Stage 2. Ambiguous input: ask one short question.

## Stage 1: Write the song

Read `references/song-writing.md` before writing a word.

1. **Ground in the real customer.** Pull the brand brief (`advibly_get_brand`), the dossier when a claim needs sourcing (`advibly_get_brand_dossier`), and for store brands the catalog (`advibly_get_products`) to pick the product. Take the target customer, their main pain, the hero benefit and the brand voice. Never invent proof, ingredients or numbers.
2. **Settle four things in one line, inferred and stated, not asked**: the **persona** (one specific person with one doubt, e.g. "a woman in her 40s who has decided her broken sleep is her own fault"), the **angle** (the outcome the song is about, never a brand brag), the **genre** (from the genre map), and the **length** (15, 30 or 60 seconds; default 30). Let the user adjust.
3. **Write 2 or 3 genuinely different options** in the format from the reference: title, concept, lyrics with structure tags, a style line under 25 words, and a visual concept that already marks which lines the lead sings on camera. Vary POV, mood or structural hook between options, never just the wording.

   Hand-off: _"Pick one (or ask for more variations) and I'll generate two takes of it."_

4. **Generate two takes** of the picked option in parallel with `advibly_generate_music`: `model: "minimax-music-3"`, `lyrics` = the exact lyrics (every structure tag alone on its own line), `prompt` = the style line, `duration_seconds` = the target plus 15 (it is a hard cap that cuts the song off mid-word, not a target), `brand_id`, `project_id`. Music is cheap and non-deterministic; two takes cost almost nothing and give the user a real choice. Share both URLs (no inline player renders) and let the user pick by ear.

   Hand-off: _"Pick the take you like. That song is now locked; everything else gets timed to it."_

## Stage 2: Plan the video against the real song

Read `references/timing-and-slicing.md`.

1. **Measure the song.** Download the picked take, get its exact length with `ffprobe`, then run `advibly_analyze_video` on the audio URL with the JSON schema from the reference (`thinking: "high"`) to get every sung line's start and end, plus the instrumental stretches. The measured length wins over the requested one; a "30 second" song often comes back at 36 or 40.
2. **Lock the heroes.** One animated lead, designed for this persona (`references/generation-prompts.md`, character sheet): front, side, back and three expression close-ups on white, in one style (default: polished feature-film 3D animation, original character, never a franchise look). Generate it with `gpt-image-2`, `quality: "high"`, and get a nod. The product gets its real photo (catalog or uploaded asset), re-attached wherever it appears. A recurring set (a stage, a bedroom) is locked only if it repeats across batches.
3. **Decide where the lead sings.** A song ad is a mix: sung shots carry the story, everything else is silent B-roll. Default: the hook and the final chorus are sung, at most one sung shot per batch and usually the batch's first shot. A lead who sings continuously gets boring by the second verse.
4. **Storyboard every second of the song.** One row per shot: time range, lyric playing, SUNG or B-ROLL, the visual, the camera. Every second from 0.00 to the song's end is covered, instrumental stretches included (they are pictures, never dead air), and the outro becomes the product end card. Then group shots into **batches**: consecutive shots whose combined length is 5 to 15 seconds, cut only in a gap between sung lines, never mid-word. Aim for 8 to 12 second batches of 3 to 5 shots. Every instrumental stretch rides at the end of the batch whose lyric leads into it.
5. **Present the storyboard with the batch plan and the credit quote.**

   Hand-off: _"Approve the storyboard (or mark shots to change) and I'll draw the batch canvases and slice the song."_

## Stage 3: Execute

1. **Draw one storyboard canvas per batch** with `advibly_generate_image` (`gpt-image-2`, `quality: "high"`, `on_brand: false`), the character sheet and product photo attached as references. The canvas lays the batch's shots out as numbered-free panels read left to right, top to bottom (layout table in `references/generation-prompts.md`). Generate every canvas in parallel, show them, and get approval; fixing a panel here is cheap, fixing it in video is not.
2. **Slice the song**, gapless: slice N ends on the exact sample slice N+1 starts. Cut locally with ffmpeg, check the slice lengths sum to the song's length, then upload each slice (`advibly_create_upload_url` with `mime_type: "audio/mpeg"` and its exact byte size, `curl -X PUT`, then `advibly_upload_asset` with the `upload_key`). Keep a table: batch, in, out, length, slice URL.
3. **Render every batch in parallel** with `advibly_generate_video`:

   ```text
   model: "minimax-h3-max"
   reference_image_urls: [<canvas>, <character sheet>, <product photo if in batch>]
   reference_audio_urls: [<this batch's slice>]
   duration: ceil(slice length), 5 to 15
   aspect_ratio: "9:16", resolution: "768P"
   prompt: the batch template from references/generation-prompts.md
   ```

   Never pass `start_image_url`: the render is reference-to-video and the canvas is Image 1. The prompt names which single shot sings and states that every other shot is silent; left open, the model lip-syncs a shot of a field. Check every clip for three things before accepting it: the sung shot is on the beat, the lead is the same character as the sheet, and no B-roll shot has a moving mouth. Regenerate only failures, up to two retries each, tightening the named constraint.
4. **Assemble** with `advibly_render_composition`: the clips as ordered `scenes`, each trimmed to its slice length (`trim_end_seconds`), `keep_scene_audio: false`, `music` = the locked song's URL, `music_volume: 1`, `aspect_ratio: "9:16"`, `project_id`. The song plays from zero under hard cuts that land exactly where its slices were cut, so nothing drifts. Add the end-card headline and CTA as `texts` over the outro only if the user wants them. Lyric captions, if wanted, are a pass with `advibly_add_subtitles` on the finished ad.
5. **Finish**: `advibly_update_project` with `cover_generation_id` set to the composition, deliver the video and its `edit_url`, and offer publishing (`advibly_social_create_post`) only after they have seen it.

## Rules

1. **Song first, and never edited.** Generated whole, once, before any picture; storyboarded against its measured timing; played unedited under the finished ad. The only permitted cut is a long silent head before the first note, trimmed once on the master before any slicing (then the trimmed master is uploaded and used everywhere).
2. **Slices touch.** No gaps, no overlaps, no trimmed instrumentals. Half a second lost between two slices makes every later clip drift off the song.
3. **The audio is the timing.** Every batch attaches its slice. Timing is never described in a prompt.
4. **One persona, one doubt.** The lyric sings the customer's outcome; the product name is never the hook, and product education starts only after the song has named the problem.
5. **One locked lead.** The same character sheet URL is attached to every canvas and every batch; never chain off a previous clip or canvas.
6. **Sung shots are marked.** Exactly which shot sings is written in the storyboard and in the batch prompt; every other shot is silent picture.
7. **Producible visuals.** Stylized animated characters, objects with faces, simple sets. No live-action crane shots, no crowds of distinct faces.
8. **No text in footage.** No captions, labels, readable packaging copy invented by the model, or lyrics in any image or video prompt; type lives in the composition.

## Self-check before presenting

- Did the song exist, measured, before a single storyboard row was written?
- Does the hook land the persona's problem inside five seconds, with no brand name as the hook?
- Is every second of the song covered by a shot, instrumental stretches and the outro included?
- Is every batch 5 to 15 seconds, cut in a gap between sung lines, with at most one sung shot?
- Do the slice lengths sum exactly to the song's length?
- Does every batch attach its canvas, the character sheet, and its slice, with no `start_image_url`?
- Does the composition play the untouched song with `keep_scene_audio: false` and each clip trimmed to its slice?
- Does every generate call carry `brand_id` and the run's `project_id`, and is the finished ad the project cover?

Method adapted from Starpop's published song-ad workflow (David Ishag, starpop.ai), rebuilt for the Advibly MCP.
