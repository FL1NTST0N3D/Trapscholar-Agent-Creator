#!/usr/bin/env bash
set -euo pipefail

# ============================================================
#   Quality Score Claude — Installer
# ============================================================

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

REPO_URL="https://github.com/0-shiv/quality-score-claude.git"
SKILL_DIR="$HOME/.claude/skills/quality-score-claude"
AGENT_DIR="$HOME/.claude/agents"
TEMP_DIR=$(mktemp -d)

cleanup() {
    rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

echo ""
echo -e "${CYAN}${BOLD}"
echo "  ╔═══════════════════════════════════════════╗"
echo "  ║       Quality Score Claude Installer       ║"
echo "  ║                                           ║"
echo "  ║   Your Quality Score is costing you money  ║"
echo "  ║   This skill shows you exactly how much    ║"
echo "  ╚═══════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# ── Prerequisite checks ──────────────────────────────────────

echo -e "${BOLD}Checking prerequisites...${NC}"

MISSING=0

if ! command -v git &> /dev/null; then
    echo -e "  ${RED}[X] git not found${NC}"
    MISSING=1
else
    echo -e "  ${GREEN}[OK]${NC} git $(git --version | cut -d' ' -f3)"
fi

if ! command -v python3 &> /dev/null; then
    echo -e "  ${RED}[X] python3 not found (requires 3.9+)${NC}"
    MISSING=1
else
    PY_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "  ${GREEN}[OK]${NC} python3 $PY_VERSION"
fi

if ! command -v claude &> /dev/null; then
    echo -e "  ${YELLOW}[!] claude CLI not found (optional but recommended)${NC}"
else
    echo -e "  ${GREEN}[OK]${NC} claude CLI found"
fi

if [ "$MISSING" -eq 1 ]; then
    echo ""
    echo -e "${RED}Missing required prerequisites. Install them and try again.${NC}"
    exit 1
fi

echo ""

# ── Clone to temp ────────────────────────────────────────────

echo -e "${BOLD}Downloading quality-score-claude...${NC}"
git clone --depth 1 "$REPO_URL" "$TEMP_DIR/quality-score-claude" 2>/dev/null || {
    echo -e "${RED}Failed to clone repository. Check your internet connection.${NC}"
    exit 1
}
echo -e "  ${GREEN}[OK]${NC} Repository cloned"
echo ""

# ── Install skills ───────────────────────────────────────────

echo -e "${BOLD}Installing skills...${NC}"
mkdir -p "$SKILL_DIR"
mkdir -p "$AGENT_DIR"

# Copy main skill files
cp "$TEMP_DIR/quality-score-claude/SKILL.md" "$SKILL_DIR/"
echo -e "  ${GREEN}[OK]${NC} Main SKILL.md"

# Copy sub-skills
if [ -d "$TEMP_DIR/quality-score-claude/skills" ]; then
    cp -r "$TEMP_DIR/quality-score-claude/skills" "$SKILL_DIR/"
    SKILL_COUNT=$(find "$SKILL_DIR/skills" -name "SKILL.md" | wc -l | tr -d ' ')
    echo -e "  ${GREEN}[OK]${NC} $SKILL_COUNT sub-skills installed"
fi

# Copy agents
if [ -d "$TEMP_DIR/quality-score-claude/agents" ]; then
    for agent_file in "$TEMP_DIR/quality-score-claude/agents"/*.md; do
        if [ -f "$agent_file" ]; then
            cp "$agent_file" "$AGENT_DIR/"
        fi
    done
    AGENT_COUNT=$(ls -1 "$TEMP_DIR/quality-score-claude/agents"/*.md 2>/dev/null | wc -l | tr -d ' ')
    echo -e "  ${GREEN}[OK]${NC} $AGENT_COUNT agents installed"
fi

# Copy scripts
if [ -d "$TEMP_DIR/quality-score-claude/scripts" ]; then
    cp -r "$TEMP_DIR/quality-score-claude/scripts" "$SKILL_DIR/"
    echo -e "  ${GREEN}[OK]${NC} Python scripts installed"
fi

# Copy templates
if [ -d "$TEMP_DIR/quality-score-claude/templates" ]; then
    cp -r "$TEMP_DIR/quality-score-claude/templates" "$SKILL_DIR/"
    echo -e "  ${GREEN}[OK]${NC} Templates installed"
fi

# Copy docs
if [ -d "$TEMP_DIR/quality-score-claude/docs" ]; then
    cp -r "$TEMP_DIR/quality-score-claude/docs" "$SKILL_DIR/"
    echo -e "  ${GREEN}[OK]${NC} Documentation installed"
fi

echo ""

# ── Install Python dependencies ──────────────────────────────

if [ -f "$TEMP_DIR/quality-score-claude/requirements.txt" ]; then
    echo -e "${BOLD}Installing Python dependencies...${NC}"
    pip3 install -r "$TEMP_DIR/quality-score-claude/requirements.txt" --quiet 2>/dev/null && \
        echo -e "  ${GREEN}[OK]${NC} Python dependencies installed" || \
        echo -e "  ${YELLOW}[!] Some dependencies failed to install. Scripts may not work.${NC}"
    echo ""
fi

# ── Done ─────────────────────────────────────────────────────

echo -e "${GREEN}${BOLD}Installation complete!${NC}"
echo ""
echo -e "${BOLD}Installed to:${NC}"
echo -e "  Skills:  $SKILL_DIR"
echo -e "  Agents:  $AGENT_DIR"
echo ""
echo -e "${BOLD}Available commands:${NC}"
echo -e "  ${CYAN}/qs analyze${NC}        Full QS analysis across your account"
echo -e "  ${CYAN}/qs components${NC}     Break down QS into 3 components per keyword"
echo -e "  ${CYAN}/qs impact${NC}         Calculate CPC waste from low Quality Scores"
echo -e "  ${CYAN}/qs trends${NC}         Track QS changes over time"
echo -e "  ${CYAN}/qs distribution${NC}   Histogram of QS across all keywords"
echo -e "  ${CYAN}/qs keywords${NC}       Per-keyword audit sorted by savings potential"
echo -e "  ${CYAN}/qs landing-pages${NC}  Landing Page Experience analysis"
echo -e "  ${CYAN}/qs relevance${NC}      Ad Relevance deep dive"
echo -e "  ${CYAN}/qs ctr${NC}            Expected CTR analysis and benchmarks"
echo -e "  ${CYAN}/qs optimize${NC}       Actionable optimization playbook"
echo -e "  ${CYAN}/qs report${NC}         Full QS audit report with estimated savings"
echo ""
