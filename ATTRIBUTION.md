# Attribution

## alirezarezvani/claude-skills

394 skills, everything in `skills/` except `asd-ste100`.

- Source: https://github.com/alirezarezvani/claude-skills
- Commit converted: `4680893` (shallow clone of `main`, 2026-11-16)
- License: MIT, Copyright (c) 2025 Alireza Rezvani (see [LICENSE](LICENSE))
- Skills taken: 394 of the 417 `SKILL.md` trees in that repo. The 23 left out are byte-identical
  mirror copies, filed both under `<domain>/skills/<name>/` and
  `<domain>/<plugin>/skills/<name>/`.

## danyuchn/asd-ste100-skill

One skill, `skills/asd-ste100/`, the ASD-STE100 controlled-language rewriter with its stdlib linter.

- Source: https://github.com/danyuchn/asd-ste100-skill
- Commit converted: `9c35169` (shallow clone of `main`, 2026-11-16)
- License: MIT, Copyright (c) 2026 Dustin Yuchen Teng. The repo's own `LICENSE` ships inside the
  skill directory, so the copy is self-contained.
- Only the prose changed. `scripts/`, `references/` and `examples/` are byte-identical to upstream.
  `SKILL.md` and `README.md` differ only in the host references described below.

The changes are mechanical and each one is listed in
[`conversion-report.md`](conversion-report.md): host-agent references retargeted from Claude Code to
Pi, paths and commands rewritten, frontmatter normalised. The substance of the skill text is
untouched. No upstream file was edited either. The converter reads a clone in `.upstream/`
(gitignored) and writes `skills/`.

Individual skills keep their own provenance in frontmatter (`metadata.derived_from`,
`metadata.original_author`, `metadata.original_license`) and in their `README.md` and `references/`
files. `grill-me`, for instance, derives from Matt Pocock's MIT grill-me, and several
`c-level-advisor` skills cite vendor skill collections.

Upstream URLs that mention Claude (`github.com/alirezarezvani/claude-skills`, `code.claude.com`)
stay as they are: they are attribution and documentation links, not instructions aimed at the host
agent.
