---
name: reduce-to-facts
description: Use for dense or messy workplace source material - Slack threads, email chains, memos, transcripts, policy docs, vendor writeups, research notes, strategy notes, or customer escalations - before replying, deciding, escalating, or acting when context is long, ambiguous, stakeholder-sensitive, high-stakes, contradictory, or easy to misread. Use source-expanded mode only when the user explicitly asks to verify, fact-check, expand sources, support or refute claims, or use outside sources; not for simple catch-ups or straightforward reply drafting unless uncertainty needs to be preserved first.
---

# reduce-to-facts

## Purpose

Turn dense workplace source material into a fact ledger the user can trust before moving to a reply, decision, or action.

## When to use

Use this when the context is too long, ambiguous, stakeholder-sensitive, high-stakes, contradictory, or too important to act on safely from a normal summary.

## When not to use

Do not use this for simple short threads where `brief-me`, `clear-ask`, or `follow-up-draft` can act directly.

## Output size rule

Default to a compact ledger with only the sections needed for the source.

Use the full ledger only when the source is dense, high-stakes, contradictory, or the user explicitly asks for a full fact ledger.

- Omit empty optional sections for compact outputs.
- For dense or high-stakes sources, include all major sections.
- Use "None surfaced in the reviewed source" only when that absence is itself useful.

For short inputs, include:

- Source scope
- Atomic facts
- Open questions
- Action-relevant implications
- Suggested next skill

See [shared-output-contract.md](../../references/shared-output-contract.md) for the common cross-skill rules about assumptions, source gaps, stakeholder sensitivities, and mutation boundaries.

## Source Mode

Default to source-only mode.

Switch to source-expanded mode only when the user explicitly asks to verify, fact-check, expand sources, support claims, refute claims, or use outside sources.

### Source-Only Mode

- Use only the supplied source material.
- Do not verify externally.
- Do not treat supplied material as true by default.
- Separate directly stated claims from implied, assumed, or unsupported claims.
- Use source anchors from the supplied material.

### Source-Expanded Mode

- Use only when explicitly asked.
- Keep the source-only ledger logic.
- Add outside evidence only where authorized.
- Do not pretend to have checked sources that were not actually checked.
- Distinguish exact support from support in substance.
- Do not use related evidence as proof of a specific claim.
- Do not collapse contested claims into facts.
- Include citations, links, or source anchors when supported.
- If tools are unavailable, say so and keep the claim unverified.

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
- Do not upgrade "supported in substance" to "supported exactly."
- Do not write a reply by default.
- Do not recommend a decision by default.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.
- Preserve uncertainty when the source is ambiguous.

## Process

- Identify the source scope first.
- Create local anchors when the source does not provide them, such as line numbers, timestamps, speaker labels, file names, or section names.
- Extract only source-supported claims.
- Treat "X said Y" as a fact about the statement, not proof that Y is true.
- Move weakly supported claims into Unsupported or Under-Supported Claims.
- Label reasoning beyond the source as Inference.
- Keep implications as constraints, not final recommendations.

## Confidence Rubric

- High: directly stated with a clear anchor, or supported by multiple consistent anchors.
- Medium: directly stated but context is incomplete, wording is ambiguous, or only one source supports it.
- Low: implied, secondhand, weakly supported, or dependent on missing context.

## Claim Status Table

Use this table in source-expanded mode, or whenever you need to show which claims got stronger, weaker, contested, or unverified after outside evidence.

| Claim | Status | Evidence | Caveat |
| --- | --- | --- | --- |

Status meanings:

- Supported exactly: the source says this directly, with matching wording or a direct equivalent.
- Supported in substance: the source backs the core point, but the exact wording is broader or sharper than the source.
- Partly supported: part of the claim is source-backed, but part of it is not.
- Contested: sources disagree.
- Overstated: the claim reaches beyond what the evidence can support.
- Unsupported: no source support found.
- Refuted: available evidence cuts against the claim.
- Unverified: not checked, or not enough evidence was found.

Do not upgrade "supported in substance" to "supported exactly."

## Rhetorical Leaps

- Show the move from exact wording to broader implication.
- Keep evidence, interpretation, and persuasion separate.
- A quote or denial can support a concern without supporting the strongest version of that concern.
- If a source step is rhetorical rather than evidentiary, label it as such.
- Do not dismiss the source; explain the leap.

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

If a named downstream skill is unavailable in the host assistant, describe the next step in plain language instead of pretending the skill can be invoked.

## Shared Output Contract

See [shared-output-contract.md](../../references/shared-output-contract.md) for the common cross-skill output rules.

## Success Standard

The user should be able to trust the fact ledger as a clean substrate for the next step.
In source-expanded mode, the user should also be able to see which claims got stronger, weaker, stayed contested, or remained unverified after outside evidence was checked.
