# C0 policy core execution record

- **Date:** 2026-07-20
- **Closure target:** uninstalled, non-activating C0 policy core and `explain` surface
- **Final status:** implemented; Sol specification-compliant; Sol quality-approved; root-verified
- **Activation:** unavailable; no installed skill/profile/runtime behavior changed
- **Git:** normal `main` worktree, pre-existing dirty/untracked state; no staging or commit
- **Authority:** evidence and implementation record only; no C1–C6 or Antigravity activation

## Artifact lineage

| Artifact | Revision/hash |
|---|---|
| Pre-execution C0 plan | revision 3 — `1e933034723eb82f1e8a2a31e0edf267e8c7a6a597fab9ce95b0d824cd5055c7` |
| [Execution-tracked C0 plan](../superpowers/plans/2026-07-20-composable-claude-policy-contract-core.md) | revision 4 — `dc7c06f21d817ae97836a96337a8f6386e40dd6752731bf324a20f770d003089` |
| [Package-boundary amendment](2026-07-20-c0-provider-neutral-package-boundary-amendment.md) | identifies revision 3; unchanged |
| [Sol specification review](2026-07-20-c0-policy-core-sol-spec-review.md) | `2e62a57d5a6e6c13e98e1d61c9191b89f08a48f4d7d74e8dfd06140811c5e7f9` |
| [Sol quality review](2026-07-20-c0-policy-core-sol-quality-review.md) | `81fb4a8fef3a12efe7aeb74f9a9f1372e2d3fbca0ee9c3fbcf8bdd10b357ca92` |

The revision-3 hash remains the exact contract supplied to the first implementer. Revision 4
changes status, evidence links, and task checkboxes only; it does not change the implemented public
interfaces or policy semantics.

## Implementation surface

Created:

- `adapters/codex/scripts/delegation_policy/{__init__,schema,diff,explain}.py`;
- `adapters/codex/tests/test_policy_{schema,diff,explain}.py`;
- `adapters/codex/delegate-to-claude/scripts/delegate_to_claude/policy_presets.py`;
- `adapters/codex/delegate-to-claude/tests/test_policy_presets.py`; and
- `adapters/codex/delegate-to-claude/tests/fixtures/policy/legacy-v3-profiles.json`.

Modified:

- `adapters/codex/delegate-to-claude/scripts/claude_delegate.py`; and
- `adapters/codex/delegate-to-claude/tests/test_claude_delegate.py`.

The shared package owns normalization, detached private bindings, semantic/authority identities,
directional transition and cache analysis, and sanitized explanation rendering. Claude owns its
presets, assurance evidence, and the non-generative CLI integration. Historical `run` and `resume`
paths remain isolated from C0 calls and `PROFILE_VERSION` remains 3.

## Delegated implementation evidence

One explicitly authorized Claude implementation run used:

- requested route: Sonnet, medium effort, `implementation-auto`;
- observed model: `claude-sonnet-5`; observed effort: unknown;
- run/session ID: `dc76fc9b-06d8-4606-9301-d58851906831`;
- result: provider exit 0, `subtype=success`, `stop_reason=end_turn`, 80 turns;
- directly observed usage: 160 input tokens, 86,480 output tokens, 234,169 cache-creation input
  tokens, and 13,866,792 cache-read input tokens;
- directly observed cost field: USD 6.862731600000004; and
- manager state/log size remained below the configured thresholds.

The wrapper returned reconciliation exit 5 because Python created four ignored `__pycache__` files
outside the exact declared ownership prefixes. The model result and owned source edits were
preserved. No paid resume, repair, or retry was launched. Root accepted the source only after native
remediation, independent review, and fresh verification. The ignored bytecode remains present; no
cleanup/deletion was authorized.

## Review and remediation history

1. The first Sonnet result reported passing tests, but Sol specification review returned ten
   deterministic findings. Root disposition: `revise`.
2. A native Luna XHigh executor added RED counterexamples and fixed validation, canonicalization,
   authority/cache identity, unresolved dimensions, presentation events, explanation safety,
   preset scope, and CLI isolation.
3. Sol re-review found bounded residual malformed-input and confirmation cases. Three RED/GREEN
   correction loops closed them. Final specification verdict: **COMPLIANT**.
4. A fresh Sol High quality review found root-transition, duplicate-private-binding, and malformed
   override defects. Two RED/GREEN correction loops closed them. Final quality verdict:
   **APPROVED**.
5. Root removed three unused test imports and annotated three intentional post-bootstrap imports
   after fresh Ruff evidence exposed the closure issue.

This run is evidence that the initial test plan had validator gaps; it is not evidence for a
universal Sonnet, Luna, or Sol ranking.

## Final root verification

Fresh commands after the final source edit:

| Check | Result |
|---|---|
| Focused shared/preset suite | 87 tests passed |
| Full `delegate-to-claude` discovery suite | 223 tests passed in 22.923 s |
| `compileall` for shared and Claude scripts | exit 0 |
| `ruff check --no-cache` on the C0 surface | all checks passed |
| Non-generative `explain --profile verified-review --compare-profile strict-readonly` | exit 0 |
| `python3 check_wids.py` | PASS; 73 Markdown files after evidence-record creation, 23 W-records defined and cited |
| `git diff --check` | PASS |
| Explicit no-index whitespace checks | PASS for 17 implementation/evidence files |
| `python3 check_state.py` | expected FAIL only for four pre-existing records expired 2026-07-19 |
| User-level delegation state | 10 MiB, below 192/240 MiB thresholds |

The four expired records are `scarcity-mode`, `fable-window-end`, `reviewer-pin`, and
`orchestrator-pin`. They remain `Unchecked` and outside this execution's write set.

## Remaining boundaries and next step

- No install, activation, deployment, runtime probe, network download, monitoring, Dionysus
  change, staging, commit, push, merge, deletion, or cleanup was performed.
- C0 does not establish runtime filesystem, sandbox, MCP, resource, cache, or host-effect
  enforcement.
- C1–C6 remain separately planned/gated work.
- The next approved sequence step is a separate test-first implementation plan for the
  [minimal Antigravity Gemini Flash adapter](../proposals/2026-07-20-codex-managed-antigravity-gemini-flash-adapter.md),
  followed by fake-CLI implementation and only then separately authorized runtime probes.

---

## Amendment 2026-07-24 — reproduction conditions (review D-5)

**Correction, appended rather than rewritten** (this record is historical evidence; the amendment
convention follows `probes/records/P-20260717-sol-b20`).

The "Final root verification" table above reports test counts without the conditions needed to
re-run them. Three artifacts in this lineage report three different totals for overlapping suites —
**195** (the [package-boundary amendment](2026-07-20-c0-provider-neutral-package-boundary-amendment.md)
and the Fable audit disposition), **184** ([Sol quality review](2026-07-20-c0-policy-core-sol-quality-review.md)),
**223** (this record) — and none states its `PYTHONPATH`, interpreter, or discovery root. Per
[`claims-discipline`], a measurement that cannot be re-run from what was written is an assertion.

Re-derived 2026-07-24 on this host:

| Command | Result |
|---|---|
| `PYTHONPATH=adapters/codex/delegate-to-claude/scripts python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests -p 'test_*.py'` | **211 tests, 1 error** before the D-4 fix (`ModuleNotFoundError: No module named 'delegation_policy'`); **223 OK** after |
| same, with `PYTHONPATH=…/delegate-to-claude/scripts:adapters/codex/scripts` | 223 OK, before and after |
| `PYTHONPATH=adapters/codex/scripts python3 -m unittest discover -s adapters/codex/tests` | 74 OK |

So this record's **223 was reproducible only under an unrecorded two-entry `PYTHONPATH`**. The
interpreter also differed: the committed `__pycache__` is `cpython-314`, while this host's default
`python3` is 3.13.13.

**Root cause (review D-4, now fixed):** `delegate_to_claude/policy_presets.py` imported the shared
core with no path bootstrap, while `claude_delegate.py` had one — so library and test imports
resolved only via ambient `PYTHONPATH`. The boundary amendment verified the direction that passes
("the shared package imports with only `adapters/codex/scripts` on `PYTHONPATH`") and never the
direction that fails. Repaired by moving the bootstrap to `delegate_to_claude/__init__.py`, the
package boundary. The CI step in `ci.yml` runs the single-entry form and would have failed.

**No test result above is retracted.** The suites did pass; what was missing was the environment
that makes "223" mean something. Future execution records state the exact command **and** the
interpreter version.
