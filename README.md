# Pi Skill Collection (converted from claude-skills)

394 [Agent Skills](https://agentskills.io/specification) for [Pi](https://github.com/badlogic/pi-mono), converted from
[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (MIT, commit `4680893`).

The upstream collection was written for Claude Code. Skills load fine in Pi as-is (`SKILL.md` is the
same standard), but their instructions pointed at a host that isn't Pi: `.claude/` paths,
`CLAUDE.md`, `/plugin install`, plugin-namespaced commands, Claude tool names. This repo fixes that
and drops the 23 duplicate mirror copies.

## Install

Any one of these, depending on how much you want in your system prompt.

**One skill, for this project** — Pi discovers directories recursively:

```bash
pi --skill ./skills/grill-me
```

**A domain for your user account:**

```bash
cp -r skills/{grill-me,session-handoff,handoff,self-improving-agent} ~/.agents/skills/
```

**Everything** — add the directory to `~/.pi/agent/settings.json`:

```json
{ "skills": ["<path-to-this-clone>/skills"] }
```

**Cost warning:** Pi inlines every skill's name, description and path into the system prompt.
All 394 skills add ~154 KB (~38k tokens) to *every* session. Install the ones you use, or point
Pi at a subset; `settings.json` resource arrays also accept `!pattern` exclusions.

Each skill is invocable as `/skill:<name>` after a `/reload`.

## What changed

| Upstream (Claude Code) | Here (Pi) |
|---|---|
| `CLAUDE.md`, `CLAUDE.local.md` | `AGENTS.md`, `AGENTS.local.md` |
| `~/.claude/`, `.claude/` | `~/.pi/agent/`, `.pi/` |
| `~/.claude/skills/` | `~/.agents/skills/` |
| `CLAUDE_CONFIG_DIR` | `PI_CODING_AGENT_DIR` |
| "Claude Code", "Claude" (the host agent) | "Pi" |
| `/plugin install …`, `/plugin marketplace …` | removed (no Pi equivalent) |
| `/cs:onboard`, `/executive-mentor:challenge`, … | `/skill:onboard`, `/skill:challenge`, … |
| `$ARGUMENTS` | "the user's request" |
| `Read`/`Write`/`Edit`/`Bash`/`Grep`/`Glob` tool names | `read`/`write`/`edit`/`bash`/`grep`/`find` |
| `Task` tool, `WebFetch`, `WebSearch`, `AskUserQuestion` | `Agent`, `ninerouter_web_fetch`, `ninerouter_web_search`, `ask_user_question` |
| `{skill_path}/scripts/x.py`, `${CLAUDE_PLUGIN_ROOT}/…` | `scripts/x.py`, `../<sibling-skill>/…` |
| `tools:`, `context:` frontmatter (Claude agent vocabulary) | dropped |
| `version:`, `domain:`, `model:` and other scalars | folded into `metadata:` |

Frontmatter is normalised to the Agent Skills fields plus `metadata`; names are lowercase-hyphen,
directories match names, descriptions are single-line and ≤1024 chars.

## Deliberately left alone

- **Code samples.** `claude --print …` or a Python parser that reads `~/.claude/projects` stays as
  written — renaming a CLI that doesn't exist in Pi would only break the example. 91 occurrences.
- **Scripts and configs** inside each skill (`.py`, `.json`, `.sh`): not rewritten. 462 occurrences.
- **Upstream attribution and URLs** (`claude-skills`, `code.claude.com`, `docs.claude.com`) — MIT
  requires keeping them, and a doc link that 404s is still more useful than a fake one.
- **Model IDs** (`claude-sonnet-5`) and third-party product names (`ClaudeBot`, `claude-coach`,
  `claude-sessions`).
- Skills whose *subject matter* is Claude Code machinery still carry Claude-Code-specific detail:
  `coding-agent-rollout`, `extract`, `workflow-builder`. Their prose now says Pi and their
  hook/settings/plugin internals have no Pi equivalent — treat those parts as Claude Code notes.

Every one of the above is enumerated in [`conversion-report.md`](conversion-report.md), including
per-skill rule hits and the 23 duplicates that were skipped.

## Regenerate

```bash
git clone --depth 1 https://github.com/alirezarezvani/claude-skills.git .upstream
python3 scripts/convert.py        # .upstream -> skills/ + conversion-report.md
python3 scripts/convert.py --check   # name/description/duplicate gate
python3 scripts/convert.py --audit   # residual `claude` references, allowlisted
```

`--check` and `--audit` exit non-zero on failure. Both are stdlib-only; no dependencies.

## Layout

```
skills/<name>/SKILL.md    394 skills, each self-contained (scripts/, references/, templates/, assets/)
scripts/convert.py        the converter and its two gates
conversion-report.md      per-skill changes, duplicates, residual references
ATTRIBUTION.md            upstream source, commit and license
LICENSE                   MIT, upstream copyright
```

## Tests

- `scripts/convert.py --check` → 394 skills, 0 problems.
- `scripts/convert.py --audit` → 0 unexpected references, 0 descriptions mentioning Claude.
- Loaded with Pi's own loader (`loadSkills` from `@earendil-works/pi-coding-agent`):
  394 skills, 0 diagnostics, 0 collisions.

## License

MIT, see [LICENSE](LICENSE). Upstream copyright Alireza Rezvani; individual skills keep their own
`license:` field and `metadata.derived_from` where they derive from other MIT projects.
