# Shopify Skills for Claude

Eight opinionated [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) that make Claude write and review **production-grade Shopify themes**, not just syntactically valid Liquid.

AI can already write Liquid. The gap is judgment: knowing that `{{ product.price }}` ships a raw `1999` to the storefront, that an inline `style="..."` gets silently stripped on theme push, that rebuilding variant logic in JavaScript throws away everything Shopify gives you for free. These skills encode that judgment as rules with good/bad examples, so the code Claude produces is the code a senior Shopify developer would sign off on.

Every Liquid example in this repo is validated against the official Shopify docs with the [Shopify Dev MCP](https://shopify.dev/docs/apps/build/devmcp) `validate_theme` tool. If a filter, tag, or object path isn't real, it isn't here.

## The skills

| Skill | What it does |
| --- | --- |
| **shopify-theme-best-practices** | Write production Liquid: `money` filter, `image_url`/`image_tag`, the `t` filter, metafields and line-item properties for custom data, composition over monolithic sections, no inline styles. |
| **shopify-cro-audit** | Audit a storefront for conversion: PDP clarity, sticky add-to-cart, trust signals, cart friction, mobile tap targets, urgency done honestly. Maps each finding to the change that lifts conversion. |
| **shopify-performance-audit** | Core Web Vitals for themes: LCP hero image, `preload_tag`, lazy-loading below the fold, deferring JS, the 50-iteration loop limit, using the Section Rendering API instead of full reloads. |
| **shopify-seo-structured-data** | Technical SEO: Product/Offer/BreadcrumbList JSON-LD, canonical URLs, one `<h1>`, descriptive `alt` text, clean meta. |
| **shopify-accessibility-audit** | WCAG 2.1 AA for themes: semantic HTML, focus states, labelled forms, color contrast, 44px tap targets, accessible variant pickers. |
| **shopify-metafields-architect** | Model custom data the right way: metafields and metaobjects with a defined schema, read via `product.metafields.*`, never by parsing the title, handle, or tags. |
| **shopify-section-builder** | Scaffold a complete Horizon section or block: schema, settings, `{% stylesheet %}`, locale keys, `shopify_attributes`, nested blocks via `content_for`. |
| **review-ai-shopify-liquid** | Audit AI-generated Liquid for the classic mistakes: hallucinated filters, JS variant logic, ignored Section Rendering API, hardcoded routes, raw prices. |

## Install (Claude Code)

Skills live in a `skills/` directory that Claude Code reads automatically. Install them at the user level (available in every project) or per-project.

**User level (recommended):**

```bash
git clone https://github.com/baslefeber/shopify-skills.git
cp -r shopify-skills/skills/* ~/.claude/skills/
```

**Per project:**

```bash
git clone https://github.com/baslefeber/shopify-skills.git
mkdir -p .claude/skills
cp -r shopify-skills/skills/* .claude/skills/
```

Restart Claude Code (or run `/doctor`) and the skills are live. Claude invokes the right one automatically when a task matches its description: ask it to "build a USP bar section" and `shopify-section-builder` fires; ask it to "review this Liquid" and `review-ai-shopify-liquid` fires. You can also name a skill explicitly.

Works the same way anywhere Agent Skills are supported (Claude Code, the Claude apps, the Agent SDK). Each skill is a self-contained folder, so you can install only the ones you want.

## Why these are different

Shopify ships excellent official tooling for *looking things up*. These skills are for *making the right call*. Each rule carries the reason behind it and the failure mode AI code tends to hit, because a rule you understand is one you can override correctly when the situation is genuinely the exception.

## License

MIT. Use them, fork them, ship them.

---

Built by [learnshopify.dev](https://learnshopify.dev), an interactive course for becoming a professional Shopify developer.
