# PROVENANCE — Opus 5 / Fable 5 routing audit (external artifact, vendored verbatim)

- **Vendored:** 2026-07-24, by the delegation-triage root session, on operator ratification
- **Artifact status:** **external evidence, preserved verbatim.** The `.md` files in this directory
  are byte-copies of the delivered bundle. They are *not* delegation-triage artifacts and are not
  edited here. Corrections belong in the W-record that cites them, never in this text.
- **Authoring model:** GPT-5.6 Thinking (per `REPORT.md` header). The prompt file is named
  `GPT-5.6-PRO-RESEARCH-PROMPT.md`; the operator recalled the run as gpt-5.6-sol. **The executing
  model is recorded as the report states it**; the discrepancy is noted, not resolved.
- **Evidence cutoff:** 24 July 2026
- **Report version:** 2.0 — supersedes an earlier uncited version that is not in this bundle

## Why only text is here

The full bundle is **71 MB** and contains three Anthropic system-card PDFs (758 pages total) plus
28 rendered page images of them. This repository is public and MIT-licensed; redistributing vendor
PDFs from it is a decision the package should not make silently. The package's existing convention
covers this case: cite external evidence through the WARRANTS KNOWN-REPOS prefix key, and quote the
load-bearing excerpts inline (D6) so a warrant stays evaluable without access to the source.

Accordingly:

| Kept here | Held in the companion store |
|---|---|
| `REPORT.md`, `CLAIM_LEDGER.md`, `SOURCE_INVENTORY.md`, `WEB_SOURCE_NOTES.md`, the research prompt, and the two provenance CSVs | the three system-card PDFs, the 28 `evidence/*.png` page renders, and the rendered chart images |

Companion store prefix: **`routing-evidence:`** (see the KNOWN-REPOS key in
[`WARRANTS.md`](../../../../WARRANTS.md)). Full bundle at
`routing-evidence:2026-07-24-opus5-fable5-routing-audit/`.

**Broken relative links are expected.** The vendored text refers to `sources/`, `evidence/`, and
`assets/` paths that resolve only inside the companion store. `check_wids.py` exempts
`docs/research/external/` for exactly this reason — verbatim fidelity of an external artifact is
worth more than internal link resolution inside this repo.

## Source integrity

The three PDF SHA-256 digests in `SOURCE_INVENTORY.md` were **independently re-verified against the
copied bundle on 2026-07-24** and all three match:

| ID | SHA-256 | Verified |
|---|---|---|
| O5-SC — Claude Opus 5 System Card | `fed3c0e6d150a6ba855f0f117a632d2b27dbb5886fd42815caa92e3e20db1d25` | ✓ |
| O48-SC — Claude Opus 4.8 System Card | `97f11ae3fb305c7105c958599bcf90f216669543393220f674610ddb83ee611a` | ✓ |
| F5-SC — Claude Fable 5 & Mythos 5 System Card | `d23b49f41fa5f3c523089c75e6718f12b59674d74fa981fd81205daf80c9029a` | ✓ |

The PDFs are re-fetchable from Anthropic's [system cards page](https://www.anthropic.com/system-cards);
the digests above are what makes a re-fetch checkable.

## Companion evidence not in the original bundle

The operator separately supplied three **official Anthropic charts** titled "Agentic coding by
effort level," covering Frontier-Bench v0.1, CursorBench, and the Artificial Analysis Coding Agent
Index, each plotting score against cost-per-task on a log axis across the full effort ladder
(low · medium · high · xhigh · max) for Opus 5, Fable 5, Opus 4.8, and GPT-5.6 Sol.

- **Source:** [anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5),
  "Performance and cost-effectiveness" section · published 2026-07-24 · fetched 2026-07-24
- **Status:** these are a **different evidence family** from the system-card figures in `REPORT.md`.
  `Frontier-Bench v0.1` (mini-SWE-agent harness, GKE backend, mean reward over 5 attempts) is **not**
  the `FrontierCode` Main/Extended benchmark cited at O5-SC p. 151, despite the similar name. The
  two sources disagree on effort shape; see [W-024](../../../../WARRANTS.md).
- **Stated confound, carried forward:** the Frontier-Bench footnote reads that Opus 4.8 *"served as
  fallback on safety-classifier refusals for Opus 5 and Fable 5."* Opus 5 and Fable scores on that
  chart therefore contain Opus-4.8-generated results on refused items, at an unstated rate.
- **Reading limit:** values used in W-024 were read off published charts by eye at approximately
  ±0.5 points. Comparisons closer than that are recorded as unresolved, not as ties. This is the
  `chart-series-conflation` hazard in [`KNOWN-WEAKNESSES.md`](../../../../probes/KNOWN-WEAKNESSES.md);
  the figures were read first-hand by the root session, not relayed.

## What this artifact is and is not

It is a **vendor-evidence synthesis with an explicit claim ledger**. Its C01–C13 are vendor-reported
observations, C14–C16 official vendor guidance or current facts, C17 an inference, and C18 a
recommendation — the report labels these itself, correctly.

It is **not** a local routing outcome. Per [`EPISTEMICS.md`](../../../../EPISTEMICS.md) a
vendor/model-card number is `Concordant`/`Reported`, never `Corroborated`, and per
[`CONTRACT.md`](../../../../CONTRACT.md) §6 no route row moves on it. It registers probes; it does
not flip rows.
