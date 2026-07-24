# Codex-managed Antigravity Gemini Flash adapter implementation plan

> **For agentic workers:** use `superpowers:subagent-driven-development` or
> `superpowers:executing-plans`. Give one implementation worker the entire adapter write set; the
> lifecycle, budget, and reconciliation tasks share state and must not be edited concurrently.

**Goal:** Build a manually selected temporary `delegate-to-antigravity` adapter that invokes the
official local `agy` CLI with two explicit authority profiles, preserves private evidence, enforces
a manager-side state ceiling, passes focused fake-CLI tests, and proves usability with one bounded
real Gemini Flash task. The fuller C0/capability/lifecycle design below remains the hardening
backlog and extension seam for the deferred router.

**Architecture:** Import only `adapters/codex/scripts/delegation_policy` as the shared contract.
Keep Antigravity presets, capability records, static command grammars, output parsers, and lifecycle
state inside `delegate-to-antigravity`; never import the Claude adapter. Copy proven state-budget
and Git-reconciliation behavior with explicit lineage for this first slice instead of extracting a
general runtime package prematurely. A future router can call the stable packet/result boundary,
but this adapter performs no routing.

**Tech stack:** Python 3.12+ standard library, `unittest`, the official local `agy` executable, and
Git CLI for workspace checks. No package install, network download, daemon, monitoring, central
database, Dionysus change, recursive agent, resume, commit, push, merge, deletion, or cleanup in
this implementation cohort. One bounded live generation is authorized only as the final smoke
check after fake-provider verification and user-level skill installation.

---

## Status and gates

- **Proposal:**
  `docs/proposals/2026-07-20-codex-managed-antigravity-gemini-flash-adapter.md`.
- **Dependency:** completed C0 plan revision 4 and
  `docs/reviews/2026-07-20-c0-policy-core-execution-record.md`.
- **Plan revision:** 5 (accelerated temporary-adapter scope).
- **Plan status:** execution approved 2026-07-20. The operator explicitly reduced the temporary
  adapter from exhaustive capability certification to a thin, usable bridge with basic tests.
- **MVP execution status:** complete; 10 focused tests pass, the user-level skill is installed, and
  one bounded read-only Gemini Flash task completed successfully. See
  `docs/reviews/2026-07-20-gemini-flash-mvp-execution-record.md`.
- **Review:** `docs/reviews/2026-07-20-gemini-flash-adapter-plan-sol-review.md`.
- **Closure target:** installed user-level skill plus thin source wrapper, fake CLI, focused tests,
  and one bounded real Flash smoke invocation. The exhaustive capability-record, durable lifecycle,
  reconciliation, and materialization design below remains the hardening backlog rather than an
  MVP release gate.
- **Generated state:** configured maximum 240 MiB; sampled admission/stop threshold 192 MiB. Tests
  use temporary directories. No automatic deletion or retention job.
- **Activation:** manual selection only. The MVP exposes explicit review and implementation
  profiles, prints the effective authority posture before launch, and relies on `agy`'s native
  sandbox/permission controls. It makes no claim that every provider behavior has been certified.
- **Git:** no staging or commits unless separately requested.

## Provider boundary

```text
private Task Packet v1 + explicit private CLI bindings
                       |
        delegation_policy (shared C0; pure)
                       |
    Antigravity preset + production capability record
                       |
       static adapter-owned command compiler (no shell)
                       |
       attempt evidence + full-workspace reconciliation
                       |
             sanitized Result Record v1
```

## Frozen contract A: Task Packet v1 and private bindings

### Packet file

The packet is an explicitly named JSON file, never auto-discovered. It must be a regular file, not
a symlink, owned by the current user, no larger than 64 KiB, and mode `0600` after masking special
bits (no group/other permission bits at all). Its parent chain must not traverse symlinks. The file
is opened with no-follow semantics and its device/inode/mode/owner are rechecked after open to
detect path swaps. Unknown or missing keys fail validation.

| Key | Exact v1 contract |
|---|---|
| `schema_version` | integer exactly `1` |
| `objective` | string, 1–32,768 UTF-8 bytes; private prompt content |
| `non_goals` | list of 0–32 unique non-empty strings, each at most 1,024 bytes |
| `escalation_conditions` | list of 0–32 unique non-empty strings, each at most 1,024 bytes |
| `profile` | `flash-investigation` or `flash-implementation-worktree` |
| `model` | exact non-empty provider model string, at most 256 bytes |
| `thinking` | `low`, `medium`, or `high`; `run` requires the exact model/thinking pair in the record, while recordless `compile` validates syntax only and reports assurance unresolved |
| `read_scopes` | v1 requires exactly `["project"]`; external read roots are deferred |
| `write_scopes` | unique stable symbolic root IDs, maximum 32; empty for investigation |
| `command_template_ids` | unique stable IDs, maximum 32; definitions come from the record-linked adapter grammar |
| `validation_template_ids` | unique subset of `command_template_ids`, maximum 32 |
| `network` | exactly `deny` |
| `installation` | exactly `deny` |
| `git_mutation` | exactly `deny` |
| `descendants` | exactly `deny` |
| `expected_output` | exactly `final-response` |
| `timeout_seconds` | integer 1–3,600, excluding booleans |

All strings may not contain NUL and obey their byte bounds. Scope/template IDs match
`^[A-Za-z][A-Za-z0-9_-]*$`; structured identifiers and private path bindings receive the stated
path/URI/environment validations. Arbitrary objective/non-goal/escalation prose is not guessed to
be a shell command, credential, URI, or path. Those prose fields are private and are never copied
into policy explanation, sanitized status, result metadata, or telemetry.

### Explicit private-binding CLI

The production CLI is frozen as:

```text
agy_delegate.py compile --packet-file FILE --workspace DIR [--capability-record FILE] \
  --read-root ID=PATH... [--owned-path ID=REL...] [--scratch-dir DIR] \
  [--output-dir DIR] [--state-root DIR] [--agy-bin FILE]

agy_delegate.py run --packet-file FILE --workspace DIR --capability-record FILE \
  --read-root ID=PATH... [--owned-path ID=REL...] [--scratch-dir DIR] \
  [--output-dir DIR] [--state-root DIR] [--agy-bin FILE]
```

`--workspace`, the capability record, binary, roots, and state/output/scratch paths are private
bindings. V1 requires exactly one `--read-root project=PATH`, and it must resolve to `--workspace`.
Each `write_scopes` ID has exactly one `--owned-path`. Duplicate, unknown, reserved, missing,
symlinked, or differently resolved bindings fail. `--owned-path` is relative to the canonical
workspace, may not escape it, and is accepted only for a dedicated linked Git worktree. The
intentional project-contains-owned relationship is valid. Owned paths must be mutually
non-overlapping and non-aliasing; scratch, state, output, capability, and binary bindings must not
overlap or alias project/owned paths or each other unless an exact contract above says otherwise.
No binding path enters semantic or
authority hashes, content-free output, or telemetry.

`compile` validates the packet, bindings, C0 policy, transition notices, and any supplied capability
record; emits a sanitized C0 explanation plus hashes and unresolved controls; creates no run state;
invokes no provider or generative command; and emits no private path or prompt content. Without a
record it succeeds with `runtime.activation="unavailable"`, no activation claim, and all provider
assurance unresolved. `run` always requires a production record.

### Exact C0 mapping

The adapter constructs a raw C0 document and calls `normalize_policy` once:

| Packet/record input | C0 field |
|---|---|
| `profile` | `profile.id`; adapter preset revision in `profile.preset_revision` |
| `model`, `thinking` | `model_inputs.model`, `model_inputs.effort` |
| system grammar/capability evidence hashes | `model_inputs.system_input_hashes` |
| SHA-256 of private objective and packet source identities | `context.objective_hash`, `context.source_identity_hashes` |
| canonical workspace lineage identity | `context.workspace_identity` |
| binary version and activation decision | `runtime.provider="antigravity"`, `runtime.version`, `runtime.activation` |
| bound symbolic roots | `filesystem.roots`; read/write grants in `filesystem.rules`; defaults deny |
| selected static templates | empty IDs → `commands.mode="deny"`, empty templates; nonempty IDs → `commands.mode="selected"`, static templates |
| fixed denies | `network`, `git`, `installation`, `descendants`, `host_effects` deny |
| manager result | `output.mode="manager"`; optional output root |
| record-approved sandbox posture | `sandbox` |
| packet timeout, 16 MiB logs, and 240/192 MiB limits | `resources.wall_time_seconds`, `log_bytes`, `generated_state_bytes`, `generated_state_admission_bytes` |
| no resume/recovery daemon | `lifecycle.resume="deny"`, `lifecycle.recovery="foreground"` |

Every selected command uses the complete C0 command-template schema: `id`, `revision`, `argv`,
`cwd_scope`, `environment.{fixed,pass}`, `stdin`, `write_scopes`, `wall_time_seconds`,
`shared_log_bytes`, `per_file_bytes`, `network.{mode,destinations}`, `sandbox`, and `evidence_id`.
The adapter supplies these definitions from static code, never from packet text.

## Frozen contract B: Capability Record v1

### Trust and schema

A production record is an explicitly passed external JSON artifact. It must be outside the project
and canonical workspace, a regular non-symlink file owned by the current user, at most 64 KiB,
neither group- nor world-writable, and under a parent chain not writable by group/world except for a
root-owned directory whose permission bits are exactly `01777`. Every other ancestor must be owned
by the current user or root and have no group/other write bit. No-follow open and post-open
device/inode/mode/owner checks detect file swaps. The adapter never searches the repository,
project, home, or provider state for records.

Unknown or missing keys fail. The exact top-level fields are:

| Field | Contract |
|---|---|
| `schema_version` | integer exactly `1` |
| `record_class` | production CLI accepts only `production`; `test` exists only as injected test data |
| `record_id` | stable non-empty ID |
| `issued_at`, `expires_at` | RFC3339 UTC timestamps; issued ≤ now < expires |
| `issuer` | `{kind:"operator", approval_id:STABLE_ID}` |
| `platform` | exact `{system, machine}` pair |
| `binary` | `{realpath, sha256, version, owner_uid, mode}` |
| `models` | non-empty exact entries `{model, thinking:[...]}` |
| `grammar_id` | ID in the adapter's static grammar allowlist |
| `parser_ids` | IDs in the adapter's static parser allowlist |
| `environment_ids` | subset of adapter-owned environment-variable identifiers |
| `provider_state_root_ids` | symbolic adapter-owned root identifiers, not paths |
| `profiles` | exact per-profile control matrix below |
| `evidence_ids` | non-empty stable evidence identifiers |
| `provider_state_risk_decision_id` | stable stakeholder decision ID or `null` |

The record cannot provide CLI flags, argv, commands, regexes, parser logic, environment values,
executable paths other than the observed binary identity, or provider-state paths. Static adapter
tables map `grammar_id`, `parser_ids`, environment IDs, and provider root IDs to implementation.
All IDs match `^[A-Za-z][A-Za-z0-9_-]*$` and are at most 128 bytes. The record permits at most 32
model entries, three unique thinking values per model, eight parser IDs, 16 environment IDs, eight
provider-state root IDs, 64 evidence IDs, and exactly the two known profile entries with exactly the
matrix keys below. Text scalars are at most 1,024 bytes except the 64-byte lowercase SHA-256 and the
256-byte model/version fields. `issued_at`/`expires_at` are strings, `owner_uid` is a non-negative
integer, and `mode` is an integer from `0` through `07777`. Binary `realpath` is canonical and
absolute; the binary must be a current-user/root-owned regular executable with no group/other write
bits. `models`, `parser_ids`, `environment_ids`, `provider_state_root_ids`, and `evidence_ids` are
unique lists; `profiles` is an object keyed by the two exact profile IDs. The implementation rejects
unknown IDs. Tests inject a
`record_class:"test"` object through an
internal constructor that is absent from the production CLI; no production flag enables it.

Immediately before every provider launch—not only during `doctor`—the adapter revalidates the
record, expiry, current platform, binary canonical realpath, regular-file/no-symlink posture,
current-user ownership, mode, SHA-256, reported version, and requested model/thinking pair. It then
runs the static-parser-backed non-generative model-list command and requires the exact requested
model/thinking pair to be present immediately before `agy -p`. Any change or parse ambiguity fails
closed before generation.

### Profile × control activation matrix

Each record profile maps every row below to exactly one of `verified`, `detected`,
`accepted-unknown`, `unavailable`, or `not-applicable`. Missing/extra controls fail. `detected`
means post-run observation only and never satisfies a permission boundary. `not-applicable` is
allowed only in the two cells explicitly marked below and is excluded from activation evaluation.

| Control | Investigation requires | Implementation requires |
|---|---|---|
| binary/model selection | `verified` | `verified` |
| prompt/result/model-observation grammar | `verified` | `verified` |
| source-only project behavior | `verified` | `not-applicable` |
| linked-worktree write behavior | `not-applicable` | `verified` |
| network denial | `verified` | `verified` |
| installation denial | `verified` | `verified` |
| external-write denial | `verified` | `verified` |
| Git-control mutation denial | `verified` | `verified` |
| descendant-agent denial | `verified` | `verified` |
| process/service/device/application host-effect denial | `verified` | `verified` |
| command-template behavior | `verified` when templates selected | `verified` when templates selected |
| sandbox/permission combination | `verified` | `verified` |
| provider-global state accounting | `verified`, or `accepted-unknown` with risk ID | same |

No other `accepted-unknown` activates a profile. In a required cell, `detected`,
`accepted-unknown` without the exact stakeholder risk-decision ID, `unavailable`, or
`not-applicable` keeps the profile unavailable. A misplaced `not-applicable` is a schema error. No
production record ships in the adapter, tests, docs, examples, or fixtures.

`doctor [--agy-bin FILE] [--capability-record FILE]` is non-generative. Without a record it reports
only separately labeled observed version/help/model facts and `activation=unavailable`. With a
record it also reports record-validation and mismatch results. It never invokes `-p`, writes attempt
state, or treats advertised help as verified behavior.

## Frozen contract C: lifecycle, evidence, and Result Record v1

### Enums and exits

- Lifecycle: `planned`, `starting`, `running`, `terminal`.
- Recovery: `none`, `manager-active`, `live-orphan`. `live-orphan` is nonterminal and valid only
  with lifecycle `running` and a matching live PID/start signature.
- Outcome: `succeeded`, `provider-failed`, `launch-failed`, `timed-out`, `interrupted`,
  `budget-exceeded`, `result-missing`, `result-ambiguous`, `model-mismatch`, `unreconciled`,
  `orphan-terminated`. Outcome is null before `terminal` and non-null at `terminal`.
- Reconciliation: `not-run`, `clean`, `owned-only`, `failed`.
- Budget: `admitted`, `running`, `clean`, `exceeded`, `truncated`, `unknown`.
- Observed-model status: `observed`, `unknown`, `conflict`.
- Exit codes: `0` successful manager command; `2` packet/configuration error; `3` capability,
  provenance, or model error; `4` budget refusal/stop; `5` reconciliation/materialization refusal;
  `6` provider/lifecycle failure; `7` preserved live/orphan state requiring operator action.

### Durable layout and concurrency

```text
STATE_ROOT/
  manager.lock
  runs/RUN_UUID/
    run.lock
    metadata.json
    private-bindings.json
    attempt-001/
      journal.jsonl
      prompt.txt
      stdout.log
      stderr.log
      provider.log
      result.txt
      result-record.json
      reconciliation.json
```

Directories/files are private. Metadata uses write–flush–fsync–atomic-replace; the append-only
journal has monotonically increasing sequence numbers and fsyncs lifecycle transitions. `fcntl`
locks permit one mutator per run. A manager lock serializes admission and launch; running attempts
may coexist only when their canonical workspace, owned, scratch, output, and provider-state roots
are pairwise disjoint. Overlap refuses launch.

All JSON objects reject unknown/missing keys. UUIDs are lowercase canonical UUID strings; hashes are
64 lowercase hexadecimal characters; timestamps are RFC3339 UTC with `Z`; relative evidence
locators contain only `attempt-NNN/<allowlisted-filename>` and no slash beyond that one.

`metadata.json` has exactly these fields and types:

| Field | Type/invariant |
|---|---|
| `schema_version` | integer `1` |
| `run_id` | UUID; directory name must match |
| `attempt` | integer `1` in v1 |
| `lifecycle` | lifecycle enum |
| `recovery` | recovery enum |
| `outcome` | null before terminal; outcome enum at terminal |
| `profile` | packet profile enum |
| `requested` | exact object `{model:string, thinking:enum}` |
| `observed` | exact object `{status:enum, model:string|null, evidence_id:ID|null}`; model/evidence are non-null only for `observed` or `conflict` |
| `identities` | exact object `{semantic_sha256:hash, authority_sha256:hash, capability_sha256:hash|null}`; capability is null only for recordless compile, which creates no metadata |
| `process` | exact object `{pid:positive-int|null, start_signature:string|null}`; both null or both non-null; running requires non-null |
| `reconciliation` | reconciliation enum |
| `budget` | budget enum |
| `last_sequence` | non-negative integer matching the last valid journal event |
| `timestamps` | exact object `{created_at:time, started_at:time|null, finished_at:time|null, updated_at:time}` with monotonic ordering; terminal requires finished |

`private-bindings.json` has exactly `schema_version`, `workspace`, `read_roots`, `owned_paths`,
`scratch_dir`, `output_dir`, `state_root`, `capability_record`, and `agy_bin`. Paths are canonical
absolute strings or null where optional; `read_roots`/`owned_paths` are ID-to-path objects. This
file, `prompt.txt`, streams, provider evidence, and result text are mode `0600`, never emitted by
`status`, and never used as telemetry. The packet prose is rendered into `prompt.txt` only after all
preflight checks pass.

Every `journal.jsonl` event has exactly:

```json
{
  "schema_version": 1,
  "sequence": 0,
  "at": "RFC3339-UTC",
  "event": "planned|launch-started|provider-started|provider-exited|watchdog-stop|recovery-changed|reconciled|terminal",
  "lifecycle": "planned|starting|running|terminal",
  "recovery": "none|manager-active|live-orphan",
  "outcome": null,
  "pid": null,
  "start_signature": null,
  "detail_code": "fixed-adapter-code"
}
```

`outcome`, PID, and signature obey the metadata nullability rules. `detail_code` is a non-private
ID from a static allowlist (for example `none`, `exec-failed`, `exit-nonzero`, `timeout`,
`state-threshold`, `result-missing`, `result-ambiguous`, `model-conflict`, or
`reconciliation-failed`), not arbitrary exception text. Journal replay accepts a truncated final
line only by discarding that line, rejects a gap/duplicate/invalid transition, and rebuilds
metadata from the last valid event plus immutable identity fields.

Valid lifecycle transitions are `planned → starting → running → terminal` and
`planned|starting → terminal` for pre-provider failure. `planned`, `launch-started`,
`provider-started`, and `terminal` respectively establish those lifecycle states;
`provider-exited`, `watchdog-stop`, and `reconciled` retain the current nonterminal lifecycle until
the terminal event. `recovery-changed` is valid only while `running`: it changes
`manager-active → live-orphan` with null outcome, or retains `live-orphan` immediately before a
terminal `orphan-terminated` event. No transition leaves `terminal`; all others are rejected.

`result-record.json` exists only after terminal and has exactly:

| Field | Type/invariant |
|---|---|
| `schema_version`, `run_id`, `attempt`, `profile` | same definitions as metadata |
| `lifecycle` | exactly `terminal` |
| `outcome` | non-null outcome enum |
| `requested`, `observed`, `identities` | same exact objects as metadata |
| `provider` | exact `{exit_code:int|null, termination:"normal"|"signal"|"manager-stop"|"not-started", signal:int|null}` with signal non-null only for `signal` |
| `reconciliation`, `budget` | terminal enums |
| `cache_status` | exactly `unknown` |
| `timestamps` | exact non-null `{created_at, started_at|null, finished_at}` in order |
| `evidence` | exact `{stdout, stderr, provider_log, result, reconciliation}`; each value is its fixed relative locator or null when not created |

It excludes prompt/transcript/result text, raw argv/command/tool output, credentials, environment
values, exceptions, and absolute paths.

The manager that owns `run.lock` reports `manager-active` while the matching provider lives. If the
lock is free but PID/start signature still match, the next command records nonterminal
`live-orphan`, refuses overlap, and does not signal it. If identity is absent/mismatched it records
terminal `interrupted`; if a previously recorded live orphan is later observed terminated it
records `orphan-terminated`. A valid terminal journal with stale metadata is replayed. The manager
never automatically kills, resumes, retries, deletes, or overwrites evidence.

An attempt is materializable only when outcome is `succeeded`, reconciliation is `clean` or
`owned-only`, budget is `clean`, result is non-truncated and unambiguous, and observed model is not
in conflict. `inspect --include-result` is the only CLI view that emits private result text.

## Frozen contract D: generated state and reconciliation

### Truthful sampled accounting

The 240 MiB value is the configured manager maximum, not a host-wide hard quota. The manager uses
a sampled 192 MiB admission/stop threshold to leave overrun headroom. It samples at most every 0.5
seconds; an overshoot is possible and is measured and recorded. Crossing the threshold terminates
the provider process group, preserves evidence, and yields `budget-exceeded`; it never deletes.

Accounted roots are manager state, scratch, the shared logs, and positive worktree delta. New files
count their full allocated size; pre-existing files count `max(0, current_allocated - baseline)`;
deleted files count zero. Symlinks, mount crossings, hard-link ambiguity, unreadable roots, and
unstable samples produce `unknown` and make the attempt non-materializable. Stdout, stderr, and the
provider log share the C0 `resources.log_bytes=16 MiB` allocation. The manager drains stdout/stderr
and discards bytes after their remaining shared allocation while recording exact discarded counts.
Because the provider writes `provider.log` directly, the 0.5-second watchdog samples its allocated
size; once aggregate stream allocation exceeds 16 MiB, it terminates the provider process group and
records measured overshoot. Any dropped or over-limit stream yields budget `truncated`, outcome
`budget-exceeded`, and no materialization. A future proven pipe transport may replace this behavior,
but the fake-first grammar may not claim discard-before-storage for a direct provider log.

Provider-global roots are sampled before/after when the static provider-root mapping permits it,
but are excluded from any claimed 240 MiB guarantee unless a later probe proves redirectable quota
control. Activating with sampled/unknown provider-global accounting requires the exact stakeholder
risk-decision ID in the production record.

### Full-workspace reconciliation

- Investigation fingerprints and reconciles the complete Git workspace with an empty owned-path
  set. V1 permits only the canonical workspace as a read root. Any tracked, untracked, ignored,
  index, HEAD, Git-control, or symlink mutation yields `failed` and remains preserved.
- Implementation requires `git rev-parse --git-dir` to differ from
  `git rev-parse --git-common-dir`, proving a linked worktree; the primary checkout is rejected.
  It fingerprints the full worktree before launch and permits content changes only beneath exact,
  non-overlapping owned paths. Any undeclared/control/ignored/external effect fails.
- Interruption, timeout, provider failure, model conflict, and budget stop still run terminal
  reconciliation. Reconciliation detects; it never resets, cleans, deletes, commits, merges, or
  removes a worktree.

## Accelerated MVP execution scope (revision 5)

The operator's 2026-07-20 execution decision supersedes Tasks 1–8 below as immediate release
gates. They are retained as a hardening backlog and as the design seam for the deferred general
router. The temporary MVP implements only (all complete):

1. explicit `review` and `implementation-auto` profiles;
2. local `agy models` discovery and exact caller-selected model forwarding;
3. list-form argv with no shell, private prompt file/stdin handling, bounded timeout, explicit
   workspace, sandbox/permission mapping, and a manager-owned log/state directory;
4. a 240 MiB generated-state ceiling with a 192 MiB preflight warning/refusal threshold;
5. a fake-CLI focused test suite covering argv, prompt/result transport, profile mapping, nonzero
   exit, timeout, and state admission; and
6. a concise installed user skill plus one bounded real Flash smoke invocation.

The MVP does **not** implement capability records, the frozen journal/result schemas, resume,
recovery, full-workspace reconciliation, materialization, automatic routing, recursive delegation,
network downloads, provider installation, monitoring, or Dionysus changes. Those remain deferred.
The real smoke invocation is an operator-approved validation of usability, not certification of
the deferred controls.

## Worker-owned write set

One implementation worker owns only:

- `adapters/codex/delegate-to-antigravity/scripts/agy_delegate.py`
- `adapters/codex/delegate-to-antigravity/scripts/delegate_to_antigravity/*.py`
- `adapters/codex/delegate-to-antigravity/tests/**`

For the MVP, expected modules are `profiles.py`, `runner.py`, and `state_budget.py`, plus a fake CLI
and focused tests. The worker must not edit C0, the Claude adapter, README,
proposal/plan/review, skill, route/state/telemetry, installer, manifest, CI, or probe files. Root
owns user-consumed prose and dispositions.

---

### Task 1: Freeze C0 and build the fake-provider boundary

- [ ] Re-run the focused C0 suite and full Claude adapter suite; stop on regression.
- [ ] Build a network-free fake `agy` supporting deterministic version/help/models, success,
  stderr, nonzero, timeout, signal, partial/ambiguous output, observed-model, log growth, and writes.
- [ ] RED-test list argv/no shell, private prompt transport, and import of C0 but not Claude.

### Task 2: Implement strict packet/binding validation and non-generative compile

- [ ] RED-test every Packet v1 field, bound, privacy rule, file trust rule, binding invariant, and
  packet-to-C0 mapping above, including mode, symlink ancestors, inode swaps, and deterministic
  acceptance of path-like text in private prose. Prove valid project→owned nesting, and reject
  owned-owned overlap/alias plus unintended root overlap.
- [ ] Implement strict parsing and recordless/record-aware `compile`; prove both create no state and
  spawn no provider, and recordless compilation reports unavailable/unresolved rather than failing.
- [ ] Prove empty command IDs normalize to C0 `deny`, while nonempty IDs normalize to `selected`.
- [ ] Test semantic/authority stability across different private path bindings.

### Task 3: Implement static grammars and Capability Record v1

- [ ] Define adapter-owned grammar, parser, environment, and provider-root registries.
- [ ] RED-test exact schema/trust, production/test separation, provenance, binary revalidation,
  expiry/platform/model volatility, unrecognized IDs, and record injection attempts.
- [ ] Implement `doctor` with only non-generative version/help/models operations. Report observed
  facts separately from record assertions and create no attempt state.

### Task 4: Implement fail-closed presets and activation matrix

- [ ] Define both presets through `normalize_policy`, 240/192 MiB resources, and exact matrices.
- [ ] RED-test both all-verified matrices with their exact `not-applicable` cells, every misplaced
  `not-applicable`, and every required detected/unknown/unavailable cell.
- [ ] Require empty ownership/reconciliation for investigation and a linked worktree plus exact
  owned paths for implementation. Omit `resume` entirely.

### Task 5: Compile safe argv and private prompt/result transports

- [ ] Compile only static record-selected grammar/parser IDs; never accept record-supplied flags.
- [ ] Set `cwd` to the validated workspace/worktree, pass argv without shell, use an allowlisted
  environment, and pass prompts only by the proven stdin/private-file transport.
- [ ] Prove launch ordering revalidates binary/version and freshly parses the exact model/thinking
  pair before any `-p` process can start.
- [ ] RED-test metacharacters, secrecy, ordering, permission/sandbox mismatch, absent transport,
  model conflict, and broad skip-permission authority reporting.

### Task 6: Implement one-attempt lifecycle and recovery

- [ ] RED-test the frozen layout, enums, exit codes, atomic metadata, journal sequence, locks,
  disjoint-root concurrency, PID/start-signature recovery, truncated journal tail, active manager
  versus live orphan, the manager-active → live-orphan → orphan-terminated journal sequence, golden
  exact JSON fixtures, and every terminal outcome.
- [ ] Implement `run`, `status`, and `inspect`; every run has exactly one attempt and no retry.
- [ ] Preserve partial evidence and keep status/result records free of private content.

### Task 7: Implement sampled budget and full reconciliation

- [ ] Copy only proven stdlib behavior from the Claude adapter with source hash/lineage headers and
  a stated future extraction condition; never import its package.
- [ ] RED-test positive deltas, three-stream 16 MiB sharing/truncation, 192 MiB watchdog overshoot,
  direct-provider-log overgrowth termination, unknown links/mounts, provider-global sampling, C0
  log-resource identity, and no-deletion behavior.
- [ ] RED-test investigation empty-ownership reconciliation and implementation linked-worktree,
  full-baseline, owned/unowned, ignored, delete/rename, Git-control, symlink, and interruption cases.

### Task 8: Materialize exactly one accepted result

- [ ] Implement `materialize RUN_ID --output PATH [--attempt N] [--overwrite]` without provider use.
- [ ] Require that the run declared `--output-dir`; resolve `--output` as an existing-parent,
  no-symlink strict descendant of that bound root. A run without the binding cannot materialize,
  and later operator selection cannot create new output authority. Enforce the frozen eligibility
  predicate and refuse symlink targets, unsafe parents, races, ambiguous/truncated results, and
  failed reconciliation.
- [ ] Atomically write the exact result and record hash/attempt/time without exposing it in status.

### Task 9: Root-authored uninstalled skill, usage, and closure evidence

- [ ] After code review, root authors concise
  `adapters/codex/delegate-to-antigravity/SKILL.md` and adapter `README.md`; these remain uninstalled.
- [ ] Document `compile`, `doctor`, explicit private bindings, unavailable-live posture, and the
  separate probe/activation process without shipping a production record.
- [ ] Prove no live `agy -p`, network, Claude import, automatic routing, recursive agents, resume,
  install/deploy hook, or project-local telemetry/state root.
- [ ] Run all new tests, focused C0 tests, full Claude tests, `compileall`, Ruff,
  `check_wids.py`, `check_state.py`, `git diff --check`, explicit untracked whitespace checks, and
  generated-state accounting. Record pre-existing failures separately.
- [ ] Do not stage, commit, install, activate, invoke live generation, or create a capability probe.

## Final implementation return contract

Return status; exact files; RED evidence; focused/full counts; fake-provider proof; generated-state
size; capability-record availability; matrix/unresolved controls; lifecycle/reconciliation/
materialization results; planned/requested/observed provenance; assumptions; risks; and conflicts.
A passing fake suite is not a runtime activation claim.

## Deferred activation sequence

After this plan passes review and fake-first implementation:

1. separately approve a disposable, minimal actual-runtime probe plan;
2. probe authentication/model listing, prompt/result/model observation, source-only behavior,
   linked-worktree writes, permission/sandbox combinations, network/install/external/Git/descendant/
   host-effect denies, logs/timeouts, provider-global state, and watchdog behavior;
3. issue an external dated production record only for controls actually verified;
4. make and record any provider-global accounting risk decision explicitly;
5. activate one profile at a time after root review; and
6. collect repeated real-task evidence before considering the deferred general router.
