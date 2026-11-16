# Git Worktree Manager

Production workflow for parallel branch development with isolated ports, env sync, and cleanup safety checks. This skill packages practical CLI tooling and operating guidance for multi-worktree teams.

## Quick Start

```bash
# Create + prepare a worktree
python3 scripts/worktree_manager.py \
  --repo . \
  --branch feature/api-hardening \
  --name wt-api-hardening \
  --base-branch main \
  --install-deps \
  --format text

# Review stale worktrees
python3 scripts/worktree_cleanup.py --repo . --stale-days 14 --format text
```

## Included Tools

- `scripts/worktree_manager.py`: create/list-prep workflow, deterministic ports, `.env*` sync, optional dependency install
- `scripts/worktree_cleanup.py`: stale/dirty/merged analysis with optional safe removal

Both support `--input <json-file>` and stdin JSON for automation.

## References

- `references/port-allocation-strategy.md`
- `references/docker-compose-patterns.md`

## Installation

This copy ships in
[pi.dev-converted-skills-collection](https://github.com/pixel3design-hub/pi.dev-converted-skills-collection).
Install it with `pi --skill ./skills/git-worktree-manager` from a clone of that repo, or copy this directory into
`~/.agents/skills/git-worktree-manager` to have it available in every project. The collection README lists the
other routes.

