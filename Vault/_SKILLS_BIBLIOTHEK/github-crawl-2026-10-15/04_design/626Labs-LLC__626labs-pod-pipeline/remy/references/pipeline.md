# Pipeline Reference — Conundrum by Este

The whole machine, the scripts that run each stage, and the rules. This mirrors
`POD_DESIGN_PIPELINE.md` in the project root — if that file changes, update this one.

## Stages & the scripts that run them

```
CONCEPT -> GENERATE -> QA FILTER -> BG REMOVE -> TEXT COMPOSITE -> VARIANTS -> UPLOAD -> CREATE PRODUCT -> PUBLISH
```

| Stage | What happens | Script / how |
|---|---|---|
| 1. Concept | Trend/meme/public-domain idea, legal check | human + Remy |
| 2. Generate | Gemini image gen, **no text in prompt** | Gemini image model (session/API — generation prompt templates stay private); product panels via `generate.py` (`pod gen`) |
| 3. QA filter | AI-slop checklist (see below) | `qa.py` (`pod qa`) + manual review |
| 4. BG remove | Classical-CV matte + alpha unmix, 6 modes | `bgremove.py` (`pod cut`) — supersedes the old `remove_background_smart()` |
| 5. Text composite | PIL only, never the model | `generate.py` (`outline_text` / `auto_fit_text`); `city_nickname_art.py` for lockups |
| 6. Variant matrix | 5-10 variants per base art | `generate.py` + combos/ patterns |
| 7. Upload | Printify upload via **curl** (requests/urllib are Cloudflare-blocked) | inside `create_product.py` |
| 8. Create product | Build the listing draft | `create_product.py` (`pod build` — always a draft) |
| 9. Publish | Push drafts to Etsy, per-product confirm gate | `ship.py` (`pod ship publish`) — the primary publish route |

Background builders: `build_rich_backgrounds.py`, `gen_procedural_bgs.py`. The earlier
per-product one-off scripts are retired (kept locally, out of the shipped tree) — `generate.py`
and `create_product.py` are the only builders to reach for.

## Main builder: create_product.py

```
python3 create_product.py <image_path> <product_type> "<title>" [options]
```
Built-in types: `tee` (Gildan 64000, bp6/prov99), `hoodie` (Gildan 18500, bp77/prov99),
`mug` (bp635/prov28), `coaster` (bp1523/prov23). Full matrix in `product_matrix.md`.

Options: `--dark-only`, `--light-only`, `--all-colors`, `--colors "X,Y,Z"`, `--price CENTS`,
`--description "..."`, `--tags "x,y,z"`, `--dry-run`, `--no-publish`.

**Remy's default: always `--no-publish` (or `--dry-run`) until Estevan says ship it.**

## Stage 2 — generation rules
- Model: `gemini-3.1-flash-image-preview` (best); fallback `gemini-2.5-flash-image`.
  (`gemini_agent.py` uses `gemini-2.5-flash` for its *text/vision* calls — the split is
  intentional: image gen and analysis are different models. Not a bug; don't "fix" it.)
- Generate artwork WITHOUT text; add "no text" to every prompt.
- "square format" for most; "wide format" (3200x2000) for hats.
- Clear anatomy ("ONE mouth, TWO eyes") to dodge AI-slop limbs.

## Stage 3 — AI-slop QA checklist
- [ ] Extra/duplicate body parts (two mouths, three arms, extra fingers)
- [ ] Gibberish text/symbols that leaked in
- [ ] Artifacts on objects (random text on signs/laptops)
- [ ] Distorted / melted faces
- [ ] Background anomalies
- [ ] Inconsistent lighting/shadows
Action: regenerate with a tighter prompt if any fail.

## Stage 4 — background removal
Default ON for: tees, phone cases, totes, most accessories ("floating character" look).
Keep solid bg for: AOP (hoodies, joggers), pattern-combo overlays, posters, desk mats.

## Stage 5 — fonts (in `fonts/`)
- `Anton-Regular.ttf` — bold impact / meme text
- `BebasNeue-Regular.ttf` — clean condensed bold
- `Pacifico-Regular.ttf` — bold cursive
- `GreatVibes-Regular.ttf` — elegant cursive
- `DancingScript.ttf` — casual cursive

Text options: bold top/bottom (Anton), optional cursive scatter overlay, side-by-side panel
(hats), text variants for more SKUs, or clean/no-text.

### City Nicknames generator (NEW — `city_nickname_art.py`)
Clean, reusable, fill-the-box text-art generator. Replaces the old ad-hoc renderer that made
the broken `panther_city_v2` (tiny floating text + ghost drop-shadow collision).
- `python3 city_nickname_art.py panther_city` (preset) · `--all` · or a literal:
  `python3 city_nickname_art.py "FUNKY TOWN" --est 1849 --sub "FORT WORTH, TX" --fill "#F2A900"`
- Auto-fits type to ~86% width, controlled shadow (no ghost), transparent RGBA at print res.
- One-word nicknames -> squarer canvas; multi-word -> portrait tee canvas. Presets live in the
  `CITIES` dict (add a city = add one entry). Rule: this is the right tool for any typographic
  city/word lockup — don't hand-place text per-image again.

## Legal check (Stage 1 — non-negotiable)
- No celebrity likeness. No living-artist ripoffs. No active copyright/trademark.
- Public-domain safe list (as noted in project): Steamboat Willie (2024+), Classic Pooh book
  illustrations (2022+), Betty Boop 1930 (2026+), Pluto/Rover 1930 (2026+). Use the original
  expired versions, NOT later Disney redesigns.
- **Trademark ≠ copyright.** The dates above clear *copyright* only. Mickey (incl. Steamboat
  Willie) and Betty Boop are **active trademarks** — takedown-risky as merch regardless of the
  expired film copyrights. Treat recognizable branded characters as unsafe. (Both pulled 2026-06-02.)
- Slang/meme text: fine, but watch Etsy's profanity filters on some markets — keep a clean
  hero variant alongside any edgy one.

## Printify asset IDs
Account-scoped identifiers (shop ID, uploaded pattern/logo image IDs) live in
`pipeline_db/printify_asset_ids.md` — local operational data, not part of the public docs.

## Inventory + batch drafting (Phase 3 tools)
- **`inventory.py`** — `python3 inventory.py` scans all art folders, links files to known
  products, writes `pipeline_db/inventory.json`, and prints the backlog (live / draft / backlog
  counts + concept clusters). Run this FIRST when asked "what should we ship / what's not live".
- **`batch_draft.py`** — `python3 batch_draft.py <folder> --types tee,mug --plan` builds a draft
  plan for backlog art. `--plan` is safe (no API). `--execute` creates Printify DRAFTS only
  (`create_product.py --no-publish`), rate-limited. **Never publishes** — Remy still asks before
  anything goes live. Use these instead of generating new art when the backlog is large.

## Posting / publishing (Phase 5 tool — `ship.py`)
- `python3 ship.py review` — read-only; pulls all products, writes `ship_review.html` (mockup
  gallery, DRAFT vs LIVE) + `pipeline_db/ship_queue.json`. Run this to see what's sitting in draft.
- `python3 ship.py publish --interactive` — per-product y/n confirm gate, publishes only the
  approved ones. Also `--ids` and `--all-drafts` (types CONFIRM). This is the ONLY tool that
  pushes to Etsy — Remy still asks Estevan before running it.
- "Live" = has an Etsy `external` handle. Current live/draft counts live in
  `pipeline_db/ship_queue.json` (local) — run `ship.py review` to refresh.

## Credentials map (WHERE they live — never paste the values)
- All secrets resolve through `pod_secrets.py` → `PRINTIFY_TOKEN`, `SHOP_ID`,
  `GEMINI_API_KEY`, `printify_headers()`. Use this in any new script:
  `from pod_secrets import ...`.
- Resolution order: **OS credential manager** (`keyring`, service `pod-pipeline`) → `.env` →
  OS env vars. Store or rotate with `python pod_secrets.py set <NAME>` (hidden input);
  presence check with `python pod_secrets.py`.
- The plaintext fallbacks (`.env`, `printify_config.json`) were deleted 2026-07 — the
  credential manager is the only home for real values now.
