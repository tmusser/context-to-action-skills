# AGENTS

## Repo model

This repo turns messy workplace context into conversation state and then into context-aware responses.

Default route: `reduce-to-facts` -> `clear-ask` / `decision-brief` / `meeting-to-actions` -> `follow-up-draft` / `status-update` / `brief-me`

## Safety rules

- Read before write.
- Start with `reduce-to-facts` for dense or ambiguous source.
- Preserve uncertainty instead of smoothing it away.
- Do not send, publish, update tickets, create events, or mutate systems unless explicitly asked.
- Keep the pasted-context validation boundary intact.

## Output rules

- Prefer conversation state over long summaries.
- Label facts, assumptions, source gaps, stakeholder sensitivities, and uncertainty.
- Use the smallest useful output.
- Prefer action-oriented artifacts over long summaries.
- Keep the seven visible skills stable unless scope is explicitly changing.

## Validation commands

```sh
python scripts/validate_repo.py
python scripts/validate_examples.py
python scripts/validate_schemas.py
git diff --check
```

## Docs-only edits: do not change

- skill names or count
- safety boundaries
- validation boundaries
- example semantics just for style
- connector or mutation claims
