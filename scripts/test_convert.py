"""Smoke tests for convert.py — require pandoc in PATH."""
from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from convert import convert

SOURCE_ROOT = Path("/Users/taehee/Documents/이우20년사/통합편집본")
PILOT = SOURCE_ROOT / "역사편찬위-발간사.docx"


def _tools_available() -> bool:
    return bool(shutil.which("pandoc"))


@pytest.mark.skipif(not _tools_available(), reason="pandoc not installed")
@pytest.mark.skipif(not PILOT.exists(), reason="pilot source file missing")
def test_convert_pilot_produces_markdown(tmp_path):
    result = convert(PILOT, tmp_path)
    assert result.exists()
    assert result.suffix == ".md"
    content = result.read_text(encoding="utf-8")
    # 본문에 최소 한글이 100자 이상 담겨야 함
    hangul = [c for c in content if "가" <= c <= "힣"]
    assert len(hangul) > 100, "converted markdown has too little Korean text"
