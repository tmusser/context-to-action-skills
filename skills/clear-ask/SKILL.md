---
name: clear-ask
description: Turn vague workplace context into a crisp ask with clear ownership and timing.
---

# clear-ask

## Purpose

Convert a fuzzy request, thread, or note into a direct ask someone can understand and act on.

## Use For

- Turning a rambling draft into a clear request
- Clarifying what decision is actually needed
- Making ownership and timing explicit before sending a message

## Inputs

- Slack or email draft
- Meeting notes
- Project context
- Pasted workplace context
- A `reduce-to-facts` ledger or conversation-state record

## Guardrails

- Read before write.
- Do not send the message unless explicitly asked.
- Separate known facts from assumptions.
- Flag missing owner, timing, or decision context.
- Prefer the smallest useful ask.

## Portable Output Contract

- Use only the useful subset of source-backed facts, assumptions, source gaps,
  stakeholder sensitivities, potential misreads, and the suggested next action.
- Use the smallest useful output.
- Label assumptions and preserve source gaps, source anchors, and confidence labels.
- When consuming upstream state, do not promote an assumption, inference, open
  question, proposed action, or stakeholder position into a fact, decision,
  commitment, owner, or deadline without new source support.
- Keep unresolved approvals, owners, timing, and blockers explicit in the ask and draft.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.

## Output

- Clean ask
- Audience
- Owner
- Deadline / timing
- Decision needed
- Missing info
- Potential misread
- Why this ask is clearer
- Suggested message

## Success Standard

The output should remove ambiguity and make the next action obvious within 5 minutes.
