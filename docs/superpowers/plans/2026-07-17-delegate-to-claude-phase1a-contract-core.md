# Delegate-to-Claude Phase 1A Contract Core Implementation Plan

> **Path note (2026-07-24):** `adapters/codex/delegate-to-*` paths in this document refer to the
> runtime trees as they lived in this repository's worktree at writing time. They moved to the
> `delegation-runtime` repository (D-3, 2026-07-24) and were flattened to its root — read
> `adapters/codex/X` as `X` there. Quoted paths are preserved verbatim.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a pure, stdlib-only canonical contract core for governed Codex-to-Claude delegation, with strict packet/provenance/result/event validation and deterministic fixtures, without launching Claude or persisting runtime state.

**Architecture:** The canonical code lives inside the Codex adapter at `adapters/codex/delegate-to-claude/`, mirroring the preview skill's eventual deployment shape while remaining independent of the user-level preview MVP. Small Python modules validate one responsibility each: primitive values, opaque identifiers, owned paths, individual records, and cross-record reconciliation. Phase 1A has no process manager, no state-root default, no installer, and no network/model call.

**Tech Stack:** Python 3.12+ standard library, `unittest`, JSON fixtures, existing repository checks.

---

## Authority and boundaries

This plan implements only proposal §13 Phase 1 sub-slice 1: packet, route-decision,
lifecycle/reconciliation, result, descendant-manifest, and content-free event contracts with fake
fixtures. It does **not** implement `plan --dry-run`, Claude process launch/resume, runtime state,
termination, worktrees, telemetry sinks, the progressive skill, installation, deployment, or a real
capability probe.

The user-level preview at `~/.codex/skills/delegate-to-claude/` is read-only reference
material. Do not copy it wholesale, edit it, or turn its provisional `~/.codex/state` default into
canonical policy. Do not touch `ROUTES.md`, `STATE.md`, `WARRANTS.md`, `probes/`, the proposal,
handoff, or concurrent dirty files.

## Locked file map

| Path | Responsibility |
|---|---|
| `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/__init__.py` | Public validation API and schema version. |
| `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/validation.py` | Strict JSON-object primitives and stable `ContractError`. |
| `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/identifiers.py` | Typed opaque IDs, UUID session IDs, and SHA-256 locators. |
| `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/ownership.py` | Repository-relative path canonicalization and overlap rejection. |
| `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/contracts.py` | Individual record validators and cross-record bundle reconciliation. |
| `adapters/codex/delegate-to-claude/tests/support.py` | Fixture loader and valid-record builders used only by tests. |
| `adapters/codex/delegate-to-claude/tests/test_validation.py` | Primitive and identifier contract tests. |
| `adapters/codex/delegate-to-claude/tests/test_ownership.py` | Path escape, symlink, duplicate, and overlap tests. |
| `adapters/codex/delegate-to-claude/tests/test_contracts.py` | Record, privacy, provenance, lifecycle, and reconciliation tests. |
| `adapters/codex/delegate-to-claude/tests/fixtures/*.json` | One valid fixture for each canonical record plus invalid reconciliation cases. |
| `.github/workflows/ci.yml` | Run the canonical contract tests before existing build gates. |
| `adapters/codex/README.md` | Document Phase 1A boundary and preview-MVP relationship. |

All runtime modules must remain importable by adding only the canonical `scripts/` directory to
`PYTHONPATH`; no packaging dependency or generated file is introduced.

## Canonical record vocabulary

All validators reject unknown fields. `schema_version` is integer `1`. Every typed identifier has
the exact prefix shown and a 16–64 character base64url body (`A-Z`, `a-z`, `0-9`, `_`, `-`):

| Field | Prefix |
|---|---|
| `packet_id` | `pkt_` |
| `project_id` | `prj_` |
| `run_id` | `run_` |
| `lane_id` | `lane_` |
| `parent_id` | `parent_` |
| `route_decision_id` | `route_` |
| `lifecycle_id` | `life_` |
| `reconciliation_id` | `recon_` |
| `event_id` | `evt_` |
| `descendant_id` | `desc_` |

`session_id` is a canonical UUID string. Hashes and evidence locators are lowercase 64-character
SHA-256 hex digests in this slice; paths and free text never serve as event-plane locators.

The contract functions are:

```python
validate_route_decision(value: object) -> dict
validate_task_packet(value: object) -> dict
validate_result_envelope(value: object) -> dict
validate_descendant_manifest(value: object) -> dict
validate_routing_event(value: object) -> dict
validate_reconciliation(value: object) -> dict
validate_contract_bundle(value: object) -> dict
```

They return a deep-copied normalized dictionary or raise `ContractError(code, path, message)`.
They do not read or write the filesystem except that ownership validation receives an explicit
repository root and declared path list.

---

### Task 1: Validation primitives and opaque identifiers

**Route:** Sonnet high, `acceptEdits`, R5 mechanical fully specified edit under the user's explicit
Sonnet request; this is a demotion-probe-shaped use, not a route-table flip. Nearest alternative is
Opus high. Falsifier: Sonnet cannot implement the exact API or tests without architecture changes.

**Files:**
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/__init__.py`
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/validation.py`
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/identifiers.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_validation.py`

- [ ] **Step 1: Write the failing primitive-validation tests**

Create `test_validation.py` with tests that import the planned API and assert:

```python
import copy
import sys
from pathlib import Path
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from delegate_to_claude.identifiers import validate_hash, validate_id, validate_session_id
from delegate_to_claude.validation import ContractError, expect_object, reject_unknown


class ValidationTests(unittest.TestCase):
    def test_contract_error_has_stable_fields(self):
        error = ContractError("missing", "packet.run_id", "required field")
        self.assertEqual(error.code, "missing")
        self.assertEqual(error.path, "packet.run_id")
        self.assertEqual(str(error), "packet.run_id: required field [missing]")

    def test_expect_object_rejects_non_object(self):
        with self.assertRaisesRegex(ContractError, r"record: expected object"):
            expect_object([], "record")

    def test_reject_unknown_names_exact_field(self):
        with self.assertRaisesRegex(ContractError, r"packet.extra: unknown field"):
            reject_unknown({"known": 1, "extra": 2}, {"known"}, "packet")

    def test_typed_identifier_requires_prefix_and_opaque_body(self):
        good = "run_Abcdefghijklmnop"
        self.assertEqual(validate_id(good, "run_id"), good)
        for bad in ("repo-name", "run_short", "lane_Abcdefghijklmnop", "/tmp/run_value"):
            with self.subTest(bad=bad), self.assertRaises(ContractError):
                validate_id(bad, "run_id")

    def test_session_id_is_canonical_uuid(self):
        value = "3a01d811-4f10-4c5d-9cf4-c18183033c63"
        self.assertEqual(validate_session_id(value), value)
        with self.assertRaises(ContractError):
            validate_session_id("not-a-session")

    def test_hash_is_lowercase_sha256(self):
        value = "a" * 64
        self.assertEqual(validate_hash(value, "record.hash"), value)
        for bad in ("A" * 64, "a" * 63, "/tmp/evidence"):
            with self.subTest(bad=bad), self.assertRaises(ContractError):
                validate_hash(bad, "record.hash")

    def test_validators_do_not_mutate_input(self):
        value = {"known": {"nested": [1]}}
        before = copy.deepcopy(value)
        self.assertEqual(expect_object(value, "record"), before)
        self.assertEqual(value, before)
```

- [ ] **Step 2: Run the test and verify RED**

Run:

```bash
python3 -m unittest -v adapters/codex/delegate-to-claude/tests/test_validation.py
```

Expected: import failure for `delegate_to_claude`; the test must not pass before production files
exist.

- [ ] **Step 3: Implement the minimal validation API**

`validation.py` must define `ContractError`, `expect_object`, `expect_string`, `expect_bool`,
`expect_int`, `expect_list`, `require_fields`, `reject_unknown`, and `expect_enum`. Every helper
receives a dotted `path`; booleans must not satisfy `expect_int`; returned containers are deep
copies. `identifiers.py` must define the prefix map above, compile full-match regexes, and implement
`validate_id`, `validate_session_id`, and `validate_hash`. `__init__.py` exports
`SCHEMA_VERSION = 1`, `ContractError`, and the seven public contract validators as lazy imports or
normal imports without side effects.

Use this exact exception shape:

```python
class ContractError(ValueError):
    def __init__(self, code: str, path: str, message: str) -> None:
        self.code = code
        self.path = path
        self.message = message
        super().__init__(f"{path}: {message} [{code}]")
```

- [ ] **Step 4: Run the focused tests and verify GREEN**

Run the Step 2 command. Expected: 7 tests pass with no warnings.

- [ ] **Step 5: Self-review and commit only Task 1 files**

Run `git diff --check` and inspect the exact diff. Commit subject:

```text
feat(codex): add delegation contract primitives
```

The commit body must include `Why`, `Verification`, and `Boundary`; Boundary states that no
runtime/process behavior was added.

---

### Task 2: Repository ownership canonicalization

**Route:** Opus xhigh, `acceptEdits`, R4 coding/agentic implementation because symlink and
ancestor-overlap semantics are security-bearing. Nearest alternative is Opus high. Falsifier: a
smaller route produces the same behavior under the adversarial path suite with no review findings.

**Files:**
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/ownership.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_ownership.py`
- Modify: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/__init__.py`

- [ ] **Step 1: Write failing path-boundary tests**

Create a `unittest.TestCase` using `tempfile.TemporaryDirectory`. Each test creates a repository
directory and calls:

```python
canonicalize_owned_paths(repository: Path, declared: list[str]) -> tuple[str, ...]
```

Required tests:

1. `src/a.py` returns the normalized repository-relative POSIX path `("src/a.py",)` when `src`
   exists and `a.py` does not.
2. An absolute path inside the repository normalizes to the same relative path.
3. `../outside.txt` and an absolute outside path raise code `outside_repository`.
4. A final-component symlink raises `final_symlink` without following it.
5. An intermediate symlink resolving outside raises `outside_repository`.
6. Two spellings of one real target raise `duplicate_target`.
7. `src` plus `src/a.py` raises `overlapping_targets`.
8. A path whose parent does not exist raises `missing_parent`; the validator never creates it.
9. The repository root itself cannot be an owned target and raises `repository_root_owned`.

- [ ] **Step 2: Run the test and verify RED**

Run:

```bash
python3 -m unittest -v adapters/codex/delegate-to-claude/tests/test_ownership.py
```

Expected: import failure for `delegate_to_claude.ownership`.

- [ ] **Step 3: Implement canonicalization without following an untrusted final symlink**

Resolve the repository with `strict=True`. For each declared path, join relative values to the
repository, resolve only its parent with `strict=True`, then reconstruct `parent / name`; reject a
final symlink before any full-path resolution. Use `Path.is_relative_to()` against the resolved
repository. Normalize accepted targets with `relative_to(repository).as_posix()`. Sort only for
pairwise collision checks; preserve declaration order in the returned tuple. Reject equal targets
and any pair where either target appears in the other's `.parents`.

The function must be pure with respect to the filesystem: reads/stat calls are allowed; mkdir,
touch, unlink, rename, chmod, and writes are forbidden.

- [ ] **Step 4: Run focused and Task 1 tests**

Run:

```bash
python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

Expected: all tests pass.

- [ ] **Step 5: Self-review and commit only Task 2 files**

Run `git diff --check`; inspect the diff. Commit subject:

```text
feat(codex): validate delegation ownership paths
```

Commit body includes `Why`, `Verification`, and `Boundary`; Boundary states that validation does
not create worktrees or directories.

---

### Task 3: Strict delegation records and cross-record reconciliation

**Route:** Opus xhigh, `acceptEdits`, R4 because this is the load-bearing multi-record contract and
privacy boundary. Nearest alternative is Opus high. Falsifier: review finds the xhigh route added
complexity beyond the locked vocabulary or failed to preserve exact provenance.

**Files:**
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/contracts.py`
- Create: `adapters/codex/delegate-to-claude/tests/support.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_contracts.py`
- Create: `adapters/codex/delegate-to-claude/tests/fixtures/route-decision.valid.json`
- Create: `adapters/codex/delegate-to-claude/tests/fixtures/task-packet.valid.json`
- Create: `adapters/codex/delegate-to-claude/tests/fixtures/result-envelope.valid.json`
- Create: `adapters/codex/delegate-to-claude/tests/fixtures/descendant-manifest.valid.json`
- Create: `adapters/codex/delegate-to-claude/tests/fixtures/routing-event.valid.json`
- Create: `adapters/codex/delegate-to-claude/tests/fixtures/reconciliation.valid.json`
- Modify: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/__init__.py`

- [ ] **Step 1: Write the valid JSON fixtures**

Use one shared identity set across all fixtures. Each fixture contains only these contract fields:

**Route decision:** `schema_version`, `route_decision_id`, `project_id`, `run_id`, `lane_id`,
`lifecycle_id`, `source_hashes` (`routes`, `state`, optional `overlay`), `task_class`,
`warrant_ids`, `active_profile`, `applied_layers`, `fallback_applied`,
`requested_control_mapping_version`, `planned`, `requested`, and `delivered`. `planned` and
`requested` contain `model`, `effort`, `role`, `surface`. Each delivered field contains `value`,
`status` (`observed`, `unobserved`, `conflicted`), and nullable `evidence_locator_or_hash`.
`observed` requires a non-null hash; `unobserved` requires `value` and locator to be null;
`conflicted` requires a non-empty list value and non-null hash.

**Task packet:** `schema_version`, `packet_id`, the shared route/run/lane/lifecycle IDs,
`objective`, `closure_target`, `non_goals`, `repository_root`, `owned_paths`, `allowed_writes`,
`forbidden_paths`, `write_isolation` (`read_only`, `dedicated_worktree`,
`filesystem_allowlist`), `required_sources`, `output_artifact`, `return_shape`,
`validation_oracle`, `falsifier`, `permissions` (`mode`, `allowed_tools`, `denied_tools`),
`limits` (`hard_spend_limit`, `hard_runtime_limit`, `observation_deadline`), `descendants`, and
`worker_coordination`. Each limit has `status` (`enforced`, `advisory`, `unavailable`), nullable
`value`, and nullable `capability_evidence_hash`; `enforced` requires both values,
`unavailable` requires both null, and `advisory` requires a value but permits a null hash.

**Result envelope:** `schema_version`, shared IDs, `session_id`, `status` (`complete`, `blocked`,
`failed`, `refused`, `timed_out_provider_limit`, `timed_out_manager_limit`,
`terminated_by_operator`), `artifact_paths`, `owned_file_changes`, `summary`, `assumptions`,
`open_questions`, `verification`, `observed_route`, `resume_from_session_id`,
`forked_from_session_id`, `usage`, `risks`, and `recommended_disposition`. A terminal status does
not itself claim orchestrator acceptance.

**Descendant manifest:** `schema_version`, shared parent IDs, `completeness` (`complete`,
`incomplete`, `unavailable`), `digest`, and `descendants`. Each descendant uses `descendant_id`,
`run_id`, `lane_id`, `session_id`, `route_decision_id`, `lifecycle_id`, `write_isolation`,
`permission_mode`, `limit_statuses`, `resume_from_session_id`, `forked_from_session_id`,
`observed_route`, `validation_status`, and `terminal_disposition_id`. A complete manifest requires
a digest and every descendant field; an incomplete/unavailable manifest is not comparable.

**Routing event:** only `schema_version`, `event_id`, opaque identity fields, timestamp,
policy/adapter/CLI/schema versions, task class, closure target code, planned/requested/observed route,
packet completeness code, isolation mode, numeric counters, validator outcome code, rework count,
friction codes, disposition code, probe/cohort/hypothesis/falsifier/confounder codes. It contains no
paths, names, prompts, transcripts, command text, tool output, artifacts, or arbitrary `message`,
`summary`, `details`, `text`, or `metadata` field.

**Reconciliation:** `schema_version`, `reconciliation_id`, shared IDs, `result_status`,
`orchestrator_disposition` (`accept`, `revise`, `park`, `reject`), `result_hash`,
`disposition_hash`, and `reconciled_at`. This is the single durable terminal link.

- [ ] **Step 2: Write failing record and bundle tests**

`support.py` loads fixture JSON by name and returns deep copies. `test_contracts.py` must assert:

1. Every valid fixture passes its individual validator and input objects remain unchanged.
2. Missing required and unknown fields raise `ContractError` with an exact dotted path.
3. Delivered fields enforce observed/unobserved/conflicted value/hash rules.
4. Packet limit statuses enforce the value/evidence rules above.
5. Routing events reject `project`, `repository`, `path`, `branch`, `artifact`, `message`,
   `summary`, `details`, `text`, and arbitrary nested metadata fields.
6. A complete descendant manifest with a missing child field fails; incomplete/unavailable remains
   valid but returns `comparable = False` in normalized output.
7. `validate_contract_bundle` accepts an object containing the six valid fixtures and returns
   `reconciled = True` and `comparable = True`.
8. Any mismatched route decision, run, lane, lifecycle, result status, or reconciliation ID fails
   with code `reference_mismatch`.
9. Omitting reconciliation from a terminal result returns `reconciled = False`; it never infers
   acceptance.
10. Two reconciliation objects for one lifecycle fail with code `duplicate_reconciliation`.
11. A result with both resume and fork parents populated fails with code `lineage_conflict`.
12. UUID, timestamp, non-negative integer counters, and SHA-256 fields reject malformed values.

- [ ] **Step 3: Run tests and verify RED**

Run:

```bash
python3 -m unittest -v adapters/codex/delegate-to-claude/tests/test_contracts.py
```

Expected: import failure for contract validators or missing fixture behavior.

- [ ] **Step 4: Implement strict individual validators**

In `contracts.py`, define immutable allowed-field sets and small private validators for route
tuples, delivered observations, permission blocks, limit blocks, lineage, usage, and timestamps.
Compose them into the seven public functions named in this plan. Use `datetime.fromisoformat`
after accepting `Z` as `+00:00`, and require timezone-aware timestamps. Numeric counters are
integers `>= 0`; booleans never count as integers. Return deep-copied normalized dictionaries.

Do not add JSON Schema, third-party validation, runtime persistence, CLI parsing, or a generic
schema engine. This slice's Python validators are the executable schemas.

- [ ] **Step 5: Implement cross-record reconciliation**

`validate_contract_bundle` accepts only `route_decision`, `task_packet`, `result_envelope`,
optional `descendant_manifest`, optional `routing_event`, and `reconciliations` (list). Validate
each record first, then compare shared IDs. A terminal result with zero reconciliations returns
`reconciled = False`; exactly one matching record returns `True`; more than one fails. The function
returns normalized records plus only the derived booleans `reconciled` and `comparable`.

- [ ] **Step 6: Run the full contract suite and verify GREEN**

Run:

```bash
python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

Expected: all tests pass with no warning or filesystem write outside test-owned temporary paths.

- [ ] **Step 7: Self-review and commit only Task 3 files**

Run `git diff --check`; inspect all fixtures for accidental paths, names, or free-text event fields.
Commit subject:

```text
feat(codex): define delegation record contracts
```

Commit body includes `Why`, `Verification`, and `Boundary`; Boundary says records are pure and no
runtime state or model call exists.

---

### Task 4: CI and adapter documentation for the Phase 1A boundary

**Route:** Sonnet high, `acceptEdits`, R5 mechanical fully specified edit under the user's explicit
Sonnet request. Nearest alternative is Opus high. Falsifier: documentation or CI review finds a
boundary claim not supported by the contract tests.

**Files:**
- Modify: `.github/workflows/ci.yml`
- Modify: `adapters/codex/README.md`

- [ ] **Step 1: Add the failing CI expectation locally**

Run the command that CI will add before editing CI:

```bash
python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

Expected: it already passes from Tasks 1–3. This task is a configuration/documentation exception
to production-code TDD: it does not add runtime behavior, and the executable command is already
covered by the new tests.

- [ ] **Step 2: Add one CI step**

After the existing syntax step, add:

```yaml
      - name: Codex delegation contracts
        run: python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

Do not change action versions, triggers, existing checks, or plugin build commands.

- [ ] **Step 3: Document exactly what is canonical now**

Append a `Phase 1A contract core` section to `adapters/codex/README.md` stating:

- the executable schemas and fixtures are canonical in this repository;
- the user-level `delegate-to-claude` preview remains an operational MVP and is not copied policy;
- no session manager, persistent state root, Claude launch, installer, or deployment is included;
- the next independently reviewed slice is read-only `plan --dry-run` consuming these records;
- fake fixtures prove adapter behavior only and cannot establish actual Claude CLI enforcement;
- install/deploy/policy activation remain explicit later actions.

- [ ] **Step 4: Run repository verification**

Run exactly:

```bash
python3 -m py_compile check_state.py check_wids.py install.py adapters/codex/delegate-to-claude/scripts/delegate_to_claude/*.py
python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
python3 check_state.py
python3 check_wids.py
git diff --check
```

Expected: all commands exit 0; `check_wids.py` reports all 23 W-records cited.

- [ ] **Step 5: Self-review and commit only Task 4 files**

Inspect the diff and confirm no unrelated workflow or README content moved. Commit subject:

```text
docs(codex): gate delegation contract core
```

Commit body includes `Why`, `Verification`, and `Boundary`; Boundary states that install and runtime
launch remain deferred.

---

## Subagent-driven execution contract

Execution is sequential because every task consumes the prior task's interfaces. The
`dispatching-parallel-agents` test therefore rejects parallel writers for this slice; there is no
safe write-heavy fan-out. Each task gets a fresh implementer in the same dedicated feature
worktree, followed by a read-only spec-compliance reviewer and then a read-only code-quality
reviewer. Do not start the next task until both reviews pass and all Critical/Important findings
are fixed and re-reviewed.

| Stage | Route | Surface | Class | Basis |
|---|---|---|---|---|
| Tasks 1 and 4 implementer | Sonnet high | preview wrapper, `acceptEdits` | R5 | Fully specified bounded edits; explicit user-requested Sonnet probe. |
| Tasks 2 and 3 implementer | Opus xhigh | preview wrapper, `acceptEdits` | R4 | Security/provenance-bearing implementation. |
| Per-task spec reviewer | Sonnet high | `readonly-review` | R7 | Deep read against supplied task contract. |
| Per-task quality reviewer | Opus high | `readonly-review` | R1 fallback | Finished-artifact review gate; Fable excluded by explicit Opus/Sonnet request. |
| Final whole-slice reviewer | Opus high | `readonly-review` | R1 fallback | Cross-task integration gate. |

Every worker packet must include the complete task text, not merely point at this plan; forbid
descendants; forbid edits outside the task's exact owned files; preserve unrelated dirty work; and
return `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, or `BLOCKED` with files, tests, self-review,
and risks. Reviewers receive no write tools. Requested model/effort is never copied into observed
provenance; use wrapper `modelUsage` only.

The preview wrapper's private state is operational evidence for these authorized calls, not the
canonical state-root decision. Do not use `--max-budget-usd` as a Max-subscription cap. Bound each
implementer to 30 agentic turns and each reviewer to 16 turns. No resume, repair call, permission
broadening, or route substitution occurs without fresh operator authorization after inspecting the
failed attempt.

## Plan self-review

- **Spec coverage:** Covers only proposal Phase 1 sub-slice 1 and explicitly defers all later
  components. Packet, route, lifecycle, result, descendant, event, ownership, privacy, and terminal
  reconciliation requirements each map to a task/test.
- **Placeholder scan:** No unresolved markers or shorthand steps; every file, command, error code,
  enum, and boundary is explicit.
- **Type consistency:** Public function names, identifier prefixes, status enums, and shared IDs are
  locked once and reused across all tasks.
- **Isolation:** One feature worktree, one writer at a time, read-only reviewers, exact owned files.
- **Open stakeholder decisions preserved:** No canonical persistent state root/sub-budget,
  termination implementation, paid smoke-test policy, or Option 2 milestone timing is selected.
