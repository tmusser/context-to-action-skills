#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

case "${1:-}" in
  --list)
    printf '%s\n' "Available skills:"
    for skill_file in "$SCRIPT_DIR"/skills/*/SKILL.md; do
      [ -f "$skill_file" ] || continue
      skill_dir=${skill_file%/SKILL.md}
      printf '%s\n' "- ${skill_dir##*/}"
    done
    exit 0
    ;;
esac

exec python3 "$SCRIPT_DIR/scripts/install_skills.py" "$@"
