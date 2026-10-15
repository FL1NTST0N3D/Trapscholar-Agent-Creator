# Installation

## Prerequisites

- **Python 3.8+** — required for analysis scripts
- **pip** — Python package manager
- **Claude Code CLI** — for running `/feed` commands
- **Google Merchant Center account** — to export product feeds

## Quick Install

### Option 1: Automated Installer

```bash
curl -fsSL https://raw.githubusercontent.com/0-shiv/product-feed-claude/main/install.sh | bash
```

Or clone and run locally:

```bash
git clone https://github.com/0-shiv/product-feed-claude.git
cd product-feed-claude
bash install.sh
```

### Option 2: Manual Install

1. **Clone the repository:**
   ```bash
   git clone https://github.com/0-shiv/product-feed-claude.git
   cd product-feed-claude
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Copy skill files to Claude Code:**
   ```bash
   mkdir -p ~/.claude/skills/product-feed-claude
   cp -r skills/ ~/.claude/skills/product-feed-claude/
   cp SKILL.md ~/.claude/skills/product-feed-claude/
   ```

4. **Copy agent configurations:**
   ```bash
   mkdir -p ~/.claude/agents
   cp agents/*.md ~/.claude/agents/
   ```

5. **Verify installation:**
   ```bash
   python scripts/feed_analyzer.py --help
   ```

## Directory Structure After Install

```
~/.claude/
  skills/
    product-feed-claude/
      SKILL.md                          # Master skill
      skills/
        feed-title-optimization/SKILL.md
        feed-description/SKILL.md
        feed-images/SKILL.md
        feed-attributes/SKILL.md
        feed-labels/SKILL.md
        feed-disapprovals/SKILL.md
        feed-supplemental/SKILL.md
        feed-report/SKILL.md
  agents/
    feed-quality.md
    feed-compliance.md
```

## Exporting Your Feed

Before using the skills, export your product feed from Google Merchant Center:

1. Go to **Merchant Center > Products > Feeds**
2. Click on your primary feed
3. Click **Download** (CSV or TSV format)
4. Save the file to the `feed/` directory in the repo

Alternatively, export from your ecommerce platform:
- **Shopify:** Settings > Google & YouTube > Product feed export
- **WooCommerce:** Use a feed plugin like Product Feed PRO
- **BigCommerce:** Channel Manager > Google Shopping > Export

## Uninstall

```bash
bash uninstall.sh
```

Or manually:

```bash
rm -rf ~/.claude/skills/product-feed-claude
rm -f ~/.claude/agents/feed-quality.md
rm -f ~/.claude/agents/feed-compliance.md
```

## Troubleshooting

| Issue | Solution |
|---|---|
| `ModuleNotFoundError: pandas` | Run `pip install -r requirements.txt` |
| Feed file not found | Place your feed CSV/TSV in the `feed/` directory |
| Permission denied on install.sh | Run `chmod +x install.sh && bash install.sh` |
| Python version too old | Upgrade to Python 3.8+: `python3 --version` |
