# PROBE — 2026-07-12 signal-layer Proposal F review pair (fable×opus, 3 lenses)

- probe_id: P-20260712-signal-layer-proposal-f-review-pair
- task class / ROUTES row: R1 (review gates / adversarial verification) — document class
  (governance proposal prose, not code)
- configs compared (model × effort × surface × harness): fable high × 3 lenses vs opus
  high × 3 lenses, `reviewer` roster agent both sides (opus via Agent-tool model
  override), byte-identical prompts per lens, legs independent
- harness/contract hash (if pinned): prompts recorded verbatim in the parent session
  transcript (session 0e2615c2); artifact reviewed at signal-layer commit `8d8fbb1`
- blinded?: yes — no leg saw any other leg's output (opus legs launched after fable legs
  completed, but with no findings passed in)
- frozen tree?: artifact = committed file at `8d8fbb1`; working tree not formally frozen
  (no edits to the artifact occurred during the review window — asserted by the author,
  not attested)
- adjudicator: **author** (main loop authored the artifact AND adjudicated the diff) —
  the W-001 deviation class
- router: operator directed the opus probe explicitly ("do a parallel set of reviews
  using opus… parallel and independent"); fable legs routed by main loop (Fable 5,
  session-inherited) per R1 pin — that unasked fable fleet is itself logged as
  signal-layer ledger event obs-20260712T163022-63b800
  (`shared/unasked-premium-tier-usage`)
- **attestation:** parent-session transcript JSONL
  (~/.claude/projects/-Users-rookslog-Projects-signal-layer/0e2615c2-….jsonl) carries
  all six full review outputs; synthesis + per-finding dispositions committed at
  signal-layer `proposals/reviews/2026-07-12-proposal-f-panel.md` (commit `b3aea1b`)
- verdict: **concordant with W-001 — neither tier dominated.** Verdict distribution
  identical. All blocker/structural findings convergent across tiers. Unique catches
  both sides.
- unique catches (per leg): opus-falsifiability — the cycle's highest-value finding
  (no-op refactor passes all wave-2 tests; stub-resolver prediction adopted);
  opus-fidelity — resolver status-tag spec gap; opus-scope — read the literal ADR file,
  literal-vs-generalized gate-id note. fable-fidelity — 14-finding granular sweep incl.
  dropped ARC clauses, silent-unevenness, mirror-timing (5 restorations opus missed);
  fable-scope — CC-head-retrofit authority edge. Cross-tier adjudication: 1 fable false
  positive ("majority smuggled") refuted by opus's primary quote.
- tokens / cost (if observable): fable legs ≈179k subagent tokens; opus legs ≈188k
  (harness usage counters, Reported). Near-identical volume; tier premium bought no
  volume. Per W-015 (fable ≈2.5× opus per token), fable panel ≈2.4× opus panel cost.
- **tally:** feeds W-001 demote counter (cross-tier firings): deviated-concordant — count
  after this record: 2 clean / 4 deviated (was 2/3). W-019 floor NOT met; NO demotion;
  direction stays Contested, now with one more concordant firing.
- deviations from clean protocol (named): author-adjudicator; tree not formally frozen;
  lens prompts pre-specified 4 attack questions each (tight contract — compresses any
  framing-level tier differential; see caveat below).
- record locator(s) + minimal verbatim excerpt(s): signal-layer
  `proposals/reviews/2026-07-12-proposal-f-panel.md` §3: *"the opus panel was
  competitive with the fable panel — equal on convergent structural findings, ahead on
  the one highest-value unique catch"*. **Caveat registered same day (operator
  framing-question):** this probe measured execution of a tightly-specified review
  contract, NOT open/framing review ("are we asking the right questions?") — the task
  design plausibly suppresses exactly the differential a fable premium would buy.
  Framing-review class (≈R8/R15 territory) remains UNPROBED in paired form; the
  session's fable/xhigh advisor thread produced framing-quality moves but had no opus
  baseline (unpaired, Unchecked).
