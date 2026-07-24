# PROBE — 2026-07-24 R4 effort-frontier (REGISTERED, not yet run)

- probe_id: P-20260724-r4-effort-frontier
- task class / ROUTES row: **R4 — coding / agentic implementation** (currently `opus xhigh`,
  `implementer` pin)
- configs compared (model × effort × surface × harness): **opus-5 medium** vs **opus-5 xhigh**,
  identical harness, identical packet, on an R4-shaped task from this operator's actual work.
  Optional third leg: opus-5 high. All legs via the `implementer` pin's contract with the model ×
  effort delivered per-call (Workflow `agent()` is the only surface that pins both — CONTRACT §3).
- harness/contract hash (if pinned): to be recorded at run time
- blinded?: legs blind to each other; adjudicator blind to leg identity where the artifact allows
- frozen tree?: **required** — same starting SHA for both legs
- adjudicator: **non-author required.** The vendor evidence is suggestive enough that an
  author-adjudicated result will not be worth much here.
- router: registered by the root session (Opus 5, session effort) on operator ratification
  2026-07-24
- **attestation:** registration only — rubric and predictions pre-registered below. No leg has run.
  Nothing is claimed about R4's correct effort.
- verdict: **not run**
- unique catches (per leg): n/a
- tokens / cost (if observable): to be recorded; the cost axis is half the point (see PH-2)
- **tally:** feeds **W-024** claim (c) — *medium-vs-xhigh shape*. Count after this record:
  **0 local**. Per W-019, n=1 never flips R4; this class is flip-prone, so budget ~3/side.
- deviations from clean protocol (named): none yet

## Why registered now

[W-024] records two **official vendor sources that disagree** about Opus 5's effort shape on
coding work:

- **O5-SC p. 151 (FrontierCode)** — sharply non-monotonic. Main: `Low 41.9 · Medium 53.4 ·
  High 48.0 · XHigh 43.6 · Max 48.0`. On this evidence, R4's `xhigh` pin is close to the worst
  available effort.
- **anthropic.com/news/claude-opus-5, 2026-07-24 charts** — monotonic rise through xhigh with a
  slight max regression, across Frontier-Bench v0.1, CursorBench, and the AA Coding Agent Index.

`Frontier-Bench v0.1` (mini-SWE-agent harness, GKE backend) is **not** `FrontierCode` Main/Extended
despite the near-identical name. Neither source is licensed to settle the other, and neither runs
our harness on our task mix. That is exactly the condition the probe loop exists for: a Contested
row is a probe to run, not a prior to trust (CONTRACT §2).

## Pre-registered predictions

- **PH-1 (direction):** on an R4-shaped task under our harness, opus-5 **medium** will not be
  materially worse than **xhigh** on first-pass acceptance. *Falsifier:* xhigh passes review on a
  task medium fails, twice.
- **PH-2 (cost):** medium will cost **≤60%** of xhigh for comparable accepted output. *Falsifier:*
  medium's rework loop erases the saving — measured as total cost to accepted artifact, not cost
  per attempt. This is the metric that matters and the one the vendor charts do not supply for our
  workload.
- **PH-3 (shape):** if the FrontierCode reading transfers, xhigh will be **worse than medium**, not
  merely equal. A null result (medium ≈ xhigh) resolves the Contested label toward the news-page
  charts and licenses a *cost-based* demotion without a capability claim.

## What a result would and would not license

**Would:** replace W-024 claim (c)'s `Contested` label with a direction; with ≥2 attested
concordant legs per side, support demoting R4's default effort and re-pinning `implementer`.

**Would not:** transfer to R7, R10, or R13. R13 is separately **blocked** — the Opus 5 system
card's multi-agent runs used a pre-release model and an unreleased effort configuration (bundle
claim C13), so no orchestration effort conclusion is available from vendor evidence at all.

## Cost discipline

No bespoke spend. Run at the next naturally-arising R4 task large enough to be informative, as a
paired lane. A run manufactured to close this probe would trade the thing that makes the tally
worth having.

## Coupling note

R4's default effort and the `implementer` pin frontmatter must flip **in the same commit** if this
probe ever moves the row (CLAUDE.md, profile ↔ pin coupling). The pin is what actually spawns;
ROUTES is what is read.
