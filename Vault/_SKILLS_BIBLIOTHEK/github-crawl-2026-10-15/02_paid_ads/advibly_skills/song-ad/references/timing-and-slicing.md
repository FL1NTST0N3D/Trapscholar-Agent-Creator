# Timing and slicing

The song's measured timing is the only clock. This file covers measuring it, turning it into batches, and cutting the gapless slices each batch hears.

## 1. Get the master locally

```bash
mkdir -p song-ad && cd song-ad
curl -sL "<song url from advibly_get_generation>" -o master.src   # minimax-music-3 returns WAV today
ffmpeg -v error -i master.src -ar 44100 -ac 2 master.wav       # slice from WAV, never from MP3 frames
ffprobe -v error -show_entries format=duration -of csv=p=0 master.wav   # the song's true length
```

The `ffprobe` number is the length of the ad. Write it down with two decimals.

If the song opens on more than about 2 seconds of silence or noodling before the first note, trim that head once, here, and never again:

```bash
ffmpeg -v error -i master.wav -ss <head> master_trim.wav && mv master_trim.wav master.wav
ffmpeg -v error -i master.wav -c:a libmp3lame -b:a 192k master_final.mp3
```

Then upload `master_final.mp3` (audio upload flow below) and use that URL as the composition's `music`. Without a trim, the generated song's own URL is the music.

## 2. Measure every line

`advibly_analyze_video` accepts an audio URL. Ask for a structured timeline:

```text
advibly_analyze_video
  video_url: <song url, or the uploaded trimmed master>
  format: "json"
  thinking: "high"
  quality: "best"
  question: "This is a song. List every sung line in order with its start and end
             in seconds, the exact words, and whether it is verse, chorus, bridge
             or outro. List every instrumental stretch longer than 0.5s with its
             start and end. Give the total duration."
  json_schema: {
    "type": "object",
    "properties": {
      "duration_seconds": { "type": "number" },
      "lines": { "type": "array", "items": { "type": "object", "properties": {
        "start": { "type": "number" }, "end": { "type": "number" },
        "text": { "type": "string" }, "section": { "type": "string" } },
        "required": ["start", "end", "text"] } },
      "instrumentals": { "type": "array", "items": { "type": "object", "properties": {
        "start": { "type": "number" }, "end": { "type": "number" } },
        "required": ["start", "end"] } }
    },
    "required": ["duration_seconds", "lines"]
  }
```

The timestamps are the model's estimate, good to a few tenths of a second inside the song but loose on the total (tested: 25.84s reported for a 25.02s file). Sanity-check them: lines in order, no overlaps, the last end at or before the `ffprobe` length. If the analysis disagrees with `ffprobe` on total length, `ffprobe` wins and the analysis is re-run with a follow-up (`follow_up_of`) asking it to re-check the late lines. Present the result to the user as a table: in, out, lyric, section, plus the instrumental tail.

## 3. From lines to batches

A **batch** is one video generation: 5 to 15 seconds (the H3 range), one slice of the song, 3 to 5 shots, at most one sung shot. Build batches greedily from the top of the song:

1. Start at 0.00.
2. Extend the batch line by line while it stays at or under 12 seconds.
3. Close it in the **gap between two sung lines**. The cut point is the middle of that gap; when the gap is under 0.3s, cut 0.1s before the next line starts so no word is clipped.
4. An instrumental stretch always joins the batch **before** it (the lyric that leads into it).
5. The last batch runs to the song's exact end, outro included. If that leaves a final piece under 5 seconds, merge it into the previous batch; if the merge would pass 15 seconds, split the previous batch earlier instead.

Worked example, a 36.40s song:

| Batch | In    | Out   | Length | Carries                              | Sung shot      |
| ----- | ----- | ----- | ------ | ------------------------------------ | -------------- |
| 1     | 0.00  | 10.35 | 10.35  | hook + verse 1, 5 shots              | shot 1 (hook)  |
| 2     | 10.35 | 21.80 | 11.45  | verse 2, the turn, 4 shots           | shot 2 (turn)  |
| 3     | 21.80 | 36.40 | 14.60  | final chorus + 4.2s outro, 4 shots   | shot 1 (chorus)|

Check: 10.35 + 11.45 + 14.60 = 36.40. The slice lengths must sum to the song's length exactly.

## 4. Cut the slices

Cut from the WAV with sample-accurate seeking (`-ss`/`-to` after `-i`), then encode each slice:

```bash
ffmpeg -v error -i master.wav -ss 0.00  -to 10.35 -c:a libmp3lame -b:a 192k slice_1.mp3
ffmpeg -v error -i master.wav -ss 10.35 -to 21.80 -c:a libmp3lame -b:a 192k slice_2.mp3
ffmpeg -v error -i master.wav -ss 21.80           -c:a libmp3lame -b:a 192k slice_3.mp3   # last slice runs to the end
for f in slice_*.mp3; do printf "%s " $f; ffprobe -v error -show_entries format=duration -of csv=p=0 $f; done
```

Each slice's `out` is the next slice's `in`, character for character. MP3 adds a few milliseconds of encoder padding; that is fine for a reference and never accumulates, because the composition plays the master, not the slices.

Reference audio limits on H3: each clip 2 to 15 seconds. A batch longer than 15 seconds is a planning error; go back to step 3.

## 5. Upload each slice

```bash
stat -f%z slice_1.mp3      # macOS; Linux: stat -c%s
```

```text
advibly_create_upload_url  mime_type: "audio/mpeg", size_bytes: <exact>, filename: "slice_1.mp3"
curl -X PUT --upload-file slice_1.mp3 -H 'content-type: audio/mpeg' '<upload_url>'
advibly_upload_asset       brand_id, upload_key: <from step 1>, name: "Song slice 1"
```

The returned `url` goes into `reference_audio_urls`. Upload all slices in parallel and record the table: batch, in, out, length, slice URL, generation duration (`ceil(length)`, minimum 5).

## 6. Why the composition cannot drift

Each clip is generated at `ceil(slice length)` seconds and trimmed back to the slice length with `trim_end_seconds`. Clip N therefore starts exactly where slice N starts on the master, and the sung shot inside it was timed to that same audio. Played back to back over the untouched master, every cut lands where the song was cut. The one way to break this is a slice table that does not sum to the song, which is why step 3 checks it.
