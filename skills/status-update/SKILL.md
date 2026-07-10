---
name: status-update
description: Create concise status updates for teams, managers, executives, customers, or partners.
---

# status-update

## Purpose

Create a concise update from messy conversation state without losing the ask, risk, or next milestone.

## Modes

- team
- manager
- executive
- customer / partner

## Inputs

- Slack or email context
- Project or ticket context
- Meeting notes
- Customer context
- Pasted update notes
- A `reduce-to-facts` ledger or conversation-state record

## Guardrails

- Read before write.
- Do not send the update unless explicitly asked.
- Keep risks separate from blockers.
- Tune tone and detail to the audience.
- Label assumptions and source gaps.
- Keep the output short enough to send quickly.

## Portable Output Contract

- Use only the useful subset of source-backed facts, assumptions, source gaps,
  stakeholder sensitivities, potential misreads, and the suggested next action.
- Use the smallest useful output.
- Label assumptions and preserve source gaps, source anchors, and confidence labels.
- When consuming upstream state, do not promote an assumption, inference, open
  question, proposed action, or stakeholder position into a fact, decision,
  commitment, owner, or deadline without new source support.
- Keep unresolved approvals, owners, timing, and blockers explicit in the update.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.

## Output

- Conversation state
- Status
- What changed
- Progress
- Risks / blockers
- Stakeholder sensitivities
- Asks
- Next milestone
- Suggested audience-specific version

## Success Standard

The user should get a send-ready update in under 5 minutes.
