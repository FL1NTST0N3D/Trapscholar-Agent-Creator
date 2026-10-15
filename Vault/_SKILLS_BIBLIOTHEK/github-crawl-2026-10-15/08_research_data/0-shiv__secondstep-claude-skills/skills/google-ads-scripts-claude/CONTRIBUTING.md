# Contributing to Google Ads Scripts Claude

Thanks for your interest in contributing. This guide covers how to add new scripts, improve existing ones, or fix bugs.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Submit a pull request

## Adding a New Script Template

1. Create the `.js` file in `templates/` following the naming convention: `kebab-case.js`
2. Every template must include:
   - A `CONFIG` object at the top with all configurable values
   - A `function main() {}` entry point
   - Try/catch error handling
   - `Logger.log()` statements for debugging
   - Clear comments explaining each section
3. Use `var` instead of `let`/`const` for broadest Google Ads Scripts compatibility
4. Use GAQL (not deprecated AWQL) for report queries
5. Respect execution limits (30 min runtime, 250K API calls, 50 URL fetches)

## Adding a New Skill Category

1. Create a directory under `skills/` named `script-your-category/`
2. Add a `SKILL.md` inside with:
   - Category overview
   - Available templates and what they do
   - Configuration guidance
   - Common use cases
3. Update `SKILL.md` (root) to include the new category
4. Update `README.md` to list the new category and its scripts
5. Add a corresponding `/script` command entry in `CLAUDE.md`

## Code Style

- JavaScript templates: ES5 compatible (`var`, no `async/await`)
- Python scripts: Python 3.8+ compatible, use type hints
- Markdown: Use ATX-style headers (`#`), fenced code blocks with language tags
- File names: kebab-case for all files

## Pull Request Guidelines

- One feature or fix per PR
- Write a clear description of what changed and why
- If adding a new script, include a brief example of its output
- Make sure existing scripts are not broken by your changes

## Reporting Issues

- Use GitHub Issues
- Include the script name and category
- Describe expected vs actual behavior
- Include any error messages from the Google Ads Scripts console

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
