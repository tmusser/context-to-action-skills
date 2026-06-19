# context-to-action-skills

Formerly `ai-business-skills`.

Claude skills for turning messy workplace context into clear facts, asks, decisions, owners, risks, updates, and safe replies.

Most AI tools summarize context. This repo turns context into action while preserving uncertainty.

## What it does in 30 seconds

| Messy context | Clean output |
| --- | --- |
| A workplace thread with disagreement, legal uncertainty, support readiness risk, a soft deadline, and no named decision owner | Clean ask, decision needed, owner gap, risk/tone note, and a reply draft you can paste |

The promise is small: turn messy workplace context into the next clear move without pretending uncertainty is resolved.

## Use It When...

- A Slack thread, email chain, or meeting transcript needs a fast catch-up
- Someone asked a vague question and you need to clarify the ask
- A dense memo, policy doc, vendor writeup, or transcript needs a fact ledger before anyone acts on it
- A conversation has decisions, owners, deadlines, blockers, or open loops
- You need to draft the next context-aware reply
- You need to brief other people on what changed

## Try This First

If the source is long or ambiguous, start with `reduce-to-facts` and ask for a fact ledger before asking for a reply, update, or decision.

Paste messy notes, a transcript, or connected context into Claude/Cowork and ask:

```text
Use brief-me. Catch me up on what changed, what needs my response, risks/blockers, and suggested follow-ups.
```

Tiny example:

```text
Messy input:
Alex: "Can we still send the customer note today?"
Sam: "I'd rather not wait; support can catch up after."
Priya: "Support needs the enterprise wording before anything goes out."
Jordan: "Legal has not approved the banner copy yet."
Alex: "The send queue closes at 3pm. Who owns the call?"

Clean output:
Clean ask: decide whether to send today or wait for legal/support readiness.
Decision needed: send today vs. move to tomorrow.
Owner gap: no final decision owner is named.
Suggested reply: "Can we name the decision owner and confirm by 3pm whether legal/support readiness blocks today's send?"
Full version: [examples/messy-thread-to-follow-up.md](examples/messy-thread-to-follow-up.md)
```

Shareable one-pager: [docs/one-pager.md](docs/one-pager.md)

## Works with pasted context

These are plain-text skills, so the lowest-friction mode is copy/paste: paste the thread, note, email, transcript, or doc excerpt into your AI tool and ask for the skill by name.

The tested path is Claude/Cowork-style skills. The underlying `SKILL.md` files can also be adapted as reusable prompts for ChatGPT, Gemini, Codex-style agents, or internal AI assistants. No connector is required for pasted-context mode.

Start with `reduce-to-facts` for dense or ambiguous source, then pass the ledger to `clear-ask`, `decision-brief`, `status-update`, or `follow-up-draft`.

## Meeting without a meeting

Slack threads, email chains, doc comments, tickets, and transcripts can all carry the same source state as a live meeting. Treat them as async collaboration: extract facts first, then move to the next clear action.

## Use these skills

No coding is required.

Each skill lives in `skills/` as a folder with a `SKILL.md` file.

Copy the skill folders into the skills directory used by your AI tool, then paste context and ask for a skill by name. For example:

```text
Use brief-me on this thread and tell me what needs my response.
```

These skills read and draft by default. They do not send, publish, create events, or update systems unless you explicitly ask.
Start with `reduce-to-facts` when the source is too long or ambiguous to act on safely, then move to `clear-ask`, `decision-brief`, `status-update`, or `follow-up-draft`.

## Privacy and control

- pasted-only mode uses only pasted text
- connected-context mode reads only approved tools
- draft-only mode does not send or publish
- action mode mutates systems only when explicitly asked
- Tone safety: helps avoid accidental escalation, fake certainty, overcommitment, and misreading stakeholder sensitivity

## What This Is

This repo is for the work before the work:

- reduce dense context to safe facts
- understand what people said
- identify what changed
- separate facts from assumptions
- clarify the ask
- preserve open loops
- draft the next context-aware response

## What This Is Not

This is not a deck generator, project-management framework, or heavy artifact factory.

## How it works

| Input | State extracted | Output |
| --- | --- | --- |
| Dense context, long thread, memo, policy doc, vendor writeup, or transcript | Facts you can rely on, plus opinions, unsupported claims, contradictions, open questions, and implications | `reduce-to-facts` fact ledger you can pass downstream |
| Slack thread, email chain, meeting transcript, doc comment, or Jira/Confluence discussion | What changed, clean ask, decision, owner, deadline, blocker, source confidence, and tone risk | Reply draft, follow-up, status update, decision snapshot, or action list |

## Workflows

| Workflow | User question | Skill |
| --- | --- | --- |
| Reduce dense context | What can we safely rely on? | `reduce-to-facts` |
| Catch up | What did I miss? | `brief-me` |
| Clarify | What are they actually asking? | `clear-ask` |
| Extract actions | What are the actions and open loops? | `meeting-to-actions` |
| Decide | What decision is needed? | `decision-brief` |
| Respond | What should I say back? | `follow-up-draft` |
| Broadcast | What should others know? | `status-update` |

## Operating Modes

Choose the mode that gives you the right control.

| Mode | You control |
| --- | --- |
| Pasted-only mode | Use only text you pasted |
| Connected-context mode | Read approved tools like Gmail, Slack, Calendar, Docs, Jira, or Confluence |
| Draft-only mode | Produce messages, updates, or follow-ups without sending or publishing |
| Action mode | Mutate systems only when you explicitly ask |

## Supported Context

Use pasted notes, Zoom transcripts, Slack, Gmail, Calendar, Atlassian, and Hex or other data outputs as inputs.

By default, these skills read and draft. They do not send messages, create events, update tickets, or publish outputs unless you explicitly ask.

Shared guidance for mixed-source inputs lives in [source-packet.md](references/source-packet.md).

## Examples

- [Reduce to facts vendor risk](examples/reduce-to-facts-vendor-risk.md)
- [Messy thread to follow-up](examples/messy-thread-to-follow-up.md)
- [Gmail buried obligation](examples/gmail-buried-obligation.md)
- [Leadership status update](examples/leadership-status-update.md)
- [Post-meeting follow-up](examples/post-meeting-follow-up.md)
- [Morning brief](examples/morning-brief.md)
- [Decision with data](examples/decision-with-data.md)
- [Async Slack clear ask](examples/async-slack-clear-ask.md)

## Keep It Practical

Every skill is designed to produce something you can send, decide from, or act on within 5 minutes.

Helpful supporting files:

- [clarity-check.md](checklists/clarity-check.md)
- [source-packet.md](references/source-packet.md)
- [CONVERSATION_STATE.md](templates/CONVERSATION_STATE.md)
- [ACTIONS.md](templates/ACTIONS.md)
- [DECISIONS.md](templates/DECISIONS.md)
- [UPDATE.md](templates/UPDATE.md)

## How This Repo Was Built

This repo was built using `ai-engineering-skills` as the control layer.

- [BUILD_LOG.md](docs/BUILD_LOG.md)
- [CREATION_INVOCATIONS.md](docs/CREATION_INVOCATIONS.md)
- [DESIGN_DECISIONS.md](docs/DESIGN_DECISIONS.md)
- [VERIFY.md](docs/VERIFY.md)
- [Process artifacts](docs/process/README.md)

## Part of the suite

This repo is one piece of a small set of repos for making AI-assisted work clearer, more bounded, and more verifiable. See [Suite map](docs/SUITE_MAP.md).
