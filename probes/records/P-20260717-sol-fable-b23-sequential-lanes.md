# P-20260717 — sol + fable SEQUENTIAL review lanes on B23 (not a paired probe)

- **Class:** review gates (cross-vendor, sequential lanes — NOT paired: different tree states, non-identical prompts by design)
- **Date:** 2026-07-17 (legs ran 2026-07-18 UTC)
- **Artifact:** arxiv-mcp-pro B23 (slim `[pro]` to model2vec backend + index-compat guards), PR #27
- **Design:** deliberately SEQUENTIAL, not paired. sol-code-reviewer (gpt-5.6-sol, high) reviewed the round-1 implementation (archive-frozen tree at commit `4284f1f`); its 7 findings were fixed in `562dc0a`; fable (reviewer agent, claude-fable-5) then reviewed the CUMULATIVE diff (archive-frozen tree through `562dc0a`). The codex GitHub connector ran as a third lane on the live PR. Because the legs saw different code states, **no head-to-head capability comparison is licensed** — this record contributes lane-yield and false-positive data only.

## Attestation
- Both frozen trees were `git archive` exports verified `.git`-free and `goal/`-free (B20 lesson applied).
- Every accepted finding was re-verified first-hand by the adjudicator before the fix round (uv.lock via `uv export` reproduction; model2vec normalize/force_download semantics from the installed 0.8.2 source and the v0.8.0 tag on GitHub; TOCTOU/identity-mixing by code trace).
- Ledger rows: `rev-20260718T025639` (sol), `rev-20260718T025704` ×2 (fable, codex) in arxiv-mcp-pro `goal/ledger/reviews.jsonl`.

## Lane yields (all findings adjudicated)
- **sol (round-1 tree):** 7 findings — 2 VITAL (upsert TOCTOU via BEGIN-less sample+insert, with a threaded repro; same-dim model-switch silently mixing embedding spaces + falsifying index_meta), 3 MAJOR (legacy meta-free same-dim slip-through; stale uv.lock, with a `uv lock --check` repro; custom-model normalize:false breaking cosine, with the exact model2vec source cite), 1 MINOR, 1 NIT. Verdict DO-NOT-SHIP. **0 false positives (n=3 streak).** All 7 ACCEPTED and fixed.
- **fable (round-2 cumulative tree):** 8 findings — 1 MAJOR (reindex clear_existing=true deletes the index BEFORE probing the model loads — a data-loss path on the change's own remediation message; the sharpest catch of the round), 4 MINOR, 2 NIT, 1 rejected (model2vec 0.8.0 floor — refuted by first-hand source check: normalize param + 1e-32 guard present at v0.8.0). Verdict SHIP-WITH-FIXES. Also ran its own empirical SQLite probe (rollback-on-close) to clear the transaction-hygiene surface. 1 REJECTED_FALSE_POSITIVE, 1 REJECTED_BAD_FIT (meta dim kept as diagnostic).
- **codex connector (live PR):** 2 P2s — force_download=True re-downloading the model every process (unique catch, neither other lane saw it); identity check running after the model load in query mode (overlaps fable's probe-ordering theme but a distinct call site).

## Reading (what this does and does not license)
- **Licenses:** sol-code-reviewer's zero-false-positive streak extends to n=3 on real code artifacts; its VITAL-tier yield on concurrency/data-integrity surfaces is now demonstrated twice (B16 wire-encoding, B23 TOCTOU). Three-lane diversity paid again: each lane produced ≥1 unique accepted catch (sol: TOCTOU + space-mixing; fable: pre-clear data loss; codex: force_download).
- **Does NOT license:** any fable-vs-sol dominance reading — the legs reviewed different code. Do not count this toward the W-001 demote counter's paired-firing columns.
- **Cost note (workflow-cost-discipline):** sequential lanes on an evolving branch bought three rounds of convergent hardening for one implementer thread + three reviewer spawns; right-sized for a `both`-tier item with concurrency + data-integrity surfaces.
