# Repair QA v1 — 16 Jun P1 May 2022 downstream_v2

**Disposition: local rebuild and QA PASS.** This is a builder-run repair QA record, **not** an independent audit. No publish, upload, Index, or Notion action was performed.

## Frozen-guide gate

- Recomputed guide PDF SHA-256: `910d7fca22a783a8433c57ad59c6c5f9585b6b802d7e27be855fc4bb656d66a9` — matches `guide_v2/build_verification.md`.
- `pdfinfo`: 8 pages, A4, unencrypted.
- Generator compiles with `PYTHONDONTWRITEBYTECODE=1 python3 -W error::SyntaxWarning -B -m py_compile` and retains a real strict C0 writer gate (only LF permitted below U+0020).

## Repairs applied

1. **Q5 algebra and prompt completeness**
   - Removed the false `+28/3` expansion from the generated Q5 learner card.
   - The final official-reference answer now correctly gives `-4/3 x² - 16/3 x + 20/3` and the three region inequalities.
   - Added the official Q5 givens: turning point, negative x-intercept, `l1`, perpendicular condition, `l2` point, and region boundaries.
2. **Evidence boundary**
   - Q5, Q8 and Q10 now generate an explicit *Official-reference boundary* with three masked boxes: official method label, no-working boundary, and study-use direction.
   - Their cards retain `NOT reviewed live — reference only` and `scored state is unknown`; they no longer render reconstructed step-by-step working as tutor-taught/completed work.
   - Added the missing official prompt givens to Q6, Q8 and Q10.
3. **Q1 multi-step structure**
   - Added a genuine third masked check box: differentiate the final antiderivative back to the original integrand.
4. **Exports and browser audit**
   - Rebuilt all 10 HTML cards and regenerated all 10 PNGs from the current cards, with the desktop PNG export explicitly in the fully revealed state.
   - Fixed inline MathJax layout so prompt givens remain readable; display equations retain responsive overflow protection.
   - Expanded browser QA to test pointer reveal/hide plus keyboard Enter reveal and Space hide at 1400px and 390px.

## Verification results

| Check | Result |
|---|---|
| HTML/PNG card pairs | 10/10 present; every PNG decodes; literal same-directory export anchor exists; each PNG newer than its HTML |
| Masked work-box minimum | All cards have at least 3; Q1 has exactly 3 |
| Q5 false expansion absent / corrected form present | PASS |
| Q5/Q8/Q10 explicit reference-only boundary | PASS |
| Local MathJax | PASS on 20 card viewport records |
| Browser audit | `browser_audit.json` status `pass`; 20 card viewports + 2 landing viewports; no console/page errors, failed images, horizontal overflow, or element horizontal overflow |
| Reveal/accessibility | All 20 card records: one control, initially `aria-expanded=false`/panel hidden; pointer reveal and re-hide; Enter reveal; Space hide — PASS |
| Strict-clean learner scan | 11 learner HTML files; no C0 bytes; no internal path/provider/personal-name forbidden hits |
| SHA-256 sweep | `browser_audit.json`, 10 HTML files and 10 PNG files all verified with `sha256sum -c` |

## Selected current hashes

- `browser_audit.json`: `9f51c98e51d583a73838e51a3e2fe10bc95cb44041c52d56690683f96e6ab53b`
- `cards/P1_May2022_Q5.html`: `a38c94fde62fc212133e175c2ba1071f136f8790395ed50618a53a3f81700b36`
- `cards/P1_May2022_Q5.png`: `e514e401f829f04bc542bd15dbe738c5a739625c37fa40dd44151a860fc2f26d`
- `cards/P1_May2022_Q10.html`: `414c6ddbd6e1cda0ab860e8c710741054719525c39ba05b0b7632b26dda7ca3d`
- `cards/P1_May2022_Q10.png`: `81e5f0f84c2292dbf0e01e1b8c955faf226715cf6777cad28e3bfba561c32237`

Visual spot-check of regenerated Q5 confirmed a readable inline official prompt, visible reference-only boundary, corrected `20/3` final form, and no apparent clipping.
