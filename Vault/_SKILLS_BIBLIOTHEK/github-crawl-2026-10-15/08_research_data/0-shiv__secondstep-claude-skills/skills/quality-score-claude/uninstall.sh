#!/usr/bin/env bash
set -euo pipefail

# ============================================================
#   Quality Score Claude — Uninstaller
# ============================================================

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

SKILL_DIR="$HOME/.claude/skills/quality-score-claude"
AGENT_DIR="$HOME/.claude/agents"

AGENTS=(
    "qs-analyst.md"
    "qs-monitor.md"
    "qs-optimizer.md"
    "qs-reporter.md"
)

echo ""
echo -e "${BOLD}Quality Score Claude — Uninstaller${NC}"
echo ""

# ── Remove skill directory ───────────────────────────────────

if [ -d "$SKILL_DIR" ]; then
    rm -rf "$SKILL_DIR"
    echo -e "  ${GREEN}[OK]${NC} Removed $SKILL_DIR"
else
    echo -e "  ${YELLOW}[!] Skill directory not found: $SKILL_DIR${NC}"
fi

# ── Remove agent files ───────────────────────────────────────

for agent in "${AGENTS[@]}"; do
    AGENT_PATH="$AGENT_DIR/$agent"
    if [ -f "$AGENT_PATH" ]; then
        rm "$AGENT_PATH"
        echo -e "  ${GREEN}[OK]${NC} Removed agent: $agent"
    fi
done

echo ""
echo -e "${GREEN}${BOLD}Uninstall complete.${NC} Quality Score Claude has been removed."
echo ""
