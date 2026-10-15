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
echo -e "${CYAN}║${NC}        ${GREEN}LinkedIn Ads Claude${NC} — Installer           ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}        B2B Ads Audit Skill for Claude Code       ${CYAN}║${NC}"
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
echo -e "${BLUE}Installing LinkedIn Ads Claude...${NC}"

# Create directories
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"
mkdir -p "$SKILLS_DIR" "$AGENTS_DIR"

# Determine source directory
if [ ! -t 0 ]; then
    # Piped installation (curl | bash)
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT
    git clone --depth 1 https://github.com/0-shiv/linkedin-ads-claude.git "$TEMP_DIR/linkedin-ads-claude" 2>/dev/null
    REPO_DIR="$TEMP_DIR/linkedin-ads-claude"
else
    # Running from cloned repo
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    REPO_DIR="$SCRIPT_DIR"
fi

# Copy main skill
echo -e "${BLUE}  Installing main skill...${NC}"
mkdir -p "$SKILLS_DIR/linkedin"
cp "$REPO_DIR/SKILL.md" "$SKILLS_DIR/linkedin/SKILL.md"

# Copy sub-skills
echo -e "${BLUE}  Installing sub-skills...${NC}"
for skill_dir in "$REPO_DIR/skills/"*/; do
    skill_name=$(basename "$skill_dir")
    mkdir -p "$SKILLS_DIR/$skill_name"
    cp -r "$skill_dir"* "$SKILLS_DIR/$skill_name/" 2>/dev/null || true
done

# Copy agents
echo -e "${BLUE}  Installing agents...${NC}"
for agent_file in "$REPO_DIR/agents/"*.md; do
    [ -f "$agent_file" ] && cp "$agent_file" "$AGENTS_DIR/"
done

# Copy scripts
echo -e "${BLUE}  Installing scripts...${NC}"
SCRIPTS_DIR="$SKILLS_DIR/linkedin/scripts"
mkdir -p "$SCRIPTS_DIR"
cp "$REPO_DIR/scripts/"*.py "$SCRIPTS_DIR/" 2>/dev/null || true

# Copy docs
echo -e "${BLUE}  Installing docs...${NC}"
DOCS_DIR="$SKILLS_DIR/linkedin/docs"
mkdir -p "$DOCS_DIR"
cp "$REPO_DIR/docs/"*.md "$DOCS_DIR/" 2>/dev/null || true

# Verify installation
echo ""
echo -e "${BLUE}Verifying installation...${NC}"

INSTALLED=0
TOTAL=0

for check in "$SKILLS_DIR/linkedin/SKILL.md" \
             "$SKILLS_DIR/li-campaign-structure/SKILL.md" \
             "$SKILLS_DIR/li-targeting/SKILL.md" \
             "$SKILLS_DIR/li-lead-gen-forms/SKILL.md" \
             "$SKILLS_DIR/li-content-formats/SKILL.md" \
             "$SKILLS_DIR/li-budget-cpl/SKILL.md" \
             "$SKILLS_DIR/li-audience-building/SKILL.md" \
             "$SKILLS_DIR/li-conversion-tracking/SKILL.md" \
             "$SKILLS_DIR/li-report/SKILL.md" \
             "$AGENTS_DIR/linkedin-auditor.md" \
             "$AGENTS_DIR/linkedin-strategist.md" \
             "$AGENTS_DIR/linkedin-reporter.md"; do
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
echo "  /li audit              Full 25-point LinkedIn Ads audit"
echo "  /li targeting          Targeting layer analysis & ABM review"
echo "  /li lead-gen           Lead Gen Form optimization audit"
echo "  /li formats            Content format mix & performance review"
echo "  /li budget             Budget allocation & CPL benchmarks"
echo "  /li audiences          Matched Audiences & retargeting audit"
echo "  /li tracking           Conversion tracking & attribution review"
echo "  /li report             Generate full audit report with scores"
echo ""
echo -e "${BLUE}Get started:${NC} Open Claude Code and type ${GREEN}/li audit${NC}"
echo ""
