# PROBE — 2026-07-27 Storage Advisor review artifact ownership

- probe_id: P-20260727-storage-advisor-artifact-ownership
- task class / ROUTES row: review gate / R1; contract shape, not model quality
- configs compared: existing generic disposition contract vs explicit delegate-owned artifact
  and root delta ledger
- router: Codex root; external review route was Opus high through the Claude CLI
- **attestation:** Storage Advisor's materialized Opus review, compact root disposition ledger,
  revised proposal, and Signal Layer observation `obs-20260727T223606-e6d13b`
- verdict: local contract amendment authorized by operator; later outcome check required
- **tally:** moves no ROUTES/WARRANT model counter; first attested project requirement for the
  artifact-ownership contract
- deviations from clean protocol: the first root disposition was prose-heavy before being
  collapsed; the forward baseline used a fresh Luna agent rather than repeating the paid Opus run
- record locator(s):
  - `storage-advisor:docs/reviews/2026-07-27-incident-guard-opus-review.md`
  - `storage-advisor:docs/reviews/2026-07-27-incident-guard-opus-review-disposition.md`
  - `storage-advisor:docs/proposals/2026-07-27-incident-guard-terminal-setup-revision-2.md`
  - Signal interpretation `int-20260727T223942-b3ea2d`
  - Signal intervention `ivn-20260727T224300-06ca4e`

## Observation

The read-only Opus result was already preserved verbatim by deterministic materialization. Root
integration then created a second prose-heavy disposition that repeated accepted findings.
Materialization was not missing; authoritative artifact ownership and delta-only integration were
missing from triage.

## RED baseline

A fresh agent given only the generic paid-review scenario proposed:

- an orchestrator-authored exact-stdout artifact;
- a second orchestrator-authored disposition containing rationale, evidence, follow-up, and risks;
- optional extracted reviewer proposals.

That answer preserved evidence but reproduced duplicate synthesis. It did not choose the reviewer
as authoritative author or constrain root integration to deltas.

## Intervention and prediction

Add artifact owner, transport, and integration mode to the Codex and Claude triage contracts.
Claude-specific read-only reviews use verbatim materialization. Root records only finding-ID
deltas unless multi-source synthesis was named before launch.

Prediction: the next comparable durable review produces one full worker-owned review plus a root
ledger materially shorter than the review, without loss of independent verification or unresolved
disagreement.
