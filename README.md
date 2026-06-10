# ai-business-skills

Claude skills for turning messy business context into clear asks, decisions, owners, updates, and follow-ups.

`ai-business-skills` is a Cowork-first companion to `ai-engineering-skills`. It works with pasted context and with connected tools when available, while keeping the user-facing experience focused on outcomes instead of connector mechanics.

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

- [Morning brief](/Users/thomas.musser/code/ai-business-skills/examples/morning-brief.md)
- [Post-meeting follow-up](/Users/thomas.musser/code/ai-business-skills/examples/post-meeting-follow-up.md)
- [Decision with data](/Users/thomas.musser/code/ai-business-skills/examples/decision-with-data.md)
- [Leadership status update](/Users/thomas.musser/code/ai-business-skills/examples/leadership-status-update.md)

## Skills

- [`brief-me`](/Users/thomas.musser/code/ai-business-skills/skills/brief-me/SKILL.md): catch up from messy context and surface what needs attention
- [`clear-ask`](/Users/thomas.musser/code/ai-business-skills/skills/clear-ask/SKILL.md): turn vague business context into a crisp ask
- [`meeting-to-actions`](/Users/thomas.musser/code/ai-business-skills/skills/meeting-to-actions/SKILL.md): turn meetings into decisions, owners, dates, blockers, and follow-ups
- [`decision-brief`](/Users/thomas.musser/code/ai-business-skills/skills/decision-brief/SKILL.md): turn messy context and evidence into a one-page recommendation
- [`status-update`](/Users/thomas.musser/code/ai-business-skills/skills/status-update/SKILL.md): create concise updates for different audiences
- [`follow-up-draft`](/Users/thomas.musser/code/ai-business-skills/skills/follow-up-draft/SKILL.md): draft concise Slack or email follow-ups

## Supported Context

Use pasted notes, Zoom transcripts, Slack, Gmail, Calendar, Atlassian, and Hex or other data outputs as inputs.

Shared guidance for mixed-source inputs lives in [source-packet.md](/Users/thomas.musser/code/ai-business-skills/references/source-packet.md).

## Keep It Practical

Every skill is designed to produce something you can send, decide from, or act on within 5 minutes.

Helpful supporting files:

- [clarity-check.md](/Users/thomas.musser/code/ai-business-skills/checklists/clarity-check.md)
- [ACTIONS.md](/Users/thomas.musser/code/ai-business-skills/templates/ACTIONS.md)
- [DECISIONS.md](/Users/thomas.musser/code/ai-business-skills/templates/DECISIONS.md)
- [UPDATE.md](/Users/thomas.musser/code/ai-business-skills/templates/UPDATE.md)

## How This Repo Was Built

This companion repo was built using `ai-engineering-skills` as the control layer.

- [BUILD_LOG.md](/Users/thomas.musser/code/ai-business-skills/docs/BUILD_LOG.md)
- [CREATION_INVOCATIONS.md](/Users/thomas.musser/code/ai-business-skills/docs/CREATION_INVOCATIONS.md)
- [DESIGN_DECISIONS.md](/Users/thomas.musser/code/ai-business-skills/docs/DESIGN_DECISIONS.md)
- [VERIFY.md](/Users/thomas.musser/code/ai-business-skills/docs/VERIFY.md)
