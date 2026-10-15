# Contributing to Google Ads Copy — Claude Code Skill

Thanks for your interest in contributing! This guide covers everything you need to get started.

## How to Contribute

### Reporting Issues

- Open a GitHub issue with a clear title and description.
- Include the command you ran (e.g., `/copy generate`), the input you provided, and what went wrong.
- If the output had incorrect character counts or formatting, paste the relevant section.

### Suggesting New Frameworks or Commands

- Open an issue with the tag `enhancement`.
- Describe the copywriting framework or command, who it helps, and provide an example.

### Submitting Pull Requests

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes.
4. Test your changes by running the relevant `/copy` commands in Claude Code.
5. Commit with a clear message: `git commit -m "Add XYZ framework to headline formulas"`
6. Push and open a pull request against `main`.

## Code Standards

### SKILL.md Files

- Every sub-skill SKILL.md must include: purpose, required inputs, output format, and examples.
- Character limits must be explicitly stated and enforced.
- Framework tags must be included in all output examples.

### Python Scripts

- Scripts must work with Python 3.8+ and use only the standard library (no external dependencies).
- Include docstrings and usage examples.
- Follow PEP 8 style guidelines.

### Templates

- Templates must use Markdown format.
- Include placeholder tokens (e.g., `{{BUSINESS_NAME}}`, `{{KEYWORD}}`) for dynamic content.

### Agent Workflows

- Each agent `.md` file must define: goal, steps, sub-skills used, and expected output.
- Agents should reference existing sub-skills rather than duplicating logic.

## Adding a New Sub-Skill

1. Create a new directory under `skills/` (e.g., `skills/copy-new-feature/`).
2. Add a `SKILL.md` with the standard structure: Commands, Required Inputs, Output Format, Examples.
3. Register the command in the root `SKILL.md` router table.
4. Add the command entry to `skill.json`.
5. Update `README.md` with the new command.
6. Update `CLAUDE.md` architecture section.

## Adding a New Agent

1. Create a new `.md` file in `agents/`.
2. Define the multi-step workflow referencing existing sub-skills.
3. Register the agent in `skill.json`.

## Questions?

Open an issue or reach out to [@0-shiv](https://github.com/0-shiv).
