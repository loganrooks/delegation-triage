# Gemini Flash adapter plan — Sol High cold review

- **Date:** 2026-07-20
- **Consult:** `gemini_adapter_plan_review`
- **Reviewer:** GPT-5.6 Sol High, read-only, `fork_turns=none`
- **Target:** adapter implementation plan revision 1
- **Initial verdict:** **REVISE**
- **Final verdict:** **APPROVED** at revision 4; see the final correction audit below
- **Root disposition:** **accept all findings**; issue a documentation-only revision 2 before
  implementation
- **Authority:** review evidence only; no implementation, `agy` invocation, probe, activation,
  install, network, staging, commit, or deletion

## Findings

| ID | Priority | Finding | Root disposition |
|---|---|---|---|
| APR-01 | P0 | Task Packet v1 and its private-binding channel lacked exact fields, types, limits, CLI syntax, privacy checks, C0 mapping, non-goals, escalation conditions, and thinking setting. | Accept; freeze packet, binding, CLI, and normalization contracts. |
| APR-02 | P0 | Capability records lacked trusted provenance, production/test separation, binary identity, adapter-owned grammar/parser IDs, environment controls, and profile matrices. | Accept; production records must be explicit external operator artifacts, binary-bound, and unable to inject flags/parsers. |
| APR-03 | P0 | Profile permission controls did not fail closed for network, external writes, install, Git, descendants, commands, and host effects. | Accept; permission-related unknown/detected states cannot activate either profile. |
| APR-04 | P0 | Result, lifecycle, locking, crash recovery, evidence, and exit-code contracts were conceptual. | Accept; define frozen v1 enums, layout, journal, lock, recovery, and result schema. |
| APR-05 | P1 | Investigation lacked mutation reconciliation and implementation lacked a dedicated linked-worktree predicate. | Accept; empty-ownership reconciliation for investigation and primary-checkout rejection for implementation. |
| APR-06 | P1 | Worktree delta and three-stream generated-state accounting were unspecified. | Accept; retain truthful sampled semantics and define exact positive-delta/log/watchdog behavior. |
| APR-07 | P1 | The write set omitted the proposal's skill/usage surface and a non-generative authority explanation. | Accept; add root-owned uninstalled skill/README and provider-aware `compile` command. |

## Conservative decisions for revision 2

- Unknown permission/host-effect enforcement keeps a profile unavailable. There is no generic
  permission-related `accepted unknown` path.
- Only provider-global state accounting may be accepted as sampled/unknown, and only with an
  explicit stakeholder risk-decision ID in a separately approved production record.
- Production capability records must be outside the project/workspace, owned by the current user,
  non-symlinked, non-group/world-writable, dated, and bound to binary realpath/hash/version and the
  current platform.
- Capability records select adapter-owned grammar/parser IDs; they cannot supply arbitrary flags,
  commands, regexes, or executable paths.
- Test records enter only through dependency injection unavailable from the production CLI.
- Actual prompt/result/permission semantics remain unknown until separate probes and therefore do
  not block fake-first implementation.

## Strengths retained

- fake-first, live-unavailable closure;
- clean C0/provider separation and no premature router/runtime extraction;
- no-shell argv and private prompt transport;
- distinct planned/requested/observed provenance;
- one paid attempt with no automatic retry;
- detection rather than rollback; and
- broad fake failure and regression matrices.

## Review limitations

The reviewer inspected the plan/proposals, C0 public interfaces, and existing budget/reconciliation
interfaces. No tests, network, `agy`, files, commits, or telemetry writes were used. The review does
not decide whether either profile can eventually satisfy its activation matrix; that remains a
probe and stakeholder decision.

## Revision 2 correction audit

- **Reviewer:** same GPT-5.6 Sol High consult, preserving the review thread
- **Target hash:**
  `4567b581a3bffca81c3b28d70bff60c2edfe779551b8a2ce7a8054aa9c9a7595`
- **Verdict:** **REVISE**
- **Root disposition:** accept the two residual P0 defects and all bounded P1 corrections; issue
  plan revision 3 before another correction audit

The reviewer found APR-05 closed; APR-01, APR-02, APR-06, and APR-07 partially closed; and APR-03
and APR-04 still open. The accepted residuals were:

1. introduce `not-applicable` rather than using activation-failing `unavailable` for irrelevant
   profile-matrix cells;
2. freeze exact metadata, journal, Result Record, locking, and live-orphan semantics;
3. require packet mode `0600` and deterministic no-follow/file-swap validation;
4. stop attempting to recognize shell commands, credentials, or paths in arbitrary private prose;
5. make recordless `compile` succeed as explicitly unavailable while keeping `run` record-gated;
6. require fresh static-parser-backed model listing immediately before generation;
7. map the shared 16 MiB log budget into C0 `resources.log_bytes` and specify direct provider-log
   overgrowth termination;
8. bind materialization to the run's predeclared output root; and
9. restrict first-release read roots to the canonical Git workspace instead of leaving external
   root reconciliation undefined.

Actual prompt/result grammar, permission/sandbox enforcement, network and host-effect denial,
provider-global state, and provider log behavior remain activation-only unknowns. The correction
audit did not run tests, use network, invoke `agy`, or change files.

## Revision 3 correction audit

- **Reviewer:** same GPT-5.6 Sol High consult
- **Target hash:**
  `8a635a0069f1760eb4e9ef12e9a37fddf6361416826341f350134556e845d7ad`
- **Verdict:** **REVISE**
- **Root disposition:** accept all three narrow deterministic corrections; issue revision 4

The reviewer found that revision 3 accidentally rejected the intentional project-root/owned-path
nesting required by implementation, lacked a `recovery-changed` journal event for the frozen
live-orphan behavior, and contradicted recordless/empty-command compilation. Revision 4 therefore:

1. permits project-as-umbrella nesting while rejecting owned-owned and unintended root overlaps;
2. freezes the recovery event and valid lifecycle/recovery transitions;
3. validates model/thinking syntactically when compiling without a record; and
4. maps empty command-template IDs to C0 `deny`, using `selected` only for a nonempty set.

The audit confirmed all other revision-3 corrections and preserved live-runtime semantics as
activation-only uncertainty. It verified the target hash and performed no writes, tests, network,
or `agy` invocation.

## Revision 4 final correction audit

- **Reviewer:** same GPT-5.6 Sol High consult
- **Reviewed content hash:**
  `a28b40aea5035ea033fa614707a810b3678b39c0eeb6d67921d187bd23a45ac5`
- **Verdict:** **APPROVED**
- **Confidence:** 0.99
- **Root disposition:** accept; the plan is ready for a separate fake-first execution decision

The reviewer confirmed that intentional project→owned nesting, the live-orphan journal transition,
recordless model/thinking validation, and empty-command C0 mapping are all internally consistent.
It found no new P0/P1 fake-first implementation blocker and confirmed the previously accepted file
trust, activation matrix, prelaunch model check, lifecycle/result, log-budget, output-confinement,
and canonical-read-root contracts remained intact.

The plan's subsequent status-only edit records this approval and does not change an implementation
contract. The resulting final plan hash is
`872a0f2875f99247ca2c770be7af4c5ba40b465acf6951751683c3d491a5d6d0`. Actual authentication,
prompt/result/model parsing, permissions, sandboxing, network and
external effects, and provider-global state remain separately authorized activation questions. The
review used no tests, network, `agy`, writes, installation, staging, or commits.
