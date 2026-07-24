# Cold-read review — cross-runtime routing and Codex-managed Claude delegation

- **Date:** 2026-07-17
- **Reviewer role:** independent, read-only cold reader
- **Review target:** the proposed Codex `delegate-to-claude` adapter and its implementation handoff
- **Verdict:** **revise** — preserve the architecture and gates, but resolve the five MAJOR contract gaps below before implementation planning is approved.

## Scope and sources checked

Reviewed, in the requested order: `CLAUDE.md`; `README.md`; `ROADMAP.md`; the proposal;
the handoff; `CONTRACT.md`; `ROUTES.md`; `STATE.md`; `WARRANTS.md`; `EPISTEMICS.md`; `SKILL.md`;
`LINEAGE.md`; `adapters/codex/README.md`; `adapters/codex/AGENTS-fragment.template`; `install.py`;
and SEAS ADR-0024.

This review covers architecture, canonicality, route/warrant discipline, telemetry reconstruction,
recovery, policy activation, and phase boundaries. It does not re-evaluate vendor capabilities or
run Claude/external model calls. The proposal and handoff remain planning artifacts only.

## Finding summary

| Severity | Count |
|---|---:|
| BLOCKER | 0 |
| MAJOR | 5 |
| MINOR | 2 |
| NOTE | 2 |

## Findings

### BLOCKER

None.

### MAJOR

#### MAJOR — declared ownership is not an enforceable concurrent-write boundary

**Location:** proposal §7.3 “Ownership and concurrency”; §13 Phase 3 exit.

**Impact:** The manager only rejects *declared* overlapping write sets. A Claude process that is
given a repository-capable tool can still write an undeclared path, escape a declared subtree by a
symlink or ancestor path, or modify the shared checkout while another lane is running. Separate
worktrees isolate copies, but do not enforce an allowlist inside a worktree. Thus the proposed
“cannot overlap writes” Phase 3 exit cannot be demonstrated from the current contract, and the
packet's no-broaden guarantee is presently advisory.

**Bounded correction:** Define a `write_isolation` field with only testable modes: `read_only`,
`dedicated_worktree`, or an explicitly capability-probed filesystem allowlist. Canonicalize paths,
reject ancestor/descendant and symlink collisions, launch writers only in a dedicated worktree, and
declare direct shared-checkout writers unsupported in concurrent mode. Make the Phase 3 fake-CLI
fixture attempt an undeclared write and require it to be rejected or contained before its exit
criterion can pass.

#### MAJOR — budget and timeout are described as fail-safe although their enforcement is undefined

**Location:** proposal §6.3 “Codex adapter components”; §7.1 “Task packet”; §8.4 “Polling and
timeout”; §9 “Permissions, spending, and recovery”; §13 Phases 2–3.

**Impact:** Packets require a budget and timeout policy, but the proposal does not specify which
provider/CLI control hard-enforces either one or what happens when it is absent. At the same time,
timeouts must not terminate a healthy process and termination is deferred to a separate explicit
action. A terminal `timed_out` result can therefore coexist with a still-spending child process.
That is neither a bounded timeout nor an independently budgeted Option 3 lane.

**Bounded correction:** Split the fields into `hard_spend_limit`, `hard_runtime_limit`, and
`observation_deadline`, each marked `enforced`, `advisory`, or `unavailable` with a capability
probe/evidence locator. Do not launch a packet that requires a hard limit unless the corresponding
control is proven available; otherwise require explicit operator acceptance of advisory exposure.
Define `timed_out_waiting` as non-terminal while the process lives, reserve `timed_out` for a
verified terminal process, and test the state transitions with the fake CLI.

#### MAJOR — the event/registry contract cannot yet prove planned, requested, and observed routes

**Location:** proposal §6.2 “Provider/runtime overlays”; §7.1 “Task packet”; §7.2 “Result
envelope”; §8.1 “Session registry”; §11.1 “Content-free event”; §16 “Design falsifiers”.

**Impact:** Recording three values is not sufficient to reconstruct their authority. The packet
has a cited route/W-ID and requested controls, while the registry has a packet hash and requested
controls; neither contract requires the selected source snapshots/hashes, all applied overlays,
the exact control-to-CLI mapping version, an observation status/source for delivered values, or an
immutable link from the terminal envelope to the orchestrator disposition. A worker could report
an “observed” value that was not emitted by structured output, and a mutable canonical checkout
could make an old route decision unrecoverable. This fails the stated 10-run reconstruction
falsifier without needing any content-bearing telemetry.

**Bounded correction:** Add a versioned route-decision record referenced by packet, registry,
event, envelope, and disposition. It should include hashes/commit IDs for `ROUTES.md`, `STATE.md`,
and any project overlay; profile and fallback resolution; requested-control mapping version; and
per delivered field `{value, status: observed|unobserved|conflicted, evidence_locator_or_hash}`.
Add a monotonic lifecycle/disposition ID and require one durable terminal reconciliation record;
store only opaque locators/hashes in the content-free event. Test successful, absent, conflicting,
resume, and crash-before-disposition cases.

#### MAJOR — Option 2's required manifest is mentioned but not part of the common contract

**Location:** proposal §5 “Option decision,” especially “Recommendation and compatibility”; §7.1
“Task packet”; §7.2 “Result envelope”; §13 Phase 5.

**Impact:** The proposal calls Option 2 migration-compatible and says a descendant manifest must
be declared, yet it does not define the manifest's required identity, lineage, per-descendant route
observation, ownership, permission, budget, timeout, and terminal-disposition fields—or how its
records map into the parent envelope/event. Option 2 will otherwise collapse precisely the
per-worker provenance and controls for which Option 3 is selected, creating a second opaque
control plane and a later incompatible migration.

**Bounded correction:** Define a normative `descendant_manifest` schema now, even if its
implementation remains Phase 5. Require the parent packet to declare a maximum depth and aggregate
limits; require the parent result envelope to include a manifest digest, completeness state, and
per-descendant opaque IDs; and make a missing/incomplete manifest a failed or non-comparable lane.
Use the same route-decision and terminal-disposition identifiers as Option 3.

#### MAJOR — “platform-agnostic core” and provider-specific route ownership are internally unclear

**Location:** proposal §1 “Decision requested”; §6 diagram and §6.1 “Shared core”; §6.2
“Provider/runtime overlays”; §10.1 “One source, generated adapters.”

**Impact:** The diagram places `ROUTES` and `STATE` in the platform-agnostic core, while §6.2 says
model identifiers, effort controls, and provider-specific facts belong to adapters. The existing
canonical `ROUTES.md`, `STATE.md`, and warrants contain Claude-specific model, effort, pricing,
and availability facts. Without an explicit interpretation, an implementer can either create an
unauthorized second route catalog in the Codex adapter or incorrectly move existing canonical
Claude policy out of the ADR-0024 home. Either choice weakens the stated one-source discipline.

**Bounded correction:** State that, for this proposal, “platform-agnostic” means **host-runtime
agnostic for the same Claude routing doctrine**: Codex and Claude Code consume the existing
canonical Claude route surfaces. Reserve provider-neutral doctrine for `CONTRACT.md`,
`EPISTEMICS.md`, and the schema vocabulary. Treat a true multi-provider route-overlay split as a
separate, reviewed migration with source ownership, versioning, warrant mapping, and same-pass
propagation rules; do not create it in Phase 1.

### MINOR

#### MINOR — the capability claim overstates what help-text observation licenses

**Location:** proposal §2 “Source map and claim labels,” row beginning “Locally observed Claude
Code 2.1.212 exposes …”.

**Impact:** `EPISTEMICS.md` reserves **Corroborated** for a claim that survived a severe check.
Version/help output can establish that a particular binary advertises flags, but it cannot establish
their runtime semantics, authentication behavior, budget enforcement, or structured-output field
availability. The current label may let implementation treat planned controls as observed facts.

**Bounded correction:** Split the row: label the dated binary/version and advertised flags
**Concordant**; label each runtime behavior `Unchecked` until a non-generative capability probe or
fake-CLI contract test establishes the relevant adapter behavior; retain a dated capability matrix
with probe method, result, version, and expiry/re-check trigger.

#### MINOR — `project` is not necessarily content-free or privacy-minimal

**Location:** proposal §11.1 “Content-free event”; §12 “Generated-state and privacy boundary.”

**Impact:** An unconstrained project identifier can be a repository path, customer name, or
otherwise sensitive execution context. It would not be prompt text, but it can still violate the
privacy intent and make a shared local evidence store more revealing than needed.

**Bounded correction:** Specify an opaque, salted `project_id` and a local-only mapping outside
the routing event store; prohibit paths, repository names, branch names, artifact names, and free
text in all event identifier fields. Add schema rejection tests for those fields.

### NOTE

#### NOTE — Phase 1 is testable but not yet a small vertical slice

**Location:** proposal §13 “Phase 1 — contracts and dry-run tooling.”

**Impact:** Schema work, a new skill, manager commands, installation drift/stamps, size-cap
behavior, and deterministic tests span several independently risky contracts. Combining them
makes a Phase 1 failure hard to localize and invites installer changes before the route-decision
contract is settled.

**Bounded correction:** Keep the Phase 1 exit, but sequence it as (1) pure packet/route-decision
validation and fixtures, (2) a read-only `plan --dry-run` that consumes only those objects, then
(3) installer/stamp support after the plan output is stable. No live process management is needed
for any of the three sub-slices.

#### NOTE — generated-state retention is correctly open but needs an approval gate in the plan

**Location:** proposal §12 “Generated-state and privacy boundary”; §16 “Stakeholder decisions
still needed before implementation”; handoff “Current open decisions.”

**Impact:** The proposal correctly refuses to invent a permanent state root or sub-budget, but
Phase 1 names size-cap tests before those values are chosen. An implementation could silently pick
a user-specific default and make the choice de facto policy.

**Bounded correction:** Make an approved state-root/sub-budget configuration a precondition for
any command that writes generated state. Until then, limit Phase 1 to in-memory or temporary test
fixtures and configuration validation that fails closed without explicit values.

## Strengths and adversarial checks that passed

- **ADR-0024 canonicality:** The proposal keeps the dedicated repository as canonical and rejects
  a second central package or copied Codex routes. This accords with ADR-0024 Decision 1 and
  `LINEAGE.md`.
- **Route/warrant discipline:** §10.3 retains same-pass affected-surface, warrant/flip counter,
  probe record, and index updates; §11.2 keeps events as evidence rather than direct policy
  mutation. This preserves `CONTRACT.md` §6 and W-019's no-single-observation rule.
- **No silent activation:** §§10.2–10.3 clearly separate invoked update notification from install,
  profile, route, and policy activation; the stated no-network first slice is appropriately narrow.
- **Cache and recovery claims:** §§8–9 promise eligibility, never a cache hit; preserve partial
  evidence; and prohibit automatic paid retries. These are correctly conservative.
- **Initial test gate:** Phases 1–2 prohibit model calls and require fake-CLI exercises before any
  real paid smoke test. The handoff also preserves the unrelated probe record and blocks execution
  before authorization.

## Assumptions and open questions

### Assumptions used for this review

- ADR-0024 remains the controlling canonical-home decision; no later federation decision was
  supplied.
- The existing Codex adapter is consumer guidance only, as its template and current installer show.
- No live Claude capability was verified in this review; the §2 CLI observation is treated as
  dated help-text evidence only.
- Content-bearing stdout, stderr, and debug artifacts may remain local under §12 controls, but
  they are outside the content-free routing-event plane.

### Open questions to retain for stakeholder decision

1. Which execution environment can genuinely enforce read-only and dedicated-worktree boundaries
   for a Claude CLI lane, including symlink/path-escape handling?
2. Which CLI controls, if any, provide hard spend and runtime limits, and what observation proves
   that those limits applied to an individual run?
3. What approved user-level state root, retention rules, and metadata/debug sub-budgets apply
   within the campaign cap?
4. Is Option 2 required in the first public milestone after its manifest is specified, or should
   it remain deferred through Phase 4?

## Verification performed

- Read all required sources in the supplied order, including ADR-0024.
- Inspected `git status --short`, the exact README and pre-existing probe-record diffs, and the
  proposal/handoff line-numbered content.
- Ran `python3 check_state.py` — `checked 9 dated entries, 1 exempt (no date), as of 2026-07-17:
  OK`; `python3 check_wids.py` — `51 md files · 23 W-records defined · 23 cited: OK`; and
  `git diff --check` — no whitespace errors.
- Confirmed this reviewer did not edit the proposal, handoff, README, adapter, installer, routing
  surfaces, or the pre-existing probe record.

## Final disposition

**Revise.** The canonicality, no-silent-activation, evidence, and recovery direction should be
retained. Before implementation planning, make isolation and spend/time controls enforceable;
make route/lineage/disposition provenance reconstructible; define the Option 2 manifest contract;
and clarify that the existing canonical Claude route surfaces are shared across host runtimes rather
than silently split into a second provider overlay.


## Post-revision audit — 2026-07-17

**Scope:** Re-read the revised proposal and handoff against every original finding above. This
audit assesses the design documents only; it does not validate a future CLI implementation or run
an external model.

### Original-finding disposition

| Original finding | Status | Revised location and basis |
|---|---|---|
| MAJOR — declared ownership is not an enforceable concurrent-write boundary | **resolved** | Proposal §7.3 now defines only `read_only`, `dedicated_worktree`, and capability-probed `filesystem_allowlist`; it canonicalizes/rejects aliases and overlaps, uses whole-worktree diff validation, and §13 Phase 3 requires undeclared-write containment/rejection fixtures. |
| MAJOR — budget and timeout enforcement undefined | **resolved** | Proposal §7.1 carries classified hard/advisory/unavailable controls; §8.4 distinguishes hard spend, hard runtime, and observation deadline; §9 makes unsupported hard limits fail closed and requires state-machine fixtures. See the new contradiction below for the remaining termination wording. |
| MAJOR — route/registry/event cannot prove planned, requested, and observed route | **resolved** | Proposal §7.2 adds one immutable, versioned route-decision record with route/STATE/overlay provenance, delivered-field observation status/evidence, lifecycle, and terminal reconciliation; §11.1 carries opaque route-decision/lifecycle/reconciliation identifiers. |
| MAJOR — Option 2 manifest absent from the common contract | **resolved** | Proposal §7.4 makes the descendant manifest normative now, specifies parent aggregate constraints and per-child identifiers, and treats missing/incomplete data as failed or non-comparable; §13 Phase 5 consumes that contract. |
| MAJOR — platform-agnostic core versus provider route ownership unclear | **resolved** | Proposal §1, §6.1, §6.2, and §16.3 explicitly retain one canonical Claude doctrine across host runtimes, prohibit a second Claude catalog, and defer a true provider-neutral split. |
| MINOR — help-text claim overstated its epistemic label | **partially resolved** | Proposal §2 correctly changes the advertised-flags claim to Concordant and adds an Unchecked runtime-semantics claim; §6.3 adds a dated capability matrix. However, §2 still permits a “fake-CLI contract test” as an alternative before relying on a behavior. Such a test proves adapter handling, not the real Claude CLI's semantics; the wording should require an actual dated capability observation for real-control reliance, with fake CLI limited to adapter-contract coverage. |
| MINOR — project identifier not privacy-minimal | **resolved** | Proposal §11.1 requires opaque salted project IDs, rejects names/paths/free text, and confines the mapping to separate access-controlled local state. |
| NOTE — Phase 1 too broad for a vertical slice | **resolved** | Proposal §13 divides Phase 1 into schemas/fixtures, read-only dry-run, then skill/installer work, each with a narrower dependency boundary. |
| NOTE — generated-state decision could be silently made by implementation | **resolved** | Proposal §13 requires in-memory or test-runner-owned fixtures and fails closed for persistent generated state until explicit state-root/sub-budget approval. |

### New finding

#### MAJOR — hard-runtime semantics conflict with the no-timeout-termination rule

**Location:** proposal §6.3 “Codex adapter components” says destructive termination is a separate
explicit operator action and “never a timeout side effect”; proposal §8.4 “Polling and timeout”
defines `hard_runtime_limit` as manager/runtime enforcement that makes the child terminal and says
`timed_out` follows because that hard-runtime mechanism fired.

**Impact:** The design does not say whether a manager may automatically kill a child at a
pre-authorized hard runtime limit. Both readings are consequential: a manager implementation may
silently terminate a paid review contrary to §6.3, or it may never enforce the promised hard limit.
The packet, capability matrix, and terminal-state tests cannot implement one consistent behavior
until this is decided.

**Bounded correction:** Choose and name the two semantics. Either (a) permit a
packet-authorized, capability-probed `hard_runtime_limit` to terminate the child and revise §6.3 to
say this is the sole exception to manual termination, or (b) reserve “hard runtime” for a
provider-side self-terminating ceiling and rename any manager deadline to `observation_deadline`.
In both cases, specify the emitted terminal reason and test that operator termination, provider
self-termination, and parent observation expiry are distinct states.

### Final recommendation

**Revise.** Eight original findings are resolved and one is partially resolved. No BLOCKER was
found, but the new MAJOR termination-semantics contradiction and the remaining capability-evidence
wording should be corrected before an implementation-authorization decision.

### Verification

- `python3 check_state.py` — `checked 9 dated entries, 1 exempt (no date), as of 2026-07-17: OK`.
- `python3 check_wids.py` — `51 md files · 23 W-records defined · 23 cited: OK`.
- `git diff --check` and an untracked-artifact `git diff --check --no-index` — no whitespace
  errors.


### Final correction audit

**Scope:** Latest edits to proposal §§2, 6.3, 8.4, and 9 plus the aligned handoff wording only.

- **Fake-CLI versus actual-runtime evidence — resolved.** Proposal §2 now says real-control
  reliance requires dated actual-runtime evidence and fake-CLI tests establish adapter handling
  only. Proposal §6.3 requires an actual-runtime probe in the capability matrix, and §9 repeats
  that fake fixtures cannot establish real-limit enforcement. The handoff “Decisions already
  proposed” carries the same distinction.
- **Termination semantics — resolved.** Proposal §6.3 names an operator-pre-authorized,
  capability-probed hard_runtime_limit as the sole automatic-termination exception. Proposal
  §8.4 distinguishes provider-limit, manager-limit, observation-deadline, and interactive
  termination terminal states; §9 requires fixtures for each. The handoff states the same
  packet-authorized manager-limit boundary.
- **New contradictions:** no new BLOCKER or MAJOR contradiction found in the requested narrow
  surface.

**Effective final recommendation:** **accept for implementation-authorization decision**. This
accepts the proposal as an authorization decision boundary only; actual-runtime capability evidence,
state-root/sub-budget approval, and any paid smoke test remain the proposal's explicit gates.

**Verification:** `python3 check_state.py` OK; `python3 check_wids.py` OK (23 defined / 23
cited); `git diff --check` and the untracked-artifact whitespace check reported no errors.
