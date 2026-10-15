# Contributing to Schema Markup Claude

Thanks for your interest in contributing. This guide covers the process for submitting changes.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Test your changes with Claude Code
6. Commit with a clear message
7. Push to your fork and open a Pull Request

## Project Structure

```
schema-markup-claude/
  SKILL.md                    # Main skill definition
  skills/schema-*/SKILL.md    # Sub-skills (one per schema type)
  templates/*.json             # JSON-LD templates
  scripts/*.py                 # Python utilities
  agents/*.md                  # Agent definitions
```

## Adding a New Schema Type

1. Create `skills/schema-<type>/SKILL.md` with the sub-skill definition
2. Add a JSON-LD template in `templates/<type>.json`
3. Register the command in the main `SKILL.md`
4. Update `README.md` with the new type

## Guidelines

- **SKILL.md files** must stay under 500 lines
- **Directory names** use kebab-case (e.g., `schema-local-business`)
- **JSON-LD only** -- no Microdata or RDFa
- **Templates** must include all Google-required properties for rich result eligibility
- **Validation** must check against Google requirements, not just Schema.org spec
- **No placeholder URLs** -- templates use descriptive placeholders like `YOUR_WEBSITE_URL`

## Code Style

- Python scripts: follow PEP 8
- JSON templates: 2-space indentation, trailing newline
- Markdown: one sentence per line in source

## Reporting Issues

Open an issue with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Claude Code version (if relevant)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
