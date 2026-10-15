# AI Marketing Videos

Agent skills and a small toolkit for making short-form video ads (Reels, TikTok, Shorts, Stories) with an AI coding agent. It works for any app or product. Everything here comes from shipping real ad sets and fixing everything the client called "AI slop".

Free tools only: Blender, MakeHuman, Remotion, ffmpeg, local TTS and Whisper. No API keys, no paid generators.

## What's inside

```
skills/
  ad-video-director/     Start here. Order of work and creative principles, from script to delivered mp4.
  ad-copywriting/        Storylines, hooks, script shape, CTAs, captions, safe zones, ad policy.
  blender-ad-pipeline/   100% 3D ads rendered headless in Blender, with real human figures.
  remotion-ad-pipeline/  Code-driven 2D motion ads, product stills, voice-over and the mix.
  render-precheck/       The review loop: check every shot in the tool before rendering.
kit/
  blender/   k6.py (scene, materials, lights, camera, animation), human.py (MakeHuman people:
             poses, faces, idle life, talk, real grips on phones and cards), props.py (phone,
             coins, chips, constant-speed flows, charts…), edit.py (captions + final edit in the
             Blender VSE), render_shot.sh, locked.sh (parallel render slots), precheck/ (overlay sheets)
  audio/     vo.py (voice-clone TTS + whisper word timings), mix.sh (ducked, -14 LUFS mix)
```

## Use the skills

The skills follow the [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) format: a folder with a `SKILL.md`.

**Claude Code:**

```bash
git clone https://github.com/retrogtx/ai-marketing-videos
# for one project:
mkdir -p your-app/.claude/skills && cp -r ai-marketing-videos/skills/* your-app/.claude/skills/
# or for every project:
cp -r ai-marketing-videos/skills/* ~/.claude/skills/
```

Then ask for what you want: *"Make a 30-second Reels ad for this app"*. The agent loads `ad-video-director` and follows the workflow. Other agents that read `SKILL.md` folders work the same way; for anything else, paste the skill text into your system prompt.

## The workflow in one screen

1. **Learn the product from its source.** Real data, real copy, no screenshots.
2. **Script first.** Draft 4–6 storylines, the user picks, then write line-by-line scripts with sources.
3. **One hero ad,** approved, before batching the rest.
4. **Write a build brief** for every beat.
5. **Parallel builder agents,** one per ad, sharing the kit and a render-slot lock.
6. **Precheck before render.** Preview stills with safe-zone overlays and 100% close-ups of hands, faces and clothes.
7. **Assemble, review the final at 100%,** then deliver.

## Kit requirements

- **Blender pipeline:**
  - Blender 4.2+ (tested on 5.2) and ffmpeg.
  - For people: the [MPFB](https://extensions.blender.org/add-ons/mpfb/) extension plus the free MakeHuman CC0 asset packs. See `skills/blender-ad-pipeline/SKILL.md` for setup.
  - Figtree fonts in `kit/blender/fonts/`.
- **Audio:** macOS on Apple Silicon for `mlx-audio` and `mlx-whisper` (`pip install mlx-audio mlx-whisper librosa soundfile`), plus ffmpeg. Only clone voices you have the rights to.
- **Remotion:** Node 18+ and a Remotion project.

Set `AMV_PROJECT` to your ad project folder:

```
my-ads/
  scripts.json            {"myad": [{"id": "hook", "text": "...", "pause": 0.25}, ...]}
  shots/myad/hook.py      one Blender script per shot
  shots/myad/edit_myad.py calls kit/blender/edit.py build(...)
  audio/                  voice-ref.wav, myad-vo.json, myad-mix.wav
  sfx/
  out/shots/myad/         rendered shots
```

## Hard-won rules (short version)

- Say plainly what the product gives people, and show it on the real UI.
- Hook in 2 seconds: topic plus outcome.
- Premium over gamey: one focal idea per shot, calm easing, minimal SFX. But never static.
- Colour follows the story, and real people replace mascots.
- Make no claims you can't back up. Regulated categories get "research and education" framing and a disclaimer.
- Keep key visuals inside x 65–1015, y 250–1150 on a 1080x1920 frame, with nothing important under the captions.
- Coins and particles move at constant speed and sparsely. People hold things for real.
- Check in the tool before the render happens.

## License

MIT. MakeHuman assets are CC0. Figtree is SIL OFL.
