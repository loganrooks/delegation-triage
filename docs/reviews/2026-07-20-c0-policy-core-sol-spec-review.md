# C0 policy core — Sol High specification review

- **Date:** 2026-07-20
- **Consult:** `c0_spec_review`
- **Reviewer:** GPT-5.6 Sol High, read-only, `fork_turns=none`
- **Target:** current untracked C0 implementation against plan revision 3, proposal revision 4,
  and the provider-neutral package-boundary amendment
- **Verdict:** **NOT COMPLIANT**
- **Root disposition:** **revise**; hold C0 acceptance and activation
- **Authority:** review evidence only; no implementation, activation, install, network, paid call,
  staging, commit, or deletion authority

## Findings

| ID | Severity | Finding | Required correction |
|---|---|---|---|
| SR-01 | High | `schema.py` validates command-template field presence but accepts malformed value types and arbitrary Git mutation modes. | Validate exact field types/enums and raise `PolicyValidationError` for malformed inputs. |
| SR-02 | High | Filesystem default `deny -> allow` changes have no authority atoms and compare as `exact`. | Represent default read/write authority and compare it directionally. |
| SR-03 | High | An `evidence_id`-only command-template change alters `authority_sha256`. | Hash the authority template projection without provenance-only fields. |
| SR-04 | High | Cache analysis compares command IDs rather than content-addressed definitions. | Include command-definition authority hashes in cache inputs. |
| SR-05 | High | Set-like list ordering changes semantic and authority identities. | Sort and deduplicate set-like values while preserving `argv` order. |
| SR-06 | High | Unavailable command/MCP activation is not marked unresolved; transition comparison considers only the after-policy markers. | Preserve exact unresolved activation dimensions from both sides. |
| SR-07 | Medium | Confirmation-only presentation changes produce no event and can collide with notice-only transition identities. | Record both presentation dimensions and hash both policy identities plus category facts. |
| SR-08 | Medium | Explanations omit presentation decisions and unsandboxed IDs and do not validate assurance. | Expand the allowlist, validate injected assurance, and add leak counterexamples. |
| SR-09 | Medium | Implementation presets grant the whole project root rather than declared owned paths plus scratch. | Use an unbound symbolic owned-path root; retain project reads and nonactivation. |
| SR-10 | Low | CLI accepts duplicate named roots; the runtime-isolation test exercises `run` but not `resume`. | Reject duplicates and add a real in-process resume boundary test. |

The reviewer also noted `ResourceWarning` output from the new in-process boundary test. This is a
quality signal rather than a separate specification finding.

## Deterministic counterexamples

The reviewer directly observed:

- `argv: [123]`, malformed environment/stdin/destination values, and
  `git.mutation: arbitrary` normalize successfully;
- `filesystem.defaults.read: deny -> allow` compares as `exact`;
- changing only command `evidence_id` changes `authority_sha256`;
- changing command `argv` under the same template ID can leave cache impact `unchanged`;
- reordering `tools.builtins` changes both policy hashes;
- a `verified-review` preset has no unresolved dimensions; and
- notice-only and confirmation-only presentation changes can share transition identity while the
  confirmation-only change emits no presentation event.

These counterexamples override the worker's passing-test claim for the acceptance decision.

## Verification reported by reviewer

- focused scoped suite: 159 tests passed;
- complete adapter discovery: 219 tests passed;
- `git diff --check`: passed, with the stated limitation that implementation paths are untracked;
- Python tests used `PYTHONDONTWRITEBYTECODE=1`;
- no files were edited and no network/delegation was used.

## Root remediation contract

The root launched one native bounded executor to add a failing regression test for every finding
and implement the smallest correction. No paid Claude retry or resume is authorized. The same Sol
reviewer must re-check the corrected code before the separate code-quality gate. The ambiguous
whole-project write issue is provisionally interpreted as an unbound symbolic `owned` root because
that preserves the proposal's declared-owned-path semantics without selecting an absolute path; a
worker must return `NEEDS_CONTEXT` if the existing schema cannot express that contract cleanly.

## Remediation and re-review outcome

The first remediation pass added 24 failing assertions plus one error before fixes, then produced
78 focused and 220 full-adapter passing tests. Sol re-review closed SR-02 through SR-10 but found
six residual validation/presentation/CLI-test gaps. A second RED pass observed six failures before
fixes and produced 82 focused and 222 full-adapter passing tests. A final direct counterexample
found an unhashable command-template `sandbox` value escaping as `TypeError`; the executor added a
string guard and list/object regression cases.

Final Sol High re-review verdict: **COMPLIANT**.

Final reviewer evidence:

- malformed command-template `sandbox: []` and object values both raise
  `PolicyValidationError`;
- the targeted regressions pass;
- the focused C0/spec suite reported 179 passing tests;
- all SR-01 through SR-10 findings are closed;
- no extra activation or provider coupling was found; and
- `git diff --check` passed, subject to the untracked-file limitation.

This is the specification gate only. C0 remains subject to a separate code-quality review and root
verification and remains uninstalled and non-activating.
