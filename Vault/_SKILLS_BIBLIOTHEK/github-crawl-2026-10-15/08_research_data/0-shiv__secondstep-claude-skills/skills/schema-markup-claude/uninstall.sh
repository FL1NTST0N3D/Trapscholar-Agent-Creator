#!/usr/bin/env bash
set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║                                                  ║${NC}"
echo -e "${CYAN}║${NC}   ${RED}Schema Markup Claude${NC} — Uninstaller            ${CYAN}║${NC}"
echo -e "${CYAN}║                                                  ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════╝${NC}"
echo ""

SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

echo -e "${BLUE}Removing installed components...${NC}"

# Remove main skill
if [ -d "$SKILLS_DIR/schema-markup" ]; then
    rm -rf "$SKILLS_DIR/schema-markup"
    echo -e "${GREEN}✓ Removed main skill${NC}"
fi

# Remove sub-skills
REMOVED=0
for sub_skill in schema-organization schema-local-business schema-product \
                 schema-faq schema-howto schema-article schema-video \
                 schema-breadcrumb schema-event schema-validator schema-report; do
    if [ -d "$SKILLS_DIR/$sub_skill" ]; then
        rm -rf "$SKILLS_DIR/$sub_skill"
        REMOVED=$((REMOVED + 1))
    fi
done
echo -e "${GREEN}✓ Removed $REMOVED sub-skills${NC}"

# Remove agents
AGENTS_REMOVED=0
for agent in schema-audit-agent.md schema-migration-agent.md schema-deployment-agent.md; do
    if [ -f "$AGENTS_DIR/$agent" ]; then
        rm -f "$AGENTS_DIR/$agent"
        AGENTS_REMOVED=$((AGENTS_REMOVED + 1))
    fi
done
if [ "$AGENTS_REMOVED" -gt 0 ]; then
    echo -e "${GREEN}✓ Removed $AGENTS_REMOVED agents${NC}"
fi

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Uninstall complete!                             ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}Note: The cloned repository was not removed.${NC}"
echo -e "${YELLOW}Delete it manually if you no longer need it.${NC}"
echo ""
