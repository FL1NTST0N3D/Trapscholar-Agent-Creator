# Contributing to Product Feed Claude

Thank you for your interest in contributing. This guide covers the process for submitting changes.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/product-feed-claude.git
   cd product-feed-claude
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## What to Contribute

### High-Value Contributions
- **New category templates** — title/description templates for underserved product categories
- **Scoring improvements** — better heuristics for title, description, or image quality detection
- **Feed format support** — XML feed parsing, Google Sheets integration
- **Localization** — country-specific attribute requirements (EU energy labels, Japan loyalty points)
- **Bug fixes** — GTIN validation edge cases, delimiter detection improvements

### Sub-Skill Contributions
Each sub-skill lives in `skills/<name>/SKILL.md`. When adding or modifying a sub-skill:
- Follow the existing format (Command, Overview, Rules, Process, Scoring, Output, Impact)
- Include real Google Merchant Center specifications, not assumptions
- Provide specific, actionable recommendations in the output format
- Add scoring criteria with clear thresholds

### Script Contributions
Python scripts live in `scripts/`. Requirements:
- Python 3.8+ compatibility
- Use only dependencies listed in `requirements.txt` (pandas, openpyxl)
- Include docstrings and type hints
- Deterministic output — same input must produce same output
- Handle edge cases (empty feeds, missing columns, malformed data)

## Code Style

- Python: Follow PEP 8, use type hints, write docstrings
- Markdown: Use ATX-style headers (`#`), tables for structured data
- Commit messages: Present tense, imperative mood ("Add feature" not "Added feature")

## Pull Request Process

1. Ensure your changes work against a real feed file (or the test feed in `assets/`)
2. Update documentation if you changed commands, scoring, or output format
3. Update `CHANGELOG.md` with your changes under "Unreleased"
4. Submit a PR with:
   - Clear title describing the change
   - Description of what changed and why
   - Test results if applicable

## Reporting Issues

Open a GitHub issue with:
- What you expected to happen
- What actually happened
- Feed file sample (anonymized) if relevant
- Python version and OS

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
