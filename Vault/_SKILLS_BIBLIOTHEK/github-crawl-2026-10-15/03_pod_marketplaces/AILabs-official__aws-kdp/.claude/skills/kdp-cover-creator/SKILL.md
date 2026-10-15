---
name: kdp-cover-creator
description: >
  Generate full KDP-compliant book cover (front + spine + back) as PDF.
  Sudoku books: programmatic bestseller template (color-consistent front+back).
  Coloring books: OpenAI gpt-image-1.5 (codex) artwork + programmatic back.
  Handles 8.5x11 (portrait) and 8.5x8.5 (square). Spine width auto-calculated
  from actual interior.pdf page count. Outputs cover.png + cover.pdf for KDP.
  USE WHEN user says: make cover, generate cover, create cover, kdp cover,
  tao bia, cover pdf, build cover, cover for coloring book, cover for sudoku.
---

# KDP Cover Creator

Generate a full KDP-compliant book cover (front + spine + back) as PNG + PDF.

---

## Execution Protocol

- Run ALL steps in sequence WITHOUT stopping between them.
- After each tool call, immediately proceed to the next step.
- Between steps: at most ONE short progress line, then continue.
- Stop ONLY when: (a) all steps complete, (b) blocking error, (c) step marked **(pause)**.

---

## Image renderer priority

**Default renderer: `openai`** (gpt-image-1.5, "codex" model)

| Renderer | When to use |
|---|---|
| `openai` | Default for ALL coloring book front artwork. Best quality. |
| `nanopic` | Fallback if OpenAI quota exceeded or API unavailable. |
| `ai33` | Legacy fallback only. |
| `bimai` | Square (1:1) cover art if specifically needed. |

Sudoku books skip AI renderer entirely — covers are generated programmatically.

---

## Input

Accept any of:
1. `theme_key` — reads `output/{theme_key}/bookinfo.md`
2. Manual: `title, author, page_count, page_size, book_type`

Always require: `theme_key`, `author_name`

---

## Process

### Step 1: Read book metadata

```bash
cd /path/to/aws-kdp
python3 -c "
import scripts.config as config
plan = config.load_bookinfo('{theme_key}')
import json; print(json.dumps({k: plan.get(k) for k in ['title','subtitle','author','page_size','book_type','style','puzzle_count','difficulty_distribution','front_color_scheme','cover_palette']}, indent=2))
"
```

Key fields:
- `book_type` / `style` — "sudoku" → programmatic template; "coloring" → AI artwork
- `page_size` — "8.5x11" (portrait 3:4) or "8.5x8.5" (square 1:1)
- `front_color_scheme` — if set, respect it (user override); otherwise auto-selected
- `puzzle_count` + `difficulty_distribution` — drives cover text for sudoku

### Step 2: Count actual pages (for spine width)

Spine width = pages × 0.002252". ALWAYS use the assembled interior.pdf, not estimates.

```bash
PAGE_COUNT=$(python3 -c "
from pypdf import PdfReader
print(len(PdfReader('output/{theme_key}/interior.pdf').pages))
")
echo "Page count: $PAGE_COUNT"
```

If interior.pdf doesn't exist yet, estimate: `(num_coloring_pages × 2) + 4` (title + copyright + thank-you + blank).

### Step 3: Generate cover

```bash
cd /path/to/aws-kdp

# Sudoku book (programmatic template, no AI needed):
python3 scripts/generate_cover.py --theme {theme_key} --author "{author}"

# Coloring book (OpenAI / codex artwork):
python3 scripts/generate_cover.py --theme {theme_key} --author "{author}" --renderer openai

# Force regenerate front artwork (e.g. if previous artwork was wrong):
python3 scripts/generate_cover.py --theme {theme_key} --author "{author}" --renderer openai --regenerate

# Use exact KDP dimensions (from the KDP upload dialog):
python3 scripts/generate_cover.py --theme {theme_key} --author "{author}" --kdp-width 17.452 --kdp-height 11.25
```

**IMPORTANT — Color consistency rule:**
- For sudoku books, the front cover runs FIRST (sets `plan["front_color_scheme"]`), then back uses the same palette. This is already enforced in `build_cover()`.
- For coloring books, the front artwork is AI-generated (renderer creates the image). The back is drawn with a solid color matching the `cover_palette` in bookinfo.md.
- If front and back are different colors → run with `--regenerate` and check `bookinfo.md` has `cover_palette` set correctly.

### Step 4: Validate output

```bash
python3 scripts/pdf_qc.py --pdf output/{theme_key}/cover.pdf --trim {page_size}
```

KDP pre-flight checklist:
- [ ] `cover.pdf` exists and > 500 KB
- [ ] `cover.png` preview looks correct
- [ ] Front and back use SAME color scheme / palette (no mismatch)
- [ ] Title text readable, author name visible on front
- [ ] Spine: width matches page count (`pages × 0.002252"`)
- [ ] Spine text only if ≥ 79 pages (KDP rule)
- [ ] Barcode area (bottom-right of back) is BLANK white — no template text
- [ ] Bleed: 0.125" on all 4 sides
- [ ] DPI: ≥ 300
- [ ] Metadata: title on cover EXACTLY matches title on interior title page (top rejection cause)

### Step 5: Common fixes

| Problem | Fix |
|---|---|
| Front green, back black (color mismatch) | Bug fixed — upgrade scripts. Set `front_color_scheme` in bookinfo.md explicitly, then rerun. |
| DPI < 300 | Rerun with `--regenerate` |
| Spine too narrow/wide | Recount pages from interior.pdf, use `--kdp-width` override |
| Front artwork wrong concept | Update `cover_prompt` in bookinfo.md, rerun with `--regenerate` |
| Back has template text in barcode area | KDP rejection — edit `generate_cover.py` to remove any text in that region |
| "Height ~11.25" for square book" | Rerun with `--size 8.5x8.5` |

---

## KDP Dimension Reference

```
Spine width  = total_pages × 0.002252"  (white paper)
Full width   = (2 × trim_width) + spine + 0.25" bleed
Full height  = trim_height + 0.25" bleed
```

| Book Size | Trim W × H | Cover H | Spine (100p) |
|-----------|-----------|---------|-------------|
| 8.5×11 portrait | 8.5" × 11" | 11.25" | 0.2252" |
| 8.5×8.5 square | 8.5" × 8.5" | 8.75" | 0.2252" |

Use `--kdp-width` / `--kdp-height` to paste exact values from the KDP upload dialog (overrides calculated width).

---

## Conversion-Optimized Cover Design Principles

These are baked into the programmatic templates. When writing `cover_prompt` for coloring books, follow the same principles:

**Front cover must have:**
- Strong typographic hierarchy: MAIN WORD huge, subtitle smaller, author small
- Year badge (e.g. "2026") in a colored pill — signals freshness
- Difficulty/level badge (e.g. "3 LEVELS ★ ★ ★") — scannable at thumbnail size
- Puzzle/page count pill (e.g. "100 PUZZLES") — concrete value prop
- 2–3 sample grids/pages — proof of content, builds trust
- Audience tagline band at bottom (e.g. "FOR BUSY ADULTS & COMMUTERS")
- Dark background (black, navy, deep green) + bright accent color → bestseller pattern

**Back cover must have:**
- Matching background color to front (same palette — NOT different color)
- Book title repeated + author name
- 3–5 bullet benefits (what they get)
- 3 sample puzzles/grids at different difficulty levels
- Barcode area: bottom-right, white, blank

**Avoid:**
- Front and back being different color families
- Cluttered text — max 5 text elements per zone
- AI-generated text inside artwork (always remove with "DO NOT include text" clause)
- Bleed zone content (safe = 0.375" from trim edge)

---

## Sudoku Color Schemes Available

Auto-selected based on concept keywords. Can be forced via `front_color_scheme` in bookinfo.md.

| Scheme | Background | Accent | Best for |
|--------|-----------|--------|----------|
| `black` | #0E0E10 | Gold #E9C76A | Premium, gift, luxury |
| `navy` | #1A2744 | Teal #4ECDC4 | Professional, brain training |
| `green` | #1B5E3F | Red pill | Seniors, large print |
| `teal` | #0D7377 | Gold | Mindfulness, calm |
| `purple` | #5B21B6 | Yellow | Creative, fun |
| `burgundy` | #6B1D3A | Gold | Cozy, gift, Christmas |
| `charcoal` | #2C2C2C | Purple | Premium, unisex |
| `rose` | #B5446E | White | Feminine, self-care |
| `forest` | #2D4A22 | Amber | Nature, outdoor |
| `blue` | #1E5DD8 | Yellow | Kids, bright |

---

## Output

```
COVER GENERATED!

Cover PNG: output/{theme_key}/cover.png
Cover PDF: output/{theme_key}/cover.pdf  ← Upload this to KDP

Dimensions: {W}px × {H}px  ({full_w}" × {full_h}")
Spine:      {spine}" ({pages} pages)
Scheme:     {color_scheme}
Renderer:   openai (codex) / programmatic
```
