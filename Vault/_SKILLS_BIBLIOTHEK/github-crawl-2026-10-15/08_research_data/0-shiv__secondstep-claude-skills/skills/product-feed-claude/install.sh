#!/usr/bin/env bash
set -euo pipefail

# ============================================================
#  Product Feed Claude — Installer
#  Google Merchant Center feed optimization skills for Claude
# ============================================================

cat << 'BANNER'

  ╔══════════════════════════════════════════════╗
  ║       Product Feed Claude — Installer        ║
  ║   Feed optimization skills for Claude Code   ║
  ╚══════════════════════════════════════════════╝

BANNER

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_URL="https://github.com/0-shiv/product-feed-claude.git"
INSTALL_DIR="$HOME/.claude/skills/product-feed-claude"
AGENTS_DIR="$HOME/.claude/agents"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ---------------------------------------------------------------------------
# Prerequisite checks
# ---------------------------------------------------------------------------

echo "  Checking prerequisites..."

# Python 3.8+
if ! command -v python3 &> /dev/null; then
    echo "  ERROR: Python 3 is required but not found."
    echo "  Install Python 3.8+ from https://python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MAJOR=$(echo "$PYTHON_VERSION" | cut -d. -f1)
PYTHON_MINOR=$(echo "$PYTHON_VERSION" | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    echo "  ERROR: Python 3.8+ required. Found: Python $PYTHON_VERSION"
    exit 1
fi
echo "  Python $PYTHON_VERSION .................. OK"

# pip
if ! command -v pip3 &> /dev/null && ! python3 -m pip --version &> /dev/null; then
    echo "  ERROR: pip is required but not found."
    echo "  Install pip: python3 -m ensurepip --upgrade"
    exit 1
fi
echo "  pip ............................ OK"

# git (only needed if cloning)
if [ ! -f "$SCRIPT_DIR/SKILL.md" ]; then
    if ! command -v git &> /dev/null; then
        echo "  ERROR: git is required for cloning the repo."
        exit 1
    fi
    echo "  git ............................ OK"
fi

echo ""

# ---------------------------------------------------------------------------
# Install
# ---------------------------------------------------------------------------

# If running from inside the repo, use local files. Otherwise, clone.
if [ -f "$SCRIPT_DIR/SKILL.md" ]; then
    echo "  Running from local repo: $SCRIPT_DIR"
    SOURCE_DIR="$SCRIPT_DIR"
else
    echo "  Cloning repository..."
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 "$REPO_URL" "$TEMP_DIR"
    SOURCE_DIR="$TEMP_DIR"
fi

# Create directories
echo "  Creating directories..."
mkdir -p "$INSTALL_DIR/skills"
mkdir -p "$AGENTS_DIR"
mkdir -p "$INSTALL_DIR/scripts"

# Copy skill files
echo "  Installing skills..."
cp "$SOURCE_DIR/SKILL.md" "$INSTALL_DIR/"
cp -r "$SOURCE_DIR/skills/"* "$INSTALL_DIR/skills/" 2>/dev/null || true

# Copy agents
echo "  Installing agents..."
cp "$SOURCE_DIR/agents/"*.md "$AGENTS_DIR/" 2>/dev/null || true

# Copy scripts
echo "  Installing scripts..."
cp "$SOURCE_DIR/scripts/"*.py "$INSTALL_DIR/scripts/" 2>/dev/null || true

# Install Python dependencies
echo "  Installing Python dependencies..."
if [ -f "$SOURCE_DIR/requirements.txt" ]; then
    python3 -m pip install -q -r "$SOURCE_DIR/requirements.txt"
fi

# Clean up temp directory if we cloned
if [ -n "${TEMP_DIR:-}" ] && [ -d "${TEMP_DIR:-}" ]; then
    rm -rf "$TEMP_DIR"
fi

# ---------------------------------------------------------------------------
# Verify
# ---------------------------------------------------------------------------

echo ""
echo "  Verifying installation..."

ERRORS=0

if [ ! -f "$INSTALL_DIR/SKILL.md" ]; then
    echo "  WARN: Master SKILL.md not found"
    ERRORS=$((ERRORS + 1))
fi

SKILL_COUNT=$(find "$INSTALL_DIR/skills" -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
echo "  Sub-skills installed: $SKILL_COUNT"

AGENT_COUNT=$(ls "$AGENTS_DIR"/feed-*.md 2>/dev/null | wc -l | tr -d ' ')
echo "  Agents installed: $AGENT_COUNT"

if [ -f "$INSTALL_DIR/scripts/feed_analyzer.py" ]; then
    echo "  feed_analyzer.py ............... OK"
else
    echo "  WARN: feed_analyzer.py not found"
    ERRORS=$((ERRORS + 1))
fi

if [ -f "$INSTALL_DIR/scripts/feed_report.py" ]; then
    echo "  feed_report.py ................. OK"
else
    echo "  WARN: feed_report.py not found"
    ERRORS=$((ERRORS + 1))
fi

echo ""

if [ "$ERRORS" -eq 0 ]; then
    echo "  Installation complete!"
else
    echo "  Installation complete with $ERRORS warnings."
fi

cat << 'DONE'

  ┌────────────────────────────────────────────┐
  │  Next steps:                               │
  │  1. Export your feed from Merchant Center   │
  │  2. Place the CSV/TSV in the feed/ dir     │
  │  3. Run: /feed audit                       │
  └────────────────────────────────────────────┘

DONE
