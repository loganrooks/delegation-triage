# Capability-Based Claude Profiles Implementation Plan

> **Path note (2026-07-24):** `adapters/codex/delegate-to-*` paths in this document refer to the
> runtime trees as they lived in this repository's worktree at writing time. They moved to the
> `delegation-runtime` repository (D-3, 2026-07-24) and were flattened to its root — read
> `adapters/codex/X` as `X` there. Quoted paths are preserved verbatim.

> **Status: superseded on 2026-07-19.** This plan produced a useful uninstalled candidate, but root
> review found that it treated exact Bash strings as enforcement, checked startup manifests only
> after execution, omitted aggregate resume-state enforcement, and did not implement owned-path
> reconciliation. Continue with
> [Capability-Based Claude Profiles Corrective Implementation Plan](2026-07-19-capability-based-claude-profiles-corrective.md).
> Preserve this file as execution history; do not resume or edit its checkboxes.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking, but the worker must not edit this plan.

**Goal:** Promote the working Codex-to-Claude preview manager into the canonical adapter and add versioned, fail-closed execution profiles without allowing profile arguments to silently broaden authority.

**Architecture:** Keep profile resolution in a small pure module and process/session behavior in the existing stdlib-only manager. Profiles resolve to immutable permission, built-in-tool, allowed-tool, denied-tool, and resume-compatibility manifests. The manager records both the requested manifest and Claude's observed startup tool manifest; worker-written review artifacts continue to use deterministic materialization unless a later sandbox proves exact-path writes.

**Tech Stack:** Python 3.12+ standard library, `unittest`, Claude CLI structured JSONL, existing repository checks.

---

## Authority and ownership

This execution slice is **code and tests only**. The Sonnet worker owns exactly:

- `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
- `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/__init__.py`
- `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/profiles.py`
- `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`
- `adapters/codex/delegate-to-claude/tests/test_profiles.py`
- `.github/workflows/ci.yml`

The worker may read the deployed preview under the operator's Codex skill directory, but must not
edit it. It must not edit any Markdown file, including this plan, the proposal, README, skill,
references, handoff, route/warrant/state surfaces, or probe records. It must not install, deploy,
commit, push, fetch, use the network, create descendants, or alter generated artifacts.

The existing dirty `README.md`, probe records, and untracked `docs/` tree are user/root-owned.
Any undeclared modification is a scope failure.

## Locked behavior

The canonical profile IDs and permission modes are:

| Profile | Permission mode | Built-in tools | Purpose |
|---|---|---|---|
| `strict-readonly` | `dontAsk` | `Read,Grep,Glob,Skill` | Source-only investigation; no Bash or writes. |
| `verified-review` | `dontAsk` | `Read,Grep,Glob,Skill,Bash` | Read-only review with packet-declared bounded commands. |
| `artifact-review` | `dontAsk` | same as `verified-review` | Verified review whose successful stdout is manager-materialized. |
| `implementation` | `acceptEdits` | `Read,Grep,Glob,Skill,Bash,Write,Edit` | Scoped implementation; ownership is packet-enforced and root-reconciled. |
| `implementation-auto` | `auto` | same as `implementation` | Same authority, auto interaction mode. |

`readonly-review` is a deprecated alias for `strict-readonly`. Store both `profile_requested` and
canonical `profile`; emit one stderr warning before launch. The profile version is integer `1`.

Profile invariants cannot be overridden. A redundant matching `--permission-mode` is accepted;
a mismatching value returns `2` before state creation or model launch. An explicit `--tool` or
`--allowed-tool` may only narrow or exactly match a profile contract. New tools require custom mode
(no profile). Extra `--disallowed-tool` values may narrow a profile.

`verified-review` and `artifact-review` require one or more repeated `--allowed-command` values.
Each value is a complete argv-like command string used to form a Claude permission rule. Reject
empty values, newlines, NUL, shell control operators (`;`, `&&`, `||`, `|`, redirects), command
substitution, backticks, and wildcard characters. Convert an accepted command `python3 -m
unittest discover` to `Bash(python3 -m unittest discover)` and pass it through `--allowedTools`.
This is deliberately conservative; arbitrary Bash is custom mode, not verified review.

All profiles deny `WebFetch`, `WebSearch`, agent/descendant tools, and these known mutating
codebase-memory tools:

- `mcp__codebase-memory-mcp__delete_project`
- `mcp__codebase-memory-mcp__index_repository`
- `mcp__codebase-memory-mcp__ingest_traces`
- `mcp__codebase-memory-mcp__manage_adr`

Strict and verified profiles additionally deny `Write`, `Edit`, and `NotebookEdit`; strict denies
`Bash`. Exact duplicate deny entries are removed while preserving first occurrence.

The structured `system/init` event may contain `tools` and `mcp_servers`. Record their names in the
attempt as `observed_tool_manifest`; compute `unexpected_tools` as observed names that are neither
requested built-ins nor explicitly denied. A strict or verified run with unexpected tools is
terminally recorded and returns nonzero even if the result event claims success. Explicitly denied
tools may be exposed by Claude but do not count as unexpected; they remain recorded.

Resume reuses the stored canonical profile/version/manifests exactly. The `resume` command accepts
no permission, profile, tool, command, or directory override. Any broader boundary requires a new
run. Store a SHA-256 hash over the normalized resolved profile manifest so drift is observable.

`materialize` gains `--attempt N`. Without it, use the latest successful terminal attempt rather
than simply the latest attempt. Refuse failed, truncated, or result-less attempts and existing or
symlink outputs.

---

### Task 1: Promote the preview manager under canonical tests

**Files:**
- Create: `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`

- [ ] **Step 1: Copy the existing preview test into the canonical test path only**

Adjust only `SKILL_ROOT`/`SCRIPT` path discovery so the test points at the planned canonical
manager. Do not change assertions yet.

- [ ] **Step 2: Run the canonical test and verify RED**

Run:

```bash
python3 -m unittest -v adapters/codex/delegate-to-claude/tests/test_claude_delegate.py
```

Expected: failure because the canonical manager does not exist.

- [ ] **Step 3: Copy the deployed preview manager into the canonical script path**

Preserve behavior byte-for-byte except path-neutral comments. Do not add profile behavior in this
step.

- [ ] **Step 4: Run the canonical test and verify GREEN**

Run the Step 2 command. Expected: the promoted baseline tests pass.

- [ ] **Step 5: Inspect only Task 1 paths**

Run `git diff --check` and confirm no deployed preview or Markdown file changed. Do not commit.

---

### Task 2: Add a pure versioned profile resolver

**Files:**
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/__init__.py`
- Create: `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/profiles.py`
- Create: `adapters/codex/delegate-to-claude/tests/test_profiles.py`

- [ ] **Step 1: Write failing profile tests**

Create tests for this public API:

```python
from delegate_to_claude.profiles import (
    PROFILE_VERSION,
    ProfileError,
    canonical_profile_id,
    resolve_profile,
)
```

The returned immutable record exposes `profile_id`, `profile_requested`, `version`,
`permission_mode`, `tools`, `allowed_tools`, `denied_tools`, `allowed_commands`, `warning`, and
`manifest_sha256`.

Required tests:

```python
def test_readonly_review_alias_is_strict_and_warns(self):
    resolved = resolve_profile("readonly-review", None, (), (), (), ())
    self.assertEqual(resolved.profile_id, "strict-readonly")
    self.assertEqual(resolved.permission_mode, "dontAsk")
    self.assertIn("deprecated", resolved.warning)

def test_implementation_auto_rejects_conflicting_permission(self):
    with self.assertRaisesRegex(ProfileError, "implementation-auto.*auto"):
        resolve_profile("implementation-auto", "acceptEdits", (), (), (), ())

def test_matching_permission_is_redundant_but_valid(self):
    resolved = resolve_profile("implementation-auto", "auto", (), (), (), ())
    self.assertEqual(resolved.permission_mode, "auto")

def test_verified_review_requires_a_bounded_command(self):
    with self.assertRaisesRegex(ProfileError, "allowed-command"):
        resolve_profile("verified-review", None, (), (), (), ())

def test_shell_composition_is_rejected(self):
    for value in ("python3 -m unittest; rm x", "pytest && curl x", "echo $(id)", "echo `id`"):
        with self.subTest(value=value), self.assertRaises(ProfileError):
            resolve_profile("verified-review", None, (), (), (), (value,))

def test_extra_denies_narrow_without_duplicates(self):
    resolved = resolve_profile("strict-readonly", None, (), (), ("WebFetch", "CustomTool"), ())
    self.assertEqual(resolved.denied_tools.count("WebFetch"), 1)
    self.assertIn("CustomTool", resolved.denied_tools)
```

Also assert exact profile snapshots, stable hashes, rejected tool broadening, accepted exact/narrow
tool lists, command-to-`Bash(...)` conversion, invalid profile IDs, and no warning for canonical
names.

- [ ] **Step 2: Run focused tests and verify RED**

Run:

```bash
PYTHONPATH=adapters/codex/delegate-to-claude/scripts python3 -m unittest -v adapters/codex/delegate-to-claude/tests/test_profiles.py
```

Expected: import failure for `delegate_to_claude.profiles`.

- [ ] **Step 3: Implement the minimal resolver**

Use a frozen dataclass for the resolved record and a frozen internal profile definition. Normalize
lists to tuples. Serialize the manifest with `json.dumps(..., sort_keys=True,
separators=(",", ":"))` before hashing. `ProfileError` is a `ValueError` with concise deterministic
messages. No filesystem, subprocess, environment, or network access belongs in this module.

- [ ] **Step 4: Run focused and baseline tests**

Run:

```bash
PYTHONPATH=adapters/codex/delegate-to-claude/scripts python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

Expected: all tests pass.

- [ ] **Step 5: Inspect Task 2 paths and do not commit**

Run `git diff --check`; confirm there are no documentation edits.

---

### Task 3: Integrate profiles into new-run command construction

**Files:**
- Modify: `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
- Modify: `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`

- [ ] **Step 1: Extend the fake CLI and write failing integration tests**

The fake CLI must preserve its existing behavior and record `--allowedTools`, `--disallowedTools`,
and `--tools`. Add tests asserting:

1. every canonical profile resolves to its exact permission mode and tool manifest;
2. `readonly-review` stores requested and canonical IDs and prints one deprecation warning;
3. `implementation-auto` plus `acceptEdits` exits `2`, creates no run directory, and never calls
   the fake CLI;
4. verified review without `--allowed-command` fails before launch;
5. accepted commands appear under `--allowedTools` as exact `Bash(...)` rules;
6. known MCP mutators and profile-specific write tools appear under `--disallowedTools`;
7. custom mode still requires explicit `--permission-mode` and preserves existing direct-write
   behavior;
8. metadata contains `profile_requested`, canonical `profile`, `profile_version`,
   `profile_manifest_sha256`, `tools`, `allowed_tools`, and `disallowed_tools`, but no prompt or
   raw command text.

- [ ] **Step 2: Run the manager test and verify RED**

Run the Task 1 command. Expected: new assertions fail against the promoted baseline.

- [ ] **Step 3: Integrate the resolver minimally**

Add parser choices for the five canonical IDs plus alias and repeated `--allowed-tool` and
`--allowed-command`. Call `resolve_profile` before creating the run directory. Pass allowed tools
through Claude's `--allowedTools`; keep built-in exposure under `--tools` and denies under
`--disallowedTools`. Persist only normalized rules and hashes, not raw shell or prompt content.

For custom mode, retain current semantics; `profile`, `profile_requested`, version, and manifest
hash are null. Never let an explicit flag replace a profile invariant.

- [ ] **Step 4: Run all canonical adapter tests**

Run the Task 2 Step 4 command. Expected: all tests pass.

- [ ] **Step 5: Inspect the exact diff and do not commit**

Confirm no docs or deployed skill changed.

---

### Task 4: Record effective startup tools and preserve every successful attempt

**Files:**
- Modify: `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
- Modify: `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`

- [ ] **Step 1: Write failing startup-manifest and materialization tests**

Extend fake `system/init` events to emit configurable `tools` and `mcp_servers`. Add tests that:

1. store observed tool and MCP server names per attempt;
2. treat requested tools plus explicitly denied exposed tools as expected;
3. return nonzero and record `unexpected_tools` for an unknown, non-denied tool under strict or
   verified review;
4. do not apply strict-manifest failure to custom or implementation profiles, but still record it;
5. resume reuses the same canonical profile version/hash and accepts no override flags;
6. `materialize --attempt 1` writes attempt 1 after attempt 2 exists;
7. default materialization selects the latest successful terminal attempt when the latest attempt
   failed;
8. truncated, failed, missing-result, symlink, and overwrite refusals remain intact.

- [ ] **Step 2: Run focused tests and verify RED**

Run the Task 1 command. Expected: the new assertions fail.

- [ ] **Step 3: Implement manifest comparison and attempt selection**

Normalize observed names to sorted unique strings. Store `observed_tools`, `observed_mcp_servers`,
and `unexpected_tools` inside each attempt. Strict enforcement applies only to
`strict-readonly`, `verified-review`, and `artifact-review`.

Add a pure helper that selects a numbered attempt or scans attempts in reverse for the latest
successful terminal untruncated attempt with a successful result event. Parser `--attempt` accepts
positive integers only. Never overwrite or rewrite prior stream files.

- [ ] **Step 4: Run all adapter tests**

Run the Task 2 Step 4 command. Expected: all tests pass.

- [ ] **Step 5: Run privacy and state checks**

Inspect metadata fixtures for prompt bodies, raw command strings, auth identity, and tool output.
Run `git diff --check`. Do not commit.

---

### Task 5: Add canonical CI coverage

**Files:**
- Modify: `.github/workflows/ci.yml`

- [ ] **Step 1: Inspect the existing CI job and write the expected local command first**

The canonical command is:

```bash
PYTHONPATH=adapters/codex/delegate-to-claude/scripts python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
```

- [ ] **Step 2: Run the command locally before editing CI**

Expected: all adapter tests pass. This is the precondition for wiring CI, not the RED phase of
production behavior.

- [ ] **Step 3: Add one CI step using the exact command**

Do not change action versions, triggers, permissions, or existing checks.

- [ ] **Step 4: Run the full repository verification**

Run:

```bash
PYTHONPATH=adapters/codex/delegate-to-claude/scripts python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
python3 check_state.py
python3 check_wids.py
git diff --check
```

Expected: every command exits `0`.

- [ ] **Step 5: Return without committing**

Return status; exact changed files; RED and GREEN commands observed; test counts; assumptions;
permission denials; and any unexpected or user-owned diff. Do not edit documentation to report the
result.

---

## Root-only follow-up after worker disposition

The root—not Sonnet—will:

1. inspect every code/test/CI diff and reject undeclared changes;
2. run fresh adapter and repository checks;
3. author the token-efficient canonical `SKILL.md` and progressive-disclosure references;
4. add installer/deployment behavior only after source behavior is verified;
5. baseline-test the skill instructions, verify word/token growth, and preserve strict semantics;
6. obtain any remaining installation/deployment authority before replacing the user-level preview.

No paid runtime smoke test is part of Sonnet's task.
