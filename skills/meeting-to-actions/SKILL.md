---
name: meeting-to-actions
description: Turn meeting notes or transcripts into decisions, action items, owners, dates, blockers, and follow-ups.
---

# meeting-to-actions

## Purpose

Turn meeting content into a compact action record without making the user reread the whole transcript.

## Use For

- Zoom transcripts
- Meeting notes
- Slack threads
- Email chains
- Doc comment threads
- Ticket discussions
- Post-meeting cleanup
- Preparing follow-up messages or ticket updates

## Inputs

- Zoom transcript
- Notes
- Agenda
- Related ticket or doc context when useful
- A `reduce-to-facts` ledger or conversation-state record

## Guardrails

- Read before write.
- Do not send follow-ups or update tickets unless explicitly asked.
- Separate decisions made from open decisions.
- Name owners and dates only when the source supports them.
- Surface missing owners, due dates, and unclear blockers.
- Do not dump raw transcript content by default.

## Portable Output Contract

- Use only the useful subset of source-backed facts, assumptions, source gaps,
  stakeholder sensitivities, potential misreads, and the suggested next action.
- Use the smallest useful output.
- Label assumptions and preserve source gaps, source anchors, and confidence labels.
- When consuming upstream state, do not promote an assumption, inference, open
  question, proposed action, or stakeholder position into a fact, decision,
  commitment, owner, or deadline without new source support.
- Keep unresolved approvals, owners, timing, and blockers explicit in the action record.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.

## Output

- Decisions made
- Open decisions
- Action items with owner and due date
- Blockers
- Follow-up drafts
- Tickets/docs to update if applicable
- Source gaps

If the user wants a reusable record, use the optional `CONVERSATION_STATE.md`
template from this pack when it is available.

## Success Standard

The user should leave the meeting with an action record they can send or use immediately.
