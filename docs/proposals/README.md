# Proposal map

This directory contains the design lineage for turning `delegation-triage` from a Claude-family
routing package into a transparent, auditable, research-backed delegation product that can serve
multiple providers and harnesses.

The newest document is not automatically authoritative. Read status, authority, supersession, and
review records before using a proposal as an implementation contract.

## Current review entry point

Start with the
[Claude control-plane initiative handoff](../handoffs/2026-07-24-claude-control-plane-initiative-handoff.md).
It defines the current product thesis, required proposal review, unresolved decisions, and the
boundary between this documentation transfer and later Claude Code work.

The portfolio-level review is now the
[2026-07-24 Fable portfolio decomposition review](../reviews/2026-07-24-portfolio-decomposition-fable-review.md):
verdict REVISE (two products, not three artifacts), dispositions of the root session's
recommendations R-A–R-F, four operator decisions (D-1…D-4), and the ordered next-phase
decomposition. It awaits operator disposition; nothing in it is self-authorizing.

## Orientation documents

The [evidence-commons north star](2026-07-24-evidence-commons-north-star.md) records the
long-horizon vision: a community-scale evidence commons built in three layers (record
standard → local tooling → registry/governance), binding exactly one near-term decision —
the intent-record schema (decomposition item B-3) must be shareable by construction. Its
companion, [Worldings](2026-07-24-evidence-commons-worldings.md), holds the vision to
concrete inhabited situations and states what breaks without each design commitment. Both
are orientation, not implementation contracts; the north star's §6 constraint awaits
operator disposition alongside the portfolio review's decisions.

## Recommended read order

| Proposal | Current role | Required disposition |
|---|---|---|
| [Consolidated multi-harness control plane](2026-07-21-consolidated-multi-harness-delegation-control-plane.md) | Leading product-boundary proposal. It joins provider-neutral policy, provider/harness adapters, deployment integrity, and orchestration learning. | Review and revise against the July 24 product direction before ratification. |
| [Cross-runtime routing and Codex-managed Claude delegation](2026-07-17-cross-runtime-routing-and-claude-delegation.md) | Accepted architectural lineage for Codex-managed Claude sessions, provenance, recovery, and bounded delegation. | Preserve its runtime invariants; identify which parts are absorbed by the consolidated product. |
| [Composable Claude capability and scope policy](2026-07-20-composable-claude-capability-and-scope-policy.md) | Approved direction for provider-neutral policy identity plus Claude-specific compilation. Its C0 core is implemented but non-activating. | Preserve the pure-policy boundary; revise later cohorts around the immediate Claude Code and Codex product horizon. |
| [Capability-based Claude execution profiles](2026-07-19-capability-based-claude-execution-profiles.md) | Historical profile and runtime-probe baseline, partially superseded by the composable policy. | Retain as evidence; do not treat its fixed profiles as the final public configuration model. |
| [Deferred provider-neutral router](2026-07-20-provider-neutral-multi-harness-delegation-router-deferred.md) | Earlier decision to preserve an extension seam without building a router. Its reopening triggers now require reassessment. | Decide what the consolidated proposal supersedes and what adapter invariants remain. |
| [Codex-managed Antigravity adapter](2026-07-20-codex-managed-antigravity-gemini-flash-adapter.md) | Implemented temporary provider slice and evidence about cross-provider reuse. | Treat as migration evidence and a later extension, not the immediate product center. |

## Supporting evidence

Proposal reviews, correction records, and execution records live in [`../reviews/`](../reviews/).
Implementation plans live in [`../superpowers/plans/`](../superpowers/plans/). Probe records remain
the source of truth for empirical routing outcomes under [`../../probes/`](../../probes/).

## Interpretation rules

1. Separate observed facts, source-supported claims, inferences, recommendations, user decisions,
   and open decisions.
2. A provider model is not a route. Provider, model, harness, transport, authority profile,
   validation contract, and dated capability evidence jointly identify a runnable route.
3. A new model release creates a candidate and a review trigger. It does not automatically displace
   an incumbent route.
4. Sparse or heterogeneous traces generate hypotheses. Route promotion requires the warrant and
   probe discipline in the canonical package.
5. Installed copies are deployments, not competing authorities. Stable promotion requires a
   coherent source revision, release manifest, installation receipt, and drift check.

