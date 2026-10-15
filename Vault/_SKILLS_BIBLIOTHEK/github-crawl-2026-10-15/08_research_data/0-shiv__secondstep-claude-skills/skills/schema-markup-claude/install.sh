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
echo -e "${CYAN}║${NC}   ${GREEN}Schema Markup Claude${NC} — Installer              ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}   JSON-LD Structured Data for Claude Code        ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}   20+ Schema Types | Google Rich Results          ${CYAN}║${NC}"
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
    echo -e "${YELLOW}⚠ Python 3 not found (optional, needed for scripts)${NC}"
else
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"
fi

if ! command -v claude &> /dev/null; then
    echo -e "${YELLOW}⚠ Claude Code CLI not found (optional but recommended)${NC}"
else
    echo -e "${GREEN}✓ Claude Code CLI found${NC}"
fi

echo ""
echo -e "${BLUE}Installing Schema Markup Claude...${NC}"

# Create directories
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"
mkdir -p "$SKILLS_DIR" "$AGENTS_DIR"

# Determine source directory
if [ ! -t 0 ]; then
    # Piped installation (curl | bash)
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT
    git clone --depth 1 https://github.com/0-shiv/schema-markup-claude.git "$TEMP_DIR/schema-markup-claude" 2>/dev/null
    REPO_DIR="$TEMP_DIR/schema-markup-claude"
else
    # Running from cloned repo
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    REPO_DIR="$SCRIPT_DIR"
fi

# Copy main skill
echo -e "${BLUE}  Installing main skill...${NC}"
mkdir -p "$SKILLS_DIR/schema-markup"
cp "$REPO_DIR/SKILL.md" "$SKILLS_DIR/schema-markup/SKILL.md"

# Copy sub-skills
echo -e "${BLUE}  Installing sub-skills (11 schema types)...${NC}"
for skill_dir in "$REPO_DIR/skills/"*/; do
    skill_name=$(basename "$skill_dir")
    mkdir -p "$SKILLS_DIR/$skill_name"
    cp -r "$skill_dir"* "$SKILLS_DIR/$skill_name/" 2>/dev/null || true
done

# Copy agents
echo -e "${BLUE}  Installing agents...${NC}"
if ls "$REPO_DIR/agents/"*.md 1>/dev/null 2>&1; then
    for agent_file in "$REPO_DIR/agents/"*.md; do
        cp "$agent_file" "$AGENTS_DIR/"
    done
else
    echo -e "${YELLOW}  ⚠ No agent files found (agents/ may be empty)${NC}"
fi

# Copy templates
echo -e "${BLUE}  Installing templates...${NC}"
TEMPLATES_DIR="$SKILLS_DIR/schema-markup/templates"
mkdir -p "$TEMPLATES_DIR"
cp "$REPO_DIR/templates/"*.json "$TEMPLATES_DIR/" 2>/dev/null || true

# Copy scripts
echo -e "${BLUE}  Installing scripts...${NC}"
SCRIPTS_DIR="$SKILLS_DIR/schema-markup/scripts"
mkdir -p "$SCRIPTS_DIR"
cp "$REPO_DIR/scripts/"*.py "$SCRIPTS_DIR/" 2>/dev/null || true

# Install Python dependencies if requirements.txt exists
if [ -f "$REPO_DIR/requirements.txt" ] && command -v python3 &> /dev/null; then
    echo -e "${BLUE}  Installing Python dependencies...${NC}"
    if python3 -m venv "$SKILLS_DIR/schema-markup/.venv" 2>/dev/null; then
        source "$SKILLS_DIR/schema-markup/.venv/bin/activate"
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

for check in "$SKILLS_DIR/schema-markup/SKILL.md" \
             "$SKILLS_DIR/schema-organization/SKILL.md" \
             "$SKILLS_DIR/schema-local-business/SKILL.md" \
             "$SKILLS_DIR/schema-product/SKILL.md" \
             "$SKILLS_DIR/schema-faq/SKILL.md" \
             "$SKILLS_DIR/schema-howto/SKILL.md" \
             "$SKILLS_DIR/schema-article/SKILL.md" \
             "$SKILLS_DIR/schema-video/SKILL.md" \
             "$SKILLS_DIR/schema-breadcrumb/SKILL.md" \
             "$SKILLS_DIR/schema-event/SKILL.md" \
             "$SKILLS_DIR/schema-validator/SKILL.md" \
             "$SKILLS_DIR/schema-report/SKILL.md"; do
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
echo "  /schema generate <type>    Generate any supported schema type"
echo "  /schema organization       Organization schema with social profiles"
echo "  /schema local-business     LocalBusiness with NAP, hours, geo"
echo "  /schema product            Product + Offer for e-commerce"
echo "  /schema faq                FAQPage with Q&A pairs"
echo "  /schema howto              HowTo with steps, tools, supplies"
echo "  /schema article            Article/BlogPosting/NewsArticle"
echo "  /schema video              VideoObject + BroadcastEvent"
echo "  /schema breadcrumb         BreadcrumbList navigation paths"
echo "  /schema event              Event with location, offers"
echo "  /schema validate           Validate existing schema markup"
echo "  /schema report             Schema coverage report for a site"
echo ""
echo -e "${BLUE}Get started:${NC} Open Claude Code and type ${GREEN}/schema generate organization${NC}"
echo ""
