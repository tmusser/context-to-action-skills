#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"

INPUT_HINTS = ["messy input", "raw input"]
INTERPRETATION_HINTS = ["what the skill notices", "what changed"]
OUTPUT_HINTS = ["clean output", "output fact ledger", "suggested follow-up draft"]
UNCERTAINTY_HINTS = ["source gaps", "source scope", "source confidence", "confidence"]
WHY_HINTS = ["why this is better than a generic ai reply", "why this beats a generic summary"]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")


def has_any(text: str, hints: list[str]) -> bool:
    lowered = text.lower()
    return any(hint.lower() in lowered for hint in hints)


def validate_example(path: Path) -> None:
    text = read_text(path)
    missing: list[str] = []

    if "situation" not in text.lower():
        missing.append("## Situation")
    if not has_any(text, INPUT_HINTS):
        missing.append("an input section")
    if not has_any(text, INTERPRETATION_HINTS):
        missing.append("an interpretation section")
    if not has_any(text, OUTPUT_HINTS):
        missing.append("a clean-output section")
    if not has_any(text, UNCERTAINTY_HINTS):
        missing.append("an uncertainty or source-gap section")
    if not has_any(text, WHY_HINTS):
        missing.append("a generic-summary comparison section")

    if missing:
        fail(f"{path.relative_to(ROOT)} is missing required structure: {', '.join(missing)}")


def main() -> None:
    examples = sorted(EXAMPLES_DIR.glob("*.md"))
    if not examples:
        fail("no example files found")

    for path in examples:
        validate_example(path)

    print("validate_examples.py passed")


if __name__ == "__main__":
    main()
