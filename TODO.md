## Status

- [x] Slice 1: control artifacts and proof-doc scaffold
- [x] Slice 2: repo shell for business users
- [x] Slice 3: six front-door skills
- [ ] Slice 4: contract verification and handoff

## Active Task

Slice 4: contract verification and handoff

## Scope Freeze

Selected task: Slice 4

Allowed files and folders:
- `docs/`
- `docs/BUILD_LOG.md`
- `TODO.md`

Read-only files and folders:
- `README.md`
- `AGENTS.md`
- `checklists/`
- `references/`
- `templates/`
- `examples/`
- `skills/`
- `SPEC.md`
- `PLAN.md`
- `docs/CREATION_INVOCATIONS.md`
- `docs/DESIGN_DECISIONS.md`

Forbidden operations:
- Changing the user-facing repo surface unless validation reveals a real defect
- Adding new files unless validation forces a fix

Max files changed: 4

Allowed commands:
- `find`
- `sed`
- `python3`
- `git init`
- `git add`
- `git commit`
- `git status --short`

Stop condition:
- Validation evidence is recorded, the handoff is current, and the repo is optionally committed with the requested initial message.
