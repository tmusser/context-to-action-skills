---
name: brief-me
description: Catch the user up from messy workplace context and surface what needs attention.
---

# brief-me

## Purpose

Turn messy connected or pasted context into a short conversation-state brief the user can act on quickly.

## Use For

- "What did I miss?"
- "Brief me before this meeting."
- "What changed since Monday?"
- "What needs my response?"

## Inputs

- Slack
- Gmail
- Calendar
- Zoom transcript
- Atlassian
- Hex or other data output
- Pasted notes
- Any combination of the above
- A `reduce-to-facts` ledger or conversation-state record

## Guardrails

- Read before write.
- Do not send messages, create events, update tickets, or publish outputs unless explicitly asked.
- Separate source-backed facts from assumptions and suggestions.
- Prefer small source windows.
- Surface source gaps.
- Do not dump raw transcript content by default.
- Keep the output workplace-user friendly.

## Portable Output Contract

- Use only the useful subset of source-backed facts, assumptions, source gaps,
  stakeholder sensitivities, potential misreads, and the suggested next action.
- Use the smallest useful output.
- Label assumptions and preserve source gaps, source anchors, and confidence labels.
- When consuming upstream state, do not promote an assumption, inference, open
  question, proposed action, or stakeholder position into a fact, decision,
  commitment, owner, or deadline without new source support.
- Keep unresolved approvals, owners, timing, and blockers explicit in the brief.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.

## Output

- Conversation state
- What changed
- What needs response
- Action state
- Source confidence
- Suggested next response
- Meetings to prep for
- Suggested follow-ups
- Source gaps

When the user wants a fuller record, use the optional `CONVERSATION_STATE.md`
template from this pack when it is available.

## Success Standard

The user should be able to scan the brief and know what matters within 5 minutes.
