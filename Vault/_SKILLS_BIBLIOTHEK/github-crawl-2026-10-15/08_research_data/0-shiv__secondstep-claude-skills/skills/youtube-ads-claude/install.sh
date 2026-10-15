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
echo -e "${CYAN}║${NC}        ${GREEN}YouTube Ads Claude${NC} — Installer            ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}        YouTube Campaign Optimization Skill        ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}        for Claude Code                            ${CYAN}║${NC}"
echo -e "${CYAN}║                                                  ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════╝${NC}"
echo ""

# Check prerequisites
echo -e "${BLUE}Checking prerequisites...${NC}"

if ! command -v git &> /dev/null; then
    echo -e "${RED}✗ Git is not installed${NC}"
    echo "  Install: https://git-scm.com/downloads"
    exit 1
fi
echo -e "${GREEN}✓ Git found${NC}"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 is not installed${NC}"
    echo "  Install: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"

if ! command -v claude &> /dev/null; then
    echo -e "${YELLOW}⚠ Claude Code CLI not found (optional but recommended)${NC}"
else
    echo -e "${GREEN}✓ Claude Code CLI found${NC}"
fi

echo ""
echo -e "${BLUE}Installing YouTube Ads Claude...${NC}"

# Create directories
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"
mkdir -p "$SKILLS_DIR" "$AGENTS_DIR"

# Determine source directory
if [ ! -t 0 ]; then
    # Piped installation (curl | bash)
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT
    git clone --depth 1 https://github.com/0-shiv/youtube-ads-claude.git "$TEMP_DIR/youtube-ads-claude" 2>/dev/null
    REPO_DIR="$TEMP_DIR/youtube-ads-claude"
else
    # Running from cloned repo
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    REPO_DIR="$SCRIPT_DIR"
fi

# Copy main skill
echo -e "${BLUE}  Installing main skill...${NC}"
mkdir -p "$SKILLS_DIR/youtube-ads"
cp "$REPO_DIR/SKILL.md" "$SKILLS_DIR/youtube-ads/SKILL.md"

# Copy sub-skills
echo -e "${BLUE}  Installing sub-skills...${NC}"
for skill_dir in "$REPO_DIR/skills/"*/; do
    skill_name=$(basename "$skill_dir")
    cp -r "$skill_dir" "$SKILLS_DIR/$skill_name"
done

# Copy agents
echo -e "${BLUE}  Installing agents...${NC}"
for agent_file in "$REPO_DIR/agents/"*.md; do
    cp "$agent_file" "$AGENTS_DIR/"
done

# Copy scripts
echo -e "${BLUE}  Installing scripts...${NC}"
SCRIPTS_DIR="$SKILLS_DIR/youtube-ads/scripts"
mkdir -p "$SCRIPTS_DIR"
cp "$REPO_DIR/scripts/"*.py "$SCRIPTS_DIR/" 2>/dev/null || true

# Copy docs
echo -e "${BLUE}  Installing documentation...${NC}"
DOCS_DIR="$SKILLS_DIR/youtube-ads/docs"
mkdir -p "$DOCS_DIR"
cp "$REPO_DIR/docs/"*.md "$DOCS_DIR/" 2>/dev/null || true

# Install Python dependencies
if [ -f "$REPO_DIR/requirements.txt" ]; then
    echo -e "${BLUE}  Installing Python dependencies...${NC}"
    if python3 -m venv "$SKILLS_DIR/youtube-ads/.venv" 2>/dev/null; then
        source "$SKILLS_DIR/youtube-ads/.venv/bin/activate"
        pip install -q -r "$REPO_DIR/requirements.txt" 2>/dev/null || true
        deactivate
    else
        pip3 install --user -q -r "$REPO_DIR/requirements.txt" 2>/dev/null || true
    fi
fi

# Verify installation
echo ""
echo -e "${BLUE}Verifying installation...${NC}"

INSTALLED=0
TOTAL=0

for check in "$SKILLS_DIR/youtube-ads/SKILL.md" \
             "$SKILLS_DIR/yt-campaign-audit/SKILL.md" \
             "$SKILLS_DIR/yt-creative-scoring/SKILL.md" \
             "$SKILLS_DIR/yt-targeting-strategy/SKILL.md" \
             "$SKILLS_DIR/yt-shorts-ads/SKILL.md" \
             "$SKILLS_DIR/yt-bumper-ads/SKILL.md" \
             "$SKILLS_DIR/yt-bidding/SKILL.md" \
             "$SKILLS_DIR/yt-placements/SKILL.md" \
             "$SKILLS_DIR/yt-remarketing/SKILL.md" \
             "$SKILLS_DIR/yt-report/SKILL.md" \
             "$AGENTS_DIR/campaign-auditor.md" \
             "$AGENTS_DIR/creative-analyst.md" \
             "$AGENTS_DIR/targeting-optimizer.md" \
             "$AGENTS_DIR/report-generator.md"; do
    TOTAL=$((TOTAL + 1))
    if [ -f "$check" ]; then
        INSTALLED=$((INSTALLED + 1))
    fi
done

if [ "$INSTALLED" -eq "$TOTAL" ]; then
    echo -e "${GREEN}✓ All $TOTAL components installed successfully${NC}"
else
    echo -e "${YELLOW}⚠ $INSTALLED/$TOTAL components installed${NC}"
fi

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Installation complete!                          ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}Available commands:${NC}"
echo ""
echo "  /yt audit              Full YouTube campaign audit"
echo "  /yt creative           Video ad creative scoring (ABCD)"
echo "  /yt targeting          Targeting strategy analysis"
echo "  /yt shorts             Shorts ad readiness assessment"
echo "  /yt bumper             6-second bumper ad strategy"
echo "  /yt bidding            Bidding strategy analysis"
echo "  /yt placements         Placement hygiene & brand safety"
echo "  /yt remarketing        Remarketing funnel analysis"
echo "  /yt report             Generate full audit report"
echo ""
echo -e "${BLUE}Get started:${NC} Open Claude Code and type ${GREEN}/yt audit${NC}"
echo ""
