---
name: "self-improving-agent"
description: "Curate what the agent has learned into durable project knowledge. Reviews Pi auto-memory (MEMORY.md and its topic files) for learnings worth keeping, promotes proven ones into AGENTS.md or .pi/rules/, records a correction as a lesson that persists across sessions, prunes stale or duplicate entries, and turns a recurring fix into a reusable skill. Use whenever the user asks what you have learned or saved about the project, which memories should become permanent rules, to remember a lesson or stop repeating a mistake, or to clean up, audit or check memory health."
disable-model-invocation: true
---

# Self-Improving Agent

> Auto-memory captures. This plugin curates.

Pi's auto-memory (v2.1.32+) automatically records project patterns, debugging insights, and your preferences in `MEMORY.md`. This plugin adds the intelligence layer: it analyzes what Pi has learned, promotes proven patterns into project rules, and extracts recurring solutions into reusable skills.

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/skill:memory-review` | Analyze MEMORY.md — find promotion candidates, stale entries, consolidation opportunities |
| `/skill:promote` | Graduate a pattern from MEMORY.md → AGENTS.md or `.pi/rules/` |
| `/skill:extract` | Turn a proven pattern into a standalone skill |
| `/skill:memory-status` | Memory health dashboard — line counts, topic files, recommendations |
| `/skill:remember` | Explicitly save important knowledge to auto-memory |

## How It Fits Together

```
┌─────────────────────────────────────────────────────────┐
│                  Claude Code Memory Stack                │
├─────────────┬──────────────────┬────────────────────────┤
│  AGENTS.md  │   Auto Memory    │   Session Memory       │
│  (you write)│   (Claude writes)│   (Claude writes)      │
│  Rules &    │   MEMORY.md      │   Conversation logs    │
│  standards  │   + topic files  │   + continuity         │
│  Full load  │   First 200 lines│   Contextual load      │
├─────────────┴──────────────────┴────────────────────────┤
│              ↑ /skill:promote        ↑ /skill:memory-review   │
│         Self-Improving Agent (this plugin)               │
│              ↓ /skill:extract    ↓ /skill:remember            │
├─────────────────────────────────────────────────────────┤
│  .pi/rules/    │    New Skills    │   Error Logs     │
│  (scoped rules)    │    (extracted)   │   (auto-captured)│
└─────────────────────────────────────────────────────────┘
```

## Installation

### Pi (Plugin)
```


```

### OpenClaw
```bash
clawhub install self-improving-agent
```

### Codex CLI
```bash
./scripts/codex-install.sh --skill self-improving-agent
```

## Memory Architecture

### Where things live

| File | Who writes | Scope | Loaded |
|------|-----------|-------|--------|
| `./AGENTS.md` | You (+ `/skill:promote`) | Project rules | Full file, every session |
| `~/.pi/agent/AGENTS.md` | You | Global preferences | Full file, every session |
| `~/.pi/agent/projects/<path>/memory/MEMORY.md` | Pi (auto) | Project learnings | First 200 lines |
| `~/.pi/agent/projects/<path>/memory/*.md` | Pi (overflow) | Topic-specific notes | On demand |
| `.pi/rules/*.md` | You (+ `/skill:promote`) | Scoped rules | When matching files open |

### The promotion lifecycle

```
1. Claude discovers pattern → auto-memory (MEMORY.md)
2. Pattern recurs 2-3x → /skill:memory-review flags it as promotion candidate
3. You approve → /skill:promote graduates it to AGENTS.md or rules/
4. Pattern becomes an enforced rule, not just a note
5. MEMORY.md entry removed → frees space for new learnings
```

## Core Concepts

### Auto-memory is capture, not curation

Auto-memory is excellent at recording what Pi learns. But it has no judgment about:
- Which learnings are temporary vs. permanent
- Which patterns should become enforced rules
- When the 200-line limit is wasting space on stale entries
- Which solutions are good enough to become reusable skills

That's what this plugin does.

### Promotion = graduation

When you promote a learning, it moves from Pi's scratchpad (MEMORY.md) to your project's rule system (AGENTS.md or `.pi/rules/`). The difference matters:

- **MEMORY.md**: "I noticed this project uses pnpm" (background context)
- **AGENTS.md**: "Use pnpm, not npm" (enforced instruction)

Promoted rules have higher priority and load in full (not truncated at 200 lines).

### Rules directory for scoped knowledge

Not everything belongs in AGENTS.md. Use `.pi/rules/` for patterns that only apply to specific file types:

```yaml
# .pi/rules/api-testing.md
---
paths:
  - "src/api/**/*.test.ts"
  - "tests/api/**/*"
---
- Use supertest for API endpoint testing
- Mock external services with msw
- Always test error responses, not just happy paths
```

This loads only when Pi works with API test files — zero overhead otherwise.

## Agents

### memory-analyst
Analyzes MEMORY.md and topic files to identify:
- Entries that recur across sessions (promotion candidates)
- Stale entries referencing deleted files or old patterns
- Related entries that should be consolidated
- Gaps between what MEMORY.md knows and what AGENTS.md enforces

### skill-extractor
Takes a proven pattern and generates a complete skill:
- SKILL.md with proper frontmatter
- Reference documentation
- Examples and edge cases
- Ready for `/plugin install` or `clawhub publish`

## Hooks

### error-capture (PostToolUse → Bash)
Monitors command output for errors. When detected, appends a structured entry to auto-memory with:
- The command that failed
- Error output (truncated)
- Timestamp and context
- Suggested category

**Token overhead:** Zero on success. ~30 tokens only when an error is detected.

## Platform Support

| Platform | Memory System | Plugin Works? |
|----------|--------------|---------------|
| Pi | Auto-memory (MEMORY.md) | ✅ Full support |
| OpenClaw | workspace/MEMORY.md | ✅ Adapted (reads workspace memory) |
| Codex CLI | AGENTS.md | ✅ Adapted (reads AGENTS.md patterns) |
| GitHub Copilot | `.github/copilot-instructions.md` | ⚠️ Manual promotion only |

## Related

- [Pi Memory Docs](https://code.claude.com/docs/en/memory)
- [pskoett/self-improving-agent](https://clawhub.ai/pskoett/self-improving-agent) — inspiration
- `playwright-pro` — sister plugin in this repo
