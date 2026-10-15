# Contributing to Conversion Tracking Claude

Thanks for your interest in contributing! This guide will help you get started.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Test your changes
6. Commit: `git commit -m "Add your feature"`
7. Push: `git push origin feature/your-feature`
8. Open a Pull Request

## Project Structure

- `SKILL.md` — Main skill orchestrator (do not exceed 500 lines)
- `skills/track-*/SKILL.md` — Sub-skills for each platform/feature
- `agents/*.md` — Subagent definitions
- `scripts/*.py` — Python validation utilities
- `templates/` — Report and checklist templates
- `docs/` — Extended documentation

## Guidelines

### SKILL.md Files
- Keep each SKILL.md under 500 lines
- Use kebab-case for directory names (e.g., `track-google-tag`)
- Include clear validation steps and expected outputs
- Reference the Tracking Health Score rubric from the main SKILL.md

### Python Scripts
- Target Python 3.8+ compatibility
- Add type hints to function signatures
- Include docstrings for public functions
- List new dependencies in `requirements.txt`

### Documentation
- Use Markdown for all docs
- Include practical examples
- Keep language concise and actionable

## Reporting Issues

- Use GitHub Issues
- Include steps to reproduce
- Specify which platform/sub-skill is affected
- Include the Tracking Health Score output if applicable

## Code of Conduct

Be respectful, constructive, and helpful. We are all here to make conversion tracking less painful.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
