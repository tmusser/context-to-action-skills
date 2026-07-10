---
name: decision-brief
description: Create a lightweight decision snapshot from messy workplace context and supporting evidence.
---

# decision-brief

## Purpose

Build a lightweight decision snapshot from mixed workplace context, ticket history, and evidence.

## Use For

- Lightweight decision support
- Recommendation requests
- Turning debate and evidence into a clear next step

## Inputs

- Notes or context thread
- Ticket or project context
- Supporting evidence
- Hex or other data output
- A `reduce-to-facts` ledger or conversation-state record

## Guardrails

- Read before write.
- Treat analytics outputs as evidence, not as a separate analytics workflow.
- Separate source-backed evidence from assumptions.
- Make trade-offs and reversal cost visible.
- Surface source gaps and uncertainty.

## Portable Output Contract

- Use only the useful subset of source-backed facts, assumptions, source gaps,
  stakeholder sensitivities, potential misreads, and the suggested next action.
- Use the smallest useful output.
- Label assumptions and preserve source gaps, source anchors, and confidence labels.
- When consuming upstream state, do not promote an assumption, inference, open
  question, proposed action, or stakeholder position into a fact, decision,
  commitment, owner, or deadline without new source support.
- Keep unresolved approvals, owners, timing, and blockers explicit in the recommendation.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.

## Output

- Recommendation
- Decision needed
- Options
- Trade-offs
- Evidence
- Risks
- Reversal cost
- Next step

## Success Standard

The snapshot should help someone make or frame a decision within 5 minutes.
