#!/usr/bin/env bash
set -euo pipefail

echo "Uninstalling Conversion Tracking Claude..."

# Remove main skill
rm -rf ~/.claude/skills/conversion-tracking

# Remove sub-skills
rm -rf ~/.claude/skills/track-google-tag
rm -rf ~/.claude/skills/track-enhanced-conversions
rm -rf ~/.claude/skills/track-server-side
rm -rf ~/.claude/skills/track-offline-import
rm -rf ~/.claude/skills/track-meta-pixel
rm -rf ~/.claude/skills/track-meta-capi
rm -rf ~/.claude/skills/track-linkedin-insight
rm -rf ~/.claude/skills/track-tiktok-pixel
rm -rf ~/.claude/skills/track-attribution
rm -rf ~/.claude/skills/track-report

# Remove agents
rm -f ~/.claude/agents/audit_orchestrator.md
rm -f ~/.claude/agents/tag_inspector.md
rm -f ~/.claude/agents/data_quality_agent.md
rm -f ~/.claude/agents/report_generator.md

echo "✓ Conversion Tracking Claude uninstalled successfully"
