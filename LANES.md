# LANES — fast programme state

Governed by [PROGRAMME.md](PROGRAMME.md) §0 (fast row): same-pass updates, no ceremony.
**Header state: `current`** (flips to `needs-review` per PROGRAMME §3 P-D; to
`decision_due` per §0 operator-absence rule). Every row carries owner · as-of · source;
a row whose as-of predates its source's last change reads as `unchecked`, not as true.
This surface is manually maintained today; generating it from proposal/decision/ledger
metadata is a named candidate once the P1 rollup exists (sol review, hybrid design) —
generation would cover state, never ratification.

| lane | now | next | gate | owner | as-of | source |
|---|---|---|---|---|---|---|
| **P1 rollup** | task-class enum (crosswalk §2a) publication — first deliverable, pulled forward from C-5's orbit | join + per-cell rollup as increment over shipped `summarize`; build home `delegation-runtime` (D-1); writer-side fixes are acceptance criteria per the ratified proposal | fail-loud; refuses decision-grade output below flip floor; surfaces proposals, never applies routes | driver sessions | 2026-08-01 | [passive-first ratification](docs/proposals/2026-07-31-passive-first-reprioritization.md) |
| **P2 capture surface** | unstarted (measured 2026-07-31: no hook writes records — passivity is the untested hypothesis) | install-time writer; §6.4-compliant feedback (enum codes + local-only note); H5 maintenance clause | E-1/§9: no local routing improvement ⇒ sharing layer not built | driver sessions | 2026-08-01 | same |
| **C-5 interchange** | absorbs sharing design (two-operator registry-less pooling; XV-9 consent tiers) | v2-migration items as evidenced by P1 fail-loud cells | north-star §6 binding | driver sessions | 2026-08-01 | same + [north star §6](docs/proposals/2026-07-24-evidence-commons-north-star.md) |
| **Experiments channel** | demoted by default; `passive-signal alternative considered:` field NOW IN [probes/TEMPLATE.md](probes/TEMPLATE.md) (convention-only per B-4) | B-5 cross-harness transfer test EXEMPT, runs when ready (§9 falsifier 1) | paired-trial cadence re-decided at first §9 evaluation | operator + driver | 2026-08-01 | same |
| **Charter propagation (owed)** | SEAS-side lineage note (cross-repo, cannot be same-pass) · adapter boot pointers (codex fragment + Cowork SKILL template) at next rebuild | close each with the closing commit id | — | driver sessions | 2026-08-01 | [PROGRAMME §0](PROGRAMME.md) transaction rule |
| **Housekeeping** | FP-0a status: see [WARRANTS.md](WARRANTS.md) W-026 (supersede-in-place home — never copied here; v1 copied it, review blocker) · MANIFEST: unreconciled Cowork-plugin fork (the `sol-*` trio is RATIFIED external overlay per D-2 — v1 repeated CLAUDE.md's stale "unowned" line; both corrected this pass) · C-5 vocabulary: `detected-omission` sibling | fold into P1/C-5 touches as reached | — | driver sessions | 2026-08-01 | [agents/MANIFEST.md](agents/MANIFEST.md) |
