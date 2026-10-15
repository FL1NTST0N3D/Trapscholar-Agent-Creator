# Contributing to Quality Score Claude

Thanks for your interest in contributing. This guide covers the process for submitting changes.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch from `main`

```bash
git checkout -b feature/your-feature-name
```

## Project Structure

- **Sub-skills** go in `skills/<skill-name>/SKILL.md`
- **Agents** go in `agents/<agent-name>.md`
- **Python scripts** go in `scripts/`
- **Templates** go in `templates/`
- **Documentation** goes in `docs/`

## Adding a New Sub-Skill

1. Create a new directory under `skills/` with a descriptive name prefixed with `qs-`
2. Add a `SKILL.md` inside that directory with the skill definition
3. Register the command in the main `SKILL.md` command routing table
4. Update `README.md` with the new command

## Writing Guidelines

- All QS analysis output must follow the standard format: Summary, Key Metrics, Analysis, Action Items, Estimated Impact
- Always attach dollar values to QS findings
- Prioritize recommendations by spend-weighted impact
- Use clear, direct language. No jargon without explanation.

## Submitting Changes

1. Commit your changes with a clear message
2. Push to your fork
3. Open a Pull Request against `main`
4. Describe what your change does and why

## Code Style

- Python scripts: follow PEP 8
- Markdown: use ATX-style headers (`#`), pipe tables, fenced code blocks
- Keep lines under 120 characters where practical

## Reporting Issues

Open an issue with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Any relevant data (redact account-specific information)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
