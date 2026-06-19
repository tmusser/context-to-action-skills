#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_PATTERNS = [
    re.compile(r"ai-business-skills"),
    re.compile(r"business-user", re.IGNORECASE),
    re.compile(r"business context", re.IGNORECASE),
    re.compile(r"six visible", re.IGNORECASE),
    re.compile(r"six skills", re.IGNORECASE),
    re.compile(r"Cowork-first", re.IGNORECASE),
    re.compile(r"tmusser/ai-business-skills"),
]

HISTORICAL_FILES = {
    ROOT / "docs/BUILD_LOG.md",
    ROOT / "docs/DESIGN_DECISIONS.md",
    ROOT / "docs/HANDOFF.md",
    ROOT / "docs/VERIFY.md",
    ROOT / "docs/process/PLAN.md",
    ROOT / "docs/process/README.md",
    ROOT / "docs/process/SPEC.md",
    ROOT / "docs/process/TODO.md",
}

README = ROOT / "README.md"
AGENTS = ROOT / "AGENTS.md"
SKILLS_DIR = ROOT / "skills"
SHARED_CONTRACT = ROOT / "references/shared-output-contract.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")
    except UnicodeDecodeError as exc:
        fail(f"could not decode {path.relative_to(ROOT)}: {exc}")


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(f"{path.relative_to(ROOT)} is missing YAML frontmatter")

    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def markdown_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        files.append(path)
    return sorted(files)


def line_has_allowed_former_name(path: Path, line: str) -> bool:
    if path != README:
        return False
    normalized = line.replace("`", "")
    return "Formerly ai-business-skills" in normalized or "Formerly ai-business-skills." in normalized


def validate_repo_identity() -> None:
    if not README.exists():
        fail("README.md is missing")
    if not AGENTS.exists():
        fail("AGENTS.md is missing")
    if not SHARED_CONTRACT.exists():
        fail("references/shared-output-contract.md is missing")

    shared_text = read_text(SHARED_CONTRACT).lower()
    shared_required = [
        "source-backed facts",
        "assumptions",
        "source gaps",
        "stakeholder sensitivities",
        "potential misread",
        "suggested next response or next action",
        "do not include every field mechanically",
        "use the smallest useful output",
        "label assumptions",
        "preserve source gaps",
        "do not send, publish, update tickets, create events, or mutate systems unless explicitly asked",
    ]
    for phrase in shared_required:
        if phrase not in shared_text:
            fail(f"shared-output-contract.md is missing required phrase: {phrase}")

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if len(skill_dirs) != 7:
        fail(f"expected exactly 7 skill directories, found {len(skill_dirs)}")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            fail(f"missing SKILL.md in {skill_dir.relative_to(ROOT)}")

        text = read_text(skill_file)
        frontmatter = parse_frontmatter(text, skill_file)
        name = frontmatter.get("name")
        description = frontmatter.get("description")
        if not name:
            fail(f"{skill_file.relative_to(ROOT)} is missing frontmatter name")
        if not description:
            fail(f"{skill_file.relative_to(ROOT)} is missing frontmatter description")
        if name != skill_dir.name:
            fail(f"{skill_file.relative_to(ROOT)} frontmatter name {name!r} does not match folder {skill_dir.name!r}")
        if "Read before write" not in text:
            fail(f"{skill_file.relative_to(ROOT)} is missing read-before-write guardrail")
        if "shared-output-contract.md" not in text:
            fail(f"{skill_file.relative_to(ROOT)} does not reference shared-output-contract.md")

    reduce_to_facts = SKILLS_DIR / "reduce-to-facts" / "SKILL.md"
    reduce_text = read_text(reduce_to_facts)
    if "Output size rule" not in reduce_text:
        fail("reduce-to-facts is missing the output size rule")


def validate_readme() -> None:
    text = read_text(README)
    lowered = text.lower()
    required_phrases = [
        "pasted-context validation boundary",
        "reduce-to-facts",
        "mutate systems unless explicitly asked",
    ]
    for phrase in required_phrases:
        if phrase not in lowered:
            fail(f"README is missing required phrase: {phrase}")

    example_links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    if not any(link.strip().startswith("examples/") for link in example_links):
        fail("README does not link to any examples")

    for link in example_links:
        resolved = resolve_link(README, link)
        if resolved is not None and not resolved.exists():
            fail(f"README link does not resolve: {link}")


def resolve_link(source_file: Path, link: str) -> Path | None:
    target = link.strip()
    if not target:
        return None
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    path = Path(target)
    if path.is_absolute():
        return path
    return (source_file.parent / path).resolve()


def validate_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in markdown_files():
        text = read_text(path)
        for match in link_pattern.finditer(text):
            resolved = resolve_link(path, match.group(1))
            if resolved is None:
                continue
            if not resolved.exists():
                fail(f"broken markdown link in {path.relative_to(ROOT)}: {match.group(1)}")


def validate_fences() -> None:
    for path in markdown_files():
        text = read_text(path)
        fence_lines = [line for line in text.splitlines() if line.lstrip().startswith("```")]
        if len(fence_lines) % 2 != 0:
            fail(f"unbalanced code fences in {path.relative_to(ROOT)}")


def validate_stale_phrases() -> None:
    stale_hits: list[str] = []
    for path in markdown_files():
        if path in HISTORICAL_FILES or path.is_relative_to(ROOT / "docs/process"):
            continue
        text = read_text(path)
        for line_no, line in enumerate(text.splitlines(), start=1):
            if line_has_allowed_former_name(path, line):
                continue
            for pattern in HISTORICAL_PATTERNS:
                if pattern.search(line):
                    stale_hits.append(f"{path.relative_to(ROOT)}:{line_no}: {line.strip()}")
                    break
    if stale_hits:
        details = "\n".join(stale_hits[:20])
        fail(f"stale primary-positioning phrases remain outside historical docs:\n{details}")


def main() -> None:
    validate_repo_identity()
    validate_readme()
    validate_markdown_links()
    validate_fences()
    validate_stale_phrases()
    print("validate_repo.py passed")


if __name__ == "__main__":
    main()
