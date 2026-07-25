# Decision panel adjudication — D-1, D-2, D-4, north-star §6 (2026-07-24)

**Process:** first exercise of the operator's standing rule (2026-07-24: decisions get a review
spread before they reach the operator). Two independent legs, distinct lenses, structured
verdicts; adjudicated by the authoring fable session (author of the artifacts under review —
stated, not hidden; the legs are the independence).

**Legs:** `sol-design-reviewer` @ gpt-5.6-sol/xhigh (unstated-assumptions lens; **conflict
disclosed in-output**: the leg is itself one of the `sol-*` definitions at issue in D-2) ·
`reviewer`-contract @ opus/xhigh via Workflow per-call (evidence-sufficiency lens; per-item
firsthand checks incl. the live Codex ledger). Both legs' full structured outputs:
run `wf_62173db0-bc7` journal (session transcript dir). ~237k subagent tokens, 103 tool uses.
Effort note: xhigh was the operator's explicit earlier request; the operator subsequently
observed high would likely have sufficed — consistent with R1's default. Recorded as an
unpaired effort observation, nothing more.

**Spread:** 8 verdicts — 1 CONCUR (opus on D-2), 7 CONCUR_WITH_CHANGES, 0 OBJECT.

---

## D-1 — two-product split: RATIFY, with a compatibility contract as condition

Both legs concur with the same change from opposite lenses: "consumes Product 1 as versioned
data" is not governance. **Condition C1:** Product 1 publishes versioned schemas + conformance
fixtures; delegation-runtime pins supported versions and runs consumer-conformance in its CI;
staged two-release upgrade/rollback. **Condition C2 (opus, verified firsthand by adjudicator:
181 references in 14 tracked md files):** the D-3 move left stale `adapters/codex/delegate-to-*`
paths resolving in NEITHER repo — a propagation debt to sweep (annotate-or-rewrite;
historical-quote passages get a dated pointer note, not silent rewriting). **C3 (opus, MINOR):**
proposals/README still names the consolidated proposal "Leading product-boundary proposal" —
retitle to reflect supersession when ratified.

## D-2 — sol-* stay external: ADOPT (strongest spread)

Opus CONCUR outright (gating fact corroborated firsthand: all three pins resolve only through
the private gateway); sol CONCUR_WITH_CHANGES **with its conflict disclosed** — and its changes
improve the recommendation rather than contest it: (a) R1 must cite **immutable instrument
identity** (probe/contract hash + availability predicate), not a mutable external agent name;
(b) reclassify the trio from perpetual `EXTRA`/"UNOWNED" to a **declared external overlay**
(name them in the manifest as intentional, external, gateway-gated); (c) opus MINOR: fix the
flip-condition instrumentation (contract hashes were recorded "not hashed" in the P-20260717
records — hash them going forward).

## D-4 — rung-table mechanism: ADOPT AS DIRECTION, spec must close three gaps first

The mechanism survives both lenses; the *specification* does not, yet. Gaps to close before
implementation (B-6): **(a) the rung compiles the whole execution contract** — add
contract_id / role / authority profile to the rung image, not just model × effort (sol MAJOR:
frontmatter equality can pass while the executable contract is wrong); **(b) typed condition
semantics** — defaults, overlap resolution, manual override; subjective discriminators
("judgment-discrimination reason") stay allowed but are recorded as stated-reason escapes, not
typed conditions (sol MAJOR); **(c) honest enforcement claims** — the deployed guard hook
cannot deliver the claimed zero-token rung check today, and CI has no frontmatter↔rung-image
comparator; both are build items, not existing capabilities (opus MINOR ×2 — the review's
enforcement-point claims are corrected herein rather than left standing).

## §6 — BIND AS AMENDED (the most-corrected item)

No conflict-of-intent with the Codex ledger — but three of five constraints don't survive
contact with it as written, and both legs converged on the same facts:

- **S6-1 stable IDs:** Codex `event_id`/`run_id` qualify; `project_id` is HMAC-keyed by a
  machine-local salt — same project, two machines, two IDs (sol MAJOR, opus MINOR concordant).
  Amend: define ID scopes (event / run / origin-namespace / project-pseudonym) + rekey
  migration before binding field semantics.
- **S6-2 harness-contract + S6-3 attestation:** absent from the v1 schema AND the strict
  validator rejects unknown fields — so these are **v2 requirements with a dual-read
  migration**, not fields to append (both legs MAJOR). The attestation tier vocabulary also
  doesn't exist yet as an enum anywhere (probes/TEMPLATE.md has a free locator +
  `self-reported`; EPISTEMICS labels are claim-grades, not attestation tiers) — define it.
- **S6-4/S6-5:** Codex already satisfies both in stronger form (allowlist + rejection beats
  field separation) — restate as floors, not designs (opus MINOR).
- **Cost sentence corrected:** "near zero" was true for a greenfield ~14-field record; false
  for a three-schema crosswalk + v2 migration + governance of a schema this repo does not own
  (opus IMPL-1; the north star's §6 is amended in the same pass as this adjudication).
  Schema-change governance across repos/owners = part of D-1's compatibility contract (C1).
- **The `why` free-text field contradicts S6-4** as proposed (routing-relevant but
  content-bearing; opus IMPL-2): re-spec as an enumerated reason-code + optional
  hash-referenced note, mirroring Codex's `*_code` convention.

## Dispositions applied in the same pass (propagation)

1. North star §6 amended: cost sentence corrected; five constraints restated with the
   v2/floor/ID-scope qualifications above; `why` → reason-code.
2. Portfolio review: dated addendum pointing here; its two incorrect enforcement-point claims
   (guard-hook rung check, CI comparator) corrected by reference, not silent edit.
3. MANIFEST: sol-* row reclassified from "UNOWNED (decision owed)" to "declared external
   overlay (D-2 adjudicated; operator ratification pending)".
4. The stale-path sweep (C2) and R1 instrument-identity rewrite (D-2a) are registered as
   work items — B-1 absorbs the R1 rewrite; new item C-4 = the 181-reference sweep.

## What the operator ratifies

Four yes/no items, each = "adopt the recommendation with the panel's conditions as stated
above": **D-1 yes/no · D-2 yes/no · D-4 yes/no · §6-as-amended yes/no.** A "no" on any item
names which condition fails. Until ratified, nothing here is doctrine; the §6 amendment and
MANIFEST reclassification are reversible edits made to keep surfaces honest with this record.
