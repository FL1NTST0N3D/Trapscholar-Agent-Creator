# Advibly Skills

Claude skills that drive the [Advibly](https://advibly.com) MCP to generate ad creative end to end: on-brand images, UGC-style video ads, talking-actor videos, and carousels.

Each folder in this repo is one self-contained skill:

```
skills/
└── <skill-name>/
    ├── SKILL.md          # the skill itself
    └── references/       # supporting docs the skill loads as needed
```

## Skills

| Skill | What it does |
|-------|--------------|
| [`ugc-ads`](./ugc-ads/) | Generates a complete multi-shot UGC video ad from a brand plus an ad angle: a realistic AI creator image (gpt-image-2), a 5-shot direct response script, a user-approved storyboard of start frames, one vertical clip per shot animated from its frame with native spoken dialogue (Gemini Omni Flash), then assembles the clips into a finished ad. Five preset angles: testimonial, car/on-the-go, unboxing, lifestyle demo, problem-solution. |
| [`vox-explainer`](./vox-explainer/) | Turns a brand plus one angle into a finished Vox-style paper-collage explainer ad, directed like a real short: picks a narrative arc and writes an approved beat map (hook in 3s, two shots per beat, a cut every 4 to 6 seconds, varied camera moves, rich per-shot element motion), lets the user pick a visual theme and image model by eye from bake-offs (american-retro, swiss-modern, punk-zine, paper-craft-cream, and more), renders one richly layered collage poster per shot with headlines baked in (nano-banana-2 by default for the paper texture, gpt-image-2 for type-heavy posters) and the real product photo composited photoreal, animates each poster into living-collage motion with SFX-only audio (Gemini Omni Flash; Seedance for end-frame reveals and true assemble-from-empty builds, Kling for real people), reaches the dramatic looks (pieces flying in and assembling, confetti, impact shake, whip) through motion prompts alone with no local scripts, stitches the shots into one spot, then narrates it with advibly_generate_voiceover and scores it with advibly_generate_music, mixing voice over sidechain-ducked music and paper foley with ffmpeg. |
| [`claymation-ad`](./claymation-ad/) | Turns a brand plus one product into a finished Aardman-style stop-motion claymation ad: a locked cast-and-continuity sheet plus an approved 8-beat narrated story (setup, inciting moment, social validation, quiet despair, clay infographic, discovery, transformation, resolution), one hand-sculpted plasticine storyboard still per beat (gpt-image-2, generated sequentially so the character holds), each still animated into smooth clay motion with Gemini Omni Flash by default and Seedance 2.0 as an approved secondary fallback (SFX-only), stitched into one spot, then narrated with advibly_generate_voiceover and scored with advibly_generate_music, mixed with ffmpeg (warm storyteller over ducked music and clay foley). An explicitly requested video model always wins. The product is re-sculpted as a matte clay prop, never composited photoreal. Full 8-beat (~80s) or a 5-beat short (~50s). |
| [`pixar-style-ad`](./pixar-style-ad/) | Turns a brand and product into a vertical, original feature-film 3D animated ad: an approved cast and 4-beat micro-story (anthropomorphized problem hook, product reveal, friendly mechanism mascot scene, product CTA), gpt-image-2 storyboard stills generated sequentially for continuity, then Gemini Omni Flash image-to-video clips by default, with Seedance 2.0 as a secondary fallback. An explicitly requested model always wins. User shorthand such as "Pixar-style" is translated into an original warm, expressive 3D-animation direction. |
| [`stickman-animation`](./stickman-animation/) | Directs a stick-figure animation ad or explainer (adapted from the director method of kaomei's MIT Stickman Video Director). Asks for the theme (flat white canvas with black figures, or flat black canvas with white figures) and the aspect ratio, then writes a director's proposal for approval: narration timed at 20 to 25 words per clip, one row per ~10 second clip with three timed visual beats, at least four relevant visual devices, camera moves, SFX, and a named transition interface to the next clip. Renders one flat line-art opening still per clip (gpt-image-2, faceless figures, up to three accents in plain color names, no text in any generation), animates every clip in parallel with gemini-omni-flash-1.1 from its own still landing on the next clip's still so seams execute in-camera, then composes per-clip voiceover, music, text overlays, and an optional on-twos snap with `advibly_render_composition`. 9:16, 16:9, or 1:1 (center-safe 9:16 cropped). |
| [`collage-motion`](./collage-motion/) | Decode-then-animate pipeline for halftone paper-collage and stop-motion-graphic ads. Reverse-engineers a reference image into a field-editable JSON spec, generates on-brand stills with gpt-image-2 (store products locked via catalog photo references), then animates them into a default 4-scene set of 8s assemble-from-empty clips with Gemini Omni Flash (empty color field, cut-out pieces slide in and snap into place, native audio). The final composition enables the editor's On Twos effect by default. Labels are burned in at generation, faithful to the decoded color field by default. |
| [`explainer-videos`](./explainer-videos/) | Turns a brand topic or product angle into a narrated animated explainer in one of ten visual styles. Builds an approved beat map, generates styled keyframes, animates each as a recommended 4 to 6-second shot, then composes voiceover, music, and scene audio into the finished video. Gemini Omni Flash is the default motion model, with Seedance used when an exact end-frame landing is required. |
| [`static-ads`](./static-ads/) | Generates a batch of grounded static (image) ad concepts and renders them with gpt-image-2. Fifteen proven layout templates (headline statement, us vs. them, stat callout, review card, testimonial stack, before and after, problem and solution, founder message, feature or ingredient spotlight, press mention, lifestyle hero, numbered list, FAQ card, competitor callout, origin story) are cycled across the whole batch so template diversity becomes angle diversity. Every concept pulls its copy from the brand's research brief, dossier, product catalog or the user's own reviews and cites the source; nothing is invented. Plans the batch as approvable concept cards first (template, headline, body, visual, grounding), then renders one on-brand image per concept with the copy burned in and the real product attached as a reference for store brands, and delivers an index. Defaults: 15 concepts, 4:5, gpt-image-2 at high quality. |
| [`video-restyle`](./video-restyle/) | Applies a complete visual style to an EXISTING video (talking head, UGC clip) while keeping the subject's identity, expressions, lip-sync, and original audio. Analyzes the source with advibly_analyze_video (Gemini transcript + cut plan), cuts it locally into 3-10s segments at sentence boundaries, restyles each segment with Gemini Omni Flash video-to-video against one of six templates (podcast-pop sticker-cutout with rotating bold backgrounds, watercolor-wash, anime-manga, newspaper-print, notebook-doodle, neon-vaporwave), stitches the segments back together, then remuxes the original audio track over the result with ffmpeg. Captions are baked per segment; the per-segment look rotation makes the output read as a deliberately edited multi-look cut. |
| [`song-ad`](./song-ad/) | Turns a brand plus one customer persona into an animated song ad: a micro music video where an original song carries the story and one animated lead sings on camera in chosen beats while silent B-roll visualizes the lyrics. Writes two or three song options (genre inferred from the audience, hook in the first five seconds, a real song rather than a jingle), generates two takes of the pick with exact lyrics on minimax-music-3, measures the chosen take line by line with `advibly_analyze_video`, locks a hero character sheet (gpt-image-2), storyboards every second of the song into 5 to 15 second batches, draws each batch as one multi-panel storyboard canvas, cuts the song into gapless slices with ffmpeg and uploads them, renders each batch as one minimax-h3-max reference-to-video generation with the canvas, the character sheet and the song slice attached as reference audio (which is what puts the lip sync on the beat), then lays the untouched song back under the trimmed clips with `advibly_render_composition`. |

## Install

First, connect the Advibly MCP to Claude: [advibly.com/mcp-setup](https://advibly.com/mcp-setup).

Then install a skill. `npx skills` works for any supported agent (Claude Code, Claude Desktop, Cursor, and more) and pulls straight from this GitHub repo:

**ugc-ads**
```bash
npx skills add advibly/skills -s ugc-ads
```

**vox-explainer**
```bash
npx skills add advibly/skills -s vox-explainer
```

**claymation-ad**
```bash
npx skills add advibly/skills -s claymation-ad
```

**pixar-style-ad**
```bash
npx skills add advibly/skills -s pixar-style-ad
```

**stickman-animation**
```bash
npx skills add advibly/skills -s stickman-animation
```

**collage-motion**
```bash
npx skills add advibly/skills -s collage-motion
```

**video-restyle**
```bash
npx skills add advibly/skills -s video-restyle
```

**explainer-videos**
```bash
npx skills add advibly/skills -s explainer-videos
```

**static-ads**
```bash
npx skills add advibly/skills -s static-ads
```

**song-ad**
```bash
npx skills add advibly/skills -s song-ad
```

Install all skills at once:
```bash
npx skills add advibly/skills
```

### Manual install

Prefer to install by hand?

- **Claude Desktop / Cowork**: Settings → Skills → Install, and select the skill's folder.
- **Claude Code**: clone the repo and copy the skill folder into `~/.claude/skills/`:
  ```bash
  git clone https://github.com/advibly/skills.git
  cp -R skills/ugc-ads ~/.claude/skills/
  cp -R skills/vox-explainer ~/.claude/skills/
  cp -R skills/claymation-ad ~/.claude/skills/
  cp -R skills/pixar-style-ad ~/.claude/skills/
  cp -R skills/stickman-animation ~/.claude/skills/
  cp -R skills/collage-motion ~/.claude/skills/
  cp -R skills/explainer-videos ~/.claude/skills/
  cp -R skills/video-restyle ~/.claude/skills/
  cp -R skills/static-ads ~/.claude/skills/
  ```

Then ask Claude for what you want, e.g. `Make a UGC ad for my brand. Angle: testimonial.` or `Reverse-engineer this collage reference and animate it.`

## Requirements

- An Advibly account with an onboarded brand ([advibly.com/onboarding](https://advibly.com/onboarding))
- The Advibly MCP connected to Claude
- Advibly credits (generation tools spend the account's credits)
