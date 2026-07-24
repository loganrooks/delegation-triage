# Proposal: cross-runtime routing and Codex-managed Claude delegation

- **Date:** 2026-07-17
- **Status:** Reviewed; accepted for an implementation-authorization decision
- **Closure target:** approved architecture and implementation boundary
- **Canonical home:** this repository, per SEAS ADR-0024
- **Implementation authorized:** no
- **Paid external model calls authorized:** no
- **Review:** [`2026-07-17-cross-runtime-routing-proposal-review.md`](../reviews/2026-07-17-cross-runtime-routing-proposal-review.md)

## 1. Decision requested

Extend this repository's Codex adapter into a governed `delegate-to-claude` capability. Codex
would remain the parent orchestrator and directly manage multiple explicit Claude CLI sessions,
while each Claude session would invoke the canonical `delegation-triage` skill before deciding
whether and how to create any Claude-native descendants.

Keep one canonical Claude routing doctrine, host-runtime-agnostic contract, and evidence vocabulary
in this repository, with separate Claude Code and Codex adapters. Automate drift detection and
update notification, but require a reviewed, explicit action to activate routing-policy changes.
Do not introduce a provider-neutral route catalog or provider-specific route split in this slice.

This proposal selects **Option 3: Codex-managed multiple Claude sessions** as the primary control
plane. It retains **Option 2: one Claude orchestrator session with Claude-native descendants** as
an explicitly requested lane-local mode, not as the cross-runtime manager.

## 2. Source map and claim labels

The labels below follow [`EPISTEMICS.md`](../../EPISTEMICS.md).

| Claim | Label | Source or check | What remains uncertain |
|---|---|---|---|
| This repository is the accepted canonical home for a platform-agnostic core plus runtime adapters. | Concordant | SEAS ADR-0024; [`LINEAGE.md`](../../LINEAGE.md) | A later federation decision could supersede the ADR. |
| The current Codex adapter emits consumer guidance only. | Corroborated | [`install.py`](../../install.py), [`adapters/codex/README.md`](../../adapters/codex/README.md) | It does not establish what future Codex surfaces will expose. |
| The canonical routes distinguish Claude task classes and model × effort pairs. | Concordant | [`ROUTES.md`](../../ROUTES.md), [`CONTRACT.md`](../../CONTRACT.md) | Route quality remains bounded by each cited warrant and probe history. |
| The locally observed Claude Code 2.1.212 binary advertises print mode, explicit model and effort, session IDs, resume/fork, background agents, worktrees, structured streaming output, tool restrictions, budgets, and debug files. | Concordant | `claude --version`, `claude --help`, and `claude agents --help` run 2026-07-17 | Help text does not establish runtime semantics, authentication behavior, enforcement, or output-field availability. |
| The advertised CLI controls enforce the semantics this adapter needs. | Unchecked | No live generative capability probe was authorized | Reliance on a real control requires dated actual-runtime evidence. Fake-CLI tests establish adapter handling only. |
| Resuming a stable session can preserve prompt-cache eligibility. | Provisional | Provider caching semantics plus observable cache counters in structured results | A cache hit cannot be guaranteed; exact cache keys and expiry are provider-controlled. |
| Cross-runtime routing can improve rigor through content-free outcome events and controlled probes. | Conjecture | Proposed method; consistent with this package's warrant/probe discipline | There is not yet a sufficiently large, comparable cross-runtime cohort. |

## 3. Problem

Codex can invoke `claude -p`, but a raw shell call is not a delegation system. Without a governed
adapter, a parent can silently lose or misreport:

- the route selected by Claude's own triage doctrine;
- planned versus requested versus actually observed model and effort;
- session identity, resume lineage, and cache evidence;
- task ownership and write isolation across concurrent workers;
- permission, budget, timeout, and cancellation boundaries;
- partial output and failure evidence when a paid run behaves unexpectedly;
- comparable, privacy-preserving outcome records that can challenge routing priors.

Copying Claude's routing table into a Codex-only skill would introduce a second source of truth.
Making a single Claude session the universal orchestrator would instead hide cross-session
control and evidence behind that session. Both approaches weaken the canonicality already chosen
in ADR-0024.

## 4. Goals and non-goals

### Goals

1. Let Codex start, inspect, wait for, and deliberately resume multiple Claude CLI sessions.
2. Make each route explicit before launch and distinguish planned, requested, and observed route.
3. Reuse this repository's canonical doctrine without erasing provider-specific constraints.
4. Preserve cache eligibility where reasonable and report observed cache creation/read counters.
5. Provide predictable recovery for auth, permission, wrapper, timeout, refusal, and partial-output
   failures without automatically spending on a second run.
6. Keep routing evidence content-free, auditable, and incapable of silently mutating policy.
7. Package installation, drift checks, and capability probes for reuse across projects.

### Non-goals

- A universal learned router in the first release.
- Guaranteed prompt-cache hits.
- Transcript or prompt ingestion into routing analytics.
- Automatic paid retries, automatic model escalation, or automatic policy activation.
- Replacing Claude's `delegation-triage` skill or Claude-native agent facilities.
- Synchronizing provider-specific model names, effort semantics, prices, or availability as if they
  were portable facts.
- Implementing remote telemetry, Dionysus archival, monitoring daemons, or central databases in
  this slice.
- Implementing this proposal before it is reviewed and approved.

## 5. Option decision

### Option 2 — one Claude orchestrator session

Codex launches one Claude session and asks it to triage and manage Claude-native descendants.
This is useful when the work is tightly coupled, Claude-native agent messaging is load-bearing,
or the parent only needs one final artifact. It has a smaller Codex-side control surface.

Its costs are weaker per-worker visibility from Codex, coarser cancellation and budget control,
more context concentration, and dependence on Claude's internal resume and descendant semantics.
Cross-runtime evidence tends to collapse into one parent result unless the Claude lane emits a
separate structured manifest.

### Option 3 — Codex manages multiple Claude sessions

Codex classifies a wave, assigns non-overlapping ownership, and starts one explicit Claude CLI
session per lane. Each lane still loads Claude's canonical triage skill and may recommend a
different route or refuse a mis-shaped packet. Codex owns the session registry, polling cadence,
integration, and final disposition.

This adds a small deterministic manager but gives direct session identity, independent budgets,
isolated worktrees or read-only scopes, explicit recovery, and comparable lane outcomes.

### Recommendation and compatibility

Adopt Option 3 as the primary adapter. Support Option 2 later as `mode: claude-orchestrated`, with
the same task-packet and result-envelope contracts. Pursuing Option 2 first would not make Option
3 impossible, but it would make migration harder if session lineage, ownership, and outcome
schemas were designed around one opaque parent result. Defining those contracts now keeps both
modes compatible.

Option 2 remains appropriate for a single internally coupled lane. It must not recursively become
an unbounded second control plane: its descendant policy, maximum depth, budget, and output
manifest must be declared in the packet.

## 6. Architecture

```text
platform-agnostic core
  ROUTES · STATE · CONTRACT · WARRANTS · EPISTEMICS · probes
                |
        adapter contracts
  task packet · route record · result envelope · event schema
          /                         \
Claude Code adapter              Codex adapter
native skill + roster            delegate-to-claude skill
                                  deterministic session manager
                                  capability/drift checks
                |
       Claude CLI session registry
     one owned lane per session/worktree
```

### 6.1 Shared core

For this proposal, **platform-agnostic means host-runtime agnostic for the same canonical Claude
routing doctrine**. Codex and Claude Code consume the existing Claude-specific `ROUTES.md`,
`STATE.md`, and warrants from this repository. Provider-neutral doctrine consists of the
delegation contract, epistemic vocabulary, schemas, precedence rules, probe discipline, and the
distinction between a prior and an observed outcome. These are synchronized because every adapter
consumes the same versioned files from this repository.

A future multi-provider router could separate provider-neutral task classes from provider route
catalogs, but that is a distinct migration requiring reviewed source ownership, versioning,
warrant mapping, and same-pass propagation rules. Phase 1 must not create such a split.

### 6.2 Runtime overlays

The canonical Claude route surfaces continue to own Claude model identifiers, effort priors,
prices, and availability facts. Host-runtime adapters own only the mechanisms used to deliver and
observe those routes: CLI/control mappings, permission surfaces, session semantics, cache
observations, and dated capability probes. A Codex adapter must not create a second Claude route
catalog.

The precedence rule remains:

1. project overlay;
2. active profile;
3. canonical route;
4. runtime capability fallback.

The selected and delivered route must record every applied layer.

### 6.3 Codex adapter components

The first implementation should add:

1. **`delegate-to-claude` skill** — progressive-disclosure instructions for classification,
   packet construction, safe launch, waiting, recovery, inspection, and disposition.
2. **A stdlib-only session manager** — deterministic commands such as `start`, `list`, `status`,
   `wait`, `resume`, `inspect`, and `doctor`. Destructive termination is a separate explicit
   operator action except when the operator pre-authorized a capability-probed
   `hard_runtime_limit` in the packet; that is the only permitted automatic termination path.
3. **Schemas/templates** — task packet, session registry record, result envelope, and content-free
   routing event.
4. **Capability and drift checks** — maintain a dated matrix containing CLI version, advertised
   control, actual-runtime probe method, observed result, expiry/re-check trigger, and evidence
   locator. Fail closed for any required control whose runtime behavior is Unchecked, expired, or
   unavailable; fail safe for telemetry. Fake-CLI fixtures test adapter state transitions but never
   establish real CLI enforcement.
5. **Installer support** — deploy the skill and manager into a governed Codex skill/tool location;
   `--check` reports drift, `--dry-run` shows the intended write set, and install never activates
   new routing policy silently.

Progressive disclosure means the skill's main procedure stays short. Separate references should
cover session/cache semantics, failure recovery, task/result schemas, and evidence recording. The
manager, not prose, should perform fixed-step process management.

## 7. Delegation contract

### 7.1 Task packet

Every lane packet must contain:

- stable run and lane IDs;
- task class and cited route/W-ID;
- requested model and effort plus the control surface that pins them;
- objective, closure target, and explicit non-goals;
- repository root and owned files/artifact surface;
- allowed write scope, forbidden paths, and `write_isolation` mode;
- required sources and read order;
- expected output artifact and concise return shape;
- validation oracle and falsifier;
- permission mode and allowed/disallowed tools;
- `hard_spend_limit`, `hard_runtime_limit`, and `observation_deadline`, each classified as
  `enforced`, `advisory`, or `unavailable` with its capability-evidence locator;
- whether Claude-native descendants are forbidden or bounded;
- instruction to invoke Claude's `delegation-triage` skill before any descendant delegation;
- instruction that the worker is not alone and must not revert others' changes.

The packet should be stored as a file and passed by stable reference where practical. Repeatedly
embedding a changing, large preamble undermines cache eligibility and auditability.

### 7.2 Result envelope

Every lane returns:

- status: `complete`, `blocked`, `failed`, `refused`, or `timed_out`;
- artifact path(s) and owned-file changes;
- concise findings/changes;
- assumptions and open questions;
- verification performed and result;
- planned, requested, and observed model/effort;
- session ID and resume/fork lineage;
- token and cache counters when exposed;
- risks, conflicts, and recommended disposition.

The orchestrator, not the worker, records `accept`, `revise`, `park`, or `reject`.

Every packet, registry entry, result envelope, and disposition references one immutable,
versioned **route-decision record**. That record contains:

- content hashes or commit IDs for `ROUTES.md`, `STATE.md`, and any project overlay;
- selected task class/W-ID, active profile, applied overlay, fallback decision, and their order;
- requested-control mapping version;
- planned and requested model/effort/role/surface;
- for each delivered field: `{value, status: observed|unobserved|conflicted,
  evidence_locator_or_hash}`;
- one monotonic lifecycle ID carried through resume/fork and terminal reconciliation.

The evidence locator may identify local structured output or a digest, but a self-report may not be
upgraded to `observed`. A terminal lane requires exactly one durable reconciliation record linking
the final envelope to the orchestrator disposition. Crash-before-disposition remains a visible
unreconciled state, not inferred success.

### 7.3 Ownership and concurrency

`write_isolation` has three valid values:

- `read_only` — a capability-probed tool/permission set that cannot write; if the runtime cannot
  enforce this, the mode is unavailable rather than advisory;
- `dedicated_worktree` — one writer in one isolated worktree, with a pre/post diff gate; direct
  concurrent writers in the shared checkout are unsupported;
- `filesystem_allowlist` — only when a dated capability probe establishes that the execution
  environment actually confines writes to canonicalized allowed paths.

Before launch, canonicalize the repository and declared paths without following an untrusted final
symlink; reject paths outside the repository, duplicate real targets, symlink aliases, and
ancestor/descendant overlaps across lanes. A dedicated worktree contains a lane's changes but does
not prove compliance with its internal file allowlist, so terminal validation must diff the entire
worktree and reject integration when any undeclared path changed. A reviewer is `read_only` or a
single-writer dedicated worktree owning only its review artifact.

A worktree is not permission to merge, commit, push, delete, or modify the shared checkout. No
session may broaden tools, directories, spend, runtime, or descendant depth beyond the packet.
Operator-declared conflict plans are deferred; the first concurrent release refuses overlap.

### 7.4 Option 2 descendant manifest

Option 2 is deferred, but its compatibility contract is normative now. A
`claude-orchestrated` parent packet declares maximum descendant depth, maximum concurrent and total
descendants, aggregate spend/runtime limits, ownership/isolation policy, and whether any child may
create descendants.

The parent result includes a `descendant_manifest` digest, completeness state, and one opaque entry
per descendant. Each entry uses the same run/lane/session, route-decision, lifecycle, ownership,
permission, limit, resume/fork, observed-route, validation, and terminal-disposition identifiers as
an Option 3 lane. Missing or incomplete descendant data makes the parent lane failed for strict
work and non-comparable for routing evidence; it must never be collapsed into a normal complete
parent result.

## 8. Session, resume, cache, and polling semantics

### 8.1 Session registry

The adapter keeps a small local registry under a generated-state directory, not in project source.
Each record contains IDs, timestamps, repository identity, policy/adapter version, packet hash,
requested controls, process/background-agent handle, output/debug paths, state, and result
metadata. It must not contain prompt or transcript text.

Write records atomically. Treat the CLI's observed structured output and session files as runtime
evidence; the registry is an index, not an authority that may invent success.

### 8.2 Resume policy

Resume only when the same lane's objective and trust boundary remain valid. Preserve the session
ID, model alias or full identifier, effort, settings sources, system-prefix inputs, tool policy,
and working directory. Record any difference. Use a fork when branching the reasoning history is
intentional; never disguise a fork as continuation.

A generic resume that cannot reassert or observe the planned model/effort is non-compliant. The
adapter must label the delivered route `unknown` or stop according to the packet's strictness.

### 8.3 Cache contract

The adapter promises only **cache eligibility**, not a hit. It should:

1. keep stable instructions and referenced context stable and early;
2. append new turn-specific material after the stable prefix;
3. reuse the same session when semantically valid;
4. avoid unnecessary changes to model, tools, settings, working directory, and system inputs;
5. record observed `cache_creation_input_tokens` and `cache_read_input_tokens` when emitted;
6. report zero or absent reads as cold/unknown, never as success;
7. never launch a paid retry merely to improve cache statistics.

### 8.4 Polling and timeout

Long-running Opus reviews should use multi-minute polling, normally 5–10 minutes, unless process
state requires a faster check. Silence alone is not failure.

The three time/spend controls are distinct:

- `hard_spend_limit` — a proven provider/CLI-enforced ceiling for this lane;
- `hard_runtime_limit` — a proven provider or manager/runtime enforcement that makes the child
  terminal and is explicitly pre-authorized by the operator in the packet;
- `observation_deadline` — when the parent stops waiting synchronously; it does not stop the child.

Every control carries `enforced`, `advisory`, or `unavailable` plus dated actual-runtime capability
evidence. Do not launch a packet that requires a hard limit unless that control is currently proven;
otherwise the operator must explicitly accept advisory exposure. An observation deadline reached
while the process is alive transitions to `timed_out_waiting`, which is non-terminal and
potentially still spending. `timed_out_provider_limit` records a provider-side self-terminating
ceiling; `timed_out_manager_limit` records the sole automatic manager termination path, which
requires the operator's packet-level pre-authorization; `terminated_by_operator` records an
interactive termination. Termination is never inferred from silence or loss of the parent shell.

Expiry is a process outcome, not negative review evidence. Preserve stdout, stderr, structured
output, debug logs, and the last visible messages before considering any paid follow-up. Do not
terminate a healthy process merely because the parent turn is ending.

## 9. Permissions, spending, and recovery

The adapter must default to the least-capable capability-probed tool and permission set that can
satisfy the packet. Advertised controls remain Unchecked until the capability matrix records their
runtime behavior. Permission bypass is never inferred from filesystem access or a user's general
request to proceed. Network access, installation, commits, pushes, destructive commands, and
external side effects need their own task authority.

A requested hard spend or runtime boundary fails closed when its evidence is absent, expired, or
conflicted. An advisory limit must be labeled as exposure, never rendered as a budget guarantee.
The state machine and fake CLI must cover provider self-termination, pre-authorized manager
termination, interactive operator termination, advisory observation expiry, child survival after
parent exit, refusal, and loss of process identity. These fixtures prove adapter behavior only;
actual limit enforcement remains Unchecked until a separately authorized real-runtime probe records
it.

Every Claude call is treated as paid/scarce even when covered by a subscription. On unexpected
behavior:

1. inspect process state, stdout, stderr, output files, and the last visible model messages;
2. determine whether the model attempted a write, asked for permission, was refused, hit auth or
   proxy visibility, or was blocked by the wrapper;
3. preserve partial output without overwriting it;
4. record the failure mode and stop;
5. obtain explicit approval before any new external call intended to retry, repair, or expand.

The manager's `doctor` command may check executable presence, version, help-advertised flags,
authentication status through a non-generative command, writable generated-state paths, and
adapter drift. It must not send a model prompt as a health check.

## 10. Synchronization, releases, and updates

### 10.1 One source, generated adapters

Shared route doctrine changes once in this repository. Installers materialize version-stamped
Claude and Codex adapters. Deployed copies carry source commit and content hashes so drift is
deterministic.

The Codex skill must not copy and independently edit `ROUTES.md`. It either reads the canonical
checkout or deploys a stamped snapshot whose drift can be checked against that checkout.

### 10.2 Notification without silent activation

An updater may:

- check an explicitly configured local canonical checkout;
- report installed versus available version and file hashes;
- render a dry-run diff and migration notes;
- notify through the invoking CLI's normal output.

It may not fetch from the network, install, rewrite a route, change an active profile, or deploy a
new adapter without explicit authorization. Scheduled/background update monitoring is outside this
proposal. A future network updater requires a separate supply-chain design: signed release or
verified digest, pinned source, rollback, and audit log.

### 10.3 Policy-change gate

Capability/tooling changes and routing-policy changes are released separately. A route change
requires the existing same-pass propagation discipline: affected surface, warrant/flip counter,
probe record, and probe index. Adapter releases must state which core policy version they consume.

## 11. Evidence and learning loop

### 11.1 Content-free event

Record only operational metadata needed to compare routing outcomes:

- event, opaque salted project, run, lane, parent, route-decision, lifecycle, reconciliation, and
  session identifiers;
- timestamp; core policy, adapter, CLI, and schema versions;
- task class and closure target;
- planned, requested, and observed model/effort/role/surface;
- packet completeness code and ownership/isolation mode;
- elapsed time, turns, input/output tokens, and cache creation/read counters when available;
- validator outcome, rework count, refusal/failure/friction codes, and disposition;
- probe ID, cohort key, hypothesis, falsifier code, and confounder codes where applicable.

Do not record prompts, transcripts, command text, tool output, file contents, secrets, credentials,
or raw hook payloads. Identifier fields reject filesystem paths, repository/organization/customer
names, branch names, artifact names, and free text. The salted `project_id` maps to a project only
in a separate local access-controlled mapping, never in the routing event store. Sensitive
execution lineage may be held in an access-controlled provenance system and referenced only by
opaque ID.

### 11.2 From signal to route change

The rigorous loop is:

1. append a schema-valid event;
2. compare only cohorts with compatible task class, closure target, validator, packet quality, and
   material runtime conditions;
3. preregister a bounded hypothesis, expected direction, falsifier, and confounders;
4. run controlled or naturally paired probes where spend and ethics allow;
5. review the probe artifact independently;
6. update a warrant and flip tally;
7. require the existing evidence threshold and an explicit maintainer decision;
8. version and deploy the policy change separately from evidence collection.

No event directly trains or mutates the router. At the expected early data scale, descriptive
cohorts and preregistered paired probes are preferable to a learned router. Missing validation,
selection bias, differing packet quality, retries, and parent-model effects must be treated as
confounders rather than averaged away.

## 12. Generated-state and privacy boundary

The adapter should use a user-level local data plane rather than a project `.codex/telemetry`
directory. Project repositories may hold explicit, reviewable probe records, but transient session
registries, process logs, and content-free events belong in a governed user-level state location.

Recommended lifecycle controls:

- configurable byte cap with pre-write accounting and oldest-terminal-run eviction;
- separate caps for structured metadata and potentially transcript-bearing CLI/debug artifacts;
- never evict active runs;
- surface dropped/evicted counters;
- restrictive permissions on lineage and debug artifacts;
- no remote synchronization in the initial implementation.

The previously discussed `<250 MiB` constraint is best treated as a campaign-level safety budget
for newly generated local state until measurement establishes a justified steady-state policy. It
is not a claim that a future inventory or telemetry database must remain under 250 MiB forever.
The implementation plan must allocate explicit sub-budgets and test pre-write rejection/eviction;
the exact long-term lifecycle remains a stakeholder decision.

## 13. Phased implementation

### Phase 1 — contracts and dry-run tooling

Sequence three independently reviewable vertical sub-slices:

1. pure packet, route-decision, lifecycle/reconciliation, result, descendant-manifest, and event
   schemas with fixtures;
2. a read-only `plan --dry-run` that consumes those objects and prints the exact route, capability,
   process, ownership, limit, and write plan without launching anything;
3. progressive-disclosure skill, then installer `--check`/deployment stamps only after dry-run
   output is stable.

Add deterministic tests for schema validation, route provenance, identifier privacy, canonicalized
path ownership, capability expiry, and configuration validation. Before the operator approves a
state root and sub-budgets, all Phase 1 tests use in-memory or test-runner-owned temporary fixtures;
any command that would persist generated state fails closed on missing explicit configuration.

**Exit:** a cold agent can construct and validate a complete packet and see the exact command,
route-decision provenance, enforced-versus-advisory controls, and write set without launching
Claude or writing unapproved persistent state.

### Phase 2 — one managed session

- Add explicit start/status/wait/inspect for one print-mode session.
- Capture structured result and observed route/cache counters.
- Exercise read-only and isolated-write fixtures plus hard/advisory limit state transitions using
  a non-paid fake CLI in tests.

**Exit:** failure recovery preserves evidence; no automatic retry; task/result contracts validate.

### Phase 3 — multiple isolated sessions

- Add bounded concurrency, disjoint ownership checks, and worktree integration.
- Add resume/fork validation and declared polling/timeout policy.
- Require orchestrator disposition for every terminal lane.

**Exit:** concurrent fixture lanes use only enforceable `write_isolation` modes; ancestor,
descendant, and symlink-alias overlaps are refused; an undeclared-write fixture is contained and
rejected by the whole-worktree diff gate; terminal and `timed_out_waiting` lanes recover correctly
after manager restart.

### Phase 4 — evidence and release workflow

- Emit content-free events to the existing orchestration-learning-compatible sink or a documented
  adapter; do not duplicate its store.
- Add cohort/probe templates and policy promotion checks.
- Add version/drift notification and migration notes; activation remains manual.

**Exit:** a route change can be reconstructed from events through reviewed warrant and versioned
release, with no prompt content in the evidence plane.

### Phase 5 — optional Claude-orchestrated mode

- Add Option 2 using the normative descendant-manifest, depth, aggregate-limit, ownership,
  route-observation, and reconciliation contracts defined in §7.4.

**Exit:** Option 2 and Option 3 produce compatible result envelopes and evidence fields.

## 14. Expected implementation write set

Exact filenames remain subject to review, but implementation is expected to touch only:

- `adapters/codex/` for the new skill, references, schemas, manager, and tests;
- `install.py` and its tests/check fixtures;
- core contract/route/warrant/probe surfaces only when a reviewed policy claim changes;
- `README.md`, `ROADMAP.md`, and adapter documentation;
- generated `dist/` only when explicitly building a release artifact.

The current unrelated probe record is outside this proposal's write set. No implementation agent
may revert or fold it into its work.

## 15. Alternatives considered

| Alternative | Disposition | Reason |
|---|---|---|
| New central repository | Reject | ADR-0024 already assigns this role to this repository. A second repo recreates canonicality drift. |
| Copy Claude routes into a standalone Codex skill | Reject | Independent copies will drift and erase same-pass warrant/probe updates. |
| Option 2 as the only control plane | Retain as later mode | Appropriate for coupled Claude-native work, but too opaque as the default cross-runtime manager. |
| Option 3 with automatic route learning | Reject for now | Current evidence volume and confounding do not justify a learned router; automatic mutation violates the warrant gate. |
| Human-run shell snippets only | Reject as primary | Fixed-step session/process management belongs in deterministic tooling, not repeated prose. |
| Remote central telemetry/database now | Defer | Expands privacy, lifecycle, availability, and supply-chain scope before the local contract is tested. |

## 16. Decisions, open questions, and falsifiers

### Proposed decisions

1. This repository remains the canonical package.
2. Option 3 is the primary Codex control plane; Option 2 is a later bounded mode.
3. Existing Claude routes remain canonical across host runtimes; host-control mechanics remain
   adapter-owned. A provider-neutral route split is out of scope.
4. Updates notify and diff automatically only when invoked; activation is explicit.
5. Evidence is content-free and cannot mutate policy directly.
6. Implementation proceeds in testable phases, beginning with contracts and dry-run tooling.

### Stakeholder decisions still needed before implementation

- The initial user-level generated-state root and exact sub-budget split within the `<250 MiB`
  campaign cap.
- Whether real paid-model smoke tests are permitted after fake-CLI tests pass, and their maximum
  number/budget.
- Whether termination should exist in the first manager release or remain manual.
- Whether Option 2 belongs in the first public milestone or remains deferred through Phase 4.

### Design falsifiers

- If the adapter cannot reliably observe or reassert model/effort on resume, strict resume must be
  disabled rather than inferred.
- If read-only or write isolation cannot be capability-probed and whole-lane diffs cannot reject
  undeclared writes, concurrent writer mode must remain disabled.
- If a hard spend/runtime requirement cannot be proven enforced, the lane must not launch without
  an explicit operator decision accepting advisory exposure.
- If a 10-run audit cannot reconstruct planned/requested/observed route and disposition, the event
  and registry contracts are insufficient.
- If content-free events cannot distinguish packet-quality or validator confounders, they must not
  be used to promote routes.
- If two adapter releases require hand-copying shared route doctrine, the packaging boundary has
  failed.
- If Option 3 adds manager failures without improving isolation, recoverability, or audit yield
  over comparable Option 2 lanes, reconsider the primary-mode decision.

## 17. Review and authorization gate

The cold-read [review](../reviews/2026-07-17-cross-runtime-routing-proposal-review.md) returned
`revise`: 0 BLOCKER, 5 MAJOR, 2 MINOR, and 2 NOTE. The orchestrator accepted all findings and
revised this document to:

- make isolation modes and undeclared-write rejection testable;
- distinguish hard spend/runtime enforcement from an observation deadline;
- add immutable route-decision, lifecycle, reconciliation, and disposition provenance;
- define the Option 2 descendant manifest contract now;
- clarify that current routes are Claude-specific but shared across host runtimes;
- downgrade help-text capability claims, require a dated capability matrix, salt project IDs, and
  split Phase 1 into smaller sub-slices with a generated-state approval gate.

The post-revision audit resolved eight findings and left one partial Minor plus one new Major. A
final narrow correction resolved both without a new Blocker or Major. The review's **effective
final recommendation is accept for an implementation-authorization decision**. This is not itself
implementation authorization.

Approval of this document authorizes planning only. It does not authorize implementation,
installation, deployment, model calls, network access, background monitoring, commits, or policy
activation.
