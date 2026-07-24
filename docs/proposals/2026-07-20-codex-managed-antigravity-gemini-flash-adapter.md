# Proposal: minimal Codex-managed Antigravity adapter for Gemini Flash

- **Date:** 2026-07-20
- **Status:** accelerated temporary MVP implemented and manually activated 2026-07-20; exhaustive
  capability certification remains deferred
- **Audience:** implementers and reviewers of the Codex adapter surface
- **Closure target:** an installed user-level skill and directly invocable adapter that can run bounded Gemini Flash
  work through the official Antigravity CLI without building the deferred general router
- **Authority:** the 2026-07-20 execution decision authorized implementation, user-level skill
  installation, and one bounded live smoke task. It did not authorize commits, automatic routing,
  downloads, monitoring, or the deferred hardening controls.
- **Depends on:** the non-activating composable policy core, corrected to expose its pure modules
  through a provider-neutral package boundary
- **Future compatibility:** conforms to the extension seam in the
  [deferred multi-harness router proposal](2026-07-20-provider-neutral-multi-harness-delegation-router-deferred.md)

## 1. Decision and execution order

Add a small Codex-managed adapter that invokes the official `agy` executable with an explicitly
selected Gemini Flash model. The adapter is manually selected; it does not decide between Codex,
Claude, and Gemini, and it does not introduce a provider-neutral router.

Proceed in this order:

1. revise the C0 plan so its schema, diff, and explanation modules have a provider-neutral package
   boundary while Claude-specific presets remain in the Claude adapter;
2. implement and independently verify C0 without activating any provider runtime;
3. write a separate test-first implementation plan for this Antigravity adapter;
4. implement the adapter against fake-CLI fixtures and deterministic filesystem tests;
5. separately authorize a small actual-runtime capability probe; and
6. activate only the profiles and lifecycle operations established by that probe.

The adapter must remain complete and useful without the future router. The router may later select
the adapter through its stable packet/result boundary.

## 2. Problem

The operator has subscription-backed Antigravity access with Gemini Flash capacity that can absorb
bounded implementation, investigation, test, and review work. Codex can invoke `agy -p` directly,
but a raw shell call does not preserve:

- the exact requested and observed model;
- the workspace and ownership contract;
- permission, sandbox, network, and host-effect assumptions;
- durable stdout, stderr, log, process, and terminal-state evidence;
- recovery and result materialization;
- generated-state accounting; or
- root reconciliation and disposition.

Copying the Claude manager and renaming its flags would misstate equivalence between two different
harnesses. Building the full multi-provider router would delay the immediate capability. The
minimal adapter therefore reuses stable policy and evidence contracts while owning Antigravity-
specific command construction, probes, and runtime claims.

## 3. Evidence and limitations

| Claim | Status | Evidence and limitation |
|---|---|---|
| The installed `agy` is version 1.1.4 and advertises `--print`, `--model`, `--agent`, `--conversation`, `--continue`, `--log-file`, `--print-timeout`, `--mode`, `--sandbox`, and `--dangerously-skip-permissions`. | Observed | Local `agy --version` and `agy --help`, run 2026-07-20. Help text does not establish enforcement or headless behavior. |
| The installed account currently lists Gemini 3.5 Flash at Low, Medium, and High settings. | Observed | Local `agy models`, run 2026-07-20. Availability is volatile and must be checked at launch; a listed model is not proof of delivered identity. |
| Antigravity CLI supports multi-file editing, tools, and conversation history. | Reported | Google [Antigravity CLI codelab](https://codelabs.developers.google.com/antigravity-cli-hands-on), introduction. Provider documentation does not prove the local wrapper can observe every relevant event. |
| `agy -p` is intended for non-interactive automation and `--model` selects a model for a session. | Reported | Google codelab, “Non-interactive mode” and “Choose a specific model.” The same page warns that its basic `-p` example has no follow-up interaction. |
| Antigravity documents request-review, proceed-in-sandbox, always-proceed, and strict permission concepts. | Reported | Google codelab, “Tool Permission.” The installed CLI exposes only `plan` and `accept-edits` through `--mode`, plus separate sandbox and skip-permission flags; mapping between these surfaces is Unchecked. |
| `--dangerously-skip-permissions` can allow unprompted writes. | Reported and advertised | Google codelab plus local help. It grants broad interaction authority; it is not path confinement or evidence that project-only effects are enforced. |
| The community Claude plugin has encountered changing headless write behavior and plain-text output constraints. | Reported by third-party prior art | [Antigravity for Claude Code](https://github.com/yuting0624/antigravity-for-claude-code), “Known limits.” This informs probes but is not provider authority. |

The proposal treats undocumented or unprobed behavior as unavailable or unknown. It does not
convert help text, model listings, or a community wrapper's experience into enforcement claims.

## 4. Scope

### In scope

- a Codex-side skill and stdlib-only manager for the official local `agy` executable;
- explicit Gemini Flash model selection, with the requested exact model recorded;
- deterministic task packets, run IDs, attempt directories, and sanitized status records;
- non-generative `doctor`, plus `run`, `status`, `inspect`, and `materialize` operations;
- optional `resume` only if a dated probe establishes observable conversation identity and stable
  same-task continuation;
- a source-only investigation profile and an isolated-worktree implementation profile, each
  unavailable until its required controls are probed;
- exact workspace, owned-path, command, network, installation, Git, and output declarations;
- manager-owned stdout, stderr, and `--log-file` capture;
- bounded manager state, worktree/scratch accounting, and provider-state observations;
- pre/post reconciliation and independent root validation; and
- fake-CLI fixtures and dated local-runtime probes.

### Non-goals

- automatic provider or model routing;
- using Antigravity to proxy Claude or OpenAI models;
- importing the community plugin as the canonical implementation;
- extracting or copying Google OAuth credentials;
- promising a remaining subscription-quota value that the runtime does not expose;
- network downloads, package installation, repository commits, pushes, or cleanup authority;
- recursive Antigravity subagents in the first release;
- background daemons, central telemetry, Dionysus integration, or remote monitoring;
- general Linux or Windows support in the first activation; or
- claiming that Antigravity and Claude permission names have equivalent semantics.

## 5. Architecture and package boundary

The provider-neutral C0 package owns:

- policy validation and normalization;
- semantic and authority identities;
- private binding records;
- directional transition comparison;
- sanitized policy explanation; and
- provider-independent resource and lifecycle vocabulary.

The Claude adapter continues to own Claude presets, assurance records, command compilation, stream
parsing, and Claude session behavior. The Antigravity adapter owns parallel provider-specific
presets, command compilation, text/log parsing, and conversation behavior. Neither adapter imports
the other's provider package.

```text
Codex task packet
       |
delegation_policy (pure C0)
       |
Antigravity compiler + capability record
       |
official agy process
       |
captured evidence + reconciliation
       |
root disposition
```

The first implementation may reuse small, proven utility modules for state accounting or Git
reconciliation only when their interfaces are provider-neutral in fact. Otherwise it should copy
the behavior with explicit lineage and defer extraction until both adapters demonstrate the same
semantics.

## 6. First-release profiles

### 6.1 `flash-investigation`

Purpose: source inspection, test-plan preparation, bounded review, and read-heavy evidence
collection without intended project mutation.

Requested policy:

- exact Gemini Flash model and thinking setting;
- project plus explicitly declared read roots;
- no owned project paths;
- no network, installation, Git mutation, external writes, or descendant agents;
- manager materialization for an optional result artifact; and
- a read-only or plan-like Antigravity control only after a probe demonstrates its actual effects.

If the runtime cannot prove a non-interactive source-only boundary, the profile remains unavailable.
The adapter must not relabel `plan`, `strict`, default prompts, or absence of skip-permission flags as
read-only without evidence.

### 6.2 `flash-implementation-worktree`

Purpose: bounded implementation in a dedicated Git worktree with explicit owned paths and root-run
validation.

Requested policy:

- exact Gemini Flash model and thinking setting;
- one dedicated worktree as the working directory;
- exact owned paths within that worktree;
- local tests and diagnostics declared in the task packet;
- no network, installation, commit, push, remote mutation, or external writes;
- no descendant agents in the first release;
- baseline and terminal Git/control-state fingerprints; and
- full-worktree reconciliation before root disposition.

Headless implementation may require `--dangerously-skip-permissions`. If so, the adapter records
that broad interactive authority and relies on worktree isolation, explicit task instructions,
host-side observation, and reconciliation. It must not describe that flag as path confinement.

`--sandbox` is not automatically combined with implementation. Google's documented
proceed-in-sandbox mode cannot modify the host workspace or access the local network. A capability
probe must establish whether the installed CLI can materialize intended worktree changes under any
sandboxed combination. Otherwise sandboxed work is a separate scratch-only profile or unavailable.

## 7. Command and lifecycle contract

The proposed user-facing manager surface is:

| Command | Contract |
|---|---|
| `doctor` | Check executable/version, authentication/model listing, advertised flags, workspace, state headroom, and non-generative capability records. |
| `run` | Validate a packet and profile, create one attempt, invoke `agy -p` with explicit model/workspace/log/timeout controls, and record terminal evidence. |
| `status` | Return sanitized lifecycle state without prompt, transcript, raw command, credential, or private path content. |
| `inspect` | Return additional safe provenance and, only when explicitly requested, the captured final result. |
| `materialize` | Write one successful final response to one exact manager-owned output path; refuse overwrite by default. |
| `resume` | Continue only the same semantic task, profile, model, workspace, and authority when an observable conversation ID and probe-backed behavior are available. |

The task packet includes objective, non-goals, read roots, owned paths, allowed commands, network
and installation policy, expected output, validation, escalation conditions, model, profile, and
timeout. The prompt is passed by stdin or a private prompt file rather than interpolated into a
shell command.

The adapter records planned, requested, and observed model separately. If the local stream or log
does not independently report model identity, observed model is `unknown`; the requested flag is
never copied into observed provenance.

## 8. Permission, filesystem, and host effects

An isolated worktree reduces merge conflicts and contains ordinary repository edits. It does not
confine processes, credentials, sockets, services, devices, application automation, or writes
outside the worktree. The implementation profile therefore reports filesystem enforcement and
host-effect assurance independently.

Before launch, the manager:

1. validates the worktree and ownership manifest;
2. rejects symlink aliases and ownership overlap;
3. fingerprints HEAD, index, Git control state, tracked dirty files, and relevant ignored paths;
4. records requested network, installation, Git, and host-effect denies; and
5. reserves manager log and worktree/scratch state headroom.

After launch, reconciliation classifies every observed change. Undeclared changes fail the attempt
but remain preserved for root inspection; reconciliation is detection, not rollback. The adapter
does not delete, reset, commit, or merge worker changes automatically.

## 9. Generated state and privacy

Adapter-managed generated state retains the existing 240 MiB configured maximum and 192 MiB
execution-stop/admission threshold. Accounting includes manager metadata, stdout/stderr, the
explicit `--log-file`, declared scratch roots, and worktree-generated files not present in the
baseline. Logs share a bounded byte budget and truncate with an explicit marker.

Antigravity may also write provider-owned global state outside the manager's state root. The
adapter must identify and measure relevant roots during a capability probe. Until redirection or a
stronger quota mechanism is established, it reports that provider-global accounting is sampled and
not quota-backed. It may not claim that the 240 MiB manager ceiling is a hard host-wide cap.

Run metadata excludes prompt text, transcript text, raw command text, tool output, credentials,
OAuth material, and private absolute paths from sanitized status and routing telemetry. Raw local
logs remain private evidence under the configured retention policy.

## 10. Error and recovery behavior

The adapter preserves stdout, stderr, logs, metadata, and any worktree changes for every attempt.
It distinguishes at least:

- missing or unsupported executable;
- unauthenticated or unavailable model;
- invalid packet or policy;
- permission prompt/block or soft-denied write;
- launch failure;
- timeout;
- interruption or orphaned process;
- generated-state threshold stop;
- non-zero provider exit;
- missing or ambiguous final result;
- observed-model conflict; and
- reconciliation failure.

No failure automatically launches a second paid call. Resume is offered only when the same-task
contract and conversation evidence remain valid. Otherwise the operator receives the preserved
evidence and chooses whether to start a fresh paid attempt.

## 11. Verification and activation gates

### Deterministic gates

- fake `agy` fixtures for help, model listing, success, structured absence, partial stdout, stderr,
  timeout, signal interruption, permission denial, model mismatch, and write/no-write outcomes;
- argument-order and prompt-transport tests;
- state-budget, log-truncation, symlink, worktree, dirty-tree, and reconciliation tests;
- status/result sanitization tests;
- proof that `doctor` never generates and fake tests make no network or paid calls; and
- complete existing Claude-adapter regression tests.

### Separately authorized runtime probes

1. authentication and model-list observation without generation;
2. minimal source-only run in a disposable fixture;
3. minimal write run in a disposable Git worktree;
4. permission-mode and sandbox matrix;
5. conversation-ID, resume, log, timeout, and observed-model evidence;
6. network, external-write, Git-control, process, and provider-global-state counterexamples; and
7. generated-state watchdog behavior under controlled growth.

Each probe records CLI version, platform, exact request, expected result, observed result,
artifacts, limitations, expiry, and re-check trigger. A passing fake test is not activation
evidence. A failed or ambiguous probe leaves that capability unavailable; it does not silently
degrade to broader authority.

## 12. Completion criteria

The minimal adapter is complete when a maintainer can:

1. install nothing and run deterministic tests against the fake CLI;
2. inspect exactly which authority and assurance the adapter would request;
3. invoke an explicitly approved Gemini Flash profile through the official CLI;
4. recover durable evidence from success, failure, timeout, or interruption;
5. reconcile all worktree changes against declared ownership;
6. materialize one accepted result without granting general artifact writes; and
7. use the adapter directly without the deferred general router.

Completion does not imply installation, route activation, automatic selection, or provider-term
approval beyond the official client boundary. Those remain separate decisions.
