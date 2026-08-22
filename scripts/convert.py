"""DOCX → Markdown converter via pandoc.

Source documents were originally HWPX/HWP files. Homebrew's LibreOffice
lacks a working HWP/HWPX filter, so DOCX conversion is done manually in
Hancom Office beforehand; this script only handles the DOCX → Markdown
step via pandoc.
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def convert(source: Path, output_dir: Path) -> Path:
    """Convert a DOCX file to Markdown. Returns the .md path."""
    source = Path(source)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    md_out = output_dir / f"{source.stem}.md"
    media_dir = output_dir / "images" / source.stem
    subprocess.run(
        [
            "pandoc", "-f", "docx", "-t", "gfm",
            f"--extract-media={media_dir}",
            "-o", str(md_out), str(source),
        ],
        check=True,
    )
    return md_out


def main() -> None:
    p = argparse.ArgumentParser(description="Convert DOCX to Markdown.")
    p.add_argument("source", type=Path, help="입력 DOCX 파일")
    p.add_argument(
        "-o", "--output-dir", type=Path, default=Path("/tmp/ewoo-convert"),
        help="Markdown 출력 폴더 (기본 /tmp/ewoo-convert)",
    )
    args = p.parse_args()
    result = convert(args.source, args.output_dir)
    print(f"wrote {result}")


if __name__ == "__main__":
    main()
