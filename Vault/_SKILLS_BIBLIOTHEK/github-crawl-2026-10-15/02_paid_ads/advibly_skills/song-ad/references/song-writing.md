# Song writing

The song is the ad. Everything here serves one test: would the persona let this play if it came on in a feed, and does the first line tell her it is about her?

## The persona comes first

Write the brief as one sentence about one person before any lyric. "She is in her 40s, her sleep is broken, and she has quietly decided it is her fault." A song written for everyone has nothing to sing about; a song written for one doubt can run 60 seconds and still hold the people it is for.

The classic shape is four beats, the same one a country song uses:

1. **The problem**, literal and specific (the alarm clock reads 3:00 AM).
2. **The turn**, the line that reframes it (it was never you, it was the mattress).
3. **The villain**, the old way made memorable (a grumpy, lumpy factory mattress with a face).
4. **The payoff**, the morning after.

Product education starts only after the turn. From there the lyric works like a landing page, one mechanism per line, over shots of the thing working. A viewer still watching has already agreed with the premise, so the claims land as relief rather than as a pitch.

## Genre map (infer from the audience, then state it)

| Audience                    | Genres that resonate                              |
| --------------------------- | ------------------------------------------------- |
| Moms (general)              | pop, indie pop, light acoustic                    |
| Moms (Gen X / 40+)          | country, soft pop, throwback pop                  |
| Gen Z women                 | pop, hyperpop, R&B, indie pop                     |
| Gen Z men                   | hip-hop, trap, EDM, indie rock                    |
| Millennial women            | pop, indie pop, R&B, alt-pop                      |
| Millennial men              | indie rock, hip-hop, alt-rock                     |
| Black audiences             | hip-hop, R&B, trap, neo-soul, pop                 |
| Latino / Latina market      | reggaeton, Latin pop, bachata, trap latino        |
| Fitness enthusiasts         | hip-hop, EDM, hard rock, trap                     |
| Skincare / beauty           | pop, R&B, indie pop, hyperpop                     |
| Luxury buyers               | ambient, modern jazz, cinematic pop               |
| Pet owners                  | folk, indie pop, country                          |
| Wellness / spiritual        | ambient, indie folk, soft acoustic                |
| Outdoor adventurers         | folk, indie folk, alt-rock, americana             |
| Gamers / tech               | EDM, synthwave, hyperpop, lo-fi, electro-pop      |
| Foodies                     | indie pop, jazz-pop, acoustic                     |
| Founders / B2B buyers       | indie rock, lo-fi hip-hop, synth-pop              |

No exact match: take the closest fit and say why in one clause.

## Lyric rules

- **Hook in the first five seconds.** The catchiest line comes first, whatever the length. No slow instrumental intro: the style line says "starts immediately on the vocal".
- **Sing the outcome, not the brand.** The product name may appear once, late. Never chant it.
- **A real song, not a jingle.** Real verses, a real chorus, a real rhyme scheme. Never "buy it now".
- **Short singable lines**: 4 to 8 syllables for a pop hook, a little longer for rap. Long lines get rushed when sung and the lip sync smears.
- **Vocabulary and energy match the genre.** Country tells a story in plain nouns; hip-hop rides internal rhyme; pop repeats the hook.
- **Structure by length**:
  - 15s: hook plus one chorus pass.
  - 30s: verse, chorus, short verse, chorus.
  - 60s: verse, chorus, verse, chorus, bridge, final chorus.
- **Every line must be picturable** as a stylized animated shot: an object with a face, a character doing one thing, a simple set. If a line cannot be shown, rewrite it.
- **Mark the sung lines** in the visual concept: the hook and the final chorus by default, one more at most.

## Style line (the music prompt)

Under 25 words, in this order:

```
[genre], [vocal: female lead / male rap / duet], [tempo in BPM], [mood], [production], starts immediately on the vocal
```

Example: `modern country ballad, warm female lead, 76 BPM, tender then hopeful, polished Nashville production, starts immediately on the vocal`

Never name an artist or band; describe the sound. Keep instruments to two or three.

## minimax-music-3 formatting

- `lyrics` holds only the words and structure tags. Every tag sits **alone on its own line**; text after a tag on the same line is dropped.
- Tags: `[verse]`, `[chorus]`, `[bridge]`, `[outro]`. Use `[outro]` with no words under it to ask for the short instrumental tail the end card sits on.
- Max 3500 characters. Plain text, no stage directions, no parentheses the singer might read aloud.
- `duration_seconds` is a **hard cap**: the track is cut off at that length, mid-word if the lyric runs over (tested: a 25s cap cut the final chorus line in half). Ask for the target plus 15 and let the lyric decide the real length; you pay only for seconds you asked for, which is still a few hundredths of a credit.
- The model sometimes sings an ad-libbed intro (the hook line plus "ooh"s) before the first `[verse]`. That is fine and often a better hook; the measured timeline in Stage 2 is what counts, not the lyric sheet.
- Before offering a take, check its last sung line is complete (the analysis in `timing-and-slicing.md` shows it). A take that ends mid-word goes back for a regenerate with a longer cap.
- `model: "minimax-music-3"` is the only model that takes exact lyrics. `elevenlabs-music-2.5` writes its own words, so never use it here.

```text
advibly_generate_music
  model: minimax-music-3
  prompt: <style line>
  lyrics: "[verse]\nThree a.m., the ceiling fan\n...\n[chorus]\n...\n[outro]"
  duration_seconds: 45
  brand_id, project_id
```

## Option format (Stage 1 output)

```
### Option [N]: "[Title]"
**Concept:** 1 to 2 sentences, the song's vibe and the animated treatment.

**Lyrics:**
[verse]
...
[chorus]
...

**Style:** <style line, under 25 words>

**Visual concept:** 2 to 3 sentences tied to lyric moments. Marks which lines
the lead sings on camera and what the B-roll shows.
```

The options differ in POV (the customer, the product, a narrator), in mood (upbeat, tender, playful, defiant), or in the structural hook (a question, a confession, a villain intro). Never ship near-duplicates.

## Worked example (the bar, not a template)

**Mattress brand, country ballad, ~79s.** Persona: a woman in her 40s who blames herself for broken sleep. The problem is literal (3:00 AM on the clock, a partner asleep beside her). The turn is sung on a small stage, the character stepping out of her own story. The villain is a lumpy factory mattress with a grumpy face, the frame people describe when they talk about the ad. Product verses follow: airflow, support, the unboxing, the morning after. The lead sings the turn and the payoff; everything else is silent B-roll. Reported result for this one creative: 4.95 ROAS over two months on about $2.2k spend at a $554 AOV (one ad in one account, not a benchmark). What its makers would change: a first frame that states the persona instantly instead of a dark bedroom, and an end card on the instrumental outro.
