# EPISTEMICS — the label vocabulary this package's warrants use

_Lineage: condensed from SEAS `governance/epistemics.md` §1–§2 (ADR-0002/0008 rationale). Carried
in-package so W-records stay interpretable if the package relocates. On any divergence, this
excerpt governs the package's own records; it does not govern SEAS._

We **corroborate, never verify**: each label names the *check performed* and what it licenses you
to say — never "true." Every W-record carries exactly one label.

| Label | Check performed | Licenses | Does NOT license |
|---|---|---|---|
| `Resolved` | locator retrieves a real record | "the source exists at L" | correctness or relevance |
| `Concordant` | our description matches the source's own words | "the source states S; no misattribution" | that S is true |
| `Reported` | a source asserts it at surface level | "source X asserts P" | that P is correct |
| `Corroborated` | P withstood a *severe* check it could have failed; carries a grade | "P withstood check K; grade G" | proven / established |
| `Provisional` | our synthesis across ≥2 sources | "on current synthesis, P" | that P is settled |
| `Conjecture` | plausible, weakly-supported hypothesis | "as a hypothesis, P" | that P is supported |
| `Contested` | sources genuinely disagree | "sources disagree on P" | that P is resolved |
| `Unchecked` | not established this pass | "P is not yet checked" | that P is false |

A vendor/model-card number copied correctly is `Concordant`/`Reported`, **never** `Corroborated`.
**Grades** (load-bearing claims): High / Moderate / Low / Very-Low — start from the evidence-type
prior, then downgrade for risk of bias, imprecision (single run, small n), indirectness,
inconsistency, or selection bias; upgrade only for independent replication or convergent,
methodologically diverse evidence. A bare grade with no downgrade reasoning is non-compliant.
**Severity:** every load-bearing W-record states its flip condition — what would show it false
and whether that was sought. **Expired STATE entries read as `Unchecked`, not as true.**
