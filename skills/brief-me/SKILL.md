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

## Guardrails

- Read before write.
- Do not send messages, create events, update tickets, or publish outputs unless explicitly asked.
- Separate source-backed facts from assumptions and suggestions.
- Prefer small source windows.
- Surface source gaps.
- Do not dump raw transcript content by default.
- Keep the output workplace-user friendly.

## Shared Output Expectations

When context is messy or multi-source, include only the useful subset of:

- Source-backed facts
- Assumptions
- Source gaps
- Stakeholder sensitivities
- Potential misread
- Suggested next response or next action

Do not include every field mechanically. Use the smallest useful output.

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

When the user wants a fuller record, map the result into [CONVERSATION_STATE.md](../../templates/CONVERSATION_STATE.md).

## Success Standard

The user should be able to scan the brief and know what matters within 5 minutes.
