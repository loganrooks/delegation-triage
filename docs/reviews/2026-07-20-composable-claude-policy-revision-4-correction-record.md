# Revision-4 correction record: composable Claude policy and C0 plan

- **Date:** 2026-07-20
- **Purpose:** bind the dispositioned Fable correction audit to the exact corrected proposal and
  implementation-plan revisions
- **Fable audit:** [correction audit](2026-07-20-composable-claude-capability-and-scope-policy-fable-audit.md)
- **Root disposition:** [finding dispositions](2026-07-20-composable-claude-capability-and-scope-policy-fable-audit-disposition.md)
- **Authority:** documentation evidence only; no implementation, installation, activation, commit,
  paid call, or runtime probe

## Hash lineage

| Artifact | Audited revision/hash | Corrected revision/hash |
|---|---|---|
| [Proposal](../proposals/2026-07-20-composable-claude-capability-and-scope-policy.md) | revision 3 — `bbb76fb05c5e298ebf044220c0f2a4cf72132505c4c98adce60c02ab00a6335e` | revision 4 — `1767aa376be5a1d973d55a0efbd43d75d6e885c1c98bf5ba3f301482c11c417a` |
| [C0 implementation plan](../superpowers/plans/2026-07-20-composable-claude-policy-contract-core.md) | revision 1 — `3d860d04b012fe32be7444a5b33e64dc2005d89fd9e5265090bc735520b73f61` | revision 2 — `dbffe74d45001be01aeed26d0689cde977b506599a4c905998dac89cc2367d25` |

The corrected hashes are external to the artifacts they identify, avoiding a self-referential hash
field. Any later edit requires a new hash record and must not be described as the reviewed revision.

## Correction coverage

| Finding or accepted case | Corrected contract |
|---|---|
| CA-001 | Separate `semantic_sha256` and `authority_sha256`; detach private bindings; compare rebinding as context. |
| CA-002 | Replace overloaded null limits with explicit unavailable/bounded/unbounded records; presets retain 240/192 MiB values. |
| CA-003 | Notices remain always/once/never; confirmations are ask/never. |
| CA-004 | Add `known_kind`, final `kind`, and exact unresolved dimensions; `unavailable` is not authority-ranked. |
| CA-005 | Compare grants and denies directionally; allows require declared scopes; private raw selectors are deny-only. |
| CA-006 | Type and content-address command-template authority fields. |
| CA-007 | Use in-process mocks for call-boundary tests and subprocess integration tests for external effects. |
| CA-008 | Put assurance in a separate versioned preset/operation matrix outside requested-policy hashes. |
| CA-009 | Current operator-owned settings govern; warning-off is honored immediately; facts remain privately recorded. |
| CA-010 | C0 marks unresolved MCP registry identity; C1 must bind resolved record versions/hashes. |
| CA-011 | Define notice `once` identity; C1 owns private per-lineage display state. |
| CA-012 | Add explicit cross-field reject/normalize rules while retaining dormant required-sandbox presets. |
| CA-013 | Add sandbox, network, and resource directional comparators; assurance changes remain runtime evidence. |
| Root rebinding | Add private lineage-scoped binding identity without raw/global path fingerprints. |
| Version namespaces | Separate preset revision from legacy profile-contract version. |
| Migration seam | Dispatch schema version explicitly; defer semantic no-op migration testing until version 2 exists. |
| Hard-link materialization | Add concrete device/inode/link-count counterexamples to C2/C4. |
| Process/socket/service/device/application effects | Add default-denied/unavailable typed `host_effects` contract in C0 and defer enforcement probes to C3/C4. |
| Scratch/cache redirection | Add supported-runner counterexamples to C3. |

## Root deviations from literal Fable remedies

- An unresolved activation/runtime dimension is not ordered below `deny`; the report preserves
  known broadening and separately marks the final relation unresolved when needed.
- Removing a deny is handled by a dedicated directional deny comparison, not by ordinary negative
  set subtraction.
- Disabling a notice takes effect on the current operator-owned invocation; the adapter does not
  force the previous setting's “last warning.”
- Enforcement assurance is not an authority ordering.
- The command-template schema is defined in C0 rather than rejected until C3 because it is an
  authority-bearing contract primitive even though compilation remains deferred.

## Remaining gates

The corrected proposal and plan authorize no implementation by themselves. C0 execution requires
a separate user decision. C1–C6 still require their own plans, deterministic verification, and
separately authorized runtime probes before activation.

## Verification record

Recorded after the corrected proposal and plan hashes were fixed:

- `python3 check_wids.py`: PASS; 66 Markdown files, 23 W-records defined and cited, and all local
  links resolve.
- `git diff --check`: PASS.
- trailing-whitespace and placeholder scans: PASS.
- fenced-code counts are balanced: 20 fence lines in the proposal and 44 in the plan.
- proposal and plan SHA-256 values exactly match the corrected hashes in this record.
- the existing adapter baseline remains the independently observed 195 passing tests from earlier
  in the same session; it was not re-run after these documentation-only corrections.
- `python3 check_state.py`: FAIL only for the pre-existing `scarcity-mode`, `fable-window-end`,
  `reviewer-pin`, and `orchestrator-pin` records that expired on 2026-07-19. They remain outside
  this correction's write set and are treated as `Unchecked`.

No code, installed skill, route, warrant, state record, probe, runtime profile, or deployment
surface was changed by this correction.
