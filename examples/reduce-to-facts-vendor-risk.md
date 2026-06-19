# Reduce to Facts Vendor Risk Example

## Situation

A launch-readiness thread needs a fact ledger before anyone decides whether the vendor integration can ship Friday.

## Raw Input

```text
1 Alex: Product wants the vendor integration live Friday if legal clears it.
2 Priya: Legal still has not approved the updated DPA.
3 Jordan: Support can handle the launch, but only if we have a rollback plan.
4 Mina: Security flagged missing SSO logs and wants a short risk note.
5 Sam: Implementation risk looks low based on the pilot.
6 Priya: "Looks low" is not evidence; we still need the review note.
7 Jordan: The on-call team is stretched next week.
8 Alex: Exec updates go out at 3pm today.
9 Sam: Who owns the go/no-go call?
10 Mina: No final owner is listed in the thread.
```

## Invocation

```text
Use reduce-to-facts on this thread. Give me a fact ledger with source scope, atomic facts, attributed opinions, unsupported claims, contradictions, open questions, and action-relevant implications.
```

## Output Fact Ledger

# Fact Ledger

## Source Scope

- Source(s) reviewed: vendor-risk Slack thread, lines 1-10
- Source type: Slack thread
- Time period covered: one morning thread
- Known limitations: no DPA text, no staffing plan, no security ticket
- Missing context: final decision owner, rollback readiness, exact launch criteria

## Atomic Facts

| ID | Fact | Source anchor | Confidence | Notes |
| --- | --- | --- | --- | --- |
| F1 | Product wants the vendor integration live Friday if legal clears it. | Line 1 | High | Friday is a target, not approval. |
| F2 | Legal has not approved the updated DPA. | Line 2 | High | Direct blocker. |
| F3 | Support readiness depends on having a rollback plan. | Line 3 | High | Conditional readiness, not full clearance. |
| F4 | Security flagged missing SSO logs and wants a short risk note. | Line 4 | High | Compliance concern remains open. |
| F5 | Exec updates go out at 3pm today. | Line 8 | High | Deadline pressure on the thread. |
| F6 | No final owner is listed in the thread. | Line 10 | High | Decision ownership is unresolved. |

## Attributed Opinions / Positions

| ID | Who/Source | Position | Basis | Confidence |
| --- | --- | --- | --- | --- |
| O1 | Sam, line 5 | Implementation risk looks low. | Sam cites the pilot. | Low |
| O2 | Jordan, line 3 | Support can handle the launch if rollback is ready. | Conditional support statement. | Medium |
| O3 | Alex, line 1 | Friday launch is the product goal if legal clears it. | Product priority. | Medium |

## Unsupported or Under-Supported Claims

| ID | Claim | Why unsupported | Evidence needed |
| --- | --- | --- | --- |
| C1 | "Implementation risk looks low." | No pilot details or metrics are attached. | Pilot results, defect rate, or rollout history. |
| C2 | Support can handle the launch. | No staffing or coverage plan is provided. | On-call coverage and launch support plan. |

## Inferences

| ID | Inference | Based on | Risk if wrong |
| --- | --- | --- | --- |
| I1 | Friday launch is blocked unless legal, security, and support all clear. | Facts F1-F6 plus the opinion conditions. | The team may overstate readiness. |
| I2 | The 3pm exec update should stay conservative until the missing evidence lands. | Deadline pressure plus unresolved blockers. | The update could sound falsely final. |

## Contradictions / Tensions

| ID | Conflict | Sources involved | Needs resolution |
| --- | --- | --- | --- |
| T1 | Product wants Friday launch, but legal approval is incomplete. | Lines 1-2 | Go/no-go decision. |
| T2 | Support is conditional, but the thread lacks a rollback plan. | Lines 3, 7 | Support readiness gate. |
| T3 | Sam says risk is low, but Priya says the review note is still missing. | Lines 5-6 | Evidence standard for risk claims. |

## Open Questions

| ID | Question | Why it matters | Likely owner |
| --- | --- | --- | --- |
| Q1 | Who owns the final go/no-go call? | Without an owner, escalation is unclear. | PM lead or launch owner |
| Q2 | What evidence supports the low-risk claim? | The launch readout needs supportable risk language. | Sam or engineering lead |

## Action-Relevant Implications

- Do not treat the Friday target as approval.
- The thread supports a readiness risk, not a launch decision.
- The 3pm update should state blockers plainly instead of implying readiness.
Do not treat these implications as final decisions.

## What Changed

- The thread is not a clean launch approval.
- Legal, support, and security are all still conditional.
- The low-risk claim is not source-backed.
- No decision owner is named.

## Why This Beats a Generic Summary

- It separates fact, opinion, unsupported claim, and inference instead of blending them.
- It keeps legal, support, and security tensions visible.
- It gives downstream skills a factual substrate they can use safely.

## Suggested Next Skill

Use `decision-brief` if the next problem is choosing whether to launch Friday or delay.
