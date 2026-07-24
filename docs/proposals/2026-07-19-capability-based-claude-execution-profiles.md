# Proposal: capability-based Claude execution profiles

> **Historical baseline:** This approved-but-uninstalled proposal records the contract used for
> the version-1 through version-3 candidate and the first actual-runtime probe. It is partially
> superseded for future implementation by the
> [composable capability and scope policy proposal](2026-07-20-composable-claude-capability-and-scope-policy.md).
> The body below is preserved as the historical decision and evidence baseline.

- **Date:** 2026-07-19
- **Status:** approved for corrective implementation; not installed or deployed
- **Audience:** maintainers of the Codex-managed Claude adapter
- **Decision recorded:** use Claude Code's native sandbox, with adapter-enforced profile and
  lifecycle controls, rather than build a second operating-system sandbox
- **Implementation authority:** code, tests, and canonical documentation only; no installation,
  deployment, commit, route activation, or descendant paid calls

### Revision record

| Revision | Date | Disposition |
|---|---|---|
| Initial | 2026-07-19 | Proposed capability-profile delta and identified the sandbox mechanism as an open decision. |
| Corrective revision | 2026-07-19 | Retains the profile model, selects Claude Code's native sandbox, makes scratch roots argument-declared, and supersedes the first incomplete implementation plan. |
| Supersession notice | 2026-07-20 | Preserves this body as the candidate's historical contract and points future work to the composable-policy proposal. |

## 1. Problem and observed failure

The current Codex prototype can launch Claude with custom permission modes and tools, but it has
only one named profile: `readonly-review`. That profile pins `dontAsk` and the built-in tools
`Read`, `Grep`, `Glob`, and `Skill`. The name conflates a task class (review) with a capability
boundary (strict read-only), while the absence of other named profiles makes the strict profile
an attractive but incorrect default for reviews that require execution evidence.

On 2026-07-19, a paid Fable product and technical review used that strict profile. The reviewer
could inspect source but could not run the test suite, execute SQLite counterexamples, inspect
query plans, or read one required external handoff because its directory was not declared. A
separate executable Sol review later reproduced two High-severity defects that the Fable review
missed. An additional paid Fable continuation was also required to correct an over-constrained
product framing. This incident is one observation, not proof that executable reviewers always
dominate, but it is a direct falsifier of using strict source-only review as the general review
default.

The same run exposed a second contract gap. Claude's effective startup manifest included the
connected codebase-memory MCP server and both read and mutating MCP tools, even though the
wrapper's stored profile listed only four built-in tools. The reviewer made no MCP calls, but the
stored requested tool list was not an accurate statement of the effective tool surface.

## 2. Relationship to the accepted architecture

This is a bounded delta to the existing cross-runtime delegation proposal:

- its resume rule already requires the objective and trust boundary to remain valid (§8.2);
- its cache contract already requires stable tools, settings, working directory, and system
  inputs (§8.3);
- its permission contract already requires the least-capable proven tool set that can satisfy the
  packet (§9);
- its task packet already declares permission mode, allowed and denied tools, filesystem scope,
  required sources, and output artifacts (§7.1).

The delta makes those abstract requirements executable through named, versioned profiles. It does
not change model routing, warrant grades, or the Option 2/Option 3 decision.

## 3. Source map and claim status

| Claim | Status | Evidence and limitation |
|---|---|---|
| The deployed prototype supports custom tools and several Claude permission modes but defines only one named profile. | Observed | Prototype wrapper symbols `PROFILES`, `READONLY_REVIEW_TOOLS`, `cmd_run`, and `_build_command`, inspected 2026-07-19. The prototype is not yet the canonical package implementation. |
| The effective Fable manifest included codebase-memory MCP tools that were absent from stored profile metadata. | Observed | Fable session `785abf2f-ea69-4638-952c-d9afae18d724`, startup `init` event. Exposure does not prove permission to execute every listed tool. |
| Permission-mode changes alone can preserve cache eligibility, while tool-definition changes invalidate the cache from the tool/system prefix. | Reported | Anthropic [prompt-caching documentation](https://code.claude.com/docs/en/prompt-caching). Exact provider cache keys and retention remain provider-controlled. |
| Claude sessions retain prior prompts, tool calls/results, and responses when resumed. | Reported | Anthropic [session documentation](https://code.claude.com/docs/en/agent-sdk/sessions). Retained context is useful for continuation but weakens evidentiary independence. |
| Claude supports changing allowed tools on resume, but the prototype wrapper deliberately reasserts stored controls. | Concordant | Anthropic session examples plus prototype wrapper resume command construction. Runtime support does not make trust-boundary expansion on resume desirable. |
| External read roots can be added explicitly. | Reported | Anthropic [CLI reference](https://code.claude.com/docs/en/cli-usage). An added directory does not automatically import all configuration beneath it. |
| Claude Code's native Bash sandbox uses operating-system enforcement on macOS and Linux, but built-in Edit and Write tools remain permission-controlled rather than Bash-sandboxed. | Reported | Anthropic [sandbox documentation](https://code.claude.com/docs/en/sandboxing). The adapter still needs explicit tool denies and post-run ownership reconciliation. |
| The native sandbox can fail open when unavailable and permits an unsandboxed-command escape hatch unless configured otherwise. | Reported | Anthropic [sandbox configuration reference](https://code.claude.com/docs/en/configuration). The verified profile therefore pins fail-closed settings and disables the escape hatch. |
| Array-valued settings merge across configuration scopes rather than replacing lower-priority values. | Reported | Anthropic [settings precedence documentation](https://code.claude.com/docs/en/configuration). An invocation-local settings file alone is not evidence that broader user or project arrays disappeared. |

## 4. Design principles

1. **Profiles are contracts, not overrideable defaults.** A profile declares invariants and may be
   narrowed by a packet, never silently broadened by a command-line flag.
2. **Task class and capability are separate.** Routing decides which reviewer or implementer is
   appropriate; the execution profile decides what that worker may do.
3. **Requested and effective surfaces are distinct.** Store both the requested profile manifest
   and the effective startup manifest. Never copy one into the other.
4. **Execution evidence is first-class.** A review that needs tests or diagnostics must select a
   profile that can produce them.
5. **Write authority is path- and purpose-scoped.** General edit permission is not a substitute
   for an owned-file or output-artifact contract.
6. **Resume never expands trust.** A broader tool, directory, network, or write boundary starts a
   fresh session with new lineage.
7. **No profile implies network, installation, commits, pushes, destructive commands, or external
   side effects.** Those remain separately declared authorities.

## 5. Canonical profiles

Profiles are versioned data records consumed by the adapter, not conditionals scattered through
the launcher. Each record declares permission mode, built-in tools, MCP policy, filesystem reads,
writes, command policy, network policy, output contract, and resume compatibility.

### 5.1 `strict-readonly`

Use for source-only audits, document reviews, investigations where execution would be inappropriate,
and high-sensitivity contexts.

- no Bash, Write, Edit, NotebookEdit, agent spawning, installation, or network tools;
- only explicitly named read-only built-ins;
- MCP disabled by default;
- an MCP server may be enabled only through an explicit read-only tool allowlist;
- no project or artifact writes; stdout capture and deterministic manager materialization only;
- permission mode pinned to `dontAsk` unless a capability probe establishes a stronger strict
  read-only mode.

`readonly-review` becomes a deprecated compatibility alias for `strict-readonly`. The alias emits
a warning and resolves to the exact same versioned manifest. Remove it only after at least one
documented release cycle and installer drift report.

### 5.2 `verified-review`

Use for code and systems reviews whose conclusions depend on tests, query plans, reproductions,
benchmarks, or other local diagnostics.

- all `strict-readonly` read capabilities;
- bounded local command execution under an exact adapter-enforced command policy;
- test-runner-owned temporary writes under one argument-declared, run-scoped scratch root;
- no source edits or project artifact writes;
- no network, installation, package-manager mutation, destructive command, commit, or push;
- explicit external read roots for required handoffs or sibling repositories;
- read-only codebase-memory tools may be enabled explicitly; mutating MCP calls are denied.

The adapter uses Claude Code's native sandbox rather than implementing a second operating-system
sandbox. For this profile it launches Claude from the declared scratch root and adds the actual
project as an explicit read root. The resulting boundary is scratch-writable and project-readable,
while Write, Edit, and NotebookEdit remain denied. The adapter pins sandbox availability as a hard
requirement, disables automatic approval of arbitrary sandboxed Bash, disables unsandboxed-command
fallback, allows no excluded commands, and denies Bash network access. Exact command rules still
matter: sandboxing limits effects but does not authorize an arbitrary command.

If the installed Claude runtime, active settings layers, or observed behavior cannot establish
these boundaries, `verified-review` fails closed before accepting a result. It never degrades to
unsandboxed Bash or a permission-only approximation.

### 5.3 `artifact-review`

Use when the reviewer must leave a durable review document.

- all `verified-review` capabilities;
- one packet-declared output artifact;
- no worker file-write tools or checkout edits;
- manager materializes a successful structured result to the declared output and records its hash.

When path-scoped writes cannot be enforced, the profile falls back to stdout capture followed by
deterministic manager materialization. It must not silently grant general Edit or Write tools.

### 5.4 `implementation`

Use for bounded implementation with explicit owned files or an isolated worktree.

- project edits limited to the packet's ownership manifest;
- interactive or `acceptEdits`-class permission mode, selected only after capability probing;
- local tests and diagnostics;
- undeclared diffs fail reconciliation;
- network, installation, commit, push, destructive operations, and external writes remain denied
  unless separately authorized in the packet.

Claude's native sandbox supplies the outside-workspace filesystem and Bash-network boundary. The
adapter separately snapshots HEAD, index state, Git-visible dirty paths, and ignored non-scratch
paths before execution, then reconciles the final state against declared owned paths and scratch
roots. Dirty-file hashes are streamed without the earlier 8 MiB size-only shortcut. Git control
changes and ignored installation/build side effects always fail; ownership declarations apply only
to product paths. Reconciliation is detection, not rollback: an undeclared change fails the attempt
and remains preserved for root disposition.

### 5.5 `implementation-auto`

Use for unattended bounded implementation when Claude auto mode has passed a dated capability
probe and the packet supplies a complete ownership and validation contract.

- permission mode pinned to `auto`;
- the same filesystem, network, ownership, diff, and reconciliation boundaries as
  `implementation`;
- no broader authority merely because the interaction mode is automatic;
- fail closed when auto mode is unavailable, its configuration is unreadable, or its effective
  behavior cannot be observed.

Auto mode changes permission interaction, not task authority.

Neither implementation profile is safe as a standalone raw launcher. It requires an ownership
manifest, a pre-run worktree snapshot, post-run reconciliation, and a root disposition step.

## 6. Precedence and conflicting arguments

The adapter resolves controls in this order:

1. runtime and operator hard prohibitions;
2. versioned profile invariants;
3. task-packet scopes that may narrow the profile;
4. invocation arguments that must agree with the resolved contract.

There is no last-flag-wins behavior for authority-bearing fields.

- `--profile implementation-auto --permission-mode auto` is valid but redundant.
- `--profile implementation-auto --permission-mode acceptEdits` is a configuration error.
- adding denied tools or narrowing directories is allowed when internally consistent;
- adding a tool, directory, write root, network capability, or permission mode beyond the profile
  is an error;
- omitting `--profile` selects explicit custom mode, where every authority-bearing field must be
  supplied and recorded. Custom mode is never an implicit fallback.

The error reports the conflicting field, profile invariant, and safe alternatives. It must occur
before a paid model invocation.

## 7. Effective tool and MCP manifest

The adapter computes an expected manifest before launch and records its content hash. The expected
manifest includes:

- built-in tools;
- allowed and denied MCP tool identifiers;
- MCP server configuration hash;
- permission mode;
- working directory and external read roots;
- writable roots and output artifacts;
- command-policy version;
- network and subprocess policy.

Structured startup output supplies the observed effective tool and MCP manifest. The manager
compares observed identifiers with the expected manifest and records `match`, `narrower`,
`broader`, or `unknown`. An unexpected broader surface is a permission failure even when the model
never calls the extra tool.

For strict profiles, comparison happens as soon as the startup event arrives. A broader or unknown
manifest terminates the attempt before assistant or tool events are accepted. An absent startup
event, or an event that omits the tool list, is `unknown`, not an empty or narrower manifest.
Explicitly allowed read-only MCP tools are part of the expected manifest; explicitly denied exposed
tools remain recorded but do not count as permission-allowed.

The first candidate admits only a versioned exact allowlist of codebase-memory query identifiers.
Its strict MCP configuration must declare exactly the namespaces required by those identifiers and
must use a local absolute stdio executable with no arguments, URL transport, or environment
overrides. The adapter records both configuration and executable hashes. This pins provenance but
does **not** prove the executable's semantics; the profile remains unactivated until the separately
authorized actual-runtime probe verifies effective per-tool permission behavior.

MCP servers that combine read and mutating tools require one of:

1. a proven per-tool deny mechanism that prevents mutating calls;
2. a read-only facade exposing only approved operations; or
3. exclusion from strict and verified review profiles.

Merely seeing an MCP tool in a startup manifest does not prove it is callable, so the capability
matrix must distinguish exposed, permission-allowed, and successfully invoked. Unknown state fails
closed for strict profiles.

## 8. Commands, scratch roots, external roots, and output artifacts

The task packet declares each required source and classifies it as project, external read-only, or
writable output. The adapter rejects missing declarations rather than allowing a reviewer to
silently omit evidence.

`--scratch-dir` declares the only worker-writable scratch root for verified and artifact reviews.
The manager canonicalizes the path, rejects symlinks and unsafe ownership or permissions, records it
in a run-bound ownership marker, and includes it in the generated-state budget. Existing roots must
be owned by the current user, mode `0700`, and either empty or carry the exact marker for the current
run. When omitted, the manager creates a
run-scoped scratch directory under its managed state root. A caller may instead select a dedicated
workspace directory; because Claude executes from that directory while the project is attached as
a read root, this does not make the rest of the workspace Bash-writable. The adapter sets temporary
and supported cache environment variables to the scratch root, but commands that require undeclared
project-local build output are incompatible with `verified-review`.

`--artifact-output` declares a durable output path. The default artifact-review contract keeps
Write and Edit denied and materializes a successful structured result through the manager. Direct
worker writes require a separately proven exact-path permission mechanism and are not part of the
first corrective implementation.

For executable reviews, the command policy is declarative and versioned. It may authorize test
runners, linters, type checkers, read-only database inspection, process inspection, and bounded
temporary fixtures. It separately denies shell composition or programs that could mutate source,
install software, access the network, change Git state, or operate outside declared temporary
roots. The effective policy and any permission denials appear in the result envelope.

The first corrective implementation combines exact Claude Bash permission rules with the native
sandbox boundary. Command-string filtering alone is not the security boundary. The sandbox must be
enabled, available, escape-hatch-disabled, and configured with no Bash network destinations before
the command policy is considered effective.

Review artifacts are written either by an enforceably artifact-scoped worker or by deterministic
materialization from structured stdout. The manager preserves every successful attempt separately;
a resume must not make an earlier result impossible to materialize.

### 8.1 Generated-state budget

The adapter accepts no configured ceiling above 240 MiB and uses a lower 192 MiB operational
threshold to preserve headroom beneath the user-level `<250 MiB` constraint. Admission checks the
operational threshold—not the higher configuration cap—and reserves the shared log budget before
every new attempt and resume. The accounting scope covers metadata, stdout, stderr, and every
manager-created or manager-authorized scratch root. During execution, historical state is accounted
once; the bounded in-process watchdog repeatedly samples only the current run and non-overlapping
scratch roots. Manager-written logs use one exact shared byte budget, while subprocess files also
receive a conservative per-file resource limit where the platform supports it. Any shared-log
truncation is non-materializable. An attempt that cannot reserve bounded state fails before launch;
an attempt that crosses the operational threshold terminates and records the overrun. An external
scratch root does not escape accounting merely because it is outside the managed state directory.

The native sandbox is not a filesystem quota. The headroom and watchdog make accidental threshold
overshoot unlikely but do not prove that an adversarial subprocess can never cross 250 MiB between
samples. A hard adversarial byte ceiling would require a quota-backed filesystem or container and
is outside this implementation. This limitation must remain visible until an actual-runtime probe
measures termination behavior.

## 9. Resume, freshness, and cache behavior

Resume is allowed only when objective, trust boundary, profile ID and version, effective tools,
MCP configuration, model, effort, working directory, and source roots remain compatible.

Any expansion of tools, external roots, writable roots, command authority, network authority, or
permission interaction starts a fresh session. This remains true even when the underlying Claude
CLI supports changing those options on resume. A fresh session provides clean lineage and avoids
presenting a continuation as an independent audit.

Changing permission mode without changing tool definitions may remain cache-eligible according to
current provider documentation. Changing tool definitions changes the system/tool prefix and should
be treated as cold from that point. The adapter records observed cache creation and read counters;
it never promises a hit and never launches a paid call merely to improve cache behavior.

For the 2026-07-19 Fable incident, the recommended follow-up is a fresh `verified-review` session,
not a resume: the tool boundary changes and an independent technical verdict is desired.

## 10. Configuration and result records

Add these fields to the canonical task and lifecycle records:

- `profile_id` and `profile_version`;
- `profile_alias_used`, when applicable;
- expected and observed manifest hashes;
- manifest comparison status;
- command-policy ID and version;
- external read roots and writable artifact roots;
- scratch root, its provenance (`default` or `argument`), and its accounted byte total;
- native sandbox policy hash, availability result, and unsandboxed-fallback status;
- MCP servers plus exposed, allowed, denied, and invoked tool sets;
- conflict or fail-closed reason;
- materialized attempt number and artifact hash;
- resume-compatibility decision and reason;
- cache creation/read counters per attempt.

Content-free cross-project telemetry records only bounded codes and hashes. Paths, command text,
tool output, prompts, transcripts, and artifact contents remain in private run state.

## 11. Implementation sequence

1. **Profile schema and resolver:** versioned records, compatibility alias, narrowing rules, and
   deterministic conflict errors.
2. **Fake-CLI manifest fixtures:** expected versus observed built-in/MCP tools, including unexpected
   mutating MCP exposure.
3. **Resume compatibility:** fresh-session requirement for capability expansion and per-attempt
   result preservation.
4. **Strict profile:** reproduce existing source-only behavior under the new canonical name.
5. **Verified review:** generate fail-closed native-sandbox settings, exact command permissions,
   scratch-root execution, and external read declarations.
6. **Artifact review:** enforce output ownership or deterministic materialization.
7. **Implementation profiles:** add owned-path worktree reconciliation, then separately
   capability-probe auto mode.
8. **Installer and deployment:** drift checks, version stamps, migration warning, and documentation.
9. **Actual-runtime probes:** separately authorized, smallest sufficient calls; fake fixtures do not
   establish real enforcement.

## 12. Verification contract

Deterministic tests must cover:

- `readonly-review` alias resolution and warning;
- exact profile snapshots and version hashes;
- every permission-mode/profile mismatch, including `implementation-auto` conflicts;
- allowed narrowing versus rejected expansion;
- absent, narrower, exact, broader, and unknown effective manifests;
- mutating or unknown MCP tools under strict and verified profiles;
- immediate termination for broader or unknown startup manifests;
- explicitly allowed read-only MCP tools in the effective manifest;
- native-sandbox unavailable and escape-hatch configuration failures;
- command-policy shell composition, project-write, network, and scratch-root escape attempts;
- default and argument-declared scratch roots, including a workspace-local scratch root;
- aggregate state enforcement across new runs, resumes, logs, and external scratch roots;
- external required source omitted from the allowed roots;
- artifact-only writes and undeclared diff rejection;
- dirty-worktree ownership reconciliation without overwriting or reverting prior changes;
- legacy successful-attempt materialization when the newer convenience flag is absent;
- materialization of every successful attempt after later resumes;
- fresh-session selection when tools or trust boundaries expand;
- observed cache counters without claims of guaranteed hits;
- fake CLI behavior separately labeled from actual-runtime evidence.

Package-level checks remain `check_state.py`, `check_wids.py`, and exact-diff inspection. An
actual-runtime smoke test requires separate paid-call authority and must record the installed CLI
version, requested controls, effective startup manifest, permission denials, cache counters, and
retained state size.

### 12.1 First actual-runtime probe (2026-07-20)

The first authorized Sonnet-high probe was useful but inconclusive. Claude Code `2.1.215` exposed
all ten pinned non-mutating codebase-memory tools in its init manifest while only `list_projects`
was permission-allowed. Version 2 incorrectly treated the other nine exposed identifiers as
broader and terminated before any assistant or tool event. No filesystem or network action ran,
so the probe did not establish sandbox enforcement.

Version 3 explicitly denies every unselected pinned MCP identifier and classifies their startup
visibility as exposed-but-denied. The version bump prevents resume of the failed version-2 session
under changed authority semantics. Full evidence and remaining unknowns are recorded in
`probes/records/P-20260720-claude-profile-actual-runtime.md`. Activation remains blocked on one
fresh, separately approved version-3 probe; a paid retry is not implicit in the first approval.

## 13. Alternatives

| Alternative | Disposition | Reason |
|---|---|---|
| Keep only `readonly-review` plus raw flags | Reject | Repeats capability-selection judgment at every call and makes omission of Bash, external roots, or MCP policy likely. |
| Rename the strict profile but add no others | Reject | Fixes terminology without fixing the routing failure. |
| Let explicit flags override profile fields | Reject | A stray or reordered argument can silently broaden authority; provenance becomes ambiguous. |
| One general `review` profile with unrestricted Bash | Reject | Over-corrects the incident and weakens strict audits. |
| Treat MCP startup visibility as proof of permission | Reject | Exposure, authorization, and successful invocation are distinct observations. |
| Resume whenever it may save cache | Reject | Cache economics do not justify trust-boundary expansion or contaminated review evidence. |
| Build and maintain a second operating-system sandbox | Reject for the first implementation | Claude Code already supplies native OS-level Bash isolation; the adapter should configure, verify, and fail closed around it. |
| Enable Claude's sandbox with its defaults | Reject | Default workspace writes, settings-array merging, unavailable-sandbox fallback, and the unsandboxed escape hatch do not satisfy the profile contract. |
| Hard-code `/tmp` as the review write root | Reject | Callers need an explicit workspace or external scratch choice, while the manager needs a bounded default with attributable lifecycle state. |

## 14. Decisions and open questions

### Proposed decisions

1. Adopt the five canonical profiles above.
2. Rename the strict profile to `strict-readonly` and retain `readonly-review` temporarily as a
   deprecated alias.
3. Treat profile conflicts as pre-launch errors; never use last-flag-wins authority semantics.
4. Require fresh sessions for trust-boundary expansion.
5. Record and compare requested versus effective built-in and MCP manifests.
6. Preserve every successful attempt as an independently materializable result.
7. Implement bounded command execution before calling any profile `verified-review`.
8. Use Claude Code's native sandbox for Bash isolation and treat its effective configuration as
   evidence to verify, not an implicit guarantee.
9. Make scratch roots argument-declared, defaulting to manager-owned run state.
10. Reject configured ceilings above 240 MiB, admit runs against a 192 MiB operational threshold
    with reserved headroom, and sample only current-run growth during execution.

### Resolved stakeholder decisions

- Claude Code's native sandbox is the first implementation's Bash isolation mechanism. macOS is
  the initial validation target; Linux remains a required architectural boundary but not a first-
  release validation target.
- Unknown manifest state fails strict and verified profiles. A tool that is exposed but explicitly
  denied remains recorded and does not itself make the allowed surface broader.
- `readonly-review` remains an alias for at least one documented release cycle.
- The completed Sonnet/Opus implementation-review calls and root correction pass are historical
  evidence, not standing authority for additional paid Claude calls. Actual-runtime enforcement
  probes remain separately gated.

### Remaining release decisions

- Whether to authorize one fresh version-3 Sonnet-high probe to complete the already-bounded
  filesystem, localhost-network, and MCP checks.
- Whether a later direct-write artifact profile is worth supporting beyond manager materialization.

## 15. Authorization gate

The operator approved the completed corrective worker passes and the local root correction pass.
The root remains the sole writer for proposal, plan, skill, README, and other user-consumed prose.
No additional paid call, installation, deployment, commit, route change, policy activation,
descendant agent, network download, or paid runtime probe is authorized after P-20260720. The corrective
implementation must preserve unrelated dirty files, enforce the aggregate generated-state budget,
and keep fake-CLI validation distinct from actual-runtime evidence.
