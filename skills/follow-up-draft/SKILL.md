---
name: follow-up-draft
description: Draft concise Slack or email follow-ups from context, notes, actions, or open asks.
---

# follow-up-draft

## Purpose

Draft a concise follow-up that preserves the ask, owner, timing, context, and next step.

## Use For

- Post-meeting follow-ups
- Slack reminders
- Email recaps
- Nudges on open asks

## Inputs

- Notes
- Action list
- Open ask
- Project context
- Prior thread context
- A `reduce-to-facts` ledger or conversation-state record

## Guardrails

- Read before write.
- Do not send the draft unless explicitly asked.
- Include the ask, owner, deadline or timing, and next step when known.
- Label assumptions or missing details.
- Keep the message concise and workplace-user friendly.

## Portable Output Contract

- Use only the useful subset of source-backed facts, assumptions, source gaps,
  stakeholder sensitivities, potential misreads, and the suggested next action.
- Use the smallest useful output.
- Label assumptions and preserve source gaps, source anchors, and confidence labels.
- When consuming upstream state, do not promote an assumption, inference, open
  question, proposed action, or stakeholder position into a fact, decision,
  commitment, owner, or deadline without new source support.
- Keep unresolved approvals, owners, timing, and blockers explicit or conditional in the draft.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.

## Output

- Direct version
- Warm version
- Executive concise version
- Context note, when helpful

If the user wants a fuller record before drafting, use the optional
`CONVERSATION_STATE.md` template from this pack when it is available.

## Success Standard

The user should be able to copy, tweak, and send a version within 5 minutes.
