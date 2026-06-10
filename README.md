# ai-business-skills

Claude skills for turning messy business context into clear asks, decisions, owners, updates, and follow-ups.

`ai-business-skills` is a Cowork-first companion to `ai-engineering-skills`. It works with pasted context and with connected tools when available, while keeping the user-facing experience focused on outcomes instead of connector mechanics.

If you are new here, start with `brief-me` and the morning brief example.

## Use It When...

- Before a meeting and you need a fast catch-up
- After a meeting and you need owners, deadlines, and follow-ups
- Slack or Gmail context is messy and you need the signal
- A decision needs a crisp one-page brief
- A stakeholder update needs to be sent without sounding vague

## Example Workflows

```text
brief-me -> meeting-to-actions -> follow-up-draft -> status-update
```

```text
brief-me -> decision-brief -> follow-up-draft
```

```text
clear-ask -> follow-up-draft
```

## Start With Examples

- [Morning brief](./examples/morning-brief.md)
- [Post-meeting follow-up](./examples/post-meeting-follow-up.md)
- [Decision with data](./examples/decision-with-data.md)
- [Leadership status update](./examples/leadership-status-update.md)

## Skills

- [`brief-me`](./skills/brief-me/SKILL.md): catch up from messy context and surface what needs attention
- [`clear-ask`](./skills/clear-ask/SKILL.md): turn vague business context into a crisp ask
- [`meeting-to-actions`](./skills/meeting-to-actions/SKILL.md): turn meetings into decisions, owners, dates, blockers, and follow-ups
- [`decision-brief`](./skills/decision-brief/SKILL.md): turn messy context and evidence into a one-page recommendation
- [`status-update`](./skills/status-update/SKILL.md): create concise updates for different audiences
- [`follow-up-draft`](./skills/follow-up-draft/SKILL.md): draft concise Slack or email follow-ups

## Supported Context

Use pasted notes, Zoom transcripts, Slack, Gmail, Calendar, Atlassian, and Hex or other data outputs as inputs.

By default, these skills read and draft. They do not send messages, create events, update tickets, or publish outputs unless you explicitly ask.

Shared guidance for mixed-source inputs lives in [source-packet.md](./references/source-packet.md).

## Keep It Practical

Every skill is designed to produce something you can send, decide from, or act on within 5 minutes.

Helpful supporting files:

- [clarity-check.md](./checklists/clarity-check.md)
- [source-packet.md](./references/source-packet.md)
- [ACTIONS.md](./templates/ACTIONS.md)
- [DECISIONS.md](./templates/DECISIONS.md)
- [UPDATE.md](./templates/UPDATE.md)

## How This Repo Was Built

This companion repo was built using `ai-engineering-skills` as the control layer.

- [BUILD_LOG.md](./docs/BUILD_LOG.md)
- [CREATION_INVOCATIONS.md](./docs/CREATION_INVOCATIONS.md)
- [DESIGN_DECISIONS.md](./docs/DESIGN_DECISIONS.md)
- [VERIFY.md](./docs/VERIFY.md)
