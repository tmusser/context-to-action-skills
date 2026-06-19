# AGENTS

- Preserve the repo model: messy workplace context -> reduce-to-facts -> conversation state -> context-aware response.
- When the source is too dense to act on safely, start with `reduce-to-facts`.
- Keep outputs workplace-user friendly.
- Prefer conversation state over long summaries.
- Treat Slack threads, email chains, doc comments, tickets, and meeting transcripts as possible async meetings.
- Prefer action-oriented artifacts over long summaries.
- Do not mutate connected systems unless explicitly asked.
- Label facts, assumptions, and source gaps.
- Use the smallest useful output.
- Keep the seven visible skills stable unless a future version explicitly changes scope.
- Keep the skill surface lean.
