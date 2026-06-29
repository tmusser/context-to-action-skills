#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
TEMPLATES_ROOT = ROOT / "templates"


@dataclass(frozen=True)
class InstallTarget:
    source: Path
    destination: Path


@dataclass(frozen=True)
class PlannedInstall:
    target: InstallTarget
    action: str
    reason: str = ""


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def available_skills() -> list[str]:
    if not SKILLS_ROOT.exists():
        fail(f"missing skills directory: {SKILLS_ROOT.relative_to(ROOT)}")

    skills: list[str] = []
    for path in sorted(SKILLS_ROOT.iterdir(), key=lambda item: item.name):
        if path.is_dir() and (path / "SKILL.md").is_file():
            skills.append(path.name)
    return skills


def parse_only(value: str) -> list[str]:
    names = [item.strip() for item in value.split(",")]
    names = [item for item in names if item]
    if not names:
        fail("--only requires at least one skill name")
    deduped: list[str] = []
    for name in names:
        if name not in deduped:
            deduped.append(name)
    return deduped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="install.sh",
        description="Install the context-to-action-skills pack into a Claude or Codex skills directory.",
        epilog=(
            "If no target is provided, install.sh defaults to --claude-user. "
            "Use --force to replace an existing destination that differs from the source."
        ),
    )
    target_group = parser.add_mutually_exclusive_group()
    target_group.add_argument(
        "--claude-user",
        action="store_true",
        help="Install into ~/.claude/skills/",
    )
    target_group.add_argument(
        "--codex-user",
        action="store_true",
        help="Install into ~/.agents/skills/",
    )
    target_group.add_argument(
        "--claude-project",
        metavar="PATH",
        help="Install into PATH/.claude/skills/",
    )
    target_group.add_argument(
        "--codex-project",
        metavar="PATH",
        help="Install into PATH/.agents/skills/",
    )
    parser.add_argument(
        "--only",
        metavar="a,b,c",
        help="Install only the named skills.",
    )
    parser.add_argument(
        "--include-templates",
        action="store_true",
        help="Also copy templates/ to the matching templates location.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without creating anything.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing destinations that differ from the source.",
    )
    args = parser.parse_args()
    if not any(
        [
            args.claude_user,
            args.codex_user,
            args.claude_project,
            args.codex_project,
        ]
    ):
        args.claude_user = True
    return args


def resolve_target(args: argparse.Namespace) -> tuple[Path, Path]:
    if args.claude_user:
        base = Path.home() / ".claude"
        return base / "skills", base / "context-to-action-skills" / "templates"
    if args.codex_user:
        base = Path.home() / ".agents"
        return base / "skills", base / "context-to-action-skills" / "templates"
    if args.claude_project:
        project_root = Path(args.claude_project).expanduser()
        if not project_root.exists():
            fail(f"project path does not exist: {project_root}")
        if not project_root.is_dir():
            fail(f"project path is not a directory: {project_root}")
        return project_root / ".claude" / "skills", project_root / "docs" / "context-to-action-skills" / "templates"
    if args.codex_project:
        project_root = Path(args.codex_project).expanduser()
        if not project_root.exists():
            fail(f"project path does not exist: {project_root}")
        if not project_root.is_dir():
            fail(f"project path is not a directory: {project_root}")
        return project_root / ".agents" / "skills", project_root / "docs" / "context-to-action-skills" / "templates"
    fail("no install target selected")


def validate_selected_skills(selected: list[str], all_skills: list[str]) -> None:
    available = set(all_skills)
    unknown = [name for name in selected if name not in available]
    if unknown:
        fail(
            "unknown skill name(s): "
            + ", ".join(unknown)
            + ". Available skills: "
            + ", ".join(all_skills)
        )

    for name in selected:
        source = SKILLS_ROOT / name
        skill_md = source / "SKILL.md"
        if not source.is_dir():
            fail(f"missing skill directory: skills/{name}")
        if not skill_md.is_file():
            fail(f"skill directory is missing SKILL.md: skills/{name}")


def copy_directory(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)


def remove_existing_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def compare_paths(source: Path, destination: Path) -> tuple[bool, str]:
    if not destination.exists():
        return False, "destination is missing"

    if source.is_dir():
        if not destination.is_dir():
            return False, "destination is not a directory"

        source_entries = sorted(child.name for child in source.iterdir())
        destination_entries = sorted(child.name for child in destination.iterdir())
        if source_entries != destination_entries:
            missing = [name for name in source_entries if name not in destination_entries]
            extra = [name for name in destination_entries if name not in source_entries]
            details: list[str] = []
            if missing:
                details.append("missing " + ", ".join(missing))
            if extra:
                details.append("extra " + ", ".join(extra))
            return False, "; ".join(details) or "directory contents differ"

        for name in source_entries:
            same, reason = compare_paths(source / name, destination / name)
            if not same:
                return False, f"{name}: {reason}"
        return True, ""

    if destination.is_dir():
        return False, "destination is a directory"

    try:
        if source.read_bytes() == destination.read_bytes():
            return True, ""
    except OSError as exc:
        return False, f"could not read files: {exc}"

    return False, "file contents differ"


def plan_install(targets: list[InstallTarget], force: bool) -> list[PlannedInstall]:
    plans: list[PlannedInstall] = []
    for target in targets:
        if not target.destination.exists() and not target.destination.is_symlink():
            plans.append(PlannedInstall(target, "copy"))
            continue

        same, reason = compare_paths(target.source, target.destination)
        if same:
            plans.append(PlannedInstall(target, "skip", "already installed"))
        elif force:
            plans.append(PlannedInstall(target, "replace", reason or "destination differs"))
        else:
            plans.append(PlannedInstall(target, "fail", reason or "destination differs"))
    return plans


def format_plan_line(plan: PlannedInstall, dry_run: bool) -> str:
    source_label = plan.target.source.relative_to(ROOT)
    destination = plan.target.destination
    if plan.action == "copy":
        prefix = "Would copy" if dry_run else "Copying"
        return f"- {prefix} {source_label} -> {destination}"
    if plan.action == "skip":
        prefix = "Would skip" if dry_run else "Already installed"
        suffix = " (already installed)" if dry_run else ""
        return f"- {prefix} {source_label} -> {destination}{suffix}"
    if plan.action == "replace":
        if dry_run:
            return f"- Would replace {source_label} -> {destination} (destination differs; --force will replace)"
        return f"- Replacing {source_label} -> {destination}"
    if plan.action == "fail":
        return f"- Would fail {source_label} -> {destination} (destination differs; rerun with --force)"
    raise AssertionError(f"unknown plan action: {plan.action}")


def apply_plan(plans: list[PlannedInstall]) -> None:
    for plan in plans:
        if plan.action == "copy":
            copy_directory(plan.target.source, plan.target.destination)
            continue
        if plan.action == "skip":
            continue
        if plan.action == "replace":
            remove_existing_path(plan.target.destination)
            copy_directory(plan.target.source, plan.target.destination)
            continue
        raise AssertionError(f"cannot apply plan action: {plan.action}")


def main() -> int:
    args = parse_args()
    all_skills = available_skills()
    if not all_skills:
        fail("no skills found under skills/")

    if args.only:
        selected = parse_only(args.only)
    else:
        selected = list(all_skills)

    validate_selected_skills(selected, all_skills)

    skills_dest, templates_dest = resolve_target(args)
    targets: list[InstallTarget] = []
    for skill_name in selected:
        targets.append(InstallTarget(SKILLS_ROOT / skill_name, skills_dest / skill_name))
    if args.include_templates:
        if not TEMPLATES_ROOT.is_dir():
            fail("missing templates directory: templates/")
        targets.append(InstallTarget(TEMPLATES_ROOT, templates_dest))

    plans = plan_install(targets, force=args.force)

    if args.dry_run:
        print(f"Would install {len(selected)} skill(s) into {skills_dest}")
        for plan in plans:
            print(format_plan_line(plan, dry_run=True))
        if args.include_templates:
            print(f"Templates would go to {templates_dest}")
        return 0

    failures = [plan for plan in plans if plan.action == "fail"]
    if failures:
        details = "; ".join(
            f"{plan.target.destination}: {plan.reason}" for plan in failures
        )
        fail(f"destination differs and --force is required: {details}")

    print(f"Installing {len(selected)} skill(s) into {skills_dest}")
    apply_plan(plans)
    for plan in plans:
        print(format_plan_line(plan, dry_run=False))

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
