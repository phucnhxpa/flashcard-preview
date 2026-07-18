# Independent downstream audit v1 — 16 Jun P1 May 2022

**Disposition: FAIL — release blocked.**

## Release blockers

1. **Q5 mathematical working is internally false in the live HTML.** `cards/P1_May2022_Q5.html`, Part (a), Step 1 expands
   \[
   12-\tfrac43(x+2)^2
   \]
   as
   \[
   -\tfrac43x^2-\tfrac{16}{3}x+\tfrac{28}{3},
   \]
   whereas the constant is \(12-\tfrac{16}{3}=\tfrac{20}{3}\). The same card subsequently claims the correct \(\tfrac{20}{3}\) form, so its revealed method contradicts its final/reference answer. This fails mathematics and source fidelity.

2. **HTML/PNG export parity is broken.** The Q5 PNG does **not** export the current Q5 HTML: its rendered working instead presents the corrected short form and omits the live HTML's erroneous \(\tfrac{28}{3}\) expansion. Q10 likewise has materially abbreviated PNG working versus its current HTML. The ten PNGs therefore cannot be represented as static exports of the audited HTML. Re-render and audit the exact live cards after correction.

3. **The source-limited boundary is violated for Q5, Q8 and Q10.** Each card visibly declares “NOT reviewed live — reference only,” which is correct, but each then supplies a reconstructed, step-by-step solution beyond the frozen guide's reference-answer-only evidence. The guide provides only reference answers for these unavailable lesson items; it does not support presenting reconstructed working as lesson-derived/reference-only completion. This conflicts with the declared status boundary.

4. **Several prompts/solutions are not standalone or source-faithful.** The deck calls these “Official question[s]” while omitting indispensable official givens:
   - Q5(b)/(c): the stated point/gradient and the actual three inequalities/region diagram are absent;
   - Q6: the simultaneous equations are absent;
   - Q8: the radius/diagram and the derivation givens are absent;
   - Q10: the curve, point and relation containing \(k\) are absent.

   Their answers consequently introduce or rely on information not available in the visible prompt (for example, “the given point,” “worksheet values,” or “the curve”). This fails standalone recall, official-question wording, and marks/content fidelity.

5. **The current browser-audit artifact is itself a failed release record.** `browser_audit.json` has top-level `"status": "fail"`; it records mobile failures for Q2, Q4, Q5, Q7, Q8 and Q10. A fresh independent Chromium interaction check did confirm functional reveal/hide, local MathJax, no runtime errors and no document-width overflow at 1400px/390px, but that does not cure the shipped failed audit or establish PNG parity.

6. **Q1 misses the current multi-step box minimum.** `P1_May2022_Q1.html` contains only two `.work` boxes; the multi-step contract requires at least three per card.

---

This audit read, recomputed and compared only. No publish, upload, Index, Notion write, or artifact rebuild was performed.
