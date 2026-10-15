#!/usr/bin/env bash
set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

SKILL_NAME="ga4-audit"
CLAUDE_DIR="$HOME/.claude"
SKILLS_DIR="$CLAUDE_DIR/skills"
AGENTS_DIR="$CLAUDE_DIR/agents"
INSTALL_DIR="$SKILLS_DIR/$SKILL_NAME"

echo ""
echo -e "${BOLD}Uninstalling GA4 Audit Claude Skill...${NC}"
echo ""

# ── Remove Skill Files ──────────────────────────────────
if [ -d "$INSTALL_DIR" ]; then
    rm -rf "$INSTALL_DIR"
    echo -e "  ${GREEN}[ok]${NC} Removed skill files from $INSTALL_DIR/"
else
    echo -e "  ${YELLOW}[skip]${NC} Skill directory not found at $INSTALL_DIR/"
fi

# ── Remove Agent Files ──────────────────────────────────
AGENT_FILES=(
    "audit-orchestrator.md"
    "event-validator.md"
    "ecommerce-debugger.md"
    "report-generator.md"
)

for agent_file in "${AGENT_FILES[@]}"; do
    if [ -f "$AGENTS_DIR/$agent_file" ]; then
        rm "$AGENTS_DIR/$agent_file"
        echo -e "  ${GREEN}[ok]${NC} Removed agent: $agent_file"
    else
        echo -e "  ${YELLOW}[skip]${NC} Agent not found: $agent_file"
    fi
done

echo ""
echo -e "${GREEN}${BOLD}Uninstall complete.${NC}"
echo -e "The GA4 Audit skill has been removed from your Claude Code installation."
echo ""
