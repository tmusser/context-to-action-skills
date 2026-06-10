## Goal

Ship a lean v0.1 companion repo that is immediately usable by business users and visibly built with the `ai-engineering-skills` workflow.

## Slices

1. Control artifacts and proof-doc scaffold
   Visible result: build intent and workflow are documented at repo start.
   Verification: `SPEC.md`, `PLAN.md`, `TODO.md`, and `docs/` proof files exist.

2. Repo shell for business users
   Visible result: README, guidance, checklist, templates, references, and examples make the repo usable without reading internals.
   Verification: README links resolve and examples align to target use cases.

3. Six front-door skills
   Visible result: each skill has clear purpose, inputs, guardrails, and business-ready outputs.
   Verification: frontmatter validates and folder names match skill names.

4. Contract verification and handoff
   Visible result: `docs/VERIFY.md` and `docs/HANDOFF.md` capture evidence, status, and the next safe task.
   Verification: custom validation passes and changed files are summarized.

## Risks

- Overbuilding the repo with framework language instead of practical outputs
- Letting connector details leak into user-facing skill descriptions
- Inconsistent skill structure across six folders

## Verification Strategy

- Use a deterministic Python validation script for files, frontmatter, code fences, and README links
- Keep proof artifacts updated as slices complete
- End with a git diff summary and next-step recommendation
