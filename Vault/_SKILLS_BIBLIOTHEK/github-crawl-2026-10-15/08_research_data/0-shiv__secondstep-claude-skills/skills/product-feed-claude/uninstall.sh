#!/usr/bin/env bash
set -euo pipefail

# ============================================================
#  Product Feed Claude — Uninstaller
#  Removes skill files, agents, and scripts
# ============================================================

cat << 'BANNER'

  ╔══════════════════════════════════════════════╗
  ║      Product Feed Claude — Uninstaller       ║
  ╚══════════════════════════════════════════════╝

BANNER

INSTALL_DIR="$HOME/.claude/skills/product-feed-claude"
AGENTS_DIR="$HOME/.claude/agents"

echo "  This will remove:"
echo "    - $INSTALL_DIR"
echo "    - $AGENTS_DIR/feed-quality.md"
echo "    - $AGENTS_DIR/feed-compliance.md"
echo ""

read -p "  Continue? (y/N): " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo "  Cancelled."
    exit 0
fi

echo ""

# Remove skill directory
if [ -d "$INSTALL_DIR" ]; then
    rm -rf "$INSTALL_DIR"
    echo "  Removed: $INSTALL_DIR"
else
    echo "  Not found: $INSTALL_DIR (skipped)"
fi

# Remove agent files
for agent in feed-quality.md feed-compliance.md; do
    if [ -f "$AGENTS_DIR/$agent" ]; then
        rm -f "$AGENTS_DIR/$agent"
        echo "  Removed: $AGENTS_DIR/$agent"
    else
        echo "  Not found: $AGENTS_DIR/$agent (skipped)"
    fi
done

echo ""
echo "  Uninstall complete."
echo ""
echo "  Note: Python packages (pandas, openpyxl) were not removed."
echo "  To remove them: pip uninstall pandas openpyxl"
echo ""
