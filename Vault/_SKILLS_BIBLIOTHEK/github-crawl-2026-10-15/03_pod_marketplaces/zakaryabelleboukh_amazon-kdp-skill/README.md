# 📚 Amazon KDP Publishing Expert

> A professional Claude Skill for planning, writing, editing, formatting, packaging, and quality-checking books for Amazon Kindle Direct Publishing (KDP).

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blueviolet)](https://claude.ai/)
[![Amazon KDP](https://img.shields.io/badge/Amazon-KDP-orange)](https://kdp.amazon.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Overview

**Amazon KDP Publishing Expert** turns Claude into a structured book-production assistant. It helps creators move from an idea or manuscript to a polished KDP-ready publishing package.

**Idea → Planning → Manuscript → Editing → Interior → Cover → Metadata → QA → Publishing Checklist**

## ✨ Features

- 📖 Book planning and chapter architecture
- ✍️ Manuscript development and editing
- 🔎 Consistency and quality checks
- 📐 Paperback, hardcover and Kindle preparation
- 🎨 Cover briefs and image-generation prompts
- 📝 KDP title, subtitle and description preparation
- 🔑 Keyword strategy and category suggestions
- 📋 Pre-publication QA checklist
- 🧠 Clear separation between facts, assumptions and estimates
- 🛡️ Copyright-aware workflow
- 🌐 Current requirements can be verified when web access is available

## 🚀 Installation in Claude

1. Download or clone this repository.
2. Keep `SKILL.md` at the root of the skill folder.
3. Package the folder as a ZIP if your Claude interface requires ZIP upload.
4. Open **Settings / Customize → Skills** in Claude.
5. Upload and enable the skill.

### Clone

```bash
git clone https://github.com/zakaryabelleboukh/amazon-kdp-skill.git
cd amazon-kdp-skill
```

## 💬 Example prompts

### Create a book

```text
I want to create a children's activity book for ages 6–8.
Build the complete book concept, page structure, activity plan,
writing guidelines, cover brief, metadata and publishing checklist.
```

### Improve a manuscript

```text
Review this manuscript as a professional editor.
Improve clarity, structure, consistency and reader experience.
Do not change factual claims unless they are clearly identified for verification.
```

### Prepare metadata

```text
Create a complete KDP metadata package for this book:
title, subtitle, description, seven keyword ideas, category suggestions,
audience and publishing checklist.
Keep every claim accurate to the actual manuscript.
```

### Final QA

```text
Run a complete pre-publication KDP QA audit.
Check manuscript structure, front matter, back matter, TOC,
formatting consistency, metadata consistency, cover requirements
and anything that could cause publishing problems.
```

## 📁 Repository structure

```text
amazon-kdp-skill/
├── SKILL.md
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── SECURITY.md
├── NOTICE.md
├── .gitignore
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── pull_request_template.md
└── examples/
    ├── README.md
    ├── nonfiction-book.md
    ├── childrens-book.md
    └── kdp-qa-checklist.md
```

## ⚠️ Important

This project is an AI-assisted publishing workflow, not an official Amazon product.

KDP requirements, policies, categories, royalties, trim options and other platform details can change. When current information matters, verify it against official Amazon KDP documentation before publishing.

The skill does not guarantee KDP approval, sales, rankings, reviews or revenue.

## 🤝 Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

## 👤 Author

Created by **Zakarya Belleboukh**.

- GitHub: [@zakaryabelleboukh](https://github.com/zakaryabelleboukh)

If this project is useful, consider giving the repository a ⭐.
