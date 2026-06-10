## Objective

Create `ai-business-skills`, a Cowork-first companion repo to `ai-engineering-skills` that helps business users turn messy context into clear asks, decisions, owners, updates, and follow-ups.

## Audience

- PMs
- Operators
- Analysts
- Managers
- Customer-facing teams
- Cross-functional leads using Claude/Cowork

## v0.1 Scope

- Ship six visible skills: `brief-me`, `clear-ask`, `meeting-to-actions`, `decision-brief`, `status-update`, `follow-up-draft`
- Add one shared source-packet reference for optional connected context
- Add one clarity checklist, three templates, and four business-work examples
- Add business-friendly repo guidance in `README.md` and `AGENTS.md`
- Add proof artifacts showing the repo was built with the `ai-engineering-skills` workflow

## Acceptance Criteria

1. The expected repo structure exists with the required files.
2. Each skill file has valid YAML frontmatter with `name` and `description`.
3. Skill names match folder names.
4. The README leads with business use cases and examples instead of architecture.
5. Connector mechanics stay in the background and appear only as optional input sources.
6. Proof artifacts document `$mini-spec`, `$thin-plan`, `$scope-freeze`, `$build-one`, `$test-mini`, `$verify-contract`, and `$handoff`.
7. Verification evidence is recorded in `docs/VERIFY.md`.

## Non-Goals

- Building connector-specific skills
- Building a project-management framework
- Adding automation scripts, telemetry, or installation tooling beyond what is needed for a lean repo
- Turning analytics inputs into a separate analytics workflow

## Constraints

- Keep the repo lean and business-user friendly
- Do not add extra visible front-door skills
- Do not mutate connected systems unless explicitly asked
- Prefer plain language over jargon
- Every skill must produce something the user can send, decide from, or act on within 5 minutes

## Verification Commands

- `find . -type f | sort`
- `python3 - <<'PY' ... PY` for structural and Markdown validation
- `git status --short`

## Smallest Demo

Open the README, choose one example workflow, inspect one skill, and confirm the repo contains the promised artifacts and passes the validation script.

## Open Questions

- No blocker for v0.1. Future work can decide whether to add tests or packaging once the content shape is stable.
