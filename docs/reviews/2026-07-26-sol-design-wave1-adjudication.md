# Cross-vendor (gpt-5.6-sol) wave-1 reviews — spread + adjudication (2026-07-26)

**Instrument:** two standing `codex exec` sessions, native OpenAI auth (NOT the claudex
gateway — deliberately, so the review path shares no transport with the artifacts under
review), sandbox read-only, auto-compact on. **Resumable for later waves:** design session
`019fa059-0781-7633-a6f0-d9a89704bccc` (xhigh), code session
`019fa059-36ce-74b3-8c8c-f14070b59439` (high) — `codex exec resume <id>`.
First live exercise of the ROUTES R1 cross-vendor CANDIDATE lens outside the gateway
instruments; recorded in the v2 ledger as runs `sol-{design,code}-wave1-20260726`
(surface `cli`).

## Verdicts

| session | artifacts | verdict | findings |
|---|---|---|---|
| design @ xhigh | pilot v2 · crosswalk v0.2.2 | **OBJECT** (both artifacts) | XV-1..5 BLOCKER · XV-6..10 MAJOR |
| code @ high | intent_writer.py @ b1a8646 · its 142-test suite | **OBJECT** | SC-1..5 HIGH · SC-6..10 MEDIUM |

Both reports label every claim Observed/Inferred/Verified-by-execution and declare their
verification boundary (the code session could not run temp-backed tests in its read-only
sandbox — 56 non-filesystem tests run there; the full 449 remain green on our side).

## Adjudication — design (XV): all 10 ACCEPTED

Firsthand checks before acceptance: probe TEMPLATE.md field inventory (confirms XV-4/XV-5's
missing evaluator-lineage/rubric fields); pilot §§2.2/6 equal rework credit (XV-2); the
remaining Observed claims are quotes of text this session authored, verified by authorship
+ spot-reads. Dispositions:

- **XV-1 (incumbent asymmetry) — pilot v3, feasibility-only branch adopted:** wave 1
  produces NO overlay proposal under any outcome; a passing wave unlocks a pre-registered
  wave-2 paired substitution trial (identical frozen tasks, Flash AND opus-medium,
  symmetric stopping/retirement, counterbalanced, vendor-blinded adjudication). Sol's
  alternative 2 becomes the only routing-operative instrument.
- **XV-2 (unbounded rework credit) — pilot v3 §2.2:** pre-registered rework budget;
  `rework_actor: root` = negative executor outcome (root-salvage; the B-7 run-1 salvage is
  the local specimen); delegate-rework within one review cycle positive; beyond budget
  negative regardless of actor.
- **XV-6 (freeze) — pilot v3 §3:** task-population pre-registration + exclusion log;
  FP-C legs in separate clean worktrees at same commit, cache noted, order counterbalanced,
  blinded adjudication.
- **XV-5/XV-10 wave-1 slices — pilot v3 §5:** oracle content-digest pinning; wave-end
  closure rule + all-intents denominator.
- **XV-4 local half — probes/TEMPLATE.md:** `evaluator lineage:` field added (vendor/model
  family of each verifying leg + author-separation).
- **XV-3, XV-4 (schema half), XV-5 (evaluation-event separation), XV-7, XV-8, XV-9, XV-10
  (schema half) — REGISTERED as the C-5 interchange-hardening package**, not patched into
  v0.2.x now: each is a commons-scale sufficiency gap (assignment/counterfactual
  provenance; orthogonal evaluator-provenance fields with the tier as derived view;
  evaluation events separate from dispositions; versioned vendor-neutral capability
  profile; endpoint/weights lineage + evidence expiry; hash-fingerprinting/consent tiers;
  completeness accounting). Rationale for registering rather than amending: these change
  the record model, not a field; churning v0.2.x weekly would defeat the §6.1 stability
  §6.4's consumers need. They are now C-5's opening requirements list, and none blocks the
  feasibility-only wave 1. **The XV-9 hash-linkage risk gets an interim §5 consent-text
  caveat at next crosswalk touch.**

## Adjudication — code (SC): all 10 ACCEPTED; fix round dispatched (R4)

Firsthand reproductions before acceptance: SC-2 (NaN `cost_usd` accepted; literal `NaN`
in the JSONL — invalid JSON, a strict reader rejects the store), SC-4 (cross-origin
outcome accepted as non-orphan), SC-5 (duplicate intent per `run_id` accepted). SC-1
(reclaim race) and SC-3 (trailing-newline corruption) accepted from the cited code paths —
the interleavings are unambiguous on read; SC-1 is a direct catch on the Claude-loop's own
F-8 fix (pid+nonce does not make reclaim atomic). Fix directives:

| # | finding | fix |
|---|---|---|
| SC-1 | stale-reclaim race + `_holds()`/`unlink()` TOCTOU | switch to `fcntl.flock` on a lock file (kernel-released; stdlib; CI is ubuntu, local is macOS — both fine); delete the sentinel protocol |
| SC-2 | non-finite floats emit invalid JSON | `math.isfinite` on all numerics + `json.dumps(..., allow_nan=False)` as belt-and-braces |
| SC-3 | newline-less final line corrupted by next append | preflight under the lock: non-empty store must end `\n` else repair/fail |
| SC-4 | joins ignore `origin` | canonicalize omitted origin → `local`; key ALL joins/invariants by `(origin, run_id)` |
| SC-5 | intent identity unenforced | reject duplicate `(origin, run_id)` intents and `(origin, session_id, spawn_ordinal)`; define omitted-session behavior explicitly |
| SC-6 | O(N²) rescans + fixed 30s lease | flock removes the lease; consolidate to ONE scan per write; volume note in README (index deferred, stated) |
| SC-7 | ULID overflow form + non-monotonic same-ms | reject first-char >7; monotonic generator (clamp regression, increment entropy) or documented disclaimer — implementer's call, stated |
| SC-8 | symlink-follow + inherited perms | `O_NOFOLLOW`, `fstat` regular-file check, `fchmod` 0600 |
| SC-9 | date/surrogate/bidi acceptance | `date.fromisoformat` for `as_of`; reject surrogates + bidi controls in display-bearing text |
| SC-10 | fsync unknown-commit | explicit unknown-commit error carrying the `event_id` |

Plus the 12-item test-gap list from the report as suite additions.

**Fix round LANDED and verified (same day):** delegation-runtime `97fbfba` (all ten SC
fixes + 51 tests → suite 193, repo 500) + `4b49aea` (SPEC re-sync, `[SC]`-marked —
adjudicated as implementation hardening, NOT a crosswalk bump: §1 already made `run_id`
origin-scoped; the round enforced existing semantics). Parent verification: suites,
SC-2/4/5/9 reject probes, live store validates clean under the new invariants (16 records,
no grandfathering needed). Two durable byproducts: (1) the implementer's own SC-8 FIFO test
HUNG the suite — the obvious implementation of "reject non-regular files" (open then check)
blocks forever on a planted FIFO; only execution surfaced it (`O_NONBLOCK` fix) — another
runnable-probe datum; (2) the implementer's close-out framing of SC-1, worth keeping
verbatim: F-8's pid+nonce "narrowed the race and read as a fix, and it took a
different-lineage reviewer to see that narrowing a race isn't closing one" — the
cross-vendor leg earns its cost specifically on concurrency/filesystem code, where
same-lineage review inherits the blind spot about what "looks careful."

## What this instrument bought (the meta-result)

Every one of XV-1..10 and SC-1..10 passed through TWO Claude-lineage review rounds
unflagged; the sol report's "why a Claude stack would miss it" table gives structural
reasons (incumbent-protective framing, orchestration-salience, process-independence read
as lineage-independence, incumbent-shaped feature ontology). This is the strongest
single-session evidence yet for R1's cross-vendor lens — recorded as supporting context on
W-001/W-019 (moves no counter; single paired-ish observation, and the sol legs reviewed
LATER revisions than the Claude panels saw, so catch-sets are not strictly comparable
[per: claims-discipline]).
