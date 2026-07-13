# agents/ MANIFEST — canonical definitions + recorded deployments

**Canonicality (ADR-0022 A5):** the definitions in THIS directory are canonical; every deployed
copy is a recorded deployment stamped here with a content hash. Drift = diffable, never
discoverable-by-accident. Roster changes register at session START — a deploy without a restart
is a silent no-op; stamp the deploy AND note the restart.

**Deploy step (until a sync script exists, documented-manual):** copy changed definitions to the
target, re-hash (`shasum -a 256 agents/*.md`), update the deployments table, restart the session.
`--check` equivalent: re-hash the target and diff against this table.

## Canonical candidates (0.1.0-stage1-draft, hashed 2026-07-10)

| definition | model × effort | sha256 | provenance |
|---|---|---|---|
| reviewer.md | fable × high (SCHEDULED FLIP → opus × high at 2026-07-19 <!--vf:fable-window-->, STATE.md) | a9b8d34381f7c25a9beb8942b5221e192e80506fd6a31b23f23864088c37f103 | adopted verbatim from the 2026-07-10 `~/.claude` state; pin per ADR-0022 A3 |
| explorer.md | opus × high, read-only | abf2e469019ad052aca1011e16a660c3419bba3f705bb4c896ae905fc9290199 | carries the 2026-07-10 operator correction (facts + follow-ups, never judgments) |
| explorer-light.md | sonnet × medium, read-only | 4389ba1abcc7f53113da1f6e46d65b990531fdd973fd2532e95e412e2f580413 | minted 2026-07-05 as the sonnet-medium probe instrument (W-006) |
| implementer.md | opus × xhigh | 1d28f514220af29a0fb50df367eac0cf8edfec29913323fd4ef6bafdd1420fa2 | W-004 |
| implementer-light.md | opus × high | f2f1d3355500523275f0567038889b33b02c2ea670b24aaee1edaba5aced36fa | W-005; sonnet demotion probe open (count 1/3) |
| orchestrator.md | fable × high | 39bcd0c45edb246dd75cd9baa32614ff4aaeceaed300bc654d6c7a55161aff14 | minted 2026-07-10 after the effort-inheritance firing; post-window pin adjudication OWED (STATE.md) |
| advisor.md | fable × xhigh, tool-less | 6f1811a5b7f46a36444d66db7da2d0e12e15a216734f6ce8a94ff20485598250 | adopted 2026-07-10 from the Cowork `delegation-roster` fork 0.2.2 (its advisor.md sha `3d3eae34…76e766`), operator-claimed design; route R15 (CANDIDATE, W-022). Basis: subagent advisor = plaintext on any model (tool caveats out of scope); xhigh reason: single bounded turn, judgment-dense checkpoint. Disconfirmer: R15's owed local probe (incl. high-vs-xhigh pair) grading advice quality/actionability — parity at high demotes the pin. Window management is project-side (graceful degradation, operator 2026-07-10): no dates in the definition |

Excluded from the roster migration: `knowledge-store.md` (a reference specification that was
sitting in the deployment directory, not an agent definition — left where it lives; flagged for
the operator to relocate).

## Recorded deployments

| target | stamped | status |
|---|---|---|
| `~/.claude/agents/` | **2026-07-10 @ `0fa9ee8` (install.py claude-code — first scripted deploy)** | roster: 7 definitions incl. `advisor` (new; hashes = canonical table above); skill home `~/.claude/skills/delegation-triage/` current @ `0fa9ee8` (31 files, `install.py claude-code --check` clean); **restart pending at stamp time** — advisor registers at next session START. History: Stage-2 deploy from `14c3311` same day (routing-table archived, guard re-pointed to STATE.md); ROUTES+WARRANTS interim re-sync @ `cf95ea1` |
| SEAS `harness/agents/` | 2026-07-10 | superseded records (marked in-file per ADR-0010 convention); TRIAGE.md re-scoped to consumer-side pointer + overlay |
| Cowork `delegation-roster` plugin (installed) | — | **UNRECONCILED FORK, discovered 2026-07-10:** a GPT-5.6-Pro repackaging of the PRE-package routing table + probe corpus (its routing-evidence.md cites the same bridgewright/prix-guesser/signal-layer records) — 7 agents (ours + an `advisor` @ fable/**xhigh**) + a skill with a routes/evidence split but **NO STATE layer** (volatile facts deliberately omitted → no expiry mechanism; its fable pins will silently outlive the 07-12 window — the C-012 failure mode in a third home). Stage-2 reconciliation owed: regenerate from canonical or diff-and-stamp; until then it is a live drifting copy in exactly the environment (Cowork) the proposal diagnosed as blind. |
