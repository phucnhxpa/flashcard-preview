# Deterministic self-QA — Harry P3 October 2025 + ESAT multi-step v2

**Scope:** local-only build under `multistep_v2/`; five cards (ESAT + P3 Q2–Q5), landing page, diagrams, static PNG exports.

**Status:** `PASS`

This is builder-run deterministic self-QA. It is **not** an independent card review, and no publication has been performed.

## Checks
- [PASS] **guide_provenance_exists** — /root/agent-artifacts/workspace/revision_pipeline/lessons/2026-07-11_harry_p3_esat/guide/harry_2026-07-11_p3_esat_revision_guide.tex
- [PASS] **exact_card_count** — 5 card HTML files; intended source-bounded scope is ESAT + P3 Q2–Q5
- [PASS] **landing_tile_count** — index.html declares five card tiles
- [PASS] **ESAT_warmup:depth** — 10030 bytes
- [PASS] **ESAT_warmup:mathjax_svg** — tex-svg present; CHTML absent
- [PASS] **ESAT_warmup:literal_export** — literal same-directory PNG anchor
- [PASS] **ESAT_warmup:question_header** — standalone header and visible marks
- [PASS] **ESAT_warmup:parts_and_carryins** — 2 exam parts; 3 outside-mask carry-ins (including recall strip)
- [PASS] **ESAT_warmup:maskable_work** — 3 grey maskable panels
- [PASS] **ESAT_warmup:visual_anchor** — at least one compact teaching visual
- [PASS] **P3_Oct2025_Q2:depth** — 11163 bytes
- [PASS] **P3_Oct2025_Q2:mathjax_svg** — tex-svg present; CHTML absent
- [PASS] **P3_Oct2025_Q2:literal_export** — literal same-directory PNG anchor
- [PASS] **P3_Oct2025_Q2:question_header** — standalone header and visible marks
- [PASS] **P3_Oct2025_Q2:parts_and_carryins** — 3 exam parts; 4 outside-mask carry-ins (including recall strip)
- [PASS] **P3_Oct2025_Q2:maskable_work** — 4 grey maskable panels
- [PASS] **P3_Oct2025_Q2:visual_anchor** — at least one compact teaching visual
- [PASS] **P3_Oct2025_Q3:depth** — 10928 bytes
- [PASS] **P3_Oct2025_Q3:mathjax_svg** — tex-svg present; CHTML absent
- [PASS] **P3_Oct2025_Q3:literal_export** — literal same-directory PNG anchor
- [PASS] **P3_Oct2025_Q3:question_header** — standalone header and visible marks
- [PASS] **P3_Oct2025_Q3:parts_and_carryins** — 3 exam parts; 4 outside-mask carry-ins (including recall strip)
- [PASS] **P3_Oct2025_Q3:maskable_work** — 4 grey maskable panels
- [PASS] **P3_Oct2025_Q3:visual_anchor** — at least one compact teaching visual
- [PASS] **P3_Oct2025_Q4:depth** — 11165 bytes
- [PASS] **P3_Oct2025_Q4:mathjax_svg** — tex-svg present; CHTML absent
- [PASS] **P3_Oct2025_Q4:literal_export** — literal same-directory PNG anchor
- [PASS] **P3_Oct2025_Q4:question_header** — standalone header and visible marks
- [PASS] **P3_Oct2025_Q4:parts_and_carryins** — 3 exam parts; 4 outside-mask carry-ins (including recall strip)
- [PASS] **P3_Oct2025_Q4:maskable_work** — 4 grey maskable panels
- [PASS] **P3_Oct2025_Q4:visual_anchor** — at least one compact teaching visual
- [PASS] **P3_Oct2025_Q5:depth** — 11531 bytes
- [PASS] **P3_Oct2025_Q5:mathjax_svg** — tex-svg present; CHTML absent
- [PASS] **P3_Oct2025_Q5:literal_export** — literal same-directory PNG anchor
- [PASS] **P3_Oct2025_Q5:question_header** — standalone header and visible marks
- [PASS] **P3_Oct2025_Q5:parts_and_carryins** — 4 exam parts; 5 outside-mask carry-ins (including recall strip)
- [PASS] **P3_Oct2025_Q5:maskable_work** — 5 grey maskable panels
- [PASS] **P3_Oct2025_Q5:visual_anchor** — at least one compact teaching visual
- [PASS] **banned_draft_meta_phrases** — 0 hits
- [PASS] **no_placeholders** — 0 hits
- [PASS] **no_illegal_control_characters** — 0 files
- [PASS] **privacy_scan** — no emails, tokens, passwords, or card-like numbers
- [PASS] **local_relative_assets** — 26 destinations checked; 0 missing
- [PASS] **png_integrity_dimensions_variance** — 13 PNGs checked; failures: []
- [PASS] **browser_desktop_mobile_mathjax_overflow** — all cards + landing clean

## Scope and source boundary
- Guide provenance is the SHA-256 recorded in `build_manifest.json` for the passed final 11 July guide.
- P3 Q1 is omitted rather than reconstructed from legacy material: the passed guide says it was discussed only and does not retain a complete verbatim standalone prompt. P3 Q6–Q9 were not discussed.
- `independent_review.status = not_recorded`; `publication.status = local_only`.
