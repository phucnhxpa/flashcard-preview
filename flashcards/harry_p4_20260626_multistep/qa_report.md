# Clean downstream_v2 local QA report

## Verdict: PASS (local-only; not an independent review)

- **Frozen guide proof:** SHA-256 of `guide_v2/revision_guide.pdf` is `34ce9ab8dc45d124f39f7d3ecb951bae3c92f607be5f998615628e118457a56a`. It exactly matches the authorised final guide identity.
- **Quarantine:** the predecessor was moved to `_quarantine/downstream_v2_contaminated_pre_final_guide_2026-07-17/` before this build. The clean generator reads only the frozen final guide, its text mirror and source register.
- **Deliverables:** reader-safe recall Markdown + 2-page unencrypted A4 PDF; one landing; exactly seven standalone multi-step cards and seven regenerated static PNGs.
- **Reveal UI:** every card starts with its grey working panel hidden and an accessible native button labelled “Reveal working”. Across all seven cards at desktop and 390-px mobile widths, pointer reveal/hide and keyboard Enter-reveal/Space-hide changed `aria-expanded` truthfully without reload. Status, marks, prompt, visual, final answer and study boundary remained visible while working was hidden. `browser_audit.json` records all 14 card/viewport checks.
- **UI/asset checks:** all seven cards use the staged local MathJax tex-svg asset, rendered MathJax in Chromium, have at least three grey work boxes, and carry a literal same-directory PNG download anchor. PNGs were captured after revealing all working. All linked child HTML/PNG assets returned local HTTP 200. Desktop/mobile overflow and console/page-error checks passed.
- **Content/status checks:** corrected P4 Q4 curve/derivative/gradient relation/result, Q5/Q6 reference boundaries, P3 separation, and self-assessed Q2/Q8 boundaries are present. Unsupported mark allocations are explicitly not supplied rather than invented.
- **Contamination scan:** zero legacy source-signature matches, zero date/lane-marker matches, and zero private-path/full-name matches in learner-facing HTML, Markdown or recall-PDF extracted text.
- **Visual evidence:** `cards_contact_sheet.png`, `recall_pdf_contact_sheet.png`, `desktop_landing.png`, and `mobile_landing.png` were regenerated for local inspection.

This is a deterministic local QA record, not a publication, upload, Index/Notion operation, or independent-review claim.
