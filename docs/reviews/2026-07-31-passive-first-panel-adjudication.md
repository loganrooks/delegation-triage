# Passive-first reprioritization — panel adjudication (2026-07-31)

Panel: three single-lens reviewer legs (opus×high, claude-code-teammate surface, DELIVERY
clause; verbatim reports in the driver session transcript, session c4ca9689/9e739566) over
`docs/proposals/2026-07-31-passive-first-reprioritization.md` @ 42cf94c. Two legs
independently executed the data plane (parsed all 131 live v2 records); the runnable leg
built and ran the projector the proposal describes.

## Verdict matrix

| leg | lens | verdict |
|---|---|---|
| ppr-leg-commons | commons alignment / foreclosure | CONCUR_WITH_CHANGES (2 blockers) |
| ppr-leg-parsimony | parsimony / honest scope | CONCUR_WITH_CHANGES (2 blockers) |
| ppr-leg-runnable | runnable evidence (P1 executed) | CONCUR_WITH_CHANGES (3 blockers on P1 as specced) |

**No leg objects to the ranking itself.** All three affirm the gap is real (no
decomposition item owns ledger consumption) and the direction follows the north star's §2
and §7.1. Every blocker is against the draft's *claims and specifications*, not the
priority order.

## Adjudicated dispositions (all ACCEPTED; the revision at v2 carries them)

**A. The empirical premise was false as written (parsimony F1 BLOCKER · runnable MINOR-11
— concordant, both measured).** All 131 ledger records are research-program exhaust
written deliberately by an expensive router (fable-5 or sol at high/xhigh); zero records
come from ordinary non-meta work; no automated writer is wired into any hook. The draft's
"cheap path quietly worked… as a side effect of ordinary orchestration" inverted its own
evidence — a claims-discipline failure in my draft, accepted without reservation.
Restated in v2: the write path is proven cheap; passive capture from ordinary use is the
UNTESTED hypothesis, and E-1 is its test.

**B. P1's headline axis is empty by design; the enum is the upstream precondition
(commons M3 · parsimony F2 BLOCKER · runnable BLOCKER-1 — triple-concordant, all
measured: `task_class.class` null 57/57, writer fails closed per crosswalk §2a).**
v2 makes publishing the §2a candidate class enum P1's first deliverable, explicitly
pulling that C-5-orbit item forward, and requires the rollup to report its own null-class
rate.

**C. Writer-side schema fixes are P1 acceptance criteria, not follow-ons (runnable
BLOCKER-2/3, MAJOR-4/5/7/8/9; parsimony F2/F3).** Measured defects the rollup must force:
features-inclusive harness-contract hash with the zero sentinel abolished (15/57 zero-sha;
one real hash spans three contracts with differing `tool_profile`/`review_gate`); friction
enum extended from the ~34 observed free-text families (43/50 coded entries are `other`);
model-id normalization (`opus-5` vs `claude-opus-5` fragments the binding axis);
attestation tier currently a constant column (131/131 driver-attested); host-harness axis
inexpressible outside prose. Unit of account = run collapsed on `terminal` with
attempts-per-run as a named output (the shipped `summarize` reads retries as failures:
57% per-record vs 74% per-run on the same corpus — and the existing `summarize` is v2's
stated baseline; P1 is the increment over it, not a from-scratch workstream).

**D. Fail-loud beats wait-for-migration (runnable's judgment, adopted).** Building the
rollup now is the cheapest forcing function on the schema — two of the blockers were found
in twenty minutes of running it — PROVIDED it emits `UNDERIVABLE`/`NO-IDENTITY`/
`UNKNOWN-CONTRACT` as first-class cells and refuses decision-grade output below the flip
floor (24/35 cells in the live corpus are n=1; nothing in the current table can move a
route row, and the rollup must say so itself).

**E. The scope disclaimer was false (commons BLOCKER 1 · parsimony F4 — concordant).**
v2 names its revisions instead of disclaiming them: it revises north-star §4's layer
ordering (a status-2 hypothesis, revisable on evidence, revised explicitly with the
trial-day warrant); it demotes ROUTES.md from sole carrier to commentary-over-evidence
(named as an architectural change, with the selector/profile layer given a distinct named
home per commons M6); and it assigns the rollup's product home explicitly (delegation-
runtime builds it; this repo specifies and consumes it) under D-1's compatibility
contract.

**F. P2's feedback affordance breached §6.4 (commons BLOCKER 2).** v2 specifies enumerated
reason-codes drawn from the registered friction vocabulary + an optional hash-referenced
note that is local-only by construction, and says plainly the note never leaves the
machine (W3's consent-screen honesty preserved).

**G. Falsifier selection + trial-channel starvation (commons M4 · parsimony F7 —
concordant).** v2 exempts falsifier-testing work (B-5's cross-harness transfer test
foremost) from the experiment demotion and time-boxes the ranking to one rollup cycle,
with the paired-trial channel re-evaluated at §9 review — otherwise XV-1's only promotion
channel is starved while hypothesis-records accumulate that XV-1 forbids acting on, and
the attestation tiers (already a constant column) never diversify.

**H. Aggregation discipline (commons M7/M9).** The rollup spec gains §3's requirements:
every cell carries its transformation list and source event_id set; no cell collapse
(scalar-leaderboard guard); a Contested/disagreement state; and the rollup surfaces
proposals, never applies a route (W1's known bug not reproduced).

**I. Smaller accepted items.** Rename P1 "route-evidence rollup" — "projection" is
already three other things in this vocabulary (parsimony F6). The CONTRACT §1 clause moves
to `probes/TEMPLATE.md` as a requested field (`passive-signal alternative considered:`),
labeled convention-only per B-4, and reworded to the promotion tier ("could passive signal
*promote* this claim under H3's discipline?") (parsimony F5 · commons M8). P3 folds into
C-5 (parsimony F10 — its only new scope, registry-less two-operator pooling, becomes a
C-5 requirement; §8's no-new-proposal-cycle honored rather than half-invoked). Operator
ruling gets a locator; H4/§7.1 citations restated as hypotheses-to-test, not warrants
(F8/F9). README proposal map updated in the same pass (commons M10).

## What was probed and found sound (both directions preserved)

The ledger instrument itself: 131/131 parse, run_id joins 57/57 with zero orphans,
terminal/ordinal modeling 100% well-formed — "the spine is sound and that is the
expensive part." The ranking's §7 alignment: local-first honored, opt-in/consent honored,
no §7 commitment foreclosed by the ordering itself; XV-1 textually untouched; §9 restated
faithfully (modulo G above); all cited artifacts exist on disk.
