# Verification record

**Verified:** 2026-07-24  
**Executing model:** GPT-5.6 Pro

## Report artifacts

- `report/Fable_5_vs_Opus_5_Decision_Report.docx`: ZIP container integrity check passed.
- `report/Fable_5_vs_Opus_5_Decision_Report.pdf`: 45 pages; tagged; no forms; no JavaScript; not encrypted; Letter page size; 88,614 extractable text characters; all 7 fonts embedded.
- All 45 rendered pages were visually inspected through five contact sheets. No clipping, overlapping objects, broken tables, or broken charts were observed.
- The PDF contains 41 live link annotations, as recorded during PDF preflight.

## Workbook

- `Fable_5_vs_Opus_5_Audit_Workbook.xlsx`: ZIP container integrity check passed.
- Key formula cells were re-imported with `artifact_tool` and recomputed to 0.5, 0.5, 2.1044957473, and 0.6913730255.
- A workbook-wide error scan found zero matches for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, and `#N/A`.
- Five rendered sheet previews were visually inspected: Executive Routing, Routing Table, Claim Ledger, Effort Curves, and Evaluation Design.

## Data and calculations

- Claim ledger: 30 rows.
- Routing table: 20 rows and all required routing fields present.
- Source inventory: 19 rows.
- Effort-curve data: 100 model–benchmark–effort points.
- Recomputed ratios and selected source transcriptions passed assertions.

## Controlled local evaluation harness

- Fixture-mode execution produced 80 synthetic trajectories.
- Control balance passed for all 20 task/repeat pairs.
- Three unit tests passed.
- Fixture mode performs no model calls and provides no model-performance evidence; it validates causal controls, schema, analysis plumbing, and balance only.

## Tool limitations and failures

- `qpdf` was not installed, so PDF validation used `pdfinfo`, `pdftotext`, `pdffonts`, PDF rendering, link inspection, and visual review instead.
- Official PDFs could not be opened through the web PDF renderer (`(400) OK`); stable official PDFs were downloaded, hashed, rendered locally, and inspected.
- One arXiv PDF download and one local Git clone failed DNS resolution; HTML/abstract and a pinned raw commit file were used instead.
- No live model API access was available for the controller experiment.
