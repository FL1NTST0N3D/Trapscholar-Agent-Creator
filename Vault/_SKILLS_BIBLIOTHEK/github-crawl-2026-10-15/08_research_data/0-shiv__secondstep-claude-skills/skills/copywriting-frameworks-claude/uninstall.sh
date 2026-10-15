#!/usr/bin/env bash
set -euo pipefail

# ─────────────────────────────────────────────
# Copywriting Frameworks for Claude Code
# Uninstaller
# ─────────────────────────────────────────────

ORANGE='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

info()    { echo -e "  ${BLUE}[INFO]${NC}  $1"; }
success() { echo -e "  ${GREEN}[OK]${NC}    $1"; }
warn()    { echo -e "  ${ORANGE}[WARN]${NC}  $1"; }

echo ""
echo -e "${ORANGE}${BOLD}  Uninstalling Copywriting Frameworks for Claude Code${NC}"
echo ""

CLAUDE_DIR="$HOME/.claude"

# ── Skills to remove ──
SKILL_DIRS=(
  "copy-aida"
  "copy-pas"
  "copy-fab"
  "copy-bab"
  "copy-4cs"
  "copy-storytelling"
  "copy-power-words"
  "copy-headlines"
  "copy-cta-formulas"
  "copy-objection-handling"
  "copy-social-proof"
  "copy-report"
)

# ── Remove skills ──
info "Removing skills..."
for skill in "${SKILL_DIRS[@]}"; do
  if [ -d "$CLAUDE_DIR/skills/$skill" ]; then
    rm -rf "$CLAUDE_DIR/skills/$skill"
    success "Removed skills/$skill"
  fi
done

# ── Remove agents ──
AGENT_FILES=(
  "copy-strategist.md"
  "copy-reviewer.md"
  "copy-ab-tester.md"
)

info "Removing agents..."
for agent in "${AGENT_FILES[@]}"; do
  if [ -f "$CLAUDE_DIR/agents/$agent" ]; then
    rm -f "$CLAUDE_DIR/agents/$agent"
    success "Removed agents/$agent"
  fi
done

# ── Remove copy router ──
if [ -d "$CLAUDE_DIR/copy" ]; then
  rm -rf "$CLAUDE_DIR/copy"
  success "Removed copy/ router"
fi

echo ""
echo -e "${GREEN}${BOLD}  Uninstall complete.${NC}"
echo ""
echo "  The cloned repo has not been removed."
echo "  To fully remove, delete the repo directory manually."
echo ""
