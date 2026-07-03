# context-to-action-skills

## What this repo is

This repo is the action layer for messy workplace context.

It packages seven visible skills that turn dense source into facts, asks, decisions, actions, updates, and replies while preserving uncertainty.

## When to use it

Use it when a thread, memo, transcript, policy doc, vendor writeup, research note, or escalation is long, ambiguous, stakeholder-sensitive, contradictory, or easy to misread.

Start with `reduce-to-facts` for dense or ambiguous source, then route the result into the most useful downstream skill.

## Canonical workflow

`reduce-to-facts` -> `clear-ask` / `decision-brief` / `meeting-to-actions` -> `follow-up-draft` / `status-update` / `brief-me`

This workflow should preserve facts, assumptions, source gaps, stakeholder sensitivities, and uncertainty.

## Important files and directories

- `README.md` - human-facing front door and install guidance
- `AGENTS.md` - short repo-specific agent rules
- `skills/` - the seven visible skills
- `examples/` - proof examples and fixtures
- `templates/` - shared output shapes
- `references/` - shared contracts and source packets
- `schemas/` - optional machine-readable handoff schemas
- `scripts/` - validation and installer helpers
- `docs/` - verification, process history, and suite docs

## Common repo commands

```sh
python scripts/validate_repo.py
python scripts/validate_examples.py
python scripts/validate_schemas.py
bash install.sh --help
git diff --check
```

## Agent operating rules

- Read before write.
- Use the smallest useful output.
- Prefer action-oriented artifacts over long summaries.
- Read and draft by default.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.
- Keep pasted-context mode as the primary validated path.
- Keep the seven visible skills stable unless scope is intentionally changing.

## What counts as done

Done means the repo still validates, the docs stay honest, and the output contracts still support a safe next step.

For docs work, that usually means the wording is clear, the links resolve, and the README still explains how to use the pack without overclaiming.

## What not to do

- Do not broaden the repo into a workflow engine or platform claim.
- Do not weaken safety boundaries for convenience.
- Do not imply connected tools are available by default.
- Do not mutate systems unless the user explicitly asks.
- Do not add or remove skills unless the task is explicitly about scope change.
