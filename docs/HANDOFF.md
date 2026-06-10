# Handoff

## Resume Packet

Read [`SPEC.md`](/Users/thomas.musser/code/ai-business-skills/SPEC.md), [`PLAN.md`](/Users/thomas.musser/code/ai-business-skills/PLAN.md), [`TODO.md`](/Users/thomas.musser/code/ai-business-skills/TODO.md), and [`docs/VERIFY.md`](/Users/thomas.musser/code/ai-business-skills/docs/VERIFY.md) before continuing.

Confirm:
- current phase
- next recommended task
- exact verification command
- assumptions before proceeding

## Workflow State

- Active modes: default
- Current phase: implementation
- Current loop: slice-by-slice repo build
- Next gate: complete repo shell and skill content, then run custom validation
- Context risk: low
- Active hypothesis: a lean, example-led structure will satisfy both usability and proof-artifact requirements

## Goal

Create a Cowork-first repo for business users that ships six lean skills and visibly documents its own creation workflow.

## Current Status

- Slice 1 is complete.
- Slices 2 through 4 are pending.

## Changed Files

- [`SPEC.md`](/Users/thomas.musser/code/ai-business-skills/SPEC.md): repo objective, scope, and acceptance criteria
- [`PLAN.md`](/Users/thomas.musser/code/ai-business-skills/PLAN.md): four-slice implementation plan
- [`TODO.md`](/Users/thomas.musser/code/ai-business-skills/TODO.md): task tracker and current scope freeze
- [`docs/CREATION_INVOCATIONS.md`](/Users/thomas.musser/code/ai-business-skills/docs/CREATION_INVOCATIONS.md): explicit workflow proof
- [`docs/DESIGN_DECISIONS.md`](/Users/thomas.musser/code/ai-business-skills/docs/DESIGN_DECISIONS.md): core design choices
- [`docs/BUILD_LOG.md`](/Users/thomas.musser/code/ai-business-skills/docs/BUILD_LOG.md): chronological build notes
- [`docs/VERIFY.md`](/Users/thomas.musser/code/ai-business-skills/docs/VERIFY.md): pending verification plan
- [`docs/HANDOFF.md`](/Users/thomas.musser/code/ai-business-skills/docs/HANDOFF.md): current session state

## Working Commands

- `sed -n '1,220p' <file>`
- `find . -type f | sort`
- `python3 - <<'PY' ... PY`

## Known Failing Commands

- None recorded.

## Important Decisions

- Keep the repo business-user friendly and example-led.
- Keep connectors as optional sources, not visible mechanics.
- Preserve exactly six front-door skills.

## Open Decisions

- None required for v0.1.

## Traps / Do-Not-Change Notes

- Do not add connector-specific skills.
- Do not broaden the skill list beyond the requested six.
- Do not let proof artifacts overshadow the user-facing repo content.

## Next Recommended Task

Create the README, AGENTS guide, checklist, templates, references, and examples.

## Suggested Verification Command

- `find . -type f | sort`
