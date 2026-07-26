# P-20260726 — B-7 intent-writer build (R4 ×2 runs) + conformance gate (R1) — outcome observations; move no counter

- **What ran:** the D-B3-2-authorized B-7 build. Run-1: `implementer` pin (opus/medium, R4)
  died on a provider 429 — but NOT zero-output: its transcript's Write at
  2026-07-25T03:01:13Z (matches the untracked file's mtime to the second) left a 916-line
  near-complete implementation. Run-2 (same pin, re-spawn 2026-07-26): audited the salvage,
  **caught a REIMPLEMENT-constraint violation in it** (near-verbatim transcription of the S3
  lock code), rewrote that portion independently, added the 88-test suite/README/CI step
  (commit `6dcfaee`), then implemented the 13-finding fix list (commit `b361fa2`, suite →
  126). Gate: one R1 leg (`reviewer` pin, opus/high) — verdict OBJECT, 1 BLOCKER + 6 MAJOR +
  6 MINOR, **13/13 accepted on adjudication, zero false positives** (4 reproduced firsthand
  by the adjudicator before acceptance); 7 findings required crosswalk amendments (v0.2.1).
- **Outcome proxies:** all four suites green post-fix (223+10+74+126 = 433, CI invocations,
  run by parent); the reviewer's own exploit scripts abort at their first exploit post-fix;
  parent's 9 independent accept/reject spot-checks pass. Re-review of the fix commit was
  deterministic exploit-replay + suite regression, NOT a second R1 leg — stated decision, the
  probes are stronger than a fresh reviewer on a bounded fix list.
- **Routing notes (unpaired observations, no counters):**
  - R4 opus/medium carried a substantial greenfield build to a competent first cut, but the
    first cut violated an explicit prompt constraint (copy-not-reimplement) and the R1 gate
    found 13 real conformance gaps — the pin + gate harness did the quality work, consistent
    with the fit-line frame (capability of the system, not the model).
  - The 429 run is a liveness-discipline specimen: the idle notification was
    indistinguishable from zero-output failure; the artifact existed
    [per: claims-discipline#failure-claims].
  - First live R1 catch of an over-strictness class (F-12) — the lens clause "over-strictness
    is also a finding" earned its place.
- **Dogfood (first live v2 records):** `~/.delegation/v2/intents-2026-07.jsonl` — 6 records,
  3 runs (both build runs + the gate), intents carry route_id/warrant_ids/harness-contract
  hashes (pin hashes cross-check against STATE.md's recorded reviewer-pin hash);
  observed_model transcript-verified `claude-opus-5` on all three (first live
  requested-vs-observed conformance checks — all match). Two schema-fitness observations for
  E-1: (1) per-run dispositions flatten cross-run artifact salvage (run-1 `error` is true but
  lossy); (2) the v0.2→v0.2.1 tightening immediately invalidated a pre-amendment record
  (`friction_codes` free value) — migrated by hand-rewrite of the one line, event_id/ts
  preserved, pre-migration backup in the session scratchpad; grandfathering vs migration is a
  real design question C-5 inherits.
- **attestation:** parent-verified (suites, exploits, spot-checks run firsthand; both
  subagent reports treated as Reported until checked; models read from subagent transcripts).
- **tally:** none — moves no counter. R4 observations are single-route (no paired leg);
  R1 observation is single-leg. Kept for the instrumentation ledger + as supporting context
  on W-004/W-024 (R4) and W-001 (R1 gate value).
- **Artifacts:** [R1 adjudication](../../docs/reviews/2026-07-26-b7-r1-review-adjudication.md) ·
  [crosswalk v0.2.1](../../docs/proposals/2026-07-24-intent-outcome-record-crosswalk.md) ·
  delegation-runtime commits `6dcfaee`, `49c354f`, `b361fa2` · subagent transcripts (session
  dir, `agent-ab7-intent-writer-…`/`agent-ab7-r1-review-…`).
