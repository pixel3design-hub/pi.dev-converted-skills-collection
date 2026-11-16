# MCP Server Builder

Generate and validate MCP servers from OpenAPI contracts with production-focused tooling. This skill helps teams bootstrap fast and enforce schema quality before shipping.

## Quick Start

```bash
# Generate scaffold from OpenAPI
python3 scripts/openapi_to_mcp.py \
  --input openapi.json \
  --server-name my-mcp \
  --language python \
  --output-dir ./generated \
  --format text

# Validate generated manifest
python3 scripts/mcp_validator.py --input generated/tool_manifest.json --strict --format text
```

## Included Tools

- `scripts/openapi_to_mcp.py`: OpenAPI -> `tool_manifest.json` + starter server scaffold
- `scripts/mcp_validator.py`: structural and quality validation for MCP tool definitions

## References

- `references/openapi-extraction-guide.md`
- `references/python-server-template.md`
- `references/typescript-server-template.md`
- `references/validation-checklist.md`

## Installation

This copy ships in
[pi.dev-converted-skills-collection](https://github.com/pixel3design-hub/pi.dev-converted-skills-collection).
Install it with `pi --skill ./skills/mcp-server-builder` from a clone of that repo, or copy this directory into
`~/.agents/skills/mcp-server-builder` to have it available in every project. The collection README lists the
other routes.

