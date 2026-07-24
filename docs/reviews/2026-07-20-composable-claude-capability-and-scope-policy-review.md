DECISION

# Independent cold review — composable Claude capability and scope policy, revision 2

- **Consult ID:** `/root/policy_proposal_review` *(task-path surrogate; no separate Consult ID was supplied)*
- **Date:** 2026-07-20
- **Reviewer:** GPT-5.6 Sol High
- **Target:** `2026-07-20-composable-claude-capability-and-scope-policy.md`, revision 2
- **Scope:** Read-only policy review; no edits, installation, activation, paid calls, runtime mutation, or Git-state changes
- **Executive verdict:** **Revise**
- **Recommended action:** Preserve the composable compiler, evidence model, `explain` surface, manager materialization, and activation gates, but issue revision 3 before implementation planning. Narrow the first activation cohort and resolve the three Blockers below.
- **Rationale:** Revision 2 is directionally strong but does not yet supply an implementable authority contract. Its selected enforcement layers cannot presently establish every promised filesystem boundary; several declared capability dimensions lack normative schemas; and capability-expanding resume preserves prompt-injected context while adding effect authority.
- **Constraints:** Keep the candidate uninstalled and unchanged; retain historical artifacts; do not authorize paid probes through this review; do not silently replace stakeholder decisions.
- **Required checks:** Normative schema fixtures, per-profile enforcement matrix, inherited-configuration probes, negative filesystem/MCP tests, transition-safety tests, recovery/resource tests, and separately approved macOS runtime probes.
- **Alternatives rejected:** Implement revision 2 as written; rely on confirmation alone for effect-expanding resume; treat permission rules or startup exposure as OS enforcement; activate all five profiles together; solve uncertainty by granting host-wide reads.
- **Confidence:** High (0.91)
- **Human approval required:** Yes. Revision 3 would narrow the approved resume policy and first-release profile set.
- **Remaining uncertainty:** The installed runtime has not demonstrated built-in file-tool confinement, MCP process containment, sandbox effects, resource ceilings, or successful resume/cache behavior. The recorded paid probe stopped before a model turn.
- **XHigh:** Not justified. This was a bounded document-and-primary-evidence review; Sol High was sufficient.

## Strengths worth preserving

1. **Clear evidence staging.** Requested, configured, exposed, allowed, attempted, and successful states are deliberately separated (§§8.3, 12–14), directly addressing the failed probe.
2. **Composable direction.** Separating profiles, capabilities, grants, and named scopes is preferable to profile proliferation (§§6–7).
3. **Useful preflight UX.** A non-generative `explain` surface with provenance, unresolved controls, and resource classifications is a strong product requirement (§10).
4. **Conservative MCP posture.** The proposal correctly rejects names and MCP annotations as trust evidence and recognizes server startup/internal-state effects (§8).
5. **Resource epistemics.** Sampled guardrails are not mislabeled as hard quotas (§9.3).
6. **Recovery discipline.** Partial evidence is preserved, user work is not rolled back, and no crash automatically triggers another paid call (§12).
7. **Activation discipline.** Fake-CLI evidence is separated from runtime evidence, and platform/version-scoped probes remain separately authorized (§14).
8. **Historical preservation.** The prior proposal, corrective plan, and failed probe remain evidence rather than being rewritten (§§2, 5).

## Finding summary

| Severity | Count |
|---|---:|
| Blocker | 3 |
| High | 6 |
| Medium | 3 |
| Low | 0 |

## Prioritized findings

### POL-001 — Blocker — The selected layers cannot yet establish the promised scoped filesystem contract

**Proposal sections:** §§7.3–7.4, 10, 13–15.

**Evidence/reasoning:**

- **Observed:** Revision 2 promises operation-specific scoped roots and says allowed boundaries are compiled into built-in tool permissions and the native Bash sandbox.
- **Reported:** Anthropic documents the OS sandbox as applying to Bash and its descendants, not built-in file tools. It describes `Read` enforcement across Grep, Glob, prompt file mentions, and IDE context as best-effort. It also states that scoped `Write`, `NotebookEdit`, and `Glob` rules are accepted but not matched; `Read(path)` and `Edit(path)` are the matching forms. See [permissions, “Read and Edit”](https://code.claude.com/docs/en/permissions#read-and-edit) and [sandboxing, “Permission rules”](https://code.claude.com/docs/en/sandboxing#permission-rules).
- **Reported:** The sandbox defaults to host-wide reads and working-directory writes; a linked worktree may also expose shared Git control state for writing. See [sandboxing, “Filesystem isolation”](https://code.claude.com/docs/en/sandboxing#filesystem-isolation).
- **Observed:** The current candidate allows base `Read`, `Grep`, and `Glob` in `strict-readonly`, while Bash-capable implementation runs rely on native sandbox settings and post-run reconciliation (`adapters/codex/delegate-to-claude/scripts/delegate_to_claude/profiles.py`, lines 73–118; `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/runtime_policy.py`, lines 197–227)<!-- de-linked 2026-07-24: the delegate-to-claude tree is intentionally uncommitted pending the runtime-home decision (portfolio review D-3/C-2); paths preserved verbatim -->. This is historical candidate evidence, not proof that revision 2 is impossible, but it demonstrates the migration gap.

**Impact:** `strict-readonly` cannot currently claim a hard project-plus-declared-roots confidentiality boundary. Implementation profiles also cannot claim owned-path-only Bash writes if Claude starts in the project, because the working directory is writable by default. A policy hash would make an unenforced abstraction look authoritative.

**Bounded correction:** Add a normative per-profile enforcement matrix covering each operation and tool:

- exact Claude rule and sandbox setting;
- process working directory;
- whether enforcement is provider permission, OS-enforced, manager-staged, post-run detection, or unknown;
- required negative probe;
- activation disposition when the layer is best-effort.

For the first release, either stage declared source material into a manager-controlled root or disable built-in file readers and use sandboxed, scoped read commands. Launch write-scoped workers from scratch or an isolated worktree with explicit project read and owned-path write grants. Do not activate a profile whose advertised boundary is only reconciliation.

### POL-002 — Blocker — The canonical policy schema is incomplete for the capabilities the proposal declares authoritative

**Proposal sections:** §§1, 6, 7, 9, 12–15.

**Evidence/reasoning:** Revision 2 lists filesystem, command, network, MCP, Git, installation, descendant-agent, output, resource, and lifecycle capabilities (§§1, 6.2), but only filesystem, MCP, and network receive partial declarative shapes. Command support is described as what the first implementation “may support”; Git, installation, descendants, output, confirmation, resources, and lifecycle lack normative fields, defaults, conflict rules, and compiler mappings. Section 7.2 requires the profile to mark dimensions “extensible,” but no preset extensibility matrix exists. The pipeline in §6.1 uses additive notation without defining conflicts between packet grants, invocation grants, registry restrictions, and hard boundaries.

**Impact:** A replacement implementation plan cannot be derived without inventing public schema, defaults, and authority precedence—the opposite of the stated closure target.

**Bounded correction:** Add a normative schema appendix and fixture set. For every dimension define:

- type and allowed values;
- default-deny behavior;
- narrowing/broadening relation;
- hard-boundary interaction;
- preset value and whether extensible;
- interactive and unattended approval requirements;
- compiler target and observable evidence;
- unsupported/unknown behavior.

Unsupported first-release dimensions should remain explicit `deny` or `unavailable`, not underspecified.

### POL-003 — Blocker — Confirmation does not make effect-expanding resume safe

**Proposal sections:** §§11.1–11.2, 17.1–17.2.

**Evidence/reasoning:**

- **Observed:** The historical contract required a fresh session for trust-boundary expansion ([historical proposal](../proposals/2026-07-19-capability-based-claude-execution-profiles.md), §§4, 9).
- **Stakeholder decision:** Revision 2 replaces that rule with a semantic diff and acknowledgement.
- **Inference:** Existing context may contain prompt injection, adversarial repository content, forged tool output, or instructions adapted to a previously harmless read-only boundary. Adding write, network, Git, installation, credentials, or external-side-effect authority turns that retained content into influence over new effects. A transition-hash acknowledgement records operator acceptance; it does not remove the contaminated context.

**Impact:** The resume design creates a confused-deputy path across trust boundaries, including unattended execution. Cache preservation is not a safety justification.

**Bounded correction:** In the first release, permit only `exact` and provably `narrower` resumes. Require a fresh session whenever effect authority is added. Preserve the semantic diff and transition-hash UX as the explanation and audit record. A later advanced override should require its own reviewed threat model, an explicit trusted-context predicate, and negative prompt-injection probes.

### POL-004 — High — Approval and authorization states contradict each other

**Proposal sections:** Metadata, §§1, 5, 17.2, 18.

**Evidence/reasoning:** The header and revision record say revision 2 is stakeholder-approved. Section 1 still requests approval, §17.2 labels eight central decisions “awaiting approval,” §5 says a new plan follows review and approval, and §18 says approval authorizes planning.

**Impact:** A future maintainer cannot tell whether policy decisions are settled, provisionally approved, or awaiting post-review reapproval. This weakens the authorization boundary.

**Bounded correction:** In revision 3, distinguish:

1. stakeholder-approved direction;
2. reviewer findings pending disposition;
3. decisions reopened by accepted findings;
4. implementation-planning authority;
5. activation authority.

Mark every §17.2 item settled, revised, or still pending, and give revision 3 a new content hash.

### POL-005 — High — `mcp-readonly` lacks a complete trust and process-containment contract

**Proposal sections:** §8, §§10, 14, 17.3.

**Evidence/reasoning:** The trusted registry records useful fields, but does not normatively specify registry ownership, review authority, expiry, signature/integrity, transitive executable provenance, environment allowlisting, dynamic dependencies, concurrency/locking, or process-group containment. Section 8.3 correctly notes startup effects, while §17.3 leaves it open whether MCP servers share the Bash boundary. The MCP specification confirms that tool annotations are untrusted hints ([MCP ToolAnnotations](https://modelcontextprotocol.io/specification/2025-11-25/schema#toolannotations)).

**Impact:** A tool may be project-read-only while its server mutates undeclared host state, accesses the network, inherits credentials, spawns descendants, or corrupts a shared index. Tool-level permission does not contain server startup behavior.

**Bounded correction:** Make a registry entry admissible only when it binds:

- reviewed tool semantics and negative tests;
- exact transport, executable/config/dependency provenance;
- scrubbed environment and credential requirements;
- process filesystem/network/resource boundary;
- declared internal-state roots and lock/recovery behavior;
- reviewer, evidence grade, expiry, and invalidation triggers.

Limit first-release `readonly` to explicitly reviewed local bundles; keep remote/generic third-party MCP admission unavailable.

### POL-006 — High — Preflight overstates “effective policy” before runtime observation

**Proposal sections:** §§1, 6.1, 10, 13–14.

**Evidence/reasoning:** Revision 2 says the adapter reports the effective policy before paid launch. Yet it also acknowledges inherited managed controls and unresolved runtime behavior. Provider documentation states that `--settings` merges with other layers, array values concatenate across sources, managed settings outrank CLI settings, and `/status` lists active sources without identifying which source supplied each field. See [settings precedence](https://code.claude.com/docs/en/settings#settings-precedence) and [verify active settings](https://code.claude.com/docs/en/settings#verify-active-settings).

**Impact:** A preflight prediction may be recorded as established authority even though the runtime can only classify it as unknown or broader after startup. Startup itself may already initialize hooks or MCP servers and may incur paid execution.

**Bounded correction:** Use four explicit stages:

```text
requested -> compiled -> preflight-assessed -> runtime-observed
```

Reserve “effective” for runtime-observed evidence. `explain` should report compiled policy plus unresolved inherited controls. Strict profiles must refuse prelaunch when required sources cannot be assessed and terminate before accepting meaningful model/tool events if startup evidence contradicts the compilation.

### POL-007 — High — Resource and crash-recovery requirements lack minimum per-profile guarantees

**Proposal sections:** §§9.3, 12–14, 17.3.

**Evidence/reasoning:** Revision 2 requires resource classification but does not state which profiles require hard versus sampled limits. Section 13 says unknown enforcement fails closed for strict profiles, while §9.3 anticipates `unknown` where the OS cannot establish a hard limit. Crash recovery says the manager reconciles child processes, but a crashed manager cannot itself perform that work; no durable supervisor, lease, PID-reuse defense, or next-start recovery protocol is defined.

**Impact:** Implementers may either make strict profiles unusable or silently treat sampled limits as sufficient. Unattended runs can leave paid or mutating descendants alive after manager failure.

**Bounded correction:** Define per-profile minimums. Before unattended activation require at least:

- aggregate run admission;
- process-group ownership and bounded termination;
- wall-time limit;
- log/output cap;
- orphan detection;
- durable attempt journal;
- idempotent next-start recovery with PID/start-time validation.

Memory may remain sampled where macOS cannot provide a reliable hard limit, but that limitation must be an explicit profile decision. Keep `implementation-auto` unavailable until recovery tests pass.

### POL-008 — High — Path and operation semantics remain nondeterministic

**Proposal sections:** §§7.1–7.3, 14.1, 17.3.

**Evidence/reasoning:** The policy defines only `read` and `write` without stating whether write includes create, truncate, delete, rename, chmod, xattr, link, and directory mutation. Preflight must “identify” overlaps, mounts, and hard links but does not specify accept/reject outcomes. Writable-root symlink checks do not address path replacement after preflight, untrusted writable parents, output materialization races, or aliases created through mounts and hard links.

**Impact:** Two conforming implementations can resolve the same policy differently. Preflight validation can be invalidated before access or materialization.

**Bounded correction:** Specify operation semantics and deterministic overlap outcomes. Reject ambiguous writable aliases and writable roots beneath untrusted parent chains. Require race-resistant manager writes (`openat`/no-follow or platform equivalent), revalidation at materialization, and post-run reconciliation. Label mount/hard-link checks as enforcement or detection; do not leave them as generic threat-model items.

### POL-009 — High — The executable-review contract does not cover common test workflows

**Proposal sections:** §§7.4, 9.1, 14–15.

**Evidence/reasoning:** `verified-review` grants only scratch writes, but tests and analyzers commonly require a project working directory and create repository-local caches, build directories, coverage files, databases, sockets, or lockfiles. The proposal does not define command working directory, environment allowlist, timeout, stdin, expected output roots, or behavior when a tool cannot redirect project-local generated state.

**Impact:** The profile may be secure but unusable, or implementations may silently broaden project writes to make tests pass.

**Bounded correction:** Define command-template fields for argv, cwd scope, environment keys, timeout, expected write roots, and output limits. `explain` should report incompatibility before launch. First-release support may be limited to manager-executed diagnostics and runners proven to redirect generated state to scratch.

### POL-010 — Medium — “Content-free telemetry” still permits linkable or identifying metadata

**Proposal sections:** §§7.3, 10, 12, 14.1.

**Evidence/reasoning:** The proposal excludes raw paths and content, but policy, artifact, configuration, and executable hashes may fingerprint known projects, software, or artifacts across runs. “Minimum” private-state retention has no duration, access-control, deletion, or export contract.

**Impact:** Cross-project telemetry can become a correlation surface, and private recovery state can persist longer than intended.

**Bounded correction:** Define an explicit cross-project field allowlist; use keyed, domain-separated pseudonyms rather than raw content hashes where correlation is unnecessary; prohibit artifact hashes from cross-project export; and specify private-state retention, permissions, inspection, and deletion. Telemetry export should remain disabled until this schema is tested.

### POL-011 — Medium — Supersession is helpful but not requirement-complete

**Proposal sections:** §5, §§12, 14–15.

**Evidence/reasoning:** Section 5 maps broad historical sections, but a replacement plan could still lose narrower retained requirements: alias retention for a documented release cycle, independent materialization of every successful attempt, rejection of meaningful pre-init events, exact Git-control reconciliation, and explicit no-rollback behavior. Some are present indirectly; none have stable requirement IDs.

**Impact:** Future maintainers must reconstruct obligations by diffing historical prose and the corrective plan.

**Bounded correction:** Add a requirement ledger with stable IDs and dispositions: `retained`, `superseded`, `deferred`, or `retired`, each pointing to the new normative section and required test. Include all historical verification obligations that remain active.

### POL-012 — Medium — “First release” is not a defined activation cohort

**Proposal sections:** §§3, 7.4, 14–15, 17.3.

**Evidence/reasoning:** The proposal retains five profiles but leaves direct artifact writes, MCP containment, resource enforcement, and implementation path semantics open. It does not state whether all five must activate together.

**Impact:** Planning can either expand into a large platform project or expose incomplete profiles prematurely.

**Bounded correction:** Separate:

1. non-activating schema/compiler/`explain`;
2. source-only review;
3. manager-materialized artifact review;
4. executable review;
5. interactive implementation;
6. unattended implementation;
7. advanced custom/host-read policies.

Gate each independently. Defer interactive and unattended implementation until POL-001, POL-003, and POL-007 are resolved and probed.

## First-release blockers versus later improvements

### Must be resolved before implementation planning is approved

- POL-002: normative schema and precedence;
- POL-004: authorization/status correction;
- POL-011: requirement-level lineage;
- POL-012: explicit release cohort.

### Must be resolved before affected profiles activate

- POL-001: filesystem enforcement;
- POL-003: effect-expanding resume;
- POL-005: MCP process trust;
- POL-006: preflight/runtime evidence stages;
- POL-007: resource and recovery minimums;
- POL-008: deterministic path semantics;
- POL-009: executable-review command contract;
- POL-010: telemetry schema, if telemetry export is enabled.

### Appropriate later improvements

- direct worker artifact writes beyond manager materialization;
- remote or third-party MCP registries;
- host-wide read policies;
- native Linux activation and a separate portability matrix;
- multiple artifact outputs and richer policy-diff UI;
- non-Git implementation profiles;
- advanced credential-masking and controlled network workflows;
- configurable direct-write custom policies after the standard presets are proven.

## Missing workflow and edge-case matrix

| Workflow/setup | Revision 2 coverage | Material gap | Recommended disposition |
|---|---|---|---|
| Strict source review | Named preset and declared roots | Built-in read confinement is best-effort | Block activation; stage sources or use sandboxed reads |
| Review with external handoff | Named external roots | Alias, confidentiality, and parent-ownership semantics | First release after path fixtures |
| Executable review | Scratch writes and command capability | Cwd, repo-local outputs, env, timeout undefined | Gate per supported runner |
| Durable artifact review | Manager materialization default | Multiple artifacts, overwrite/recovery semantics incomplete | Single artifact first release |
| Interactive implementation | Owned project paths | Bash write enforcement versus reconciliation unclear | Defer until enforcement probe |
| Unattended implementation | Transition acknowledgement and auto mode | Orphan recovery and prompt-injection transition risk | Defer |
| Advanced custom/host reads | Warning and confirmation | Sensitive-path completeness impossible to guarantee | Later, explicitly experimental |
| Non-Git project/document set | Read profiles generally fit | Implementation assumes Git reconciliation | Read-only supported; implementation deferred |
| Linked worktree/submodule | Mentioned in path tests | Shared `.git`, nested roots, submodule controls undefined | Add explicit fixtures before implementation |
| Local MCP with persistent index | Internal-state roots recognized | Locks, corruption, concurrency, recovery unspecified | Admit only reviewed bundle |
| Remote MCP | Generic modes imply possibility | Transport, credentials, open-world containment absent | Unavailable first release |
| Managed enterprise settings | Provenance required | Field-level effective source may remain unknowable | Strict profiles fail closed |
| Required project plugin/hook/skill | Disabled or unresolved | Task may depend on disabled runtime behavior | `explain` incompatibility, no silent enable |
| Parallel delegated runs | Aggregate concurrency named | Root overlap, MCP state locking, artifact collision unresolved | Serialize until lock contract exists |
| Resume after upgrade | Semantic diff intended | Schema migration and contaminated-context risks | Exact/narrower only first release |
| Manager crash after child launch | Partial recovery prose | No durable reaper/lease protocol | Block unattended activation |
| Linux | Next target | Dependencies and semantics differ from macOS | Separate post-macOS matrix |

## Epistemic and auditability assessment

### Strong

- The evidence map distinguishes observed, reported, and inferred claims.
- The runtime probe accurately limits its conclusion to startup exposure and early termination.
- Fake-CLI behavior is not promoted to runtime enforcement.
- Resource sampling is not mislabeled as quota enforcement.
- Historical documents remain intact and linked.

### Needs correction

1. **“Effective before launch” is an inference presented as an attainable fact.** The proposal should say compiled or preflight-assessed until runtime observation.
2. **`permission-allowed` requires an evidence source.** Adapter-generated rules, provider startup output, denied-call observation, and successful calls are different grades.
3. **`mcp-readonly` is a reviewed classification, not an observed property.** Each registry record needs its evidence grade and severe check.
4. **Approval state is conflated with policy status.** Stakeholder decisions, reviewer recommendations, and implementation authority must be separate.
5. **Provider documentation is reported evidence.** Current official documentation clarifies intended behavior but does not prove Claude Code `2.1.215` enforced it in the parked run.
6. **Source silence must remain silence.** The incomplete probe did not address filesystem, network, MCP callability, caching, or materialization.

## Proposed finding-disposition checklist

- [ ] **POL-001:** accept / revise / park / reject — choose a realizable first-release filesystem enforcement strategy.
- [ ] **POL-002:** accept / revise / park / reject — add the normative schema and preset extensibility matrix.
- [ ] **POL-003:** accept / revise / park / reject — decide whether first-release effect-expanding resume is prohibited.
- [ ] **POL-004:** accept / revise / park / reject — reconcile approval and authorization states.
- [ ] **POL-005:** accept / revise / park / reject — define MCP registry governance and process containment.
- [ ] **POL-006:** accept / revise / park / reject — rename and stage preflight/effective evidence.
- [ ] **POL-007:** accept / revise / park / reject — set per-profile resource and recovery minimums.
- [ ] **POL-008:** accept / revise / park / reject — make operation, overlap, and race semantics normative.
- [ ] **POL-009:** accept / revise / park / reject — define supported executable-review command contracts.
- [ ] **POL-010:** accept / revise / park / reject — define telemetry pseudonymization and retention.
- [ ] **POL-011:** accept / revise / park / reject — add stable historical requirement lineage.
- [ ] **POL-012:** accept / revise / park / reject — approve a staged first-release profile cohort.
- [ ] Issue revision 3 with a new target hash.
- [ ] Have the reviewer audit accepted corrections before implementation planning.
- [ ] Keep all runtime probes separately authorized.

## Verification performed

- Read the required sources in the supplied order:
  1. revision-2 proposal;
  2. historical proposal;
  3. historical corrective execution record;
  4. runtime probe;
  5. bounded candidate inspection;
  6. `README.md`, `CONTRACT.md`, `EPISTEMICS.md`, and the prior cold-review artifact.
- Used the repository knowledge graph for candidate symbol discovery, then inspected exact candidate source where line-precise evidence was needed.
- Inspected current official Anthropic documentation for sandbox, permission, and settings-layer semantics, and the MCP schema for annotation trust.
- Ran `git status --short`; the worktree was already dirty and the proposal tree was untracked.
- Ran `git diff --check`; it returned success with no whitespace errors.
- Recorded target SHA-256: `477ba42cef52a93414c219b865e44fc5bb637280792b7d168574b116b5fdc28d`.
- No files were edited. No tests, installations, downloads, paid calls, runtime probes, commits, staging operations, or configuration changes were performed.

## Limitations

- The review did not execute the uninstalled candidate or reproduce its 195-test result.
- Provider documentation was inspected as reported primary evidence; no runtime semantics were inferred from documentation alone.
- The parked probe did not reach a model or tool turn, so its negative-effect observations establish only early termination.
- No Linux, Windows/WSL, remote MCP, enterprise-managed-policy, or crash-recovery runtime was tested.
- Conclusions apply to revision 2 at the recorded hash; later edits require a new review disposition.

## Root disposition — 2026-07-20

**Disposition scope:** Reviewer findings against target revision 2. These dispositions preserve
the reviewer text above and incorporate subsequent stakeholder decisions. They authorize proposal
revision and planning only, not code changes or runtime activation.

| Finding | Disposition | Root rationale and revision-3 action |
|---|---|---|
| POL-001 | **Revise** | Accept the need for a profile × operation/tool-family enforcement matrix and honest assurance labels. Reject staging all sources or disabling built-in readers as the standard workflow. Standard profiles use Claude permissions for built-in tools, the native OS sandbox for Bash, and reconciliation for detection; a later high-isolation mode may stage sources. |
| POL-002 | **Accept** | Add a normative core schema, defaults, partial order, hard-boundary behavior, preset extensibility, warning/confirmation policy, compiler target, and evidence state. Unsupported activation dimensions remain explicit `unavailable`. |
| POL-003 | **Revise** | Accept the prompt-injection and confused-deputy risk. Reject a categorical prohibition on broader or mixed resumes: the stakeholder requires them to remain available. Add independently configurable profile, cache, authority, context, runtime, and sandbox notices; allow each notice and confirmation to be disabled by operator-owned configuration; always retain the transition audit record. |
| POL-004 | **Accept** | Distinguish approved direction, review verdict, root dispositions, implementation-plan authority, execution authority, and activation authority. |
| POL-005 | **Accept** | Define registry governance, provenance, environment, process boundary, state roots, locking, expiry, and invalidation. Keep remote/generic third-party MCP unavailable in the first activation cohort. |
| POL-006 | **Accept** | Use `requested`, `compiled`, `preflight-assessed`, and `runtime-observed`; reserve `effective` for a conclusion supported by runtime evidence. |
| POL-007 | **Accept** | Define minimum resource/recovery guarantees by cohort. Do not claim a hard memory ceiling when macOS supplies only sampled guardrails. Keep unattended activation gated on durable recovery tests. |
| POL-008 | **Accept** | Define write operations, path precedence, overlap outcomes, alias/race handling, revalidation, and enforcement-versus-detection labels. |
| POL-009 | **Accept** | Add command-template fields for argv, cwd, environment, timeout, stdin, expected writes, output limits, and sandbox disposition. Detect incompatible runners before a paid call. |
| POL-010 | **Accept** | Add an explicit telemetry allowlist, prohibit raw cross-project hashes where linkability is unnecessary, do not conflate the current 30-day Codex session-log policy with adapter run-state retention, and keep export disabled until both schemas are tested. |
| POL-011 | **Accept** | Add stable requirement IDs and a retained/superseded/deferred/retired ledger tied to tests and activation cohorts. |
| POL-012 | **Accept** | Split activation into independently gated cohorts. The first implementation plan covers only the non-activating schema/compiler/`explain` core. |

**Overall root disposition:** **Revise proposal.** Issue revision 3, write a bounded
non-activating contract-core implementation plan, then request a correction audit before executing
that plan. No paid probe is authorized by this disposition.
