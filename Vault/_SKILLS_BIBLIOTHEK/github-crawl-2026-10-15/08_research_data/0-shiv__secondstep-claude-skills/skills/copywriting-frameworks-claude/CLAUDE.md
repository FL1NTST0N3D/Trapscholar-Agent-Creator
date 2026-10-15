# CLAUDE.md — Copywriting Frameworks for Claude Code

## Project Overview

A collection of 25+ battle-tested copywriting frameworks packaged as Claude Code skills and agents. Generates high-converting copy for ads, emails, landing pages, sales pages, and social media.

## Architecture

```
copywriting-frameworks-claude/
├── skills/           # 12 individual framework skills (each has SKILL.md)
│   ├── copy-aida/
│   ├── copy-pas/
│   ├── copy-fab/
│   ├── copy-bab/
│   ├── copy-4cs/
│   ├── copy-storytelling/
│   ├── copy-power-words/
│   ├── copy-headlines/
│   ├── copy-cta-formulas/
│   ├── copy-objection-handling/
│   ├── copy-social-proof/
│   └── copy-report/
├── agents/           # 3 specialized agents
│   ├── copy-strategist.md
│   ├── copy-reviewer.md
│   └── copy-ab-tester.md
├── copy/             # Root copy skill (router for /copy commands)
│   └── SKILL.md
├── scripts/          # Python utilities
│   ├── copy_generator.py
│   └── copy_analyzer.py
├── docs/             # Documentation
│   ├── framework-cheatsheet.md
│   ├── industry-examples.md
│   ├── testing-guide.md
│   └── prompt-engineering.md
├── assets/           # Static assets
├── SKILL.md          # Master skill reference
├── README.md         # GitHub readme
├── CLAUDE.md         # This file
├── LICENSE           # MIT
├── install.sh        # Automated installer
├── uninstall.sh      # Clean uninstaller
├── .gitignore
├── CONTRIBUTING.md
└── CHANGELOG.md
```

## Commands

All commands are invoked via `/copy <subcommand>`:

| Command | Skill Directory |
|---------|----------------|
| `/copy aida` | `skills/copy-aida/` |
| `/copy pas` | `skills/copy-pas/` |
| `/copy fab` | `skills/copy-fab/` |
| `/copy bab` | `skills/copy-bab/` |
| `/copy 4cs` | `skills/copy-4cs/` |
| `/copy story` | `skills/copy-storytelling/` |
| `/copy power-words` | `skills/copy-power-words/` |
| `/copy headlines` | `skills/copy-headlines/` |
| `/copy cta` | `skills/copy-cta-formulas/` |
| `/copy objections` | `skills/copy-objection-handling/` |
| `/copy proof` | `skills/copy-social-proof/` |
| `/copy report` | `skills/copy-report/` |

## Development Rules

1. **Each skill is self-contained.** Every skill directory must have its own `SKILL.md` with complete instructions. No cross-skill dependencies.
2. **SKILL.md is the source of truth.** Claude reads SKILL.md to know what to do. Keep them actionable, not theoretical.
3. **Output formats.** Every framework skill must support: raw copy, structured (labeled sections), variations (3-5 for A/B), and channel-specific formatting.
4. **Tone modifiers.** All skills must respect `--formal`, `--casual`, `--urgent`, `--luxury`, `--technical`, `--playful`, `--empathetic`, `--bold` flags.
5. **No hardcoded examples in output.** Examples in SKILL.md are for Claude's reference. Generated copy must be original based on user input.
6. **Agents route, skills execute.** Agents (copy-strategist, copy-reviewer, copy-ab-tester) analyze and recommend; skills generate the actual copy.
7. **Keep copy/ SKILL.md as the router.** It maps `/copy <subcommand>` to the correct skill directory.
8. **Python scripts are optional utilities.** Core functionality lives in SKILL.md files, not Python. Scripts are helpers for batch processing or analysis.

## Testing

To verify a skill works:
1. Open Claude Code in any project
2. Run the `/copy <subcommand>` with a sample product/audience
3. Check that output follows the framework pattern
4. Verify tone modifiers change the output appropriately

## File Naming Conventions

- Skills: `skills/copy-<name>/SKILL.md` (lowercase, hyphenated)
- Agents: `agents/copy-<name>.md` (lowercase, hyphenated)
- Scripts: `scripts/copy_<name>.py` (lowercase, underscored)
- Docs: `docs/<name>.md` (lowercase, hyphenated)
