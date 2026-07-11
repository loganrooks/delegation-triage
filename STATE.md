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

| key | value | valid_until | re-check trigger | source (entered) |
|---|---|---|---|---|
| active-profile | balanced | — (config, exempt) | operator flip, committed | operator (2026-07-10) |
| scarcity-mode | **fable-window**: included fable up to 50% of weekly limits; fable spawns = enumerated classes + durable-artifact test only; no fable-dependent task that can't finish in-window | 2026-07-12 | on expiry → mode flips to **no-fable**: usage credits at API rates = effective cliff (operator ruling); Fallback column becomes the Route; any fable row needs explicit operator action | anthropic.com/news/redeploying-fable-5 + operator-confirmed extension [SEAS litgap C-001–C-003] (2026-07-10) |
| fable-window-end | 2026-07-12 (extension from the vendor-stated 07-07; vendor primary pages NOT yet updated) | 2026-07-12 | operator plan-usage UI; vendor release notes | operator confirmation 2026-07-10 + secondary (iwoszapar.com) [C-003, Corroborated/Moderate] (2026-07-10) |
| reviewer-pin | **fable / high** (`agents/reviewer.md`) | 2026-07-12 | **SCHEDULED FLIP at expiry (ADR-0022 D3, first exercise of this mechanism):** frontmatter → `model: opus` + `effort: high`; xhigh per stated reason; flip recorded in probes/ as an availability event. **Until the manual flip lands, drivers take R1's fallback (opus high) regardless of the pin** — the pin frontmatter, not STATE, is what actually spawns (review lens 2 F5) | SEAS ADR-0022 Decision 3 (2026-07-10) |
| orchestrator-pin | **fable / high** (`agents/orchestrator.md`) | 2026-07-12 | at expiry: post-window fable requires explicit operator action; **until the owed adjudication lands (only the reviewer pin was adjudicated, A3), expired = route on R13's fallback (opus xhigh + reviewer gate on the synthesis) via a stated-reason spawn** (review lens 2 F1) | ~/.claude mint 2026-07-10; SEAS ADR-0022 (2026-07-10) |
| fable-post-window-terms | metered via usage credits at API rates; new classifier flags benign coding/debugging more often, auto-fallback to Opus 4.8 with notification | 2026-09-08 (60-day as-of decay) | vendor release notes on any fable announcement | anthropic.com/news/redeploying-fable-5 [C-002, C-013] (2026-07-10) |
| price-sonnet-5 | intro **$2/$10** MTok in/out (batch $1/$5), `priced_as_of: 2026-07-03` | 2026-08-31 (vendor-stated) | 2026-09-01 → $3/$15; re-price sonnet lanes | vendor pricing page [routing-table RC-19] (2026-07-03) |
| price-opus-4.8-fast | fast mode **$10/$50** MTok (= fable sticker), `priced_as_of: 2026-07-03` | 2026-09-01 (60-day as-of decay) | vendor pricing page on any model/pricing release | vendor pricing page [routing-table RC-21] (2026-07-03) |
| platform-no-per-call-effort | Agent tool exposes `model` only; frontmatter `effort:` is the only pin; generic spawns inherit session effort; roster definitions register at session START (hot-load refuted 2026-06-12) | 2026-09-08 (60-day as-of decay) | any platform release notes mentioning spawn parameters or hot-reload | SEAS TRIAGE.md Known trap + re-observed in Cowork 2026-07-10 [C-005, C-006] (2026-07-10) |
| cowork-boundary | user-level skills, roster pins, and hooks do NOT load in Cowork sessions; knowledge surfaces must be readable as plain files | 2026-09-08 (60-day as-of decay) | any Cowork release notes on skills/agents/hooks | observed 2026-07-10, n=1 session; mechanism Reported [C-005] (2026-07-10) |

## Scheduled items

1. **2026-07-12 — reviewer pin flip** (ADR-0022 D3): `reviewer.md` frontmatter `model: fable` →
   `opus` (effort stays `high`; xhigh per stated reason); scarcity-mode entry flips to no-fable;
   this table's fable rows re-checked the same pass. Supersedes SEAS ADR-0013's reviewer row at
   the flip. **Do not execute from a sandboxed session — operator terminal.**
2. **2026-09-01 — sonnet re-price** (RC-19): update price-sonnet-5, re-check budget-conscious
   deltas' economics.
