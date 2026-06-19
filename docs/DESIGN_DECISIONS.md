# Design Decisions

> Historical launch decisions from the original ai-business-skills repo.

## Chosen Decisions

1. Cowork-first, not repo-first
   The repo is written for business users who want usable outputs quickly, not for people browsing an abstract framework.

2. Six visible skills only
   The skill surface stays narrow so users can choose confidently without browsing a large marketplace.

3. Connectors as inputs, not product complexity
   Slack, Gmail, Calendar, Zoom transcripts, Atlassian, and Hex outputs appear as optional context sources rather than user-facing mechanics.

4. `status-update` over `exec-update`
   `status-update` is broader, plainer language, and fits more audiences including managers, partners, and customers.

5. `brief-me` as the front door
   Business users often start with "what changed?" or "what did I miss?", so `brief-me` anchors the repo around catching up from messy context.

6. Minimal durable artifacts
   The repo includes proof and guidance artifacts, but avoids scripts, automation layers, or heavy process language.
