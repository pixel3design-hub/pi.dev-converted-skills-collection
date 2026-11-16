# Pi Skill Collection (converted from claude-skills)

394 [Agent Skills](https://agentskills.io/specification) for [Pi](https://github.com/badlogic/pi-mono), converted from
[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (MIT, commit `4680893`).

Upstream targets Claude Code. The skills load in Pi as they are, because `SKILL.md` is the same
standard, but their instructions point at the wrong host: `.claude/` paths, `CLAUDE.md`,
`/plugin install`, plugin-namespaced commands, Claude tool names. This repo rewrites those and drops
23 duplicate mirror copies.

## Install

Pick one, by how much you want in your system prompt.

### One skill, for this project

Pi discovers skill directories recursively.

```bash
pi --skill ./skills/grill-me
```

### A few skills, for your user account

```bash
cp -r skills/{grill-me,session-handoff,handoff,self-improving-agent} ~/.agents/skills/
```

### Everything

Add the directory to `~/.pi/agent/settings.json`:

```json
{ "skills": ["<path-to-this-clone>/skills"] }
```

Pi inlines every skill's name, description and path into the system prompt, so all 394 add about
154 KB (roughly 38k tokens) to every session. Install the ones you use. `settings.json` resource
arrays also accept `!pattern` exclusions, in case you want one directory to hold more skills than
you want Pi to see.

After a `/reload`, each installed skill answers to `/skill:<name>`.

## What changed

| Upstream (Claude Code) | Here (Pi) |
|---|---|
| `CLAUDE.md`, `CLAUDE.local.md` | `AGENTS.md`, `AGENTS.local.md` |
| `~/.claude/`, `.claude/` | `~/.pi/agent/`, `.pi/` |
| `~/.claude/skills/` | `~/.agents/skills/` |
| `CLAUDE_CONFIG_DIR` | `PI_CODING_AGENT_DIR` |
| "Claude Code", "Claude" for the host agent | "Pi" |
| `/plugin install`, `/plugin marketplace` | removed, no Pi equivalent |
| `/cs:onboard`, `/executive-mentor:challenge` | `/skill:onboard`, `/skill:challenge` |
| `$ARGUMENTS` | "the user's request" |
| `Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob` | `read`, `write`, `edit`, `bash`, `grep`, `find` |
| `Task`, `WebFetch`, `WebSearch`, `AskUserQuestion` | `Agent`, `ninerouter_web_fetch`, `ninerouter_web_search`, `ask_user_question` |
| `{skill_path}/scripts/x.py` | `scripts/x.py` |
| `${CLAUDE_PLUGIN_ROOT}/vendor/<skill>/x` | `../<skill>/x` |
| `tools:`, `context:` (Claude agent fields) | dropped |
| `version:`, `domain:`, `model:` and other scalars | moved into `metadata:` |

Frontmatter comes out with the Agent Skills fields plus `metadata`. Names are lowercase with
hyphens, directories match names, descriptions are one line of at most 1024 characters.

## Left alone on purpose

Code samples keep their Claude references. `claude --print` or a Python parser that reads
`~/.claude/projects` stays as written, since renaming a CLI that Pi does not have would break the
example. That covers 91 occurrences.

Scripts and configs inside each skill (`.py`, `.json`, `.sh`) were not rewritten either, which
leaves 462.

Upstream attribution and URLs (`claude-skills`, `code.claude.com`, `docs.claude.com`) stay because
MIT requires it, and a link to the real docs beats a dead one. Model IDs such as `claude-sonnet-5`
and third-party product names such as `ClaudeBot`, `claude-coach` and `claude-sessions` stay too.

Three skills are about Claude Code machinery rather than written for it: `coding-agent-rollout`,
`extract` and `workflow-builder`. Their prose says Pi now, but the hooks, settings and plugin
internals they document have no Pi equivalent. Read those sections as Claude Code notes.

`conversion-report.md` lists each of these per skill, with the rule counts and the 23 skipped
duplicates.

## Regenerate

```bash
git clone --depth 1 https://github.com/alirezarezvani/claude-skills.git .upstream
python3 scripts/convert.py           # .upstream -> skills/ + conversion-report.md
python3 scripts/convert.py --check   # name, description and duplicate gate
python3 scripts/convert.py --audit   # residual `claude` references, allowlisted
```

Both gates exit non-zero on failure and use only the standard library.

## Layout

```
skills/<name>/SKILL.md    394 skills, each with its own scripts/, references/, templates/, assets/
scripts/convert.py        the converter and its two gates
conversion-report.md      per-skill changes, duplicates, residual references
ATTRIBUTION.md            upstream source, commit and license
LICENSE                   MIT, upstream copyright
```

## Verification

On the committed tree, `--check` reports 394 skills and no problems, and `--audit` reports no
unexpected references and no description that mentions Claude. Loading the same tree through Pi's
own `loadSkills` gives 394 skills, no diagnostics and no name collisions.

## License

MIT, see [LICENSE](LICENSE). Copyright for the upstream skills is Alireza Rezvani's. Individual
skills keep their own `license:` field and `metadata.derived_from` where they derive from other MIT
projects.
