# Optional Operator Setup

`brief-me` should work immediately without setup. Use this flow only when the
user wants recurring briefs tailored to how they actually operate.

## Setup Principles

- Opt in. Do not require setup before the first useful brief.
- Tailor prioritization and presentation, not truth.
- Never let preferences override source confidence, unresolved gaps, or safety
  guardrails.
- Do not infer an operator profile from connected context. Ask for preferences
  directly or use preferences the user explicitly supplies.
- Keep the profile small enough to scan and revise quickly.
- Treat the current request as higher priority than any saved preference.

## Setup Flow

When the user says something like "set up brief-me for me" or "tailor my
briefs," ask only for the preferences that will materially change the output.
Cover these areas compactly:

1. **Priority signals** — What should reliably rise to the top? Examples:
   deadlines, decisions, blockers, customer impact, executive attention,
   people risk, or work that needs the operator personally.
2. **Compression rules** — What can usually stay terse or be omitted unless it
   changes? Examples: routine FYIs, status chatter, completed work, or low-risk
   background.
3. **Brief shape** — Preferred depth and ordering. Examples: skim vs. standard,
   action-first vs. chronology, bullets vs. compact prose.
4. **Response behavior** — Whether to include suggested replies, follow-ups,
   meeting prep, or only surface them when clearly needed.
5. **Working vocabulary** — Project names, team shorthand, recurring
   stakeholders, or terms that should be used consistently.

If the user gives enough information in one message, do not force a questionnaire.
Summarize the resulting profile and use it immediately.

## Portable Profile

Use the smallest useful subset of these fields:

```text
Operator profile
- Priority signals:
- Deprioritize or compress:
- Brief depth: skim | standard | deep
- Default ordering: action-first | decision-first | chronology | custom
- Suggested replies: always | when useful | only when asked
- Meeting prep: always | when imminent | only when asked
- Working vocabulary:
- Hard constraints:
```

The profile may be supplied inline for one request or stored by the user in a
host-supported location for reuse. The skill must remain useful when no profile
is available.

## Application Rules

The profile may change:

- which source-backed items are surfaced first
- how aggressively low-value context is compressed
- the order and depth of sections
- whether suggested replies and meeting prep appear by default
- terminology and formatting preferences

The profile may not change:

- whether a claim is treated as fact, assumption, inference, or source gap
- source confidence or source anchors
- whether unresolved approvals, owners, blockers, or deadlines stay explicit
- read-before-write behavior
- mutation boundaries or authorization requirements

When a profile preference conflicts with the user's current request, follow the
current request. When it conflicts with source truth or a guardrail, follow the
source truth or guardrail.
