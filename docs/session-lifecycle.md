# Session lifecycle

Use the [routing protocol](../protocol/03-session-routing.md) to discover
capabilities and decide whether to reuse or create a session. A session is not
an artifact owner until its contract records that assignment.

## Session summary versus execution attempt

The diagram's labels summarize coordination, not a host API or a second
execution state machine. Track each contract revision and attempt using the
authoritative [execution states](../protocol/06-execution-and-monitoring.md#execution-states).
Record validation [gate results](../protocol/07-validation.md#gate-results) and
[closure disposition](../protocol/08-handoff-and-closure.md#closure-decision)
separately. A session can retain several historical attempts; one label must
not erase their results or imply that external jobs stopped.

```text
DISCOVERED → ROUTED → CONTRACTED → ACTIVE
                                  ↓
                       BLOCKED ↔ ACTIVE
                                  ↓
                      READY_FOR_REVIEW → REVIEWED
                                  ↓             ↓
                          REWORK_REQUIRED   ACCEPTED / REJECTED
                                  ↓             ↓
                                ACTIVE        HANDED_OFF
```

| Coordination label | Related execution state or record | Interpretation |
|---|---|---|
| `DISCOVERED`, `ROUTED`, `CONTRACTED` | Route and proposed/effective contract | Discovery or a contract offer alone is not runnable work; the activation handshake is required. |
| `ACTIVE` | `READY` or `RUNNING` for the effective attempt | `READY` follows activation; `RUNNING` describes actual authorized work. |
| `BLOCKED` | `BLOCKED` with prerequisite and owner | Resume only after rechecking the prerequisite, authority and current bounds. A deliberate `PAUSED` checkpoint is recorded separately. |
| `READY_FOR_REVIEW` | `AWAITING_VALIDATION` plus frozen candidate and evidence | Candidate readiness is not a validation pass or completion. |
| `REVIEWED` | Versioned validation report | Each criterion retains its own outcome; review does not automatically change execution state. |
| `REWORK_REQUIRED` | Findings and a new candidate/attempt or contract revision | Recheck authority before returning to `ACTIVE`; preserve old results and revalidate affected checks. |
| `ACCEPTED`, `REJECTED` | Validation outcome and applicable human decision | Acceptance does not grant release authority; rejection is not proof that execution stopped. |
| `HANDED_OFF` | Handoff packet and closure/transfer record | Packet receipt, ownership transfer, recipient activation, and verified quiescence are distinct facts. |

`FAILED`, `STOP_REQUESTED`, and `STOPPED` remain attempt-level states even when
the session summary is blocked or administratively closed. Do not map them to
`ACCEPTED` or `REJECTED` based only on a process exit. `INCOMPLETE` describes
an outcome, not an additional execution state.

Transitions require evidence appropriate to the host. A worker states
`READY_FOR_REVIEW` only when it freezes the relevant version, provides the
handoff fields, and stops changing the reviewed artifact. A validator reports
what it independently checked; human acceptance is separate when required.
`BLOCKED`, `REJECTED`, and `INCOMPLETE` are valid outcomes, not success.

Use purpose-specific temporary critics, retain their findings and provenance,
then close their work without deleting history. A new task should not
repurpose unrelated context just because a session exists. Preserve historical
sessions as read-only references unless the authorized owner decides otherwise.
At a stop boundary, prevent new work and preserve active job IDs and evidence;
stopping a worker does not automatically authorize canceling its jobs.

## Example transition

An activated attempt moves from `READY` to `RUNNING` while its coordination
summary is `ACTIVE`. The worker freezes candidate v1 and submits evidence:
execution becomes `AWAITING_VALIDATION`, summarized as `READY_FOR_REVIEW`.
A validator records `FAIL` for a required criterion. The coordination record
becomes `REVIEWED` with `REWORK_REQUIRED`; the failed report remains tied to v1.
After authorized remediation, v2 gets fresh affected checks. Only the resulting
gate evidence and applicable authority decision can support acceptance. A final
handoff still records running or unknown operations; it is not a stop receipt.

If there is no session host, use the same states in a shared handoff record and
have a human relay messages. Explicitly label the mode `MANUAL`; do not
represent a relay as a direct tool delivery.
