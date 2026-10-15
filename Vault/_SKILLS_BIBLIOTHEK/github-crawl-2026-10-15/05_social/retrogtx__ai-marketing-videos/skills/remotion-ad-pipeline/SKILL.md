---
name: remotion-ad-pipeline
description: Build code-driven 2D motion video ads and product stills with Remotion (React), plus the voice-over, captions and music mix used by every ad. Use when the ad doesn't need full 3D, for product/store stills and thumbnails, or for generating VO (voice clone TTS plus whisper word timings) and the loudness-normalized mix. Uses kit/audio/.
---

# Remotion ads, stills and audio

## Remotion motion ads

- **Project:** a standalone Remotion project for marketing. Compositions go in `src/<set>/`, assets in `public/<set>/`. Render at 1080x1920 and 30fps.
- **From scratch, in code:** read real data from the app's repo (content, pricing, feature lists) and rebuild its surfaces as animated components. Don't screenshot-pan and don't open a browser to capture the site.
- **Motion language:** borrow it from the product's own landing page, e.g. floating rotated cards, growing bars on `cubic-bezier(0.22,1,0.36,1)`. Don't reuse the site's calm editorial typography in ads.
- **Pacing:**
  - A visual change every 0.8–1.5s, and a bigger scene or palette shift every 3–4s.
  - Fades of at most 6–8 frames. Hard cuts are fine.
  - Hold each focal idea long enough to read.
- **Split screens:** before/after halves get equal bands, with captions kept out of both.
- **3D inside Remotion:** `@remotion/three` with `--gl=angle`.
- **Check your work** by rendering stills at key frames with safe-zone overlays before a full render (see `render-precheck`).

## Product stills (store pages, thumbnails)

- **Design stills separately.** Stills reusing the video's cards, or recoloured card walls, get rejected as "same design".
- **A direction that works:**
  - one glossy 3D hero object per image,
  - a bold two-line headline,
  - outcome-led copy,
  - a small "More … on the way" pill if the product is still growing.
- **Leave off:** a price, and content counts as the lead.

## Voice-over (`kit/audio/vo.py`)

- **Engine:** Qwen3-TTS (1.7B) via `mlx-audio` on Apple Silicon, cloning a voice from `audio/voice-ref.wav` and its transcript (`AMV_VOICE_REF_TEXT`). Only clone a voice you have rights to.
- **Takes:** each script line is generated with 3 seeds. The best take is chosen by whisper word accuracy, pacing and pitch variation.
- **Timing:** the whole track is played at tempo 1.05, then mlx-whisper large-v3-turbo produces word timings.
- **Output:** `audio/<ad>-vo.wav` and `audio/<ad>-vo.json` (`duration`, `lines`, `words`). This JSON drives captions and animation cues in both pipelines.
- **Voices to avoid:** stock TTS voices (e.g. Kokoro presets) get called "fake voice, AI slop". Aim for a natural, conversational read at about 170–190 wpm.

```
pip install mlx-audio mlx-whisper librosa soundfile
AMV_PROJECT=. AMV_VOICE_REF_TEXT="exact words in the reference clip" python kit/audio/vo.py myad
```

`scripts.json` looks like `{"myad": [{"id": "hook", "text": "…", "pause": 0.25}, …]}`.

## Mix (`kit/audio/mix.sh`)

`BED=music/bed.wav kit/audio/mix.sh myad` produces `audio/myad-mix.wav`. The VO is highpassed and compressed, the bed is sidechain-ducked under it, and loudnorm targets −14 LUFS with −1.5 dBTP true peak.

## Music and SFX

- **Music:** a low bed (minor-key lo-fi or soft trap) ducked about 12dB under the VO.
- **Synthesized music:** write samples at integer offsets. Round the start once, then add +j. Flooring `(start+t)*SR` per sample skips or duplicates samples and causes a shrill, screeching artefact.
- **SFX:** minimal and premium. Frantic stingers on every cut read as a game ad. Retime SFX when animations move.
