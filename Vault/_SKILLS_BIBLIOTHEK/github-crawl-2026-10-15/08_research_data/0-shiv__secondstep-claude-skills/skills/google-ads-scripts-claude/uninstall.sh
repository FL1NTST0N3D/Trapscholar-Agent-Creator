#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Google Ads Scripts Claude — Uninstaller
# ============================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

INSTALL_DIR="${HOME}/.claude/skills/google-ads-scripts-claude"
AGENTS_DIR="${HOME}/.claude/agents"

echo ""
echo -e "${BOLD}Google Ads Scripts Claude — Uninstaller${NC}"
echo ""

REMOVED=0

# Remove skills directory
if [ -d "${INSTALL_DIR}" ]; then
    rm -rf "${INSTALL_DIR}"
    echo -e "  ${GREEN}Removed${NC} ${INSTALL_DIR}/"
    REMOVED=1
else
    echo -e "  ${YELLOW}Skills directory not found${NC} (${INSTALL_DIR}/)"
fi

# Remove agent files
AGENTS=("script-builder.md" "script-debugger.md" "script-optimizer.md")
for agent in "${AGENTS[@]}"; do
    if [ -f "${AGENTS_DIR}/${agent}" ]; then
        rm -f "${AGENTS_DIR}/${agent}"
        echo -e "  ${GREEN}Removed${NC} ${AGENTS_DIR}/${agent}"
        REMOVED=1
    fi
done

echo ""

if [ "${REMOVED}" -eq 1 ]; then
    echo -e "${GREEN}${BOLD}Uninstall complete.${NC} All Google Ads Scripts Claude files have been removed."
else
    echo -e "${YELLOW}Nothing to uninstall.${NC} No installed files were found."
fi
