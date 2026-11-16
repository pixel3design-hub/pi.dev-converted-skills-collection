# Conversion report

Sources: `.upstream`, `.upstream-extra` · skills converted: 395 · duplicates skipped: 23

## Rule hits

| rule | occurrences |
|---|---|
| `command:namespace` | 547 |
| `host:Claude` | 390 |
| `path:project-dir` | 231 |
| `host:Claude Code` | 175 |
| `path:user-dir` | 132 |
| `file:CLAUDE.md` | 119 |
| `path:cross-skill` | 113 |
| `path:skill_path` | 52 |
| `path:project-skills` | 36 |
| `path:user-skills` | 32 |
| `tool:backtick` | 22 |
| `arg:ARGUMENTS` | 16 |
| `host:claude` | 14 |
| `path:user-context` | 8 |
| `path:plugin-root-unresolved` | 8 |
| `tool:phrase` | 4 |
| `file:CLAUDE.local.md` | 3 |
| `env:config-dir` | 3 |

## Duplicates skipped

- `.upstream/c-level-advisor/skills/arquiteto-de-empresa` -> skipped, duplicate of `.upstream/c-level-advisor/arquiteto-de-empresa/skills/arquiteto-de-empresa` (identical mirror)
- `.upstream/c-level-advisor/skills/chief-ai-officer-advisor` -> skipped, duplicate of `.upstream/c-level-advisor/chief-ai-officer-advisor/skills/chief-ai-officer-advisor` (identical mirror)
- `.upstream/c-level-advisor/skills/chief-customer-officer-advisor` -> skipped, duplicate of `.upstream/c-level-advisor/chief-customer-officer-advisor/skills/chief-customer-officer-advisor` (identical mirror)
- `.upstream/c-level-advisor/skills/chief-data-officer-advisor` -> skipped, duplicate of `.upstream/c-level-advisor/chief-data-officer-advisor/skills/chief-data-officer-advisor` (identical mirror)
- `.upstream/c-level-advisor/skills/general-counsel-advisor` -> skipped, duplicate of `.upstream/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor` (identical mirror)
- `.upstream/c-level-advisor/vpe-advisor/skills/vpe-advisor` -> skipped, duplicate of `.upstream/c-level-advisor/skills/vpe-advisor` (identical mirror)
- `.upstream/engineering/skills/agent-regression-evals` -> skipped, duplicate of `.upstream/engineering/agent-regression-evals/skills/agent-regression-evals` (identical mirror)
- `.upstream/engineering/skills/agent-run-forensics` -> skipped, duplicate of `.upstream/engineering/agent-run-forensics/skills/agent-run-forensics` (identical mirror)
- `.upstream/engineering/skills/chaos-engineering` -> skipped, duplicate of `.upstream/engineering/chaos-engineering/skills/chaos-engineering` (identical mirror)
- `.upstream/engineering/skills/coding-agent-rollout` -> skipped, duplicate of `.upstream/engineering/coding-agent-rollout/skills/coding-agent-rollout` (identical mirror)
- `.upstream/engineering/skills/commit-craft` -> skipped, duplicate of `.upstream/engineering/commit-craft/skills/commit-craft` (identical mirror)
- `.upstream/engineering/skills/feature-flags-architect` -> skipped, duplicate of `.upstream/engineering/feature-flags-architect/skills/feature-flags-architect` (identical mirror)
- `.upstream/engineering/skills/i18n-localization` -> skipped, duplicate of `.upstream/engineering/i18n-localization/skills/i18n-localization` (identical mirror)
- `.upstream/engineering/skills/kubernetes-operator` -> skipped, duplicate of `.upstream/engineering/kubernetes-operator/skills/kubernetes-operator` (identical mirror)
- `.upstream/engineering/slo-architect/skills/slo-architect` -> skipped, duplicate of `.upstream/engineering/skills/slo-architect` (identical mirror)
- `.upstream/finance/skills/month-end-close` -> skipped, duplicate of `.upstream/finance/month-end-close/skills/month-end-close` (identical mirror)
- `.upstream/product-team/skills/design-qa` -> skipped, duplicate of `.upstream/product-team/design-qa/skills/design-qa` (identical mirror)
- `.upstream/ra-qm-team/skills/access-lifecycle` -> skipped, duplicate of `.upstream/ra-qm-team/access-lifecycle/skills/access-lifecycle` (identical mirror)
- `.upstream/ra-qm-team/skills/cmmc-readiness` -> skipped, duplicate of `.upstream/ra-qm-team/cmmc-readiness/skills/cmmc-readiness` (identical mirror)
- `.upstream/ra-qm-team/skills/cra-readiness` -> skipped, duplicate of `.upstream/ra-qm-team/cra-readiness/skills/cra-readiness` (identical mirror)
- `.upstream/ra-qm-team/skills/eu-ai-act-specialist` -> skipped, duplicate of `.upstream/ra-qm-team/compliance-team-eu-ai-act/skills/eu-ai-act-specialist` (identical mirror)
- `.upstream/ra-qm-team/skills/iso42001-specialist` -> skipped, duplicate of `.upstream/ra-qm-team/compliance-team-iso42001/skills/iso42001-specialist` (identical mirror)
- `.upstream/ra-qm-team/skills/medical-device-software` -> skipped, duplicate of `.upstream/ra-qm-team/medical-device-software/skills/medical-device-software` (identical mirror)

## Per skill

| skill | source | files | rules applied | notes |
|---|---|---|---|---|
| `agent-launcher-orchestrator` | `.upstream/agent-launcher/skills/agent-launcher-orchestrator` | 4 | host:Claude×1 | dropped `context` |
| `grade-iterate` | `.upstream/agent-launcher/skills/grade-iterate` | 4 | — | — |
| `interview` | `.upstream/agent-launcher/skills/interview` | 4 | host:Claude×1 | — |
| `run-without-you` | `.upstream/agent-launcher/skills/run-without-you` | 4 | — | — |
| `stage-launch` | `.upstream/agent-launcher/skills/stage-launch` | 4 | — | — |
| `wrap-up` | `.upstream/agent-launcher/skills/wrap-up` | 4 | — | — |
| `business-growth-skills` | `.upstream/business-growth/skills/business-growth-skills` | 0 | — | — |
| `contract-and-proposal-writer` | `.upstream/business-growth/skills/contract-and-proposal-writer` | 0 | — | — |
| `customer-success-manager` | `.upstream/business-growth/skills/customer-success-manager` | 12 | — | — |
| `revenue-operations` | `.upstream/business-growth/skills/revenue-operations` | 13 | — | — |
| `sales-engineer` | `.upstream/business-growth/skills/sales-engineer` | 11 | — | — |
| `business-operations-skills` | `.upstream/business-operations/skills/business-operations-skills` | 0 | — | dropped `context` |
| `capacity-planner` | `.upstream/business-operations/skills/capacity-planner` | 7 | — | — |
| `internal-comms` | `.upstream/business-operations/skills/internal-comms` | 7 | — | — |
| `knowledge-ops` | `.upstream/business-operations/skills/knowledge-ops` | 8 | — | dropped `context` |
| `process-mapper` | `.upstream/business-operations/skills/process-mapper` | 7 | — | — |
| `procurement-optimizer` | `.upstream/business-operations/skills/procurement-optimizer` | 7 | — | — |
| `vendor-management` | `.upstream/business-operations/skills/vendor-management` | 7 | — | dropped `context` |
| `arquiteto-de-empresa` | `.upstream/c-level-advisor/arquiteto-de-empresa/skills/arquiteto-de-empresa` | 14 | host:Claude×1, host:Claude Code×1 | — |
| `chief-ai-officer-advisor` | `.upstream/c-level-advisor/chief-ai-officer-advisor/skills/chief-ai-officer-advisor` | 7 | command:namespace×5, host:Claude×11 | — |
| `chief-customer-officer-advisor` | `.upstream/c-level-advisor/chief-customer-officer-advisor/skills/chief-customer-officer-advisor` | 7 | — | — |
| `chief-data-officer-advisor` | `.upstream/c-level-advisor/chief-data-officer-advisor/skills/chief-data-officer-advisor` | 7 | command:namespace×5 | — |
| `board-prep` | `.upstream/c-level-advisor/executive-mentor/skills/board-prep` | 0 | command:namespace×2 | — |
| `challenge` | `.upstream/c-level-advisor/executive-mentor/skills/challenge` | 0 | command:namespace×3 | — |
| `executive-mentor` | `.upstream/c-level-advisor/executive-mentor/skills/executive-mentor` | 5 | command:namespace×11 | — |
| `hard-call` | `.upstream/c-level-advisor/executive-mentor/skills/hard-call` | 0 | command:namespace×2 | — |
| `postmortem` | `.upstream/c-level-advisor/executive-mentor/skills/postmortem` | 0 | command:namespace×2 | — |
| `stress-test` | `.upstream/c-level-advisor/executive-mentor/skills/stress-test` | 0 | command:namespace×2 | — |
| `general-counsel-advisor` | `.upstream/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor` | 5 | command:namespace×5 | — |
| `agent-protocol` | `.upstream/c-level-advisor/skills/agent-protocol` | 1 | command:namespace×4, path:project-dir×3, path:user-dir×3 | — |
| `board-deck-builder` | `.upstream/c-level-advisor/skills/board-deck-builder` | 2 | — | — |
| `board-meeting` | `.upstream/c-level-advisor/skills/board-meeting` | 3 | command:namespace×6, path:project-dir×14, path:user-dir×14 | — |
| `c-level-skills` | `.upstream/c-level-advisor/skills/c-level-skills` | 0 | command:namespace×1, file:CLAUDE.md×1, path:project-dir×2, path:user-dir×2 | — |
| `ceo-advisor` | `.upstream/c-level-advisor/skills/ceo-advisor` | 5 | — | — |
| `cfo-advisor` | `.upstream/c-level-advisor/skills/cfo-advisor` | 6 | — | — |
| `change-management` | `.upstream/c-level-advisor/skills/change-management` | 1 | — | — |
| `chief-of-staff` | `.upstream/c-level-advisor/skills/chief-of-staff` | 2 | command:namespace×1, path:project-dir×5, path:user-dir×5 | — |
| `chro-advisor` | `.upstream/c-level-advisor/skills/chro-advisor` | 5 | — | — |
| `ciso-advisor` | `.upstream/c-level-advisor/skills/ciso-advisor` | 5 | — | — |
| `cmo-advisor` | `.upstream/c-level-advisor/skills/cmo-advisor` | 5 | — | — |
| `company-os` | `.upstream/c-level-advisor/skills/company-os` | 2 | — | — |
| `competitive-intel` | `.upstream/c-level-advisor/skills/competitive-intel` | 2 | — | — |
| `context-engine` | `.upstream/c-level-advisor/skills/context-engine` | 1 | path:project-dir×3, path:user-dir×3 | — |
| `coo-advisor` | `.upstream/c-level-advisor/skills/coo-advisor` | 5 | — | — |
| `cpo-advisor` | `.upstream/c-level-advisor/skills/cpo-advisor` | 5 | — | — |
| `cro-advisor` | `.upstream/c-level-advisor/skills/cro-advisor` | 5 | — | — |
| `cs-onboard` | `.upstream/c-level-advisor/skills/cs-onboard` | 2 | path:project-dir×3, path:user-dir×3 | — |
| `cto-advisor` | `.upstream/c-level-advisor/skills/cto-advisor` | 5 | — | — |
| `culture-architect` | `.upstream/c-level-advisor/skills/culture-architect` | 2 | — | — |
| `decision-logger` | `.upstream/c-level-advisor/skills/decision-logger` | 2 | command:namespace×1, path:project-dir×11, path:user-dir×11 | — |
| `founder-coach` | `.upstream/c-level-advisor/skills/founder-coach` | 2 | — | — |
| `internal-narrative` | `.upstream/c-level-advisor/skills/internal-narrative` | 2 | — | — |
| `intl-expansion` | `.upstream/c-level-advisor/skills/intl-expansion` | 2 | — | — |
| `ma-playbook` | `.upstream/c-level-advisor/skills/ma-playbook` | 2 | — | — |
| `org-health-diagnostic` | `.upstream/c-level-advisor/skills/org-health-diagnostic` | 2 | — | — |
| `scenario-war-room` | `.upstream/c-level-advisor/skills/scenario-war-room` | 2 | command:namespace×1 | — |
| `strategic-alignment` | `.upstream/c-level-advisor/skills/strategic-alignment` | 2 | — | — |
| `vpe-advisor` | `.upstream/c-level-advisor/skills/vpe-advisor` | 7 | command:namespace×1 | — |
| `boardroom` | `.upstream/c-level-agents/skills/boardroom` | 0 | command:namespace×21, path:cross-skill×2, path:project-dir×2, path:user-dir×2 | — |
| `brief` | `.upstream/c-level-agents/skills/brief` | 0 | command:namespace×15, path:cross-skill×2, path:project-dir×3, path:user-dir×3 | — |
| `c-level-agents` | `.upstream/c-level-agents/skills/c-level-agents` | 0 | command:namespace×29, host:Claude×1, path:cross-skill×1 | — |
| `caio-review` | `.upstream/c-level-agents/skills/caio-review` | 0 | command:namespace×9, path:cross-skill×5 | — |
| `cco-review` | `.upstream/c-level-agents/skills/cco-review` | 0 | command:namespace×8, path:cross-skill×4 | — |
| `cdo-review` | `.upstream/c-level-agents/skills/cdo-review` | 0 | command:namespace×8, path:cross-skill×6 | — |
| `cfo-review` | `.upstream/c-level-agents/skills/cfo-review` | 0 | command:namespace×6, path:cross-skill×4 | — |
| `ciso-review` | `.upstream/c-level-agents/skills/ciso-review` | 0 | command:namespace×7, path:cross-skill×3 | — |
| `cmo-review` | `.upstream/c-level-agents/skills/cmo-review` | 0 | command:namespace×6, path:cross-skill×3 | — |
| `cpo-review` | `.upstream/c-level-agents/skills/cpo-review` | 0 | command:namespace×6, path:cross-skill×3 | — |
| `cro-review` | `.upstream/c-level-agents/skills/cro-review` | 0 | command:namespace×7, path:cross-skill×3 | — |
| `cross-eval` | `.upstream/c-level-agents/skills/cross-eval` | 0 | command:namespace×6, host:Claude×5, path:cross-skill×2, path:project-dir×1, path:user-dir×1 | — |
| `cto-review` | `.upstream/c-level-agents/skills/cto-review` | 0 | command:namespace×7, path:cross-skill×3 | — |
| `decide` | `.upstream/c-level-agents/skills/decide` | 0 | command:namespace×17, path:cross-skill×1, path:project-dir×3, path:user-dir×3 | — |
| `execute` | `.upstream/c-level-agents/skills/execute` | 0 | command:namespace×13, path:cross-skill×3, path:project-dir×1, path:user-dir×1 | — |
| `founder-mode` | `.upstream/c-level-agents/skills/founder-mode` | 0 | command:namespace×20, path:cross-skill×2, path:project-dir×2, path:user-dir×2 | — |
| `freeze` | `.upstream/c-level-agents/skills/freeze` | 0 | command:namespace×10, path:cross-skill×1, path:project-dir×1, path:user-dir×1 | — |
| `gc-review` | `.upstream/c-level-agents/skills/gc-review` | 0 | command:namespace×6, path:cross-skill×5 | — |
| `office-hours` | `.upstream/c-level-agents/skills/office-hours` | 0 | command:namespace×10, host:Claude×1, host:Claude Code×1 | — |
| `onboard` | `.upstream/c-level-agents/skills/onboard` | 0 | command:namespace×2, path:cross-skill×4, path:project-dir×8, path:user-dir×8 | — |
| `post-mortem` | `.upstream/c-level-agents/skills/post-mortem` | 0 | command:namespace×18, path:cross-skill×2, path:project-dir×1, path:user-dir×1 | — |
| `vpe-review` | `.upstream/c-level-agents/skills/vpe-review` | 0 | command:namespace×8, path:cross-skill×4 | — |
| `channel-economics` | `.upstream/commercial/skills/channel-economics` | 7 | — | — |
| `commercial-forecaster` | `.upstream/commercial/skills/commercial-forecaster` | 7 | — | — |
| `commercial-policy` | `.upstream/commercial/skills/commercial-policy` | 7 | — | — |
| `commercial-skills` | `.upstream/commercial/skills/commercial-skills` | 0 | — | dropped `context` |
| `deal-desk` | `.upstream/commercial/skills/deal-desk` | 7 | — | — |
| `partnerships-architect` | `.upstream/commercial/skills/partnerships-architect` | 7 | — | — |
| `pricing-strategist` | `.upstream/commercial/skills/pricing-strategist` | 7 | — | — |
| `rfp-responder` | `.upstream/commercial/skills/rfp-responder` | 7 | — | dropped `context` |
| `ai-act-readiness` | `.upstream/compliance-os/skills/ai-act-readiness` | 0 | command:namespace×8, path:cross-skill×5 | — |
| `aims-audit` | `.upstream/compliance-os/skills/aims-audit` | 0 | command:namespace×9, path:cross-skill×4 | — |
| `compliance-os` | `.upstream/compliance-os/skills/compliance-os` | 13 | path:cross-skill×13 | — |
| `compliance-readiness` | `.upstream/compliance-os/skills/compliance-readiness` | 0 | command:namespace×10, path:cross-skill×5 | — |
| `fda-qsr-audit-prep` | `.upstream/compliance-os/skills/fda-qsr-audit-prep` | 0 | command:namespace×7, path:cross-skill×4 | — |
| `gdpr-audit-prep` | `.upstream/compliance-os/skills/gdpr-audit-prep` | 0 | command:namespace×8, path:cross-skill×5 | — |
| `iso13485-audit-prep` | `.upstream/compliance-os/skills/iso13485-audit-prep` | 0 | command:namespace×9, path:cross-skill×5 | — |
| `iso27001-audit-prep` | `.upstream/compliance-os/skills/iso27001-audit-prep` | 0 | command:namespace×9, path:cross-skill×4 | — |
| `soc2-audit-prep` | `.upstream/compliance-os/skills/soc2-audit-prep` | 0 | command:namespace×7, path:cross-skill×5 | — |
| `a11y-audit` | `.upstream/engineering-team/a11y-audit/skills/a11y-audit` | 15 | command:namespace×1 | — |
| `google-workspace-cli` | `.upstream/engineering-team/google-workspace-cli/skills/google-workspace-cli` | 10 | — | — |
| `browserstack` | `.upstream/engineering-team/playwright-pro/skills/browserstack` | 0 | command:namespace×6, file:CLAUDE.md×1 | — |
| `coverage` | `.upstream/engineering-team/playwright-pro/skills/coverage` | 0 | command:namespace×1 | — |
| `fix` | `.upstream/engineering-team/playwright-pro/skills/fix` | 1 | arg:ARGUMENTS×1 | — |
| `generate` | `.upstream/engineering-team/playwright-pro/skills/generate` | 1 | arg:ARGUMENTS×2 | — |
| `migrate` | `.upstream/engineering-team/playwright-pro/skills/migrate` | 2 | arg:ARGUMENTS×1, command:namespace×1 | — |
| `pw` | `.upstream/engineering-team/playwright-pro/skills/pw` | 62 | command:namespace×25, file:CLAUDE.md×1, host:Claude×1, host:Claude Code×1 | — |
| `pw-init` | `.upstream/engineering-team/playwright-pro/skills/pw-init` | 0 | — | — |
| `pw-review` | `.upstream/engineering-team/playwright-pro/skills/pw-review` | 1 | arg:ARGUMENTS×1, tool:backtick×1 | — |
| `report` | `.upstream/engineering-team/playwright-pro/skills/report` | 0 | command:namespace×2 | — |
| `testrail` | `.upstream/engineering-team/playwright-pro/skills/testrail` | 0 | command:namespace×6, file:CLAUDE.md×1 | — |
| `extract` | `.upstream/engineering-team/self-improving-agent/skills/extract` | 0 | command:namespace×8, host:Claude×2, host:Claude Code×2, host:claude×3, path:project-dir×1 | — |
| `memory-review` | `.upstream/engineering-team/self-improving-agent/skills/memory-review` | 0 | command:namespace×8, file:CLAUDE.md×10, host:Claude×2, host:Claude Code×1, path:project-dir×7, path:user-dir×2 | — |
| `memory-status` | `.upstream/engineering-team/self-improving-agent/skills/memory-status` | 0 | command:namespace×9, file:CLAUDE.md×6, host:Claude×1, path:project-dir×5, path:user-context×2, path:user-dir×2 | — |
| `promote` | `.upstream/engineering-team/self-improving-agent/skills/promote` | 0 | command:namespace×6, file:CLAUDE.md×11, host:Claude×3, path:project-dir×8, path:user-context×1, path:user-dir×1 | — |
| `remember` | `.upstream/engineering-team/self-improving-agent/skills/remember` | 0 | command:namespace×9, file:CLAUDE.md×5, host:Claude×3, path:project-dir×2, path:user-context×1, path:user-dir×1 | — |
| `self-improving-agent` | `.upstream/engineering-team/self-improving-agent/skills/self-improving-agent` | 0 | command:namespace×13, file:CLAUDE.md×10, host:Claude×11, host:Claude Code×5, path:project-dir×10, path:user-context×1, path:user-dir×3 | — |
| `adversarial-reviewer` | `.upstream/engineering-team/skills/adversarial-reviewer` | 0 | file:CLAUDE.md×1, host:Claude×2 | — |
| `ai-security` | `.upstream/engineering-team/skills/ai-security` | 2 | — | — |
| `aws-solution-architect` | `.upstream/engineering-team/skills/aws-solution-architect` | 8 | — | — |
| `azure-cloud-architect` | `.upstream/engineering-team/skills/azure-cloud-architect` | 6 | — | — |
| `cloud-security` | `.upstream/engineering-team/skills/cloud-security` | 2 | — | — |
| `code-reviewer` | `.upstream/engineering-team/skills/code-reviewer` | 30 | — | — |
| `email-template-builder` | `.upstream/engineering-team/skills/email-template-builder` | 0 | — | — |
| `embedded-iot-mentor` | `.upstream/engineering-team/skills/embedded-iot-mentor` | 1 | — | — |
| `engineering-skills` | `.upstream/engineering-team/skills/engineering-skills` | 0 | file:CLAUDE.md×1, host:Claude×1, host:Claude Code×1 | — |
| `epic-design` | `.upstream/engineering-team/skills/epic-design` | 11 | — | — |
| `gcp-cloud-architect` | `.upstream/engineering-team/skills/gcp-cloud-architect` | 6 | — | — |
| `incident-commander` | `.upstream/engineering-team/skills/incident-commander` | 22 | host:Claude×1 | — |
| `incident-response` | `.upstream/engineering-team/skills/incident-response` | 2 | — | — |
| `ms365-tenant-manager` | `.upstream/engineering-team/skills/ms365-tenant-manager` | 8 | — | — |
| `named-persona-adversarial-review` | `.upstream/engineering-team/skills/named-persona-adversarial-review` | 1 | path:project-dir×1 | — |
| `red-green-proof` | `.upstream/engineering-team/skills/red-green-proof` | 3 | — | — |
| `red-team` | `.upstream/engineering-team/skills/red-team` | 2 | — | — |
| `security-pen-testing` | `.upstream/engineering-team/skills/security-pen-testing` | 6 | — | — |
| `senior-architect` | `.upstream/engineering-team/skills/senior-architect` | 6 | — | — |
| `senior-backend` | `.upstream/engineering-team/skills/senior-backend` | 13 | file:CLAUDE.md×1 | — |
| `senior-computer-vision` | `.upstream/engineering-team/skills/senior-computer-vision` | 7 | — | — |
| `senior-data-engineer` | `.upstream/engineering-team/skills/senior-data-engineer` | 8 | — | — |
| `senior-data-scientist` | `.upstream/engineering-team/skills/senior-data-scientist` | 6 | — | — |
| `senior-devops` | `.upstream/engineering-team/skills/senior-devops` | 6 | — | — |
| `senior-frontend` | `.upstream/engineering-team/skills/senior-frontend` | 13 | file:CLAUDE.md×1 | — |
| `senior-fullstack` | `.upstream/engineering-team/skills/senior-fullstack` | 12 | file:CLAUDE.md×1 | — |
| `senior-ml-engineer` | `.upstream/engineering-team/skills/senior-ml-engineer` | 6 | — | — |
| `senior-prompt-engineer` | `.upstream/engineering-team/skills/senior-prompt-engineer` | 6 | host:claude×1 | — |
| `senior-qa` | `.upstream/engineering-team/skills/senior-qa` | 7 | — | — |
| `senior-secops` | `.upstream/engineering-team/skills/senior-secops` | 6 | — | — |
| `senior-security` | `.upstream/engineering-team/skills/senior-security` | 5 | — | — |
| `stripe-integration-expert` | `.upstream/engineering-team/skills/stripe-integration-expert` | 0 | — | — |
| `tdd-guide` | `.upstream/engineering-team/skills/tdd-guide` | 17 | host:Claude×10, host:Claude Code×4, path:project-dir×3, path:project-skills×3, path:user-dir×2, path:user-skills×2 | — |
| `tech-stack-evaluator` | `.upstream/engineering-team/skills/tech-stack-evaluator` | 14 | — | — |
| `threat-detection` | `.upstream/engineering-team/skills/threat-detection` | 2 | command:namespace×1 | — |
| `snowflake-development` | `.upstream/engineering-team/snowflake-development/skills/snowflake-development` | 4 | — | — |
| `agent-harness` | `.upstream/engineering/agent-harness/skills/agent-harness` | 27 | host:Claude×7, host:Claude Code×5 | — |
| `agent-memory` | `.upstream/engineering/agent-memory/skills/agent-memory` | 9 | file:CLAUDE.md×7, host:Claude×4, host:Claude Code×4 | folded `argument-hint` into metadata |
| `agent-regression-evals` | `.upstream/engineering/agent-regression-evals/skills/agent-regression-evals` | 10 | host:Claude×1 | folded `argument-hint` into metadata |
| `agent-run-forensics` | `.upstream/engineering/agent-run-forensics/skills/agent-run-forensics` | 9 | env:config-dir×2, host:Claude×11, host:Claude Code×11, path:project-dir×2, path:user-dir×2 | folded `argument-hint` into metadata |
| `agenthub` | `.upstream/engineering/agenthub/skills/agenthub` | 9 | command:namespace×13, host:Claude×1, host:Claude Code×1, path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `board` | `.upstream/engineering/agenthub/skills/board` | 0 | command:namespace×5, path:skill_path×8 | — |
| `eval` | `.upstream/engineering/agenthub/skills/eval` | 0 | command:namespace×6, path:skill_path×4 | — |
| `hub-init` | `.upstream/engineering/agenthub/skills/hub-init` | 0 | command:namespace×4, path:skill_path×2 | — |
| `hub-run` | `.upstream/engineering/agenthub/skills/hub-run` | 0 | command:namespace×6, path:skill_path×2 | — |
| `hub-status` | `.upstream/engineering/agenthub/skills/hub-status` | 0 | command:namespace×1, path:skill_path×6 | — |
| `merge` | `.upstream/engineering/agenthub/skills/merge` | 0 | command:namespace×5, path:skill_path×4 | — |
| `spawn` | `.upstream/engineering/agenthub/skills/spawn` | 0 | command:namespace×6, path:skill_path×2 | — |
| `ar-loop` | `.upstream/engineering/autoresearch-agent/skills/ar-loop` | 0 | path:skill_path×2 | — |
| `ar-resume` | `.upstream/engineering/autoresearch-agent/skills/ar-resume` | 0 | path:skill_path×2 | — |
| `ar-run` | `.upstream/engineering/autoresearch-agent/skills/ar-run` | 0 | path:skill_path×4 | — |
| `ar-status` | `.upstream/engineering/autoresearch-agent/skills/ar-status` | 0 | path:skill_path×10 | — |
| `autoresearch-agent` | `.upstream/engineering/autoresearch-agent/skills/autoresearch-agent` | 5 | command:namespace×1, host:Claude×4, host:Claude Code×1, host:claude×1, path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `setup` | `.upstream/engineering/autoresearch-agent/skills/setup` | 0 | command:namespace×6, path:skill_path×6 | — |
| `behuman` | `.upstream/engineering/behuman/skills/behuman` | 1 | host:Claude×1, host:Claude Code×1 | — |
| `book-to-skill` | `.upstream/engineering/book-to-skill/skills/book-to-skill` | 27 | host:Claude×4, host:Claude Code×2, path:project-dir×4, path:project-skills×4, path:user-dir×3, path:user-skills×3 | — |
| `boost-asio-pro` | `.upstream/engineering/boost-asio-pro` | 5 | — | — |
| `caveman` | `.upstream/engineering/caveman/skills/caveman` | 6 | — | — |
| `chaos-engineering` | `.upstream/engineering/chaos-engineering/skills/chaos-engineering` | 9 | — | dropped `context` |
| `claude-coach` | `.upstream/engineering/claude-coach/skills/claude-coach` | 6 | host:Claude×37 | — |
| `code-tour` | `.upstream/engineering/code-tour/skills/code-tour` | 0 | — | — |
| `coding-agent-rollout` | `.upstream/engineering/coding-agent-rollout/skills/coding-agent-rollout` | 10 | env:config-dir×1, file:CLAUDE.local.md×3, file:CLAUDE.md×20, host:Claude×26, host:Claude Code×25, host:claude×2, path:project-dir×14, path:user-context×2, path:user-dir×8, tool:backtick×1 | folded `argument-hint` into metadata |
| `collab-proof` | `.upstream/engineering/collab-proof/skills/collab-proof` | 4 | host:Claude×20, host:Claude Code×9, path:project-dir×3, path:user-dir×2 | — |
| `commit-craft` | `.upstream/engineering/commit-craft/skills/commit-craft` | 11 | — | folded `argument-hint` into metadata |
| `data-quality-auditor` | `.upstream/engineering/data-quality-auditor/skills/data-quality-auditor` | 4 | — | — |
| `deep-learning-book` | `.upstream/engineering/deep-learning-book/skills/deep-learning-book` | 34 | — | — |
| `demo-video` | `.upstream/engineering/demo-video/skills/demo-video` | 1 | — | — |
| `docker-development` | `.upstream/engineering/docker-development/skills/docker-development` | 4 | path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `feature-flags-architect` | `.upstream/engineering/feature-flags-architect/skills/feature-flags-architect` | 8 | — | dropped `context` |
| `grill-me` | `.upstream/engineering/grill-me/skills/grill-me` | 6 | tool:backtick×1 | — |
| `grill-with-docs` | `.upstream/engineering/grill-with-docs/skills/grill-with-docs` | 8 | — | — |
| `handoff` | `.upstream/engineering/handoff/skills/handoff` | 7 | host:Claude×1, host:Claude Code×1 | folded `argument-hint` into metadata |
| `helm-chart-builder` | `.upstream/engineering/helm-chart-builder/skills/helm-chart-builder` | 4 | path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `hivemind` | `.upstream/engineering/hivemind` | 19 | arg:ARGUMENTS×8, host:Claude×6, host:Claude Code×3, host:claude×3, path:project-dir×5, path:project-skills×2, path:user-dir×4, path:user-skills×2, tool:phrase×2 | — |
| `human-gate` | `.upstream/engineering/human-gate/skills/human-gate` | 8 | — | — |
| `i18n-localization` | `.upstream/engineering/i18n-localization/skills/i18n-localization` | 8 | — | folded `argument-hint` into metadata |
| `karpathy-coder` | `.upstream/engineering/karpathy-coder/skills/karpathy-coder` | 11 | file:CLAUDE.md×1, host:Claude×4, host:Claude Code×4, path:plugin-root-unresolved×1, path:project-dir×2 | dropped `context` |
| `kubernetes-operator` | `.upstream/engineering/kubernetes-operator/skills/kubernetes-operator` | 9 | — | dropped `context` |
| `llm-cost-optimizer` | `.upstream/engineering/llm-cost-optimizer/skills/llm-cost-optimizer` | 0 | — | — |
| `llm-wiki` | `.upstream/engineering/llm-wiki/skills/llm-wiki` | 42 | file:CLAUDE.md×15, host:Claude×11, host:Claude Code×7, path:project-dir×7, path:project-skills×7, path:user-dir×7, path:user-skills×7, tool:phrase×2 | dropped `context` |
| `memory-engineering` | `.upstream/engineering/memory-engineering/skills/memory-engineering` | 11 | host:Claude×5, path:project-dir×1, path:user-dir×1 | folded `argument-hint` into metadata |
| `minimalist` | `.upstream/engineering/minimalist` | 0 | — | — |
| `prompt-governance` | `.upstream/engineering/prompt-governance/skills/prompt-governance` | 0 | — | — |
| `security-guidance` | `.upstream/engineering/security-guidance/skills/security-guidance` | 1 | host:Claude×18, host:Claude Code×9, path:project-dir×9, path:user-dir×7, tool:backtick×6 | — |
| `skill-retro` | `.upstream/engineering/skill-retro/skills/skill-retro` | 11 | host:Claude×4, host:Claude Code×4, path:project-dir×3, path:project-skills×1, path:user-dir×2 | folded `argument-hint` into metadata |
| `skillopt-sleep` | `.upstream/engineering/skillopt-sleep/skills/skillopt-sleep` | 0 | file:CLAUDE.md×7, host:Claude×4, host:Claude Code×1, host:claude×4, path:plugin-root-unresolved×6, path:project-dir×2, path:user-dir×2 | — |
| `agent-designer` | `.upstream/engineering/skills/agent-designer` | 13 | host:Claude×3, host:Claude Code×2 | — |
| `agent-workflow-designer` | `.upstream/engineering/skills/agent-workflow-designer` | 2 | — | — |
| `api-design-reviewer` | `.upstream/engineering/skills/api-design-reviewer` | 5 | host:Claude×1 | — |
| `api-test-suite-builder` | `.upstream/engineering/skills/api-test-suite-builder` | 1 | — | — |
| `browser-automation` | `.upstream/engineering/skills/browser-automation` | 6 | — | — |
| `changelog-generator` | `.upstream/engineering/skills/changelog-generator` | 9 | host:Claude×1, host:Claude Code×1, path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `ci-cd-pipeline-builder` | `.upstream/engineering/skills/ci-cd-pipeline-builder` | 7 | host:Claude×1, host:Claude Code×1, path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `codebase-onboarding` | `.upstream/engineering/skills/codebase-onboarding` | 3 | — | — |
| `database-designer` | `.upstream/engineering/skills/database-designer` | 14 | — | — |
| `database-schema-designer` | `.upstream/engineering/skills/database-schema-designer` | 1 | — | — |
| `dependency-auditor` | `.upstream/engineering/skills/dependency-auditor` | 15 | — | — |
| `engineering-advanced-skills` | `.upstream/engineering/skills/engineering-advanced-skills` | 0 | host:Claude×1, host:Claude Code×1 | — |
| `env-secrets-manager` | `.upstream/engineering/skills/env-secrets-manager` | 3 | — | — |
| `focused-fix` | `.upstream/engineering/skills/focused-fix` | 0 | — | — |
| `full-page-screenshot` | `.upstream/engineering/skills/full-page-screenshot` | 1 | — | — |
| `git-worktree-manager` | `.upstream/engineering/skills/git-worktree-manager` | 5 | host:Claude×1, host:Claude Code×1, path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `interview-system-designer` | `.upstream/engineering/skills/interview-system-designer` | 15 | — | — |
| `mcp-oauth-triage` | `.upstream/engineering/skills/mcp-oauth-triage` | 16 | host:Claude×1, host:Claude Code×1, path:project-dir×2, path:project-skills×2, path:user-dir×2, path:user-skills×2 | — |
| `mcp-server-builder` | `.upstream/engineering/skills/mcp-server-builder` | 8 | host:Claude×1, host:Claude Code×1, path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `migration-architect` | `.upstream/engineering/skills/migration-architect` | 19 | — | — |
| `monorepo-navigator` | `.upstream/engineering/skills/monorepo-navigator` | 3 | file:CLAUDE.md×10, host:Claude×4, host:Claude Code×3 | — |
| `observability-designer` | `.upstream/engineering/skills/observability-designer` | 12 | host:Claude×1 | — |
| `performance-profiler` | `.upstream/engineering/skills/performance-profiler` | 3 | — | — |
| `pr-review-expert` | `.upstream/engineering/skills/pr-review-expert` | 0 | — | — |
| `rag-architect` | `.upstream/engineering/skills/rag-architect` | 6 | — | — |
| `runbook-generator` | `.upstream/engineering/skills/runbook-generator` | 2 | — | — |
| `secrets-vault-manager` | `.upstream/engineering/skills/secrets-vault-manager` | 6 | — | — |
| `self-eval` | `.upstream/engineering/skills/self-eval` | 0 | arg:ARGUMENTS×1, host:Claude×2, host:Claude Code×2 | — |
| `ship-gate` | `.upstream/engineering/skills/ship-gate` | 3 | host:Claude×4 | — |
| `skill-security-auditor` | `.upstream/engineering/skills/skill-security-auditor` | 2 | — | — |
| `skill-tester` | `.upstream/engineering/skills/skill-tester` | 17 | host:Claude×4, host:Claude Code×1 | — |
| `sample-text-processor` | `.upstream/engineering/skills/skill-tester/assets/sample-skill` | 6 | host:Claude×1, host:Claude Code×1 | — |
| `slo-architect` | `.upstream/engineering/skills/slo-architect` | 9 | — | dropped `context` |
| `spec-driven-workflow` | `.upstream/engineering/skills/spec-driven-workflow` | 6 | — | — |
| `sql-database-assistant` | `.upstream/engineering/skills/sql-database-assistant` | 6 | — | — |
| `tc-tracker` | `.upstream/engineering/skills/tc-tracker` | 9 | host:Claude×1, host:Claude Code×1, path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `tech-debt-tracker` | `.upstream/engineering/skills/tech-debt-tracker` | 17 | — | — |
| `spinning-up-deep-rl` | `.upstream/engineering/spinning-up-deep-rl/skills/spinning-up-deep-rl` | 23 | — | — |
| `statistical-analyst` | `.upstream/engineering/statistical-analyst/skills/statistical-analyst` | 4 | — | — |
| `strict-api` | `.upstream/engineering/strict-api` | 0 | — | — |
| `terraform-patterns` | `.upstream/engineering/terraform-patterns/skills/terraform-patterns` | 5 | path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `universal-scraping-architect` | `.upstream/engineering/universal-scraping-architect/skills/universal-scraping-architect` | 7 | — | — |
| `workflow-builder` | `.upstream/engineering/workflow-builder/skills/workflow-builder` | 14 | host:Claude×12, host:Claude Code×8, path:project-dir×5 | — |
| `write-a-skill` | `.upstream/engineering/write-a-skill/skills/write-a-skill` | 8 | host:Claude×3, host:Claude Code×2 | — |
| `zero-hallucination-coder` | `.upstream/engineering/zero-hallucination-coder/skills/zero-hallucination-coder` | 0 | host:Claude×1 | — |
| `business-investment-advisor` | `.upstream/finance/business-investment-advisor/skills/business-investment-advisor` | 0 | — | — |
| `month-end-close` | `.upstream/finance/month-end-close/skills/month-end-close` | 11 | — | folded `argument-hint` into metadata |
| `finance-skills` | `.upstream/finance/skills/finance-skills` | 0 | — | — |
| `financial-analyst` | `.upstream/finance/skills/financial-analyst` | 13 | — | — |
| `passive-deal-screener` | `.upstream/finance/skills/passive-deal-screener` | 20 | — | — |
| `saas-metrics-coach` | `.upstream/finance/skills/saas-metrics-coach` | 6 | — | — |
| `stock-analysis` | `.upstream/finance/skills/stock-analysis` | 60 | — | — |
| `loop-library` | `.upstream/loop-library` | 5 | — | — |
| `design-system` | `.upstream/markdown-html/skills/design-system` | 7 | file:CLAUDE.md×2 | — |
| `markdown-html-orchestrator` | `.upstream/markdown-html/skills/markdown-html-orchestrator` | 6 | file:CLAUDE.md×1, host:Claude×5, host:Claude Code×4 | dropped `context` |
| `md-document` | `.upstream/markdown-html/skills/md-document` | 7 | file:CLAUDE.md×1, host:Claude×3, host:Claude Code×3 | — |
| `md-review` | `.upstream/markdown-html/skills/md-review` | 7 | host:Claude×1, host:Claude Code×1 | — |
| `md-slides` | `.upstream/markdown-html/skills/md-slides` | 7 | host:Claude×1, host:Claude Code×1 | — |
| `ab-test-setup` | `.upstream/marketing-skill/skills/ab-test-setup` | 3 | path:project-dir×1 | — |
| `ad-creative` | `.upstream/marketing-skill/skills/ad-creative` | 3 | path:project-dir×1 | — |
| `aeo` | `.upstream/marketing-skill/skills/aeo` | 8 | host:Claude×22 | — |
| `ai-decision-authority` | `.upstream/marketing-skill/skills/ai-decision-authority` | 0 | — | — |
| `analytics-tracking` | `.upstream/marketing-skill/skills/analytics-tracking` | 4 | path:project-dir×1 | — |
| `app-store-optimization` | `.upstream/marketing-skill/skills/app-store-optimization` | 16 | host:Claude×14, host:Claude Code×2, path:project-dir×3, path:project-skills×3, path:user-dir×2, path:user-skills×2 | — |
| `brand-guidelines` | `.upstream/marketing-skill/skills/brand-guidelines` | 1 | path:project-dir×1 | — |
| `business-name-fit` | `.upstream/marketing-skill/skills/business-name-fit` | 2 | — | — |
| `campaign-analytics` | `.upstream/marketing-skill/skills/campaign-analytics` | 11 | — | — |
| `churn-prevention` | `.upstream/marketing-skill/skills/churn-prevention` | 3 | path:project-dir×1 | — |
| `cinematic-shot-prompting` | `.upstream/marketing-skill/skills/cinematic-shot-prompting` | 2 | host:Claude×1, host:Claude Code×1 | — |
| `cold-email` | `.upstream/marketing-skill/skills/cold-email` | 4 | path:project-dir×1 | — |
| `competitor-alternatives` | `.upstream/marketing-skill/skills/competitor-alternatives` | 3 | path:project-dir×1 | — |
| `content-creator` | `.upstream/marketing-skill/skills/content-creator` | 7 | host:Claude×1 | — |
| `content-humanizer` | `.upstream/marketing-skill/skills/content-humanizer` | 3 | path:project-dir×4 | — |
| `content-production` | `.upstream/marketing-skill/skills/content-production` | 9 | host:Claude×1, path:project-dir×3 | — |
| `content-strategy` | `.upstream/marketing-skill/skills/content-strategy` | 2 | path:project-dir×1 | — |
| `copy-editing` | `.upstream/marketing-skill/skills/copy-editing` | 5 | path:project-dir×1 | — |
| `copywriting` | `.upstream/marketing-skill/skills/copywriting` | 3 | path:project-dir×1 | — |
| `email-sequence` | `.upstream/marketing-skill/skills/email-sequence` | 2 | path:project-dir×1 | — |
| `form-cro` | `.upstream/marketing-skill/skills/form-cro` | 2 | path:project-dir×2 | — |
| `free-tool-strategy` | `.upstream/marketing-skill/skills/free-tool-strategy` | 3 | path:project-dir×1 | — |
| `launch-strategy` | `.upstream/marketing-skill/skills/launch-strategy` | 2 | path:project-dir×1 | — |
| `local-seo-manager` | `.upstream/marketing-skill/skills/local-seo-manager` | 6 | — | — |
| `marketing-context` | `.upstream/marketing-skill/skills/marketing-context` | 2 | path:project-dir×4 | — |
| `marketing-demand-acquisition` | `.upstream/marketing-skill/skills/marketing-demand-acquisition` | 5 | — | — |
| `marketing-ideas` | `.upstream/marketing-skill/skills/marketing-ideas` | 1 | path:project-dir×1 | — |
| `marketing-ops` | `.upstream/marketing-skill/skills/marketing-ops` | 1 | path:project-dir×1 | — |
| `marketing-psychology` | `.upstream/marketing-skill/skills/marketing-psychology` | 1 | path:project-dir×1 | — |
| `marketing-skills` | `.upstream/marketing-skill/skills/marketing-skills` | 0 | path:project-dir×2 | — |
| `marketing-strategy-pmm` | `.upstream/marketing-skill/skills/marketing-strategy-pmm` | 4 | — | — |
| `onboarding-cro` | `.upstream/marketing-skill/skills/onboarding-cro` | 1 | path:project-dir×1 | — |
| `page-cro` | `.upstream/marketing-skill/skills/page-cro` | 1 | path:project-dir×2 | — |
| `paid-ads` | `.upstream/marketing-skill/skills/paid-ads` | 7 | path:project-dir×1 | — |
| `paywall-upgrade-cro` | `.upstream/marketing-skill/skills/paywall-upgrade-cro` | 0 | path:project-dir×1 | — |
| `popup-cro` | `.upstream/marketing-skill/skills/popup-cro` | 1 | path:project-dir×1 | — |
| `pricing-strategy` | `.upstream/marketing-skill/skills/pricing-strategy` | 3 | path:project-dir×1 | — |
| `programmatic-seo` | `.upstream/marketing-skill/skills/programmatic-seo` | 1 | path:project-dir×2 | — |
| `prompt-engineer-toolkit` | `.upstream/marketing-skill/skills/prompt-engineer-toolkit` | 6 | host:Claude×1, host:Claude Code×1, path:project-dir×3, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `referral-program` | `.upstream/marketing-skill/skills/referral-program` | 3 | path:project-dir×1 | — |
| `schema-markup` | `.upstream/marketing-skill/skills/schema-markup` | 3 | path:project-dir×1 | — |
| `seo-audit` | `.upstream/marketing-skill/skills/seo-audit` | 6 | path:project-dir×2 | — |
| `signup-flow-cro` | `.upstream/marketing-skill/skills/signup-flow-cro` | 2 | path:project-dir×2 | — |
| `site-architecture` | `.upstream/marketing-skill/skills/site-architecture` | 3 | path:project-dir×1 | — |
| `social-content` | `.upstream/marketing-skill/skills/social-content` | 3 | path:project-dir×1 | — |
| `social-media-analyzer` | `.upstream/marketing-skill/skills/social-media-analyzer` | 6 | host:Claude×4 | — |
| `social-media-manager` | `.upstream/marketing-skill/skills/social-media-manager` | 1 | path:project-dir×1 | — |
| `webinar-marketing` | `.upstream/marketing-skill/skills/webinar-marketing` | 6 | path:project-dir×1 | — |
| `x-twitter-growth` | `.upstream/marketing-skill/skills/x-twitter-growth` | 6 | — | — |
| `youtube-full` | `.upstream/marketing-skill/skills/youtube-full` | 0 | — | — |
| `video-content-strategist` | `.upstream/marketing-skill/video-content-strategist/skills/video-content-strategist` | 0 | path:project-dir×1 | — |
| `landing` | `.upstream/marketing/landing/skills/landing` | 6 | host:Claude×4, host:Claude Code×2 | — |
| `linkedin-analytics` | `.upstream/marketing/linkedin/skills/linkedin-analytics` | 7 | — | — |
| `linkedin-content` | `.upstream/marketing/linkedin/skills/linkedin-content` | 9 | — | — |
| `linkedin-engagement` | `.upstream/marketing/linkedin/skills/linkedin-engagement` | 7 | — | — |
| `linkedin-profile` | `.upstream/marketing/linkedin/skills/linkedin-profile` | 7 | — | — |
| `linkedin-skills` | `.upstream/marketing/linkedin/skills/linkedin-skills` | 5 | — | dropped `context` |
| `linkedin-strategy` | `.upstream/marketing/linkedin/skills/linkedin-strategy` | 8 | — | — |
| `agile-product-owner` | `.upstream/product-team/agile-product-owner/skills/agile-product-owner` | 5 | — | — |
| `apple-hig-expert` | `.upstream/product-team/apple-hig-expert/skills/apple-hig-expert` | 5 | — | — |
| `code-to-prd` | `.upstream/product-team/code-to-prd/skills/code-to-prd` | 8 | — | — |
| `design-qa` | `.upstream/product-team/design-qa/skills/design-qa` | 12 | — | folded `argument-hint` into metadata |
| `research-summarizer` | `.upstream/product-team/research-summarizer/skills/research-summarizer` | 4 | path:project-dir×1, path:project-skills×1, path:user-dir×1, path:user-skills×1 | — |
| `competitive-teardown` | `.upstream/product-team/skills/competitive-teardown` | 5 | — | — |
| `experiment-designer` | `.upstream/product-team/skills/experiment-designer` | 3 | — | — |
| `landing-page-generator` | `.upstream/product-team/skills/landing-page-generator` | 5 | — | — |
| `product-analytics` | `.upstream/product-team/skills/product-analytics` | 3 | — | — |
| `product-discovery` | `.upstream/product-team/skills/product-discovery` | 2 | — | — |
| `product-manager-toolkit` | `.upstream/product-team/skills/product-manager-toolkit` | 7 | — | — |
| `product-skills` | `.upstream/product-team/skills/product-skills` | 8 | — | dropped `context` |
| `product-strategist` | `.upstream/product-team/skills/product-strategist` | 5 | — | — |
| `roadmap-communicator` | `.upstream/product-team/skills/roadmap-communicator` | 3 | — | — |
| `saas-scaffolder` | `.upstream/product-team/skills/saas-scaffolder` | 5 | — | — |
| `spec-to-repo` | `.upstream/product-team/skills/spec-to-repo` | 3 | — | — |
| `ui-design-system` | `.upstream/product-team/skills/ui-design-system` | 6 | — | — |
| `ux-researcher-designer` | `.upstream/product-team/skills/ux-researcher-designer` | 6 | — | — |
| `andreessen` | `.upstream/productivity/andreessen/skills/andreessen` | 13 | host:Claude×3, host:Claude Code×1 | — |
| `capture` | `.upstream/productivity/capture/skills/capture` | 6 | host:Claude×5, host:Claude Code×3, tool:backtick×4 | — |
| `deep-work` | `.upstream/productivity/deep-work/skills/deep-work` | 8 | arg:ARGUMENTS×1, host:Claude×2, host:Claude Code×1 | folded `argument-hint` into metadata |
| `inbox-setup` | `.upstream/productivity/email/skills/inbox-setup` | 6 | host:Claude×2, host:Claude Code×1 | — |
| `inbox-triage` | `.upstream/productivity/email/skills/inbox-triage` | 6 | host:Claude×2, host:Claude Code×1 | — |
| `fable-goal` | `.upstream/productivity/fable-goal/skills/fable-goal` | 2 | file:CLAUDE.md×2, host:Claude×1, host:Claude Code×1, path:project-dir×2, path:user-context×1, path:user-dir×2 | — |
| `session-handoff` | `.upstream/productivity/handoff/skills/session-handoff` | 14 | host:Claude×2, host:Claude Code×2 | folded `argument-hint` into metadata |
| `meetings` | `.upstream/productivity/meetings/skills/meetings` | 8 | — | folded `argument-hint` into metadata |
| `monetize` | `.upstream/productivity/monetize` | 5 | path:plugin-root-unresolved×1 | — |
| `reflect` | `.upstream/productivity/reflect/skills/reflect` | 6 | host:Claude×3, host:Claude Code×1 | — |
| `roast` | `.upstream/productivity/roast/skills/roast` | 9 | arg:ARGUMENTS×1, command:namespace×1, host:Claude×3, host:Claude Code×1 | folded `argument-hint` into metadata |
| `swedish-mentor` | `.upstream/productivity/swedish-mentor` | 1 | — | — |
| `weekly-review` | `.upstream/productivity/weekly-review/skills/weekly-review` | 8 | host:Claude×3, host:Claude Code×1 | folded `argument-hint` into metadata |
| `atlassian-admin` | `.upstream/project-management/skills/atlassian-admin` | 4 | — | — |
| `atlassian-templates` | `.upstream/project-management/skills/atlassian-templates` | 3 | command:namespace×1 | — |
| `confluence-expert` | `.upstream/project-management/skills/confluence-expert` | 5 | command:namespace×34 | — |
| `jira-expert` | `.upstream/project-management/skills/jira-expert` | 6 | — | — |
| `meeting-analyzer` | `.upstream/project-management/skills/meeting-analyzer` | 0 | — | — |
| `pm-skills` | `.upstream/project-management/skills/pm-skills` | 8 | host:Claude×1, host:Claude Code×1 | dropped `context` |
| `scrum-master` | `.upstream/project-management/skills/scrum-master` | 11 | — | — |
| `senior-pm` | `.upstream/project-management/skills/senior-pm` | 11 | — | — |
| `team-communications` | `.upstream/project-management/skills/team-communications` | 4 | — | — |
| `access-lifecycle` | `.upstream/ra-qm-team/access-lifecycle/skills/access-lifecycle` | 10 | — | folded `argument-hint` into metadata |
| `cmmc-readiness` | `.upstream/ra-qm-team/cmmc-readiness/skills/cmmc-readiness` | 10 | — | folded `argument-hint` into metadata |
| `eu-ai-act-specialist` | `.upstream/ra-qm-team/compliance-team-eu-ai-act/skills/eu-ai-act-specialist` | 7 | — | — |
| `iso42001-specialist` | `.upstream/ra-qm-team/compliance-team-iso42001/skills/iso42001-specialist` | 7 | — | — |
| `cra-readiness` | `.upstream/ra-qm-team/cra-readiness/skills/cra-readiness` | 12 | — | folded `argument-hint` into metadata |
| `medical-device-software` | `.upstream/ra-qm-team/medical-device-software/skills/medical-device-software` | 13 | — | folded `argument-hint` into metadata |
| `agent-decision-receipts` | `.upstream/ra-qm-team/skills/agent-decision-receipts` | 2 | — | — |
| `capa-officer` | `.upstream/ra-qm-team/skills/capa-officer` | 4 | — | — |
| `fda-consultant-specialist` | `.upstream/ra-qm-team/skills/fda-consultant-specialist` | 8 | — | — |
| `gdpr-dsgvo-expert` | `.upstream/ra-qm-team/skills/gdpr-dsgvo-expert` | 7 | — | — |
| `information-security-manager-iso27001` | `.upstream/ra-qm-team/skills/information-security-manager-iso27001` | 5 | — | — |
| `isms-audit-expert` | `.upstream/ra-qm-team/skills/isms-audit-expert` | 5 | — | — |
| `mdr-745-specialist` | `.upstream/ra-qm-team/skills/mdr-745-specialist` | 4 | — | — |
| `qms-audit-expert` | `.upstream/ra-qm-team/skills/qms-audit-expert` | 4 | — | — |
| `quality-documentation-manager` | `.upstream/ra-qm-team/skills/quality-documentation-manager` | 4 | — | — |
| `quality-manager-qmr` | `.upstream/ra-qm-team/skills/quality-manager-qmr` | 4 | — | — |
| `quality-manager-qms-iso13485` | `.upstream/ra-qm-team/skills/quality-manager-qms-iso13485` | 3 | — | — |
| `ra-qm-skills` | `.upstream/ra-qm-team/skills/ra-qm-skills` | 0 | — | — |
| `regulatory-affairs-head` | `.upstream/ra-qm-team/skills/regulatory-affairs-head` | 6 | — | — |
| `risk-management-specialist` | `.upstream/ra-qm-team/skills/risk-management-specialist` | 5 | — | — |
| `soc2-compliance` | `.upstream/ra-qm-team/skills/soc2-compliance` | 7 | — | — |
| `clinical-research` | `.upstream/research-ops/skills/clinical-research` | 10 | command:namespace×1 | — |
| `interview-mapper` | `.upstream/research-ops/skills/interview-mapper` | 96 | — | — |
| `market-research` | `.upstream/research-ops/skills/market-research` | 10 | command:namespace×1 | — |
| `product-research` | `.upstream/research-ops/skills/product-research` | 10 | command:namespace×1 | — |
| `research-finance` | `.upstream/research-ops/skills/research-finance` | 10 | command:namespace×1 | — |
| `research-ops-skills` | `.upstream/research-ops/skills/research-ops-skills` | 0 | — | dropped `context` |
| `deepread` | `.upstream/research/deepread` | 2 | — | — |
| `dossier` | `.upstream/research/dossier/skills/dossier` | 6 | host:Claude×1, host:Claude Code×1, tool:backtick×2 | — |
| `grants` | `.upstream/research/grants/skills/grants` | 6 | host:Claude×2, host:Claude Code×1 | — |
| `litreview` | `.upstream/research/litreview/skills/litreview` | 7 | host:Claude×3, host:Claude Code×1 | — |
| `meta-research` | `.upstream/research/meta-research/skills/meta-research` | 1 | — | — |
| `notebooklm` | `.upstream/research/notebooklm/skills/notebooklm` | 6 | host:Claude×12, host:Claude Code×3 | — |
| `patent` | `.upstream/research/patent/skills/patent` | 6 | host:Claude×2, host:Claude Code×1, tool:backtick×1 | — |
| `pulse` | `.upstream/research/pulse/skills/pulse` | 6 | host:Claude×7, host:Claude Code×5, tool:backtick×2 | — |
| `research` | `.upstream/research/research/skills/research` | 6 | host:Claude×3, host:Claude Code×1, tool:backtick×4 | — |
| `syllabus` | `.upstream/research/syllabus/skills/syllabus` | 7 | file:CLAUDE.md×2, host:Claude×2, host:Claude Code×1 | — |
| `asd-ste100` | `.upstream-extra/asd-ste100` | 6 | host:Claude×3, host:Claude Code×2, path:project-dir×2, path:project-skills×2, path:user-dir×2, path:user-skills×2 | — |

## Residual `claude` references

| category | count |
|---|---|
| code sample | 91 |
| untouched file | 442 |
| allowlisted | 243 |
| UNEXPECTED | 0 |

Code samples and non-`.md` files keep their Claude references on purpose (rewriting `claude --print` or a Python parser would break them).

### Skills whose subject matter is Claude Code machinery

Their guidance was rewritten to Pi mechanically; the steps that depend on Claude Code hook/settings/plugin internals have no Pi equivalent.

| skill | host-specific refs |
|---|---|
| `coding-agent-rollout` | 16 |
| `extract` | 1 |
| `workflow-builder` | 3 |


Descriptions mentioning Claude: 0
