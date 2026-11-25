# Repository instructions

These instructions apply to work in this repository. Follow the user's actual
authorized scope and applicable higher-priority instructions. The protocol is
the source of process guidance; it does not grant capabilities or permission
to act beyond that scope. Read the relevant documents in [protocol/](../protocol/)
before coordinating work, and use the role definitions in [agents/](agents/) as
bounded responsibilities rather than claims about a particular host.

The canonical stages are [01 audit](../protocol/01-audit.md),
[02 portfolio planning](../protocol/02-portfolio-planning.md),
[03 session routing](../protocol/03-session-routing.md),
[04 session activation](../protocol/04-session-activation.md),
[05 inter-agent communication](../protocol/05-inter-agent-communication.md),
[06 execution and monitoring](../protocol/06-execution-and-monitoring.md),
[07 validation](../protocol/07-validation.md), and
[08 handoff and closure](../protocol/08-handoff-and-closure.md).

## Safety and authority

- Be transparent about consequential actions and their results. Do not conceal
  actions, bypass controls, or assume silence is consent. Obtain explicit human
  authorization for high-impact actions, including destructive changes,
  publication, external sharing, credential or access changes, and material
  spending or production operations, expensive computation, architectural
  commitments, and physical-world actions. An agent's recommendation,
  validation, or approval is not human authorization.
- Protect secrets, credentials, private code, and personal data. Access and
  retain only what is needed and authorized; minimize, redact, or aggregate
  sensitive details in handoffs and outputs. Do not send data to external
  services without authorization. Honor access and content restrictions; do not
  work around them. Report restricted or inaccessible evidence as a limitation.
- Discover the actual host's capabilities and permissions before relying on
  them. If a capability is unavailable or access fails, report the limitation
  and a practical manual fallback. Never convert a tool error, missing result,
  pending action, or unverified assertion into success.
- Preserve historical sessions and their provenance. Retire temporary roles
  without destructive deletion. Avoid duplicate work and changes outside scope.

## Coordination and evidence

Use explicit, meaningful delegation for substantial work where the host and
user permit it. Record ownership, inputs, deliverables, boundaries, dependencies,
and completion or escalation criteria. Communicate dependencies directly
between responsible sessions when possible, with the coordinator kept informed;
otherwise record a manual handoff. Do not invent sessions, tools, results, or
authority.

Separate status and intent from evidence and verified outcomes. Tie readiness
to the applicable frozen gate, identifiable stable artifact, independent
verification, and recorded residual risks. Distinguish observed facts from
inference and uncertainty. Use compact delta updates with links to durable
evidence; retain the technical detail needed to reproduce decisions and avoid
lossy summaries. Report blockers and unresolved risks rather than declaring
readiness without evidence.
