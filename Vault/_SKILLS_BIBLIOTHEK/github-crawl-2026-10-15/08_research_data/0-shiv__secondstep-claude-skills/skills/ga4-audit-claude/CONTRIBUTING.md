# Contributing to GA4 Audit Claude Skill

Thank you for your interest in contributing to this project. This guide covers how to get involved.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch from `main`
4. Make your changes
5. Submit a pull request

## Project Structure

- **`skills/`** — Sub-skill definitions (one per audit dimension). Each sub-skill has its own `SKILL.md`.
- **`agents/`** — Agent definitions for audit orchestration.
- **`scripts/`** — Python utility scripts (health score calculator, event validator, report generator).
- **`docs/`** — Reference documentation and methodology.

## Types of Contributions

### Adding a New Audit Check

1. Identify which dimension the check belongs to (e.g., events, conversions, e-commerce).
2. Edit the corresponding `skills/<dimension>/SKILL.md` file.
3. Add the check to the appropriate checklist section.
4. Include impact level (High/Medium/Low), expected configuration, and fix instructions.
5. Update the scoring criteria if the new check changes the dimension's total.

### Improving Documentation

- Reference data lives in `docs/`.
- Event references should follow GA4's official naming conventions.
- Keep `common-issues.md` updated with newly discovered misconfigurations.

### Adding Python Scripts

- Scripts go in `scripts/`.
- Use Python 3.8+ compatible syntax.
- Stick to the standard library (no external dependencies).
- Include docstrings and `--help` argument support.
- Add usage examples in the script's module docstring.

### Adding Agent Definitions

- Agent files go in `agents/`.
- Each agent should have a clear role, defined capabilities, and orchestration rules.
- Follow the existing format in `agents/audit-orchestrator.md`.

## Code Style

- **Python**: Follow PEP 8. Use type hints. Include docstrings.
- **Markdown**: Use ATX-style headers (`#`). Use fenced code blocks with language identifiers.
- **GA4 Events**: Always use snake_case (e.g., `add_to_cart`, not `AddToCart`).

## Commit Messages

Use clear, descriptive commit messages:

```
Add cross-domain tracking check to data streams audit
Fix ecommerce weight calculation for non-ecommerce properties
Update GA4 event reference with new recommended events
```

## Pull Request Guidelines

- Keep PRs focused on a single change.
- Reference any related issues.
- Describe what the PR does and why.
- Test Python scripts locally before submitting.

## Reporting Issues

Open an issue on GitHub with:

- A clear title describing the problem or suggestion.
- Steps to reproduce (for bugs).
- Expected vs. actual behavior.
- GA4 property type (e-commerce, lead gen, SaaS, etc.) if relevant.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
