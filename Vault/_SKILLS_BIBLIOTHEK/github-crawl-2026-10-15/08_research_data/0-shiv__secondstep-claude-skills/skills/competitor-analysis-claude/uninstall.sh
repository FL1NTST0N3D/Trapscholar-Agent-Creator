#!/usr/bin/env bash
set -euo pipefail

echo "Uninstalling Competitor Analysis Claude..."

rm -rf ~/.claude/skills/competitor
rm -rf ~/.claude/skills/comp-*
rm -f ~/.claude/agents/ci-researcher.md
rm -f ~/.claude/agents/ci-analyst.md
rm -f ~/.claude/agents/ci-strategist.md

echo "✓ Competitor Analysis Claude uninstalled successfully"
