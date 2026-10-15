#!/usr/bin/env bash
set -euo pipefail

# ─────────────────────────────────────────────
#   Google Ads Copy — Claude Code Skill
#   Installer
# ─────────────────────────────────────────────

REPO="0-shiv/google-ads-copy-claude"
SKILL_DIR="$HOME/.claude/skills/google-ads-copy"
AGENT_DIR="$HOME/.claude/agents"
TEMP_DIR=$(mktemp -d)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${CYAN}${BOLD}"
echo "  ╔══════════════════════════════════════════╗"
echo "  ║   Google Ads Copy — Claude Code Skill    ║"
echo "  ║   RSA Generator • Headline Formulas      ║"
echo "  ║   Ad Strength • Emotional Triggers       ║"
echo "  ╚══════════════════════════════════════════╝"
echo -e "${NC}"

# ── Prerequisite checks ──────────────────────

echo -e "${BOLD}Checking prerequisites...${NC}"

missing=0

if ! command -v git &> /dev/null; then
    echo -e "  ${RED}✗${NC} git — not found (install from https://git-scm.com)"
    missing=1
else
    echo -e "  ${GREEN}✓${NC} git"
fi

if ! command -v python3 &> /dev/null; then
    echo -e "  ${RED}✗${NC} python3 — not found (install from https://python.org)"
    missing=1
else
    echo -e "  ${GREEN}✓${NC} python3"
fi

if ! command -v claude &> /dev/null; then
    echo -e "  ${YELLOW}!${NC} claude — not found (install Claude Code CLI to use slash commands)"
else
    echo -e "  ${GREEN}✓${NC} claude"
fi

if [ "$missing" -eq 1 ]; then
    echo ""
    echo -e "${RED}Missing required tools. Install them and re-run.${NC}"
    exit 1
fi

# ── Clone repository ─────────────────────────

echo ""
echo -e "${BOLD}Cloning ${REPO}...${NC}"
git clone --depth 1 "https://github.com/${REPO}.git" "$TEMP_DIR/google-ads-copy-claude"

# ── Install skills ───────────────────────────

echo ""
echo -e "${BOLD}Installing skills to ${SKILL_DIR}/${NC}"
mkdir -p "$SKILL_DIR"

# Copy root SKILL.md
cp "$TEMP_DIR/google-ads-copy-claude/SKILL.md" "$SKILL_DIR/SKILL.md"

# Copy skill.json
cp "$TEMP_DIR/google-ads-copy-claude/skill.json" "$SKILL_DIR/skill.json"

# Copy sub-skills
if [ -d "$TEMP_DIR/google-ads-copy-claude/skills" ]; then
    cp -r "$TEMP_DIR/google-ads-copy-claude/skills" "$SKILL_DIR/skills"
    echo -e "  ${GREEN}✓${NC} Sub-skills installed"
fi

# Copy templates
if [ -d "$TEMP_DIR/google-ads-copy-claude/templates" ]; then
    cp -r "$TEMP_DIR/google-ads-copy-claude/templates" "$SKILL_DIR/templates"
    echo -e "  ${GREEN}✓${NC} Templates installed"
fi

# Copy docs
if [ -d "$TEMP_DIR/google-ads-copy-claude/docs" ]; then
    cp -r "$TEMP_DIR/google-ads-copy-claude/docs" "$SKILL_DIR/docs"
    echo -e "  ${GREEN}✓${NC} Docs installed"
fi

# Copy scripts
if [ -d "$TEMP_DIR/google-ads-copy-claude/scripts" ]; then
    cp -r "$TEMP_DIR/google-ads-copy-claude/scripts" "$SKILL_DIR/scripts"
    echo -e "  ${GREEN}✓${NC} Scripts installed"
fi

# ── Install agents ───────────────────────────

echo ""
echo -e "${BOLD}Installing agents to ${AGENT_DIR}/${NC}"
mkdir -p "$AGENT_DIR"

if [ -d "$TEMP_DIR/google-ads-copy-claude/agents" ]; then
    for agent_file in "$TEMP_DIR/google-ads-copy-claude/agents"/*.md; do
        [ -f "$agent_file" ] || continue
        cp "$agent_file" "$AGENT_DIR/"
        echo -e "  ${GREEN}✓${NC} $(basename "$agent_file")"
    done
fi

# ── Install Python dependencies ──────────────

if [ -f "$TEMP_DIR/google-ads-copy-claude/requirements.txt" ]; then
    echo ""
    echo -e "${BOLD}Installing Python dependencies...${NC}"
    python3 -m pip install -r "$TEMP_DIR/google-ads-copy-claude/requirements.txt" --quiet
    echo -e "  ${GREEN}✓${NC} Python dependencies installed"
fi

# ── Cleanup ──────────────────────────────────

rm -rf "$TEMP_DIR"

# ── Done ─────────────────────────────────────

echo ""
echo -e "${GREEN}${BOLD}Installation complete!${NC}"
echo ""
echo -e "${BOLD}Available commands:${NC}"
echo -e "  ${CYAN}/copy generate${NC}     Generate a full RSA (15 headlines + 4 descriptions)"
echo -e "  ${CYAN}/copy headlines${NC}    50+ headline variations using proven formulas"
echo -e "  ${CYAN}/copy descriptions${NC} Conversion-optimized descriptions"
echo -e "  ${CYAN}/copy dki${NC}          Dynamic Keyword Insertion setup"
echo -e "  ${CYAN}/copy strength${NC}     Ad Strength audit and optimization"
echo -e "  ${CYAN}/copy competitor${NC}   Competitor ad copy analysis"
echo -e "  ${CYAN}/copy emotional${NC}    Emotional trigger scoring"
echo -e "  ${CYAN}/copy cta${NC}          CTA optimization by industry"
echo -e "  ${CYAN}/copy test${NC}         A/B test variation generator"
echo -e "  ${CYAN}/copy report${NC}       Full ad copy audit report"
echo ""
