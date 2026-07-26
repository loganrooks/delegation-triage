# Flash-pilot protocol — §6.7a panel, spread + adjudication (2026-07-26)

**Artifact under review:** the Gemini 3.6 Flash pilot protocol v1 (superseded in place by
[v2](../proposals/2026-07-26-gemini-flash-36-pilot.md), which disposes every finding).
**Panel:** 2 legs, both `reviewer` pin @ opus/high (R1), independent, read-only, §6.8
commons check mandatory in both. Adjudicator: the authoring fable session
(author-adjudicator confound as in the B-3 panel; mitigated by firsthand re-verification of
load-bearing findings — commands and results below).

## Verdict spread

| leg | primary lens | verdict | findings |
|---|---|---|---|
| validity | experimental validity / decision quality | **OBJECT** | 3 BLOCKER · 11 MAJOR · 3 MINOR |
| feasibility | operational feasibility / consumer viability (ran the writer against every promised record shape) | **CONCUR_WITH_CHANGES** | 4 BLOCKER · 5 MAJOR · 3 MINOR |

Near-zero duplication — only the promotion rule drew both legs' fire (for different defects:
sufficiency-vs-floor confusion; counting-unit ambiguity). Both §6.8 checks: net **toward**
the commons, one foreclosure each (attestation-tier flattening; decisive signals born
non-exportable) — related defects, fixed together by tier floors + vocabulary registration.

## Adjudication — ALL 25 findings ACCEPTED, zero rejected

Firsthand checks before acceptance [per: delegation]: CONTRACT.md:68 overlay precedence
(V-B1); WARRANTS.md:453 "floor the evidence is consistent with but does not fix" (V-B3);
gateway README — bare `gemini-3.6-flash` unserved, `-high` is Google's naming (F-1), zero
tool-loop coverage (F-2, grep count 0), exit-0-empty as the known failure mode (F-9);
`~/.gemini/GEMINI.md` = 1,063 bytes (F-3); zero gemini/flash matches in WARRANTS/ROUTES
(F-4). The feasibility leg's writer-tests were performed by the leg against a temp store
with event ids reported; its "sound" list matches my own B-7-era probes. V-M5 remains
**Reported** (leg's label — it rests on BRIEFING.md characterizations, transcripts unread);
adopted anyway because the fix (cause adjudication before retirement) is right under either
reading of the specimens.

Highest-weight dispositions (full mapping in the v2 revision log §9):

| finding | disposition in v2 |
|---|---|
| V-B1 promotion silently displaces R4 via overlay precedence | promotion now produces a lane-scoped overlay PROPOSAL surfaced as an operator decision; never a row by stopping-rule consequence |
| V-B2 FP-C-first rationale forbidden by AHR-C §3.6 | rationale withdrawn; FP-C re-scoped to whole-harness comparison with per-task n; order recommendation flipped |
| V-B3 floor imported as sufficiency; rare-event math absent | reasoning shown per Q7: rule-of-three bounds stated (n=2 → ~78%, n=8 → ~31% upper bound at 95%); promotion licenses "no evidence against at stated exposure" only |
| F-1 binding names an unserved model | bound to `google:gemini-3.6-flash-high`; alias file to be created |
| F-2 tool loop untested on the only live path | FP-0d smoke gate added, runs first |
| F-3 FP-C legs don't share a prompt contract | claim narrowed to whole-harness A/B (still the north-star H1 test) |
| F-4 no W-record to tally against | W-026 minted (Unchecked; flip = the amended promotion rule) |
| F-5 native leg fits no `surface` member | crosswalk v0.2.2: `cli` member added |
| F-8 `accepted-after-rework` earns no credit; severe events unqueryable | counts toward promotion with `rework_actor`; three severe codes REGISTERED (v0.2.2) |
| V-M4 severe events invisible to self-report | attestation floor ≥ third-party-verified on severe-failure records |
| V-M5 retirement lacks cause adjudication; operator corpus holds 2 ambiguous specimens | cause adjudication precedes the trigger; harness-fault doesn't retire the lane; re-entry paths for all three triggers |
| V-M8 park-guard restated, not applied | applied: pilot promotion = restated-weaker unpark for D3-RT04/M04; D3-RT05/08 acknowledged indefinite |
| V-M9 "ordinary work" mislabel | relabeled instrumented probes; §7 cost booked against C-P2 |
| V-M10 predictor unnamed → calibration unmeasurable | `predictor` recorded; operator registers his own prediction pre-run |
| commons foreclosures (both legs) | tier floors named per direction; severe codes registered ⇒ exportable |

**Panel-instrument observation:** the feasibility leg's instruction to RUN the writer rather
than read the spec produced 4 of its 7 highest-value findings (F-1/F-5/F-7/F-8's
enforcement half) — runnable-probe review earns its cost; noted for future panel design.

## Decisions this packet carries (see pilot v2 §8 for full five-point expansions)

D-FP-1 (ratify protocol conditionally + register lanes under W-026) · D-FP-2 (order:
FP-0d → FP-B → FP-C → FP-A) · D-FP-3 (name the licensable C-P1 disposition before the wave;
if it isn't worth §7's cost, do-nothing is the honest option). Recommendation on all three:
YES / adopt-as-stated — load-bearing assumption: the chatgpt-cli session's task set passes
§2 eligibility; flip: FP-0d failing (loopback lanes then blocked, native-only degradation)
or the operator judging D-FP-3's deliverable not worth ~50 steps of loop cost.

## Declared limits

Both legs Claude-lineage (single-vendor spread, disclosed per §6.7a); the v2 revision was
authored by the adjudicator (author), not a third leg — the standing remedy is that v2's
own §2/§6 discipline is exercised by the wave itself, and the ratification decision sits
with the operator with this spread attached. Neither leg read the seven Antigravity
transcripts (both flagged it); V-M5 inherited that limit and is labeled accordingly.
