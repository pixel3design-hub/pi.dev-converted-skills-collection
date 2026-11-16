#!/usr/bin/env python3
"""Convert alirezarezvani/claude-skills (agentskills.io SKILL.md trees) into Pi skills.

    python3 scripts/convert.py            # convert .upstream -> skills/
    python3 scripts/convert.py --check    # validate skills/ (exit 1 on failure)

What it changes:
  * frontmatter: name slugified, description flattened/limited to 1024, Claude-only
    keys (tools, context) dropped, unknown keys folded into metadata
  * prose: Claude host-agent references -> Pi, .claude/ paths -> pi paths,
    CLAUDE.md -> AGENTS.md, /ns:cmd -> /skill:cmd, Claude tool names -> pi tool names
  * kept on purpose: upstream URLs/attribution, model IDs, third-party names
"""

import argparse
import hashlib
import os
import re
import shutil
import sys

EXCLUDE_DIRS = {
    ".git", ".claude", ".codex", ".codex-plugin", ".gemini", ".hermes",
    ".vibe", "integrations", "docs",
}
KEEP_KEYS = ("name", "description", "license", "compatibility", "disable-model-invocation")
DROP_KEYS = ("allowed-tools", "tools", "context")  # Claude agent/subagent vocabulary
MAX_NAME, MAX_DESC = 64, 1024

PI_TOOL = {
    "Read": "read", "Write": "write", "Edit": "edit", "MultiEdit": "edit",
    "NotebookEdit": "edit", "Bash": "bash", "Grep": "grep", "Glob": "find",
    "Task": "Agent", "WebFetch": "ninerouter_web_fetch",
    "WebSearch": "ninerouter_web_search", "TodoWrite": "scratchpad",
    "AskUserQuestion": "ask_user_question", "SlashCommand": None, "Skill": None,
}

NS_RULE = (r"(?<![\w/:.])/([a-z][a-z0-9-]*):([a-z][a-z0-9-]*)", r"/skill:\2", "command:namespace")

# Applied everywhere, code fences included (paths in shell examples must work too).
# `${CLAUDE_PLUGIN_ROOT}/...` is handled per skill by rewrite_plugin_paths().
RULES_ANY = [
    (r"~/\.claude/skills", "~/.agents/skills", "path:user-skills"),
    (r"\$HOME/\.claude/skills", "$HOME/.agents/skills", "path:user-skills"),
    (r"~/\.claude/CLAUDE\.md", "~/.pi/agent/AGENTS.md", "path:user-context"),
    (r"~/\.claude", "~/.pi/agent", "path:user-dir"),
    (r"\{skill_path\}/", "", "path:skill_path"),
    (r"\{skill_path\}", ".", "path:skill_path"),
    (r"\.claude/skills", ".agents/skills", "path:project-skills"),
    (r"\.claude/", ".pi/", "path:project-dir"),
    (r"CLAUDE\.local\.md", "AGENTS.local.md", "file:CLAUDE.local.md"),
    (r"CLAUDE\.md", "AGENTS.md", "file:CLAUDE.md"),
    (r"CLAUDE_CONFIG_DIR", "PI_CODING_AGENT_DIR", "env:config-dir"),
    NS_RULE,
    (r"\$ARGUMENTS", "the user's request", "arg:ARGUMENTS"),
]

# `${CLAUDE_PLUGIN_ROOT}/vendor/<domain>/<skill>/x` and `.../skills/<skill>/x` point at
# sibling skills; after flattening they are `../<skill>/x` (`x` for the skill itself).
PLUGIN_PATH = re.compile(
    r"\$\{CLAUDE_PLUGIN_ROOT\}/(?:vendor/[A-Za-z0-9._-]+/|skills/)?"
    r"([A-Za-z0-9._-]+)((?:/[^\s)`\"'\],]*)?)")
SKILL_NAMES = set()
SCRIPT_OWNER = {}  # basename.py -> skill that ships it, only when unambiguous

SKILL_PATH = re.compile(r"\{skill_path\}/scripts/([A-Za-z0-9_.-]+\.py)")


def rewrite_plugin_paths(text, current, hits):
    def localise(m):
        basename = m.group(1)
        owner = SCRIPT_OWNER.get(basename)
        if owner is None:
            return f"scripts/{basename}"
        if owner == current:
            hits["path:skill_path"] = hits.get("path:skill_path", 0) + 1
            return f"scripts/{basename}"
        hits["path:skill_path-xref"] = hits.get("path:skill_path-xref", 0) + 1
        return f"../{owner}/scripts/{basename}"

    text = SKILL_PATH.sub(localise, text)

    def swap(m):
        ident, rest = m.group(1), m.group(2) or ""
        if ident == current:
            return rest.lstrip("/") or "."
        if ident in SKILL_NAMES:
            hits["path:cross-skill"] = hits.get("path:cross-skill", 0) + 1
            return f"../{ident}{rest}"
        hits["path:plugin-root-unresolved"] = hits.get("path:plugin-root-unresolved", 0) + 1
        return f"{ident}{rest}"
    return PLUGIN_PATH.sub(swap, text)

# Applied only outside code fences: English prose, where a blind swap mangles
# ordinary words ("Task assignments", "Read the verdict").
RULES_PROSE = [
    (r"Claude Code", "Pi", "host:Claude Code"),
    (r"\bClaude\b", "Pi", "host:Claude"),
    (r"\bclaude\b(?![-./])", "pi", "host:claude"),
    (r"\b(%s) tool\b" % "|".join(PI_TOOL), lambda m: f"{PI_TOOL[m.group(1)]} tool", "tool:phrase"),
    (r"`(%s)`" % "|".join(k for k in PI_TOOL if k not in ("Task", "Skill")),
     lambda m: f"`{PI_TOOL[m.group(1)]}`", "tool:backtick"),
]

# Skills that run bundled Python tools get a fallback note: some environments
# block bare `python`, and `uv run --no-project python` is the drop-in they do allow.
PY_RUN = re.compile(r"(?<![\w-])python3?[ \t]+(?:-m\b|\S*\.py\b|scripts?/)")
PY_NOTE = """## Running the Python tools

Run a tool with `python3 scripts/<tool>.py`. If `python` is blocked in this environment, put the same
arguments after `uv run --no-project python`. If `uv` is missing or blocked as well, stop and ask the
user to install it from https://docs.astral.sh/uv/getting-started/installation/."""


def ships_python(skill_dir, body):
    """Does this skill run Python: a bundled .py file, or a python command in its text?"""
    if PY_RUN.search(body):
        return True
    return any(f.endswith(".py") for _, _, fns in os.walk(skill_dir) for f in fns)


def insert_python_note(body, hits):
    hits["note:python-fallback"] = hits.get("note:python-fallback", 0) + 1
    m = re.search(r"^# .*$", body, re.M)
    at = m.end() if m else 0
    return body[:at] + "\n\n" + PY_NOTE + "\n\n" + body[at:].lstrip("\n")


# Claude plugin install instructions have no Pi equivalent.
PLUGIN_LINE = re.compile(r"^\s*(?:[-*]\s*)?(?:\*\*)?`?/plugin (?:install|marketplace)\b.*$", re.M)
FENCE = re.compile(r"^```.*?^```", re.M | re.S)


def split_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, text


def parse_entries(fm_lines):
    """[(key, value, [continuation lines])] — continuation = indented/block lines."""
    entries, cur = [], None
    for line in fm_lines:
        m = re.match(r"^([A-Za-z0-9_.-]+):(.*)$", line)
        if m:
            cur = [m.group(1), m.group(2).strip(), []]
            entries.append(cur)
        elif cur is not None and (line.startswith((" ", "\t")) or line.strip() == ""):
            cur[2].append(line)
    return entries


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return value


def quote(value):
    return '"%s"' % value.replace("\\", "\\\\").replace('"', '\\"')


def yaml_val(value):
    if value == "" or re.search(r"[:#]|^\s|\s$|^[\"'\[\]{}>|&*!%@`]", value):
        return quote(value)
    return value


def block_scalar(cont):
    return " ".join(l.strip() for l in cont if l.strip())


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return re.sub(r"-{2,}", "-", s)[:MAX_NAME].strip("-")


def apply_rules(text, rules):
    for pattern, repl, label in rules:
        text = re.sub(pattern, repl, text)
    return text


def convert_body(body, hits):
    """Rules_ANY everywhere, rules_PROSE only outside fenced code blocks."""
    def count(rules):
        for pattern, _, label in rules:
            hits[label] = hits.get(label, 0) + len(re.findall(pattern, body))
    count(RULES_ANY)
    plain = FENCE.split(body)
    for pattern, _, label in RULES_PROSE:
        hits[label] = hits.get(label, 0) + sum(len(re.findall(pattern, c)) for c in plain)

    body = apply_rules(body, RULES_ANY)
    out, last = [], 0
    for fence in FENCE.finditer(body):
        out.append(apply_rules(body[last:fence.start()], RULES_PROSE))
        out.append(fence.group(0))
        last = fence.end()
    out.append(apply_rules(body[last:], RULES_PROSE))
    return "".join(out)


def convert_skill(skill_dir, hits):
    path = os.path.join(skill_dir, "SKILL.md")
    raw = open(path, encoding="utf-8", errors="replace").read()
    fm_lines, body = split_frontmatter(raw)
    entries = parse_entries(fm_lines or [])

    fields, meta, notes = {}, [], []
    for key, value, cont in entries:
        if key == "metadata":
            meta.extend(re.sub(NS_RULE[0], NS_RULE[1], l) for l in cont)
            continue
        if key in DROP_KEYS:
            notes.append(f"dropped `{key}`")
            continue
        if key in KEEP_KEYS:
            fields[key] = (value, cont)
        else:
            val = value if value else block_scalar(cont)
            meta.append(f"  {key}: {yaml_val(val)}")
            notes.append(f"folded `{key}` into metadata")

    name = slugify(unquote(fields.get("name", ("", []))[0]) or os.path.basename(skill_dir))
    desc = unquote(fields.get("description", ("", []))[0]) or block_scalar(fields.get("description", ("", []))[1])
    desc = " ".join(desc.split())
    if len(desc) > MAX_DESC:
        desc = desc[:MAX_DESC].rsplit(" ", 1)[0] + "…"
        notes.append("description truncated")

    desc_hits = {}
    for rules in (RULES_ANY, RULES_PROSE):
        for pattern, _, label in rules:
            if re.search(pattern, desc):
                desc_hits[label] = 1
        desc = apply_rules(desc, rules)
    hits.update({k: v for k, v in desc_hits.items()})

    body = rewrite_plugin_paths(body, name, hits)
    body = PLUGIN_LINE.sub("", convert_body(body, hits))
    if ships_python(skill_dir, body + "\n" + desc):
        body = insert_python_note(body, hits)

    head = [f"name: {quote(name)}", f"description: {quote(desc)}"]
    for key in ("license", "compatibility"):
        if key in fields:
            head.append(f"{key}: {fields[key][0]}")
    if fields.get("disable-model-invocation", ("", []))[0] == "true":
        head.append("disable-model-invocation: true")
    if meta:
        head.append("metadata:")
        head.extend(meta)

    return name, "---\n" + "\n".join(head) + "\n---\n" + body.rstrip("\n") + "\n", notes


def discover(src):
    found = []
    for dirpath, dirnames, filenames in os.walk(src):
        rel = os.path.relpath(dirpath, src)
        if rel != "." and any(p in EXCLUDE_DIRS for p in rel.split(os.sep)):
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")]
        if "SKILL.md" in filenames and rel != ".":
            found.append(dirpath)
    return sorted(found)


def planned_names(dirs):
    names = set()
    for d in dirs:
        fm, _ = split_frontmatter(open(os.path.join(d, "SKILL.md"), encoding="utf-8", errors="replace").read())
        fields = {k: v for k, v, _ in parse_entries(fm or [])}
        names.add(slugify(unquote(fields.get("name", "")) or os.path.basename(d)))
    return names


def convert(srcs, out):
    """srcs: list of source roots; several repos convert into one flat tree."""
    dirs = [(src, d) for src in srcs for d in discover(src)]
    SKILL_NAMES.update(planned_names([d for _, d in dirs]))
    owners = {}
    for _, d in dirs:
        for _, _, fns in os.walk(d):
            for f in fns:
                if f.endswith(".py"):
                    owners.setdefault(f, set()).add(os.path.basename(d))
    SCRIPT_OWNER.update({f: next(iter(o)) for f, o in owners.items() if len(o) == 1})
    skills, report, seen = [], [], {}
    for src, skill_dir in dirs:
        rel = os.path.relpath(skill_dir, src)
        hits, notes = {}, []
        name, text, notes = convert_skill(skill_dir, hits)
        digest = hashlib.sha256(text.encode()).hexdigest()[:12]
        if name in seen:
            kind = "identical mirror" if seen[name] == digest else "CONFLICT (different content)"
            report.append(f"- `{src}/{rel}` -> skipped, duplicate of `{seen[name + '/src']}` ({kind})")
            continue
        seen[name] = digest
        seen[name + "/src"] = f"{src}/{rel}"

        dst = os.path.join(out, name)
        os.makedirs(dst, exist_ok=True)
        open(os.path.join(dst, "SKILL.md"), "w", encoding="utf-8").write(text)
        extra = 0
        for dirpath, dirnames, filenames in os.walk(skill_dir):
            # Claude packaging (.claude-plugin/, .gitignore) is not skill content.
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for fn in filenames:
                if fn.startswith("."):
                    continue
                s = os.path.join(dirpath, fn)
                if s == os.path.join(skill_dir, "SKILL.md"):
                    continue
                frel = os.path.relpath(s, skill_dir)
                d = os.path.join(dst, frel)
                os.makedirs(os.path.dirname(d), exist_ok=True)
                if fn.endswith((".md", ".txt")):
                    sub_hits = {}
                    txt = convert_body(open(s, encoding="utf-8", errors="replace").read(), sub_hits)
                    txt = rewrite_plugin_paths(txt, name, hits)
                    open(d, "w", encoding="utf-8").write(PLUGIN_LINE.sub("", txt))
                    for k, v in sub_hits.items():
                        hits[k] = hits.get(k, 0) + v
                else:
                    shutil.copy2(s, d)
                extra += 1
        skills.append((name, f"{src}/{rel}", hits, notes, extra))
    return skills, report


def check(out):
    problems, names = [], []
    for entry in sorted(os.listdir(out)):
        d = os.path.join(out, entry)
        p = os.path.join(d, "SKILL.md")
        if not os.path.isfile(p):
            problems.append(f"{entry}: no SKILL.md")
            continue
        fm, _ = split_frontmatter(open(p, encoding="utf-8", errors="replace").read())
        if fm is None:
            problems.append(f"{entry}: missing frontmatter")
            continue
        fields = {k: v for k, v, _ in parse_entries(fm)}
        name = unquote(fields.get("name", ""))
        desc = unquote(fields.get("description", ""))
        names.append(name)
        if name != entry:
            problems.append(f"{entry}: name {name!r} != directory")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > MAX_NAME:
            problems.append(f"{entry}: invalid name {name!r}")
        if not desc.strip():
            problems.append(f"{entry}: empty description")
        if len(desc) > MAX_DESC:
            problems.append(f"{entry}: description {len(desc)} chars")
    dups = {n for n in names if names.count(n) > 1}
    if dups:
        problems.append(f"duplicate names: {sorted(dups)}")
    return len(names), problems


def audit(out):
    """Residual `claude` references, split into code / untouched files / allowlist."""
    allow = [
        r"claude-skills[\w./-]*", r"claude-code[\w./-]*", r"claude-code-skills",
        r"(?:[\w-]+\.)*claude\.com[\w./-]*", r"(?:[\w-]+\.)*claude\.ai", r"com\.anthropic\.claudecode",
        r"claude-(?:\d|sonnet|opus|haiku)[\w.-]*", r"claudebot", r"claudecode[\w./-]*",
        r"claude(?:-|_)(?:coach|sessions?|diary|memory-compiler|code-workflow-creator|plugins-official|home|directory)",
        r"claude_(?:md_layering_audit\.py|code[\w.]*)", r"claudebin", r"claude\.json", r"claudefa\.st[\w./-]*",
        r"\.?claude-plugin[\w./-]*", r"claude-(?:managed-agents|api[\w./-]*|mcp-tools|plugin-development|deep-research)",
        r"build-with-claude[\w./-]*", r"claude/handoff[\w-]*", r"claude_plugin_root", r"claude",
    ]
    # Skills whose subject matter IS Claude Code machinery: flag, don't fake a rewrite.
    host_specific = re.compile(r"claude_code[\w.]*|claude-plugin[\w./-]*|claudecode[\w./-]*")
    allow = [re.compile(a) for a in allow]
    fence = re.compile(r"^```.*?^```", re.M | re.S)
    token = re.compile(r"(?i)[\w.-]*claude[\w./-]*")
    counts = {"code sample": 0, "untouched file": 0, "allowlisted": 0, "UNEXPECTED": 0}
    unexpected, flagged, unsafe_desc = [], {}, []
    for dirpath, _, filenames in os.walk(out):
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            text = open(path, encoding="utf-8", errors="replace").read()
            skill = path.split(os.sep)[1]
            if fn == "SKILL.md":
                desc = re.search(r'^description: "(.*)"$', text, re.M)
                if desc and token.search(desc.group(1)):
                    unsafe_desc.append(skill)
            if not token.search(text):
                continue
            prose = fn.endswith((".md", ".txt"))
            if prose:
                counts["code sample"] += sum(len(token.findall(f.group(0))) for f in fence.finditer(text))
                text = fence.sub(lambda m: " " * len(m.group(0)), text)
            for m in token.finditer(text):
                tok = m.group(0)
                if not prose:
                    counts["untouched file"] += 1
                elif any(a.fullmatch(tok.lower()) for a in allow):
                    counts["allowlisted"] += 1
                    if host_specific.fullmatch(tok.lower()):
                        flagged[skill] = flagged.get(skill, 0) + 1
                else:
                    counts["UNEXPECTED"] += 1
                    line = text[:m.start()].count("\n") + 1
                    unexpected.append(f"{path}:{line}: {tok}")
    return counts, unexpected, flagged, unsafe_desc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", action="append", metavar="DIR",
                    help="repo root to convert; repeat for several sources (default .upstream)")
    ap.add_argument("--out", default="skills")
    ap.add_argument("--report", default="conversion-report.md")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--audit", action="store_true")
    args = ap.parse_args()

    if args.audit:
        counts, unexpected, flagged, unsafe_desc = audit(args.out)
        for k, v in counts.items():
            print(f"{k:16} {v}")
        print(f"descriptions mentioning claude: {len(unsafe_desc)} {unsafe_desc}")
        print(f"skills flagged host-specific: {len(flagged)}")
        for k in sorted(flagged):
            print(f"  · {k} ({flagged[k]})")
        for line in unexpected[:40]:
            print("  ✗", line)
        return 1 if unexpected or unsafe_desc else 0

    if args.check:
        total, problems = check(args.out)
        print(f"checked {total} skills, {len(problems)} problems")
        for p in problems[:40]:
            print("  ✗", p)
        return 1 if problems else 0

    if os.path.isdir(args.out):
        shutil.rmtree(args.out)
    os.makedirs(args.out)
    srcs = args.src or [".upstream"]
    skills, dups = convert(srcs, args.out)

    totals = {}
    for _, _, hits, _, _ in skills:
        for k, v in hits.items():
            totals[k] = totals.get(k, 0) + v
    src_list = ", ".join("`%s`" % src for src in srcs)
    lines = ["# Conversion report", "",
             f"Sources: {src_list} · skills converted: {len(skills)} · "
             f"duplicates skipped: {len(dups)}", "", "## Rule hits", "",
             "| rule | occurrences |", "|---|---|"]
    lines += [f"| `{k}` | {v} |" for k, v in sorted(totals.items(), key=lambda kv: -kv[1])]
    lines += ["", "## Duplicates skipped", ""] + (dups or ["none"]) + [
        "", "## Per skill", "", "| skill | source | files | rules applied | notes |",
        "|---|---|---|---|---|"]
    for name, src, hits, notes, extra in skills:
        applied = ", ".join(f"{k}×{v}" for k, v in sorted(hits.items()) if v) or "—"
        lines.append(f"| `{name}` | `{src}` | {extra} | {applied} | {'; '.join(notes) or '—'} |")
    counts, unexpected, flagged, unsafe_desc = audit(args.out)
    lines += ["", "## Residual `claude` references", "",
              "| category | count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in counts.items()]
    lines += ["", "Code samples and non-`.md` files keep their Claude references on purpose "
              "(rewriting `claude --print` or a Python parser would break them).", ""]
    if flagged:
        lines += ["### Skills whose subject matter is Claude Code machinery", "",
                  "Their guidance was rewritten to Pi mechanically; the steps that depend on "
                  "Claude Code hook/settings/plugin internals have no Pi equivalent.", "",
                  "| skill | host-specific refs |", "|---|---|"]
        lines += [f"| `{k}` | {v} |" for k, v in sorted(flagged.items())]
        lines.append("")
    if unexpected:
        lines += ["### UNEXPECTED references", ""] + [f"- `{u}`" for u in unexpected]
    lines.append(f"\nDescriptions mentioning Claude: {len(unsafe_desc)}")
    open(args.report, "w", encoding="utf-8").write("\n".join(lines) + "\n")

    print(f"converted {len(skills)} skills, skipped {len(dups)} duplicates")
    for k, v in sorted(totals.items(), key=lambda kv: -kv[1]):
        print(f"  {k:22} {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
