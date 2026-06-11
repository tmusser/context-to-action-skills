---
name: decision-brief
description: Create a lightweight decision snapshot from messy business context and supporting evidence.
---

# decision-brief

## Purpose

Build a lightweight decision snapshot from mixed business context, ticket history, and evidence.

## Use For

- Lightweight decision support
- Recommendation requests
- Turning debate and evidence into a clear next step

## Inputs

- Notes or context thread
- Ticket or project context
- Supporting evidence
- Hex or other data output

## Guardrails

- Read before write.
- Treat analytics outputs as evidence, not as a separate analytics workflow.
- Separate source-backed evidence from assumptions.
- Make trade-offs and reversal cost visible.
- Surface source gaps and uncertainty.

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
