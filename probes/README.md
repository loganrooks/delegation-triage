# probes/ — the package's own append-only evidence loop

One file per probe / post-mortem under [`records/`](records/); running tallies in
[`INDEX.md`](INDEX.md); recurring failure kinds in [`KNOWN-WEAKNESSES.md`](KNOWN-WEAKNESSES.md).
SEAS observability (or any project ledger) is an optional read-only *feeder* — where a probe's
raw data lives elsewhere, the record carries a quoted minimal excerpt + a repo-qualified locator
(WARRANTS.md KNOWN-REPOS key) so it stays evaluable after relocation.

**Schema-as-template (D5):** [`TEMPLATE.md`](TEMPLATE.md) is a *template*, prose-tolerant — only
two fields are REQUIRED, because their absence is what the diagnosis actually evidenced:

1. **`attestation:`** how the outcome is verifiable (transcript JSONL / raw legs on disk / commit
   / review record), or `self-reported`. Self-reported outcomes are recorded but tallied
   separately [W-001 discipline; C-016/C-008 direction].
2. **`tally:`** which W-record flip counter this feeds, and the count after this record.

Everything else (class, configs, harness hash, blinded?, frozen-tree?, verdict, unique catches,
tokens) is requested, not enforced. Full-schema enforcement waits for a logged failure a schema
would have caught. **Grandfathered:** records migrated 2026-07-10 from the predecessor routing
table's warrant cells are prose blobs marked `grandfathered: true`; they keep their evidentiary
force (the primaries are quoted) and are not retrofitted.

**Flip discipline [W-019]:** n=1 never flips a row; ≥2 attested concordant is the floor;
flip-prone classes (verdicts near-tied, severity-calibration confounds) accumulate toward ~3 per
side before a route changes.
