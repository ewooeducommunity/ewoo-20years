"""mkdocs-macros-plugin entry point. Loads YAML data into page context."""
from __future__ import annotations

from pathlib import Path

import yaml

DATA_DIR = Path(__file__).parent / "docs" / "data"


def _load(name: str) -> list:
    path = DATA_DIR / f"{name}.yml"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def define_env(env):
    env.variables["executives"] = _load("executives")
    env.variables["timeline"] = _load("timeline")
