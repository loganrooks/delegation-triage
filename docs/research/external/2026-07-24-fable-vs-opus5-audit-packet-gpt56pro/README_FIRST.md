# Fable 5 vs Opus 5 — audit packet index

**Evidence cutoff:** 2026-07-24  
**Executing model:** GPT-5.6 Pro  
**Decision unit:** model × effort × harness × worker mix × task × verification policy

## Best current answer

Use **Opus 5 as the default solo model and bounded controller**. Start contained implementation at **Medium**, bounded orchestration at **High**, and difficult coherent recovery at **XHigh**. Reserve **Fable 5 High/XHigh** for persistent asynchronous workers, changing decomposition, repeated inter-agent communication, or days-scale integration where coordination topology is itself the hard part. Do not default either model to Max; official effort curves contain plateaus and regressions.

This is a conditional routing judgment, not a universal model ranking. Public multi-agent results use homogeneous or pre-release configurations and do not isolate Fable-versus-Opus-5 controller quality with identical workers.

## Primary deliverables

- `report/Fable_5_vs_Opus_5_Decision_Report.pdf` — 45-page audit-ready report; exact PDF pages/figures and web-section citations are inline.
- `report/Fable_5_vs_Opus_5_Decision_Report.docx` — editable report.
- `report/Fable_5_vs_Opus_5_Decision_Report.md` — machine-readable report with stable links.
- `Fable_5_vs_Opus_5_Audit_Workbook.xlsx` — 11-sheet audit workbook with formulas, routing, claims, sources, chart data, search log, and evaluation design.
- `data/claim_ledger.csv` — 30 load-bearing claims with epistemic status, direct support, contrary evidence, confidence basis, calculations, scope, and revision triggers.
- `data/source_inventory.csv` — source roles, incentives, dependence, versions, dates, access limits, exact locations, stable links, hashes, and local copies.
- `data/routing_table.csv` — 20 detailed model–effort–harness–worker routes.
- `data/effort_curves.csv` and `data/orchestration_results.csv` — graph-ready values with page/figure provenance.
- `local_eval/` — pre-registered controller-isolation harness and fixture-mode validation results.
- `sources/` — local copies of the four load-bearing Anthropic system cards and the supplied AHR-C 2.0 constitution, with SHA-256 hashes.
- `evidence_pages/` — rendered and text-extracted load-bearing PDF pages.
- `SOURCES_AND_LINKS.md` — convenient stable-link and local-copy index.

## Verification record

- Report DOCX and emitted PDF were rendered; all 45 pages were visually inspected through contact sheets, with no observed clipping or broken charts/tables.
- PDF preflight: 45 tagged pages, embedded fonts, 41 link annotations, no forms, JavaScript, encryption, or reported structural errors.
- Workbook: key formulas recomputed correctly; workbook-wide error scan found no `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, or `#N/A` cells; rendered previews were visually inspected.
- Local evaluation harness: 80 synthetic fixture trajectories, 20 control-balance pairs passed, and 3 unit tests passed. Fixture results are **not model-performance evidence**.

## Important limits

No live calls to Fable 5, Opus 5, Sonnet 5, or GPT-5.6 Sol were available in this execution environment. The local harness therefore validates experimental controls and artifact plumbing only. The report preserves this as a missing-evidence boundary and supplies the test that would isolate controller quality.
