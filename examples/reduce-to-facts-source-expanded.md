# Reduce to Facts Source-Expanded Example

## Situation

A viral clip is making a vendor announcement sound like proof of secret surveillance.

## Raw Input

```text
Viral clip: "They're secretly building the company's surveillance backbone."
Source A - Vendor announcement: "We signed a multi-year agreement to become the central operating system for store ops."
Source B - Public denial: "We do not collect employee surveillance data and do not sell customer identities."
Source C - Executive interview: "We want to be the system of record for operational decisions."
Source D - Government procurement notice: the contract covers workforce scheduling, inventory, and device management.
Clip follow-up: "The CEO called labor the enemy."
Internal note: the fuller quote is "union demands are the blocker," not "the enemy."
```

## Invocation

```text
Use reduce-to-facts in source-expanded mode. Check which claims are supported, refuted, contested, overstated, or unverified.
```

## What The Skill Notices

- The clip mixes an exact quote with a much stronger interpretation.
- Source A and Source D support a broader operational platform story, but not surveillance.
- Source B cuts against the strongest allegation.
- The CEO line looks like a rhetorical leap from "blocker" to "enemy," and the full quote is not available here.

## Output Fact Ledger

### Source Scope

- Source(s) reviewed: viral clip, Source A vendor announcement, Source B public denial, Source C executive interview, Source D procurement notice
- Source type: mixed public sources plus clip transcript
- Time period covered: one rumor cycle plus supporting references
- Known limitations: no contract text, no full interview transcript, no legal review
- Missing context: whether the clip omitted surrounding quotes, what "surveillance backbone" means in the clip, full wording around the CEO quote

### Claim Status Table

| Claim | Status | Evidence | Caveat |
| --- | --- | --- | --- |
| Vendor X is secretly building the company's surveillance backbone. | Overstated | Sources A, B, C, D | The sources support operational platform expansion, not secret surveillance. |
| Vendor X described itself as a central operating system for store ops. | Supported exactly | Source A | Exact wording is about store ops. |
| Vendor X is becoming the company's central operating system. | Supported in substance | Source A | The source is narrower than the claim. |
| Vendor X collects employee surveillance data. | Refuted | Source B | The public denial directly cuts against it. |
| The contract covers workforce scheduling, inventory, and device management. | Supported exactly | Source D | Scope is operational systems, not surveillance. |
| The CEO called labor the enemy. | Unverified | Clip follow-up, internal note | The fuller quote is missing, so the stronger wording cannot be checked here. |
| The denial fully settles every privacy concern. | Contested | Sources B and D | The denial narrows the allegation, but the procurement scope still leaves room for operational data questions. |

Do not upgrade "supported in substance" to "supported exactly."

### Rhetorical Leaps

- `"central operating system for store ops"` -> `"company's surveillance backbone"` is a rhetorical leap, not an evidence chain.
- A broader operational footprint does not prove hidden surveillance intent.
- `"union demands are the blocker"` -> `"the enemy"` changes the claim from conflict to motive.
- A denial narrows the allegation; it does not create evidence for the stronger rumor.

### Updated Atomic Facts

| ID | Fact | Source anchor | Confidence | Notes |
| --- | --- | --- | --- | --- |
| F1 | Vendor X signed a multi-year agreement to become the central operating system for store ops. | Source A | High | Exact quote. |
| F2 | Vendor X wants to be the system of record for operational decisions. | Source C | High | Platform ambition, not surveillance. |
| F3 | The contract covers workforce scheduling, inventory, and device management. | Source D | High | Operational scope is explicit. |
| F4 | Vendor X publicly denied collecting employee surveillance data and selling customer identities. | Source B | High | Direct denial. |

### Unsupported / Under-Supported Claims

| ID | Claim | Why unsupported | Evidence needed |
| --- | --- | --- | --- |
| C1 | Vendor X is secretly building the company's surveillance backbone. | The exact sources support operational expansion and a denial of surveillance, not this stronger allegation. | Contract text or direct statement of surveillance purpose. |
| C2 | The CEO called labor the enemy. | The fuller wording in the note says "union demands are the blocker." | Full transcript or exact quote. |
| C3 | The clip's strongest interpretation is fully grounded in the reviewed sources. | The reviewed sources do not support the rumor's strongest wording. | The original clip context and any missing surrounding quotes. |

### Action-Relevant Implications

- If you brief this internally, keep exact quotes separate from wider interpretation.
- Use the denial and procurement scope to narrow the rumor, not to overclaim certainty.
- Treat the "enemy" framing as a rhetorical leap unless the full quote confirms it.
- If you need a response draft, avoid repeating the clip's strongest wording as fact.

Do not treat these implications as final decisions.

### Suggested Next Skill

Use `follow-up-draft` if the next step is writing a careful reply or internal note that keeps exact quotes, implications, and unsupported claims separate.
