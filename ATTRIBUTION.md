# Attribution

All skill content in `skills/` comes from **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)**.

- Source: https://github.com/alirezarezvani/claude-skills
- Commit converted: `4680893` (shallow clone of `main`, 2026-11-16)
- License: MIT, Copyright (c) 2025 Alireza Rezvani (see [LICENSE](LICENSE))
- Skills in this repo: 394 of 417 `SKILL.md` trees; the 23 skipped are byte-identical mirror
  copies under `<domain>/skills/<name>/` vs `<domain>/<plugin>/skills/<name>/`.

Changes are mechanical and listed in [`conversion-report.md`](conversion-report.md):
host-agent references retargeted from Claude Code to Pi, paths and commands rewritten, frontmatter
normalised. No skill content was rewritten in substance, and no upstream file was modified — the
converter reads a clone in `.upstream/` (gitignored) and writes `skills/`.

Individual skills also carry their own provenance, preserved verbatim in frontmatter
`metadata.derived_from` / `metadata.original_author` / `metadata.original_license` and in their
`README.md`/`references/` files. Examples: `grill-me` derives from Matt Pocock's MIT grill-me;
several `c-level-advisor` skills cite vendor skill collections.

Upstream URLs mentioning Claude (`github.com/alirezarezvani/claude-skills`, `code.claude.com`) are
kept on purpose: they are attribution and documentation links, not host-agent instructions.
