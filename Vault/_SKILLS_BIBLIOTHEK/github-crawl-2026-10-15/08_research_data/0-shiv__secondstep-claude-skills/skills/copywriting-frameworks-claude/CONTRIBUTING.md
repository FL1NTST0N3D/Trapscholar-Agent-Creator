# Contributing to Copywriting Frameworks for Claude Code

Thanks for your interest in contributing! This project aims to be the most comprehensive collection of copywriting frameworks for Claude Code.

## How to Contribute

### Adding a New Framework

1. **Fork and clone** this repository.
2. Create a new skill directory: `skills/copy-<framework-name>/`
3. Add a `SKILL.md` inside the directory following the existing pattern:
   - Framework name and description
   - Step-by-step pattern
   - When to use / when not to use
   - Channel-specific adaptations
   - At least 3 examples across different industries
   - Tone modifier support
4. Update the root `SKILL.md` framework reference table.
5. Update `README.md` commands table if adding a new command.
6. Update `CHANGELOG.md` under an `[Unreleased]` section.
7. Submit a pull request.

### Improving Existing Frameworks

- Add more examples (especially industry-specific ones)
- Improve prompt instructions in SKILL.md files
- Add channel-specific formatting rules
- Fix copy errors or unclear instructions

### Adding Documentation

- Industry-specific examples in `docs/industry-examples.md`
- New entries in `docs/framework-cheatsheet.md`
- Testing methodology in `docs/testing-guide.md`

## Pull Request Guidelines

1. **One framework per PR.** Keep changes focused.
2. **Test your skill.** Run it in Claude Code with at least 2 different products/audiences before submitting.
3. **Follow naming conventions.** `copy-<name>` for directories, lowercase and hyphenated.
4. **Keep SKILL.md actionable.** Write instructions Claude can follow, not academic theory.
5. **Include examples.** Every framework needs concrete examples showing the pattern in action.

## Style Guide

- Use clear, direct language in SKILL.md files
- Prefer tables for structured reference data
- Use code blocks for copy templates and fill-in patterns
- Keep line lengths reasonable (wrap at ~100 chars in prose)
- No emoji in SKILL.md files (they are instructions, not decoration)

## Reporting Issues

- Open a GitHub issue for bugs, unclear instructions, or framework requests
- Include the command you ran and what you expected vs. what you got
- Label issues: `bug`, `enhancement`, `new-framework`, or `docs`

## Code of Conduct

Be professional. Be helpful. Respect others' time. This is a tool for marketers and copywriters — keep contributions practical and high-quality.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
