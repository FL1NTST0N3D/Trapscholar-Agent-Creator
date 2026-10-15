#!/usr/bin/env bash
set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# ASCII Header
echo -e "${CYAN}"
cat << 'HEADER'

   ____    _    _  _      _             _ _ _
  / ___|  / \  | || |    / \  _   _  __| (_) |_
 | |  _  / _ \ | || |_  / _ \| | | |/ _` | | __|
 | |_| |/ ___ \|__   _|/ ___ \ |_| | (_| | | |_
  \____/_/   \_\  |_| /_/   \_\__,_|\__,_|_|\__|

  Claude Code Skill Installer

HEADER
echo -e "${NC}"

# ── Config ──────────────────────────────────────────────
SKILL_NAME="ga4-audit"
CLAUDE_DIR="$HOME/.claude"
SKILLS_DIR="$CLAUDE_DIR/skills"
AGENTS_DIR="$CLAUDE_DIR/agents"
INSTALL_DIR="$SKILLS_DIR/$SKILL_NAME"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ── Prereq Checks ──────────────────────────────────────
echo -e "${BOLD}Checking prerequisites...${NC}"

# Check for Claude Code CLI
if command -v claude &> /dev/null; then
    echo -e "  ${GREEN}[ok]${NC} Claude Code CLI found"
else
    echo -e "  ${YELLOW}[warn]${NC} Claude Code CLI not found in PATH"
    echo -e "        Install from: https://github.com/anthropics/claude-code"
fi

# Check for Python 3.8+
if command -v python3 &> /dev/null; then
    PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    PY_MAJOR=$(echo "$PY_VERSION" | cut -d. -f1)
    PY_MINOR=$(echo "$PY_VERSION" | cut -d. -f2)
    if [ "$PY_MAJOR" -ge 3 ] && [ "$PY_MINOR" -ge 8 ]; then
        echo -e "  ${GREEN}[ok]${NC} Python $PY_VERSION found"
    else
        echo -e "  ${YELLOW}[warn]${NC} Python $PY_VERSION found (3.8+ recommended)"
    fi
else
    echo -e "  ${YELLOW}[warn]${NC} Python 3 not found (needed for scoring scripts)"
fi

echo ""

# ── Create Directories ─────────────────────────────────
echo -e "${BOLD}Installing GA4 Audit skill...${NC}"

mkdir -p "$INSTALL_DIR"
mkdir -p "$AGENTS_DIR"

# ── Copy Skills ─────────────────────────────────────────
echo -e "  ${BLUE}>>>${NC} Copying skill files to $INSTALL_DIR/"

# Copy main SKILL.md
cp "$SCRIPT_DIR/SKILL.md" "$INSTALL_DIR/SKILL.md"
echo -e "  ${GREEN}[ok]${NC} Main SKILL.md"

# Copy sub-skills
if [ -d "$SCRIPT_DIR/skills" ]; then
    cp -r "$SCRIPT_DIR/skills/"* "$INSTALL_DIR/"
    echo -e "  ${GREEN}[ok]${NC} Sub-skills (10 audit dimensions)"
fi

# Copy scripts
if [ -d "$SCRIPT_DIR/scripts" ]; then
    mkdir -p "$INSTALL_DIR/scripts"
    cp -r "$SCRIPT_DIR/scripts/"* "$INSTALL_DIR/scripts/"
    echo -e "  ${GREEN}[ok]${NC} Python scripts"
fi

# Copy docs
if [ -d "$SCRIPT_DIR/docs" ]; then
    mkdir -p "$INSTALL_DIR/docs"
    cp -r "$SCRIPT_DIR/docs/"* "$INSTALL_DIR/docs/"
    echo -e "  ${GREEN}[ok]${NC} Documentation"
fi

# ── Copy Agents ─────────────────────────────────────────
echo -e "  ${BLUE}>>>${NC} Copying agent files to $AGENTS_DIR/"

if [ -d "$SCRIPT_DIR/agents" ]; then
    cp "$SCRIPT_DIR/agents/"* "$AGENTS_DIR/"
    echo -e "  ${GREEN}[ok]${NC} Agent definitions (4 agents)"
fi

# ── Install Python Dependencies ─────────────────────────
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    echo -e "  ${BLUE}>>>${NC} Installing Python dependencies..."
    if command -v pip3 &> /dev/null; then
        pip3 install -r "$SCRIPT_DIR/requirements.txt" --quiet
        echo -e "  ${GREEN}[ok]${NC} Python dependencies installed"
    else
        echo -e "  ${YELLOW}[warn]${NC} pip3 not found — install requirements.txt manually"
    fi
else
    echo -e "  ${GREEN}[ok]${NC} No external Python dependencies required"
fi

echo ""

# ── Done ────────────────────────────────────────────────
echo -e "${GREEN}${BOLD}Installation complete!${NC}"
echo ""
echo -e "${BOLD}Available commands:${NC}"
echo -e "  ${CYAN}/ga4 audit${NC}         Full property audit (all 10 dimensions)"
echo -e "  ${CYAN}/ga4 streams${NC}       Audit data stream configuration"
echo -e "  ${CYAN}/ga4 events${NC}        Audit event implementation"
echo -e "  ${CYAN}/ga4 conversions${NC}   Audit conversion setup"
echo -e "  ${CYAN}/ga4 audiences${NC}     Audit audience configuration"
echo -e "  ${CYAN}/ga4 attribution${NC}   Audit attribution settings"
echo -e "  ${CYAN}/ga4 ecommerce${NC}     Audit e-commerce tracking"
echo -e "  ${CYAN}/ga4 dimensions${NC}    Audit custom dimensions"
echo -e "  ${CYAN}/ga4 reporting${NC}     Audit report configuration"
echo -e "  ${CYAN}/ga4 integrations${NC}  Audit Google product links"
echo -e "  ${CYAN}/ga4 report${NC}        Generate final audit report"
echo ""
echo -e "${BOLD}Installed to:${NC}"
echo -e "  Skills: $INSTALL_DIR/"
echo -e "  Agents: $AGENTS_DIR/"
echo ""
