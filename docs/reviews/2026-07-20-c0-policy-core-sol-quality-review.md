# C0 policy core — Sol High code-quality review

- **Date:** 2026-07-20
- **Consult:** `c0_quality_review`
- **Reviewer:** GPT-5.6 Sol High, read-only, `fork_turns=none`
- **Target:** specification-compliant C0 implementation
- **Final verdict:** **APPROVED**
- **Root disposition:** **accept** after two bounded remediation passes
- **Authority:** review evidence only; no activation, install, staging, commit, deletion, network,
  or runtime-probe authority

## Initial findings and disposition

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| QR-01 | High | Root kind/binding metadata could change authority identity while comparison reported `exact`. | Fixed: root authority changes are unresolved context; resolved exact transitions require equal authority hashes. |
| QR-02 | Medium | Duplicate raw-deny IDs allowed ambiguous, order-dependent private bindings. | Fixed: conflicting paths are rejected and exact duplicates deduplicate deterministically. |
| QR-03 | Medium | Malformed custom-policy `output`, `notices`, or `confirmation` sections plus overrides escaped with tracebacks. | Fixed: section/override shapes validate before mutation and return exit 2. |

The first re-review confirmed QR-01 through QR-03 behavior but found one internally inconsistent
report: a root-projection mismatch was `unknown` with zero unresolved dimensions. The bounded fix
adds `filesystem.roots` and `authority.projection`, exposes triggered context events, and includes
the reasons in explanations and transition identity.

## Final approval evidence

The reviewer independently verified:

- root-kind and binding-status changes carry both unresolved reason IDs;
- residual authority-projection mismatch carries `authority.projection`;
- root context notices are triggered and displayed while unrelated mismatches do not falsely
  trigger context notices;
- explanation output includes the unresolved reasons;
- reconstructed transition hashes match, and removing an unresolved reason changes the hash;
- bound-path-only rebinding remains authority-exact while triggering context presentation; and
- no new quality finding remains.

Reviewer checks:

- scoped suite: 184 tests passed with `-B` and `PYTHONDONTWRITEBYTECODE=1`;
- deterministic root, binding, residual-projection, explanation, and hash counterexamples passed;
- `ruff check --no-cache` passed on the final corrected surface; and
- no files, network, delegation, staging, or commits were used by the reviewer.

The implementation remains untracked in a pre-existing dirty `main` worktree. Git cannot supply
historical attribution for the untracked adapter tree; root verification and the external worker's
pre/post reconciliation provide the available evidence.
