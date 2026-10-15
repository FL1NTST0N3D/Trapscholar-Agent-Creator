#!/usr/bin/env bash
set -euo pipefail

# ─────────────────────────────────────────────
# Copywriting Frameworks for Claude Code
# Installer
# ─────────────────────────────────────────────

ORANGE='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

header() {
  echo ""
  echo -e "${ORANGE}${BOLD}"
  echo "   ╔═══════════════════════════════════════════════╗"
  echo "   ║   Copywriting Frameworks for Claude Code      ║"
  echo "   ║   25+ frameworks · 12 commands · 3 agents     ║"
  echo "   ╚═══════════════════════════════════════════════╝"
  echo -e "${NC}"
}

info()    { echo -e "  ${BLUE}[INFO]${NC}  $1"; }
success() { echo -e "  ${GREEN}[OK]${NC}    $1"; }
fail()    { echo -e "  ${RED}[FAIL]${NC}  $1"; exit 1; }

# ── Header ──
header

# ── Prereq checks ──
info "Checking prerequisites..."

if ! command -v claude &>/dev/null; then
  fail "Claude Code CLI not found. Install: https://docs.anthropic.com/en/docs/claude-code"
fi
success "Claude Code CLI found"

if ! command -v git &>/dev/null; then
  fail "git not found. Install git first."
fi
success "git found"

# ── Detect script directory (works for cloned repo or manual run) ──
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ── Create target directories ──
CLAUDE_DIR="$HOME/.claude"
SKILLS_DIR="$CLAUDE_DIR/skills"
AGENTS_DIR="$CLAUDE_DIR/agents"
COPY_DIR="$CLAUDE_DIR/copy"

info "Installing to $CLAUDE_DIR ..."

mkdir -p "$SKILLS_DIR"
mkdir -p "$AGENTS_DIR"
mkdir -p "$COPY_DIR"

# ── Copy skills ──
if [ -d "$SCRIPT_DIR/skills" ]; then
  cp -r "$SCRIPT_DIR/skills/"* "$SKILLS_DIR/" 2>/dev/null || true
  success "Copied skills to $SKILLS_DIR"
else
  fail "skills/ directory not found in $SCRIPT_DIR"
fi

# ── Copy agents ──
if [ -d "$SCRIPT_DIR/agents" ]; then
  cp -r "$SCRIPT_DIR/agents/"* "$AGENTS_DIR/" 2>/dev/null || true
  success "Copied agents to $AGENTS_DIR"
else
  info "No agents/ directory found — skipping"
fi

# ── Copy root copy skill ──
if [ -d "$SCRIPT_DIR/copy" ]; then
  cp -r "$SCRIPT_DIR/copy/"* "$COPY_DIR/" 2>/dev/null || true
  success "Copied copy router to $COPY_DIR"
else
  info "No copy/ directory found — skipping"
fi

# ── Install Python dependencies (optional) ──
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
  if command -v pip3 &>/dev/null; then
    info "Installing Python dependencies..."
    pip3 install -r "$SCRIPT_DIR/requirements.txt" --quiet 2>/dev/null && \
      success "Python dependencies installed" || \
      info "Python dependencies skipped (non-critical)"
  else
    info "pip3 not found — skipping Python dependencies (optional)"
  fi
fi

# ── Done ──
echo ""
echo -e "${GREEN}${BOLD}  Installation complete!${NC}"
echo ""
echo "  Available commands:"
echo "  ─────────────────────────────────────────"
echo "    /copy aida          AIDA framework"
echo "    /copy pas           PAS framework"
echo "    /copy fab           FAB framework"
echo "    /copy bab           BAB framework"
echo "    /copy 4cs           4Cs clarity check"
echo "    /copy story         StoryBrand + PASTOR"
echo "    /copy power-words   200+ power words"
echo "    /copy headlines     50+ headline formulas"
echo "    /copy cta           30+ CTA formulas"
echo "    /copy objections    Objection handling"
echo "    /copy proof         Social proof frameworks"
echo "    /copy report        Copy audit & scoring"
echo "  ─────────────────────────────────────────"
echo ""
echo -e "  Run ${BOLD}claude${NC} and try: ${ORANGE}/copy aida${NC}"
echo ""
