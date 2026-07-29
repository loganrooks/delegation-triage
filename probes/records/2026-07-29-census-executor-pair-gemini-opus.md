# PROBE — 2026-07-29 census executor pair: gemini-flash-high vs opus-high (browser enumeration)

- probe_id: P-20260729-census-executor-pair
- task class / ROUTES row: browser-driven read-only enumeration (closest existing class:
  sweeps/enumeration; no browser-lane row exists yet — this is its first paired evidence)
- configs compared (model × effort × surface × harness): gemini-3.6-flash × high ×
  claude-code-teammate (flash-executor-high pin, CENSUS-002, 2026-07-28, Sol-high orchestrator)
  VS claude-opus-5 × high (session-inherited) × claude-code-teammate (explorer pin + model
  override, CENSUS-003, 2026-07-29, Sol-high orchestrator). Same three delegation packets
  VERBATIM (observability prompt store, sha-named), same browser instrument (Playwright MCP
  under the A-012 deny-list), same live target.
- harness/contract hash (if pinned): packets at
  `~/.claude/observability/prompts/{fe9322d0…,7e0050bd…,cda9a826…}.txt` (content-addressed)
- blinded?: yes between vendors (opus legs instructed "no access to the prior run's output");
  legs sequential within each wave. NOT blind: the packet itself (authored after a rejected
  first gemini-medium attempt).
- frozen tree?: packets content-addressed; UI target is a LIVE product surface — the two waves
  ran ~1 day apart, so product drift is an uncontrolled variable (one measured instance:
  session date rollover mid-census2). Treat name-level diffs as upper bounds.
- adjudicator: Sol-high orchestrator per wave (non-author of legs), main loop (fable)
  re-verified counts and personal-content greps against raw reports both waves.
- router: fable main loop (operator-directed executor choice both waves; operator also
  ordered the comparison itself and the terra substitution on leg 4).
- **attestation:** transcript JSONLs on disk
  (`~/.claude/projects/-Users-rookslog-Development-chatgpt-cli/b6ea1c54-*/subagents/agent-acensus2-*.jsonl`,
  `agent-a7cfcd23*.jsonl`/`agent-ab433cb1*.jsonl`/`agent-ad099e52*.jsonl` [opus legs]); committed
  reports `chatgpt-cli:docs/discovery/findings/census-001/census{2,3}-*.md` @ 464fefc/e4af8db.
- verdict: **complementary coverage, not dominance.** Deep nested surface (16-tab Settings
  bundle): opus 147 unique row names vs gemini 117, shared only 78 — each found real controls
  the other missed (opus-only: billing history, cancel plan, archived chats, canvas;
  gemini-only: add github, apple intelligence, codex cli). Shallow surface (More/GPTs/
  Scheduled/Plugins): near-parity, 46 of ~50 shared. Union beats either. Compliance: opus
  1 of 3 legs REJECTED (continued past an explicit stop condition after browser_find pulled
  conversation titles into tool output — self-reported), gemini-high 3/3 accepted; but
  gemini-MEDIUM (prior wave) leaked 15 installed-plugin titles into durable evidence where
  every high-effort leg of both vendors withheld them, and gemini b2 silently copied a stale
  packet run-ID that opus b1 caught and flagged. Reporting fidelity: opus > gemini
  (consistent with the pilot-wave weaknesses already on the flash pins).
- unique catches (per leg): see committed diff analysis + per-report §Stop events. Notable:
  opus b3's finding that browser_find cannot be region-scoped (adopted into the leg-4 packet
  as a hard rule); opus b1's stale-stamp catch (packet template carried the census2 run-ID —
  both waves' evidence, main-loop-corrected at e4af8db).
- tokens / cost (if observable): output tokens gemini-high 24,103 (13,160+8,469+2,474) vs
  opus 80,310 (35,834+28,403+16,073) ≈ 3.3× — for +25% rows on the deep bundle, parity on the
  shallow one. Turns 229 vs 287. CAVEAT: gateway-translated usage (cacheW always 0 on gateway
  models) — cross-vendor token counts are differently-measured quantities; per-vendor pricing
  not applied here.
- **tally:** feeds a NEW counter (browser-enumeration lane, no W-record yet — candidate row:
  "browser enumeration: gemini-flash-high default, opus for deep/nested panels or where
  stop-condition judgment is load-bearing... except opus was the one that violated a stop
  condition; direction genuinely unresolved"); count after this record: 1/1 paired.
- deviations from clean protocol (named): (1) live-surface drift between waves, unquantified;
  (2) opus effort was session-inherited high, not pinned — the known Agent-tool inheritance
  hazard; (3) run-ID stamp contamination from the packet template (both waves affected,
  corrected post-hoc); (4) gemini-medium leg is from the SAME wave as gemini-high but a
  different effort tier — cited for the boundary-fidelity contrast only, not the coverage diff.
- record locator(s) + minimal verbatim excerpt(s):
  `chatgpt-cli:docs/discovery/findings/census-001/census3-opus-high-b3-report.md` ("I did not
  stop"); orchestrator adjudication in main-session transcript 2026-07-29 ("164 / 57 / 4 …
  2 accepted, 1 rejected"); diff table in main-session turn of 2026-07-29 (b1: shared 78,
  opus-only 69, gemini-only 39).
