# Schema Markup Claude

JSON-LD structured data generation, validation, and deployment skill for Claude Code.

## Architecture

- `SKILL.md` -- Main skill definition, routes all `/schema` commands
- `skills/schema-*/SKILL.md` -- 11 specialized sub-skills (organization, local-business, product, faq, howto, article, video, breadcrumb, event, validator, report)
- `templates/*.json` -- Pre-built JSON-LD templates for 12 schema types
- `scripts/*.py` -- Python utilities (generator, validator, report crawler)
- `agents/` -- 3 agents: schema-audit, schema-migration, schema-deployment

## Commands

| Command | Sub-Skill |
|---------|-----------|
| `/schema generate <type>` | Generate any supported schema type |
| `/schema organization` | Company identity, logo, social profiles |
| `/schema local-business` | NAP, hours, geo, service areas |
| `/schema product` | Product + Offer for e-commerce |
| `/schema faq` | FAQPage Q&A pairs |
| `/schema howto` | Steps, tools, supplies, timing |
| `/schema article` | Article/BlogPosting/NewsArticle |
| `/schema video` | VideoObject, thumbnails, livestream |
| `/schema breadcrumb` | BreadcrumbList navigation |
| `/schema event` | Events with location, offers |
| `/schema validate` | Validate against Google requirements |
| `/schema report` | Site-wide coverage report |

## Development Rules

- Keep SKILL.md files under 500 lines
- Use kebab-case for directory names (e.g., `schema-local-business`)
- JSON-LD only -- no Microdata or RDFa generation
- All generated schema must be wrapped in `<script type="application/ld+json">` tags
- Validate against Google rich result requirements, not just Schema.org spec
- Never use example.com placeholders -- always prompt for real URLs
- Prefer nested entities over flat references
- Agents run via Task tool with `context: fork`
- All output files go to current working directory
