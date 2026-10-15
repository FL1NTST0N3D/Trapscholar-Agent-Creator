#!/usr/bin/env bash
set -euo pipefail

echo "Uninstalling LinkedIn Ads Claude..."

rm -rf ~/.claude/skills/linkedin
rm -rf ~/.claude/skills/li-*
rm -f ~/.claude/agents/linkedin-*.md

echo "✓ LinkedIn Ads Claude uninstalled successfully"
