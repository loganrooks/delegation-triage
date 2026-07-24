# Capability-Based Claude Profiles Corrective Implementation Plan

> **Historical plan:** This plan records the work that produced and corrected the uninstalled
> version-3 candidate. It is not authority for further implementation. Future work must follow the
> [composable capability and scope policy proposal](../../proposals/2026-07-20-composable-claude-capability-and-scope-policy.md)
> and a new implementation plan approved against that proposal. The completed and incomplete
> checkboxes below are preserved as historical execution evidence.

> **For the delegated implementer:** Execute this plan test-first. Do not edit this plan or any
> other Markdown, proposal, skill, README, probe, manifest, or deployment file. Do not commit.

**Goal:** Correct and complete the uninstalled capability-profile candidate by using Claude Code's
native sandbox, argument-declared scratch roots, immediate manifest enforcement, aggregate state
accounting, and owned-path reconciliation.

**Architecture:** Keep profile resolution pure. Add small standard-library modules for runtime
policy, state accounting, and worktree reconciliation; keep process/session orchestration in the
manager. Claude Code supplies OS-level Bash isolation. The adapter supplies exact tool authority,
settings generation, fail-closed startup checks, scratch lifecycle, result preservation, and
post-run ownership reconciliation.

**Technology:** Python 3.12+ standard library, `unittest`, Git CLI, Claude Code CLI. No package
installation, network access, third-party Python dependency, or actual paid-runtime probe.

---

## Status and boundaries

This plan supersedes `2026-07-19-capability-based-claude-profiles.md`. Its first worker produced an
uninstalled candidate with 47 passing tests. Root review dispositioned that result as `revise`.
Preserve useful candidate behavior and add regression coverage before changing it.

The candidate is not deployed. Profile contract version becomes `2`; a version-1 profiled session
must not resume under the new boundary, but successful legacy attempts remain inspectable and
materializable.

### Worker-owned write set

- Modify: `.github/workflows/ci.yml`
- Modify: `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
- Modify: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/__init__.py`
- Modify: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/profiles.py`
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/runtime_policy.py`
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/state_budget.py`
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/reconcile.py`
- Modify: `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`
- Modify: `adapters/codex/delegate-to-claude/tests/test_profiles.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_runtime_policy.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_state_budget.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_reconcile.py`

Any other write is a scope failure. Existing dirty README, proposal, plan, and probe files belong to
the root or user. Do not format, restore, stage, or report them as worker changes.

### Non-authorities

- no installation or deployment to `.codex`, `.claude`, Cowork, or another consumer;
- no commit, staging, push, branch, worktree creation, or destructive Git operation;
- no network, download, package-manager operation, monitoring service, or background daemon;
- no descendant agent or paid Claude invocation;
- no user-facing prose edits.

---

## Locked contract

1. Claude Code's native sandbox is the Bash isolation mechanism; the adapter does not implement a
   second OS sandbox.
2. `strict-readonly`, `verified-review`, and `artifact-review` fail on broader or unknown startup
   manifests before accepting assistant or tool events.
3. `verified-review` and `artifact-review` execute Claude from one declared scratch directory and
   attach the project as a read root. Write, Edit, and NotebookEdit remain denied.
4. `--scratch-dir` selects the scratch root. When omitted, use a run-local directory under managed
   state. The selected root may be a dedicated workspace directory or an external directory.
5. `artifact-review` uses manager materialization to one required `--artifact-output`; the worker
   receives no built-in file-write tool.
6. `implementation` and `implementation-auto` require repeated `--owned-path` declarations and
   reconcile final Git-visible changes against the baseline. Unexpected changes fail and remain
   untouched for root disposition.
7. The default aggregate state ceiling is 240 MiB and the CLI rejects a configured value above
   240 MiB. Execution stops at a lower 192 MiB threshold; logs and manager-authorized scratch are
   accounted together.
8. Fake-CLI tests establish adapter logic only. They do not label Claude's effective native
   sandbox as proven.

---

## Task 1: Freeze the candidate and add root-review regressions

**Files:** existing adapter tests only.

- [ ] **Step 1: Run the candidate suite unchanged**

```bash
PYTHONPATH=adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest discover \
  -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

Expected baseline: 47 tests pass. If not, stop and report the mismatch.

- [ ] **Step 2: Add failing counterexample tests**

Add deterministic tests proving the current candidate is wrong for each case:

1. an explicitly allowed read-only MCP tool is expected rather than unexpected;
2. an init event without a `tools` list is `unknown` and fails a strict profile;
3. a broader init manifest terminates the fake process before it emits a result;
4. a successful legacy attempt without `materializable` can still be selected;
5. status and inspect include requested/canonical profile, version/hash, allowed tools, observed
   tools/MCP servers, manifest classification, unexpected tools, and materializability;
6. the exact command string accepted by a verified profile is not treated as filesystem
   enforcement;
7. a version-1 profiled run cannot resume under version 2 but remains materializable.

Extend the fake CLI with a bounded pause-after-init mode so immediate termination is observable
without races. Keep the ordinary fake path fast.

- [ ] **Step 3: Run the focused tests and capture RED**

Use the Task 1 command. Return the failing test names in the worker result.

---

## Task 2: Correct profile versioning, manifests, and audit output

**Files:** profile module, manager, and their existing tests.

- [ ] **Step 1: Implement profile contract version 2**

Bump `PROFILE_VERSION` to `2`. Deny both current `Agent` descendant rules and the older `Task`
identifier defensively. Keep the compatibility alias. Do not add a model route or installed
profile.

Normalize expected startup tools as:

- requested built-ins;
- explicitly allowed exact MCP identifiers;
- explicitly denied identifiers, recorded as exposed-but-denied rather than allowed;
- permission-rule specifiers such as `Bash(command)` normalized to their observed base tool only
  when the base tool is otherwise requested.

Record `match`, `narrower`, `broader`, or `unknown`, not only an unexpected-tool list.

- [ ] **Step 2: Enforce strict manifests at init time**

When a strict-profile init event arrives, compare immediately. For `broader` or `unknown`:

1. persist the observed event and failure reason;
2. terminate the child gracefully, then kill after a short bounded timeout if necessary;
3. drain bounded stderr;
4. do not accept a later result as successful or materializable;
5. return the documented manifest-violation code.

An absent init event is also `unknown`. A known empty tool list is distinct from an omitted list.

- [ ] **Step 3: Restore legacy materialization and complete sanitized output**

When `materializable` is absent, derive legacy eligibility from terminal status, zero exit, an
untruncated stream, and a successful result event. Never reinterpret an explicit false value.

Expose the profile and per-attempt evidence listed in Task 1 without exposing prompt bodies,
result text by default, raw tool output, authentication identity, or secrets.

- [ ] **Step 4: Run focused and full tests GREEN**

Use the Task 1 command. All old and new tests must pass before continuing.

---

## Task 3: Generate a fail-closed Claude native-sandbox policy

**Files:** create `runtime_policy.py`; modify manager, profiles, and tests.

- [ ] **Step 1: Write pure runtime-policy tests**

Test a pure builder that returns normalized settings data, CLI arguments, environment overrides,
and a SHA-256 policy hash. Cover strict, verified, artifact, implementation, and custom modes.

Verified and artifact policy must request:

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "autoAllowBashIfSandboxed": false,
    "allowUnsandboxedCommands": false,
    "excludedCommands": [],
    "network": {
      "allowedDomains": [],
      "deniedDomains": ["*"]
    }
  }
}
```

Write, Edit, NotebookEdit, WebFetch, WebSearch, and descendants remain denied through permissions.
Exact approved Bash commands remain under allowed tools; arbitrary sandboxed Bash is not
auto-approved.

- [ ] **Step 2: Add explicit MCP configuration**

Add repeated `--mcp-config` paths for profiled runs. Hash each declared configuration and pass
`--strict-mcp-config` so undeclared MCP sources are ignored. With no declared MCP configuration,
materialize an empty run-local MCP configuration. An explicitly allowed MCP tool without a
declared server configuration is a pre-launch error.

Do not store configuration contents in cross-project telemetry. Private run metadata may store
canonical paths and hashes, not credentials copied out of the source file.

- [ ] **Step 3: Materialize invocation-local settings**

Write normalized settings atomically under the run directory with mode `0600`; pass them through
`--settings`. Suppress user, project, and local settings sources where the installed CLI supports
that flag. Record the requested sandbox policy as `requested-unproven`; fake tests may not promote
it to effective or proven.

Managed settings can still exist outside adapter control. Preserve that uncertainty for the later
actual-runtime probe rather than claiming the local file replaced every settings layer.

- [ ] **Step 4: Test unavailable and conflicting capability preflight**

Extend the fake CLI doctor/help behavior. A profile requiring native sandboxing must fail before a
paid launch when required flags are absent or an eligibility/config probe errors. Auto mode must
also fail before launch when its non-generative configuration check is unavailable or unreadable.

- [ ] **Step 5: Run focused and full tests GREEN**

Use the Task 1 command.

---

## Task 4: Add declared scratch roots and aggregate state enforcement

**Files:** create `state_budget.py`; modify manager and tests.

- [ ] **Step 1: Write failing path and budget tests**

Cover:

- default run-local scratch;
- an explicit external scratch directory;
- an explicit workspace-local scratch directory;
- nonexistent leaf creation beneath an existing safe parent;
- symlink leaf or ancestor refusal;
- nonempty unowned scratch refusal;
- configured limits above 240 MiB refusal;
- new-run and resume preflight at the aggregate threshold;
- a shared stdout/stderr budget rather than two independent maxima;
- scratch growth causing bounded child termination;
- external scratch bytes included in accounting;
- state and scratch paths that overlap counted once.

- [ ] **Step 2: Implement scratch lifecycle**

For verified and artifact profiles:

1. resolve and validate `--scratch-dir`, or create `<run>/scratch`;
2. require an empty directory or the manager's matching ownership marker;
3. use mode `0700` for manager-created directories and `0600` for files;
4. launch Claude with scratch as process working directory;
5. attach the project root as an explicit read root;
6. set `TMPDIR`, `TMP`, `TEMP`, `XDG_CACHE_HOME`, and Python cache controls beneath scratch;
7. record root, provenance, initial size, final size, and budget disposition.

For implementation profiles, retain the project as process working directory and treat declared
scratch as an additional writable/generated root.

- [ ] **Step 3: Implement aggregate budget accounting**

Use one shared log-byte counter. Before every run and resume, account for managed state plus each
non-overlapping declared scratch root. Reserve bounded log headroom before launch.

During execution, a bounded in-process watchdog may sample manager-owned state and scratch size;
it is not a service or persistent monitor. Use an operational kill threshold below 250 MiB so
sampling and metadata overhead cannot knowingly consume the user-level ceiling. Record an
over-budget attempt as non-materializable. Apply a conservative per-file resource limit to the
Claude process and its subprocesses where the platform supports it. Never delete user files as
budget recovery, and do not claim a quota-grade adversarial guarantee from sampled accounting.

- [ ] **Step 4: Run state-focused and full tests GREEN**

```bash
PYTHONPATH=adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest -v \
  adapters/codex/delegate-to-claude/tests/test_state_budget.py
```

Then run the Task 1 command.

---

## Task 5: Add implementation ownership reconciliation

**Files:** create `reconcile.py`; modify manager, profiles, and tests.

- [ ] **Step 1: Write dirty-worktree reconciliation tests**

Use temporary Git repositories. Cover:

- implementation profiles require at least one `--owned-path`;
- exact file and directory ownership;
- a clean owned-file edit succeeds;
- an unowned tracked edit, delete, rename, or untracked file fails;
- a pre-existing dirty owned or unowned file remains distinguishable from worker changes;
- a worker change to an already-dirty unowned file is detected;
- declared scratch changes do not count as product edits;
- staged user changes are preserved and not attributed to the worker;
- reconciliation never stages, restores, deletes, or overwrites;
- non-Git project roots fail profiled implementation preflight;
- symlink-owned paths cannot escape the project root.

- [ ] **Step 2: Implement baseline and final fingerprints**

Record a bounded private baseline sufficient to compare Git-visible tracked, staged, deleted,
renamed, and untracked paths, including content hashes for paths already dirty before launch. Do
not hash `.git` internals, transcript content, or declared scratch payloads. Keep the algorithm
correct for dirty worktrees; do not assume `git status` was clean.

- [ ] **Step 3: Reconcile without rollback**

Classify final changes as owned, pre-existing-unchanged, scratch, or undeclared. An undeclared
change makes the attempt non-materializable and returns nonzero after preserving logs and the final
worktree. Return the path classification in private status output. Do not automatically revert.

Implementation native-sandbox settings disable Bash network and unsandboxed escape while retaining
project writes. `implementation-auto` additionally requires a successful non-generative auto-mode
capability preflight.

- [ ] **Step 4: Run reconciliation-focused and full tests GREEN**

```bash
PYTHONPATH=adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest -v \
  adapters/codex/delegate-to-claude/tests/test_reconcile.py
```

Then run the Task 1 command.

---

## Task 6: Complete manager-materialized artifact review

**Files:** manager and existing manager tests.

- [ ] **Step 1: Write failing artifact tests**

Require `--artifact-output` for `artifact-review`. Test successful atomic materialization, attempt
number and hash recording, existing-output refusal, explicit overwrite, symlink leaf/ancestor
refusal, failed/truncated result refusal, and no Write/Edit tool exposure.

- [ ] **Step 2: Reuse one materialization primitive**

Do not duplicate the `materialize` command's security checks. The run command invokes the same
primitive after a successful reconciled attempt. The output artifact is not scratch and is not
implicitly writable by Claude.

- [ ] **Step 3: Run the full suite GREEN**

Use the Task 1 command.

---

## Task 7: CI and final worker verification

**Files:** CI only if the existing step requires correction.

- [ ] **Step 1: Preserve the existing adapter CI command**

Do not change workflow triggers, permissions, action versions, or unrelated steps. Add no network
or paid-runtime job.

- [ ] **Step 2: Run exact final verification**

```bash
PYTHONPATH=adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest discover \
  -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
python3 check_state.py
python3 check_wids.py
git diff --check
```

- [ ] **Step 3: Inspect only the worker-owned write set**

Return:

- status: complete, partial, or blocked;
- exact files changed or created;
- RED tests observed and final test count;
- verification commands and exit status;
- assumptions and unresolved native-runtime uncertainty;
- any undeclared diff or conflict;
- no prose summary longer than needed for root disposition.

Do not commit, install, deploy, or launch another agent.

---

## Root-only review and activation gates

After the worker returns, the root will:

1. disposition every worker file as accept, revise, park, or reject;
2. reproduce the state, manifest, MCP, command-write, and dirty-worktree counterexamples;
3. inspect effective command construction against the locally installed Claude CLI;
4. run the complete deterministic verification independently;
5. update user-facing skill and README prose only after code acceptance;
6. request separate authority for the smallest paid actual-runtime sandbox probe;
7. keep the candidate uninstalled and uncommitted until that probe and final review pass.

---

## Root correction follow-up (approved 2026-07-20)

**Status:** root correction pass complete; corrected candidate dispositioned **accept as an uninstalled candidate**. The Opus worker return remains dispositioned **revise** because root changes were required. The user
approved a local root correction pass without another paid-model call. This is an extension of the
corrective implementation plan, not a new proposal.

The root independently reproduced the following release-blocking counterexamples after the worker's
172-test pass:

1. **Repository ownership could be bypassed.** A worker could edit and commit an owned file, mutate
   the Git index, create an ignored installation tree, or change an already-dirty file larger than
   8 MiB without reliable rejection. Reconciliation must cover HEAD/index control state, hash full
   dirty-file content, and treat ignored non-scratch changes as undeclared side effects.
2. **Strict manifest enforcement assumed `init` arrived first.** A tool, assistant, or result event
   before a validated startup manifest could be accepted. Manifest-enforced profiles must terminate
   on any meaningful pre-init event.
3. **Read-only MCP access was declarative rather than enforced.** Unknown MCP identifiers could be
   admitted. Profiled modes must admit only explicitly audited read-only identifiers; all other MCP
   identifiers fail closed pending a separate trust mechanism and actual-runtime probe.
4. **Scratch authorization accepted unsafe existing directories and arbitrary marker contents.**
   Run-scoped marker provenance, current-user ownership, and private permissions must be validated.
5. **Implementation scratch was admitted but not wired into the child environment or sandbox.**
   All scratch-bearing modes must receive deterministic temp/cache variables and an exact native
   sandbox write allowance; implementation modes must also deny writes to `.git`.
6. **State enforcement repeatedly scanned historical state and used the aggregate ceiling as a
   per-file limit.** Historical bytes must be accounted once, the watchdog must observe only the
   current run plus non-overlapping scratch, and the per-file limit must be conservative.
7. **Shared-log truncation was incompletely reflected in materializability.** Any stdout or stderr
   truncation under the shared log budget must make an attempt non-materializable.

### Root correction write set

- `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/{reconcile,profiles,runtime_policy,state_budget}.py`
- `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
- matching adapter tests only
- this live plan and, if semantics change, the approved proposal

### Root correction verification contract

- add and observe focused RED tests for every counterexample above;
- make each focused suite GREEN before proceeding to the next subsystem;
- run the complete adapter suite plus `check_state.py`, `check_wids.py`, and `git diff --check`;
- leave the candidate uninstalled, uncommitted, and unactivated;
- preserve unrelated pre-existing changes and generated review evidence.

### Root correction progress

- [x] Reproduced the HEAD/index, ignored-path, large-dirty-file, pre-init-event, unknown-MCP,
  unsafe-marker, unwired-scratch, historical-scan, and shared-log-truncation counterexamples.
- [x] Added focused RED tests before the corresponding root changes.
- [x] Added repository-control/ignored-path reconciliation, run-bound scratch authorization,
  pinned MCP query-identifier admission with local executable provenance, implementation scratch
  wiring, `.git` native-sandbox denial, current-run watchdog scoping, and truncation failure.
- [x] Confirmed locally installed Claude Code `2.1.215` advertises the required CLI flags; local
  binary inspection contains `sandbox.filesystem.allowWrite` and `denyWrite` keys.
- [x] Full adapter verification before the actual-runtime probe: 192 tests passed on 2026-07-20; `check_wids.py` and
  `git diff --check` passed. `check_state.py` remains red only for four pre-existing routing records
  (`scarcity-mode`, `fable-window-end`, `reviewer-pin`, and `orchestrator-pin`) that expired on
  2026-07-19. Updating those records would be an unauthorized route change, so they remain visible.
- [x] Disposition the corrected candidate and leave it uninstalled/uncommitted pending the
  separately authorized actual-runtime probe.

**Activation boundary:** fake-CLI and local static checks establish adapter logic, not effective
Claude sandbox or MCP semantics. Claude Code 2.1.215 also warns that invalid settings are silently
ignored in print mode. Installation therefore remains blocked on the smallest separately approved
actual-runtime probe that observes settings acceptance, filesystem/network denial, and MCP
per-tool behavior.

### Actual-runtime probe follow-up (2026-07-20)

- [x] Launched one authorized Sonnet-high version-2 probe with a five-action packet.
- [x] Preserved the failed startup evidence; no effect path changed and retained run state was
  20 KiB.
- [x] Root-caused the broader-manifest result to exposed-versus-allowed MCP normalization.
- [x] Added RED tests, explicit denies for unselected pinned MCP identifiers, and profile version
  3 so the version-2 session cannot resume across the authority change.
- [x] Post-correction verification: 195 adapter tests, `check_wids.py`, `git diff --check`, and the
  orchestration-learning audit passed. `check_state.py` remains red only for the already-recorded
  expired routing entries; no route state was changed.
- [ ] Effective scratch/project/`.git`/localhost/MCP behavior remains gated on one fresh paid
  version-3 run. No retry is authorized by the first call.
