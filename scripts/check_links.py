"""Verify cross-part anchor links inside docs/part1/ and docs/part2/.

For each Markdown link of the form `[label](../part{3,4}/index.md#anchor)`
or `[label](../part2/slug.md)`, check:
  - Part 3 anchors: exist in executives.yml
  - Part 4 anchors: exist in timeline.yml (matches YYYY, YYYY-MM, YYYY-MM-N)
  - Part 2 slugs: file exists at docs/part2/<slug>.md

Exit non-zero if any broken link found. Print each broken link with source
file + line number.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

DOCS = Path(__file__).resolve().parents[1] / "docs"


def anchors_from(yml_path: Path, key: str = "anchor") -> set[str]:
    data = yaml.safe_load(yml_path.read_text(encoding="utf-8")) or []
    return {row[key] for row in data if key in row}


def scan_body_links(body_files: list[Path]) -> list[tuple[Path, int, str]]:
    """Return list of (file, line_no, link_target) for broken links."""
    exec_anchors = anchors_from(DOCS / "data" / "executives.yml")
    time_anchors = anchors_from(DOCS / "data" / "timeline.yml")
    part2_files = {p.stem for p in (DOCS / "part2").glob("*.md") if p.name != "index.md"}

    pat = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    broken: list[tuple[Path, int, str]] = []

    for path in body_files:
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for m in pat.finditer(line):
                target = m.group(1)
                if "../part3/index.md#" in target:
                    anchor = target.split("#", 1)[1]
                    if anchor not in exec_anchors:
                        broken.append((path, i, target))
                elif "../part4/index.md#" in target:
                    anchor = target.split("#", 1)[1]
                    if anchor not in time_anchors:
                        broken.append((path, i, target))
                elif target.startswith("../part2/") and target.endswith(".md"):
                    slug = Path(target).stem
                    if slug not in part2_files:
                        broken.append((path, i, target))
    return broken


def main() -> int:
    body_files = list((DOCS / "part1").glob("*.md")) + list((DOCS / "part2").glob("*.md"))
    body_files = [f for f in body_files if f.name != "index.md"]
    broken = scan_body_links(body_files)
    if not broken:
        print("all crosslinks resolve.")
        return 0
    for path, line, target in broken:
        rel = path.relative_to(DOCS.parent)
        print(f"{rel}:{line}: broken link → {target}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
