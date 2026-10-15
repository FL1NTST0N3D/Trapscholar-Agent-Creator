#!/usr/bin/env bash
set -euo pipefail

echo "Uninstalling YouTube Ads Claude..."

rm -rf ~/.claude/skills/youtube-ads
rm -rf ~/.claude/skills/yt-*
rm -f ~/.claude/agents/campaign-auditor.md
rm -f ~/.claude/agents/creative-analyst.md
rm -f ~/.claude/agents/targeting-optimizer.md
rm -f ~/.claude/agents/report-generator.md

echo "✓ YouTube Ads Claude uninstalled successfully"
