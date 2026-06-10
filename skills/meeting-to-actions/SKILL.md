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
- Post-meeting cleanup
- Preparing follow-up messages or ticket updates

## Inputs

- Zoom transcript
- Notes
- Agenda
- Related ticket or doc context when useful

## Guardrails

- Read before write.
- Do not send follow-ups or update tickets unless explicitly asked.
- Separate decisions made from open decisions.
- Name owners and dates only when the source supports them.
- Surface missing owners, due dates, and unclear blockers.
- Do not dump raw transcript content by default.

## Output

- Decisions made
- Open decisions
- Action items with owner and due date
- Blockers
- Follow-up drafts
- Tickets/docs to update if applicable
- Source gaps

## Success Standard

The user should leave the meeting with an action record they can send or use immediately.
