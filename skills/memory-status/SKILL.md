---
name: "memory-status"
description: "Health check of agent auto-memory: line counts, topic files, capacity, stale entries and what to prune. Use whenever the user asks how full or healthy memory is, or runs /skill:memory-status."
---

# /skill:memory-status — Memory Health Dashboard

Quick overview of your project's memory state across all memory systems.

## Usage

```
/skill:memory-status                    # Full dashboard
/skill:memory-status --brief            # One-line summary
```

## What It Reports

### Step 1: Locate all memory files

```bash
# Auto-memory directory
MEMORY_DIR="$HOME/.pi/projects/$(pwd | sed 's|/|%2F|g; s|%2F|/|; s|^/||')/memory"

# Count lines in MEMORY.md
wc -l "$MEMORY_DIR/MEMORY.md" 2>/dev/null || echo "0"

# List topic files
ls "$MEMORY_DIR/"*.md 2>/dev/null | grep -v MEMORY.md

# AGENTS.md
wc -l ./AGENTS.md 2>/dev/null || echo "0"
wc -l ~/.pi/agent/AGENTS.md 2>/dev/null || echo "0"

# Rules directory
ls .pi/rules/*.md 2>/dev/null | wc -l
```

### Step 2: Analyze capacity

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| MEMORY.md lines | < 120 | 120-180 | > 180 |
| AGENTS.md lines | < 150 | 150-200 | > 200 |
| Topic files | 0-3 | 4-6 | > 6 |
| Stale entries | 0 | 1-3 | > 3 |

### Step 3: Quick stale check

For each MEMORY.md entry that references a file path:
```bash
# Verify referenced files still exist
grep -oE '[a-zA-Z0-9_/.-]+\.(ts|js|py|md|json|yaml|yml)' "$MEMORY_DIR/MEMORY.md" | while read f; do
  [ ! -f "$f" ] && echo "STALE: $f"
done
```

### Step 4: Output

```
📊 Memory Status

  Auto-Memory (MEMORY.md):
    Lines:        {{n}}/200 ({{bar}}) {{emoji}}
    Topic files:  {{count}} ({{names}})
    Last updated: {{date}}

  Project Rules:
    AGENTS.md:    {{n}} lines
    Rules:        {{count}} files in .pi/rules/
    User global:  {{n}} lines (~/.pi/agent/AGENTS.md)

  Health:
    Capacity:     {{healthy/warning/critical}}
    Stale refs:   {{count}} (files no longer exist)
    Duplicates:   {{count}} (entries repeated across files)

  {{if recommendations}}
  💡 Recommendations:
    - {{recommendation}}
  {{endif}}
```

### Brief mode

```
/skill:memory-status --brief
```

Output: `📊 Memory: {{n}}/200 lines | {{count}} rules | {{status_emoji}} {{status_word}}`

## Interpretation

- **Green (< 60%)**: Plenty of room. Auto-memory is working well.
- **Yellow (60-90%)**: Getting full. Consider running `/skill:memory-review` to promote or clean up.
- **Red (> 90%)**: Near capacity. Auto-memory may start dropping older entries. Run `/skill:memory-review` now.

## Tips

- Run `/skill:memory-status --brief` as a quick check anytime
- If capacity is yellow+, run `/skill:memory-review` to identify promotion candidates
- Stale entries waste space — delete references to files that no longer exist
- Topic files are fine — Pi creates them to keep MEMORY.md under 200 lines
