# Task: implement the non-activating C0 policy core

> **Path note (2026-07-24):** `adapters/codex/delegate-to-*` paths in this document refer to the
> runtime trees as they lived in this repository's worktree at writing time. They moved to the
> `delegation-runtime` repository (D-3, 2026-07-24) and were flattened to its root — read
> `adapters/codex/X` as `X` there. Quoted paths are preserved verbatim.

Invoke `$delegation-triage` before creating descendants. Descendants are forbidden for this run.
You are not alone in the codebase: preserve all pre-existing and concurrent work and never revert
or reformat files outside the ownership manifest.

## Objective

Implement every Task 1–8 code and test requirement in
`docs/superpowers/plans/2026-07-20-composable-claude-policy-contract-core.md`, revision 3, using
test-first RED/GREEN steps. Produce an uninstalled, non-activating policy core whose shared pure
primitives live under `adapters/codex/scripts/delegation_policy/`, whose Claude-specific presets
remain in `delegate-to-claude`, and whose only CLI integration is the non-generative `explain`
command.

Treat the plan's exact interfaces, validation rules, comparisons, fixtures, expected commands, and
boundary tests as the acceptance contract. The package-boundary amendment is authoritative where
revision 3 differs from earlier reviewed paths.

## Non-goals

- Do not implement the Gemini/Antigravity adapter or the deferred general router.
- Do not activate or change Claude `run`, `resume`, materialization, reconciliation, installation,
  deployment, skill, route, state, telemetry, or profile-version behavior.
- Do not invoke Claude from tests or code, use network access, install dependencies, download
  anything, run runtime probes, or start monitoring/background services.
- Do not edit user-facing prose, proposals, plans, reviews, README files, handoffs, probes,
  manifests, CI, warrants, routes, or state records.
- Do not stage, commit, push, merge, delete, reset, clean, or otherwise mutate Git history/control
  state.
- Do not create descendants or broaden permissions.

## Ownership

- **Working directory:** repository root (`.`)
- **Isolation:** exclusive writer for the exact code/test surface below; the checkout is already
  dirty with unrelated work that must be preserved.
- **Allowed creates:**
  - `adapters/codex/scripts/delegation_policy/__init__.py`
  - `adapters/codex/scripts/delegation_policy/schema.py`
  - `adapters/codex/scripts/delegation_policy/diff.py`
  - `adapters/codex/scripts/delegation_policy/explain.py`
  - `adapters/codex/tests/test_policy_schema.py`
  - `adapters/codex/tests/test_policy_diff.py`
  - `adapters/codex/tests/test_policy_explain.py`
  - `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/policy_presets.py`
  - `adapters/codex/delegate-to-claude/tests/test_policy_presets.py`
  - `adapters/codex/delegate-to-claude/tests/fixtures/policy/legacy-v3-profiles.json`
- **Allowed modifications:**
  - `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`
  - `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`
- **Forbidden:** every other path and every external side effect not required for local read-only
  inspection or the listed deterministic tests.

## Route and permissions

- **Task class:** bounded agentic implementation; user-directed Sonnet demotion probe relative to
  R4/R5.
- **Requested model / effort:** Sonnet / medium.
- **Permission mode / profile:** auto / `implementation-auto`.
- **Allowed tools:** local Read, Grep, Glob, Skill, Write, Edit, and Bash for repository inspection
  and deterministic Python/Git verification only.
- **Descendants:** forbidden.
- **No paid follow-up:** if blocked, stop and report; do not retry, resume, or switch model/mode.

## Required sources and invariants

Read in this order:

1. `docs/superpowers/plans/2026-07-20-composable-claude-policy-contract-core.md` (revision 3);
2. `docs/reviews/2026-07-20-c0-provider-neutral-package-boundary-amendment.md`;
3. `docs/proposals/2026-07-20-composable-claude-capability-and-scope-policy.md` (revision 4);
4. the existing manager, profiles, runtime policy, reconciliation, and tests needed to preserve
   version-3 behavior.

Load project instructions before editing. The plan already incorporates the dispositioned Sol and
Fable findings. Do not reopen product decisions or silently simplify their semantics.

Critical revision-3 invariants:

- `delegation_policy` uses only the standard library and imports no Claude adapter module.
- Schema, diff, and explanation tests pass with only `adapters/codex/scripts` on `PYTHONPATH`.
- Claude presets import the shared normalizer and keep `PRESET_ASSURANCE` provider-specific.
- `build_explanation(..., *, assurance=None)` receives assurance explicitly and never reads Claude
  presets.
- Direct execution of `claude_delegate.py` locates the repo-local shared scripts directory through
  the narrowly specified import bootstrap.
- `run` and `resume` neither call the C0 code nor change their historical behavior.
- All policy/path/status output remains sanitized as specified.
- The configured 240 MiB maximum and 192 MiB admission/stop values remain explicit preset data;
  C0 does not claim host-wide quota enforcement.

## Verification

Follow each RED/GREEN command in the plan. At the end run:

```bash
PYTHONPATH=adapters/codex/scripts:adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest -v \
  adapters/codex/tests/test_policy_schema.py \
  adapters/codex/delegate-to-claude/tests/test_policy_presets.py \
  adapters/codex/tests/test_policy_diff.py \
  adapters/codex/tests/test_policy_explain.py
PYTHONPATH=adapters/codex/scripts:adapters/codex/delegate-to-claude/scripts \
  python3 -m unittest discover \
  -s adapters/codex/delegate-to-claude/tests -p 'test_*.py' -v
python3 -m compileall -q adapters/codex/scripts adapters/codex/delegate-to-claude/scripts
python3 check_wids.py
python3 check_state.py
git diff --check
git status --short
```

The known acceptable repository-check exception is only `check_state.py` reporting the four
pre-existing records expired on 2026-07-19: `scarcity-mode`, `fable-window-end`, `reviewer-pin`,
and `orchestrator-pin`. Do not edit them. Any other failure is a blocker or incomplete result.

## Return contract

Return one concise structured result containing:

- `STATUS`: `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, or `BLOCKED`;
- exact created/modified files;
- RED evidence and final verification commands/counts/exits;
- proof that historical `run`/`resume` behavior and `PROFILE_VERSION == 3` remain unchanged;
- self-review findings and fixes;
- assumptions, unresolved questions, conflicts, or undeclared changes;
- route provenance actually observed by the runtime, if exposed.

If blocked, preserve partial work and return
`BLOCKED: <what> | NEED: <input> | TRIED: <steps>`. Do not retry, broaden permissions, switch
model/mode, or spend on a follow-up call.
