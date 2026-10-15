# 🎨 design-system-extractor

> An AI agent skill that reverse-engineers Design Systems from any website — extracting colors, typography, spacing, and components — and generates complete, interactive HTML documentation.

![Version](https://img.shields.io/badge/version-2.0.0-3ecf8e?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow?style=flat-square)

---

## What it does

`design-system-extractor` is an AI agent skill that takes any public website URL and produces a complete, single-file HTML design system reference — similar to Storybook or a Figma Design System doc, but generated entirely from the live site.

It works around the AI token limit problem by running a **Python pre-processor** first: sanitizing HTML, extracting CSS variables from `:root`, detecting Tailwind utility classes, and mapping component patterns. Only the compact JSON result is passed to the AI for analysis and generation.

### Output includes

- ✅ Complete color palette (CSS variables, Radix scales, hex values, usage notes)
- ✅ Typography scale (font families, sizes, weights, line-heights, letter-spacing)
- ✅ Spacing system with named tokens
- ✅ Border radius, shadows, and transition tokens
- ✅ Interactive component demos: buttons, badges, forms, cards, alerts, navigation
- ✅ Real images and logos pulled directly from the source site
- ✅ Syntax-highlighted code blocks with CSS variable snippets
- ✅ Scroll progress indicator + smooth navigation

---

## Live Example — Supabase Design System

This repo includes a complete design system reference generated from **[supabase.com](https://supabase.com)** using this skill.

👉 **[View the generated output: `supabase_design_system.html`](./supabase_design_system.html)**

### Preview

The Supabase output covers:

| Section | What's documented |
|---|---|
| **Colors** | 12-step brand green scale, Radix Slate grays, surface layers, status colors |
| **Typography** | Inter + Source Code Pro, 6-level type scale, letter-spacing & line-height system |
| **Spacing** | 2px base scale, xs→2xl named tokens, max content width (1128px) |
| **Border Radius** | xs (2px) through full (9999px) with visual demos |
| **Buttons** | Primary, Default, Outline, Ghost, Danger — 3 sizes each |
| **Badges** | 7 color variants with real-site label examples |
| **Forms** | Text input, select, textarea, toggle, checkbox — all states |
| **Cards** | Feature cards, stat cards, partner logo cards |
| **Navigation** | Sticky nav bar with blur, logo, links, CTA |
| **Alerts** | Success, info, warning, error variants |
| **Code Blocks** | Syntax-highlighted JS + SQL examples |
| **Transitions** | Fast/Normal/Slow with hover preview |
| **Partner Logos** | Real logos (Mozilla, GitHub, 1Password, PwC, LangChain…) |

---

## Repository structure

```
design-system-extractor/
│
├── README.md                          ← You are here
│
├── supabase_design_system.html        ← Example output (Supabase)
│
└── skills/
    └── design-system-extractor/
        ├── SKILL.md                   ← Skill definition
        └── tools/
            ├── design_system_extractor.py   ← Main extraction script
            ├── extract_tokens.py            ← Standalone CSS token extractor
            ├── requirements.txt             ← Python dependencies
            └── README.md                    ← Tool-level docs
```

---

## Installation

### One-line install with npx

```bash
npx skills add kalilfagundes/design-system-extractor-skill --skill design-system-extractor
```

This installs the skill into your local agent directory and makes it available to Cursor, Windsurf, and other supported agents automatically.

> Requires [skills CLI](https://www.npmjs.com/package/skills) — installed automatically via `npx`.

### Manual install

1. Clone or download this repo
2. Copy `skills/design-system-extractor/` into your agent's skills directory (e.g. `~/.agents/skills/`)
3. The skill will be auto-detected as `design-system-extractor`

### Prerequisites

- Any AI agent that supports skills (`.md`-based skill definitions)
- Python 3.8+

---

## How to use the skill

### Running it

Simply prompt your agent:

```
Extract the design system from this site: https://example.com
```

Or any of these trigger phrases:

- *"Analyze the design of this website"*
- *"Create design system documentation for [URL]"*
- *"Reverse engineer the UI from this site"*
- *"Extract colors and typography from [URL]"*

The agent will:
1. Run the Python pre-processor on the URL
2. Parse the resulting JSON
3. Generate a complete `design_pattern.html` file in your output folder

---

## Running the Python tools directly

You can also run the extraction scripts standalone, without any agent.

### Full site extraction

```bash
cd skills/design-system-extractor/tools/

# Install dependencies
pip install -r requirements.txt

# Extract design system data from any URL
python design_system_extractor.py https://example.com
# → Saves design_system_data.json
```

### CSS token extraction only

```bash
python extract_tokens.py https://example.com/path/to/styles.css
# → Prints colors, fonts, font sizes, line heights, component classes
```

### What `design_system_extractor.py` outputs

```json
{
  "url": "https://example.com",
  "fonts": ["Inter", "Source Code Pro"],
  "css_variables": {
    "color-brand": "#3ECF8E",
    "font-family-body": "Inter"
  },
  "colors": ["#3ECF8E", "#020405", "#111415"],
  "classes": ["btn-primary", "card", "nav-bar"],
  "tailwind_tokens": {
    "colors": ["bg-[#3ECF8E]", "text-slate-900"],
    "spacing": ["p-4", "gap-8", "m-6"],
    "typography": ["font-bold", "text-xl", "tracking-tight"]
  },
  "components": [
    { "type": "button", "count": 8 },
    { "type": "card", "count": 126 },
    { "type": "navigation", "count": 2 }
  ],
  "images": ["https://example.com/logo.png", "..."]
}
```

---

## How it works

The skill solves a core problem: websites are too large to feed to an AI token window. A typical homepage can be 500KB+ of HTML, SVGs, and scripts.

```
Website URL
    │
    ▼
┌─────────────────────────────┐
│  Python Pre-Processor       │
│                             │
│  1. Fetch HTML              │
│  2. Strip SVGs, scripts,    │
│     base64, iframes         │
│  3. Keep structure only     │
│  4. Fetch CSS files         │
│  5. Extract :root variables │
│  6. Detect Tailwind tokens  │
│  7. Map component classes   │
└──────────────┬──────────────┘
               │ compact JSON (~5KB)
               ▼
┌─────────────────────────────┐
│  AI Agent Analysis          │
│                             │
│  • Classify color roles     │
│  • Build type scale         │
│  • Map component patterns   │
│  • Inject real image URLs   │
│  • Generate HTML output     │
└──────────────┬──────────────┘
               │
               ▼
    design_pattern.html
```

### Why Python pre-processing?

| Without pre-processing | With pre-processing |
|---|---|
| Raw HTML: 200–500KB | Sanitized JSON: ~5KB |
| Token limit hit instantly | Fits comfortably in context |
| SVGs bloat the context | SVGs stripped entirely |
| Base64 images waste tokens | Base64 removed, URLs kept |
| Expensive per-request | ~10x cheaper |

---

## Anti-hallucination design

The skill is built with strict grounding rules:

- All colors must come from the extracted JSON — no invented hex values
- All font families must appear in CSS variables or `@font-face` rules
- Missing values use documented defaults (labeled as "Default"), never fabricated data
- Real image URLs from the site are injected directly into the HTML output

---

## Requirements

```
requests>=2.31.0
beautifulsoup4>=4.12.0
```

Install with:

```bash
pip install -r skills/design-system-extractor/tools/requirements.txt
```

---

## Limitations

- Works best on sites using standard CSS (custom properties, Google Fonts)
- Sites with heavy JS rendering or anti-scraping protection may return incomplete data
- Does not copy or reproduce copyrighted content — for reference and educational use only
- Respect font and asset licenses when using extracted resources

---

## License

MIT — free to use, modify, and distribute. See [LICENSE](./LICENSE) for details.

---

## Contributing

PRs are welcome. Areas for improvement:

- Support for CSS-in-JS extraction (styled-components, Emotion)
- Dark/light mode token diffing
- Figma token export format (W3C Design Tokens spec)
- CLI wrapper with flags for output path and section selection
