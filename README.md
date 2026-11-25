# Agent Orchestration Protocol

A reusable, evidence-driven protocol for coordinating persistent AI agent
sessions through auditing, planning, dependency management, peer-to-peer
communication, and independent validation.

## What this does

This repository provides instructions and templates, not an orchestration
server. It helps an orchestrator discover work and existing sessions, map
dependencies, delegate bounded work, and verify stable results. It fits
software, research, data, documentation, and other projects without assuming
a particular tool, infrastructure, priority, or project layout.

Ordinary parallel agents may each solve an isolated task and return to a
parent. A persistent-session orchestrator additionally tracks ownership,
history, dependencies, approvals, and handoffs across work that may outlive
a single turn. Direct session-to-session communication lets an owner resolve
an actual dependency without routing every technical detail through the
orchestrator. Messages are evidence and requests, not authority to change
scope or write another worker's artifacts.

## Prerequisites and installation

1. A working directory you are authorized to inspect and an approved place to
   write planning artifacts.
2. An AI assistant or team willing to follow Markdown instructions. For automatic
   session discovery, inspection, messaging, and creation, the chosen host
   must actually provide and authorize those capabilities. They are optional.
3. Optional: a host supporting VS Code-compatible custom agents. These files
   supply role instructions; they do **not** install tools or enforce a security
   sandbox.

Clone or copy this repository to a location you control. Open it in your
assistant host. If your host supports repository-local custom agents, select
one of the roles in [.github/agents](.github/agents/); consult your host's
documentation to configure available tools. The
[setup guide](docs/getting-started.md#configure-roles-and-session-capabilities)
explains how to check tool access and use a manual fallback. Otherwise, copy
the relevant role instructions into a chat. Never change private editor
internals to expose tools. Do not share a private project, session transcript,
or artifact with any external provider without authorization.

## Quick start

1. Choose an authorized `<WORKSPACE_ROOT>` and `<OUTPUT_DIRECTORY>` outside
   protected artifacts. Set the desired outcome, budget and approval boundary.
2. Ask the orchestrator: “Audit the approved workspace and discover existing
   projects, sessions, evidence, and available session capabilities. Do not
   modify existing work. Record unknowns.” Use the [audit procedure](protocol/01-audit.md)
   and [audit template](templates/audit-report.md).
3. Review the audit. Ask for a prioritized portfolio and a worker plan for each
   actionable project using [portfolio planning](protocol/02-portfolio-planning.md).
   Plans must investigate relevant state of the art and compare alternatives,
   using verified sources and noting uncertain or inaccessible research.
4. Route existing sessions or propose new ones using [routing](protocol/03-session-routing.md).
   Record the canonical owner, historical references and artifact ownership.
5. Once the human authorizes the scope, activate bounded workers with the
   [worker contract](templates/worker-contract.md) and
   [activation procedure](protocol/04-session-activation.md). Workers may
   communicate directly with a relevant dependency using the
   [communication protocol](protocol/05-inter-agent-communication.md).
6. Monitor meaningful transitions rather than repeatedly asking a model for
   job status. See [execution and monitoring](protocol/06-execution-and-monitoring.md).
   At a consequential decision or conflict, use a temporary, independent,
   read-only critic; at a stable gate, use an independent validator.
7. Preserve results, failed attempts, verification scope, and unresolved
   decisions in the [evidence manifest](templates/evidence-manifest.md) and
   [handoff](protocol/08-handoff-and-closure.md).

Try the fully fictional [sample project](examples/sample-project/README.md)
before using this on an active workspace.

### If session tools are unavailable

Do not claim to have listed, inspected, contacted, or created sessions. Record
each missing capability and obtain authorized inventories and handoffs from a
human instead. The same audit, plan, contract, and validation formats work
with manually operated chats. Peer communication then requires a human to
relay the specific message and receipt; independent roles require separate
people or separate contexts when available. See [session routing](protocol/03-session-routing.md).

## Reading map

- [Getting started](docs/getting-started.md) and [architecture](docs/architecture.md)
- [Session lifecycle](docs/session-lifecycle.md) and [safety and boundaries](docs/safety-and-boundaries.md)
- [Research and state of the art](docs/research.md)
- [Audit](protocol/01-audit.md) → [planning](protocol/02-portfolio-planning.md) →
  [routing](protocol/03-session-routing.md) → [activation](protocol/04-session-activation.md) →
  [communication](protocol/05-inter-agent-communication.md) →
  [execution](protocol/06-execution-and-monitoring.md) →
  [validation](protocol/07-validation.md) → [closure](protocol/08-handoff-and-closure.md)
- [Templates](templates/) and [contributing](CONTRIBUTING.md)

## Limits

Roles are behavioral instructions, not access controls. Tool availability,
persistence, isolation, provenance, resource tracking, and notification
semantics depend on the host. A watcher event, file existence, or worker
statement alone does not establish a successful engineering result. This
protocol cannot guarantee correctness, safety, independence, or token savings;
it makes evidence and decisions inspectable. Human approval is required for
consequential actions as defined by the project boundary.
