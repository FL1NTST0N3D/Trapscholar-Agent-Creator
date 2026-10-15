# Voiceover, music, composition, and gotchas (Phase 5)

## Why the narration is external

A narrator baked into each clip gets a different voice every generation and ties pacing to the
video model. Clips stay SFX-only; the narration is rendered separately in one voice and placed per
clip. The clip prompts forbid voice and music for this reason.

## Voiceover: one segment per clip

```
advibly_generate_voiceover      # once PER CLIP, same voice every time
  brand_id, project_id
  text: "<this clip's approved narration line only>"
  voice: <eve | leo | rex | ara | sal>
```

- One combined read of the whole script ignores clip timing: short `[pause]` tags do not stretch to
  ten seconds, so the lines bunch at the start and later clips play silent. One segment per clip
  keeps every line on its visuals.
- Each segment must fit its ~10 second window with a short breath. If one runs long, shorten the
  line and regenerate it. Never time-stretch a voice.
- Delivery tags (`[pause]`, `<slow>...</slow>`) are fine sparingly. A `<slow>` wrap on a very short
  line has returned clipped renders; use plain text if it happens.
- Voice map: `eve` bright and energetic (explainers, motivational), `leo` deep announcer (hard sell),
  `rex` confident CTA, `ara` warm, `sal` smooth and calm (wellness).

## Music

```
advibly_generate_music
  brand_id, project_id
  prompt: "<mood and arc from the proposal>, instrumental"
  instrumental: true
```

One bed is usually enough. When the proposal has a hard emotional turn (tense to released), render
two beds and splice at the turn, or render one bed prompted with the change ("starts sparse and
tense, lifts into driving drums and bright synths around 35 seconds"). No lyrics; they fight the
narration.

## The composition call

```
advibly_render_composition
  brand_id, project_id
  aspect_ratio: <the FINAL ratio: "9:16", "16:9", or "1:1">
  scenes: [ { source: <clip 1 id>, volume: 0.25 }, ... ]     # in order, max 12
  voiceovers: [ { source: <vo 1 id>, start_seconds: 0 },
                { source: <vo 2 id>, start_seconds: 10 }, ... ]
  music: <music id>
  keep_scene_audio: true
  frame_cadence: <"on_twos" | "smooth", per the approved proposal>
  texts: [ { content: "WHAT IF?", start_seconds: 12, duration_seconds: 2.5,
             position: "top", size: "lg" }, ... ]
```

- `start_seconds` for clip N's narration is the sum of the durations of the clips before it. If a
  clip is trimmed (`trim_start_seconds` / `trim_end_seconds`), recompute the offsets.
- Leave `music_volume` unset; the renderer ducks the bed under narration.
- **Overlays** come from the approved list only. Match the theme: black text on a light canvas,
  white on dark, or white on a solid accent pill (`background_color`) for a CTA. Keep them short
  and inside the platform-safe area.
- **Cadence**: `on_twos` holds about 12 distinct frames per second with continuous audio, the
  snappy limited-animation feel. `smooth` keeps long camera travel fluid. Use what the proposal
  approved.
- **`1:1`**: pass `aspect_ratio: "1:1"`; the 9:16 clips scale to fill and crop top and bottom,
  which is why the stills kept the action in the center square.
- The call returns `status: pending`, `generation_id`, `edit_url`. Then
  `advibly_update_project` with `cover_generation_id` set to that generation id.

Deliver the finished video with the `edit_url`: overlays, trims, cadence, and levels can all be
adjusted in the Advibly editor.

## Captions (optional)

Only if the user wants word-by-word captions on top of the overlays: `advibly_add_subtitles` on the
finished render, brand and product names in `vocabulary`. Captions and overlays should not occupy
the same area.

## Gotchas

| Symptom | Cause | Fix |
|---|---|---|
| Clip opens on a different composition | Omni 1.1 treats the start frame as a suggestion | Strengthen HOLD, name what must stay (figure position, the big object, the canvas). |
| Light canvas drifts gray or gets a vignette | the model "lights" the scene | Lead LOCK with the canvas sentence; add "flat vector at every moment". |
| Figures grow faces, hair, or volume | drift toward a cartoon character | Repeat the figure lock; re-roll; check the still did not already have it. |
| Random letters or numbers appear | a prompt mentioned text, a code, or a labeled object | Remove the mention; make the object icon-only; keep the negative block. |
| Hex codes or color names show on screen | a color code was in the prompt | Plain color names only. |
| Middle of a clip idles | beat 2 too thin | Give beat 2 a real transformation plus a camera move. |
| Seam stutters | end-frame landing arrives early or late | Trim a few frames at the seam in the editor. |
| Voice differs between clips | narration baked into clips | Keep clips SFX-only; one voice per voiceover segment. |
| Later clips silent | one combined voiceover | One voiceover segment per clip at its offset. |
| Accent bleeds onto the wrong object | palette sentence too loose | Name exactly which object carries which accent in this frame. |
| `content_rejected` | policy wording | No real people or third-party marks; reword. |
| `insufficient_credits` | balance | `advibly_buy_credits`, share the checkout link. |
