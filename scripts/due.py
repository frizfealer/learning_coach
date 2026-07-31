#!/usr/bin/env python3
"""List due and new chunks in a learning-coach study vault.

Usage: python due.py <vault-path> [--date YYYY-MM-DD]

Read-only: never modifies vault state. No dependencies beyond stdlib.
"""
import re
import sys
from datetime import date
from pathlib import Path


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm


def parse_list(v):
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if '"' in inner or "'" in inner:
            # quoted entries, e.g. ["Q2: confuses retrieval direction"]
            return re.findall(r'["\']([^"\']+)["\']', inner)
        return [x.strip() for x in inner.split(",") if x.strip()]
    return []


def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        print(__doc__)
        sys.exit(1)
    vault = Path(args[0])
    today = date.today()
    if "--date" in args:
        today = date.fromisoformat(args[args.index("--date") + 1])

    if not vault.is_dir():
        print(f"error: vault not found at {vault}")
        sys.exit(1)

    chunks = []
    for f in sorted(vault.glob("sources/*/chunks/*.md")):
        fm = parse_frontmatter(f.read_text(encoding="utf-8"))
        try:
            box = int(fm.get("box", 0))
        except ValueError:
            box = 0
        try:
            nr = date.fromisoformat(fm.get("next_review", ""))
        except ValueError:
            nr = None
        chunks.append({
            "path": f"{f.parent.parent.name}/{f.stem}",
            "box": box,
            "next": nr,
            "weak": parse_list(fm.get("weak", "[]")),
        })

    new = [c for c in chunks if c["box"] == 0]
    due = [c for c in chunks if c["box"] > 0 and c["next"] and c["next"] <= today]
    due.sort(key=lambda c: (c["box"], c["next"]))
    upcoming = sorted(
        (c for c in chunks if c["box"] > 0 and c["next"] and c["next"] > today),
        key=lambda c: c["next"],
    )

    print(f"# Vault status — {today}")
    print(f"\nDUE FOR REVIEW ({len(due)}) — hardest first:")
    for c in due:
        ids = [w.split(":")[0].strip() for w in c["weak"]]
        weak = f"  weak:{','.join(ids)}" if ids else ""
        overdue = (today - c["next"]).days
        print(f"  box {c['box']}  due {c['next']} ({overdue}d overdue)  {c['path']}{weak}")
    if not due:
        print("  (none)")

    print(f"\nNEW / NOT YET STUDIED ({len(new)}):")
    for c in new:
        print(f"  {c['path']}")
    if not new:
        print("  (none)")

    if upcoming:
        n = upcoming[0]
        print(f"\nNext upcoming review: {n['next']}  {n['path']}")
    print(f"\nTotal chunks: {len(chunks)}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)  # output piped to head etc.
