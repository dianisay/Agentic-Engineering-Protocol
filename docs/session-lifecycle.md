# Session lifecycle

Use the [routing protocol](../protocol/03-session-routing.md) to discover
capabilities and decide whether to reuse or create a session. A session is not
an artifact owner until its contract records that assignment.

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

If there is no session host, use the same states in a shared handoff record and
have a human relay messages. Explicitly label the mode `MANUAL`; do not
represent a relay as a direct tool delivery.
