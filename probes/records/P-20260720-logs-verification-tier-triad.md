# PROBE — 2026-07-20 logs-verification model×effort triad (haiku vs sonnet-medium vs sonnet-high; R7 verification)

- probe_id: P-20260720-logs-verification-tier-triad · **post-hoc: true** (operator ran the three
  sessions as their own model×effort test; analyzed after the fact)
- task class / ROUTES row: **R7** (deep-read / adversarial verify) — subtype: *filesystem
  verification of a document's factual claims*. NOT R6 (the deliverable is a claims-discipline
  judgment, not coverage) and NOT R1 (no shipped artifact under gate).
- configs compared (model × effort × surface × harness): `claude-haiku-4-5` (effort n/a) ·
  `claude-sonnet-5`×medium · `claude-sonnet-5`×high — three main-loop Claude Code sessions,
  IDENTICAL task + repo + `CLAUDE.md` harness + operator prompt ("verify this logs doc by checking
  locally"). Task was NOT routed through the delegation-triage skill.
- harness/contract hash (if pinned): none — main-loop sessions. Harness = the AHR repo `CLAUDE.md`
  + global claims-discipline rule-files, identical across all three legs.
- blinded?: **effectively** — three independent sessions, no cross-contamination (legs could not
  see each other). Not a deliberate blind.
- frozen tree?: n/a — no reviewed artifact; the "artifact" is the live filesystem, read-only and
  unchanged across all three legs.
- adjudicator: **author** (analyst; non-author of the three runs). Sole adjudicator.
- router: **operator (human)** — model + effort set manually per run (`/model` + effort setting).
  No driver-model routing decision, so this datum carries **no routing-competence signal** (G-02).
- **attestation:** raw session JSONLs on disk @
  `~/.claude/projects/-Users-rookslog-Projects-AgenticHarnessResearch-agentic-harness-research/`:
  - high:   `ac9fcf3f-2bf9-4620-a6d2-125342069015.jsonl`
  - medium: `5118722b-abae-4eae-801b-6e44e5058be3.jsonl`
  - haiku:  `8ffe6708-d992-44e2-87c5-f21251f9dec3.jsonl`
  model ids measured from the `model` field; effort from `effort`/`mode` records; tokens from
  `usage` fields; costs computed. **Attested, not self-reported.**
- verdict: **quality high > medium ≫ haiku — the cliff is medium→haiku and it is a
  CLAIMS-DISCIPLINE cliff, not a coverage cliff.** All three located the files. Haiku overclaimed
  ("all major claims accurate / all locally verifiable"), MISSED the one real discrepancy
  (`~/.claude/image-cache/` absent), and gave no scope statement on the behavioral claims it could
  not check from the filesystem. Both sonnet legs caught the image-cache gap and explicitly scoped
  "not checked locally". Sonnet-high added only **marginal depth** over medium — nothing
  load-bearing that medium missed.
- unique catches (per leg):
  - **haiku:** surfaced operator instrumentation dirs (`observability/`, `workflow-gate/`,
    `cache-timer/`) — a coverage bonus. FAILED the judgment layer (overclaim + missed discrepancy).
  - **sonnet-medium:** caught `image-cache` absent; opened one `audit.jsonl` and reported its key
    set including the undocumented `_audit_hmac`; explicit "not checked locally" scope block.
  - **sonnet-high:** everything medium did + read the actual `cleanupPeriodDays=3650` from
    `settings.json` (turned a can't-check into a checked fact) + `stat`-verified `claude-code-sessions/`
    and `local-agent-mode-sessions/` are NOT inode aliases + found `telemetry/1p_failed_events.*`.
- tokens / cost (observed): billed today (Sonnet 5 intro $2/$10; Haiku $1/$5; cache-write 1.25×,
  cache-read 0.1×):

  | leg | total tok | output tok | assistant turns | cost (intro) | cost (std $3/$15) |
  |---|---|---|---|---|---|
  | sonnet·high | 2.02M | 21,026 | 25 | $1.356 | $2.034 |
  | sonnet·medium | 1.22M | 12,217 | 16 | $1.072 | $1.608 |
  | haiku | 0.86M | 9,399 | 18 | $0.419 | — |

  ratios: **high = 1.26× medium** (either basis); high/haiku = 3.2× (intro) / 4.9× (std);
  med/haiku = 2.6× / 3.8×. **Cost driver = cache-read tokens** (turns × large `CLAUDE.md` prefix
  re-read each turn), NOT output. **Wall-clock ~4 min for all three** (I/O-bound on tool
  round-trips; NOT a tier discriminator — medium was slowest at 4.7 min).
- **tally:** attested datum feeding **W-023** (R7 class) + **W-016** (effort-dial). Does **NOT**
  move a flip counter:
  - W-023 R7-proper paired tally stays **0** — no opus leg was run; the W-023 flip needs
    sonnet-fails-where-opus-succeeds.
  - Not the W-006 medium-revert counter — off-class (R7 verification, not an R6 sweep).
  - Supporting reads: (a) sonnet (both efforts) clears the claims-discipline bar on R7
    verification → consistent with W-023 "harness carries the discipline". (b) The harness carries
    discipline down to **sonnet**, NOT to **haiku** — haiku broke on the judgment layer → **boundary
    datum on the harness-compensation thread** (W-006 "+7pp on Haiku" steering-helps-weaker-models):
    compensation holds for coverage/retrieval, **not** for the claims-discipline layer. (c) high→medium
    marginal at 1.26× cost → directional corroboration of W-016 (high = sweet spot; medium sufficient
    here), single observation, new task subtype.
- deviations from clean protocol (named):
  - post-hoc, not pre-registered (operator ran the legs for their own purpose).
  - n=1 per cell, single task, single repo.
  - human router (operator set model+effort manually) — no agent-routing signal.
  - not run through the delegation-triage skill.
  - no opus leg → cannot bear on the W-023 sonnet-vs-opus flip.
- implication for ROUTES (proposed, not applied): confirms the **roster floor = sonnet, not haiku**,
  for judgment-bearing R7 verification (haiku's failure mode is claims-discipline, not coverage);
  **sonnet-medium is sufficient** for the filesystem-verification subtype, high buys marginal depth
  at 1.26×. n=1 — a prior to add, not a route change.
- record locator(s) + minimal verbatim excerpt(s):
  - haiku final (overclaim): *"I've verified the information locally and can confirm all the major
    claims in that document are accurate"* / *"The document's claims are all locally verifiable."*
    — `8ffe6708-…jsonl` (final assistant text).
  - sonnet-medium final (caught gap + scope): *"`~/.claude/image-cache/` — does NOT exist on this
    machine"* / *"Not checked / can't verify locally — these are behavioral/documentation claims, not
    filesystem facts"* — `5118722b-…jsonl`.
  - sonnet-high final (marginal depth): *"cleanupPeriodDays is a real key in `~/.claude/settings.json`
    (this user has it set to 3650…)"* / *"not aliases of each other (different inodes, verified via
    stat)"* — `ac9fcf3f-…jsonl`.
