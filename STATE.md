# STATE — volatile facts (every temporal entry: value · valid_until · re-check · source)

**Reading rule (D3):** an entry past its `valid_until` is **Unchecked, not true** — re-verify it or
route on the ROUTES fallback column. `check_state.py` enforces this deterministically (exit 1 on
any expired entry); run it from any session's shell, including Cowork.

**Active: balanced**
<!-- the one line you edit to reconfigure triage; commit the flip so it's audited.
     FORMAT CONTRACT (review lens 2 F2): the line must stay BOLD — the deployed
     spawn-triage-guard parses `\*\*Active:\s*([\w-]+)\*\*` and silently falls back to
     "balanced" on any other format. Stage-2 re-point requirement: when the hook re-points
     here, the old routing-table's Active: line is archived in the SAME commit so exactly one
     Active: line exists; check_state.py fails if this line is missing. -->

> **Fable-window dates below are synced mirrors of the canonical `~/.claude/vendor-facts.md`** — edit there and run `python3 ~/.claude/bin/vendor-facts.py sync`; the `<!--vf:...-->`-tagged cells are machine-updated, don't hand-edit them [per: vendor-facts#fable-window].

| key | value | valid_until | re-check trigger | source (entered) |
|---|---|---|---|---|
| active-profile | balanced | — (config, exempt) | operator flip, committed | operator (2026-07-10) |
| scarcity-mode | **fable-permanent** (corrected 2026-07-24, same day, by the fable leg: the post-window/metered row's premise is superseded by vendor primary — from **2026-07-20 Fable 5 is permanently included in all Max and Team Premium plans at 50% of usage limits**; this account is Max, so fable does NOT bill at API rates here). Discipline retained from the window era: fable spawns = **enumerated classes + durable-artifact test**, within the 50% ceiling. Per-spawn operator authorization (the metered-era ceremony) is dropped per this row's own simplification trigger | 2026-09-22 <!--vf:fable-window--> (60-day as-of decay) | any vendor fable/plan announcement; an operator budget-stance change | Claude official X post 2026-07-18 (effective 07-20: "included in all Max and Team Premium plans, at 50% of limits"; Pro/Team-Standard stay on usage credits + one-time $100); operator statement in-session 2026-07-24 ("renewed indefinitely for Max accounts"); coverage: simonwillison.net 07-18, thenewstack.io, enterprisedna.co. Supersedes the same-day post-window/metered entry (fable leg, 2026-07-24) |
| fable-window-end | **RE-OPENED AS PERMANENT (2026-07-24)** — this row's re-open trigger fired: the 2026-07-18 vendor announcement makes Fable 5 a permanent Max/Team-Premium inclusion (50% of limits) from 2026-07-20, so there is no window end. Historical: window lapsed 07-19 after 2nd extension 2026-07-13 (was 07-12; vendor-stated 07-07) and read closed/metered for part of 07-24 | — (ongoing plan fact, exempt) | any vendor announcement changing plan inclusion | Claude official X post 2026-07-18; operator statement in-session 2026-07-24; prior closure recorded 2026-07-24 (opus leg), re-opened same day (fable leg) |
| reviewer-pin | **opus / high** (`agents/reviewer.md`) — **FLIPPED 2026-07-24 by operator quality ruling**, not the ADR-0022 availability cliff: "opus 5 is now the model… you can get away with opus high for reviews"; fable retained for orchestration/decomposition/brainstorming (R13 unchanged). Applied same-session: frontmatter edited, re-hashed 2369d9d3…, MANIFEST stamped. Registers at next session start (pins register at START; running sessions keep the old pin) | — (operator ruling; re-check on Opus 5 review-quality evidence) | an R1 review miss attributable to opus-vs-fable capability → revisit with a paired probe; any vendor change to Opus 5 | operator in-session ruling 2026-07-24 (fable leg, campaign session); supersedes: pin-retained entry earlier same day, ADR-0022 D3 scheduled flip (executed early, different basis) |
| orchestrator-pin | **fable / high** (`agents/orchestrator.md`) — same disposition as `reviewer-pin`: pin retained under permanent plan inclusion. The 2026-07-24 decomposition spawn is the first exercise, and it is **paired against R13's fallback** (opus xhigh + reviewer gate) so retention is measured rather than assumed [W-024(d); packet §7]. **Pairing caveat (fable leg, 2026-07-24): the two legs shared live state — both edited this repo and both machines the same day — so adjudicate as convergent-work evidence, not an independent A/B** | 2026-09-22 <!--vf:fable-window--> (tied to `scarcity-mode`) | the paired probe returning fable-not-better on the decomposition class → flip to the fallback and record it | ~/.claude mint 2026-07-10; SEAS ADR-0022; metered-era disposition 2026-07-24 (opus leg); premise corrected + pairing caveat + malformed extra cells repaired 2026-07-24 (fable leg) |
| fable-post-window-terms | **SCOPE NARROWED 2026-07-24: applies to Pro/Team-Standard only** (usage credits + one-time $100 credit) — Max/Team-Premium are plan-included from 07-20 (see `scarcity-mode`). Classifier note stands: benign coding/debugging flagged more often, auto-fallback to Opus 4.8 with notification | 2026-09-08 (60-day as-of decay) | vendor release notes on any fable announcement | anthropic.com/news/redeploying-fable-5 [C-002, C-013] (2026-07-10); scope narrowed per Claude X post 2026-07-18 (fable leg, 2026-07-24) |
| price-sonnet-5 | intro **$2/$10** MTok in/out (batch $1/$5), `priced_as_of: 2026-07-03` | 2026-08-31 (vendor-stated) | 2026-09-01 → $3/$15; re-price sonnet lanes | vendor pricing page [routing-table RC-19] (2026-07-03) |
| price-opus-4.8-fast | fast mode **$10/$50** MTok (= fable sticker), `priced_as_of: 2026-07-03` | 2026-09-01 (60-day as-of decay) | vendor pricing page on any model/pricing release | vendor pricing page [routing-table RC-21] (2026-07-03) |
| price-opus-5 | **$5/$25** MTok in/out — **half fable's $10/$50**; the premium tier is no longer the expensive one, so budget-conscious deltas that assume opus≈fable pricing need re-checking, `priced_as_of: 2026-07-24` | 2026-09-22 (60-day as-of decay) | vendor pricing page on any model/pricing release | vendor pricing page, audit-bundle claim C16 [W-024] (2026-07-24) |
| platform-no-per-call-effort | Agent tool exposes `model` only; frontmatter `effort:` is the only pin; generic spawns inherit session effort; roster definitions register at session START (hot-load refuted 2026-06-12) | 2026-09-08 (60-day as-of decay) | any platform release notes mentioning spawn parameters or hot-reload | SEAS TRIAGE.md Known trap + re-observed in Cowork 2026-07-10 [C-005, C-006] (2026-07-10) |
| cowork-boundary | user-level skills, roster pins, and hooks do NOT load in Cowork sessions; knowledge surfaces must be readable as plain files | 2026-09-08 (60-day as-of decay) | any Cowork release notes on skills/agents/hooks | observed 2026-07-10, n=1 session; mechanism Reported [C-005] (2026-07-10) |

## Scheduled items

1. ~~**2026-07-19 — reviewer pin flip** (ADR-0022 D3)~~ — **DISPOSITIONED 2026-07-24, not executed.**
   The flip was designed for a cliff (window closes ⇒ fable unreachable); the actual regime is
   metering, so the pin is retained and the gate moved to `scarcity-mode`'s per-spawn
   authorization. The flip remains the documented remedy if authorization proves too costly —
   see the `reviewer-pin` re-check trigger. **First exercise of ADR-0022 D3's scheduled-expiry
   mechanism: the mechanism fired correctly (the rows DID read Unchecked and CI DID fail for 5
   days), but nothing forced the disposition — the scheduled action sat undone until a review
   surfaced it (review D-7).** That gap, not the flip, is the finding.
2. **2026-09-01 — sonnet re-price** (RC-19): update price-sonnet-5, re-check budget-conscious
   deltas' economics.
