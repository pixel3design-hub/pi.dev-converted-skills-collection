---
name: "c-level-agents"
description: "Use when the founder wants a virtual executive team or a /c-level-agents command. Lists the 13 C-suite agents and 21 commands and routes multi-role decisions."
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: c-level
  domain: executive-orchestration
  updated: 2026-05-12
  agents: cs-cfo-advisor, cs-cmo-advisor, cs-cro-advisor, cs-cpo-advisor, cs-coo-advisor, cs-chro-advisor, cs-ciso-advisor, cs-general-counsel-advisor, cs-cdo-advisor, cs-caio-advisor, cs-cco-advisor, cs-vpe-advisor, cs-chief-of-staff
  commands: cs-office-hours, cs-cfo-review, cs-cmo-review, cs-cpo-review, cs-cro-review, cs-cto-review, cs-ciso-review, cs-gc-review, cs-cdo-review, cs-caio-review, cs-cco-review, cs-vpe-review, cs-brief, cs-boardroom, cs-decide, cs-execute, cs-post-mortem, cs-founder-mode, cs-onboard, cs-cross-eval, cs-freeze
---

# c-level-agents — Founder-Mode Executive Team

A virtual C-suite delivered through slash commands and persona agents.

## Keywords

founder mode, virtual c-suite, executive team, boardroom, office hours, cfo review, cmo review, strategic sprint, decision logging, cross-model consensus, persona agents, chief of staff, forcing questions

## What This Plugin Provides

### 13 cs-* Agents (in `agents/`)

Each agent wraps an existing c-level skill and adds:
- A distinct cognitive voice (numerate skeptic, narrative-first, etc.)
- Forcing questions specific to the role
- Workflow orchestration tied to skill Python tools
- Output template: Bottom Line → What → Why → How to Act → Your Decision

See `../../references/persona-voices.md` for voice specs.

### 21 /c-level-agents:* Slash Commands (in `skills/`)

**Forcing-question office hours (12):**
- `/skill:office-hours` — YC-style 6-question intake
- `/skill:cfo-review` — unit economics, runway, dilution
- `/skill:cmo-review` — ICP, CAC payback, positioning
- `/skill:cpo-review` — RICE, JTBD, North Star, PMF
- `/skill:cro-review` — pipeline coverage, win rate, NRR
- `/skill:cto-review` — architecture risk, scaling cliff
- `/skill:ciso-review` — threat model, blast radius, compliance
- `/skill:gc-review` — contracts, IP, regulatory, term sheets
- `/skill:cdo-review` — training-data rights, data products, data assets
- `/skill:caio-review` — model selection, evals, AI risk, AI costs
- `/skill:cco-review` — GRR/NRR decomposition, churn root cause, CS coverage
- `/skill:vpe-review` — DORA metrics, cycle time, eng hiring funnel, team structure

**Strategic sprint pipeline (5):**
- `/skill:brief` → `/skill:boardroom` → `/skill:decide` → `/skill:execute` → `/skill:post-mortem`

**Meta + safety (4):**
- `/skill:founder-mode` — auto-routes to the right C-role
- `/cs-onboard` — founder interview → `company-context.md`
- `/skill:cross-eval` — multi-model consensus
- `/skill:freeze` — cooldown lock on a decision

## Quick Start

```
/cs-onboard                          # populate company context first
/skill:office-hours "should we hire a VP Sales?"
/skill:founder-mode "runway pressure"   # auto-routes to CFO
/skill:boardroom briefs/pricing-v3.md   # full panel
```

## Architecture

```
User question
   │
   ├─ Single-role? → cs-{role}-advisor agent
   │                     ↓
   │                  /cs-{role}-review command (forcing Qs)
   │                     ↓
   │                  Skill tools + references
   │                     ↓
   │                  Bottom Line + Memo
   │
   └─ Multi-role?  → /skill:boardroom
                        ↓
                     6-phase deliberation (Phase 2 isolation)
                        ↓
                     /skill:decide → decision-logger (two-layer memory)
                        ↓
                     /skill:execute → 90-day plan
```

## Integration Points

- **Existing 33 c-level skills** — wrapped, not replaced
- **decision-logger** — every `/skill:decide` writes here
- **chief-of-staff** — routing layer the agent orchestrates
- **board-meeting** — protocol the `/skill:boardroom` command runs
- **llm-wiki** — optional persistent memory bridge (see `../../references/llm-wiki-bridge.md`)
- **executive-mentor** — adversarial `/executive-mentor:*` commands stack cleanly on top

## Design Principles

1. **Voice is bookended, analysis is neutral.**
2. **Artifacts over chat.** Every command produces a Markdown artifact the next command consumes.
3. **Phase 2 isolation in boardroom.** Independent thinking before cross-examination.
4. **Graceful degradation.** `/skill:cross-eval` falls back to Pi-only.
5. **No paid dependencies.** All Python tools are stdlib-only.

## References

- [persona-voices.md](../../references/persona-voices.md)
- [llm-wiki-bridge.md](../../references/llm-wiki-bridge.md)
- [Existing executive-mentor sibling](../executive-mentor/executive-mentor/SKILL.md)

---

**Version:** 1.0.0
**Last Updated:** 2026-05-12
**Status:** Production Ready
