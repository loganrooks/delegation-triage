# C0 provider-neutral package-boundary amendment

- **Date:** 2026-07-20
- **Status:** root-authored plan correction; not an external review
- **Authority:** documentation evidence only; no implementation, installation, activation, paid
  call, runtime probe, staging, commit, or deployment
- **Trigger:** the approved
  [minimal Antigravity Gemini Flash adapter proposal](../proposals/2026-07-20-codex-managed-antigravity-gemini-flash-adapter.md)
  requires a reusable policy seam without importing Claude-specific adapter code
- **Prior correction record:**
  [revision-4 correction record](2026-07-20-composable-claude-policy-revision-4-correction-record.md)

## Observed mismatch

Revision 2 of the C0 plan described normalized policy as provider-neutral, but placed schema, diff,
and explanation modules under `delegate_to_claude`. It also coupled the shared explanation builder
to Claude's preset assurance mapping. That layout would make a minimal Antigravity adapter either
import Claude-owned code or duplicate policy primitives.

This is an architectural package-boundary defect in the plan, not evidence that the reviewed
policy semantics were wrong. The prior Fable audit did not review this later multi-provider reuse
requirement.

## Decision

Revision 3 moves only pure policy primitives to
`adapters/codex/scripts/delegation_policy/`:

- schema validation, normalization, identities, and private bindings;
- directional transition and cache analysis; and
- sanitized explanation rendering.

Claude-specific presets, assurance evidence, command compilation, CLI behavior, and runtime
activation remain under `delegate-to-claude`. The shared explanation API accepts an optional
caller-supplied assurance mapping and may not import provider packages. The directly executed
Claude CLI gets one explicit repo-local import bootstrap; this is not plugin discovery,
installation, or activation.

Provider-neutral here means reusable among Codex-managed provider adapters. It does not claim a
cross-harness package, stable public API, or completed general router.

## Hash lineage

| Artifact | Prior corrected revision/hash | Amended revision/hash |
|---|---|---|
| [C0 implementation plan](../superpowers/plans/2026-07-20-composable-claude-policy-contract-core.md) | revision 2 — `dbffe74d45001be01aeed26d0689cde977b506599a4c905998dac89cc2367d25` | revision 3 — `1e933034723eb82f1e8a2a31e0edf267e8c7a6a597fab9ce95b0d824cd5055c7` |

The proposal remains revision 4 at
`1767aa376be5a1d973d55a0efbd43d75d6e885c1c98bf5ba3f301482c11c417a`.
The prior correction record remains unchanged and continues to identify the exact revision-2 plan
that incorporated the dispositioned Fable findings. This amendment identifies revision 3; it does
not retroactively describe revision 3 as Fable-reviewed.

## Contract impact

Unchanged:

- policy schema semantics and default-deny/unavailable posture;
- semantic and authority identity rules;
- private path detachment;
- transition, cache, notice, confirmation, and resource semantics;
- the 240 MiB configured maximum and 192 MiB admission/stop threshold in Claude presets;
- C0's non-activating boundary; and
- the requirement for separate later activation plans and probes.

Changed:

- pure-module and shared-test paths;
- the explanation API now accepts optional assurance explicitly;
- Claude presets import the shared normalizer rather than a sibling Claude module; and
- verification proves the shared package imports with only `adapters/codex/scripts` on
  `PYTHONPATH`.

## Alternatives rejected or deferred

- **Leave primitives inside the Claude adapter:** rejected because it creates false provider
  ownership and import coupling.
- **Duplicate the primitives in the Antigravity adapter:** rejected because identities and
  transition semantics could drift.
- **Move Claude presets into the shared package:** rejected because preset assurance and runtime
  availability are provider-specific.
- **Build the full provider-neutral router now:** deferred by the stakeholder; the shared package
  is a bounded extension seam, not premature router implementation.
- **Publish or install a user-level package now:** deferred; C0 remains an uninstalled repository
  candidate.

## Remaining gates

This amendment does not authorize C0 execution. After documentation verification, the stakeholder
may separately authorize the revised C0 plan. The Antigravity adapter still requires its own
test-first implementation plan after C0 is implemented and independently reviewed.

## Verification record

Recorded after the revision-3 plan hash was fixed:

- `python3 check_wids.py`: PASS; 69 Markdown files, 23 W-records defined and cited, and all local
  links resolve.
- `git diff --check` and explicit no-index whitespace checks for the three new documentation
  artifacts: PASS.
- trailing-whitespace, stale-path, and placeholder scans: PASS.
- Markdown fence count across the Flash proposal, revised C0 plan, and this amendment is even.
- the C0 plan SHA-256 exactly matches the revision-3 hash in this record; the Flash proposal hash
  is `c72274926bc943b18f96ce0adf38d2ce2b5049b732ad9c0e47295b86292bea50`.
- `python3 check_state.py`: FAIL only for the pre-existing `scarcity-mode`, `fable-window-end`,
  `reviewer-pin`, and `orchestrator-pin` records expired on 2026-07-19. They are outside this
  amendment's write set and remain `Unchecked`.
- the 195-test adapter baseline was not re-run for these documentation-only edits.

No model, network, install, activation, staging, commit, runtime, or telemetry operation was
performed as part of this amendment.
