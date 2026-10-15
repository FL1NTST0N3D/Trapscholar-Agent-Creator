# Claude Code Setup

A production Claude Code setup running on a home server with 30+ agents, 14 skills, 16 hooks, and strict operational rules. This is the actual configuration powering daily workflows across Docker infrastructure, media production, e-commerce, and content creation.

## What's Inside

```
.claude/
  agents/           # 30 specialized agents (API wrappers, code review, deployment, media gen)
    scripts/        # Python scripts used by agents (GEO auditing, crawler checks)
  rules/            # 5 behavioral rules (planning, quality gates, agent behavior)
  hooks/            # 12 hook scripts (pre/post tool use, validators, session management)
    validators/     # 3 validation scripts (deploy, NocoDB, plan review)
  helpers/          # 2 helper scripts (session memory, pre-compact context)
  skills/           # 14 skills (debugging, PDF, image gen, design, copywriting, etc.)
  settings.json     # Full hook wiring, plugin config, telemetry setup
  CLAUDE.md         # Project-level instructions
```

## Architecture

### Rules (always loaded into context)

| Rule | Purpose |
|------|---------|
| `context.md` | Server identity, hardware, critical rules (no localhost, CLI-only, local-first AI) |
| `planning.md` | Mandatory plan-agent usage, dependency-first workflow, prerequisites phase |
| `quality-gates.md` | Code review enforcement, security checklist, secret management |
| `agent-behavior.md` | Handle corrections, act on problems, verify UI changes |
| `skill-vs-agent.md` | Decision framework: when to build an agent vs a skill |

### Hooks (automated guardrails)

| Hook | Event | Purpose |
|------|-------|---------|
| `docker-compose-enforcer.sh` | PreToolUse:Bash | Blocks `docker restart` for compose services (must use stop/rm/up) |
| `pre-edit.sh` | PreToolUse:Edit,Write | Blocks Anthropic SDK imports and localhost URLs in browser code |
| `doc-file-blocker.sh` | PreToolUse:Write | Prevents unnecessary .md/.txt file creation |
| `telegram_confirm.py` | PreToolUse:Bash,Edit,Write | AI-powered autonomous approval via Telegram for dangerous ops |
| `comfyui-logger.sh` | PostToolUse:Bash | Logs ComfyUI generation events |
| `geo-check.sh` | PostToolUse:Write | GEO/SEO advisory checks on HTML files |
| `post_tool_router.sh` | PostToolUse:* | Routes events to plan archival and review |
| `review_code.sh` | PostToolUse | Multi-LLM consensus code review (4-phase pipeline) |
| `review_plan.sh` | PostToolUse | Multi-LLM consensus plan review (3 independent reviewers) |
| `review_on_exit_plan.sh` | PostToolUse:ExitPlanMode | Triggers plan review when exiting plan mode |
| `archive_plan.sh` | PostToolUse | Archives completed plans |
| `printwalk-session.sh` | SessionStart/End | Dashboard session lifecycle tracking |

### Helpers (session infrastructure)

| Helper | Purpose |
|--------|---------|
| `session-memory.sh` | Loads/saves persistent memory context across sessions |
| `pre-compact.sh` | Preserves critical context before conversation compression |

### Agents (30 specialized subprocesses)

**Infrastructure**: deploy-agent, browser-agent, security-reviewer, code-reviewer
**Media**: local-image-gen (skill), veo3_agent, kling2pro_agent, suno_agent, avatar-agent, thumbnail-agent, video-pipeline-agent, ad-gen-agent
**APIs**: etsy-agent, printify-agent, nocodb-agent, scrape-creators-agent, slack-agent, telegram-agent, youtube-uploader-agent, youtube-analytics-agent, youtube-seo-agent, elevenlabs-agent, nest-agent
**AI Routing**: model-router-agent, claude-llm-agent, glm-agent
**Planning**: plan-agent, skill-improver-agent, geo-audit-agent, health-audit-agent

### Skills (14 methodology injections)

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Root-cause debugging methodology (no fixes without investigation) |
| `local-image-gen` | ComfyUI image generation with model selection |
| `interface-design` | Dashboard/admin panel design with craft foundations |
| `frontend-design` | Production-grade frontend avoiding generic AI aesthetics |
| `copywriting` | Marketing copy with GEO optimization |
| `content-idea-generator` | Content ideas rooted in positioning |
| `pdf` | PDF processing (read, merge, split, OCR, create) |
| `skill-creator` | Meta-skill for creating and evaluating new skills |
| `youtube-analyzer` | Video analysis (transcript + frame-by-frame visual) |
| `etsy-browser` | Etsy shop management via API and browser automation |
| `nest-control` | Google Nest thermostat control via SDM API |
| `cost-estimate` | Claude Code productivity analysis and ROI |
| `disk-cleanup` | Disk audit and NAS offload |
| `remember` | Persistent memory management |

## Key Design Patterns

### Multi-LLM Consensus Review
Both `review_code.sh` and `review_plan.sh` use 3-4 independent LLM reviewers (Claude, Codex, Gemini, GLM) that review independently, then a consensus vote determines pass/fail. This catches issues that any single model might miss.

### Plan-First Workflow
The `planning.md` rule enforces: Plan -> Review -> Prerequisites -> Execute. No implementation starts without an approved plan. The plan-agent runs as a subagent, gets reviewed by consensus hooks, and must pass before ExitPlanMode.

### Telegram Approval Gate
`telegram_confirm.py` uses a local LLM (GLM-5) to assess whether each tool call is dangerous. If dangerous, it sends a Telegram message for human approval before proceeding. Non-dangerous operations pass through automatically.

### Session Memory Persistence
`session-memory.sh` + `pre-compact.sh` maintain memory across sessions and conversation compressions. Memory files in `~/.claude/projects/*/memory/` survive context window limits.

### Hook-Enforced Guardrails
Hooks prevent common mistakes automatically:
- `docker-compose-enforcer.sh` prevents the `docker restart` footgun (doesn't pick up compose changes)
- `pre-edit.sh` blocks Anthropic SDK usage (must use CLI) and localhost URLs in browser code
- `doc-file-blocker.sh` prevents Claude from creating unnecessary documentation files

## Setup

1. Copy the directory structure into `~/.claude/`
2. Edit `rules/context.md` with your hardware, domains, and infrastructure
3. Configure `settings.json` hook paths to match your installation
4. Set environment variables in `~/.env` for API keys
5. Make hook scripts executable: `chmod +x ~/.claude/hooks/*.sh`

## Customization

- **Remove agents you don't need** -- each agent is independent
- **Edit `rules/context.md`** -- this is the main customization point (your hardware, domains, rules)
- **Adjust hooks** -- remove or modify hooks that don't match your workflow
- **Add your own skills** -- follow the `skill-creator` skill's patterns

## Notes

- This setup assumes a single-user Linux server with Docker
- Paths use `~/` -- expand to your actual home directory
- API keys are never hardcoded -- always loaded from `~/.env`
- The `settings.json` includes hook wiring but not `settings.local.json` (permissions are personal)
- Some agents reference specific APIs (kie.ai, ElevenLabs, Printify, etc.) -- remove if unused
