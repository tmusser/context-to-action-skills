# Changelog

## [Unreleased]

### Added

- `LLM.md` as a compact agent-readable guide to the repo.
- README front-door cleanup, including the routing table and compatibility/control matrix.
- A clearer repo-specific `AGENTS.md`.
- A portable output contract inside every installed skill.
- Validation that rejects skill links escaping the installed skill folder.

### Changed

- README sections were consolidated for faster scanning.
- The quickstart now asks users to choose one install target instead of running both installers.
- Downstream skills now accept fact ledgers or conversation-state records explicitly and preserve their source classifications.
- Optional template references no longer use repository-relative paths that break after installation.

### Fixed

- Installed skills no longer depend on `../../references` or `../../templates` paths that are absent from the installed layout.
- Assumptions, open questions, proposed actions, and stakeholder positions may not be promoted into facts, decisions, commitments, owners, or deadlines without new source support.
