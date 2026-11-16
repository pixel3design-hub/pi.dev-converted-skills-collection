# CI/CD Pipeline Builder

Detects your repository stack and generates practical CI pipeline templates for GitHub Actions and GitLab CI. Designed as a fast baseline you can extend with deployment controls.

## Quick Start

```bash
# Detect stack
python3 scripts/stack_detector.py --repo . --format json > stack.json

# Generate GitHub Actions workflow
python3 scripts/pipeline_generator.py \
  --input stack.json \
  --platform github \
  --output .github/workflows/ci.yml \
  --format text
```

## Included Tools

- `scripts/stack_detector.py`: repository signal detection with JSON/text output
- `scripts/pipeline_generator.py`: generate GitHub/GitLab CI YAML from detection payload

## References

- `references/github-actions-templates.md`
- `references/gitlab-ci-templates.md`
- `references/deployment-gates.md`

## Installation

This copy ships in
[pi.dev-converted-skills-collection](https://github.com/pixel3design-hub/pi.dev-converted-skills-collection).
Install it with `pi --skill ./skills/ci-cd-pipeline-builder` from a clone of that repo, or copy this directory into
`~/.agents/skills/ci-cd-pipeline-builder` to have it available in every project. The collection README lists the
other routes.

