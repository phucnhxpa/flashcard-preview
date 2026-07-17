# PDF fragment repair QA v1 — 26 June Harry P4 downstream_v2 recall PDF (Q4)

## Result: FIXED & PASS — local-only repair; **no publication, upload, Index, or Notion/remote write performed**

## 1. Defect (pre-fix, from `independent_downstream_reaudit_v3.md`)
The reader-facing two-page recall PDF `harry_p4_recall.pdf` (A4, unencrypted) had a page-fragment defect at the **P4 Q4** section:
- Page 1 opened P4 Q4 (heading + first three bullets).
- Page 2 began with the **orphaned** final bullet `• Official reference answer: P=(2,8); reject (6,0) because b>0.` — no repeated section heading, no continuation label.

Root cause: the recall HTML carried no print-orphan control, so WeasyPrint broke the Q4 `<ul>` across the page boundary, stranding its last `<li>` at the top of page 2. The defect was a layout/orphan issue only (no clipping, overlap, or content loss); all P4 content/status/maths were otherwise correct.

Pre-fix evidence hashes (retained baseline, reproduced byte-for-byte via `python3 -m weasyprint harry_p4_recall.html harry_p4_recall.pdf`):
- `harry_p4_recall.pdf` = `c45d1bf589404c8194bff57d5c6bfb23648309a195fa115518eaec5b44fc9d5a`
- Page-1 / page-2 render markers confirmed the Q4 orphan bullet fell on page 2 (`pdftotext` shows a single `\f` form-feed immediately before the "Official reference answer" line).

## 2. Controlled recall-builder fix
Single, minimal change in `build_clean_downstream.py` (the authoritative recall-HTML generator). The recall PDF is built from `harry_p4_recall.html` via WeasyPrint — verified by byte-identical reproduction of the retained PDF.

Added a print-only orphan-control rule to the recall HTML `<style>` block:
```css
@media print {
  h3 { break-after: avoid }     /* keep each section heading with its following list */
  ul { break-inside: avoid }    /* keep each question's bullet list together */
  main { font-size:15px; line-height:1.42 }
  li { line-height:1.34 } h3 { font-size:18px }
}
```
Plus a slightly tighter `section` margin (`20px → 14px`) so the intact lists still fit the established **2-page** contract (the first attempt with lists kept-together alone pushed the PDF to 3 pages; the modest print-spacing tightening restored 2 pages without losing the Q4 fix). No change to the recall Markdown/HTML **text** — the P4 content, status labels, and maths are byte-identical to the pre-fix source strings.

## 3. Regeneration chain (deterministic, local)
1. `python3 build_clean_downstream.py` — regenerates `harry_p4_recall.md`, `harry_p4_recall.html` (now with the print rule), 7 card HTML files, `index.html`, and `build_manifest.json`.
2. `python3 -m weasyprint harry_p4_recall.html harry_p4_recall.pdf` — rebuilds the 2-page A4 recall PDF.
3. `pdftoppm -png -r 200 -f 1 -l 2 harry_p4_recall.pdf page` — regenerates `recall_pdf_renders/page-1.png` and `page-2.png` (overwriting the exact retained filenames, 1654×2339 = A4 @ 200 dpi).
4. `python3 qa_clean_downstream.py` — runs the full deterministic local QA; regenerates the 7 revealed card PNGs, `cards_contact_sheet.png`, `recall_pdf_contact_sheet.png`, `desktop_landing.png`, `mobile_landing.png`, `browser_audit.json`, `qa_report.md`, and the final `build_manifest.json` with up-to-date file hashes.

## 4. Exact post-repair evidence

### 4.1 Frozen final-guide identity — UNCHANGED (authorised)
`guide_v2/revision_guide.pdf` SHA-256 = `34ce9ab8dc45d124f39f7d3ecb951bae3c92f607be5f998615628e118457a56a` — matches the authorised `34ce…` value exactly. The recall builder refuses to run on any other guide hash.

### 4.2 Recall PDF technical facts (`pdfinfo`)
- Pages: **2**
- Encrypted: **no**
- Page size: **595.276 × 841.89 pts (A4)**
- No JavaScript / forms / URI annotations / embedded files.

### 4.3 Post-repair SHA-256 (generated artifacts)
| Artifact | SHA-256 |
|---|---|
| `harry_p4_recall.pdf` | `d3427a7b5f928fffda469b50b876360f1d443a81d0478d5bb339e33859322da2` |
| `recall_pdf_renders/page-1.png` | `5368ff97c68d523cc0ccb1f595cccf1ad884af3b0bbe0d225fb2707c0a7d713b` |
| `recall_pdf_renders/page-2.png` | `46f3ec263b524c65bf62302a14ab38f1ac16006be3333facf0f37cd0f7bed9e1` |
| `recall_pdf_contact_sheet.png` | `d6a549eb096cf0d70d02e5068402fa6903593e41280b2d841509e5b42bed03b5` |

(These match the entries written into `build_manifest.json` under `files`.)

### 4.4 Section → page map (from `pdftotext -layout`, `\f` = page boundary)
| Section | Page |
|---|---|
| P4 Q1 - negative-index binomial | 1 |
| P4 Q2 - volume of revolution | 1 |
| P4 Q4 - implicit differentiation | 1 |
| **P4 Q4 "Official reference answer: P=(2,8); reject (6,0) because b>0."** | **1 (no longer orphaned)** |
| P4 Q5 - vector-line intersection | 1 |
| *(page break)* | — |
| P4 Q6 - trigonometric substitution | 2 |
| Prior P3 review - range and inverse domain | 2 |
| P4 Q8 - separable differential equation | 2 |
| Status key | 2 |

The single page break now falls *between* completed sections (after Q5, before Q6). **No section heading or bullet is orphaned at a page top.**

### 4.5 Rendered-page visual confirmation
- **`recall_pdf_renders/page-1.png`**: P4 Q4 section heading appears together with its complete 4-bullet list, *including* the final "Official reference answer: P=(2,8); reject (6,0) because b>0." bullet, entirely on page 1. Last visible content = P4 Q5 "Official reference: β=−40, P=(−7,−37,−15)."
- **`recall_pdf_renders/page-2.png`**: page opens directly with the proper section heading **"P4 Q6 - trigonometric substitution …"** — no bullet stranded at the top without a heading. Subsequent headings: Prior P3 review, P4 Q8, Status key.

## 5. P4 content / status / maths preservation
The recall Markdown/HTML text is unchanged byte-for-byte from the pre-fix source. The deterministic QA confirms all required final-guide markers are present and no stale/contamination markers leaked:
- Present: `4x^2 + y^2 − 2xy = 24x`, `2a+b=12`, `P=(2,8)`, `8√3−40/3`, `β=−40`, `200π/3`, `STATUS:`.
- Absent (contamination guard): `23c096`, `2026-06-29`, `29 June`, `S1`, `Harry Williams`, `Phuc Nguyen`, `/root/`, `http(s)://`, `4a+b=12`, `(y−4x)/(y−x)`, `9 marks`, and the authorised guide hash itself.

## 6. Full dependent-asset QA — PASS
`qa_clean_downstream.py` exit 0: "QA PASS: final guide hash, 7 reveal/hide cards and fully revealed PNGs, desktop/mobile pointer/keyboard/ARIA browser checks, recall PDF, and contamination scan."
- 7/7 cards × 2 viewports reveal/hide interaction: PASS (repaired in prior v1; retained here).
- 7 card PNGs decoded and ≥1000 px: PASS.
- Recall PDF 2-page/unencrypted facts and reader-safe text scan: PASS.
- Frozen-guide hash gate and quarantine presence: PASS.
- `build_manifest.json` `final_guide_hash_proof.matches_authorized_34ce` = **true**.

## 7. Scope
Local QA only. No publish/upload/Index/Notion/remote write was performed. All regenerated artifacts remain in `…/2026-06-26_harry_p4/downstream_v2/`. This record is deterministic local QA evidence, not an independent audit.
