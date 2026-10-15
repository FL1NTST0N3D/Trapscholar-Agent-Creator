# 07 – Agent-Architektur, Modell-Routing und Token-Sparen (Claude Code / Agent SDK / Routinen)

Stand: 2026-10-15. Quellenlage: Offizielle Docs (code.claude.com, per WebFetch gelesen) sind als **[DOC]** markiert; Repo-READMEs als **[REPO]**; Blog-/Suchmaschinen-Behauptungen als **[BLOG]**. Zahlen aus Repos/Blogs sind Eigenangaben der Autoren und nicht unabhängig geprüft, sofern nicht anders vermerkt.

Alle Repo-Pfade liegen unter `/tmp/claude-0/-home-user-Trapscholar-Agent-Creator/565203ac-a19a-5fc6-82c5-f701b96a51c7/scratchpad/crawl/repos/<dir>`. Neu geklonte Verzeichnisse heißen `<owner>__<repo>`, die bereits vorhandenen `<owner>_<repo>`.

---

## Gecrawlte Repos

Relevanz 1-5 bezieht sich auf: "vollautomatisierter E-Commerce-Betrieb mit Claude Code / Agent SDK / Scheduled Routines" (Architektur, Routing, Kosten). Zählungen stammen aus `grep "^model:"` bzw. `find SKILL.md`/`hooks` im Klon (Stichtag oben).

| Repo | URL | Lizenz | Inhalt kurz | Agents / Skills / Hooks | Relevanz |
|---|---|---|---|---|---|
| shanraisshan/claude-code-best-practice (vorh.) | https://github.com/shanraisshan/claude-code-best-practice | MIT | Best-Practice-Sammlung: Command→Agent→Skill-Orchestrierung, Agent-Teams-Demo, Reports (`why-harness-is-important.md`: 10 Harness-Fähigkeiten inkl. Model-Routing), Boris/Thariq-Tipps zu Effort/Context | 26 Agents mit `model:` (5 haiku/12 sonnet/12 opus) / 9 Skills / 3 Hooks | 5 |
| affaan-m/everything-claude-code (ECC) (vorh.) | https://github.com/affaan-m/everything-claude-code | MIT | "Agent Harness OS": 303 Agents, 1062 SKILL.md, 173 Hook-Dateien; `docs/token-optimization.md`, Skills `strategic-compact`, `cost-aware-llm-pipeline`, `cost-tracking`, `context-budget`, `token-budget-advisor`, `council`, `continuous-agent-loop`, `orch-pipeline`, `team-agent-orchestration`, `unified-memory`; `rules/common/performance.md` (Modellwahl) | 303 (28 haiku/242 sonnet/33 opus) / 1062 / 173 | 5 |
| wshobson/agents (vorh.) | https://github.com/wshobson/agents | MIT | 92 Plugins, 202 Agents mit expliziten Modell-Tiers (Opus/inherit/Sonnet/Haiku), ARCHITECTURE.md mit Tier-Tabelle, Plugins `agent-orchestration`, `agent-teams`, `context-management`, `plugin-eval` | 202 (24 haiku/70 sonnet/54 opus/52 inherit/2 fable) / 185 / 6 | 5 |
| VoltAgent/awesome-claude-code-subagents (vorh.) | https://github.com/VoltAgent/awesome-claude-code-subagents | MIT | 155 Subagents in 10 Kategorien inkl. `09-meta-orchestration` | 155 (19 haiku/109 sonnet/26 inherit) / 0 / 0 | 3 |
| davila7/claude-code-templates (vorh.) | https://github.com/davila7/claude-code-templates | MIT | Komponenten-Katalog: 112 Agents, 916 Skills, 156 Hook-Dateien; Guard-Hooks (`subagent-read-only-guard`, `scope-guard`, `doordash-spend-guard` = Budget-Gate via Exit-2) | 112 (1 haiku/70 sonnet/2 inherit) / 916 / 156 | 4 |
| obra/superpowers (vorh.) | https://github.com/obra/superpowers | MIT | Methodik-Skills: `subagent-driven-development`, `dispatching-parallel-agents`, `writing-plans`, `verification-before-completion` | 0 / 15 / 3 | 4 |
| hesreallyhim/awesome-claude-code (vorh.) | https://github.com/hesreallyhim/awesome-claude-code | CC BY-NC-ND 4.0 | Kuratierte Liste (CSV `THE_RESOURCES_TABLE_NEW.csv`) mit Kategorien "Agent Orchestration", "Memory & Context Persistence", "Usage & Cost" (ccusage, ccvitals, toktrack, cc-costline, CCDash, AgentWatch…) | – | 3 |
| ruvnet/claude-flow (ruflo) (vorh.) | https://github.com/ruvnet/claude-flow | MIT | Schwarm-Harness: Router, Hive-Mind, 27 Hooks, Plugins `ruflo-cost-tracker`, `ruflo-loop-workers`, `ruflo-ruvllm` (Smart Routing), "Task Routing 89% accuracy" (Eigenangabe) | 68 (9 haiku/57 sonnet/2 opus) / 380 / 773 | 3 |
| juliusbrussee/caveman (vorh.) | https://github.com/JuliusBrussee/caveman | Apache-2.0 | Output-Kompression ("Say less"), Input-Filter ("Read less": 33,2 % weniger Input-Token über 54 Runs), "Auto"-Modellwahl (54 % billiger als Opus 5.5 xhigh bei gleichem Score, 85 Tasks, Zwischenstand), Blocks (Code-Mode) | 5 (5 haiku) / 28 / 11 | 5 |
| rtk-ai/rtk (vorh.) | https://github.com/rtk-ai/rtk | Apache-2.0 + BUSL-1.1 | Rust-CLI, filtert Bash-Output vor dem Kontext (bis 90 % kleiner, Eigenangabe; betrifft nur Bash-Output-Anteil); PreToolUse-Rewrite-Hook für 13 Agents | 21 (11 haiku/10 sonnet) / 12 / 12 | 4 |
| Dubibubii/usage-limit-reducer (vorh.) | https://github.com/Dubibubii/usage-limit-reducer | k.A. | Skill mit 11 Regeln + `usage-report.py` (liest `~/.claude/projects/*.jsonl`); Kernaussage "98,5 % der Tokens gehen oft an Re-Lesen der History" | 0 / 1 / 0 | 3 |
| lst97/claude-code-sub-agents (vorh.) | https://github.com/lst97/claude-code-sub-agents | MIT | 37 Subagents + `agent-organizer` (Meta-Orchestrator, 1-3-Agent-Teams) | 37 (6 haiku/31 sonnet) / 0 / 0 | 2 |
| zhsama/claude-sub-agent (vorh.) | https://github.com/zhsama/claude-sub-agent | k.A. | Spec-Workflow: `spec-orchestrator` → analyst → architect → planner → Quality Gates | Agents ohne `model:` | 2 |
| **michael-harris/claude-code-multi-agent-dev-system (DevTeam)** | https://github.com/michael-harris/claude-code-multi-agent-dev-system | MIT | Vollautomatische Sprints; **Model Escalation haiku→sonnet→opus** (konfigurierbar `consecutive_failures`), **Eco-Mode**, Bug Council (5 Agents), SQLite-Kostentracking, Quality Gates | 83 (16 haiku/35 sonnet/42 opus) / 20 / 14 | 5 |
| **TurboKach/claude-code-setup** | https://github.com/TurboKach/claude-code-setup | MIT | Parallel-Fan-out-Starter: Rolle→Modell-Tabelle (`skills/agent-teams/SKILL.md`), Token-Disziplin-Regeln, Executor mit `isolation: worktree`, Plan-Approval-Gate | 9 (7 sonnet/1 opus/1 inherit) / 4 / 6 | 5 |
| **robomello/claude-code-setup** (von anderem Crawler geklont) | https://github.com/robomello/claude-code-setup | k.A. | **E-Commerce-nah**: etsy-, printify-, nocodb-, telegram-Agents alle `model: haiku`; `model-router-agent.md` (Komplexität 1/2/3 → haiku/sonnet/opus); **Telegram-Approval-Gate** (`telegram_confirm.py`) für gefährliche Tool-Calls; Multi-LLM-Konsens-Review | 26 (20 haiku/3 sonnet/3 opus) / 14 / 15 | 5 |
| **fltman/loop-engineer** | https://github.com/fltman/loop-engineer | MIT | Skill+Subagent für "Loop Engineering": Templates `headless-loop.sh`, `evaluator-optimizer.sh`, `fanout-orchestrator.sh`, `meta-prompt-refine.sh`; `guardrails.md` (Loopmaxxing, Kosten-Blowups, Evaluator-Kollusion); Cost-Gating über `total_cost_usd` | 0 / 1 / 0 | 5 |
| **pejmanjohn/slot-machine** | https://github.com/pejmanjohn/slot-machine | MIT | Best-of-N: N Implementierungen parallel → unabhängige Reviewer → Meta-Judge (pick/synthesize/reject) | 0 / 2 / 0 | 4 |
| **anthropics/claude-agent-sdk-demos** | https://github.com/anthropics/claude-agent-sdk-demos | MIT | Offizielle SDK-Demos; `research-agent/` = Orchestrator/Worker (Lead → parallele Researcher auf `model="haiku"` → Analyst → Writer) | 0 / 6 / 4 | 4 |
| **anthropics/commerce-agents** | https://github.com/anthropics/commerce-agents | (LICENSE vorhanden) | Offizieller Commerce-Blueprint: Shopping-Agent + **Merchant-Agent, jede Schreibaktion ist ein "staged change", den ein Mensch freigibt**; Gates/Fencing/Caps im Tool-Call; Messages API / Agent SDK / Managed Agents; `merchant-agent/managed-agents/` mit Scheduled Digest | 0 / 16 / 0 | 5 |
| Shopify/claude-for-commerce-examples (vorh.) | https://github.com/Shopify/claude-for-commerce-examples | (LICENSE vorhanden) | Shopify-Umsetzung des Blueprints: `storefront/` (UCP) + `merchant/` (Admin API, staged writes) | 0 / 10 / 0 | 4 |
| **sweetpotating/claude-commerce-agents** | https://github.com/sweetpotating/claude-commerce-agents | (README-Stub) | Kleine Commerce-Agent-Sammlung (5 Skills); inhaltlich dünn | 0 / 5 / 0 | 2 |
| **marlinjai/orchestrator** | https://github.com/marlinjai/orchestrator | k.A. | Worker (Agent-SDK-Session) + zustandsloser **Decision Proxy** (`continue/replan/escalate/stop`), persistenter State, Kill-Switch, Worktree je Task, Telemetrie | 0 / 1 / 0 | 4 |
| **T0UGH/agent-cron** | https://github.com/T0UGH/agent-cron | k.A. | Agent-SDK-Tasks als `.md` (Prompt + Cron), Feishu-Delivery, Claude-Code-Skill zur Verwaltung | 0 / 1 / 0 | 4 |
| **tonybentley/claude-mcp-scheduler** | https://github.com/tonybentley/claude-mcp-scheduler | MIT | Cron + Claude API + lokale MCP-Server (Demo) | 0 / 0 / 0 | 2 |
| **TechNickAI/openclaw-config** | https://github.com/TechNickAI/openclaw-config | k.A. | Claude-Code-basierter "persönlicher Agent": 3-Tier-Memory, Workflows per Cron (`cron-healthcheck`, `llm-usage-report`, `email-steward`…), Skill `smart-delegation` (Routing zu Opus/Grok) | 1 / 24 / 0 | 4 |
| **shareAI-lab/learn-claude-code** | https://github.com/shareAI-lab/learn-claude-code | MIT | Lehr-Repo "Harness Engineering": Agent-Loop von 0 an, Subagents, Kontext-Management | 0 / 4 / 4 | 3 |
| **shareAI-lab/claw0** | https://github.com/shareAI-lab/claw0 | k.A. | 10 Lektionen bis zum Agent-Gateway inkl. s07 Heartbeat & Cron, s08 Delivery-Queue, s09 Retry-Onion | 0 / 1 / 0 | 3 |
| **VoltAgent/awesome-openclaw-skills** | https://github.com/VoltAgent/awesome-openclaw-skills | MIT | Katalog mit 5300+ OpenClaw-Skills (ClawHub) | – | 2 |
| openclaw/openclaw (geklont, **gelöscht**, 952 MB) | https://github.com/openclaw/openclaw | MIT | Agent-Runtime: Automations/Cron (`docs/automation/cron-jobs*.md`): per-Job `--model`, `--thinking`, `--light-context`, `--tools`, Sessions `main/current/isolated/custom`; Heartbeat (30 min default, `lightContext`, `isolatedSession`, `activeHours`, eigenes `model`) | 4 / 125 / 100 | 4 (Konzepte) |
| NousResearch/hermes-agent (geklont, **gelöscht**, 350 MB) | https://github.com/NousResearch/hermes-agent | MIT | Cron: Modell-Auflösung "per-job pin → `cron.model` → Hauptmodell", per-Job Reasoning-Effort, No-Agent-Modus (Script ohne LLM), Preflight (keine LLM-Kosten bei Fehlkonfiguration), Cron darf keine Cron-Jobs anlegen; `delegate_task` (bis 10 parallel); Memory 2 200 Zeichen Cap; Fallback-Provider | 42 / 212 / 217 | 4 (Konzepte) |
| thedotmack/claude-mem (geklont, **gelöscht**, 301 MB) | https://github.com/thedotmack/claude-mem | Apache-2.0 | Persistentes Memory-Plugin: Hooks Setup/SessionStart/UserPromptSubmit/PostToolUse/Stop/SessionEnd, SQLite+Chroma, Kompression via Agent SDK | 0 / 37 / 20 | 3 |
| **egorfedorov/claude-context-optimizer** | https://github.com/egorfedorov/claude-context-optimizer | MIT | Plugin: Read-Cache + "Context Shield" (PreToolUse Read), Prompt-Coach, Kostenreport pro Modell (Opus 5.5 $4/$20, Cache-Read $0.20/M laut README); "30-50 % Waste" (Eigenangabe) | 0 / 22 / 1 | 4 |
| **alexgreensh/token-optimizer** | https://github.com/alexgreensh/token-optimizer | (LICENSE vorhanden) | Plugin mit 31 Hook-Dateien: Delta-Reads, Skeleton-Reads, Bash/Search-Kompression, Checkpoint vor Auto-Compact, Session-DB, Quality-Score; Roundup-Claim "~18 %" [BLOG] | 0 / 18 / 31 | 4 |
| **mksglu/context-mode** | https://github.com/mksglu/context-mode | Elastic 2.0 | MCP-Server + Hooks: Tool-Output im Sandbox halten, "315 KB → 5,4 KB (98 %)", "Think in Code" (`ctx_execute`), FTS5-Session-Index | 0 / 11 / 44 | 4 |
| **ww-w-ai/claude-code-token-saver** | https://github.com/ww-w-ai/claude-code-token-saver | k.A. | "super-token-saver": SubTask-Delegation (Cache-Write $6,25 statt $10/MTok laut README), `/s-continue` (Restore ohne LLM-Call), Cache-Expiry-Guard, Git-Lite (−2 200 Token/Session); "$326→$180/Tag" (Eigenangabe) | 0 / 6 / 5 | 4 |
| **drona23/claude-token-efficient** | https://github.com/drona23/claude-token-efficient | MIT | Eine CLAUDE.md für knappe Antworten; warnt selbst, dass Instruktionsdateien Input-Token kosten | 0 / 0 / 0 | 2 |
| **aandersen2323/ai-context-stack** | https://github.com/aandersen2323/ai-context-stack | k.A. | Kontext einmal speichern, referenzieren; "80-90 %" (unbelegte Eigenangabe) | 0 / 0 / 0 | 1 |
| **TokenRollAI/cc-plugin (llmdoc)** | https://github.com/TokenRollAI/cc-plugin | k.A. | Persistente Architektur-Doku für Agents, nur benötigten Kontext laden; "83 %" [BLOG] | 3 (inherit) / 10 / 1 | 2 |
| **Bande-a-Bonnot/Boucle-framework (tools/read-once)** | https://github.com/Bande-a-Bonnot/Boucle-framework | MIT | **read-once**-PreToolUse-Hook: blockt/warnt bei Re-Read unveränderter Dateien ("~2000+ Token je verhindertem Re-Read"), 20-min-Expiry wegen Compaction, `READ_ONCE_MODE=deny`; weitere Guards (bash-guard, file-guard, git-safe, worktree-guard) | 0 / 1 / 0 | 4 |
| **wrsmith108/claude-md-optimizer** | https://github.com/wrsmith108/claude-md-optimizer | k.A. | Skill: CLAUDE.md/AGENTS.md auf <200 Zeilen via Progressive Disclosure (`@import`, `.claude/rules/*.md`) | 0 / 1 / 0 | 3 |
| **thepushkarp/handoff** | https://github.com/thepushkarp/handoff | MIT | PreCompact → `docs/handoff/HANDOFF.md`, SessionStart(compact) injiziert zurück, Stop-Hook erzwingt Ausfüllen | 0 / 0 / 1 | 3 |
| **Sonovore/claude-code-handoff** | https://github.com/Sonovore/claude-code-handoff | MIT | Live `session-state.md` via UserPromptSubmit + PostToolUse + PreCompact | 0 / 0 / 6 | 3 |
| **mvara-ai/precompact-hook** | https://github.com/mvara-ai/precompact-hook | k.A. | PreCompact ruft frische `claude`-Instanz für Recovery-Brief (kostet selbst Tokens) | 0 / 0 / 1 | 2 |
| **karanb192/claude-code-hooks** | https://github.com/karanb192/claude-code-hooks | MIT | 22 Hook-Plugins: `git-safety`, `protect-secrets`, `protect-tests`, `subagent-spawn-cap`, `context-hogs`, `cache-tax`, `instructions-audit`; "Token Diet" (3 Presets aus Bordmitteln: Read-Cap, Subagent-Modell…) + `bench/read-replay` | 1 / 8 / 78 | 5 |
| **kenryu42/cc-safety-net** | https://github.com/kenryu42/cc-safety-net | MIT | PreToolUse-Guard: parst Kommandos semantisch (nicht Regex), blockt destruktive git/fs-Befehle und Secret-Zugriffe; 13 CLIs | 0 / 5 / 1 | 4 |
| **loqimean/awesome-claude-code-hooks** | https://github.com/loqimean/awesome-claude-code-hooks | CC0 | Kuratierte Hook-Liste: Security, Observability, Session-Memory (claude-memory-compiler, deja-vu, Continuous-Claude-v3, Citadel, harness-scope) | – | 3 |
| **disler/claude-code-hooks-mastery** | https://github.com/disler/claude-code-hooks-mastery | k.A. | Alle Hook-Events mit Payloads, Meta-Agent, `/plan_w_team` (Team-Orchestrierung mit Stop-Hook-Validierung) | 20 (6 haiku/6 sonnet/9 opus) / 0 / 25 | 4 |
| **disler/claude-code-hooks-multi-agent-observability** | https://github.com/disler/claude-code-hooks-multi-agent-observability | k.A. | Hook → HTTP → Bun/SQLite → WebSocket → Vue: Echtzeit-Observability für mehrere Agents | 13 / 4 / 40 | 4 |
| **FlorianBruniaux/claude-code-ultimate-guide** | https://github.com/FlorianBruniaux/claude-code-ultimate-guide | (LICENSE vorhanden) | Umfassender Guide; `examples/hooks/` mit `rtk-auto-wrapper.sh`, Session-Summary (ccusage/rtk), LLM-as-Judge-Commit-Hook (~$0,01-0,05 mit Haiku); `guide/ops/ai-finops.md`, `ai-unit-economics.md`, `subscription-strategy.md` | 42 (23 haiku/37 sonnet/18 opus) / 99 / 69 | 4 |
| **TribeAI/claude-evals** | https://github.com/TribeAI/claude-evals | Apache-2.0 | Eval-Harness für Agent SDK: Hooks auf PreToolUse/PostToolUse/**SubagentStop**, LLM-Judge mit Rubrik (2 Durchläufe, Median), Modellvergleich "billigstes noch gutes Modell" | 0 / 0 / 0 | 4 |
| **bkper/claude-eval** | https://github.com/bkper/claude-eval | MIT | "TDD für Claude Code": Prompt auf Sonnet, Haiku urteilt PASS/FAIL je Kriterium | 0 / 0 / 0 | 3 |
| **wenxuec/llm-judge** | https://github.com/wenxuec/llm-judge | MIT | Skill: Rubrik, Judge-Prompts, Harness mit Content-Hash-Cache (nur Neues neu bewerten), Step-Attribution, Kalibrierung (Kappa) | 0 / 1 / 0 | 4 |
| **ryoppippi/ccusage** | https://github.com/ryoppippi/ccusage | MIT | `npx ccusage`: Kosten aus lokalen JSONL, daily/monthly/session/5h-blocks, `blocks --live`, Statusline | 0 / 17 / 0 | 4 |
| **Maciek-roboblog/Claude-Code-Usage-Monitor** | https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor | MIT | Live-Terminal-Monitor mit Burn-Rate und Zeit-bis-Limit | – | 3 |
| **musistudio/claude-code-router** | https://github.com/musistudio/claude-code-router | MIT | Lokales Gateway: Routing nach Szenario (default/background/think/longContext/webSearch), Fallbacks, Key-Rotation, Kosten-Logs; ~37,7k Stars [BLOG] | – | 3 |
| **daymade/claude-code-skills** | https://github.com/daymade/claude-code-skills | MIT | Skill-Marktplatz, `skill-creator`-Fork; CLAUDE.md beschreibt Lazy-Loading-Muster | 0 / 118 / 5 | 2 |
| Pimzino/claude-code-spec-workflow (vorh.) | https://github.com/Pimzino/claude-code-spec-workflow | MIT | Spec-Workflow (Requirements→Design→Tasks) mit Dashboard | – | 2 |
| alinaqi/claude-bootstrap (vorh.) | https://github.com/alinaqi/claude-bootstrap | MIT | Bootstrap mit Agents/Hooks/Rules/Evals | 7 (6 sonnet/1 inherit) / 73 / 5 | 2 |
| lyndonkl/claude (von anderem Crawler) | https://github.com/lyndonkl/claude | k.A. | 85 "orchestrating agents" (48 inherit/22 opus/15 sonnet) über 271 Skills; Muster "ein Orchestrator routet zu 14 Spezialisten" | 85 / 271 / 2 | 3 |
| Microck/ordinary-claude-skills (vorh.) | https://github.com/Microck/ordinary-claude-skills | k.A. | 2148 Skills, 27 Agents (18 haiku/18 sonnet/6 inherit) | 27 / 2148 / 2 | 2 |

Nicht geklont, aber in Suchen relevant (Hinweis): `Shopify`-internes "Helix" (Orchestrator + 4 Quality Gates, nur Blog), `coleam00/claude-memory-compiler`, `parcadei/Continuous-Claude-v3`, `SethGammon/Citadel` (Cost-Telemetrie), `dwarvesf/claude-guardrails`, `hahahahahahahahah6/agent-guard`, `kjetilfuras` "Koda" (15 Cron-Tasks/Tag auf Agent SDK + node-cron + pm2, nur Blog).

---

## Modell-Routing: was die Docs und die besten Repos konkret sagen

### 1. Subagent-Frontmatter `model:` [DOC https://code.claude.com/docs/en/sub-agents]
- Erlaubte Werte: `sonnet`, `opus`, `haiku`, `fable`, eine volle Modell-ID (z. B. `claude-opus-5-5`) oder `inherit`. Fehlt das Feld, greift die Auflösungsreihenfolge unten.
- Weitere kostenrelevante Felder: `effort: low|medium|high|xhigh|max` (überschreibt nicht `CLAUDE_CODE_EFFORT_LEVEL`), `maxTurns`, `autoCompactWindow` (100k–1M, v2.1.296+), `omitClaudeMd: true` (v2.1.271+, spart CLAUDE.md-Tokens im Subagent), `skills:` (Vollinhalt wird injiziert), `background: true`, `isolation: worktree`, `memory: user|project|local`, `experimental: {cacheTtl: 5m|1h}` (v2.1.248+).
- **Auflösungsreihenfolge (seit v2.1.251):** (1) per-Invocation-`model`-Parameter im Agent-Tool-Call → (2) `model`-Frontmatter (`inherit` = Hauptmodell) → (3) `CLAUDE_CODE_SUBAGENT_MODEL` → (4) Modell der Hauptkonversation. Ein Mod-`agent.spawn`-Hook kann (1) überschreiben. Vor v2.1.251 stand `CLAUDE_CODE_SUBAGENT_MODEL` an erster Stelle (das ist die Reihenfolge, die ältere Blogs noch zitieren [BLOG dev.to "Opus plans, Haiku executes"]).
- **Alles auf ein Modell zwingen:** `CLAUDE_CODE_SUBAGENT_MODEL=haiku` + `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` (v2.1.257+). Nur `_FORCE` ohne Modell → Hauptmodell; Explore behält sein Modell. `CLAUDE_CODE_SUBAGENT_MODEL` allein ändert Explore/Plan nicht.
- **Built-ins:** Explore = Hauptmodell (auf Subscriptions/Console mit Fable-Hauptmodell läuft Explore auf Opus-Alias), read-only, startet ohne CLAUDE.md/git-status, nicht resumierbar; Plan = inherit; general-purpose = `CLAUDE_CODE_SUBAGENT_MODEL` oder Hauptmodell; `statusline-setup` = Sonnet; `claude-code-guide` = Haiku. **Explore auf Haiku:** eigenen Agent `Explore` mit `model: haiku` definieren (überschreibt Built-in). Abschalten: `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` bzw. `permissions.deny: ["Agent(Explore)"]`, im SDK `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1`.
- Subagent-Beschreibungen kosten Kontext: Warnung ab 15 000 Token Gesamtgröße. Limits: `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (Default 20), `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (Default 3). Hinweis der Doc: Subagents "senden eigene Requests, die auf dieselben Usage-Limits zählen".
- Settings-Rule-Syntax erlaubt Deny/Ask auf Modellparameter: `Agent(model:opus)` [REPO shanraisshan `best-practice/claude-settings.md` Z. 333, zitiert Doc].

### 2. Hauptmodell, Aliase, Effort [DOC https://code.claude.com/docs/en/model-config]
- Aliase: `default`, `best`, `fable`, `sonnet`, `opus`, `haiku`, `sonnet[1m]`, `opus[1m]`, **`opusplan`** ("`opus` im Plan-Modus, `sonnet` in der Ausführung"). Auf der Anthropic API: `opus`→Opus 5.5, `sonnet`→Sonnet 5.5, `haiku`→Haiku 5.5.
- Priorität: `/model` > `claude --model` > `ANTHROPIC_MODEL` > `model` in settings.json > `ANTHROPIC_DEFAULT_MODEL` (v2.1.236+). Alias-Ziele: `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL` ("für `haiku` oder Hintergrundfunktionen"), `ANTHROPIC_DEFAULT_FABLE_MODEL`.
- Effort: Auflösung `CLAUDE_CODE_EFFORT_LEVEL`/`--effort`/`/effort` > `modelSettings`/`effortLevel` > Modell-Default (Default `medium` auf Opus 5.5/Sonnet 5.5/Haiku 5.5, sonst `high`). Doc-Aussage: "Opus 5.5 at `medium` effort matches or exceeds Opus 5 at `high`". Auto-Compact-Fenster: `/autocompact 500k`, `autoCompactWindow`, `CLAUDE_CODE_AUTO_COMPACT_WINDOW`; `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` hält 200k.
- Kostenhinweis Doc: Haiku 5.5 "costs more per token when its prompt is longer than 100K tokens"; Fable kann auf Usage-Credits gehen, in `-p` "bills it without asking".

### 3. Agent Teams und Workflows [DOC agent-teams, workflows]
- Teams: Modellwahl (1) Spawn-Prompt → (2) Subagent-Definition (`inherit` = Lead) → (3) `CLAUDE_CODE_SUBAGENT_MODEL` ≠ inherit → (4) Lead-Modell. `teammateDefaultModel` entfernt (v2.1.234). Teams nur interaktiv; in `-p`/SDK werden benannte Subagents normale Subagents. Cache der Teammates: 5 min TTL, `subagentPromptCacheTtl: 1h` möglich (teurere 1h-Writes). Quality-Gate-Hooks: `TeammateIdle`, `TaskCreated`, `TaskCompleted` (Exit 2 = Feedback + weiterarbeiten).
- Workflows (`agent()`, `pipeline()`, `parallel()`, `phase()`, Schema-Output): Modell je Stage zählt als per-Invocation-Modell; Fan-out teilt Prompt-Cache-Prefix (Stagger bis 5 s, `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS`); max. 16 gleichzeitige Agents (`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` 1-256), 1000 Agents/Run, "Large workflow"-Warnung ab 25 Agents oder 1,5 M projizierten Tokens; `workflowSizeGuideline: small|medium|large`. Workflows laufen auch unter `claude -p`/SDK (Freigabe via `Workflow`-Allow-Rule oder PreToolUse-Hook).

### 4. Kostenzahlen mit Quelle
| Aussage | Zahl | Quelle |
|---|---|---|
| Durchschnittskosten Claude Code (Enterprise) | ~$13/Entwickler/aktiver Tag, $150-250/Monat, 90 % unter $30/Tag | [DOC costs] |
| Hintergrund-Token (Resume-Summaries etc.) | typisch < $0,04 je Session | [DOC costs] |
| Agent Teams | "approximately 7x more tokens" wenn Teammates im Plan-Modus laufen; Token ~ proportional zur Teamgröße; Empfehlung "Use Sonnet for teammates" | [DOC costs] |
| Scheduled Tasks | jede Auslösung sendet den **vollen Kontext**; Cache-Lifetime 1 h (Subscription) / 5 min (API oder bei Usage-Credits) | [DOC costs, scheduled-tasks] |
| CLAUDE.md | "Aim to keep CLAUDE.md under 200 lines" | [DOC costs] |
| Hook-Preprocessing | 10 000-Zeilen-Log → nur ERROR-Zeilen: "tens of thousands of tokens to hundreds" | [DOC costs] |
| Preise Haiku 5.5 | $0,10 in / $0,50 out bis 100k Prompt, darüber $0,50/$2,50; Cache-Read $0,01 | [BLOG venturebeat/marktechpost, 2026-10-07; nicht gegen Preisseite geprüft] |
| Preise Sonnet 5.5 / Opus 5.5 | $2/$10 bzw. $4/$20; Opus-Cache-Read $0,20/M | [BLOG growthcab/tech-insider; README egorfedorov bestätigt $4/$20 und $0,20/M für Opus 5.5] |
| ECC-Empfehlung | `model: sonnet` + `CLAUDE_CODE_EFFORT_LEVEL=medium` + `CLAUDE_CODE_SUBAGENT_MODEL=haiku`; "Sonnet ~60 % Kostenreduktion vs Opus", "Haiku ~80 % billiger" | [REPO ECC `docs/token-optimization.md`] |
| ECC-Regel | "Haiku (90 % of Sonnet capability, 3x cost savings): Worker agents in multi-agent systems" | [REPO ECC `rules/common/performance.md`] |
| wshobson-Tiers | Opus = Architektur/Security/Review/Produktionscode; inherit = komplex, Nutzer wählt; Sonnet = Docs/Tests/Debugging; Haiku = "Fast ops, SEO, deployment, simple tasks" (24 haiku/70 sonnet/54 opus/52 inherit) | [REPO `wshobson_agents/ARCHITECTURE.md`, `docs/agents.md`] |
| DevTeam-Eskalation | `haiku_to_sonnet: 2`, `sonnet_to_opus: 2`, `opus_max_failures: 3` → Bug Council; Eco-Mode für Komplexität 1-6 | [REPO michael-harris README/`docs/GETTING_STARTED.md`] |
| TurboKach-Rollen | Executor = Sonnet 5.5 (Opus nur mit begründeter Plan-Markierung), Reviewer = Opus/medium, Merger = Sonnet/medium, Explorer = Sonnet/medium; Modell-Pin über `model:`-Parameter des Agent-Tools, nicht im Prompttext | [REPO `TurboKach__claude-code-setup/skills/agent-teams/SKILL.md` Z. 184-231] |
| robomello Router | Komplexität 1 (Format/Extraktion/Klassifikation) → haiku; 2 (Codegen, Summaries, "Default when uncertain") → sonnet; 3 (Multi-File, Architektur, Planung) → opus; alle API-Agents (etsy, printify, nocodb, telegram) auf haiku | [REPO `robomello__claude-code-setup/agents/model-router-agent.md`] |
| caveman Auto | 0,46× Kosten von Opus 5.5 xhigh bei 43,7 % vs 44,3 % gelösten Tasks (85 Tasks, Zwischenstand) | [REPO caveman README "Auto"] |
| Hermes Cron | Modell: per-Job-Pin → `cron.model` → Hauptmodell zum Auslösezeitpunkt; per-Job Effort `none…ultra`; No-Agent-Modus ohne LLM | [REPO hermes `website/docs/user-guide/features/cron.md`] |
| OpenClaw Cron | per-Job `--model`, `--thinking`, `--light-context`, `--tools`; Heartbeat: eigenes `model`, `lightContext`, `isolatedSession`, Default 30 min | [REPO openclaw `docs/automation/cron-jobs/payloads.md`, `docs/gateway/heartbeat.md`] |

---

## Token-Sparen: die 15 wirksamsten Maßnahmen (Quelle, behauptete Ersparnis)

1. **Subagents für Grunt-Work auf Haiku pinnen** (`model: haiku` im Frontmatter oder `CLAUDE_CODE_SUBAGENT_MODEL=haiku`), Verbose-Operationen (Tests, Logs, Doku-Fetch) in Subagents auslagern, nur Summary zurück. [DOC sub-agents/costs]; ECC: "Haiku ~80 % billiger" [REPO]; Beam/Blog: Haiku-Subagents ≈ 7 % der Rechnung [BLOG].
2. **Hauptmodell Sonnet statt Opus, `opusplan` für Planung** (Opus nur im Plan-Modus). [DOC model-config/costs]; ECC "~60 % Kostenreduktion" [REPO].
3. **Effort senken** (`/effort medium`, `CLAUDE_CODE_EFFORT_LEVEL`), Thinking-Budget (`MAX_THINKING_TOKENS`) bei Fixed-Budget-Modellen; Thinking-Tokens werden als Output abgerechnet, "tens of thousands of tokens per request" möglich. [DOC costs]
4. **`/clear` zwischen unabhängigen Tasks; lange Sessions vermeiden** – Doc: unerwartet hohe Kosten "usually traces back to long sessions that were never cleared or to Opus left as the default". usage-limit-reducer: "98,5 % der Tokens gehen oft an Re-Lesen der History" [REPO].
5. **Hook-Preprocessing von Tool-Output** (PreToolUse `updatedInput` → `| grep -A5 FAIL | head -100`): [DOC costs, mit Beispielscript]; rtk: Bash-Output "bis 90 % kleiner" [REPO rtk, mit Warnung, dass das nicht 1:1 Rechnung ist]; caveman "Read less": 33,2 % weniger Input-Token je Session, CSV/Logs/YAML je 98-99 % je Datei [REPO caveman Benchmarks]; context-mode: "315 KB → 5,4 KB" [REPO].
6. **Read-once / Read-Cache-Hooks** gegen Re-Reads unveränderter Dateien: Boucle read-once "~2000+ Token je verhindertem Re-Read" [REPO]; egorfedorov "30-50 % der Tokens verschwendet" [REPO]; alexgreensh Delta-Reads/Skeletons [REPO]; karanb192 `bench/read-replay` misst es vorher auf eigenen Transkripten [REPO].
7. **CLAUDE.md < 200 Zeilen, Spezialwissen in Skills (lazy) und `.claude/rules/*.md` mit `paths:`** (laden nur bei Treffer). [DOC costs: "Move instructions from CLAUDE.md to skills"]; wrsmith108 Skill automatisiert das; shanraisshan `why-harness-is-important.md` ("Lazy-loaded rules & memory"); TurboKach `global/rules/` [REPO].
8. **Output-Kompression / knappe Antworten** (caveman "Say less": 63→20 Token gleiche Antwort; JetBrains-A/B: 8,5 % weniger Output-Token ohne messbaren Qualitätsverlust; Adobe-Paper 1,4-2,4× billiger) [REPO caveman, verweist auf externe Studien – nicht selbst geprüft]; drona23 CLAUDE.md-Regeln [REPO].
9. **MCP-Overhead begrenzen**: Tool-Definitionen sind deferred, aber Server-Instruktionen kosten; CLI (`gh`, `aws`) statt MCP; `/mcp` zum Abschalten; ECC-Regel "unter 10 MCP-Server je Projekt". [DOC costs; REPO ECC]
10. **Strategisches statt automatisches Compacting** (nach Exploration/Meilenstein, nie mitten in Multi-File-Refactor), `/compact <Fokus>`, Compact-Instruktionen in CLAUDE.md. [DOC costs]; ECC `strategic-compact` Hook (PreToolUse Edit/Write) [REPO]; Handoff-Dateien (thepushkarp, Sonovore) statt teurer Compaction; ww-w-ai `/s-continue` "zero LLM calls" [REPO].
11. **Prompt-Cache warm halten**: Cache-Lifetime 1 h Subscription / 5 min API; Pause > TTL = voller Re-Read des Kontexts; `/usage` zeigt "Prompt cache (main)"-Zeile; Subagent-Cache per `subagentPromptCacheTtl` [DOC costs/agent-teams]; ww-w-ai "Token Guardian" warnt/blockt bei Cache-Expiry, "900K Token → $9 pro Miss" [REPO]; caveman "keeps the prompt cache warm while you pause" [REPO].
12. **Scheduled Tasks/Routinen schlank halten**: jede Auslösung schickt den vollen Session-Kontext → für Cron frische, kleine Sessions (`claude -p --bare`, `--max-turns`, `--max-budget-usd`, `--output-format json` mit `total_cost_usd`) statt `/loop` in einer fetten Session; `/loop` läuft 7 Tage ab; Cloud-Routinen min. 1 h. [DOC scheduled-tasks/headless]; OpenClaw `--light-context`/`isolatedSession`, Hermes No-Agent-Modus + Preflight ("a misconfigured job never spends tokens") [REPO].
13. **Subagent-Kontext schlank**: `omitClaudeMd: true`, kurze `description` (Warnung ab 15k Token Summe), `maxTurns`, nur nötige `tools:`, Spawn-Prompt "goal + boundaries, keine Prozedur" [DOC sub-agents; REPO TurboKach Spawn-Contract].
14. **Spezifische Prompts, Plan-Mode, früh abbrechen, Verifikationsziele mitgeben** – vermeidet "broad scanning" und Re-Work. [DOC costs]
15. **Agent Teams / Workflows nur bei echt parallelem Nutzen**: Teams ≈ 7× Token; Workflows mit `small`-Guideline (< 5 Agents) und Slice-Test vor Full-Run; Subagents (Ergebnis-Summary) statt Teams. [DOC costs/agent-teams/workflows]; TurboKach: "Fan-out uses significantly more tokens … not routine tasks" [REPO].

Ergänzend (Messen): `/usage` (Attribution je Skill/Subagent/MCP, Behavior-Flags ≥ 10 %, Loops-Zeilen v2.1.242+), `/context`, `/insights` [DOC]; `ccusage`, Claude-Code-Usage-Monitor, ECC `stop:cost-tracker` (`~/.claude/metrics/costs.jsonl`), disler Observability-Stack [REPO].

---

## Referenz-Architektur-Muster aus den Repos

| Muster | Beschreibung | Wer implementiert es (Pfad) |
|---|---|---|
| **Command → Agent (mit preloaded Skill) → Skill** | Slash-Command orchestriert, Agent holt Daten mit injiziertem Skill, unabhängiger Skill erzeugt Output | shanraisshan `orchestration-workflow/orchestration-workflow.md`, `.claude/commands/weather-orchestrator.md` |
| **Orchestrator/Worker (Lead → parallele Haiku-Worker → Analyst → Writer)** | Lead zerlegt in 2-4 Subthemen, Researcher parallel, Dateien als Übergabe (`files/research_notes/`) | anthropics `claude-agent-sdk-demos/research-agent/research_agent/agent.py` (Worker `model="haiku"`) |
| **Pipeline mit Quality Gates** | spec-orchestrator → analyst → architect → planner → Gate → Entwicklung → Gate; Orch-Pipeline Research-Plan-TDD-Review-Commit mit 2 Human-Gates (Plan-Approval, Commit-Confirm) | zhsama `agents/spec-agents/`; ECC `skills/orch-pipeline/SKILL.md`, `skills/plan-orchestrate/` |
| **Fan-out + Judge (Best-of-N)** | N Implementierungen parallel → unabhängige Reviewer → Meta-Judge pick/synthesize/reject | pejmanjohn `slot-machine/SKILL.md` + `references/`; fltman `templates/fanout-orchestrator.sh` |
| **Evaluator-Optimizer (Generator ≠ Critic)** | getrennter Kritiker (anderes Modell/Instruktion), Anker-Set, Drift-Monitoring | fltman `.claude/skills/loop-engineer/reference/guardrails.md`, `templates/evaluator-optimizer.sh`; ECC `skills/council/` (Skeptic/Pragmatist/Critic-Subagents); robomello `hooks/review_code.sh` (3-4 LLM Konsens) |
| **Model Escalation Ladder** | Task startet auf Haiku; nach N Fehlschlägen Sonnet, dann Opus, dann Bug Council; Eco-Mode | michael-harris `README.md` (`model_escalation:`), `agents/orchestration/`, `agent-registry.json` |
| **Router-Agent (billiges Modell klassifiziert, dann routet)** | Haiku-Agent schätzt Komplexität 1/2/3 und führt auf passendem Modell aus | robomello `agents/model-router-agent.md`; caveman "Auto"; TechNickAI `skills/smart-delegation/` |
| **Rolle→Modell-Matrix für Teams** | Explorer/Executor/Merger = Sonnet, Reviewer = Opus, Pin per Spawn-Parameter, Executor `isolation: worktree`, Plan-Approval-Gate | TurboKach `skills/agent-teams/SKILL.md`, `agents/team-executor.md`, `agents/team-reviewer.md` |
| **Subagent-Driven Development** | frischer Implementer-Subagent je Task, Review (Spec + Qualität) nach jedem Task, Abschluss-Review; "Rulings, not stalls" | obra `skills/subagent-driven-development/SKILL.md`, `skills/dispatching-parallel-agents/SKILL.md` |
| **Worker + zustandsloser Decision Proxy** | Worker (Agent-SDK-Session) auf Goal-File, Proxy entscheidet `continue/replan/escalate/stop`, Kill-Switch, Worktree je Task | marlinjai `orchestrator/`, `goals/`, `personas/` |
| **Cron-Routinen als Markdown-Tasks** | `.md` = Prompt + Cron-Expression, Agent SDK führt aus, Delivery an Chat | T0UGH `tasks/*.md`, `src/`; TechNickAI `workflows/*` (12 Stewards inkl. `cron-healthcheck`, `llm-usage-report`) |
| **Staged Writes + Human Approval (Commerce)** | Merchant-Agent: jede Schreibaktion (Listing, Restock, Preis, Kampagne) ist "staged change", Host-Approval-Surface wendet an; Gates/Fencing/Caps im Tool-Call | anthropics `commerce-agents/merchant-agent/core/` (change guardrails, gates), `docs/safety.md`; Shopify `claude-for-commerce-examples/merchant/` |
| **Spend/Write-Guard per PreToolUse (Exit 2)** | deterministisches Budget-Gate ("a budget in a prompt is advisory, an exit-2 hook is not"); read-only-Subagents; Telegram-Freigabe für gefährliche Calls | davila7 `cli-tool/components/hooks/doordash/doordash-spend-guard.json`, `security/subagent-read-only-guard.json`; robomello `hooks/telegram_confirm.py`; karanb192 `plugins/git-safety`, `protect-secrets`, `subagent-spawn-cap`; kenryu42 `cc-safety-net` |
| **Heartbeat + isolierte Cron-Jobs** | periodischer Main-Session-Turn (30 min) mit `HEARTBEAT.md`-Checkliste, "HEARTBEAT_OK" wird verworfen; isolierte Jobs mit eigenem Modell | openclaw `docs/gateway/heartbeat.md`, `docs/automation/cron-jobs/` (Repo gelöscht, Doku oben zusammengefasst); claw0 `s07` |
| **Handoff/Memory statt Compaction** | PreCompact → HANDOFF.md, SessionStart(compact) injiziert; Live-`session-state.md`; MEMORY.md mit hartem Zeichen-Cap (Hermes 2 200 Zeichen) | thepushkarp `handoff`, Sonovore `claude-code-handoff`, ECC `skills/unified-memory/`, `hooks/memory-persistence/` |
| **Eval-Harness mit SubagentStop-Hook** | Rubrik-Judge, Modellvergleich "billigstes noch ausreichendes Modell", Regression-Compare | TribeAI `claude-evals`; wenxuec `llm-judge` (Hash-Cache); bkper `claude-eval` |
| **Dynamic Workflows (Script hält den Plan)** | `agent()/pipeline()/parallel()` in `.claude/workflows/*.js`, Zwischenergebnisse im Script statt im Kontext, Resume, Schema-Output | [DOC workflows]; TurboKach-Skill verweist auf Workflows als Fan-out-Mechanismus; ECC `dmux-workflows` |

---

## Top-Repos/Skills zum Übernehmen (Pfad, was)

1. `affaan-m_everything-claude-code/docs/token-optimization.md` + `rules/common/performance.md` – fertige settings.json-Empfehlung (`sonnet` + `effort medium` + `CLAUDE_CODE_SUBAGENT_MODEL=haiku`), Modell-Matrix.
2. `affaan-m_everything-claude-code/skills/strategic-compact/` – PreToolUse-Hook, der `/compact` an logischen Grenzen vorschlägt.
3. `affaan-m_everything-claude-code/skills/cost-aware-llm-pipeline/SKILL.md` – Routing-Funktion nach Textlänge/Item-Zahl, Budget-Tracking, Retry, Caching (für eigene Pipeline-Skripte).
4. `affaan-m_everything-claude-code/skills/cost-tracking/` + `hooks/hooks.json` (`stop:cost-tracker`) – lokale Kosten-JSONL pro Session.
5. `affaan-m_everything-claude-code/skills/council/`, `skills/continuous-agent-loop/`, `skills/orch-pipeline/` – Entscheidungs-Council, Loop-Auswahl, gated Pipeline.
6. `michael-harris__claude-code-multi-agent-dev-system/README.md` + `agent-registry.json` – Escalation-Ladder-Konfiguration und Eco-Mode als Vorlage für "Haiku zuerst, Opus nur bei Fehlschlag".
7. `TurboKach__claude-code-setup/skills/agent-teams/SKILL.md` + `agents/team-*.md` – Rolle→Modell→Effort-Tabelle, Spawn-Prompt-Contract, Worktree-Isolation, Plan-Gate.
8. `robomello__claude-code-setup/agents/model-router-agent.md`, `agents/etsy-agent.md`, `agents/printify-agent.md`, `hooks/telegram_confirm.py` – Haiku-API-Agents und Chat-Approval-Gate (direkt E-Commerce-relevant).
9. `fltman__loop-engineer/.claude/skills/loop-engineer/` – Guardrail-Checkliste (Exit-Bedingung, Iterationscap im Code, `total_cost_usd`-Gate, getrennter Kritiker) + 5 Shell-Templates.
10. `pejmanjohn__slot-machine/SKILL.md` – Best-of-N mit Meta-Judge für kritische Artefakte (z. B. Produkttexte, Ad-Creatives).
11. `anthropics__commerce-agents/merchant-agent/core/` + `docs/safety.md` – Staged-Change-Gate als Referenz für alle Shop-Schreibaktionen; `merchant-agent/managed-agents/` Scheduled Digest.
12. `karanb192__claude-code-hooks/docs/token-diet.md` + `bench/read-replay/` + Plugins `subagent-spawn-cap`, `context-hogs`, `cache-tax`, `git-safety`, `protect-secrets`.
13. `Bande-a-Bonnot__Boucle-framework/tools/read-once/` – Read-once-Hook (warn-Modus empfohlen; deny hat bekannten Bug nach Compaction, Issue llmenv #2381 [BLOG]).
14. `juliusbrussee_caveman/` (`hooks/`, `agents/`, `benchmarks/`) – Read-less-Filter und Say-less-Skill; Auto-Routing optional (benötigt Account).
15. `rtk-ai_rtk/hooks/claude/rtk-rewrite.sh` – transparenter Bash-Rewrite; FlorianBruniaux `examples/hooks/bash/rtk-auto-wrapper.sh`.
16. `davila7_claude-code-templates/cli-tool/components/hooks/doordash/doordash-spend-guard.json` + `security/subagent-read-only-guard.json` – Vorlage für ein Ausgaben-/Schreib-Gate per Exit 2.
17. `anthropics__claude-agent-sdk-demos/research-agent/` – minimaler SDK-Orchestrator mit `model="haiku"`-Workern (Vorlage für Research-/Crawl-Routinen).
18. `T0UGH__agent-cron/` – Cron-Tasks als Markdown; `TechNickAI__openclaw-config/workflows/cron-healthcheck/`, `llm-usage-report/` – Selbstüberwachung von Cron-Jobs und täglicher Kostenreport.
19. `TribeAI__claude-evals/` + `wenxuec__llm-judge/` – Rubrik-Evals mit SubagentStop-Hook bzw. Hash-Cache für Output-QA.
20. `thepushkarp__handoff/` oder `Sonovore__claude-code-handoff/` – Handoff-Datei statt teurer Compaction; `wrsmith108__claude-md-optimizer/` zum Schrumpfen der CLAUDE.md.
21. `ryoppippi__ccusage/` – `npx ccusage blocks --live` / Statusline für Kosten-Sichtbarkeit; `Maciek-roboblog__Claude-Code-Usage-Monitor/` für Burn-Rate.
22. `wshobson_agents/ARCHITECTURE.md`, `docs/agents.md` – Tier-Definitionen und Auswahlkriterien (Haiku: "well-defined specifications, established patterns, customer support responses, SEO, deployment").
23. `shanraisshan_claude-code-best-practice/reports/why-harness-is-important.md`, `best-practice/claude-subagents.md`, `agent-teams/` – kompakte Referenz der Harness-Mechanismen und Agent-Team-Demo mit `model: haiku` + `maxTurns: 3`.
24. `obra_superpowers/skills/subagent-driven-development/`, `dispatching-parallel-agents/` – Vorgehensmodell für frische Subagents je Task.

---

## Lücken

- **Kein Repo liefert eine komplette, lauffähige "E-Commerce-Business-Routine"** (Orchestrator + Modell-Routing + Cron + Approval-Gates) – nur Bausteine: commerce-agents (Gates, kein Scheduling außer Managed-Agents-Digest), robomello (Haiku-API-Agents, Telegram-Gate, aber ohne Lizenz und projektspezifisch), DevTeam (Escalation, aber Software-Dev-fokussiert).
- **Unabhängige Kosten-Benchmarks fehlen fast völlig**: die meisten %-Angaben (rtk 90 %, context-mode 98 %, ai-context-stack 80-90 %, TokenRoll 83 %, ww-w-ai 45 %) sind Eigenangaben; einzig caveman verweist auf externe A/B-Tests (JetBrains, Adobe) und veröffentlicht Rohdaten (`benchmarks/results`), ebenfalls nicht hier reproduziert. Die Doc nennt nur Enterprise-Durchschnitte und das 7×-Teams-Verhältnis.
- **Preistabelle** der 5.5-Modelle nur aus Blogs/README (Haiku-5.5-100k-Stufe); offizielle Preisseite nicht gefetcht.
- **Scheduled Tasks in Claude Code sind sessiongebunden** (7-Tage-Expiry, volle Kontext-Resendung); dauerhafte Routinen brauchen Cloud-Routines (min. 1 h), Desktop-Tasks, GitHub Actions oder externe Runner (agent-cron, pm2/node-cron). Ein Repo, das Claude-Cloud-Routines programmatisch verwaltet, wurde nicht gefunden.
- **Dry-Run-Muster für Write-Actions** ist in keiner Doc/kein Repo als Standard beschrieben; nähere Annäherungen: PreToolUse-Deny mit Begründung, Staged-Changes (commerce-agents), Telegram-Freigabe (robomello), `permissionMode: plan` für read-only-Subagents.
- **read-once/deny-Modus** kollidiert mit Compaction (Issue in llmenv #2381) – nur warn-Modus sicher.
- Hermes/OpenClaw sind > 150 MB und wurden nach Doku-Extraktion gelöscht; Code-Details (z. B. Hermes `cronjob_manage`-Implementierung) sind damit nicht lokal verfügbar.
- Lizenzlücken: robomello, T0UGH/agent-cron, marlinjai/orchestrator, disler (beide), mvara-ai, wrsmith108, TechNickAI, aandersen2323, TokenRollAI, sweetpotating haben keine LICENSE-Datei → nur als Referenz, nicht kopieren.
- `hesreallyhim/awesome-claude-code` ist CC BY-NC-ND – Inhalte nicht ableiten/weiterverbreiten.
- GitHub-API war gesperrt, daher keine Star-/Aktivitätsprüfung; Stale-Status einzelner kleiner Repos unbekannt.

---

## Quellen

Offizielle Docs (WebFetch, 2026-10-15):
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/costs
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/workflows
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/headless

WebSearch (22 Abfragen, "extended"), u. a. ausgewertete Treffer:
- https://github.com/michael-harris/claude-code-multi-agent-dev-system
- https://dev.to/max_quimby/opus-plans-haiku-executes-the-agent-cost-stack-13h0
- https://beam.ai/agentic-insights/claude-haiku-5-5-subagents
- https://computingforgeeks.com/reduce-claude-code-token-usage-tools/
- https://www.deployhq.com/blog/free-github-repos-for-claude-code
- https://github.com/egorfedorov/claude-context-optimizer , https://github.com/alexgreensh/token-optimizer , https://github.com/mksglu/context-mode , https://github.com/ww-w-ai/claude-code-token-saver
- https://github.com/T0UGH/agent-cron , https://github.com/tonybentley/claude-mcp-scheduler
- https://dev.to/nick_t_eac6be7ee8e88de2f3/i-handed-a-tiny-business-to-claude-code-agents-on-a-cron-schedule-heres-the-architecture-2615
- https://kjetilfuras.com/run-claude-agent-on-schedule/
- https://github.com/NousResearch/hermes-agent , https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron
- https://github.com/TechNickAI/openclaw-config , https://github.com/shareAI-lab/claw0 , https://saulius.io/blog/openclaw-autonomous-ai-agent-framework-heartbeat-monitoring
- https://github.com/loqimean/awesome-claude-code-hooks , https://github.com/karanb192/claude-code-hooks , https://github.com/kenryu42/cc-safety-net
- https://github.com/thedotmack/claude-mem
- https://github.com/ccusage/ccusage , https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor
- https://github.com/anthropics/claude-agent-sdk-demos , https://github.com/marlinjai/orchestrator
- https://github.com/wrsmith108/claude-md-optimizer
- https://github.com/musistudio/claude-code-router
- https://github.com/wenxuec/llm-judge , https://github.com/TribeAI/claude-evals , https://github.com/bkper/claude-eval
- https://github.com/Shopify/claude-for-commerce-examples , https://github.com/anthropics/commerce-agents , https://agentconn.com/blog/shopify-claude-code-orchestrator-gates/
- https://venturebeat.com/technology/anthropic-launches-claude-haiku-5-5-with-90-api-price-reduction-matching-gpt-6-luna , https://www.marktechpost.com/2026/10/07/anthropic-releases-claude-haiku-5-5-a-small-model-with-1m-context-priced-at-0-10-per-million-input-tokens/ , https://www.growthcab.com/claude-opus-api-pricing
- https://github.com/Bande-a-Bonnot/Boucle-framework/tree/main/tools/read-once , https://github.com/phaedrus1992/llmenv/issues/2381
- https://github.com/disler/claude-code-hooks-mastery , https://github.com/disler/claude-code-hooks-multi-agent-observability
- https://github.com/thepushkarp/handoff , https://github.com/Sonovore/claude-code-handoff , https://github.com/mvara-ai/precompact-hook , https://github.com/anthropics/claude-code/issues/43733
- https://backgroundclaude.com/blog/github-actions , https://agentpatterns.ai/workflows/headless-claude-ci/ , https://www.swareco.com/blog/claude-code-headless-mode
- https://github.com/TurboKach/claude-code-setup , https://github.com/pejmanjohn/slot-machine , https://github.com/fltman/loop-engineer

Lokal inspizierte Repo-Dateien: siehe Pfadangaben in den Tabellen oben.
