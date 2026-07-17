# Independent downstream_v2 release re-audit v4 — 26 June 2026 Harry P4

## Release verdict: **PASS**

This is an independent re-audit of the 26 June P4 `downstream_v2` candidate after the recall-PDF page-fragment repair (`pdf_fragment_repair_qa_v1.md`). All four repair-specific checks and all six previously-passed gates were re-verified from first principles — computing live hashes, parsing the actual PDF text layout, and inspecting the card source and browser audit directly — rather than trusting prior reports.

No learner artifact, source, build file, publication target, upload, Index/Notion record, or remote system was modified. This report is the only persistent write.

## 1. Repair-specific checks

| Check | Method (independent) | Result |
|---|---|---|
| Q4 list no longer orphaned at page top | `pdftotext -layout` section→page map + visual inspection of `recall_pdf_renders/page-2.png` | **PASS** |
| 2-page contract intact (A4, unencrypted) | `pdfinfo harry_p4_recall.pdf` | **PASS** |
| Recall content SHA unchanged | `sha256sum harry_p4_recall.md / .html / .pdf` | **PASS** |

### 1.1 Q4 orphan eliminated
- The Q4 final bullet `Official reference answer: P=(2,8); reject (6,0) because b>0.` now sits **entirely on page 1**. `pdftotext -f 1 -l 1` finds it **1** time; `pdftotext -f 2 -l 2` finds it **0** times.
- Page 2 opens directly with the proper section heading **`P4 Q6 - trigonometric substitution …`** (verified by both the text dump and a visual read of `page-2.png` — "first content on the page is the heading: P4 Q6 …", no orphaned bullet).
- The single page break now falls *between* completed sections (after Q5, before Q6). No heading or bullet is stranded at a page top.

### 1.2 2-page contract
`pdfinfo` confirms: **Pages: 2**, Page size 595.276 × 841.89 pts (**A4**), **Encrypted: no**, Form: none, JavaScript: no, no URI annotations / embedded files. File size 17149 bytes. Matches the established 2-page contract — the repair's tighter print spacing (`section` margin 20px→14px) held 2 pages without losing the Q4 fix.

### 1.3 Content SHA unchanged
| Artifact | SHA-256 (live) | Matches retained |
|---|---|---|
| `harry_p4_recall.md` | `385afad3dd68156c5dc0d2eb4d312acc4a4acb74cb1d3faf05410b9cfe202023` | **YES** (385afad…) |
| `harry_p4_recall.html` | `bbea753f2e4205c47b750f9a66d67f9f7bf4499fc4d83cf3e2263b80bf03a362` | matches manifest |
| `harry_p4_recall.pdf` | `d3427a7b5f928fffda469b50b876360f1d443a81d0478d5bb339e33859322da2` | matches manifest |

The recall **text** content is byte-identical to the pre-fix source — only a print-only orphan-control CSS rule (`@media print { h3 {break-after:avoid} ul {break-inside:avoid} }`) and a print-margin tightening were added. The repair did not alter any P4 question, status label, or maths.

## 2. Previously-passed gates — re-confirmed

| Gate | Independent method | Result |
|---|---|---|
| Reveal/hide UI | Source inspection of all 7 cards + `browser_audit.json` | **PASS** |
| Maths / marks / status boundaries | Unicode-safe grep of `harry_p4_recall.md` | **PASS** |
| Manifest integrity / freshness | Recomputed SHA-256 of all 33 manifest-listed files | **PASS** |
| Privacy / contamination | 13-term banned-marker scan of MD+HTML | **PASS** |
| Exports (7 PNGs) | Manifest file-hash match + contact sheets present | **PASS** |
| Browser (Chromium) | `browser_audit.json` parse | **PASS** |

### 2.1 Reveal/hide UI — PASS
Independent source parse: all **7/7** cards expose exactly one `button.reveal-control` with a unique `aria-controls` matching its hidden panel; every card opens with `aria-expanded="false"`. `browser_audit.json`: `result: "PASS"`, **14** card/viewport records (7 cards × desktop+mobile), `console_errors: []`, `page_errors: []`, all `initially_collapsed: true`, all `mathjax_rendered: true`, no horizontal overflow, no reload.

### 2.2 Maths / status boundaries — PASS
All required final-guide markers present in `harry_p4_recall.md`: `4x²+y²−2xy=24x`, `2a+b=12`, `P=(2,8)`, `8√3−40/3`, `β=−40`, `200π/3`, plus status labels `self-assessed`, `reference completion`, `Reached`, and the per-question headings (negative-index binomial, volume of revolution, implicit differentiation, separable differential). The Q4 corrected curve/derivative/result and Q5/Q6 reference boundaries are intact.

### 2.3 Manifest integrity — PASS
All **33/33** files listed in `build_manifest.json` match their current on-disk SHA-256 byte-for-byte. `final_guide_hash_proof.matches_authorized_34ce` = **true**. Manifest correctly identifies exactly 7 card HTML + 7 card PNG derivatives and the recall assets.

### 2.4 Privacy / contamination — PASS
Zero matches for all 13 banned markers in `harry_p4_recall.md` and `.html`: `23c096`, `2026-06-29`, `29 June`, `S1`, `Harry Williams`, `Phuc Nguyen`, `/root/`, `http://`, `https://`, `4a+b=12`, `(y−4x)/(y−x)`, `9 marks`, and the authorised guide hash itself. No stale Q4 equation, old derivative, invented nine-mark claim, private path, or full name leaked to learner surfaces.

### 2.5 Exports — PASS
Exactly 7 decodable card PNGs present (`cards/*.png`); each matches its manifest hash. `recall_pdf_contact_sheet.png` and `cards_contact_sheet.png` are present and current (`recall_pdf_contact_sheet.png` SHA `d6a549eb…` matches manifest). Rendered PDF pages `recall_pdf_renders/page-1.png` + `page-2.png` both present with hashes matching manifest.

### 2.6 Browser — PASS
`browser_audit.json` `result: "PASS"` with 14/14 records having truthful `aria-expanded` transitions, pointer + keyboard reveal/hide, MathJax rendered, no overflow, no reload, and zero console/page errors. This corroborates the independent source inspection in 2.1.

## 3. Frozen guide identity (authorised)
SHA-256 of `../guide_v2/revision_guide.pdf` = `34ce9ab8dc45d124f39f7d3ecb951bae3c92f607be5f998615628e118457a56a` — recomputed live and **exact match** to the authorised `34ce…` identity. The recall builder refuses any other guide hash.

## Scope
Independent local re-audit only. No publish / upload / Index / Notion / remote write was performed. The only write is this report. The prior v3 FAIL (recall-PDF Q4 page fragmentation) is now **closed PASS**; all previously-passed gates remain PASS. Overall downstream_v2 release decision: **PASS**.
