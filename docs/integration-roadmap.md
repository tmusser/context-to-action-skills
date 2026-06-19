# Integration Roadmap

`context-to-action-skills` is intentionally a skill pack first.

MCP, IDE exports, and native assistant integrations are useful future packaging layers, but they should not be required for the core pasted-context workflow.

Near-term priorities:

1. Keep pasted-context usage clear and validated.
2. Add optional schemas for machine-checkable handoff state.
3. Add lightweight packaging and install support.
4. Consider MCP only when there is a concrete tool, resource, or prompt server use case.

MCP would be useful for:

- exposing skills as discoverable prompts
- serving examples and schemas as resources
- validating structured outputs
- connecting to approved context sources

MCP is not needed just to read a pasted thread and draft a safer reply.
