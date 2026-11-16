---
name: "boardroom"
description: "Use for /skill:boardroom, or a decision spanning several executive domains (a pricing change, raise vs cut). Runs a 6-phase C-suite deliberation and writes a board memo."
---

# /skill:boardroom — Multi-Role Boardroom Deliberation

**Command:** `/skill:boardroom <brief-path>`

Runs the `board-meeting` skill protocol across the C-suite for a single strategy brief. This is the **heart of the plugin** — the multi-role deliberation that gstack's review chain only approximates.

## Pipeline Position

```
/skill:office-hours  →  /skill:brief  →  /skill:boardroom  →  /skill:decide  →  /skill:execute  →  /skill:post-mortem
                                     ↑ you are here
```

## The 6 Phases (from board-meeting skill)

### Phase 1 — Briefing
- Chief of Staff distributes the brief to all advisors marked in **Affected Roles**.
- Each advisor reads company-context.md + the brief.
- No discussion yet.

### Phase 2 — Independent Thinking (ISOLATION)
- **Critical:** each advisor produces their position **independently**, without seeing others' positions.
- This prevents groupthink and surfaces dissent.
- Each writes: their voice's opening, recommendation, top 3 concerns, top 3 supports.

### Phase 3 — Cross-Examination
- Positions revealed simultaneously.
- Each advisor critiques the others' positions on the dimensions they own:
  - cs-cfo-advisor critiques the math
  - cs-ciso-advisor critiques the risk
  - cs-cpo-advisor critiques the JTBD
  - cs-cmo-advisor critiques the positioning
  - cs-cro-advisor critiques the revenue math
  - etc.

### Phase 4 — Devil's Advocate Pass
- `executive-mentor/devils-advocate` agent runs `/skill:challenge` on the leading option.
- Surfaces three concerns with severity ratings.

### Phase 5 — Synthesis
- Chief of Staff synthesizes: which option commands majority, what are unresolved dissents.
- Produces the **board memo** with recommendation + dissent.

### Phase 6 — Decision Hand-off
- Memo is presented to the founder.
- Founder accepts, modifies, or rejects.
- Approved memo routes to `/skill:decide` for logging.

## Output: Board Memo

Saved to `~/.pi/agent/boardroom/YYYY-MM-DD-<slug>.md`:

```markdown
# Board Memo: <topic>
**Date:** YYYY-MM-DD
**Brief:** <link to /skill:brief file>
**Status:** AWAITING FOUNDER DECISION | APPROVED | REJECTED

## Question
[One sentence from the brief]

## Recommended Option
**<Option name>** — chosen because <synthesis reasoning>

## Vote Tally
| Advisor | Vote | One-Sentence Reason |
|---|---|---|
| cs-ceo-advisor | A | <reason> |
| cs-cfo-advisor | A | <reason> |
| cs-cto-advisor | B | <reason> |
| ... | | |

## Dissent
- **<dissenter>:** <unresolved concern>

## Devil's Advocate Concerns
1. **CRITICAL** — <concern> — Mitigation: <plan>
2. **HIGH** — <concern> — Mitigation: <plan>
3. **MEDIUM** — <concern> — Mitigation: <plan>

## Success & Kill Criteria
[Copied from brief, refined by the panel]

## Recommended Decision Path
- `/skill:decide` → log the decision
- `/skill:execute` → 90-day plan
- `/skill:cross-eval` → multi-model sanity check (optional, high-stakes)
- `/skill:freeze N` → cooldown lock (optional, irreversible)
```

## Why Phase 2 Isolation Matters

If advisors see each other's positions before forming their own, they anchor. Phase 2 isolation is the single highest-leverage practice in the board-meeting protocol — it surfaces the dissents that sycophancy would have suppressed.

## Why This Beats gstack's Review Chain

| | gstack `/autoplan` | `/skill:boardroom` |
|---|---|---|
| Roles | CEO → design → eng (3) | Up to 10 C-roles |
| Order | Sequential | Phase 2 isolation, then simultaneous |
| Dissent capture | Implicit | Explicit dissent column |
| Adversarial pass | No | Phase 4 devil's advocate |
| Output | Reviewed plan | Voted memo with dissent + kill criteria |

## Workflow

1. Read brief from `~/.pi/agent/briefs/<file>`
2. Identify affected roles
3. Invoke each cs-* advisor independently (Phase 2)
4. Collect positions
5. Run cross-examination round (Phase 3)
6. Run `/skill:challenge` on leading option (Phase 4)
7. Synthesize memo (Phase 5)
8. Hand off to founder (Phase 6)

## Routing

- `/skill:decide` — log approved memo
- `/skill:cross-eval` — high-stakes second opinion
- `/skill:freeze` — cooldown lock

## Related

- Agent: [`cs-chief-of-staff`](../../agents/cs-chief-of-staff.md)
- Skills: [`board-meeting`](../board-meeting/SKILL.md), [`executive-mentor`](../executive-mentor/executive-mentor/SKILL.md)

---

**Version:** 1.0.0
