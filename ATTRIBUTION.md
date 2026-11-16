# Attribution

Every skill in `skills/` comes from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills).

- Source: https://github.com/alirezarezvani/claude-skills
- Commit converted: `4680893` (shallow clone of `main`, 2026-11-16)
- License: MIT, Copyright (c) 2025 Alireza Rezvani (see [LICENSE](LICENSE))
- Skills here: 394 of the 417 `SKILL.md` trees in the repo. The 23 left out are byte-identical
  mirror copies, filed both under `<domain>/skills/<name>/` and
  `<domain>/<plugin>/skills/<name>/`.

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
