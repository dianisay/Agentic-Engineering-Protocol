# Agent Orchestration Protocol

## Copy-Paste This Prompt to Get Started

You do not need to clone or install anything yourself. Copy the prompt below
into a coding agent that can run terminal commands (for example, a CLI or IDE
agent with shell access). It finds or downloads this repository, sets it up,
verifies it, and tells you how to start.

```text
Set up the Agentic Engineering Protocol on this machine. Actually perform
every step below with your own tools; do not just explain them to me. Work
autonomously and stop only for the items under "Ask me first".

Repository: https://github.com/dianisay/Agentic-Engineering-Protocol
(its README is titled "Agent Orchestration Protocol"; same project)

1. Find or get the checkout. Choose the path with the first rule that applies:
   a. the path in the AEP_HOME environment variable, if it is set;
   b. the current directory or one of its parents, if it is a checkout of
      this repository;
   c. a folder named Agentic-Engineering-Protocol in my home directory.
   A folder is a checkout of this repository when "git remote get-url origin"
   names dianisay/Agentic-Engineering-Protocol (HTTPS or SSH, with or without
   .git). Then:
   - Path does not exist: run
     git clone https://github.com/dianisay/Agentic-Engineering-Protocol.git <path>
   - Path is a checkout: reuse it; never clone a second copy. Run
     "git fetch origin". If the working tree is clean and the current branch
     is the default branch (origin/HEAD, normally main), run
     "git pull --ff-only". If it has local
     changes, is on another branch, or cannot fast-forward, do not reset,
     stash, discard, or force anything: keep it as it is and report it.
   - Path exists but is not a checkout: do not touch it. Use the same name
     with the first free suffix (-2, -3, ...) in the same folder.
2. Read README.md in the checkout, especially "Setup and verification" and
   "Start using it", and the documents they link to. They are the source of
   truth. If they disagree with this prompt, follow them and tell me why.
   Do not invent a different setup.
3. Inspect the environment: operating system, shell, git, Python, uv,
   network access, and which capabilities you actually have (running
   commands; reading and writing files; listing, messaging, or creating
   agent sessions; custom agents). Verify each with read-only or harmless
   checks; if checking would create a session or send a message, report it
   as untested instead. Do not assume.
4. Perform "Setup and verification" exactly, including its fallback when uv
   is unavailable. Fix ordinary problems yourself when it is safe, such as a
   missing user-level tool or a broken .venv inside the checkout.
5. Run its verification commands. Setup is complete only if every one
   passes. Never report success for a failed or skipped check.
6. Report: checkout path and commit; whether you cloned, updated, or reused
   it and anything you left untouched; what you installed; each command and
   its result; verified and unavailable capabilities; anything I must do.
   Then tell me the protocol is ready and give me the first prompt from
   "Start using it", with the checkout path filled in, and ask me which
   project folder and output folder to use for the other placeholders.

Ask me first before: using administrator or sudo rights; entering or
creating credentials; deleting or overwriting existing files; changing an
existing checkout's branch or local changes; writing outside the checkout
and user-level tool locations and caches; or choosing which of my projects
to audit.
Send nothing to any service except what setup needs (the git host and the
Python package and tool downloads named in the README).
```

When setup is done, the agent reports the checkout path and the
[first prompt](#start-using-it) to use. Re-running the prompt updates an
existing checkout instead of downloading another copy.

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

The [bootstrap prompt](#copy-paste-this-prompt-to-get-started) obtains and
verifies a checkout for you; to do it by hand, follow
[setup and verification](#setup-and-verification). Open the checkout in your
assistant host. If your host supports repository-local custom agents, select
one of the roles in [.github/agents](.github/agents/); consult your host's
documentation to configure available tools. The
[setup guide](docs/getting-started.md#configure-roles-and-session-capabilities)
explains how to check tool access and use a manual fallback. Otherwise, copy
the relevant role instructions into a chat. Never change private editor
internals to expose tools. Do not share a private project, session transcript,
or artifact with any external provider without authorization.

## Setup and verification

The protocol is a set of Markdown files; nothing runs as a service and
nothing is installed into your projects. Setup means having a checkout of
this repository and confirming it is intact with its offline checks. Run
these commands from the checkout root.

1. **Get or update the checkout.** You need `git`.

   ```sh
   git clone https://github.com/dianisay/Agentic-Engineering-Protocol.git
   cd Agentic-Engineering-Protocol
   ```

   Any folder works; the bootstrap prompt defaults to
   `Agentic-Engineering-Protocol` in your home directory. For an existing
   clean checkout on the default branch, update it instead with
   `git pull --ff-only`. Do not reset or discard local changes to
   update.
2. **Install the check tools.** Use [uv](https://docs.astral.sh/uv/). If it is
   missing, install it at user level with its
   [official instructions](https://docs.astral.sh/uv/getting-started/installation/).
   `uv` creates `.venv` inside the checkout and downloads a Python 3.11+
   interpreter if none is available.

   ```sh
   uv sync --locked
   ```

3. **Verify.** Both commands must succeed:

   ```sh
   uv run --locked python -m unittest discover -s tests
   uv run --locked python scripts/check_docs.py
   ```

   Expected: the tests end with `OK`, and the checker reports
   `Checked <N> Markdown files and 5 agent headers; 0 errors.`

**Fallback without uv** (requires Python 3.11 or newer; the package versions
match [pyproject.toml](pyproject.toml)):

```sh
python3 -m venv .venv
.venv/bin/python -m pip install "markdown-it-py>=3.0,<5" "PyYAML>=6.0.3,<7"
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/check_docs.py
```

If `python3` is older than 3.11, use a newer interpreter such as
`python3.12`. On Windows, use `py -3` instead of `python3`, and
`.venv\Scripts\python` instead of `.venv/bin/python`. On Debian or Ubuntu,
`venv` may need the `python3-venv` system package, which requires
administrator rights; installing uv at user level avoids that.

These checks confirm that the files are complete and internally linked. They
do not test your agent host. Which capabilities your host has (running
commands, listing, messaging, or creating sessions) is checked when you start,
as part of the audit.

## Start using it

Paste this prompt into your agent, replacing the placeholders. `<AEP_PATH>`
is the checkout path reported by setup. `<WORKSPACE_ROOT>` is the project
folder you want coordinated. `<OUTPUT_DIRECTORY>` is a folder where planning
records may be written, outside protected work.

```text
Use the Agentic Engineering Protocol in <AEP_PATH>. Read its README.md and
act as its Orchestrator, as defined in
<AEP_PATH>/.github/agents/orchestrator.agent.md. Audit <WORKSPACE_ROOT>
following <AEP_PATH>/protocol/01-audit.md: discover existing projects,
sessions, evidence, and the session capabilities you actually have. Do not
modify existing work. Write records only under <OUTPUT_DIRECTORY>, using the
templates in <AEP_PATH>/templates/. Record unknowns. Do not start workers
or take consequential actions until I approve a plan.
```

If your host supports repository-local custom agents (for example VS Code),
you can instead open the checkout as a workspace and select the
**Orchestrator** agent. Continue with the [quick start](#quick-start) after
the audit.

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
