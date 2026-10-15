#!/usr/bin/env bash
set -euo pipefail

# ─────────────────────────────────────────────
#   Google Ads Copy — Claude Code Skill
#   Uninstaller
# ─────────────────────────────────────────────

SKILL_DIR="$HOME/.claude/skills/google-ads-copy"
AGENT_DIR="$HOME/.claude/agents"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${BOLD}Uninstalling Google Ads Copy skill...${NC}"
echo ""

# ── Remove skills ────────────────────────────

if [ -d "$SKILL_DIR" ]; then
    rm -rf "$SKILL_DIR"
    echo -e "  ${GREEN}✓${NC} Removed skills from ${SKILL_DIR}"
else
    echo -e "  ${YELLOW}!${NC} Skills directory not found at ${SKILL_DIR} — skipping"
fi

# ── Remove agents ────────────────────────────

AGENTS=(
    "full-rsa-workflow.md"
    "bulk-ad-generator.md"
    "competitor-to-ad.md"
    "copy-audit-agent.md"
)

for agent in "${AGENTS[@]}"; do
    if [ -f "$AGENT_DIR/$agent" ]; then
        rm "$AGENT_DIR/$agent"
        echo -e "  ${GREEN}✓${NC} Removed agent: ${agent}"
    else
        echo -e "  ${YELLOW}!${NC} Agent not found: ${agent} — skipping"
    fi
done

# ── Done ─────────────────────────────────────

echo ""
echo -e "${GREEN}${BOLD}Uninstall complete.${NC}"
echo ""
