---
name: frontend-design
description: >
  This skill should be used when the user asks to "build a page", "create component",
  "make a dashboard", "landing page", "style this", "beautify", "make it look good",
  "UI for", "web app", "build a website", "create a form". Creates distinctive,
  production-grade frontend interfaces with high design quality. Generates creative,
  polished code avoiding generic AI aesthetics.
  DO NOT trigger on: "review this design", "critique the UI", "what do you think
  of this layout" (those are review/feedback, not building).
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.

## Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

## Frontend Aesthetics Guidelines

Focus on:
- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

Remember: Claude is capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.

## Motion & Animation

For React projects, use **framer-motion** (v10+) for orchestrated animations:
- Page entry: staggered reveals with `variants` and `staggerChildren`
- Scroll-triggered: `whileInView` with `viewport={{ once: true }}`
- Hover micro-interactions: `whileHover` and `whileTap` for tactile feel

For plain HTML/CSS, prefer CSS-only solutions: `@keyframes`, `animation-delay` for staggers, `scroll-timeline` for modern browsers, `:hover` transitions.

## Execution Checklist

Before delivering, verify:
- Aesthetic direction locked (not default/generic)
- Typography paired (display + body, loaded via Google Fonts or similar)
- Color palette defined as CSS variables
- At least one "wow" moment identified (animation, layout break, visual surprise)
- Tested at 2+ viewport widths (mobile + desktop)
- No Inter, Roboto, or Arial anywhere
- GEO checks pass (see below)

## GEO Awareness (AI Search Optimization)

Every HTML page you build must be optimized for AI search engines (ChatGPT, Perplexity, Claude, Google AI Overviews). These are not optional extras -- they are baseline requirements:

- **Meta description**: Always include `<meta name="description" content="...">` (150-160 chars, phrased to answer a question)
- **JSON-LD structured data**: Add `<script type="application/ld+json">` with appropriate schema (Organization, WebPage, Article, Product, FAQ, etc.)
- **First 200 words**: Must be self-contained and fact-rich. AI engines pull citations from the opening content. No filler intros like "Welcome to our site"
- **Semantic HTML**: Use `<article>`, `<section>`, `<nav>`, `<main>`, `<header>`, `<footer>`. AI crawlers rely on structure to understand content hierarchy
- **Server-side rendering**: Content must be visible in raw HTML. GPTBot, ClaudeBot, PerplexityBot cannot execute JavaScript. Critical content must not be JS-rendered only
- **AI crawler access**: Include `<meta name="robots" content="index, follow, max-snippet:-1">` to allow full-length AI citations
- **H1 tag**: Every page needs exactly one `<h1>` that clearly describes the page topic
- **Open Graph tags**: Include `og:title`, `og:description`, `og:image` for social sharing and AI context

## GEO Awareness (AI Search Optimization)

When building pages that will be publicly accessible, apply these GEO (Generative Engine Optimization) practices so the content performs well in AI-powered search engines (ChatGPT, Perplexity, Google AI Overviews, Claude):

- **Meta description**: Always include `<meta name="description" content="...">` (150-160 chars). Write it as a direct answer to the page's core question -- AI engines use this as the primary snippet source.
- **JSON-LD structured data**: Add `<script type="application/ld+json">` with the appropriate schema (Organization, WebPage, Product, FAQPage, etc.). This gives AI crawlers structured context about the page.
- **First 200 words**: The opening content must be self-contained, fact-rich, and directly answer what the page is about. AI snippet generators pull heavily from early content.
- **Semantic HTML**: Use `<article>`, `<section>`, `<nav>`, `<main>`, `<header>`, `<footer>` -- AI crawlers rely on semantic structure to understand content hierarchy. Avoid `<div>` soup.
- **Server-side rendering**: Ensure content is present in the initial HTML response. GPTBot, ClaudeBot, and most AI crawlers cannot execute JavaScript. If using React/Vue/Svelte, verify SSR or pre-rendering is in place.
- **AI crawler access**: Add `<meta name="robots" content="index, follow, max-snippet:-1">` to allow AI engines to use longer snippets from the content.
- **Heading hierarchy**: Always include one `<h1>` that clearly states the page topic. Use `<h2>`/`<h3>` for subtopics. AI engines use headings as topic signals.
