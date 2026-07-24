# Proposal: composable Claude capability and scope policy

- **Date:** 2026-07-20
- **Revision:** 4
- **Status:** stakeholder-approved direction; Sol and Fable reviews dispositioned; corrected C0
  plan ready for a separate execution decision
- **Audience:** maintainers and reviewers of the Codex-managed Claude adapter
- **Closure target:** a corrected execution-policy contract and non-activating C0 plan from which
  later cohort plans and bounded runtime activation probes can be derived
- **Authority:** documentation only; no implementation, installation, deployment, commit, route
  change, profile activation, network download, or paid model call
- **Supersedes:** selected future-facing requirements of the
  [2026-07-19 capability-profile proposal](2026-07-19-capability-based-claude-execution-profiles.md);
  it does not rewrite that proposal's historical decisions, implementation record, or probe
  interpretation
- **Reviews:** [revision-2 Sol High cold review and root dispositions](../reviews/2026-07-20-composable-claude-capability-and-scope-policy-review.md),
  then the [revision-3 Fable correction audit](../reviews/2026-07-20-composable-claude-capability-and-scope-policy-fable-audit.md)
  and [root disposition](../reviews/2026-07-20-composable-claude-capability-and-scope-policy-fable-audit-disposition.md)
- **Correction evidence:** [revision-4 correction record](../reviews/2026-07-20-composable-claude-policy-revision-4-correction-record.md)

### Revision record

| Revision | Date | Disposition |
|---|---|---|
| 1 | 2026-07-20 | Root draft created as a partial supersession; no implementation or runtime authority granted. |
| 2 | 2026-07-20 | Stakeholder approved the proposal; independent review and finding disposition remain required before implementation planning. |
| 3 | 2026-07-20 | Dispositions all Sol findings, adds normative policy and sandbox contracts, preserves user-controlled profile transitions, and authorizes a draft contract-core plan but no execution. |
| 4 | 2026-07-20 | Dispositions the Fable correction audit; separates policy, authority, binding, presentation, and assurance identity; makes unresolved comparisons reachable; types resources, commands, and host effects; and corrects the C0 plan without authorizing execution. |

## 1. Approved direction and remaining gates

The stakeholder approved this composable policy direction for Codex-managed Claude runs:

1. stable named profiles remain as convenient presets;
2. profiles resolve into independent filesystem, command, network, MCP, Git, installation,
   descendant-agent, output, resource, host-effect, and lifecycle capabilities;
3. `project`, `scratch`, `output`, and caller-declared roots are symbolic scopes with independent
   read and write grants;
4. `mcp-readonly` is a generic capability backed by trusted, versioned server/tool records rather
   than a codebase-memory-specific public profile;
5. the adapter compiles the requested policy, reports the preflight assessment before a paid
   launch, and records the runtime-observed surface without treating exposure as authorization;
6. resuming under a different compiled policy is allowed under independently configurable profile,
   cache, authority, context, runtime, and sandbox notice/confirmation settings rather than
   rejected solely because a profile version changed;
7. host-wide reads are supported only as an advanced, explicitly configured policy and are never a
   standard-profile default;
8. runtime activation remains gated on deterministic tests plus dated, platform-specific probes.

Revision 4 retains revision 3's decision that warnings are informational controls, not
paternalistic prohibitions.
Profile, cache, authority, context, runtime, and sandbox notices are separate categories. An
operator may configure each as `always`, `once`, or `never`, and may configure confirmation
separately. Broader and mixed resumes remain available when the normalized policy otherwise permits
them.

The Sol and Fable reviews have been dispositioned. The corrected implementation plan covers only
the non-activating contract core. Executing it still requires a separate user decision; activation,
installation, and paid probes remain separately gated.

The intended post-read action is concrete: a maintainer should be able to decide whether to
authorize C0 execution without guessing how profiles compose, how paths are scoped, what
`mcp-readonly` promises, or how transition and presentation semantics interact.

## 2. Why a superseding proposal is required

The historical proposal was approved, implemented as an uninstalled candidate, corrected, and
used for a paid startup probe. Substantially rewriting it would obscure the contract against which
the candidate and probe were evaluated.

The probe then falsified one implementation assumption: Claude's startup event exposed all ten
connected codebase-memory tools even though only one was permission-allowed. The candidate treated
the other nine as broader authority and terminated before a model turn. The root correction made
unselected identifiers explicit denies, but subsequent stakeholder review exposed broader design
issues:

- exact per-tool selection is too narrow for the normal read-only MCP-review workflow;
- profile names should not encode every possible path and capability combination;
- project scope, external read roots, and external write roots need one coherent model;
- a profile-version mismatch is not by itself sufficient reason to prohibit resume;
- filesystem read-only access, subprocess network denial, and confidentiality are distinct;
- disk-state limits do not protect the host from memory or process exhaustion.

These are contract changes, not editorial corrections. This proposal therefore preserves the old
record and supplies a future-facing replacement for the affected sections.

## 3. Scope and non-goals

### In scope

- the policy vocabulary and precedence rules;
- standard profile presets and custom policy composition;
- filesystem root naming, read/write grants, and path conflict behavior;
- MCP trust, read-only semantics, and server-state boundaries;
- requested, effective, exposed, allowed, invoked, and observed runtime evidence;
- cross-profile resume, cache warnings, and authority-transition confirmation;
- inherited Claude configuration and runtime provenance;
- resource, generated-state, crash-recovery, and concurrency boundaries;
- deterministic and actual-runtime verification gates;
- macOS as the first activation target and Linux as the next portability target.

### Out of scope

- changing model routes or warrant grades;
- installing or activating the candidate;
- authorizing a paid retry of the incomplete runtime probe;
- building a second general-purpose operating-system sandbox;
- Windows activation in the first release;
- automated network updates, package installation, commits, pushes, or cleanup jobs;
- inferring that an MCP server is safe from its name or self-reported annotations alone.

## 4. Evidence map and epistemic status

| Claim | Status | Evidence and limitation |
|---|---|---|
| The candidate exposes five named profiles, a compatibility alias, exact pinned codebase-memory query identifiers, native-sandbox settings, path-scoped scratch/output/ownership arguments, and a hard profile-version resume check. | Observed | Candidate modules and deterministic tests inspected 2026-07-20. The candidate is uninstalled and uncommitted; fake-CLI tests do not establish Claude runtime enforcement. |
| Claude Code `2.1.215` exposed ten connected codebase-memory tools in the init event while the packet permission-allowed one. | Observed | [P-20260720 runtime probe](../../probes/records/P-20260720-claude-profile-actual-runtime.md), “Observed facts” and “Root-cause disposition.” The run terminated before a model turn, so tool callability and sandbox effects remain unknown. |
| Claude distinguishes tool availability, permission rules, and permission modes; `dontAsk` denies calls that would otherwise prompt. | Reported | Anthropic [CLI reference](https://code.claude.com/docs/en/cli-usage), [permissions](https://code.claude.com/docs/en/permissions), and [permission modes](https://code.claude.com/docs/en/permission-modes). Provider documentation does not prove the candidate composed these controls correctly. |
| Claude's native Bash sandbox defaults to broad host reads and working-directory writes, supports additional read/write/deny paths, and is complementary to tool permissions. | Reported | Anthropic [sandbox documentation](https://code.claude.com/docs/en/sandboxing). The sandbox applies to Bash and child processes; built-in file tools and MCP need their own authority controls. |
| Some sandbox path arrays merge across settings scopes instead of replacing earlier arrays. | Reported | Anthropic [sandbox documentation](https://code.claude.com/docs/en/sandboxing), “Granting subprocess write access to specific paths.” Effective managed settings may remain outside adapter control. |
| MCP defines `readOnlyHint`, `destructiveHint`, `idempotentHint`, and `openWorldHint`, but explicitly treats them as untrusted hints. | Reported | MCP [schema reference](https://modelcontextprotocol.io/specification/2025-11-25/schema), `ToolAnnotations`. A reviewed registry or stronger provenance remains necessary. |
| Changing tool definitions invalidates the tool, system, and message cache prefixes; other policy changes may have narrower or no cache effects. | Reported | Anthropic [tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching), “What invalidates your cache.” Claude Code's exact cache keys remain provider-controlled. |
| Host-wide file reads can disclose sensitive content through the model request even when subprocess network access is denied. | Inference | Claude's model connection is necessary for the delegated run, while sandbox network rules govern Bash and child processes. Therefore filesystem confidentiality cannot be reduced to subprocess egress control. Exact provider handling remains governed by the user's provider agreement and runtime configuration. |
| The generated-state ceiling does not prevent memory, process, or CPU exhaustion. | Inference | The existing ceiling accounts for files and logs. It does not measure or constrain resident memory, process count, or CPU time. Platform-specific enforcement remains to be designed and probed. |

Memory, prior chat, and the earlier implementation findings are treated as discovery aids. The
load-bearing local claims above are anchored to the candidate, historical proposal, or probe
record; provider behavior is labeled reported until an actual-runtime probe observes it.

## 5. Supersession and lineage

The historical proposal remains authoritative for why named profiles were introduced, why the
native Claude sandbox was selected for Bash, why output materialization and worktree reconciliation
exist, and what the first probe observed. This proposal changes future behavior as follows:

| Historical area | Disposition for future work |
|---|---|
| §4 profile principles | Retain profiles as contracts, but define them as presets compiled from orthogonal capabilities and scopes. |
| §5 canonical profiles | Retain the user-facing profile names provisionally; replace duplicated per-profile authority prose with preset manifests over one policy schema. |
| §6 precedence | Retain hard prohibitions and deterministic conflict errors; add an explicit, auditable confirmation path for authorized broadening and cross-profile resume. |
| §7 MCP manifest | Replace the codebase-memory-specific public abstraction with generic `mcp-readonly`; retain server-specific verified registry entries internally. |
| §8 roots and artifacts | Replace scratch/output special cases with named roots and operation-specific path grants while retaining manager materialization as the safest artifact default. |
| §8.1 generated state | Retain the 240 MiB configured maximum and 192 MiB admission threshold as explicit standard-preset values; add non-disk resource governance rather than treating disk accounting as host protection. |
| §9 resume | Replace the categorical fresh-session rule and version-only rejection with a compiled-policy transition diff, operator-configured notices/confirmation, and a recorded recommendation. |
| §10 records | Expand the record to include policy provenance, transition evidence, runtime trust, resource disposition, and staged tool states. |
| §§11–12 implementation and verification | Supersede with the sequence and gates in this proposal. Preserve completed historical test/probe claims as historical evidence only. |
| §§13–14 alternatives and decisions | Supersede where they reject all capability-expanding resumes or assume exact-tool MCP selection as the standard review interface. |
| §15 authorization | Retain unchanged: no implementation, activation, installation, deployment, or paid call follows from proposal drafting. |

The [historical corrective implementation plan](../superpowers/plans/2026-07-19-capability-based-claude-profiles-corrective.md)
remains an execution record for the version-3 candidate. The
[revision-2 C0 implementation plan](../superpowers/plans/2026-07-20-composable-claude-policy-contract-core.md)
is the bounded successor for the non-activating contract core; later cohorts require separate
plans and activation decisions.

## 6. Architectural model

### 6.1 Policy compilation

The adapter resolves each invocation through a deterministic pipeline:

```text
operator hard boundaries
  + profile preset
  + task-packet capabilities and scopes
  + explicit invocation grants
  + trusted runtime/server registry
  -> normalized requested policy
  -> inherited-source and runtime preflight
  -> compiled policy
  -> preflight-assessed policy and transition diff
  -> operator confirmation when required
  -> Claude settings and arguments
  -> runtime-observed evidence and effective conclusion
  -> post-run reconciliation and disposition
```

The compiled normalized policy—not a profile name or one settings file—is the requested contract.
It receives two identities:

- `semantic_sha256` covers the normalized, provider-neutral requested contract, including
  operator-owned presentation preferences, but excludes private resolved paths and runtime
  observations;
- `authority_sha256` covers only the normalized requested authority projection: grants, denies,
  limits, fallbacks, and content-addressed capability definitions over symbolic scopes.

Private path bindings and their run-lineage-scoped identities remain in a separate binding record.
Changing a presentation preference may change `semantic_sha256` without changing
`authority_sha256`; changing a root binding may trigger `context_change` without exporting or
globally fingerprinting the path. `Effective` is reserved for a conclusion supported by
runtime-observed evidence; preflight prediction alone is never labeled effective.

### 6.2 Profiles, capabilities, and scopes

- A **profile** is a stable preset for a common workflow such as strict review, executable review,
  artifact-producing review, or implementation.
- A **capability** is one independent kind of authority: filesystem read, filesystem write, local
  command execution, network access, MCP access, Git mutation, installation, descendant agents,
  output materialization, or selected host effects such as process signaling/debugging, Unix-socket
  access, service/device control, and application automation.
- A **scope** names where a capability applies. Built-in symbolic scopes are `project`, `scratch`,
  `output`, and `state`; callers may declare additional named roots.
- A **grant** binds operations to scopes. Read and write are always separate.
- A **hard boundary** cannot be overridden by a project, task packet, profile, or last CLI flag.

This separation keeps the common path concise without preventing custom contracts.

## 7. Filesystem scope contract

### 7.1 Declarative form

The canonical schema should be able to express:

```yaml
filesystem:
  defaults:
    read: deny
    write: deny

  roots:
    project: {kind: project, binding: ${workspace}}
    output: {kind: output, binding: ${artifact_directory}}
    shared_docs: {kind: external, binding: /absolute/path/to/shared-docs}

  rules:
    - operations: [read, write]
      scope: project
      effect: allow
    - operations: [read, write]
      scope: output
      effect: allow
    - operations: [read]
      scope: shared_docs
      effect: allow
    - operations: [read, write]
      rule_id: protect-credentials
      path: ~/.ssh
      effect: hard-deny
```

The requested form may contain private bindings. Normalization moves each binding into a private
record and leaves only the root ID, kind, and bound/unbound state in the canonical document. Allow
rules must reference declared root IDs through `scope`; raw `path` selectors are deny-only and need
a stable `rule_id`. A private selector rebinding is a context change and makes the authority
relation unresolved when its narrowing effect cannot be ordered safely.

This example does not grant host-wide reads. An advanced custom policy may instead set the read
default to allow and then declare sensitive hard denies. Preflight always creates a confidentiality
notice event explaining that any readable content may become model input; display and confirmation
follow the operator's settings. `network: deny` does not make host-wide reads confidential.

### 7.2 Rule precedence

Rules are resolved independently for each operation:

1. operator or managed hard denies;
2. the most-specific matching path rule;
3. deny over allow at equal specificity;
4. the operation default.

Profiles may be narrowed without confirmation. A run-level grant that broadens the preset is valid
only when the governing profile marks that dimension extensible and the operator explicitly
requested or configured the grant; notice and confirmation behavior follow operator settings.
Raw last-flag-wins behavior is prohibited.

### 7.3 Path normalization and escape resistance

Before launch, the adapter must:

- bind symbolic roots to absolute paths and record their provenance;
- derive run-lineage-scoped binding identities for context comparison without exporting raw paths
  or stable global path fingerprints;
- normalize case and canonicalize existing ancestors using platform-appropriate semantics;
- reject `..` traversal, symlink leaves, and symlink ancestors for writable roots;
- validate the nearest existing ancestor for a not-yet-created output path;
- identify overlapping read, write, deny, scratch, state, and artifact roots;
- account for mount points and hard-linked files in the threat model and tests;
- validate ownership and private permissions for manager-owned state and scratch roots;
- render the resolved paths before a paid launch without exporting them to cross-project telemetry.

An abstract allow must be enforced twice where applicable: Claude tool permissions govern Read,
Edit, and Write; the native sandbox governs Bash and child processes. A boundary that cannot be
mapped and observed on the installed runtime fails closed for a strict profile.

For policy purposes, `write` includes create, overwrite, truncate, delete, rename, link, chmod,
xattr, and directory-entry mutation. Execution, network access, Git control-state mutation,
installation, and process signaling remain separate dimensions even when they can cause writes.

Path evaluation is race-aware rather than preflight-only. Manager materialization reopens parents
without following symlinks where the platform supports it, revalidates the destination immediately
before mutation, writes atomically, and performs post-run reconciliation. Ambiguous writable mount
or hard-link aliases are rejected or labeled detection-only; they are never silently promoted to
hard enforcement.

### 7.4 Internal enforcement matrix

Users select profiles and named roots; they do not configure every tool. The adapter and its tests
maintain the cross-product of profile × operation/tool family:

| Operation/tool family | `strict-readonly` | `verified-review` / `artifact-review` | implementation profiles |
|---|---|---|---|
| Built-in Read/Grep/Glob | Claude-enforced project and declared roots; documented best-effort propagation | same | same |
| Built-in Edit/Write | denied as whole tools | denied as whole tools | Claude-enforced grants plus reconciliation |
| Bash filesystem | Bash unavailable | native OS sandbox; scratch writable | native OS sandbox; declared project/worktree and scratch writes |
| MCP | denied or reviewed local read-only bundle | reviewed local read-only bundle | separately declared reviewed bundle |
| Artifact materialization | manager only | manager only by default | manager or separately declared worker root |
| Undeclared mutation | no worker mutation expected | sandbox boundary plus reconciliation | reconciliation detects and fails; it is not rollback |

Every cell carries one assurance label: `os-enforced`, `claude-enforced`, `manager-controlled`,
`detected`, or `unknown`. `explain` shows the labels without asking the user to author the matrix.
Standard profiles do not claim a hard host-confidentiality boundary from Claude's best-effort
built-in read propagation. A later high-isolation cohort may stage sources or expose only sandboxed
read commands when that stronger boundary is required.

### 7.5 Standard preset defaults

| Preset | Read roots | Worker write roots |
|---|---|---|
| `strict-readonly` | `project` plus declared external sources | none |
| `verified-review` | `project` plus declared external sources | run-scoped `scratch` only |
| `artifact-review` | same as verified review | `scratch`; manager materializes `output` by default |
| `implementation` | `project` plus declared external sources | declared owned project paths plus `scratch` |
| `implementation-auto` | same as implementation | same as implementation |

Host-wide reads are not part of any standard preset. They are an advanced, explicitly configured
custom option with independently configurable confidentiality notice and confirmation behavior.

## 8. MCP capability contract

### 8.1 User-facing modes

The MCP policy is generic:

```yaml
mcp:
  mode: deny | readonly | selected | unrestricted
  servers: [declared_server_names]
  selected_tools: [exact_identifiers]
```

`readonly` means every admitted tool must have a trusted registry record compatible with the
compiled filesystem, network, and state policy, then remain subject to runtime observation. It
does not mean “allow any tool whose name sounds like a query” or “trust `readOnlyHint: true` from
any server.”

The normal codebase-memory review flow enables the whole reviewed read-only query bundle. Exact
per-tool selection remains available as a stricter custom mode, not the default user experience.

### 8.2 Trusted registry records

Each admitted server/tool record includes at least:

- canonical server and tool identifiers;
- executable or transport provenance and content/configuration hashes where available;
- reviewed mutation semantics;
- open-world/network behavior;
- allowed internal cache, index, log, and database roots;
- startup and shutdown side effects;
- credential/environment requirements without copying secrets;
- compatibility version and last probe date;
- evidence grade and invalidation trigger.

An MCP query may be read-only with respect to the project while maintaining a bounded internal
index. That internal state is allowed only under declared, accounted roots. Undeclared project,
host, remote, or external-state mutation is incompatible with `mcp-readonly`.

### 8.3 Tool-state evidence

The lifecycle record distinguishes:

```text
configured -> exposed -> permission-allowed -> attempted -> succeeded
```

These states are not interchangeable. Startup exposure may establish configuration reachability;
it does not establish permission, successful invocation, or non-mutation. Strict profiles fail on
unknown or unauthorized callable authority, not merely because an explicitly denied identifier is
visible in an init manifest.

The server process itself may have startup effects before a tool call. A server is therefore not
admitted to a strict profile until its process boundary is trusted or constrained consistently
with the policy.

## 9. Commands, network, and resources

### 9.1 Command capability

Executable review and implementation use bounded command capabilities rather than treating Bash
as generally safe. The first implementation may support:

- normalized argument-vector templates for known test, lint, type-check, query-plan, and diagnostic
  commands;
- a sandboxed-command capability for explicitly authorized broader local investigation;
- manager-executed deterministic diagnostics whose results are supplied to the reviewer.

Shell composition, command substitution, redirection, and environment mutation require explicit
policy treatment. Command-string matching is authorization logic, not the filesystem or network
security boundary.

Tests execute repository code. A review profile that runs tests therefore has a materially
different risk boundary from a source-only review even when it cannot edit the checkout.

Each admitted command template normatively declares:

- an argument vector or exact provider command form;
- working-directory scope;
- allowed environment keys and fixed values;
- stdin mode;
- wall-time limit;
- expected write roots;
- stdout/stderr and per-file limits;
- network disposition;
- sandbox disposition (`required`, `preferred`, or `outside`);
- evidence and invalidation trigger.

Schema version 1 uses this normalized element shape:

```yaml
id: adapter-tests
revision: 1
argv: [python3, -m, unittest]
cwd_scope: project
environment:
  fixed: {PYTHONDONTWRITEBYTECODE: "1"}
  pass: []
stdin: closed
write_scopes: [scratch]
wall_time_seconds: 180
shared_log_bytes: 16777216
per_file_bytes: 8388608
network: {mode: deny, destinations: []}
sandbox: required
evidence_id: runner-adapter-tests-v1
```

The authority projection content-addresses `argv`, working scope, environment, stdin, write scopes,
limits, network, and sandbox disposition; changing any of those fields changes the template's
authority atom even when `id` and `revision` were not updated. `evidence_id` and presentation text
remain provenance rather than authority.

If a runner requires undeclared project-local caches, locks, sockets, databases, or build outputs,
`explain` reports it as incompatible before a paid call. Redirecting those outputs to scratch or
granting one narrow root is preferred to disabling the sandbox.

### 9.2 Network capability

Network policy is orthogonal to filesystem and MCP policy:

```yaml
network:
  subprocess: deny | allowlist | unrestricted
  mcp_open_world: deny | allowlist | unrestricted
  allowed_destinations: []
```

Provider/model traffic required for the Claude session is recorded as part of the runtime, not
misrepresented as denied. No standard profile implies package download, WebFetch, WebSearch, Git
push, remote API mutation, or arbitrary MCP open-world access.

### 9.3 Host resource governance

The existing generated-state controls remain necessary but insufficient. The replacement plan
must add a platform-probed resource contract covering:

- aggregate concurrent delegated runs;
- per-run process and descendant-process count;
- resident-memory observation and enforceable limits where the platform supports them;
- CPU or wall-clock duration;
- shared stdout/stderr and per-file output bounds;
- generated-state admission and in-run growth;
- process-group termination and orphan detection;
- clear `unknown` status when the operating system cannot establish a claimed hard limit.

The design must distinguish sampled guardrails from hard resource enforcement. A watchdog is not a
quota, and an unsupported or advisory memory limit must not be reported as a proven ceiling.

Each requested limit uses one explicit form:

```yaml
{mode: unavailable, value: null}  # no activatable claim yet
{mode: bounded, value: 251658240} # finite requested maximum
{mode: unbounded, value: null}    # intentional absence of a maximum
```

Omission normalizes to `unavailable`, never `unbounded`. A bounded value must be a positive integer;
`unavailable` and `unbounded` require `null`. Enforcement evidence is separate and reports
`enforced`, `sampled`, or `unknown`; it does not change requested authority. Standard C0 presets
retain a bounded generated-state maximum of 240 MiB and a separate 192 MiB admission threshold.

Minimums are cohort-specific. Every command-capable cohort requires aggregate admission, process-
group ownership, wall time, shared log/output bounds, generated-state accounting, and bounded
termination. Unattended implementation additionally requires a durable attempt journal,
PID-plus-start-time validation, orphan detection, and idempotent next-start recovery. Memory may be
sampled on macOS when no reliable hard ceiling is available, but the profile must say so.

### 9.4 Native sandbox construction

The adapter uses Claude Code's native sandbox rather than implementing a second general-purpose OS
sandbox. Standard command-capable presets compile to the equivalent of:

```yaml
sandbox:
  enabled: true
  availability: required
  unsandboxed_retry: deny
  filesystem:
    read: [project, scratch, declared_external_reads]
    write: [scratch, declared_profile_write_roots]
    deny_write: [git_control_state, protected_roots]
  network:
    mode: deny
```

The adapter maps that provider-neutral shape to version-probed Claude settings such as
`failIfUnavailable`, `allowUnsandboxedCommands`, `allowRead`, `allowWrite`, `denyRead`, and
`denyWrite`. It launches executable reviews from scratch and attaches the project as a read root.
Implementation runs use the project or an isolated worktree only when the compiled write contract
permits that whole working-directory boundary; owned-path reconciliation must not be presented as
OS enforcement.

Sandbox policy is user-controlled. A custom policy may choose `fail`, `warn-and-run`, or `run` when
the sandbox is unavailable, and may allow exact unsandboxed exceptions. Named profiles default to
no silent fallback, but the operator can change fallback, warning, and confirmation settings. Any
resulting authority change appears in the compiled policy and audit record.

### 9.5 Sandbox pitfalls and mitigations

| Failure mode | Consequence | Mitigation and user control |
|---|---|---|
| Sandbox dependencies or platform support are absent | Claude may otherwise run Bash unsandboxed | Probe before paid launch; named profiles default to `fail`; custom policy may select `warn-and-run` or `run`. |
| Claude retries with `dangerouslyDisableSandbox` | One command escapes the OS boundary | Disable automatic retry by default; permit exact per-command exceptions; warn or confirm according to operator settings. |
| Inherited `excludedCommands` or path arrays merge | Project/user settings silently widen authority | Suppress unneeded settings sources, enumerate unresolved managed sources, classify broader or unknown preflight, and record runtime observation. |
| Working directory is writable by default | A review or owned-path task can change more than intended | Launch reviews from scratch; use an isolated worktree or explicitly accept whole-project sandbox writes for implementation; reconcile afterward. |
| Linked worktree exposes shared Git control state | Worker can affect another checkout or repository metadata | Resolve all Git control paths, deny them in the sandbox, fingerprint HEAD/index/control state, and test linked-worktree cases. |
| Unix socket access, especially Docker | Socket grants host-level or service-level authority | Deny sockets by default; treat every allowed socket as a separate capability; expose Docker as explicit unsandboxed/host authority. |
| Apple Events, `open`, or `osascript` | Sandboxed code can control unsandboxed applications | Keep Apple Events off in standard profiles; require a visible host-automation capability and record macOS TCC dependence. |
| Broad network domains or proxy limitations | Data exfiltration or domain-fronting paths | Default deny; use narrow destinations; label host filtering limitations; require an inspecting proxy for stronger claims. |
| Host credentials remain readable | Repository code or model context can disclose secrets | Standard read roots are project plus declarations; scrub environment; deny credential roots; make host-wide read advanced and explicitly described. |
| Symlink, mount, hard-link, or TOCTOU alias | Path-scoped grants affect another target; a scratch hard link can make manager materialization copy an undeclared inode | Canonicalize and check aliases, reject ambiguous writable roots, validate device/inode/link count during materialization, use race-resistant manager writes, revalidate, and reconcile. |
| MCP server starts outside the Bash boundary | Server startup can read, write, spawn, or use network | Treat process containment as unknown until probed; admit only reviewed local bundles with declared state; keep remote MCP unavailable initially. |
| Sandboxed code can signal or debug unrelated host processes | Availability or confidentiality impact outside filesystem policy | Default the host-effect capability to deny/unavailable; probe process signaling and debugging separately before admitting either operation. |
| Sandbox lacks memory/CPU/process quotas | Tests can freeze the host despite filesystem isolation | Apply separate admission, time, output, process, and sampled memory controls; serialize risky cohorts until resource recovery is proven. |
| Manager crashes while descendants run | Orphan processes and ambiguous paid/runtime state | Use process groups, durable journals, leases, PID/start-time checks, and next-start recovery before unattended activation. |
| Sandbox changes test behavior | False product failures from blocked caches, sockets, watch services, network, or tools that ignore redirected temporary/cache variables | Declare runner needs, redirect state to scratch, probe whether each supported runner honors the redirect, provide compatible flags such as disabling watchers, and report sandbox-caused incompatibility separately. |

### 9.6 Running outside the sandbox

Unsandboxed execution is a first-class, explicit exception—not a hidden fallback. Legitimate cases
include Docker daemon access, Apple Events or browser-based authentication, host service control,
privileged package/system operations, host-process debugging, device access, WSL host-binary
interop, and specific tools proven incompatible with the native sandbox.

Before an unsandboxed command, the adapter renders the exact command template, why isolation is
incompatible, inherited filesystem/network/credential authority, and likely side effects. The
operator may configure its notice as `always`, `once`, or `never` and its confirmation as `ask` or
`never`. Exceptions are scoped to the exact command template where possible; disabling the sandbox
for an entire session is supported only as an explicit custom policy. Manager hashing,
reconciliation, and atomic artifact materialization are trusted control-plane operations outside
the worker sandbox and are not exposed as arbitrary worker commands.

## 10. Configuration provenance and preflight

The adapter must not assume that an invocation-local settings file replaces user, project, local,
plugin, hook, MCP, or managed configuration. Before launch it computes:

1. requested policy;
2. selected configuration sources;
3. inherited sources that remain active;
4. compiled Claude settings and CLI arguments;
5. managed or runtime-controlled settings it cannot suppress;
6. expected tool and server exposure;
7. preflight assessment: `exact`, `narrower`, `broader`, or `unknown` relative to the compiled
   policy.

Strict modes select only required settings and MCP sources where the installed CLI supports that
control. Unrequested hooks, plugins, agents, auto-memory, development channels, and project-local
runtime extensions are disabled or treated as unresolved authority. Project instructions needed
for the task are declared and hashed separately from executable configuration.

A dry-run command such as the following is a required product surface:

```bash
delegate-to-claude explain \
  --profile verified-review \
  --workspace /path/to/project \
  --output-dir /path/to/review-artifacts
```

It performs no model call and reports the compiled and preflight-assessed policy:

- policy schema, preset revision, and separately labeled legacy contract version;
- resolved read, write, scratch, state, and output roots;
- commands and network destinations;
- MCP servers and admitted tool bundles;
- configuration sources and unresolved managed controls;
- resource limits and whether each is enforced, sampled, or unknown;
- whether confirmation is required;
- for resume, the transition and likely cache impact.

Secrets, prompt bodies, tool output, and raw settings payloads are excluded from the display and
cross-project telemetry.

## 11. Resume and cache contract

### 11.1 Compatibility by semantic diff

Preflight resume compatibility is determined from normalized compiled policies, objectives,
workspace and source identities, model/effort choices, and runtime provenance. Runtime-observed
evidence may later support an effective-policy conclusion. A profile version mismatch is an input
to the comparison, not an automatic rejection.

Each transition is classified:

- `exact`: no authority change;
- `narrower`: authority only removed;
- `broader`: authority only added;
- `mixed`: some authority removed and other authority added;
- `unknown`: the adapter cannot compute the preflight transition.

The report also carries `known_kind` and `unresolved_dimensions`. Known broadening is never hidden
because another dimension is unresolved. Grant and deny relations are directional: adding a grant
or removing a deny broadens; removing a grant or adding a deny narrows. Content-bearing command
templates and resolved MCP registry records are compared by their authority hashes, not names
alone. `unavailable` is activation/runtime state rather than an authority rank; a transition that
depends on an unavailable bundle remains unresolved until the bundle is resolved.

Finite resource-limit increases broaden and decreases narrow; bounded-to-unbounded broadens.
Enforcement assurance (`enforced`, `sampled`, `unknown`) is runtime evidence and triggers runtime
analysis rather than masquerading as requested authority. Rebinding a private root triggers
`context_change`; if the changed binding affects an unorderable deny selector, authority is also
unresolved.

### 11.2 Confirmation

Resume produces independent notice categories:

- `profile_transition`: profile ID or version changed;
- `cache_impact`: model-facing tools, system inputs, model, effort, or other cache-relevant inputs
  changed;
- `authority_change`: capabilities or scopes narrowed, broadened, mixed, or unresolved;
- `context_change`: objective, workspace, source identity, or trust context changed;
- `runtime_change`: Claude/runtime or enforcement capability changed;
- `sandbox_change`: sandbox availability, fallback, or unsandboxed exception changed.

Each notice is configurable as `always`, `once`, or `never`. `once` means once per
`(category, transition_sha256)` within a run lineage; the private run record owns that presentation
state when display activates in a later cohort. Confirmation is configured separately as `ask` or
`never`; it may be disabled and has no stateful `once` mode.

Presentation settings resolve only from operator-owned current configuration, an explicit operator
invocation, or trusted managed policy. Untrusted repository configuration cannot change their
visibility. The current operator choice governs the current transition, including a change to the
presentation settings themselves; the adapter does not force a final warning after the operator
selects `never`. Regardless of display choices, preference changes, transition facts, unresolved
dimensions, and policy hashes remain in the private audit record.

Broader and mixed resumes are permitted when the normalized policy permits them. Interactive and
unattended modes use the same policy; unattended runs simply cannot depend on an interactive
prompt. A fresh session may be recommended when prior untrusted content gains new effect authority,
but the adapter does not substitute or require one solely for that reason. Invalid policies and
operator hard prohibitions remain errors.

### 11.3 Cache claims

The adapter may report provider-observed cache creation/read counters and a conservative
`unchanged`, `likely invalidated`, or `unknown` expectation. It never promises a cache hit or
launches a paid call solely to warm a cache. Authority decisions are not hidden behind cache
economics.

## 12. Records, privacy, and recovery

Each run and attempt records enough bounded evidence to reconstruct the decision:

- requested profile, capabilities, scopes, `semantic_sha256`, and `authority_sha256`;
- private root-binding identities and rebinding events, without exporting raw paths;
- effective policy and configuration-source provenance;
- exposed, allowed, denied, attempted, and successful tools;
- MCP server provenance and state-root disposition;
- resource contract and observed termination reason;
- known and final transition classifications, unresolved dimensions, presentation decisions,
  confirmation mechanism, and resume lineage;
- observed cache counters when supplied by the provider;
- baseline and final worktree classification for implementation profiles;
- materializable attempts and artifact hashes;
- unresolved enforcement claims and activation-probe identifiers.

Prompt text, transcript text, command text, tool output, secrets, credentials, raw hook payloads,
and artifact contents remain out of cross-project telemetry. Private run state may retain the
minimum content needed for explicit inspection and recovery under the governing retention policy.

Cross-project telemetry uses an explicit field allowlist. Raw paths, artifact hashes, executable
hashes, configuration hashes, and globally stable project fingerprints are excluded unless a
separate privacy review establishes a need. When correlation is required, use domain-separated,
keyed pseudonyms with bounded rotation. Telemetry export remains disabled until the schema and
deletion behavior are tested. The existing 30-day Codex session-log policy is not silently applied
to adapter run state; adapter retention, access, inspection, and deletion require an explicit
contract in the implementation plan.

On interruption, crash, or resource termination, the manager preserves bounded partial evidence,
marks the attempt non-materializable unless its success contract was already satisfied, and
reconciles surviving child processes and filesystem changes without reverting user work. Recovery
never silently launches another paid call.

## 13. Error handling

Failures before launch are preferred to paid ambiguous runs. Preflight errors identify:

- the conflicting field and source;
- the compiled versus preflight-assessed authority;
- whether the issue can be narrowed automatically;
- the smallest safe operator action;
- whether continuing would require a paid call, a profile transition, or new authority.

Unknown enforcement under strict profiles fails closed. A permissive custom profile may declare
the unresolved boundary acceptable and continue; the event remains in the private audit record,
while its notice and confirmation behavior follow operator settings.

An unexpected runtime surface terminates the attempt, preserves the evidence, and does not treat a
later result event as successful. Termination itself is recorded as process behavior, not evidence
that every intended filesystem, network, MCP, or resource boundary worked.

## 14. Verification and activation

### 14.1 Deterministic verification

The replacement plan must cover at least:

- policy-schema normalization, version dispatch, semantic/authority hashing, private-binding
  detachment, provenance, and readable rendering;
- profile preset equivalence and deprecated alias behavior;
- narrowing, broadening, mixed, and unresolved transitions; directional grant/deny comparison;
  operator-controlled confirmation; and unattended transition acknowledgement;
- stable resume across a policy-schema upgrade with no semantic change, beginning with the first
  real schema migration rather than a fictitious version-1 self-migration;
- generic MCP read-only bundles, exact selected tools, unknown tools, mutating tools, startup
  effects, and internal-state roots;
- exposed-versus-allowed manifest fixtures based on the actual 2026-07-20 init shape;
- inherited settings, merged arrays, hooks, plugins, MCP sources, and managed unknowns;
- project, external read-only, external writable, scratch, output, and host-read policies;
- traversal, symlink, case, mount, hard-link, overlap, ownership, and permission counterexamples;
- built-in file tools and Bash subprocess enforcement as separate layers;
- command-template content addressing, composition, network, installation, Git, descendant-agent,
  and host-effect denials;
- memory, process, duration, log, file, and aggregate-state termination behavior;
- dirty-worktree and ignored-path reconciliation without rollback;
- crash recovery, partial output, and orphan-process disposition;
- content-free telemetry and bounded private-state records.

Tests using a fake Claude CLI prove adapter behavior only.

### 14.2 Actual-runtime probes

Activation requires separately authorized, minimal probes that record:

- Claude Code version and platform;
- selected and inherited configuration sources;
- requested and observed tools, servers, permission mode, and sandbox status;
- allowed and denied filesystem effects;
- subprocess and MCP network behavior;
- permitted MCP query and denied mutating call behavior;
- MCP startup/internal-state effects;
- resource-limit behavior without intentionally threatening host stability;
- process-signaling/debugging denial, runner scratch/cache redirection, and hard-link materialization
  counterexamples where the cohort exposes those surfaces;
- resume behavior and provider-reported cache counters;
- generated-state total and retained private evidence.

Probe conclusions are scoped to the tested version, platform, profile, and action. macOS is the
first activation target. Linux receives a separate capability matrix; Windows remains deferred.

### 14.3 Review gate

The revision-2 Sol review and revision-3 Fable correction audit are complete and dispositioned.
The Fable audit challenged the proposal and plan for:

- contract completeness and internal consistency;
- privilege and confidentiality boundaries;
- usability for strict review, executable review, artifact review, interactive implementation,
  and unattended implementation;
- portability and runtime observability;
- unnecessary complexity and dependencies;
- which requirements are first-release blockers versus later improvements.

The root disposition records `accept`, `revise`, `park`, or `reject` for each finding. Revision 4
implements the accepted correction boundary, and a separate correction record binds the final
proposal and plan hashes to that disposition. No additional paid audit is required for faithful
corrections within this boundary; material changes need a new review decision.

## 15. Implementation and activation cohorts

Each cohort receives its own implementation plan, review, and activation decision:

1. **C0 — contract core:** pure schema, version dispatch, normalizer, precedence, semantic and
   authority identities, private-binding records, directional/unknown diff, notice/confirmation
   settings, typed command and host-effect contracts, profile presets, migration fixtures, and
   non-generative `explain`. It changes no deployed profile and performs no paid call.
2. **C1 — source-only review:** Claude built-in read scoping, strict write/tool denies,
   configuration-source assessment, and source-review runtime probes.
3. **C2 — manager-materialized artifact review:** single-output atomic materialization and
   recovery, initially without worker direct-write authority.
4. **C3 — executable review:** native sandbox compilation, command templates, scratch writes,
   resource controls, host-effect denial probes, and supported-runner fixtures.
5. **C4 — interactive implementation:** project/worktree writes, Git-control protection,
   ownership reconciliation, and explicit unsandboxed exceptions.
6. **C5 — unattended implementation:** auto mode, durable recovery, orphan handling, and concurrency
   governance.
7. **C6 — advanced policies:** host-wide reads, remote/third-party MCP, direct worker artifacts,
   controlled network/credentials, Linux activation, and stronger container/VM isolation.

Only C0 is covered by the corrected revision-2 implementation plan. Later cohorts may reuse the core
but may not claim activation from C0 tests. Every cohort is test-first, preserves unrelated dirty
work, and keeps actual-runtime evidence separate from fake-CLI claims.

## 16. Alternatives

| Alternative | Disposition | Reason |
|---|---|---|
| Continue adding fixed profiles for every scope combination | Reject | Produces profile explosion and couples task names to path and tool authority. |
| Expose raw Claude settings as the public configuration | Reject | Provider settings do not form a stable, auditable cross-runtime contract and may merge with inherited sources. |
| Trust MCP `readOnlyHint` automatically | Reject | The MCP specification labels annotations as untrusted hints. |
| Keep exact MCP tool selection as the normal review interface | Reject | Safe but unnecessarily granular for a reviewed read-only bundle; retain it as a strict option. |
| Treat all exposed init tools as authorized | Reject | Contradicted by the first actual-runtime startup observation. |
| Prohibit every cross-profile resume | Reject | Conflates authority, lineage, and cache cost; an explicit semantic transition is more informative. |
| Silently permit every cross-profile resume without an operator warning policy | Reject | Can add consequential authority to a context containing untrusted content without a recorded operator choice; an operator may intentionally set notices and confirmations to `never`. |
| Make host-wide reads a standard review default | Reject | Unnecessary confidentiality exposure; declared roots satisfy the ordinary workflow. |
| Prohibit host-wide reads in all custom configurations | Reject | Strong confidentiality posture but unnecessarily blocks legitimate diagnostics; host-wide reads remain an advanced, explicitly configured custom option with operator-controlled notices and confirmation. |
| Rely on generated-state limits as host resource protection | Reject | Disk accounting does not constrain memory, process count, or CPU. |
| Build a second general-purpose OS sandbox now | Reject | Claude's native sandbox remains the selected Bash isolation mechanism; add missing policy, verification, and resource controls around it. |

## 17. Decisions and open questions

### 17.1 Stakeholder decisions already recorded

- Use Claude Code's native sandbox rather than build a second general-purpose OS sandbox.
- Preserve named profiles, but separate task class from capability and scope.
- Use a generic `mcp-readonly` abstraction instead of a codebase-memory-specific public profile.
- Support project roots, external read-only roots, and explicit external writable roots.
- Permit cross-profile resume through an “are you sure” authority-and-cache transition rather than
  a categorical version/profile block.
- Preserve prior proposals, plans, probes, and failed results as historical evidence instead of
  rewriting them to match the new design.
- Use the native sandbox by default for command-capable standard profiles, while retaining explicit
  configurable unsandboxed execution.
- Keep profile, cache, authority, context, runtime, and sandbox notices independent and suppressible;
  warnings do not prohibit profile transitions.
- Keep standard profile usage low-friction; enforcement matrices and tool-level mappings are
  internal assurance artifacts.

### 17.2 Revision-4 settled planning decisions

1. Adopt the policy compiler and schema in §§6–12 and §18.
2. Make project-plus-declared-roots the standard read scope.
3. Retain host-wide reads only as an advanced, explicitly configured custom policy with
   independently controllable notice and confirmation behavior.
4. Treat MCP internal caches/indexes as bounded writes that require declared state roots even when
   protected project data remains read-only.
5. Require configuration-source assessment and an `explain` preflight before paid runs; reserve
   effective-policy claims for runtime-observed evidence.
6. Govern memory, processes, time, output, and concurrency separately from generated disk state.
7. Permit broader and mixed resumes; present independently configurable contextual notices and
   never turn a recommendation into an unrequested prohibition.
8. Require a new implementation plan and independent review before changing the candidate.
9. Separate semantic policy identity, requested-authority identity, private binding identity,
   presentation state, and runtime assurance rather than overloading one hash or enum.
10. Keep confirmations `ask/never`; keep notices `always/once/never`; never let untrusted
    repository configuration own either surface.
11. Make selected host effects explicit and default-denied/unavailable rather than assuming the
    filesystem or command dimension covers them.

### 17.3 Open implementation and activation questions

- Which macOS mechanisms can enforce memory and process ceilings reliably enough to claim a hard
  boundary, and which must remain sampled guardrails?
- Can the installed Claude runtime expose all effective managed settings and disabled extension
  surfaces without a paid model turn?
- Are MCP server processes launched inside the same enforceable filesystem/network boundary as
  sandboxed Bash children on each supported Claude Code version?
- Should direct worker artifact writes remain deferred if manager materialization satisfies the
  first-release workflow?
- Which hard-link and mount-point counterexamples are enforceable preflight failures versus
  reconciliation-only detections?
- Which sandbox-incompatible tools merit named command templates, and which should remain custom
  unsandboxed exceptions?

These are investigation and implementation-planning questions. They are not permission to launch
runtime probes or broaden the present candidate.

## 18. Normative core policy schema

The C0 implementation normalizes this provider-neutral shape. Omitted authority fields default to
`deny` or `unavailable`; absence never means inherit unrestricted authority.

```yaml
schema_version: 1
profile:
  id: custom
  preset_revision: null
  legacy_contract_version: null

model_inputs:
  model: null
  effort: null
  system_input_hashes: []

context:
  objective_hash: null
  workspace_identity: null
  source_identity_hashes: []

runtime:
  provider: claude-code
  version: null
  activation: unavailable

filesystem:
  defaults: {read: deny, write: deny}
  roots: {}
  rules: []

tools:
  builtins: []
  deny: []

mcp:
  mode: deny
  servers: []
  selected_tools: []

commands:
  mode: deny
  templates: []

network:
  subprocess: deny
  mcp_open_world: deny
  allowed_destinations: []

host_effects:
  mode: deny
  grants: []

git: {mutation: deny}
installation: {mode: deny}
descendants: {mode: deny}
output: {mode: manager, roots: []}

sandbox:
  mode: off
  unavailable: fail
  unsandboxed_commands: []

resources:
  wall_time_seconds: {mode: unavailable, value: null}
  process_count: {mode: unavailable, value: null}
  memory_bytes: {mode: unavailable, value: null}
  log_bytes: {mode: unavailable, value: null}
  generated_state_bytes: {mode: unavailable, value: null}
  generated_state_admission_bytes: {mode: unavailable, value: null}

lifecycle:
  resume: allow
  recovery: foreground

notices:
  profile_transition: always
  cache_impact: always
  authority_change: always
  context_change: always
  runtime_change: always
  sandbox_change: always

confirmation:
  profile_transition: never
  authority_expansion: ask
  unsandboxed_command: ask
```

Every dimension defines its value type, default, narrowing relation, hard-boundary interaction,
preset value, extensibility, compiler target, evidence source, and `unknown` behavior in schema
metadata and fixtures. Notice and confirmation settings affect presentation, not the requested
authority or recorded transition facts.

### 18.1 Identity, bindings, assurance, and version dispatch

Normalization dispatches explicitly by `schema_version`; version 1 has one registered normalizer,
and unknown versions fail rather than falling through to the latest implementation. A semantic
no-op migration test begins with the first real schema migration.

The canonical document contains root IDs, kinds, and bound/unbound state, never resolved paths. A
private companion record binds root IDs and deny-selector IDs to resolved paths, provenance, and
run-lineage-scoped binding identities. That record is excluded from both public rendering and
cross-project telemetry. `semantic_sha256` hashes the canonical document; `authority_sha256`
hashes its authority projection and excludes profile labels, context, runtime observations,
notices, and confirmation preferences.

Authority comparison maintains grants and denies separately. Adding a grant or removing a deny
broadens; removing a grant or adding a deny narrows. Private rebinding is a context transition and
becomes authority-`unknown` when the relative deny effect cannot be ordered.

Assurance is not operator-requested authority. A versioned internal matrix maps preset × operation
family to `os-enforced`, `claude-enforced`, `manager-controlled`, `detected`, or `unknown` and is
rendered separately. C0 does not emit `os-enforced` for an unprobed runtime surface.

`profile.preset_revision` names the new preset contract. `profile.legacy_contract_version` exists
only for migration provenance and is labeled distinctly in output; it is not copied from or
confused with the preset revision.

### 18.2 Cross-field validity and normalization

| Requested state | Result |
|---|---|
| `commands.mode: selected` with no templates | reject |
| a command template with an unknown scope, invalid limit, malformed field, or duplicate ID carrying different authority content | reject |
| `mcp.mode: selected` with no selected tools, no matching declared server, or a namespace mismatch | reject |
| `host_effects.mode: selected` with no `{operation, target_id}` grants, an unknown operation, or an unstable target | reject |
| `mcp.mode: readonly` without resolved registry identities | accept as unresolved and non-activating; transition authority may be `unknown` |
| subprocess or MCP `allowlist` with no destinations | normalize to `deny` |
| any allow rule using raw `path` instead of a declared root `scope` | reject |
| a raw-path deny without a stable `rule_id` and private selector binding | reject |
| `bounded` resource with a missing/non-positive value, or `unavailable`/`unbounded` with a value | reject |
| an unsandboxed command ID not naming a command template whose sandbox disposition is `outside` | reject |
| `sandbox.mode: required` with commands denied/unavailable | retain as an explainable dormant request; it grants no authority and cannot activate in C0 |

`unavailable` is not silently ordered with `deny` or `unrestricted`. It records that the requested
surface cannot yet be compiled or observed. Assurance degradation is a runtime transition, not an
authority broadening. Selected-set comparison handles grant/deny direction explicitly so
allowlist-to-unrestricted is `broader`, not `mixed`.

Host-effect grants use a closed operation vocabulary and a stable symbolic `target_id`; raw PIDs,
socket paths, device paths, service names, and application identifiers remain in private runtime
registry/binding records. C0 can normalize and compare these grants but cannot activate them.

### 18.3 Preset extensibility

| Dimension | Standard review presets | Implementation presets | Custom policy |
|---|---|---|---|
| Read roots | may add declared roots | may add declared roots | explicit |
| Write roots | strict: none; verified: scratch; artifact: manager output | owned project/worktree plus scratch | explicit |
| Commands | strict: denied; executable presets: admitted templates | admitted templates and declared sandbox disposition | explicit |
| Network | denied unless preset explicitly says otherwise | denied unless explicitly extended | explicit |
| MCP | denied or reviewed local read-only bundle | separately declared reviewed bundle | explicit registry entries |
| Git/install/descendants/host effects | denied | preset-specific, default deny | explicit |
| Notices/confirmation | operator-configurable | operator-configurable | operator-configurable |
| Sandbox fallback | operator-configurable; no silent named-profile default | operator-configurable | explicit |

## 19. Requirement lineage ledger

| Requirement | Disposition | Normative location | Verification/activation gate |
|---|---|---|---|
| R-POL-001 Stable profiles compile from one schema | retained and revised | §§6, 18 | C0 snapshot and normalization tests |
| R-POL-002 Authority conflicts fail before paid launch | retained | §§6–7, 10, 13 | C0 precedence fixtures |
| R-POL-003 Profile/cache/authority/context/runtime/sandbox notices are independent and suppressible | new stakeholder decision | §11 | C0 semantic-diff and rendering tests |
| R-POL-004 Semantic, authority, binding, presentation, and assurance identity remain separate | Fable correction | §§6.1, 11–12, 18.1 | C0 hash, rebinding, and rendering tests |
| R-FS-001 Read/write roots are separate and named | retained and revised | §7 | C0 schema; C1/C3 runtime probes |
| R-FS-002 Enforcement claims carry assurance labels | new | §7.4 | C0 rendering; cohort-specific probes |
| R-FS-003 Undeclared changes are preserved, failed, and never auto-reverted | retained | §§7, 12 | C4 reconciliation tests |
| R-CMD-001 Executable review uses declared templates and scratch | retained and revised | §§9.1, 9.4 | C3 runner fixtures and probes |
| R-CMD-002 Command-template authority is typed and content-addressed | Fable correction | §§9.1, 18.2 | C0 schema/hash tests; C3 compilation tests |
| R-SBX-001 Command-capable presets use native sandbox by default | retained and revised | §§9.4–9.6 | C3/C4 runtime probes |
| R-SBX-002 Unsandboxed execution is explicit, configurable, and recorded | new stakeholder decision | §9.6 | C0 schema; C3/C4 negative tests |
| R-MCP-001 `mcp-readonly` is generic and registry-backed | retained and revised | §8 | C0 schema; later registry plan |
| R-MCP-002 Exposure, permission, attempt, and success are distinct | retained | §§8.3, 10 | manifest fixtures and runtime probes |
| R-RES-001 Generated state remains below the existing configured/admission thresholds | retained | §§5, 9.3 | cohort budget tests |
| R-RES-002 Memory/process/time/recovery are distinct from disk budget | new | §§9.3, 12 | cohort-specific resource tests |
| R-RES-003 Omitted, bounded, unbounded, and unavailable resource states are distinct | Fable correction | §§9.3, 18 | C0 normalization and directional-diff tests |
| R-OUT-001 Every successful attempt remains independently materializable | retained | §12 | C2 compatibility tests |
| R-OUT-002 Manager materialization is the first artifact default | retained | §§7.4, 15 | C2 atomic-write tests |
| R-RSM-001 Resume uses compiled semantic and authority diff, not version alone | revised stakeholder decision | §11 | C0 exact/narrower/broader/mixed/unknown fixtures |
| R-RSM-002 Broader and mixed resumes remain available | new stakeholder decision | §11 | C0 warning/confirmation-off tests |
| R-RSM-003 Known broadening remains visible when another dimension is unresolved | Fable correction | §§11.1, 18.1 | C0 known-kind plus unresolved-dimension tests |
| R-HOST-001 Host process/socket/service/device/application effects are explicit and default denied | Fable correction | §§6.2, 9.5, 18 | C0 schema tests; C3/C4 probes |
| R-AUD-001 Historical proposal, plan, and probe remain immutable evidence | retained | §§2, 5 | link and hash audit |
| R-AUD-002 Meaningful pre-init events fail manifest-enforced profiles | retained | §§8.3, 13 | C1/C3 lifecycle tests |
| R-TEL-001 Cross-project telemetry is content-free and allowlisted | retained and revised | §12 | privacy schema tests before export |
| R-REL-001 Cohorts activate independently | new | §15 | per-cohort review and probe record |

Requirements not listed as active are not silently inherited. The revision-4 correction record
maps the accepted Fable findings to this ledger and the corrected plan.

## 20. Authorization gate

Revision 4 records the corrected proposal and C0 implementation plan. It does not authorize code
changes, installation, deployment, commit, route changes, profile activation, network downloads,
package installation, external side effects, or paid model calls.

Until the proposal, review dispositions, implementation plan, deterministic tests, and separately
approved runtime probes pass, the version-3 adapter remains an uninstalled candidate. The earlier
probe remains parked/inconclusive, and no retry is implied.
