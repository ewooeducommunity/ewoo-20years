"""mkdocs-macros-plugin entry point. Loads YAML data into page context."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

DOCS_DIR = Path(__file__).parent / "docs"
DATA_DIR = DOCS_DIR / "data"

_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
_PART3_LINK = re.compile(r"\]\(\.\./part3/index\.md#([a-z0-9-]+)\)")


def _load(name: str) -> list:
    path = DATA_DIR / f"{name}.yml"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def _body_pages() -> list[tuple[Path, dict, str]]:
    """(경로, 프론트매터, 본문) — Part 1·2 본문 페이지."""
    pages = []
    for part in ("part1", "part2"):
        for path in sorted((DOCS_DIR / part).glob("*.md")):
            if path.name == "index.md":
                continue
            text = path.read_text(encoding="utf-8")
            m = _FRONTMATTER.match(text)
            meta = (yaml.safe_load(m.group(1)) or {}) if m else {}
            pages.append((path, meta, text))
    return pages


def _attach_related(executives: list) -> None:
    """임원 표의 각 인물에 '관련 글'(본문에서 이 인물로 링크한 글 + 본인 에세이)을 붙인다.

    같은 이름이 여러 행에 나오면 첫 행에만 붙인다.
    """
    anchor_to_name = {row["anchor"]: row["name"] for row in executives}
    related: dict[str, list[dict]] = {}

    def add(name: str, path: Path, title: str, essay: bool = False) -> None:
        href = "../" + path.relative_to(DOCS_DIR).as_posix()
        items = related.setdefault(name, [])
        if any(i["href"] == href for i in items):
            return
        items.append({"href": href, "title": title, "essay": essay})

    for path, meta, text in _body_pages():
        title = str(meta.get("title") or path.stem)
        if path.parent.name == "part2":
            for author in meta.get("authors") or []:
                if author in anchor_to_name.values():
                    add(author, path, title, essay=True)
        authors = [a for a in meta.get("authors") or [] if a != "편찬위원회"]
        label = f"{title} ({', '.join(authors)})" if path.parent.name == "part2" and authors else title
        for anchor in _PART3_LINK.findall(text):
            name = anchor_to_name.get(anchor)
            if name:
                add(name, path, label)

    seen: set[str] = set()
    for row in executives:
        name = row["name"]
        if name in seen:
            row["related"] = []
            continue
        seen.add(name)
        items = related.get(name, [])
        # 본인 에세이를 먼저
        row["related"] = sorted(items, key=lambda i: not i["essay"])


def define_env(env):
    executives = _load("executives")
    _attach_related(executives)
    env.variables["executives"] = executives
    env.variables["timeline"] = _load("timeline")
