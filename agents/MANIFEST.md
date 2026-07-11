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
| reviewer.md | fable × high (SCHEDULED FLIP → opus × high at 2026-07-12, STATE.md) | a9b8d34381f7c25a9beb8942b5221e192e80506fd6a31b23f23864088c37f103 | adopted verbatim from the 2026-07-10 `~/.claude` state; pin per ADR-0022 A3 |
| explorer.md | opus × high, read-only | abf2e469019ad052aca1011e16a660c3419bba3f705bb4c896ae905fc9290199 | carries the 2026-07-10 operator correction (facts + follow-ups, never judgments) |
| explorer-light.md | sonnet × medium, read-only | 4389ba1abcc7f53113da1f6e46d65b990531fdd973fd2532e95e412e2f580413 | minted 2026-07-05 as the sonnet-medium probe instrument (W-006) |
| implementer.md | opus × xhigh | 1d28f514220af29a0fb50df367eac0cf8edfec29913323fd4ef6bafdd1420fa2 | W-004 |
| implementer-light.md | opus × high | f2f1d3355500523275f0567038889b33b02c2ea670b24aaee1edaba5aced36fa | W-005; sonnet demotion probe open (count 1/3) |
| orchestrator.md | fable × high | 39bcd0c45edb246dd75cd9baa32614ff4aaeceaed300bc654d6c7a55161aff14 | minted 2026-07-10 after the effort-inheritance firing; post-window pin adjudication OWED (STATE.md) |

Excluded from the roster migration: `knowledge-store.md` (a reference specification that was
sitting in the deployment directory, not an agent definition — left where it lives; flagged for
the operator to relocate).

## Recorded deployments

| target | stamped | status |
|---|---|---|
| `~/.claude/agents/` | — | NOT YET — Stage-2 gated; the live copies are byte-identical to the candidates above as of 2026-07-10 (these hashes were computed FROM them) |
| SEAS `harness/agents/` | — | stale 2026-06-12 roster; becomes a recorded deployment (or is archived) at Stage 2 per ADR-0022 A5 |
| Cowork `delegation-roster` plugin (installed) | — | **UNRECONCILED FORK, discovered 2026-07-10:** a GPT-5.6-Pro repackaging of the PRE-package routing table + probe corpus (its routing-evidence.md cites the same bridgewright/prix-guesser/signal-layer records) — 7 agents (ours + an `advisor` @ fable/**xhigh**) + a skill with a routes/evidence split but **NO STATE layer** (volatile facts deliberately omitted → no expiry mechanism; its fable pins will silently outlive the 07-12 window — the C-012 failure mode in a third home). Stage-2 reconciliation owed: regenerate from canonical or diff-and-stamp; until then it is a live drifting copy in exactly the environment (Cowork) the proposal diagnosed as blind. |
