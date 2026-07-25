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

**Schedule note (fable leg, 2026-07-24, operator batch-2 disposition):** the paired high-vs-xhigh renewal run (P-20260724-B in the opus-5 proposal, W-016 renewal) is SCHEDULED — surface: Cowork Workflow agent() (per-call model AND effort, the only dual-knob surface per CONTRACT §3), next Cowork session. Recorded schedule = closure per the campaign termination rule; running it converts W-004/W-016 from Unchecked-for-opus-5 to measured.

## Run 1 — 2026-07-25, Cowork Workflow agent() dual-knob (recorded by the fable leg)

- **task:** naturally-arising R4 — `dio-offload` kit v1 (dionysus D6 durable-offload CLI), fully
  specified packet, identical for both legs. No bespoke spend (the kit was needed regardless).
- **configs:** opus-5 **medium** vs opus-5 **xhigh**, sequential for cost attribution; blind
  labels fixed by author (A=xhigh, B=medium; judge instructed to evaluate A fully, then B, then
  re-check A). Adjudicator: **non-author**, blind, opus-5 high, structured verdict, ran both test
  suites itself.
- **result:** **medium ACCEPT** (spec 9 · robustness 8 · safety 9; 0 MAJOR / 9 MINOR) vs
  **xhigh REJECT** (9 · 7 · 8; **1 MAJOR** + 5 MINOR) — winner medium, margin *narrow*. The xhigh
  MAJOR: silent wrong-host split-brain (`rsh()` hardcoded the host while rsync honored
  `$DIO_REMOTE` and the README documented the override) — structurally untestable by its own
  29-assertion suite, found only by the blind judge.
- **PH-1** (medium not materially worse on first-pass acceptance): **SUPPORTED, n=1** — the
  inverse of the falsifier occurred (medium passed review where xhigh failed).
- **PH-2** (medium ≤60% cost): **Underdetermined as worded** — agent tokens medium 66,213 vs
  xhigh 73,358 (~90%); on the pre-registered metric (total cost to *accepted* artifact) medium
  reached accepted at 66k while xhigh never reached accepted.
- **PH-3** (xhigh worse, not merely equal): directionally observed — n=1, one task class.
- **deviations (named):** legs sequential, not parallel; first medium-leg attempt killed by a
  session usage limit at 35,487 tokens (excluded; clean re-run); A/B assignment fixed, no RNG on
  the surface; spec authored by the recording session.
- **tokens:** medium 66,213 · xhigh 73,358 · judge 89,110 (workflow-reported).
- **artifacts:** adopted kit = medium leg + 3 post-adjudication MINOR fixes (host-prefix
  de-doubling in push/pull, BatchMode made non-overridable), tests 21/21; deployed
  from the operator's Development dir (env-specific: dio-offload) → apollo `bin/dio`; live smoke `dio-smoke2` **done rc=0** on
  dionysus (survives disconnect — the assessment's load-test disconfirmer answered).
- **tally:** W-024(c) local count → **1** (direction: medium ≥ xhigh). Per W-019 n=1 never
  flips: R4 stays medium-Provisional; probe stays open, budget ~3/side.
