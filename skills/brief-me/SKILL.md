---
name: brief-me
description: Catch the user up from messy business context and surface what needs attention.
---

# brief-me

## Purpose

Turn messy connected or pasted context into a short business briefing the user can act on quickly.

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
- Keep the output business-user friendly.

## Output

- Situation
- What changed
- Decisions needed
- Open actions
- Owners / due dates
- Risks or blockers
- Meetings to prep for
- Suggested follow-ups
- Source gaps

## Success Standard

The user should be able to scan the brief and know what matters within 5 minutes.
