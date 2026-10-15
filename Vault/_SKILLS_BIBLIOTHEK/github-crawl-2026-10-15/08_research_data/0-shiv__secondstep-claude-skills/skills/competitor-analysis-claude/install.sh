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
echo -e "${CYAN}║${NC}        ${GREEN}Competitor Analysis Claude${NC}               ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}        Competitive Intelligence Skill             ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}        for Claude Code                           ${CYAN}║${NC}"
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
echo -e "${BLUE}Installing Competitor Analysis Claude...${NC}"

# Create directories
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"
mkdir -p "$SKILLS_DIR" "$AGENTS_DIR"

# Clone to temp directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

if [ ! -t 0 ]; then
    # Piped installation (curl | bash)
    git clone --depth 1 https://github.com/0-shiv/competitor-analysis-claude.git "$TEMP_DIR/competitor-analysis-claude" 2>/dev/null
    REPO_DIR="$TEMP_DIR/competitor-analysis-claude"
else
    # Running from cloned repo
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    REPO_DIR="$SCRIPT_DIR"
fi

# Copy main skill
echo -e "${BLUE}  Installing main skill...${NC}"
cp -r "$REPO_DIR/competitor" "$SKILLS_DIR/competitor"

# Copy sub-skills
echo -e "${BLUE}  Installing sub-skills...${NC}"
for skill_dir in "$REPO_DIR/skills/"*/; do
    skill_name=$(basename "$skill_dir")
    cp -r "$skill_dir" "$SKILLS_DIR/$skill_name"
done

# Copy agents
echo -e "${BLUE}  Installing agents...${NC}"
for agent_file in "$REPO_DIR/agents/"*.md; do
    [ -f "$agent_file" ] && cp "$agent_file" "$AGENTS_DIR/"
done

# Copy scripts
echo -e "${BLUE}  Installing scripts...${NC}"
SCRIPTS_DIR="$SKILLS_DIR/competitor/scripts"
mkdir -p "$SCRIPTS_DIR"
cp "$REPO_DIR/scripts/"*.py "$SCRIPTS_DIR/" 2>/dev/null || true

# Install Python dependencies
echo -e "${BLUE}  Installing Python dependencies...${NC}"
if python3 -m venv "$SKILLS_DIR/competitor/.venv" 2>/dev/null; then
    source "$SKILLS_DIR/competitor/.venv/bin/activate"
    pip install -q -r "$REPO_DIR/requirements.txt" 2>/dev/null || true
    deactivate
else
    pip3 install --user -q -r "$REPO_DIR/requirements.txt" 2>/dev/null || true
fi

# Verify installation
echo ""
echo -e "${BLUE}Verifying installation...${NC}"

INSTALLED=0
TOTAL=0

for check in "$SKILLS_DIR/competitor/CLAUDE.md" \
             "$SKILLS_DIR/comp-teardown/CLAUDE.md" \
             "$SKILLS_DIR/comp-positioning/CLAUDE.md" \
             "$SKILLS_DIR/comp-swot/CLAUDE.md" \
             "$SKILLS_DIR/comp-pricing/CLAUDE.md" \
             "$SKILLS_DIR/comp-ads-intel/CLAUDE.md" \
             "$SKILLS_DIR/comp-content-gap/CLAUDE.md" \
             "$SKILLS_DIR/comp-tech-stack/CLAUDE.md" \
             "$SKILLS_DIR/comp-battlecard/CLAUDE.md" \
             "$SKILLS_DIR/comp-report/CLAUDE.md" \
             "$AGENTS_DIR/ci-researcher.md" \
             "$AGENTS_DIR/ci-analyst.md" \
             "$AGENTS_DIR/ci-strategist.md"; do
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
echo "  /comp teardown           Full competitor teardown"
echo "  /comp positioning        Perceptual mapping & positioning matrix"
echo "  /comp swot               SWOT analysis with action items"
echo "  /comp pricing            Pricing comparison & packaging"
echo "  /comp ads                Ad intelligence & spend estimation"
echo "  /comp content            Content gap analysis"
echo "  /comp tech               Technology stack detection"
echo "  /comp battlecard         Sales battlecard generator"
echo "  /comp report             Full competitive intelligence report"
echo ""
echo -e "${BLUE}Get started:${NC} Open Claude Code and type ${GREEN}/comp teardown${NC}"
echo ""
