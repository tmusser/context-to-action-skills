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

## Optional Operator Setup

`brief-me` works without setup. When the user wants recurring briefs tailored to
how they operate, use the bundled [OPERATOR_PROFILE.md](OPERATOR_PROFILE.md)
flow.

An operator profile may tune prioritization, compression, section order,
terminology, meeting-prep behavior, and when suggested replies appear. It must
not change source truth, confidence, unresolved gaps, or authorization
boundaries.

- Opt in; never require setup before producing a useful brief.
- Do not infer preferences from connected data when the user has not stated them.
- Treat the user's current request as higher priority than profile defaults.
- If no profile is available, use the standard output contract below.

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

Use the smallest useful subset of:

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
With an operator profile, the brief should feel better prioritized for that user
without becoming less grounded or less portable.
