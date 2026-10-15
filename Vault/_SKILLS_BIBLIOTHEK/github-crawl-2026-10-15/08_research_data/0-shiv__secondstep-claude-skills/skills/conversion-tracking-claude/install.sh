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
echo -e "${CYAN}║${NC}   ${GREEN}Conversion Tracking Claude${NC} — Installer        ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}   Cross-Platform Tracking Audit Skill            ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}   for Claude Code                                ${CYAN}║${NC}"
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
echo -e "${BLUE}Installing Conversion Tracking Claude...${NC}"

# Create directories
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"
mkdir -p "$SKILLS_DIR" "$AGENTS_DIR"

# Clone to temp directory or use local repo
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

if [ ! -t 0 ]; then
    # Piped installation (curl | bash)
    git clone --depth 1 https://github.com/0-shiv/conversion-tracking-claude.git "$TEMP_DIR/conversion-tracking-claude" 2>/dev/null
    REPO_DIR="$TEMP_DIR/conversion-tracking-claude"
else
    # Running from cloned repo
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    REPO_DIR="$SCRIPT_DIR"
fi

# Copy main skill
echo -e "${BLUE}  Installing main skill...${NC}"
mkdir -p "$SKILLS_DIR/conversion-tracking"
cp "$REPO_DIR/SKILL.md" "$SKILLS_DIR/conversion-tracking/SKILL.md"

# Copy sub-skills
echo -e "${BLUE}  Installing sub-skills...${NC}"
for skill_dir in "$REPO_DIR/skills/"*/; do
    skill_name=$(basename "$skill_dir")
    mkdir -p "$SKILLS_DIR/$skill_name"
    cp -r "$skill_dir"* "$SKILLS_DIR/$skill_name/"
done

# Copy agents
echo -e "${BLUE}  Installing agents...${NC}"
for agent_file in "$REPO_DIR/agents/"*.md; do
    [ -f "$agent_file" ] && cp "$agent_file" "$AGENTS_DIR/"
done

# Copy scripts
echo -e "${BLUE}  Installing scripts...${NC}"
SCRIPTS_DIR="$SKILLS_DIR/conversion-tracking/scripts"
mkdir -p "$SCRIPTS_DIR"
cp "$REPO_DIR/scripts/"*.py "$SCRIPTS_DIR/" 2>/dev/null || true

# Copy templates
echo -e "${BLUE}  Installing templates...${NC}"
TEMPLATES_DIR="$SKILLS_DIR/conversion-tracking/templates"
mkdir -p "$TEMPLATES_DIR"
cp "$REPO_DIR/templates/"* "$TEMPLATES_DIR/" 2>/dev/null || true

# Install Python dependencies
if [ -f "$REPO_DIR/requirements.txt" ]; then
    echo -e "${BLUE}  Installing Python dependencies...${NC}"
    if python3 -m venv "$SKILLS_DIR/conversion-tracking/.venv" 2>/dev/null; then
        source "$SKILLS_DIR/conversion-tracking/.venv/bin/activate"
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

for check in "$SKILLS_DIR/conversion-tracking/SKILL.md" \
             "$SKILLS_DIR/track-google-tag/SKILL.md" \
             "$SKILLS_DIR/track-enhanced-conversions/SKILL.md" \
             "$SKILLS_DIR/track-server-side/SKILL.md" \
             "$SKILLS_DIR/track-offline-import/SKILL.md" \
             "$SKILLS_DIR/track-meta-pixel/SKILL.md" \
             "$SKILLS_DIR/track-meta-capi/SKILL.md" \
             "$SKILLS_DIR/track-linkedin-insight/SKILL.md" \
             "$SKILLS_DIR/track-tiktok-pixel/SKILL.md" \
             "$SKILLS_DIR/track-attribution/SKILL.md" \
             "$SKILLS_DIR/track-report/SKILL.md" \
             "$AGENTS_DIR/audit_orchestrator.md" \
             "$AGENTS_DIR/tag_inspector.md" \
             "$AGENTS_DIR/data_quality_agent.md" \
             "$AGENTS_DIR/report_generator.md"; do
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
echo "  /track audit          Full cross-platform tracking audit"
echo "  /track google-tag     Validate Google Tag (gtag.js)"
echo "  /track ec             Audit Enhanced Conversions"
echo "  /track server-side    Validate server-side GTM"
echo "  /track offline        Check offline conversion import"
echo "  /track meta-pixel     Audit Meta Pixel"
echo "  /track capi           Validate Meta Conversions API"
echo "  /track linkedin       Check LinkedIn Insight Tag"
echo "  /track tiktok         Audit TikTok Pixel"
echo "  /track attribution    Analyze attribution models"
echo "  /track report         Generate audit report"
echo ""
echo -e "${BLUE}Get started:${NC} Open Claude Code and type ${GREEN}/track audit${NC}"
echo ""
