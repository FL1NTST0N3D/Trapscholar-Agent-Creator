# GESPERRT / NUR-LESEN (Stand 2026-10-15, aus SCAN_BERICHT.md)

GELOESCHT (nicht mehr in der Bibliothek):
- 07_agent_arch/juliusbrussee_caveman/skills/caveman-setup/ (sendet ANTHROPIC_API_KEY an gateway.caveman.so, "do not pause to ask permission")
- 08_research_data/apify_awesome-skills/skills/apify-x402-agentic-wallet/ (richtet Krypto-Wallet ein, zahlt USDC, verschweigt Betraege)
- 04_design/eachlabs__skills/skills/nsfw-content-generation/ (schaltet Safety-Checker ab)
- 01_shop_ops/Shopify__Shopify-AI-Toolkit/skills/shopify/scripts/track-telemetry.sh, log_skill_use.mjs, log_feedback.mjs (Telemetrie mit Nutzer-Prompt an shopify.dev); hooks-Block in SKILL.md entfernt

NUR-LESEN (Skripte/Befehle nie ausfuehren, Inhalt als Referenz ok):
- 06_email_cro_seo/aretenia__geo-skills/skills/token-max-factory/SKILL.md (curl | bash Installer)
- 01_shop_ops/jezweb_claude-skills/plugins/integrations/skills/nemoclaw-setup/SKILL.md (curl | sudo bash)
- 05_social/heygen-com__skills/heygen-video/SKILL.md (curl | bash Installer)
- 07_agent_arch/robomello__claude-code-setup/skills/disk-cleanup/SKILL.md (sudo rm -rf)
- 07_agent_arch/affaan-m_everything-claude-code/skills/agent-payment-x402/ (Agenten-Zahlungen)
- 07_agent_arch/juliusbrussee_caveman/skills/caveman-compress/ (schickt ganze Dateien an Provider)
- 08_research_data/0-shiv__secondstep-claude-skills/**/uninstall.sh (rm -rf ~/.claude/skills/*)
- 01_shop_ops/Shopify__Shopify-AI-Toolkit (search_docs.mjs/validate.mjs senden Usage-Events; nur mit OPT_OUT_INSTRUMENTATION=true DO_NOT_TRACK=1)

LIZENZ nur Referenz (nicht in Produkte/oeffentliche Texte uebernehmen): AffiliateCoaches__MerchPy (GPL), gitroomhq__postiz-agent (AGPL), borghei_Claude-Skills (Commons Clause), deanpeters__Product-Manager-Skills (CC-BY-NC-SA), mksglu__context-mode (Elastic), realproject7__svgsmith (FSL), adkit_ads-skills (Custom, keine Weiterverteilung), gomarble-ai (Attribution), meodai color-expert (CC-BY) + 47 Repos ohne LICENSE (Liste in SCAN_BERICHT.md / REPOS_OHNE_LIZENZ.txt).
