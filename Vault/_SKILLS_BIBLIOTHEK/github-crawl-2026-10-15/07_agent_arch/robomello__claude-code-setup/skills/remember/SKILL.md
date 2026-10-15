---
name: remember
description: Save conversation learnings to persistent auto-memory files. Reviews the session, identifies key learnings, and updates topic files.
trigger: "remember", "save memory", "store this", "remember this session", "remember this", "save this to memory"
---

# /remember - Save Session Learnings to Memory

You are saving learnings from the current conversation to the persistent auto-memory system.

## Memory Location

All memory files live in: `~/.claude/projects/-home-user/memory/`

- `MEMORY.md` - Main index file (loaded into every conversation context, MUST stay under 150 lines)
- Topic files (e.g., `comfyui.md`, `etsy.md`) - Detailed notes organized by topic

## Procedure

1. **Review the conversation** - Identify what was learned:
   - Decisions made (architectural, tooling, workflow)
   - Problems solved and their solutions
   - New patterns or conventions discovered
   - Project status updates
   - Infrastructure changes (ports, services, configs)
   - User preferences learned
   - Corrections to previous assumptions

2. **Read existing memory files** - Before writing anything:
   - Read `MEMORY.md` to check the current index and avoid duplicates
   - Read any topic files that might already cover the same information
   - If the info already exists and is current, skip it

3. **Update or create topic files** as needed:
   - If a relevant topic file exists, update it with new information
   - If no topic file covers this topic, create a new one
   - Keep each topic file under 200 lines
   - Match existing format: markdown with headers, bullet points, tables where appropriate

4. **Update MEMORY.md index** if:
   - A new topic file was created (add it to the Topic Files section)
   - A major new section was added to an existing topic
   - Key operational rules changed
   - Keep MEMORY.md under 150 lines total

## Rules

- **Never duplicate** - Check before writing. Update existing entries, don't add parallel ones.
- **Only save stable, verified information** - Not speculation or in-progress debugging.
- **Be concise** - Memory files are reference docs, not narratives.
- **Preserve existing structure** - Don't reorganize files unless specifically asked.
- **Date-stamp significant changes** - Use format `(2026-MM-DD)` for time-sensitive entries.

## Output

After updating, report:
- Which files were updated and what was added/changed
- Current line count of MEMORY.md (warn if approaching 150)
