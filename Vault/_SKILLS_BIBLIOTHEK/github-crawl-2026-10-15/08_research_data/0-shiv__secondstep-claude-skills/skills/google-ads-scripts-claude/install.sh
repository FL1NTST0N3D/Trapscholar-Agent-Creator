#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Google Ads Scripts Claude — Installer
# ============================================================

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# ASCII Header
echo ""
echo -e "${CYAN}${BOLD}"
cat << 'HEADER'
  ╔══════════════════════════════════════════════════╗
  ║    Google Ads Scripts Claude                     ║
  ║    50+ Scripts for Claude Code                   ║
  ║    github.com/0-shiv/google-ads-scripts-claude   ║
  ╚══════════════════════════════════════════════════╝
HEADER
echo -e "${NC}"

# Paths
REPO_URL="https://github.com/0-shiv/google-ads-scripts-claude.git"
INSTALL_DIR="${HOME}/.claude/skills/google-ads-scripts-claude"
AGENTS_DIR="${HOME}/.claude/agents"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ------------------------------------------------------------
# Prerequisite checks
# ------------------------------------------------------------
echo -e "${BOLD}Checking prerequisites...${NC}"

# Check for git
if ! command -v git &> /dev/null; then
    echo -e "${RED}Error: git is not installed.${NC}"
    echo "Install git: https://git-scm.com/downloads"
    exit 1
fi
echo -e "  ${GREEN}git${NC} found"

# Check for Claude Code CLI
if ! command -v claude &> /dev/null; then
    echo -e "${YELLOW}Warning: claude CLI not found in PATH.${NC}"
    echo "  Install Claude Code: https://docs.anthropic.com/en/docs/claude-code"
    echo "  Continuing anyway — skills will be installed but commands won't work without Claude Code."
else
    echo -e "  ${GREEN}claude${NC} found"
fi

# Check for Python 3 (optional, for validation scripts)
if command -v python3 &> /dev/null; then
    echo -e "  ${GREEN}python3${NC} found (optional — used for script validation)"
else
    echo -e "  ${YELLOW}python3${NC} not found (optional — script validation won't be available)"
fi

echo ""

# ------------------------------------------------------------
# Install
# ------------------------------------------------------------

# Determine source: local checkout or clone
if [ -f "${SCRIPT_DIR}/SKILL.md" ]; then
    echo -e "${BOLD}Installing from local checkout...${NC}"
    SOURCE_DIR="${SCRIPT_DIR}"
else
    echo -e "${BOLD}Cloning repository...${NC}"
    TEMP_DIR="$(mktemp -d)"
    trap 'rm -rf "${TEMP_DIR}"' EXIT
    git clone --depth 1 "${REPO_URL}" "${TEMP_DIR}/google-ads-scripts-claude"
    SOURCE_DIR="${TEMP_DIR}/google-ads-scripts-claude"
fi

# Create directories
echo -e "${BOLD}Creating directories...${NC}"
mkdir -p "${INSTALL_DIR}"
mkdir -p "${AGENTS_DIR}"

# Copy skills
echo -e "${BOLD}Copying skills...${NC}"
cp -R "${SOURCE_DIR}/skills/"* "${INSTALL_DIR}/" 2>/dev/null || true
cp "${SOURCE_DIR}/SKILL.md" "${INSTALL_DIR}/SKILL.md"
echo -e "  ${GREEN}Skills${NC} installed to ${INSTALL_DIR}/"

# Copy scripts-skill
if [ -d "${SOURCE_DIR}/scripts-skill" ]; then
    mkdir -p "${INSTALL_DIR}/scripts-skill"
    cp -R "${SOURCE_DIR}/scripts-skill/"* "${INSTALL_DIR}/scripts-skill/" 2>/dev/null || true
    echo -e "  ${GREEN}Scripts skill${NC} copied"
fi

# Copy agents
if [ -d "${SOURCE_DIR}/agents" ] && [ "$(ls -A "${SOURCE_DIR}/agents/" 2>/dev/null)" ]; then
    cp "${SOURCE_DIR}/agents/"*.md "${AGENTS_DIR}/" 2>/dev/null || true
    echo -e "  ${GREEN}Agents${NC} installed to ${AGENTS_DIR}/"
else
    echo -e "  ${YELLOW}No agents found to install${NC}"
fi

# Copy templates
if [ -d "${SOURCE_DIR}/templates" ]; then
    mkdir -p "${INSTALL_DIR}/templates"
    cp -R "${SOURCE_DIR}/templates/"* "${INSTALL_DIR}/templates/" 2>/dev/null || true
    echo -e "  ${GREEN}Templates${NC} copied"
fi

# Copy docs
if [ -d "${SOURCE_DIR}/docs" ]; then
    mkdir -p "${INSTALL_DIR}/docs"
    cp -R "${SOURCE_DIR}/docs/"* "${INSTALL_DIR}/docs/" 2>/dev/null || true
    echo -e "  ${GREEN}Docs${NC} copied"
fi

# Copy Python scripts
if [ -d "${SOURCE_DIR}/scripts" ]; then
    mkdir -p "${INSTALL_DIR}/scripts"
    cp -R "${SOURCE_DIR}/scripts/"* "${INSTALL_DIR}/scripts/" 2>/dev/null || true
    echo -e "  ${GREEN}Python scripts${NC} copied"
fi

echo ""

# ------------------------------------------------------------
# Done
# ------------------------------------------------------------
echo -e "${GREEN}${BOLD}Installation complete!${NC}"
echo ""
echo -e "${BOLD}Available commands in Claude Code:${NC}"
echo -e "  ${CYAN}/script generate${NC}      Generate a custom script from plain English"
echo -e "  ${CYAN}/script budget${NC}        Budget pacing & alert scripts"
echo -e "  ${CYAN}/script bids${NC}          Bid adjustment & optimization scripts"
echo -e "  ${CYAN}/script report${NC}        Automated reporting scripts"
echo -e "  ${CYAN}/script links${NC}         URL validation & broken link detection"
echo -e "  ${CYAN}/script qs${NC}            Quality Score tracking scripts"
echo -e "  ${CYAN}/script search-terms${NC}  Search term mining & negatives"
echo -e "  ${CYAN}/script anomaly${NC}       Performance anomaly detection"
echo -e "  ${CYAN}/script labels${NC}        Auto-labeling scripts"
echo -e "  ${CYAN}/script audit${NC}         Script inventory & health check"
echo ""
echo -e "To uninstall: ${YELLOW}bash uninstall.sh${NC}"
