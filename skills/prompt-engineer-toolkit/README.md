# Prompt Engineer Toolkit

Production toolkit for evaluating and versioning prompts with measurable quality signals. Includes A/B testing automation and prompt history management with diffs.

## Quick Start

```bash
# Run A/B prompt evaluation
python3 scripts/prompt_tester.py \
  --prompt-a-file prompts/a.txt \
  --prompt-b-file prompts/b.txt \
  --cases-file testcases.json \
  --format text

# Store a prompt version
python3 scripts/prompt_versioner.py add \
  --name support_classifier \
  --prompt-file prompts/a.txt \
  --author team
```

## Included Tools

- `scripts/prompt_tester.py`: A/B testing with per-case scoring and aggregate winner
- `scripts/prompt_versioner.py`: prompt history (`add`, `list`, `diff`, `changelog`) in local JSONL store

## References

- `references/prompt-templates.md`
- `references/technique-guide.md`
- `references/evaluation-rubric.md`

## Installation

This copy ships in
[pi.dev-converted-skills-collection](https://github.com/pixel3design-hub/pi.dev-converted-skills-collection).
Install it with `pi --skill ./skills/prompt-engineer-toolkit` from a clone of that repo, or copy this directory into
`~/.agents/skills/prompt-engineer-toolkit` to have it available in every project. The collection README lists the
other routes.

