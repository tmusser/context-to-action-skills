---
name: reduce-to-facts
description: Convert dense workplace source material into a compact, source-grounded fact ledger that separates supported facts, attributed opinions, unsupported claims, contradictions, open questions, and action-relevant implications.
---

# reduce-to-facts

## Purpose

Turn dense workplace source material into a fact ledger the user can trust before moving to a reply, decision, or action.

## When to use

Use this when the context is too long, political, ambiguous, or important to act on safely from a normal summary.

## When not to use

Do not use this for simple short threads where `brief-me`, `clear-ask`, or `follow-up-draft` can act directly.

## Output size rule

Default to a compact ledger with only the sections needed for the source.

Use the full ledger only when the source is dense, high-stakes, contradictory, or the user explicitly asks for a full fact ledger.

For short inputs, include:

- Source scope
- Atomic facts
- Open questions
- Action-relevant implications
- Suggested next skill

See [shared-output-contract.md](../../references/shared-output-contract.md) for the common cross-skill rules about assumptions, source gaps, stakeholder sensitivities, and mutation boundaries.

## Inputs

- Long threads
- Dense memos
- Policy docs
- Vendor writeups
- Strategy notes
- Research notes
- Customer escalations
- Transcripts
- Similar source material

## Guardrails

- Read before write.
- Do not summarize loosely.
- Do not smooth over uncertainty.
- Do not invent missing support.
- Do not collapse facts, opinions, and assumptions.
- Do not write a reply by default.
- Do not recommend a decision by default.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.
- Preserve uncertainty when the source is ambiguous.

# Fact Ledger

## Source Scope

- Source(s) reviewed:
- Source type:
- Time period covered:
- Known limitations:
- Missing context:

## Atomic Facts

Use a table:

| ID | Fact | Source anchor | Confidence | Notes |
| --- | --- | --- | --- | --- |

Rules:

- Facts must be atomic.
- Do not combine multiple claims into one fact.
- Use direct source anchors when available: section, paragraph, timestamp, speaker, file name, page, or quoted phrase.
- Confidence values: High / Medium / Low.
- If source anchors are unavailable, say so.

## Attributed Opinions / Positions

Use a table:

| ID | Who/Source | Position | Basis | Confidence |
| --- | --- | --- | --- | --- |

Rules:

- Opinions must be attributed.
- Do not convert opinions into facts.
- Include stakeholder positions, preferences, concerns, and proposed direction.

## Unsupported or Under-Supported Claims

Use a table:

| ID | Claim | Why unsupported | Evidence needed |
| --- | --- | --- | --- |

Rules:

- Include claims that sound important but lack source support.
- Include obvious-sounding assumptions if they are not actually supported by the provided source.

## Inferences

Use a table:

| ID | Inference | Based on | Risk if wrong |
| --- | --- | --- | --- |

Rules:

- Inferences are allowed, but must be explicitly labeled.
- Link each inference to facts or source material.
- Do not present inference as fact.

## Contradictions / Tensions

Use a table:

| ID | Conflict | Sources involved | Needs resolution |
| --- | --- | --- | --- |

Rules:

- Include hard contradictions and softer tensions.
- Include cases where one section implies readiness but another suggests a blocker.

## Open Questions

Use a table:

| ID | Question | Why it matters | Likely owner |
| --- | --- | --- | --- |

Rules:

- Focus on questions that block action, decision, reply, or confidence.

## Action-Relevant Implications

Use bullets.

Rules:

- These are implications, not decisions.
- Do not recommend a final decision unless the user explicitly asks.
- End this section with: "Do not treat these implications as final decisions."

## Suggested Next Skill

Recommend one downstream skill:

- `clear-ask` if the next problem is clarifying what someone wants.
- `decision-brief` if the next problem is choosing between options.
- `status-update` if the next problem is communicating what changed.
- `follow-up-draft` if the next problem is replying safely.
- `meeting-to-actions` if the next problem is extracting owners/actions.
- `brief-me` if the user needs a fast catch-up.

## Shared Output Contract

See [shared-output-contract.md](../../references/shared-output-contract.md) for the common cross-skill output rules.

## Success Standard

The user should be able to trust the fact ledger as a clean substrate for the next step.
