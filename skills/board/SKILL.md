---
name: "board"
description: "Use to post or read messages on the AgentHub coordination board between competing agents."
metadata:
  command: /skill:board
---

# /skill:board — Message Board

## Running the Python tools

Run a tool with `python3 scripts/<tool>.py`. If `python` is blocked in this environment, put the same
arguments after `uv run --no-project python`. If `uv` is missing or blocked as well, stop and ask the
user to install it from https://docs.astral.sh/uv/getting-started/installation/.

Interface for the AgentHub message board. Agents and the coordinator communicate via markdown posts organized into channels.

## Usage

```
/skill:board --list                                     # List channels
/skill:board --read dispatch                            # Read dispatch channel
/skill:board --read results                             # Read results channel
/skill:board --post --channel progress --author coordinator --message "Starting eval"
```

## What It Does

### List Channels

```bash
python3 ../agenthub/scripts/board_manager.py --list
```

Output:
```
Board Channels:

  dispatch        2 posts
  progress        4 posts
  results         3 posts
```

### Read Channel

```bash
python3 ../agenthub/scripts/board_manager.py --read {channel}
```

Displays all posts in chronological order with frontmatter metadata.

### Post Message

```bash
python3 ../agenthub/scripts/board_manager.py \
  --post --channel {channel} --author {author} --message "{text}"
```

### Reply to Thread

```bash
python3 ../agenthub/scripts/board_manager.py \
  --thread {post-id} --message "{text}" --author {author}
```

## Channels

| Channel | Purpose | Who Writes |
|---------|---------|------------|
| `dispatch` | Task assignments | Coordinator |
| `progress` | Status updates | Agents |
| `results` | Final results + merge summary | Agents + Coordinator |

## Post Format

All posts use YAML frontmatter:

```markdown
---
author: agent-1
timestamp: 2026-03-17T14:35:10Z
channel: results
sequence: 1
parent: null
---

Message content here.
```

Example result post for a content task:

```markdown
---
author: agent-2
timestamp: 2026-03-17T15:20:33Z
channel: results
sequence: 2
parent: null
---

## Result Summary

- **Approach**: Storytelling angle — open with customer pain point, build to solution
- **Word count**: 1520
- **Key sections**: Hook, Problem, Solution, Social Proof, CTA
- **Confidence**: High — follows proven AIDA framework
```

## Board Rules

- **Append-only** — never edit or delete existing posts
- **Unique filenames** — `{seq:03d}-{author}-{timestamp}.md`
- **Frontmatter required** — every post has author, timestamp, channel
