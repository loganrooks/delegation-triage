# LITERATURE SWEEP — 2026-07-12 Fable 5 vs Opus 4.8 published benchmarks (NOT a probe)

- record class: literature/benchmark sweep (explorer-light sonnet/medium, web, W-014
  hygiene enforced in the contract); feeds W-014 exemplars, W-015 context, and the
  task-class transferability question raised by P-20260712-signal-layer-proposal-f-review-pair
- attestation: full sweep text in parent-session transcript (signal-layer session
  0e2615c2, 2026-07-12); agent-tagged CONFIRMED/REPORTED/UNCERTAIN per claim
- **status: raw ingest — numbers below are the sweep agent's tags, NOT yet graded to
  this repo's EPISTEMICS source classes. Do not promote into WARRANTS cells without a
  grading pass.**

## Headlines (agent's tags preserved)

- **Vendor concentration claim [CONFIRMED — anthropic.com/news/claude-fable-5-mythos-5,
  direct fetch]:** "The longer and more complex the task, the larger Fable 5's lead
  over our other models."
- **Pattern across located data (Reasoned over REPORTED data):** Fable's lead is
  largest on long-horizon multi-step work (FrontierCode Diamond 29.3 vs 13.4 ≈2×;
  SWE-bench Pro 80.3 vs 69.2; Terminal-Bench 2.0 multi-file refactoring +8.6pts) and
  smallest or REVERSED on short/single-shot/bounded tasks (Terminal-Bench incident
  response −0.7 to Opus; Vending-Bench: Opus ahead; GDPval-AA +2.2% near-parity).
- **Review/critique/judge task class: NO published fable-vs-opus benchmark exists**
  (sweep question 1 — closest find is a weak single-blogger rubric study of
  fable-authored skills applied to opus, not a tier comparison). The R1 task class is
  publicly unmeasured; local probes are the only evidence.
- **W-014 vindicated, three exemplars:** AA "Claude Fable 5 (with fallback)" page +
  9%-fallback disclosure [CONFIRMED — AA X post + model page]; GPQA Diamond dual-score
  93.18 (fallback-retried) vs 55.56 (refusals-as-failures) — ~38pt swing on scoring
  convention [REPORTED via deeplearning.ai/the-batch]; ExploitBench/BioMysteryBench
  "Fable" scores are actually Opus's (≈100% classifier interception; vendor quote
  "our classifiers prevent Fable from making any progress on these tasks"
  [CONFIRMED-adjacent, fetched page]).
- Most fable-favoring aggregator numbers are FALLBACK-UNSTATED (SWE-bench Pro/Verified,
  FrontierCode, Terminal-Bench). ARC-AGI-2: contradictory (89.0 vs "no number exists")
  — UNRESOLVED. AA Intelligence Index composites conflict across write-ups — UNRESOLVED.
- Unverified sensational item, flagged not chased: X-sourced claim of non-US
  withdrawal 2026-06-12 under export-control — treat as unestablished.

## Routing relevance (caller's judgment, recorded for the WARRANTS grading pass)

Benchmarks corroborate-in-direction BOTH halves of the local picture: (a) parity/noise
on bounded, tightly-scaffolded tasks — the regime the P-20260712 review pair sat in;
(b) fable's premium concentrating in long-horizon open-ended autonomy — which is
adjacent to, but NOT identical with, the framing-review/advisor class (short-horizon
but judgment-dense; vendor's advisor-tool guidance in W-022 is the closer support
there). Net: published benchmarks neither confirm nor challenge the review-gate
parity finding — the task class is simply unmeasured publicly, so LOCAL probes carry
the full evidential load for R1, and the framing-review class remains unprobed
everywhere (local + published).

## Sweep cost note

~362k subagent tokens at sonnet/medium — roughly 2× either review panel's volume.
Tier is not the dominant cost dial on web sweeps; token volume is.
