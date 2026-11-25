# Architecture and responsibility

The framework is a protocol, not an executable scheduler. A host may provide
persistent sessions, messaging, isolated workers, events, or none of them.
The [routing protocol](../protocol/03-session-routing.md) specifies how to
verify capabilities and fall back.

```text
                  Human: authority and consequential decisions
                                      |
                   Orchestrator: ownership and coordination
                     /        |        |          \
                Auditor    Planner   Workers    Critic (temporary)
                  |           |       |  \               |
                  |           |       |   peer dependency |
                  +--- shared evidence index and handoffs --+
                                      |
                        Validator: stable gate evidence
```

| Role | Owns | Must not silently do |
|---|---|---|
| Orchestrator | Global routing, dependency and decision tracking | Replace all specialist work or grant human-only authority |
| Auditor | Scoped discovery and evidence inventory | Modify discovered historical evidence or assume visibility |
| Planner | Prioritized, research-grounded options, gates and worker plans | Approve costs, relax criteria or execute without authorization |
| Critic/Analyst | Temporary independent analysis of a decision | Change artifacts, issue decisions or persist as an unnecessary worker |
| Validator | Independent evidence on a stable artifact against frozen gates | Change acceptance criteria, mutate the artifact or declare release approval |
| Project worker | Bounded implementation and its assigned artifacts | Write another owner's artifacts, exceed contract or approve own gate |

The human or explicitly authorized governing process decides consequential
actions. The orchestrator records the decision and its scope; it cannot invent
approval. Actual tool permissions must enforce sensitive boundaries where
possible: a Markdown role is not a security control.

The evidence manifest is an index, not a replacement for full evidence. Source,
version, evaluator, scope, limitations, and supersession are recorded before
reusing a claim. Use direct peer communication for real dependencies with a
durable handoff; avoid broadcasting or retransmitting unchanged history.
