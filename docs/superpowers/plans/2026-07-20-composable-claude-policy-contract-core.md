# Composable Claude Policy Contract Core Implementation Plan

> **Path note (2026-07-24):** `adapters/codex/delegate-to-*` paths in this document refer to the
> runtime trees as they lived in this repository's worktree at writing time. They moved to the
> `delegation-runtime` repository (D-3, 2026-07-24) and were flattened to its root — read
> `adapters/codex/X` as `X` there. Quoted paths are preserved verbatim.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the non-activating C0 policy core: normalized contracts, detached private bindings,
semantic and authority identities, standard profile presets, directional and unresolved transition
analysis, configurable presentation controls, migration fixtures, and a non-generative `explain`
command.

**Architecture:** Add pure standard-library policy primitives under a provider-neutral Codex package,
`adapters/codex/scripts/delegation_policy/`, rather than inside the Claude adapter. Normalize policy
separately from private path bindings, provider presets, and runtime assurance; compare grants,
denies, ordered limits, and unresolved dimensions explicitly. Keep Claude-specific presets and the
non-generative `explain` command in `delegate-to-claude`. Existing `run` and `resume` paths remain
untouched during C0. Later provider adapters may import the shared primitives, but each adapter must
own its presets, assurance evidence, compilation, and activation gates.

**Tech Stack:** Python 3.12+ standard library, `dataclasses`, `json`, `hashlib`, `argparse`, and
`unittest`. No third-party dependency, YAML parser, installation, network access, paid call, or
runtime profile activation.

---

## Status and boundaries

- **Proposal:** `docs/proposals/2026-07-20-composable-claude-capability-and-scope-policy.md`,
  revision 4.
- **Plan revision:** 4 (execution-tracked; revision 3 remains the pre-execution contract).
- **Reviews:** the revision-2 Sol review and revision-3 Fable correction audit are dispositioned.
- **Correction record:** `docs/reviews/2026-07-20-composable-claude-policy-revision-4-correction-record.md`.
- **Package-boundary amendment:**
  `docs/reviews/2026-07-20-c0-provider-neutral-package-boundary-amendment.md`.
- **Implementation reviews:**
  `docs/reviews/2026-07-20-c0-policy-core-sol-spec-review.md` and
  `docs/reviews/2026-07-20-c0-policy-core-sol-quality-review.md`.
- **Execution record:** `docs/reviews/2026-07-20-c0-policy-core-execution-record.md`.
- **Plan status:** implemented, specification-compliant, quality-approved, and root-verified;
  uninstalled and non-activating. Runtime-profile activation remains separately gated.
- **Closure target:** uninstalled C0 library and CLI surface with deterministic evidence. It must
  not alter `run`, `resume`, materialization, reconciliation, installed skills, or deployed
  profiles.
- **Generated state:** presets explicitly preserve the existing 240 MiB configured ceiling and
  192 MiB admission threshold. C0 tests use temporary directories and create no persistent runtime
  state.
- **Git:** implementation remains untracked in the pre-existing dirty `main` worktree. No staging
  or commit was authorized or performed.

## Planning verification record

Original revision-2 baseline recorded 2026-07-20 before implementation:

- `python3 check_wids.py`: PASS; 62 Markdown files, 23 W-records defined and cited.
- Existing adapter suite: PASS; 195 tests in 21.246 seconds.
- `git diff --check`: PASS.
- `python3 check_state.py`: FAIL only for the four pre-existing routing records that expired on
  2026-07-19: `scarcity-mode`, `fable-window-end`, `reviewer-pin`, and `orchestrator-pin`. They are
  outside this plan's write set and remain `Unchecked` until separately re-verified.

This establishes the historical candidate baseline only. It does not test the unimplemented C0
interfaces or establish any Claude runtime, sandbox, MCP, resource, or cache behavior.
Revision-3 documentation checks and its exact hash are recorded in the package-boundary amendment;
the adapter suite was not re-run for this documentation-only correction.

## Correction coverage

| Dispositioned finding | Plan coverage |
|---|---|
| CA-001 identity/path detachment | Required interfaces; Task 2 Steps 4 and 6; Task 5 |
| CA-002 resource defaults | Task 2 Steps 1, 3, and 5; Task 3 preset limits; Task 4 comparators |
| CA-003 confirmation enum | Task 2 enum/negative test; Task 4 presentation events |
| CA-004 reachable unknown/unavailable | Required interfaces; Task 2 unresolved markers; Task 4 |
| CA-005 deny removal/raw allows | Task 2 root/rule validation; Task 4 grant/deny direction |
| CA-006 command-template schema | Task 2 Steps 1, 5, and 6 |
| CA-007 subprocess mocking | Task 7 two-level boundary tests |
| CA-008 assurance source | `PRESET_ASSURANCE` in Task 3; sanitized output in Task 5 |
| CA-009 presentation precedence | Task 4 current operator-owned policy rule |
| CA-010 registry identity | C0 unresolved marker; resolved identity remains deferred to C1 |
| CA-011 notice `once` state | C0 validates and hashes transition identity; display state remains deferred to C1 |
| CA-012 cross-field validity | Task 2 Step 5 |
| CA-013 directional comparators | Task 4 Steps 1 and 3 |
| Accepted process-control omission | `host_effects` schema/defaults in Task 2 and Task 3; runtime probe remains C3 |

## Worker-owned write set

- Create: `adapters/codex/scripts/delegation_policy/__init__.py`
- Create: `adapters/codex/scripts/delegation_policy/schema.py`
- Create: `adapters/codex/scripts/delegation_policy/diff.py`
- Create: `adapters/codex/scripts/delegation_policy/explain.py`
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/policy_presets.py`
- Modify: `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
- Create: `adapters/codex/tests/test_policy_schema.py`
- Create: `adapters/codex/tests/test_policy_diff.py`
- Create: `adapters/codex/tests/test_policy_explain.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_policy_presets.py`
- Modify: `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`
- Create: `adapters/codex/delegate-to-claude/tests/fixtures/policy/legacy-v3-profiles.json`

Do not edit proposal, plan, review, README, skill, route, warrant, state, probe, installer,
deployment, manifest, or telemetry files. Root owns user-consumed prose. Do not refactor the
existing manager or version-3 resolver during C0.

## Required interfaces

```python
# delegation_policy/schema.py
class PolicyValidationError(ValueError):
    """The requested policy cannot be normalized without guessing."""

@dataclass(frozen=True)
class PrivateBinding:
    binding_id: str
    kind: str
    resolved_path: Path
    lineage_identity: str | None

@dataclass(frozen=True)
class CompiledPolicy:
    document: dict[str, object]
    semantic_sha256: str
    authority_sha256: str
    authority_grants: frozenset[str]
    authority_denies: frozenset[str]
    private_bindings: tuple[PrivateBinding, ...]
    unresolved_dimensions: tuple[str, ...]
    cache_inputs_complete: bool

def normalize_policy(raw: Mapping[str, object]) -> CompiledPolicy:
    """Validate, default, canonicalize, hash, and classify one policy."""

def canonical_document(policy: CompiledPolicy) -> dict[str, object]:
    """Return a detached canonical document suitable for deterministic JSON."""

# delegate_to_claude/policy_presets.py
PRESET_IDS: tuple[str, ...]
PRESET_ASSURANCE: Mapping[str, Mapping[str, str]]
def preset_policy(profile_id: str) -> CompiledPolicy:
    """Compile one canonical preset or compatibility alias."""

def canonical_preset_id(profile_id: str) -> tuple[str, str | None]:
    """Return canonical ID and optional deprecation warning."""

# delegation_policy/diff.py
@dataclass(frozen=True)
class TransitionReport:
    kind: str
    known_kind: str
    broader_authority: tuple[str, ...]
    narrower_authority: tuple[str, ...]
    changed_fields: tuple[str, ...]
    unresolved_dimensions: tuple[str, ...]
    transition_sha256: str
    cache_impact: str
    notice_events: tuple[dict[str, object], ...]
    confirmation_events: tuple[dict[str, object], ...]

def compare_policies(before: CompiledPolicy, after: CompiledPolicy) -> TransitionReport:
    """Describe authority, cache, context, runtime, and presentation changes."""

# delegation_policy/explain.py
def build_explanation(policy: CompiledPolicy,
                      transition: TransitionReport | None = None,
                      *,
                      assurance: Mapping[str, str] | None = None) -> dict[str, object]:
    """Return a sanitized allowlisted explanation."""

def render_text(explanation: Mapping[str, object]) -> str:
    """Render the allowlisted explanation in stable human-readable order."""
```

The shared package must not import Claude adapter modules. Claude passes the selected preset's
assurance labels explicitly to `build_explanation`; other providers may supply their own labels or
omit them. Changing these names or shapes requires a plan revision and correction audit.

---

### Task 1: Freeze the historical candidate boundary

**Files:**
- Create: `adapters/codex/delegate-to-claude/tests/fixtures/policy/legacy-v3-profiles.json`
- Create: `adapters/codex/delegate-to-claude/tests/test_policy_presets.py`

- [x] **Step 1: Run the current suite without edits**

```bash
PYTHONPATH=adapters/codex/scripts:adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest discover \
  -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

Expected: the current historical suite passes. Last recorded count was 195. If current evidence
differs, stop and report it rather than rewriting the baseline.

- [x] **Step 2: Add the version-3 migration fixture**

Create JSON with `profile_version: 3`, the alias `readonly-review -> strict-readonly`, and these
per-profile fields copied from the current resolver: `permission_mode`, `tools`,
`requires_native_sandbox`, `uses_scratch_cwd`, `requires_artifact_output`,
`requires_owned_paths`, and `requires_auto_mode`. Use explicit values, not a generated fixture that
could silently move with the code.

Include `readonly-review` as a key in `fixture["profiles"]` with the resolved `strict-readonly`
values, and retain the alias mapping separately. This fixture intentionally freezes only the listed
historical flag/tool surface; existing snapshot tests remain authoritative for global denies,
pinned MCP identifiers, and manifest hashes.

- [x] **Step 3: Write the fixture compatibility test**

```python
def test_legacy_v3_fixture_matches_current_candidate(self):
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    for profile_id, expected in fixture["profiles"].items():
        commands = (("python3 -m unittest",)
                    if profile_id in {"verified-review", "artifact-review"} else ())
        permission = expected["permission_mode"] if profile_id.startswith("implementation") else None
        actual = resolve_profile(profile_id, permission, (), (), (), commands)
        for field, value in expected.items():
            expected_value = tuple(value) if field == "tools" else value
            self.assertEqual(getattr(actual, field), expected_value)
```

- [x] **Step 4: Run the focused test**

```bash
PYTHONPATH=adapters/codex/scripts:adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest -v adapters/codex/delegate-to-claude/tests/test_policy_presets.py
```

Expected: PASS. This freezes historical evidence; it does not force new presets to retain every
old implementation choice.

---

### Task 2: Implement versioned policy validation, private bindings, and identities

**Files:**
- Create: `adapters/codex/scripts/delegation_policy/__init__.py`
- Create: `adapters/codex/scripts/delegation_policy/schema.py`
- Create: `adapters/codex/tests/test_policy_schema.py`

- [x] **Step 1: Write RED tests**

Add tests named:

- `test_unknown_schema_version_is_rejected_by_dispatch`;
- `test_empty_authority_fields_default_to_deny_or_unavailable`;
- `test_unknown_top_level_and_nested_fields_are_rejected`;
- `test_invalid_notice_and_confirmation_modes_are_rejected`;
- `test_confirmation_once_is_rejected`;
- `test_read_and_write_rules_are_independent`;
- `test_allow_rule_requires_declared_scope`;
- `test_raw_deny_requires_stable_rule_id_and_private_binding`;
- `test_same_policy_different_absolute_bindings_has_same_semantic_and_authority_hashes`;
- `test_changed_root_roles_change_both_hashes`;
- `test_binding_identity_stays_private_and_out_of_explainable_document`;
- `test_notice_change_changes_semantic_but_not_authority_hash`;
- `test_command_template_authority_change_changes_authority_hash`;
- `test_unsandboxed_template_is_authority_bearing`;
- `test_omitted_resources_are_unavailable_not_unbounded`;
- `test_explicit_generated_state_limits_normalize`;
- `test_invalid_limit_mode_value_pairs_are_rejected`;
- `test_selected_command_mcp_and_network_empty_sets_follow_section_18_2`;
- `test_host_effects_default_to_deny`;
- `test_selected_host_effect_requires_known_operation_and_stable_target`;
- `test_system_input_hashes_empty_means_cache_inputs_incomplete`.

- [x] **Step 2: Run RED**

```bash
PYTHONPATH=adapters/codex/scripts \
  python3 -m unittest -v adapters/codex/tests/test_policy_schema.py
```

Expected: missing-module import failure.

- [x] **Step 3: Implement version dispatch, exact enums, and defaults**

Export `CompiledPolicy`, `PolicyValidationError`, `PrivateBinding`, `canonical_document`, and
`normalize_policy` from `delegation_policy.__init__`. The shared package may use Python standard
library modules only and must not import `delegate_to_claude`, Claude profile data, or Claude CLI
code. Add an import-boundary test that loads `delegation_policy` with only
`adapters/codex/scripts` on `PYTHONPATH`.

```python
TOP_LEVEL = {
    "schema_version", "profile", "model_inputs", "context", "runtime",
    "filesystem", "tools", "mcp", "commands", "network", "git",
    "host_effects", "installation", "descendants", "output", "sandbox",
    "resources", "lifecycle", "notices", "confirmation",
}
NOTICE_MODES = {"always", "once", "never"}
CONFIRMATION_MODES = {"ask", "never"}
MCP_MODES = {"deny", "readonly", "selected", "unrestricted", "unavailable"}
COMMAND_MODES = {"deny", "selected", "unrestricted", "unavailable"}
HOST_EFFECT_MODES = {"deny", "selected", "unrestricted", "unavailable"}
HOST_EFFECT_OPERATIONS = {
    "process-signal", "process-debug", "unix-socket", "service-control",
    "device-control", "application-automation",
}
SANDBOX_MODES = {"off", "preferred", "required"}
SANDBOX_UNAVAILABLE = {"fail", "warn-and-run", "run"}
LIMIT_MODES = {"unavailable", "bounded", "unbounded"}
ASSURANCE = {"os-enforced", "claude-enforced", "manager-controlled", "detected", "unknown"}
SUPPORTED_SCHEMA_VERSIONS = frozenset({1})
```

Materialize proposal §18 in `DEFAULT_DOCUMENT_V1`. Deep-copy before normalization. Dispatch on the
requested version before merging; reject unknown versions and fields. Use
`{mode: "unavailable", value: None}` for every omitted resource. Task 3's standard presets
explicitly override the generated-state maximum/admission values. `bounded` requires a positive
integer; `unavailable` and `unbounded` require `None`.

- [x] **Step 4: Implement root/rule detachment and private bindings**

Accept requested root records with `{kind, binding}`. Move `binding` into `PrivateBinding`; leave
`{kind, binding: "bound"}` or `{kind, binding: "unbound"}` in the canonical document. Allow rules
must use `scope` naming a declared root. A raw-path deny must have a stable `rule_id`; move its path
into a private binding keyed by `rule_id` and leave a `private-selector` marker in the document.

`lineage_identity` is supplied by an operator/manager-owned callback or remains `None` in C0. Do
not derive an unkeyed path hash. Sort private bindings by `(kind, binding_id)` and never include
`resolved_path` or `lineage_identity` in either policy hash or `canonical_document`.

- [x] **Step 5: Implement typed command templates and cross-field rules**

Validate every non-empty template against the exact proposal §9.1 fields: `id`, `revision`, `argv`,
`cwd_scope`, `environment.fixed`, `environment.pass`, `stdin`, `write_scopes`,
`wall_time_seconds`, `shared_log_bytes`, `per_file_bytes`, `network.mode`,
`network.destinations`, `sandbox`, and `evidence_id`. All referenced scopes must exist. The
authority-template hash covers every field except `evidence_id`; emit atom
`command:<id>@<authority-template-sha256>`.

Apply proposal §18.2 exactly:

| State | Normalizer action |
|---|---|
| selected commands with no templates | reject |
| selected MCP with no tools/server match | reject |
| selected host effects with no `{operation, target_id}` grants | reject |
| empty network allowlist | normalize to deny |
| readonly MCP without registry identities | accept, append `mcp.registry` to unresolved dimensions |
| sandbox required with commands denied/unavailable | retain as dormant |
| unsandboxed ID without an `outside` template | reject |

- [x] **Step 6: Implement canonical identities and authority projections**

Canonical JSON uses sorted keys and compact separators. SHA-256 the UTF-8 canonical bytes. Atoms
cover symbolic filesystem grants, tools, resolved MCP identities, content-addressed command
templates, network destinations, Git/install/descendant flags, host-effect operation/target grants,
output roots, sandbox
fallback, unsandboxed template hashes, and explicit resource limits. Maintain deny atoms separately.

Compute:

1. `semantic_sha256` from the detached canonical document, including notices and confirmations;
2. `authority_sha256` from an authority-only projection excluding profile labels, context,
   runtime observations, notices, confirmation, assurance, and private bindings.

Use symbolic atoms such as `filesystem.write:scratch`; no path-derived digest belongs in either
hash. A presentation-only change alters the semantic hash but not authority hash or grant/deny sets.

- [x] **Step 7: Implement `normalize_policy`**

It must validate schema version, types, enums, stable IDs, and root references; sort/deduplicate
set-like lists without reordering argv; mark unresolved registry/activation dimensions; compute
cache completeness only when model, effort, runtime version, and a non-empty complete set of
system-input hashes are known; and return `CompiledPolicy`.

- [x] **Step 8: Run GREEN**

Use the Step 2 command. Expected: all schema tests pass.

---

### Task 3: Express standard profiles as non-activating presets

**Files:**
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/policy_presets.py`
- Modify: `adapters/codex/delegate-to-claude/tests/test_policy_presets.py`

- [x] **Step 1: Add RED preset tests**

Cover all five IDs and the alias; project-plus-declared-root reads; review write defaults; native
sandbox `required` for command-capable presets; generic MCP read-only as `unavailable` until a
registry resolves it; independently configurable notices/confirmations; enforcement assurance
labels; host effects denied; explicit 240 MiB/192 MiB generated-state values; unbound symbolic
roots without absolute paths; distinct `preset_revision`/`legacy_contract_version`; and
`runtime.activation == "unavailable"` for every C0 preset.

```python
def test_verified_review_is_non_activating_and_sandbox_required(self):
    policy = preset_policy("verified-review").document
    self.assertEqual(policy["sandbox"]["mode"], "required")
    self.assertEqual(policy["sandbox"]["unavailable"], "fail")
    self.assertEqual(policy["commands"]["mode"], "unavailable")
    self.assertEqual(policy["host_effects"]["mode"], "deny")
    self.assertEqual(
        policy["resources"]["generated_state_bytes"],
        {"mode": "bounded", "value": 240 * 1024 * 1024},
    )
    self.assertEqual(
        policy["resources"]["generated_state_admission_bytes"],
        {"mode": "bounded", "value": 192 * 1024 * 1024},
    )
    self.assertEqual(policy["runtime"]["activation"], "unavailable")
```

- [x] **Step 2: Run RED**

Use the Task 1 focused command. Expected: missing preset symbols.

- [x] **Step 3: Implement literal preset records and alias resolution**

```python
PRESET_IDS = (
    "strict-readonly", "verified-review", "artifact-review",
    "implementation", "implementation-auto", "readonly-review",
)
ALIASES = {"readonly-review": "strict-readonly"}

PRESET_ASSURANCE = {
    "strict-readonly": {
        "built-in-read": "claude-enforced",
        "built-in-write": "claude-enforced",
        "bash-filesystem": "unknown",
        "artifact-materialization": "manager-controlled",
    },
    "verified-review": {
        "built-in-read": "claude-enforced",
        "built-in-write": "claude-enforced",
        "bash-filesystem": "unknown",
        "artifact-materialization": "manager-controlled",
    },
    "artifact-review": {
        "built-in-read": "claude-enforced",
        "built-in-write": "claude-enforced",
        "bash-filesystem": "unknown",
        "artifact-materialization": "manager-controlled",
    },
    "implementation": {
        "built-in-read": "claude-enforced",
        "built-in-write": "detected",
        "bash-filesystem": "unknown",
        "artifact-materialization": "manager-controlled",
    },
    "implementation-auto": {
        "built-in-read": "claude-enforced",
        "built-in-write": "detected",
        "bash-filesystem": "unknown",
        "artifact-materialization": "manager-controlled",
    },
}

def canonical_preset_id(profile_id: str) -> tuple[str, str | None]:
    if profile_id in ALIASES:
        return ALIASES[profile_id], f"{profile_id} is deprecated; use {ALIASES[profile_id]}"
    if profile_id not in PRESET_DOCUMENTS:
        raise PolicyValidationError(f"unknown profile preset: {profile_id}")
    return profile_id, None
```

Do not import historical `profiles.py` from production preset code; migration tests alone compare
the two contracts. Import `normalize_policy` and `PolicyValidationError` from the shared
`delegation_policy` package. Keep assurance outside the policy document and both hashes. Do not
label a C0 runtime surface `os-enforced`; runtime activation remains unavailable.

- [x] **Step 4: Run preset and historical resolver tests**

```bash
PYTHONPATH=adapters/codex/scripts:adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest -v \
  adapters/codex/delegate-to-claude/tests/test_policy_presets.py \
  adapters/codex/delegate-to-claude/tests/test_profiles.py
```

Expected: PASS; historical `PROFILE_VERSION` remains 3.

---

### Task 4: Implement semantic transition, notice, confirmation, and cache analysis

**Files:**
- Create: `adapters/codex/scripts/delegation_policy/diff.py`
- Create: `adapters/codex/tests/test_policy_diff.py`

- [x] **Step 1: Write RED tests**

Test exact, narrower, broader, mixed, and unknown authority; `known_kind == broader` while another
dimension is unresolved; grant addition/removal; deny addition/removal; raw deny rebinding;
allowlist-to-unrestricted; sandbox `required -> preferred -> off`; sandbox fallback
`fail -> warn-and-run -> run`; finite resource increase/decrease; bounded-to-unbounded;
unavailable resource/registry dimensions; profile-only changes; profile change with unchanged
cache; tool/system/runtime change with likely cache invalidation; incomplete cache inputs; every
notice and confirmation set to `never`; operator-current presentation precedence; a presentation
change recorded but not forced visible; and broader/mixed resumes never rejected.

- [x] **Step 2: Run RED**

```bash
PYTHONPATH=adapters/codex/scripts \
  python3 -m unittest -v adapters/codex/tests/test_policy_diff.py
```

- [x] **Step 3: Implement authority classification**

```python
broader = set(after.authority_grants - before.authority_grants)
narrower = set(before.authority_grants - after.authority_grants)
broader.update(before.authority_denies - after.authority_denies)
narrower.update(after.authority_denies - before.authority_denies)
known_kind = classify_known(broader=broader, narrower=narrower)
kind = "unknown" if unresolved_could_change(known_kind, unresolved) else known_kind
```

Comparison never returns `blocked`. Invalid policy fails schema validation; valid broader/mixed
transitions remain reports that callers may run.

Set comparison covers additive capability sets. Directional comparators run before final
classification:

- sandbox isolation: `required < preferred < off` and fallback
  `fail < warn-and-run < run`;
- activatable command/network/host authority: `deny < selected < unrestricted`;
- resource limits: smaller bounded values are narrower, larger are broader;
  bounded-to-unbounded is broader;
- `unavailable` is unresolved activation/runtime state, not an authority rank;
- assurance changes are runtime evidence, never authority ordering.

Merge relations so allowlist-to-unrestricted and 60-to-600 seconds are `broader`, not `mixed`.
When unresolved dimensions could change the aggregate relation, set `kind: unknown` while retaining
`known_kind`, known additions/removals, and the exact unresolved dimension IDs.

- [x] **Step 4: Implement cache analysis**

Cache-relevant paths are model, effort, non-empty complete system-input hashes, built-in tool
definitions, content-addressed command definitions exposed to the model, resolved MCP tool/registry
identities, provider, and runtime version. Return `unchanged`, `likely-invalidated`, or `unknown`.
Profile or presentation identity alone triggers its own event but not a claimed cache miss. Preset-
only comparisons with null model/effort/runtime remain `unknown`; the unchanged-cache test must bind
all inputs explicitly.

- [x] **Step 5: Implement audit events**

Always retain triggered events even when display/confirmation is disabled:

```python
{
    "category": "authority_change",
    "mode": "never",
    "display": False,
    "requires_confirmation": False,
    "summary": "known broader; 1 added grant; 0 removed denies; 1 unresolved dimension",
}
```

Resolve notice/confirmation modes only from the normalized current operator-owned policy. Untrusted
repository input is not accepted as a presentation source. A current `never` takes effect on the
current transition; record the setting change and transition facts privately without forcing one
last display. Produce a stable `transition_sha256` from the two policy identities, known changes,
unresolved dimensions, and category facts; later cohorts use it for once-per-lineage presentation.

- [x] **Step 6: Run GREEN**

Use the Step 2 command. Expected: PASS.

---

### Task 5: Build sanitized explanations

**Files:**
- Create: `adapters/codex/scripts/delegation_policy/explain.py`
- Create: `adapters/codex/tests/test_policy_explain.py`

- [x] **Step 1: Write RED tests**

Require `stage == "compiled"`; symbolic roots and bound/unbound state; distinct preset/legacy
versions; semantic and authority hashes; explicitly supplied assurance labels;
sandbox/fallback/unsandboxed IDs; host effects; resource modes; independent presentation decisions;
known/final transition kinds; unresolved dimensions; cache impact; deterministic output; and
absence of raw paths, binding identities, objective text, prompt text, raw command text, secrets,
executable hashes, and artifact hashes.

```python
def test_explanation_is_sanitized(self):
    with tempfile.TemporaryDirectory() as tmp:
        private_path = str(Path(tmp) / "private-sentinel")
        explanation = build_explanation(
            policy_with_private_path(private_path),
            assurance={"built-in-read": "claude-enforced"},
        )
        rendered = json.dumps(explanation, sort_keys=True)
        self.assertNotIn(private_path, rendered)
        self.assertEqual(explanation["stage"], "compiled")
```

- [x] **Step 2: Run RED**

```bash
PYTHONPATH=adapters/codex/scripts \
  python3 -m unittest -v adapters/codex/tests/test_policy_explain.py
```

- [x] **Step 3: Implement allowlisted JSON and text renderers**

Return only:

```python
{
    "stage": "compiled",
    "schema_version": 1,
    "profile": {
        "id": "verified-review",
        "preset_revision": 1,
        "legacy_contract_version": None,
    },
    "semantic_sha256": "0000000000000000000000000000000000000000000000000000000000000000",
    "authority_sha256": "1111111111111111111111111111111111111111111111111111111111111111",
    "activation": "unavailable",
    "roots": {
        "read": [{"id": "project", "binding": "bound"}],
        "write": [{"id": "scratch", "binding": "bound"}],
    },
    "capabilities": {
        "commands": "unavailable",
        "mcp": "unavailable",
        "host_effects": "deny",
    },
    "resources": {
        "generated_state_bytes": {"mode": "bounded", "value": 251658240},
        "generated_state_admission_bytes": {"mode": "bounded", "value": 201326592},
    },
    "assurance": {"built-in-read": "claude-enforced"},
    "sandbox": {"mode": "required", "unavailable": "fail"},
    "transition": None,
    "unresolved": ["commands.activation", "mcp.registry"],
}
```

Do not serialize the canonical policy wholesale. Validate only the optional assurance mapping
passed by the caller; never import provider presets from this shared module. `render_text` prints
the same fields in stable order and labels unknown assurance.

- [x] **Step 4: Run GREEN**

Use the Step 2 command. Expected: PASS.

---

### Task 6: Add the non-generative `explain` CLI

**Files:**
- Modify: `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
- Modify: `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`

- [x] **Step 1: Write RED CLI tests**

Test JSON/text preset explanation, custom JSON policy, `--compare-profile`, workspace/output and
named read/write bindings, path-independent hashes across two temporary roots, all notice and
confirmation overrides, invalid config exit 2, and proof that explain never invokes the fake
Claude binary or creates state. Existing run/resume tests must remain green.

```python
result = self.invoke(
    "explain", "--profile", "verified-review",
    "--compare-profile", "strict-readonly",
    "--notice", "cache_impact=never",
    "--confirmation", "authority_expansion=never",
    "--format", "json",
)
self.assertEqual(result.returncode, 0, result.stderr)
self.assertFalse(self.args_log.exists())
self.assertFalse(self.state.exists())
```

- [x] **Step 2: Run RED**

```bash
PYTHONPATH=adapters/codex/scripts:adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest -v adapters/codex/delegate-to-claude/tests/test_claude_delegate.py
```

- [x] **Step 3: Implement parsing and `command_explain` only**

Before importing `delegation_policy`, add the repo-local shared scripts directory computed as
`Path(__file__).resolve().parents[2] / "scripts"` to `sys.path` if it is absent. This is import
discovery for a directly executed, uninstalled candidate—not a general plugin search, install, or
activation path. Keep the existing Claude adapter scripts directory behavior unchanged.

```python
explain = sub.add_parser("explain", help="compile and explain policy without a model call")
source = explain.add_mutually_exclusive_group(required=True)
source.add_argument("--profile", choices=PRESET_IDS)
source.add_argument("--policy-file", type=Path)
explain.add_argument("--compare-profile", choices=PRESET_IDS)
explain.add_argument("--workspace", type=Path, default=Path.cwd())
explain.add_argument("--scratch-dir", type=Path)
explain.add_argument("--output-dir", type=Path)
explain.add_argument("--read-root", action="append", default=[])
explain.add_argument("--write-root", action="append", default=[])
explain.add_argument("--notice", action="append", default=[])
explain.add_argument("--confirmation", action="append", default=[])
explain.add_argument("--format", choices=("text", "json"), default="text")
explain.set_defaults(func=command_explain)
```

`command_explain` reads at most one JSON policy file, validates overrides, compiles, optionally
compares, retrieves any Claude preset assurance mapping in the adapter, passes that mapping
explicitly to the shared renderer, renders, and exits. Passing `--policy-file` is an explicit
operator invocation; C0 never
discovers presentation settings from repository files automatically. The command receives no
prompt, Claude binary, state root, or execution flags.

Parse named roots as `NAME=PATH`, reject duplicate/reserved names, and bind paths without creating
them. Resolved paths stay only in `PrivateBinding`; text/JSON output shows the symbolic name and
bound/unbound state. Hash equality across different bindings is a required CLI test.

- [x] **Step 4: Run GREEN**

Use the Step 2 command. Expected: PASS.

---

### Task 7: Prove C0 does not alter runtime behavior

**Files:** existing and C0 tests only.

- [x] **Step 1: Add boundary tests**

Prove `run`/`resume` do not call C0, `PROFILE_VERSION` remains 3, version-only historical
resume behavior remains unchanged, generated Claude settings/argv snapshots remain unchanged, and
`explain` creates no model/MCP/sandbox process or persistent state.

Use two levels:

1. import `claude_delegate` in-process, call `main(["explain", ...])`, patch
   `subprocess.Popen` and `execute_attempt`, and assert neither is called;
2. patch imported C0 entry points during in-process `run`/`resume` calls against the fake CLI and
   assert they are not called. Top-level import of C0 modules is allowed; runtime invocation is not.

Keep the subprocess integration proofs from Task 6: no fake-Claude args log, no state directory,
and unchanged historical settings/argv snapshots. Do not attempt to use `mock.patch` across the
subprocess boundary.

- [x] **Step 2: Run all focused C0 tests**

```bash
PYTHONPATH=adapters/codex/scripts:adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest -v \
  adapters/codex/tests/test_policy_schema.py \
  adapters/codex/delegate-to-claude/tests/test_policy_presets.py \
  adapters/codex/tests/test_policy_diff.py \
  adapters/codex/tests/test_policy_explain.py
```

- [x] **Step 3: Run the complete adapter suite**

```bash
PYTHONPATH=adapters/codex/scripts:adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest discover \
  -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

Expected: all historical and new tests pass.

---

### Task 8: Final deterministic verification and return

**Files:** no additional write scope.

- [x] **Step 1: Compile adapter Python**

```bash
python3 -m compileall -q \
  adapters/codex/scripts \
  adapters/codex/delegate-to-claude/scripts
```

Expected: exit 0 and no output.

- [x] **Step 2: Run repository checks**

```bash
python3 check_wids.py
git diff --check
```

Expected: both pass. Also run `python3 check_state.py`; if it still fails only for the four routing
records expired on 2026-07-19, record that exact pre-existing failure and do not change routes.

- [x] **Step 3: Inspect the exact write set**

Confirm no file outside the owned set changed. Preserve pre-existing dirty/untracked files. Do not
stage, commit, install, deploy, or invoke Claude.

- [x] **Step 4: Return a bounded report**

Return status, exact files, RED evidence, final counts, commands and exits, migration result,
proof run/resume stayed unchanged, unresolved questions, and any conflicts. Do not claim C1–C6
enforcement or activation.

---

## Root review after worker completion

The root must independently test detached path bindings; semantic-versus-authority hashes;
grant/deny direction; exact/narrower/broader/mixed/unknown transitions; known broadening with an
unresolved dimension; warnings-off behavior; cache-only changes; sandbox/resource comparators;
host-effect defaults; sanitized explain output; no process/state creation; and historical runtime
snapshots. It dispositions each file and writes separate C1–C6 plans rather than expanding C0 in
place.

## Deferred plans

- **C1:** built-in read boundaries, configuration-source observation, resolved MCP registry
  identity, private root-binding comparison, and once-per-lineage presentation state;
- **C2:** manager materialization, hard-link/inode counterexamples, overwrite/recovery, and
  retention;
- **C3:** native sandbox, command templates, resources, host-effect denial probes, scratch/cache
  redirection, and supported runners;
- **C4:** worktree/project writes, Git control state, reconciliation, and unsandboxed exceptions;
- **C5:** unattended execution, concurrency, durable recovery, and orphan handling;
- **C6:** host-wide reads, remote MCP, controlled network/credentials, containers/VMs, and Linux.

C0 completion is not evidence that any deferred cohort is safe or available.
