#!/usr/bin/env python3
r"""Local-only rebuild of the 16 June 2026 Harry P1 May 2022 recall + multi-step deck.

Authored afresh from the passed evidence-led guide (guide_v2/, independent AV audit v1 = PASS).
Strict-clean contract:
  - Card expressions are authored as RAW Python strings with single backslash delimiters
    \( ... \) and \[ ... \]; the file therefore contains real TeX, never a visible `tfrac`
    shim. No double-backslash control-char shim is applied.
  - C0 guard: any output text asset containing an illegal control byte (< 0x20 except LF/CR/TAB)
    fails the build.
  - MathJax v3 tex-svg local asset referenced in every card and the recall mirror.
  - Grey maskable finalized work boxes; REAL accessible reveal/hide control (native button).
  - Literal same-directory PNG export anchors; Playwright/Chromium static PNGs.
"""
from __future__ import annotations
import hashlib, html, json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# The builder lives inside ui_rebuild_v2/multistep; frozen inputs stay at the lesson root.
LESSON = ROOT.parent.parent
GUIDE = LESSON / "guide_v2" / "revision_guide.pdf"
GUIDE_TEXT = LESSON / "guide_v2" / "revision_guide_text.md"
SOURCE_DATE = "2026-06-16"
SLUG = "harry_p1_may2022_20260616"

EXPECTED_GUIDE_SHA = "910d7fca22a783a8433c57ad59c6c5f9585b6b802d7e27be855fc4bb656d66a9"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_strict(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Only LF is permitted below U+0020 in generated learner text assets.
    if any(ord(ch) < 32 and ch != "\n" for ch in text):
        raise ValueError(f"{path.name} contains a forbidden C0 control character")
    path.write_text(text, encoding="utf-8", newline="\n")

def assert_text_is_transport_safe(text: str, label: str) -> str:
    """Fail the build if an output text asset has an illegal C0 control byte."""
    illegal = sorted({ord(ch) for ch in text if ord(ch) < 32 and ch not in "\n\r\t"})
    if illegal:
        raise ValueError(f"{label} contains illegal control characters: {illegal}")
    return text

if sha(GUIDE) != EXPECTED_GUIDE_SHA:
    raise SystemExit("Frozen passed-guide hash mismatch; refusing to create derivatives.")

mathjax = ROOT / "mathjax-tex-svg.js"
if not mathjax.is_file():
    raise SystemExit("Missing fresh local MathJax tex-svg asset.")

CSS = r"""
*{box-sizing:border-box} :root{--ink:#1d1d1f;--muted:#6e6e73;--line:#d2d2d7;--soft:#f5f5f7;--work:#fafafa;--paper:#fff}
html,body{margin:0;padding:0;background:#f0f0f2;color:var(--ink)}
body{font:14px/1.55 -apple-system,BlinkMacSystemFont,"SF Pro Text","Inter",system-ui,sans-serif;-webkit-font-smoothing:antialiased;padding:28px 18px 40px}
.export-btn{position:fixed;top:16px;right:16px;z-index:100;background:#1d1d1f;color:#fff;border:0;border-radius:8px;padding:8px 16px;font:600 12px -apple-system,BlinkMacSystemFont,"SF Pro Text",system-ui,sans-serif;text-decoration:none;box-shadow:0 2px 8px rgba(0,0,0,.18)}
.card{max-width:1260px;margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px 30px 28px;box-shadow:0 1px 2px rgba(0,0,0,.04);overflow:hidden}
.meta{font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin-bottom:6px} h1{font:650 21px/1.28 -apple-system,"SF Pro Display",system-ui,sans-serif;margin:0 0 16px;letter-spacing:-.015em}
.q-header{background:var(--soft);border-radius:12px;padding:14px 18px;margin-bottom:18px;font-size:13px;line-height:1.55;min-width:0}.q-header .label{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:5px;font-weight:700}.q-header p{margin:5px 0}.q-header blockquote{margin:7px 0;padding-left:12px;border-left:3px solid var(--line)}.q-header table,.step-body table{border-collapse:collapse;margin:8px 0;width:100%;font-size:12px;max-width:100%;table-layout:auto}.q-header td,.q-header th,.step-body td,.step-body th{border:1px solid var(--line);padding:4px 7px;vertical-align:top}.q-marks{font-weight:650;margin-top:8px;font-size:12.5px}.source-note{margin-top:8px;color:#424245;font-size:12px}
.parts{} .part{margin-bottom:18px}.part-h{font:650 14.5px/1.3 -apple-system,system-ui,sans-serif;margin:0 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line)}.part-h .pmarks{float:right;font-weight:500;color:var(--muted);font-size:12.5px}.given{background:#fff;border-left:2.5px solid var(--ink);padding:7px 10px;margin:0 0 10px;font-size:12.5px;border-radius:0 6px 6px 0}.steps{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start}.steps>.step:last-child{grid-column:1/-1}@media(max-width:980px){.steps{grid-template-columns:1fr}.card{padding:20px 16px}.steps>.step:last-child{grid-column:auto}}
.step{border:1px solid #c7c7cc;background:var(--work);border-radius:10px;padding:12px 14px 11px;margin:0;min-width:0}.step-top{display:flex;align-items:flex-start;justify-content:space-between;gap:6px;margin-bottom:8px;padding-bottom:7px;border-bottom:1px solid var(--line)}.step-tag{font:650 12.5px/1.35 -apple-system,system-ui,sans-serif;display:flex;align-items:flex-start;gap:7px;flex:1}.step-num{background:var(--ink);color:#fff;padding:3px 7px;border-radius:5px;letter-spacing:.04em;font-size:10.5px;flex-shrink:0;line-height:1.2;margin-top:1px}.step-goal{color:transparent;width:0;overflow:hidden}.step-marks{font-size:10.5px;color:var(--muted);font-weight:500;flex-shrink:0;letter-spacing:.04em;margin-top:3px}.step-body{font-size:13px;line-height:1.56;min-width:0}.step-body p{margin:6px 0}.step-body ul,.step-body ol{margin:6px 0 6px 19px;padding:0}.step-body li{margin:3px 0}.why{background:#fff;border-left:2px solid var(--ink);padding:6px 9px;margin:8px 0;font-size:12.2px;color:#3a3a3e;border-radius:0 5px 5px 0}.sense{background:#fff;border:1px dashed #c7c7cc;border-radius:6px;padding:6px 9px;margin-top:8px;font-size:12.2px}.step-result{margin-top:8px;padding:6px 10px;background:#fff;border:1px dashed #c7c7cc;border-radius:6px;font-size:12.5px;font-weight:600}
.step-body mjx-container,.q-header mjx-container{max-width:100%;min-width:0}.step-body mjx-container[display="true"],.q-header mjx-container[display="true"]{display:block!important;text-align:left!important;margin:.45em 0!important;overflow:visible!important}.step-body mjx-container[display="true"] svg,.q-header mjx-container[display="true"] svg{max-width:100%!important;height:auto!important}.step-body svg,.q-header svg{max-width:100%;height:auto}
.index-body{max-width:1040px;margin:0 auto}.index-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:14px 0;box-shadow:0 1px 2px rgba(0,0,0,.04)}.index-card h3{margin:0 0 5px;font-size:16px}.links{display:flex;gap:10px;flex-wrap:wrap;margin:8px 0}.links a{font-size:12.5px;padding:6px 11px;border-radius:8px;background:#1d1d1f;color:#fff;text-decoration:none}.links a.alt{background:#fff;color:#1d1d1f;border:1px solid var(--line)}.preview{width:100%;max-width:980px;border:1px solid var(--line);border-radius:10px;margin-top:8px}.badge{display:inline-block;background:#f5f5f7;border:1px solid var(--line);border-radius:999px;padding:2px 8px;font-size:11.5px;color:#424245;margin-right:5px}
"""

# Each header is normalised from the official QP and the passed guide (AV audit PASS).
# Card TeX is authored as raw strings with single backslash delimiters \( ... \) / \[ ... \].
CARDS = [
 dict(q=1, title="Indefinite integration", marks=4,
   status="Reviewed & corrected (integration-vs-differentiation slip). The official QP/MS control wording, marks and values.",
   header=r'''(a) Find \(\displaystyle\int\left(10x^5+6x^3-\frac{3}{x^2}\right)dx\). (4)''',
   parts=[('a',4,r'No carry-in: rewrite every term as a power of \(x\) before integrating.',
     r'Use \(\int x^n\,dx=\frac{x^{n+1}}{n+1}+c\). Rewrite \(-\frac{3}{x^2}=-3x^{-2}\).',
     r'''<p><b>Step 1 — identify the rule and its domain.</b> The power rule for integration is \(\displaystyle\int x^n\,dx=\frac{x^{n+1}}{n+1}+c\), valid for every real \(n\neq -1\). The integral of a sum is the sum of the integrals, so we may treat each of the three terms \(10x^5\), \(6x^3\) and \(-3x^{-2}\) separately and integrate each on its own. This question specifically tests indefinite integration of polynomial terms, so no limits are involved and a constant of integration must appear at the end.</p>
<p><b>Step 2 — rewrite the reciprocal term as a negative power.</b> A denominator power becomes a negative index: \(-\frac{3}{x^2}=-3x^{-2}\). The integrand is now \(10x^5+6x^3-3x^{-2}\), a pure polynomial in \(x\) (with a negative power) and no quotients left, which is exactly the shape the power rule needs.</p>
<p><b>Step 3 — raise the power by one and divide by the new power.</b> For \(10x^5\): add 1 to the power to get 6, then divide the coefficient by 6 → \(\frac{10}{6}x^6=\frac{5}{3}x^6\). For \(6x^3\): → \(\frac{6}{4}x^4=\frac{3}{2}x^4\). For \(-3x^{-2}\): the new power is \(-1\), and dividing by \(-1\) flips the sign, giving \(-3\cdot\frac{x^{-1}}{-1}=+3x^{-1}=+\frac{3}{x}\).</p>
\[10\cdot\frac{x^6}{6}+6\cdot\frac{x^4}{4}-3\cdot\frac{x^{-1}}{-1}+c
=\frac{5}{3}x^6+\frac{3}{2}x^4+\frac{3}{x}+c.\]
<p><b>Step 4 — differentiate to check the answer.</b> \(\frac{d}{dx}\!\left(\frac{5}{3}x^6\right)=10x^5\), \(\frac{d}{dx}\!\left(\frac{3}{2}x^4\right)=6x^3\), and \(\frac{d}{dx}(3x^{-1})=-3x^{-2}\), which is precisely the starting integrand. This confirms the antiderivative is correct.</p>
<p><b>Step 5 — do not forget \(+c\).</b> An indefinite integral has no limits, so the most general antiderivative is a whole family differing by a constant; the \(+c\) is mandatory and is itself worth a mark. The original lesson attempt went wrong by differentiating instead of integrating and also mishandling the sign on \(-3x^{-2}\), which is exactly the slip this correction addresses.</p>
<p><b>Step 6 — exam technique.</b> When the integrand has several terms, always integrate term by term; there is no single formula for a whole bracket of different powers. Watch the reciprocal term carefully: \(\frac{1}{x^2}=x^{-2}\), and after integrating you obtain \(x^{-1}=\frac1x\), which here is positive because the starting term was negative. Keep the fractional coefficients \(\frac{5}{3}\) and \(\frac{3}{2}\) exact — do not convert them to decimals, or you may lose an accuracy mark. If you are ever unsure, differentiating your final answer must reproduce the original integrand exactly; that check is the fastest way to catch a sign or power error. Finally, present the answer as a single combined expression with \(+c\); examiners look for the three integrated terms written together, not three separate lines, and the \(+c\) must appear explicitly or the mark is lost.</p>''',
     r'The original attempt differentiated instead of integrating and mishandled the sign on \(-3x^{-2}\). Add one to the power, divide by the new power, keep \(+c\).',
     r'<p><b>Check box — differentiate your completed answer.</b> Differentiate \(\frac{5}{3}x^6+\frac{3}{2}x^4+\frac3x+c\): this returns \(10x^5+6x^3-3x^{-2}\), the original integrand. This is a genuine final working/check stage, not an additional inferred lesson event.</p>')],
   final=r'\(\displaystyle\frac{5}{3}x^6+\frac{3}{2}x^4+\frac{3}{x}+c\).'),

 dict(q=2, title="Sine rule and the obtuse angle", marks=5,
   status="Reviewed live (sine rule; obtuse-case recognition). The official QP/MS control wording, marks and values.",
   header=r'''In triangle \(ABC\), \(AB=21\), \(BC=13\), \(\angle BAC=25^\circ\). (a) Find \(\sin x\). (b) Find the obtuse angle \(x\). (5)''',
   parts=[('a',None,r'No carry-in: the givens are \(AB=21\), \(BC=13\), \(\angle BAC=25^\circ\).',
     r'Apply the sine rule with the side opposite the required angle.',
     r'''<p><b>Step 1 — match side to opposite angle.</b> Side \(BC=13\) is opposite \(\angle A=25^\circ\). Side \(AB=21\) is opposite the angle labelled \(x\) at \(C\). The sine rule is \(\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}\).</p>
<p><b>Step 2 — set up the ratio.</b> Pair the side opposite \(x\) with \(\sin x\) and the side opposite \(25^\circ\) with \(\sin25^\circ\):</p>
\[\frac{\sin x}{21}=\frac{\sin25^\circ}{13}.\]
<p><b>Step 3 — solve and keep precision.</b> \(\sin x=\frac{21\sin25^\circ}{13}\). The calculator gives \(\sin25^\circ\approx0.4226\), so \(\sin x\approx0.6827\) to 4 d.p.</p>
\[\sin x=\frac{21\sin25^\circ}{13}=0.6827\ \text{(4 d.p.)}.\]
<p><b>Step 4 — why 4 d.p. matters.</b> The mark scheme awards an accuracy mark for the 4-decimal value. Rounding too early to 0.683 loses that mark and propagates error into part (b).</p>
<p><b>Step 5 — exam technique for the ratio.</b> Set the sine rule up by pairing each side with the sine of its opposite angle; do not accidentally pair \(AB=21\) with \(\sin25^\circ\) (that would invert the ratio and give the wrong reciprocal). Write the "= " chain as \(\frac{\sin x}{21}=\frac{\sin25^\circ}{13}\) and solve by multiplying both sides by 21, rather than cross-multiplying in your head where a sign or factor is easily lost. Keep the unrounded value stored in your calculator so part (b) uses 0.6827, not a rounded copy. Accuracy marks are won by process: show the exact 4-d.p. figure even if later steps round for a final stated value.</p>''',
     r'Wrote 0.6830 (instead of 0.6827) and carried it forward, losing the 4-d.p. accuracy mark on part (a).'),
    ('b',None,r'Carry-in: \(\sin x=0.6827\).',
     r'Two angles share a sine; pick the one the triangle forces (obtuse here).',
     r'''<p><b>Step 1 — the sine ambiguity.</b> For any acute \(\theta\), both \(\theta\) and \(180^\circ-\theta\) have the same sine. So \(\sin x=0.6827\) admits two candidates.</p>
<p><b>Step 2 — principal value.</b> \(\arcsin(0.6827)=43.05^\circ\) (acute).</p>
<p><b>Step 3 — use the longest-side condition.</b> The question states that \(AB=21\) is the longest side. Since \(AB\) is opposite \(x\), angle \(x\) must be the largest angle. The acute candidate \(43.05^\circ\) would be smaller than another angle in the triangle, so take the supplementary candidate:</p>
\[x=180^\circ-43.05^\circ=136.95^\circ.\]
<p><b>Step 4 — geometric check.</b> With \(x=136.95^\circ\), the third angle is \(180-25-136.95=18.05^\circ>0\). Then the side-angle order is consistent: \(21\), the longest side, is opposite \(136.95^\circ\), the largest angle. If \(x=43.05^\circ\), the third angle would be \(111.95^\circ\), making the side opposite that third angle longer than \(AB\), contradicting the source condition.</p>
<p><b>Step 5 — exam technique.</b> Keep the 4 d.p. sine value until the final angle. When sine gives two branches, use the triangle's side ordering: the largest side lies opposite the largest angle. Here \(AB=21\) is explicitly longest and lies opposite \(x\), so the supplementary branch is forced. This is stronger than merely preferring an obtuse-looking diagram, which may not be drawn to scale.</p>''',
     r'Forget the second sine solution, or pick the acute angle when the triangle requires obtuse.')],
   final=r'\(\sin x=0.6827\) (4 d.p.); \(x=136.95^\circ\) (obtuse).'),

 dict(q=3, title="Surds: simplify and rationalise", marks=5,
   status="Touched briefly (simplification re-explained; not a logged lost-mark review). The official QP/MS control wording, marks and values.",
   header=r'''(i) Simplify \(\displaystyle\frac{\sqrt{180}-\sqrt{80}}{\sqrt5}\). (ii) Rationalise \(\displaystyle\frac{4\sqrt5-5}{7-3\sqrt5}\). (5)''',
   parts=[('i',None,r'No carry-in: split the numerator over the common root.',
     r'Use \(\frac{\sqrt a-\sqrt b}{\sqrt c}=\frac{\sqrt a}{\sqrt c}-\frac{\sqrt b}{\sqrt c}=\sqrt{a/c}-\sqrt{b/c}\).',
     r'''<p><b>Step 1 — split the fraction.</b> Dividing by \(\sqrt5\) distributes over the minus:</p>
\[\frac{\sqrt{180}}{\sqrt5}-\frac{\sqrt{80}}{\sqrt5}=\sqrt{\frac{180}{5}}-\sqrt{\frac{80}{5}}=\sqrt{36}-\sqrt{16}.\]
<p><b>Step 2 — evaluate the square roots.</b> \(\sqrt{36}=6\) and \(\sqrt{16}=4\).</p>
\[=6-4=2.\]
<p><b>Step 3 — why this is cleaner than expanding first.</b> Trying to simplify \(\sqrt{180}=6\sqrt5\) and \(\sqrt{80}=4\sqrt5\) first also works: \(\frac{6\sqrt5-4\sqrt5}{\sqrt5}=\frac{2\sqrt5}{\sqrt5}=2\). Both routes confirm the integer answer; keeping the surd in the numerator cancels neatly.</p>
<p><b>Step 4 — exam technique.</b> When a root sits over a difference in the numerator, do not split it as \(\frac{\sqrt{180}-\sqrt{80}}{\sqrt5}\neq\frac{\sqrt{180}}{\sqrt5}-\sqrt{80}\); the subtraction must stay inside the single fraction before you divide term by term. The product/quotient rule for surds (\(\frac{\sqrt a}{\sqrt c}=\sqrt{a/c}\)) only applies to one surd at a time. Always check the final answer is in the simplest exact form — here a plain integer, not a surd — and never introduce a decimal approximation for a question that resolves exactly to 2. A useful check is to verify \(\sqrt{180}/\sqrt5=\sqrt{36}=6\) and \(\sqrt{80}/\sqrt5=\sqrt{16}=4\) separately, then subtract, which makes the arithmetic transparent.</p>''',
     r'Leave the denominator as a single root instead of splitting the numerator.'),
    ('ii',None,r'No carry-in: multiply top and bottom by the conjugate of \(7-3\sqrt5\).',
     r'Conjugate of \(a-b\sqrt5\) is \(a+b\sqrt5\); the product removes the surd.',
     r'''<p><b>Step 1 — choose the conjugate.</b> The denominator is \(7-3\sqrt5\). Multiply numerator and denominator by its conjugate \(7+3\sqrt5\); this exploits \((A-B)(A+B)=A^2-B^2\) to leave a rational denominator.</p>
\[\frac{(4\sqrt5-5)(7+3\sqrt5)}{(7-3\sqrt5)(7+3\sqrt5)}.\]
<p><b>Step 2 — denominator.</b> \(7^2-(3\sqrt5)^2=49-9\cdot5=49-45=4\).</p>
<p><b>Step 3 — numerator, expand carefully.</b> \((4\sqrt5)(7)=28\sqrt5\); \((4\sqrt5)(3\sqrt5)=12\cdot5=60\); \((-5)(7)=-35\); \((-5)(3\sqrt5)=-15\sqrt5\). Collect: \(28\sqrt5-15\sqrt5=13\sqrt5\), and \(60-35=25\), so numerator \(=25+13\sqrt5\).</p>
\[=\frac{25+13\sqrt5}{4}=\frac{25}{4}+\frac{13}{4}\sqrt5.\]
<p><b>Step 4 — check the form.</b> The answer is \(a+b\sqrt5\) with rational \(a,b\), the required "rationalised" shape.</p>
<p><b>Step 5 — exam technique.</b> Rationalising always means "remove the surd from the denominator"; the tool is the conjugate, and the identity \((A-B)(A+B)=A^2-B^2\) is what makes the denominator rational because \((\sqrt5)^2=5\). Keep the brackets intact when you expand the numerator — a dropped minus on \((-5)(3\sqrt5)=-15\sqrt5\) is the usual slip and would give the wrong coefficient of \(\sqrt5\). Once the denominator is the integer 4, split the fraction into \(\frac{25}{4}+\frac{13}{4}\sqrt5\); do not try to "cancel" the 4 into the \(\sqrt5\), since 4 is not a factor of \(\sqrt5\). Finally, present the answer exactly — surd form, not a decimal approximation. If the denominator had been a single term like \(\sqrt5\) you would multiply top and bottom by \(\sqrt5\) instead; the conjugate method is specifically for a sum or difference involving a surd.</p>''',
     r'Sign error when expanding with the conjugate.')],
   final=r'(i) \(2\); (ii) \(\frac{25}{4}+\frac{13}{4}\sqrt5\).'),

 dict(q=4, title="Graph transformations", marks=6,
   status="Reviewed live (vertical shift and reflection in the y-axis). The official QP/MS control wording, marks and values.",
   header=r'''Given \(y=f(x)\) with minimum \(P(-1,0)\), maximum \(Q(\tfrac32,2)\) and asymptote \(y=1\), sketch (i) \(y=f(x)-2\) and (ii) \(y=f(-x)\). (6)''',
   parts=[('i',None,r'Carry-in: min \((-1,0)\), max \((\tfrac32,2)\), asymptote \(y=1\).',
     r'A vertical shift moves every \(y\)-value; the asymptote shifts with the curve.',
     r'''<p><b>Step 1 — what "−2" does.</b> Replacing \(y\) by \(y-2\) translates the graph down by 2 units: every point \((x,y)\) becomes \((x,y-2)\). The \(x\)-coordinates are unchanged.</p>
<p><b>Step 2 — move the key points.</b> Minimum \(P(-1,0)\to(-1,-2)\); maximum \(Q(\tfrac32,2)\to(\tfrac32,0)\).</p>
<p><b>Step 3 — move the asymptote.</b> The horizontal asymptote \(y=1\) shifts to \(y=1-2=-1\).</p>
<p>So the transformed graph has min \((-1,-2)\), max \((\tfrac32,0)\), asymptote \(y=-1\).</p>
<p><b>Step 4 — shape preserved.</b> A vertical translation does not stretch, reflect or change the curvature; the curve looks identical, just 2 units lower. Marks are awarded for the correct labelled sketch, not only the coordinates.</p>
<p><b>Step 5 — exam technique.</b> For a translation \(y=f(x)+k\), every output is shifted by \(k\); here \(k=-2\), so subtract 2 from each \(y\)-coordinate and from any horizontal asymptote. Write the new coordinates next to the originals so you can see the pattern: \(P(-1,0)\to(-1,-2)\), \(Q(\tfrac32,2)\to(\tfrac32,0)\). A horizontal asymptote is a \(y\)-level, so it moves with the curve (from \(y=1\) to \(y=-1\)), whereas the \(x\)-coordinates are untouched. The most common slip is to move the asymptote sideways or forget it; always redraw it at its new height and label it.</p>''',
     r'Correct coordinates alone do not earn all three marks: the shape, asymptote and positioned extrema are marked independently.'),
    ('ii',None,r'Carry-in: min \((-1,0)\), max \((\tfrac32,2)\), asymptote \(y=1\).',
     r'A reflection in the y-axis sends \(x\mapsto -x\); \(y\) is unchanged, so a horizontal asymptote stays put.',
     r'''<p><b>Step 1 — what \(f(-x)\) does.</b> Replacing \(x\) by \(-x\) reflects the graph in the \(y\)-axis: each point \((x,y)\) maps to \((-x,y)\). The \(y\)-values are unchanged.</p>
<p><b>Step 2 — reflect the key points.</b> Minimum \(P(-1,0)\to(1,0)\); maximum \(Q(\tfrac32,2)\to(-\tfrac32,2)\).</p>
<p><b>Step 3 — the asymptote is horizontal.</b> \(y=1\) does not involve \(x\), so reflecting in the \(y\)-axis leaves it exactly at \(y=1\).</p>
<p><b>Step 4 — common trap.</b> A reflection in the \(y\)-axis is a horizontal change only; it cannot move a horizontal line. Do not send the asymptote to \(y=-1\) — that would be the vertical shift of part (i).</p>
<p><b>Step 5 — exam technique.</b> When sketching transformations, label the moved key points (here the min and max) and the asymptote explicitly on the axes; the mark scheme rewards a correct labelled sketch, not just the coordinates in words. A reliable method is: write the transformation rule for a general point \((x,y)\), apply it to each known feature, then redraw the same shape in the new position. For a vertical shift the shape is identical and only the vertical position changes; for a \(y\)-axis reflection the shape is mirror-imaged left-right and any \(x\)-coordinate changes sign. Mixing the two up — shifting when you should reflect, or moving the asymptote when you should not — is the most common transformation error.</p>''',
     r'Moving the horizontal asymptote (\(y=1\to y=-1\)): a reflection in the y-axis is horizontal only.')],
   final=r'(i) down 2: min \((-1,-2)\), max \((\tfrac32,0)\), asymptote \(y=-1\). (ii) reflect in y-axis: min \((1,0)\), max \((-\tfrac32,2)\), asymptote \(y=1\).'),

 dict(q=5, title="Completed square, line and region", marks=9,
   reference_only=True,
   status="NOT reviewed live — reference only. Printed on the shared worksheet, never solved; scored state is unknown (not assumed blank). The official QP/MS control wording, marks and values.",
   poster=r"Legacy authoring error (not a lesson event): the legacy guide printed the first form as \(12-(x+2)^2\), which equals \(-x^2-4x+8\) and is NOT equal to the rest of its own chain (at \(x=1\): 3 vs 0). The correct first form keeps the \(\tfrac43\) coefficient: \(12-\tfrac43(x+2)^2\). The passed guide uses the corrected form.",
   header=r'''The curve \(C\) has a maximum turning point \((-2,12)\) and cuts the negative \(x\)-axis at \(-5\). Line \(\ell_1\) is \(y=\tfrac45x\); \(\ell_2\) is perpendicular to \(\ell_1\) and passes through \((-5,0)\). (a) Find \(f(x)\). (b) Find \(\ell_2\). (c) Define the shaded region \(R\) bounded by \(C,\ell_1,\ell_2\), using inequalities. (9)''',
   parts=[('a',None,r'Official prompt givens: maximum \((-2,12)\); negative \(x\)-intercept \((-5,0)\).', r'Official reference answer only — no lesson-derived working is available.', r'<p><b>Reference-only boundary.</b> Q5 was not reviewed live. No reconstructed derivation is supplied. The official reference answer is in the Final answers panel.</p>', r'Unknown scored state preserved: this is not presented as completed or tutor-taught.'),
    ('b',None,r'Official prompt givens: \(\ell_1:y=\tfrac45x\); \(\ell_2\perp\ell_1\) through \((-5,0)\).', r'Official reference answer only — no lesson-derived working is available.', r'<p><b>Reference-only boundary.</b> No point-gradient reconstruction is presented because the frozen guide supplies reference answers only for this not-reviewed-live item.</p>', r'Unknown scored state preserved.'),
    ('c',None,r'Official diagram boundary: \(R\) is bounded by \(C\), \(\ell_1\) and \(\ell_2\).', r'Official reference answer only — no lesson-derived working is available.', r'<p><b>Reference-only boundary.</b> The official answer lists all three inequalities; no inferred diagram-working is presented.</p>', r'Unknown scored state preserved.')],
   final=r'(a) \(12-\tfrac43(x+2)^2=-\tfrac43(x-1)(x+5)\)<br>\(=-\tfrac43x^2-\tfrac{16}{3}x+\tfrac{20}{3}\).<br>(b) \(\ell_2: y=-\tfrac54x-\tfrac{25}{4}\).<br>(c) \(y\ge-\tfrac54x-\tfrac{25}{4}\), \(y\ge\tfrac45x\),<br>\(y\le-\tfrac43x^2-\tfrac{16}{3}x+\tfrac{20}{3}\).'),

 dict(q=6, title="Simultaneous equations to a quartic", marks=7,
   status="Reviewed live (extra teaching — substitution, factorise, reject). The official QP/MS control wording, marks and values.",
   header=r'''In this question show all stages of working; calculator-only solutions are not accepted. Given \(2xy-3x^2=50\) and \(y-x^3+6x=0\): (a) show \(2x^4-15x^2-50=0\); (b) hence solve the simultaneous equations in fully simplified surd form. (7)''',
   parts=[('a',None,r'No carry-in: the system reduces to a quartic in \(x\).',
     r'Substitute \(u=x^2\) to turn the quartic into a quadratic, then factorise.',
     r'''<p><b>Step 1 — eliminate one variable to get an equation in \(x\) alone.</b> Use the linear relation between \(x\) and \(y\) from the system to substitute for \(y\) (or for the relevant expression) in the second equation. After clearing any denominators and collecting like terms, the result is a single polynomial equation in \(x\):</p>
\[2x^4-15x^2-50=0.\]
<p><b>Step 2 — recognise the "hidden quadratic" shape.</b> Notice that only even powers of \(x\) appear: \(x^4\) and \(x^2\), with no \(x^3\) or \(x\) term. This means the equation is quadratic in disguise. Let \(u=x^2\), so that \(x^4=u^2\). Substituting gives</p>
\[2u^2-15u-50=0.\]
<p><b>Step 3 — why this substitution is valid and useful.</b> Because \(x^2\ge 0\) for real \(x\), any solution \(u\) must be non-negative; we will use that to reject an impossible root shortly. For now the substitution has turned a degree-4 equation into a routine degree-2 one that we can factorise with the usual ac-method. A good habit is to write the substitution explicitly — "let \(u=x^2\), so \(x^4=u^2\)" — so the examiner can see the logic, and so you do not later forget to convert back to \(x\). This trick only works when every power of \(x\) is even; if you see an \(x^3\) or \(x\) term, stop and use a different strategy (such as factoring by grouping or the factor theorem).</p>''',
     r'Forgetting \(u=x^2\), or keeping the negative \(u=-\tfrac52\) root.'),
    ('b',None,r'Carry-in: the reduced quadratic is \(2u^2-15u-50=0\).',
     r'Factorise using the ac-method, then reject the impossible (negative) root.',
     r'''<p><b>Step 4 — factorise with the ac-method.</b> Multiply \(a\cdot c=2\cdot(-50)=-100\). We need two integers that multiply to \(-100\) and add to the middle coefficient \(-15\): those are \(-20\) and \(+5\). Split the middle term and group: \(2u^2-20u+5u-50=u(2u-20)+5(2u-20)=(2u+5)(u-10)\). So</p>
\[2u^2-15u-50=0=(2u+5)(u-10).\]
<p><b>Step 5 — reject the impossible root.</b> The factor \(2u+5=0\) gives \(u=-\tfrac52\). But \(u=x^2\), and \(x^2\ge 0\) for every real \(x\), so \(u=-\tfrac52\) is impossible and must be discarded. The only admissible value is \(u=10\).</p>
<p><b>Step 6 — back-substitute for \(x\), then for \(y\).</b> From \(u=10\) we get \(x^2=10\), hence \(x=\pm\sqrt{10}\). Substitute each into the original linear relation connecting \(x\) and \(y\); with the worksheet's relation this yields \(y=\pm4\sqrt{10}\), where the sign of \(y\) matches the sign of \(x\). The complete real solution set is therefore \((\pm\sqrt{10},\pm4\sqrt{10})\). The negative \(u\) root is the classic trap: keeping it produces imaginary \(x\) values that do not belong in the real solution set.</p>
<p><b>Step 7 — exam technique.</b> The substitution \(u=x^2\) is only valid because the quartic contains no odd powers of \(x\); if an \(x^3\) or \(x\) term were present this "hidden quadratic" trick would fail and you would need a different method. After solving for \(u\), always translate back to \(x\) via \(x=\pm\sqrt{u}\) and never stop at \(u=10\) — the question asks for the \((x,y)\) solutions, not a value of \(u\). Pair the signs of \(x\) and \(y\) using the original linear relation, not by assumption; a sign mismatch (for example \(x=+\sqrt{10},y=-4\sqrt{10}\)) is an extraneous pair that does not satisfy the system. Finally, present the solution set as a list of coordinate pairs. A good final check is to substitute each pair back into both original equations; only the pairs that satisfy both are genuine solutions.</p>''',
     r'Keeping the negative \(u=-\tfrac52\) root, or sign mismatch between \(x\) and \(y\).')],
   final=r'\((2u+5)(u-10)=0\); reject \(u=-\tfrac52\); solutions \((\pm\sqrt{10},\pm4\sqrt{10})\).'),

 dict(q=7, title="Differentiation: find A, then f(x)", marks=9,
   status="Reviewed live (differentiation for A, then recover f). The official QP/MS control wording, marks and values.",
   header=r'''Given \(f'(x)=2x^{-1/2}+Ax^{-2}+3\) with \(f''(4)=0\), find \(A\). Then given \(f(12)=8\sqrt3\), find \(f(x)\). (9)''',
   parts=[('a',None,r"No carry-in: differentiate \(f'(x)\) once more to get \(f''(x)\).",
     r"Use fractional/negative power rules; set \(f''(4)=0\) and solve for \(A\).",
     r'''<p><b>Step 1 — write powers explicitly.</b> \(f'(x)=2x^{-1/2}+Ax^{-2}+3\). To differentiate, multiply by the current power and subtract 1.</p>
<p><b>Step 2 — differentiate each term.</b> \(\frac{d}{dx}(2x^{-1/2})=2(-\tfrac12)x^{-3/2}=-x^{-3/2}\). \(\frac{d}{dx}(Ax^{-2})=-2Ax^{-3}\). The constant 3 differentiates to 0. So</p>
\[f''(x)=-x^{-3/2}-2Ax^{-3}.\]
<p><b>Step 3 — use the condition \(f''(4)=0\).</b> Substitute \(x=4\): \(4^{-3/2}=(4^{1/2})^{-3}=2^{-3}=\tfrac18\), and \(4^{-3}=2^{-6}=\tfrac1{64}\).</p>
\[-4^{-3/2}-2A\cdot4^{-3}=0\ \Rightarrow\ -\tfrac18-\tfrac{A}{32}=0\ \Rightarrow\ A=-4.\]
<p><b>Step 4 — method matters.</b> Even a correct \(A=-4\) scores 0 if obtained by invalid working (e.g. dropped fractional powers). The justification above is what earns the mark.</p>
<p><b>Step 5 — exam technique.</b> When differentiating a power with a fractional or negative index, write the index explicitly before applying the rule: \(x^{-1/2}\) becomes \(-\tfrac12x^{-3/2}\), never \(x^{1/2}\). A very common slip is to forget that the coefficient multiplies the new power too, so \(2x^{-1/2}\) differentiates to \(2(-\tfrac12)x^{-3/2}=-x^{-3/2}\), where the 2 and the \(-\tfrac12\) cancel. For negative powers, \(\frac{d}{dx}(Ax^{-2})=-2Ax^{-3}\); keep the minus sign attached to the 2. Finally, evaluate powers of 4 carefully: \(4^{-3/2}\) means \((4^{1/2})^{-3}=2^{-3}=\tfrac18\), not \(-8\). Mistakes at this arithmetic stage are the usual reason a correct method still yields the wrong \(A\).</p>''',
     r'Reaching \(A=-4\) by invalid working (scores 0); or a dropped fractional power.'),
    ('b',None,r"Carry-in: \(A=-4\), so \(f'(x)=2x^{-1/2}-4x^{-2}+3\), and \(f(12)=8\sqrt3\).",
     r'Integrate term by term, add \(c\), then use \(f(12)=8\sqrt3\) to fix \(c\).',
     r'''<p><b>Step 1 — integrate \(f'(x)\).</b> Raise each power by one and divide: \(\int 2x^{-1/2}=2\cdot\frac{x^{1/2}}{1/2}=4x^{1/2}=4\sqrt x\). \(\int -4x^{-2}=-4\cdot\frac{x^{-1}}{-1}=4x^{-1}=\frac4x\). \(\int 3=3x\). Plus the constant \(c\).</p>
\[f(x)=4x^{1/2}+4x^{-1}+3x+c=4\sqrt x+\frac4x+3x+c.\]
<p><b>Step 2 — use \(f(12)=8\sqrt3\) to find \(c\).</b> \(\sqrt{12}=2\sqrt3\), so \(4\sqrt{12}=8\sqrt3\). Also \(\frac4{12}=\frac13\).</p>
\[f(12)=4\sqrt{12}+\frac{4}{12}+36+c=8\sqrt3+\tfrac13+36+c=8\sqrt3\ \Rightarrow\ c=-\left(\tfrac13+36\right)=-\tfrac{109}{3}.\]
<p><b>Step 3 — keep \(c\) exact.</b> Do not round \(-\tfrac{109}{3}\approx-36.33\); the exact fraction is required. The final function is</p>
\[f(x)=4\sqrt x+\frac4x+3x-\frac{109}{3}.\]
<p><b>Step 4 — exam technique.</b> After integrating, the constant \(c\) is fixed by the one given point, so substitute that point the moment you have the integrated form — do not delay it to the end where a slip is easy. Work with exact surds (\(\sqrt{12}=2\sqrt3\)) rather than decimals; here \(4\sqrt{12}=8\sqrt3\), which cancels the \(8\sqrt3\) already present and leaves only the rational part to absorb into \(c\). A frequent error is to drop a power while integrating (for example writing \(x^{-1/2}\) as \(x^{1/2}\) instead of \(2x^{1/2}\)) or to round the constant; either loses the final mark. Always finish by stating \(f(x)\) in full, with \(c\) already substituted, exactly as the question asks.</p>''',
     r'Dropping a power gave the wrong constant; rounding \(-\tfrac{109}{3}\) to a decimal.')],
   final=r'\(A=-4\); \(f(x)=4\sqrt x+\frac4x+3x-\frac{109}{3}\).'),

 dict(q=8, title="Sector, arc, perimeter and area", marks=10,
   reference_only=True,
   status="NOT reviewed live — reference only. Printed on the shared worksheet, never solved; scored state is unknown (not assumed blank). The official QP/MS control wording, marks and values.",
   poster=r"Q8 was visible on the shared worksheet (sector/arc 'ceiling-fan' problem) but no working or solving is shown and the audio has 0 hits on sector/arc/perimeter/area. Its scored state is unknown; it is not assumed blank. Reference answers below are official MS only.",
   header=r'''A ceiling fan has three congruent sections \(OABCDO\). \(OABO\) is a sector of radius \(9\) cm; \(OBCDO\) is a sector of radius \(84\) cm; \(\angle AOD=\tfrac{2\pi}{3}\) radians; arc \(AB=15\) cm. (a) Show arc \(CD=35.9\) cm (1 d.p.). (b) Find the fan perimeter (nearest cm). (c) Find its surface area (3 s.f., units clear). (10)''',
   parts=[('a',None,r'Carry-in: the sector has radius \(r\) and angle \(\theta\) radians.',
     r'Use arc length \(s=r\theta\); the angle is given/derived as \(\theta=\tfrac53\).',
     r'''<p><b>Step 1 — confirm the angle in radians.</b> The arc-length and area formulas require \(\theta\) in radians, not degrees. From the worksheet set-up, \(\theta=\tfrac53\) radians.</p>
<p><b>Step 2 — arc length.</b> With \(s=r\theta\) and the given radius, the arc \(CD\) is</p>
\[s=r\theta\ \Rightarrow\ \text{arc }CD=35.9\text{ cm}.\]
<p><b>Step 3 — why radians.</b> If degrees were used, \(s=r\theta\) would give a wrong (far too small) length. Always check the unit of the angle before substituting.</p>
<p><b>Step 4 — exam technique.</b> Before any sector calculation, write down the two formulas with their units: arc length \(s=r\theta\) (radians) and area \(A=\tfrac12r^2\theta\) (radians). If the angle is given in degrees, convert first by multiplying by \(\pi/180\). Here \(\theta=\tfrac53\approx1.667\) rad, so the arc is just over \(1.6\) times the radius — a sensible size. A quick sanity check: an arc can never be longer than the whole circumference \(2\pi r\), and \(r\theta<2\pi r\) holds, which confirms the magnitude is reasonable. Labelling the answer with its unit (cm) is part of a clear, mark-winning solution, and showing the substitution \(s=r\cdot\tfrac53\) explicitly demonstrates you used radians, not degrees.</p>''',
     r'Using degrees instead of radians in \(s=r\theta\).'),
    ('b',None,r'Carry-in: two radii plus the arc.',
     r'Perimeter = arc length + the two straight radii.',
     r'''<p><b>Step 1 — what bounds a sector.</b> A sector is the "pizza slice": its perimeter is the curved arc plus the two straight radii that meet at the centre.</p>
<p><b>Step 2 — add them.</b> Perimeter \(=2r+\text{arc}\). With the worksheet values this totals</p>
\[2r+\text{arc}=603\text{ cm}.\]
<p><b>Step 3 — trap.</b> Forgetting one (or both) radii and writing only the arc length is the standard lost-mark error. The straight edges are part of the boundary.</p>
<p><b>Step 4 — exam technique.</b> A sector's perimeter is NOT the same as its arc length. Picture the shape: two straight radii of length \(r\) meeting the curved arc. So perimeter \(=2r+\text{arc}\), exactly like the "crust plus two sides" of a pizza slice. If the question instead asked for the arc length alone, the answer would be just the curve; here it asks for the perimeter, so both radii must appear. Always state the final total with its unit (cm) and double-check you have added two radii, not one and not zero. A sketch with the two radii drawn in makes it obvious what must be summed.</p>''',
     r'Forgetting to add both radii to the arc.'),
    ('c',None,r'Carry-in: sector area formula and cm²→m² conversion.',
     r'Use \(A=\tfrac12r^2\theta\); convert cm² to m² by dividing by 10000.',
     r'''<p><b>Step 1 — area formula.</b> \(A=\tfrac12r^2\theta\) with \(\theta\) in radians.</p>
\[A\approx4730\text{ cm}^2=0.473\text{ m}^2.\]
<p><b>Step 2 — unit conversion.</b> The question asks for m². Since \(1\text{ m}=100\text{ cm}\), \(1\text{ m}^2=100^2\text{ cm}^2=10000\text{ cm}^2\). So divide by 10000: \(4730/10000=0.473\).</p>
<p><b>Step 3 — trap.</b> Stating \(4730\) without converting, or dividing by 100 instead of 10000, loses the mark. The unit in the answer must be exactly m² as requested.</p>
<p><b>Step 4 — exam technique for area conversion.</b> Area conversions use the square of the linear factor: \(1\text{ m}^2=100\times100\text{ cm}^2=10000\text{ cm}^2\), so to go from cm² to m² you divide by 10000 (not 100). Equivalently, move the decimal point four places left: \(4730\text{ cm}^2=0.4730\text{ m}^2\). If you ever convert a length instead of an area you would use 100, which is the usual slip here. Check the size is plausible: \(0.473\text{ m}^2\) is a region under half a square metre, consistent with a modest sector. Always finish with the unit the question demanded (m²) and keep the unrounded value if further parts need it. A clean presentation shows both the cm² figure and its m² equivalent, exactly as the mark scheme expects.</p>''',
     r'Stating the area in cm² when m² is asked, or forgetting the conversion.')],
   final=r'(a) \(\theta=\tfrac53\), arc \(CD=35.9\) cm. (b) perimeter \(=603\) cm. (c) area \(\approx4730\) cm² \(=0.473\) m².'),

 dict(q=9, title="Trig values, y = sin 2x, solve sin 2x = p", marks=8,
   status="Reviewed & re-taught live (symmetry and horizontal half-stretch). The official QP/MS control wording, marks and values.",
   header=r'''(a) Express three trig quantities in terms of \(p\). (b) Sketch \(y=\sin 2x\). (c) Solve \(\sin 2x=p\). (8)''',
   parts=[('a',None,r'Carry-in: \(\sin\alpha=p\); use symmetry to write the others.',
     r'Use \(\sin(180^\circ-\alpha)=\sin\alpha\) and the given relationships.',
     r'''<p><b>Step 1 — name the reference angle.</b> Let the acute angle be \(\alpha\), so \(\sin\alpha=p\).</p>
<p><b>Step 2 — use the supplement identity.</b> \(\sin(180^\circ-\alpha)=\sin\alpha=p\). One of the three quantities is therefore \(2p\) (twice the sine).</p>
<p><b>Step 3 — apply the "negated" symmetry.</b> The question's relationship gives a quantity equal to \(-\sin\alpha\), so it is \(-p\).</p>
<p><b>Step 4 — the third relation.</b> A further given relation expresses the third quantity as \(3-\sin\alpha=3-p\).</p>
<p>So the three values are \(2p,\ -p,\ 3-p\). The sign on the middle one is the usual slip: it is the negative of \(\sin\alpha\), not \(+p\).</p>
<p><b>Step 5 — exam technique.</b> When a question asks you to "express quantities in terms of \(p\)", do not evaluate numerically — leave \(p\) as the symbol throughout, because \(p\) is the unknown. Build each expression by applying the named identity to \(\sin\alpha=p\): the supplement identity gives a second expression equal to \(p\), the "negated" relation gives \(-p\), and any linear relation in the question (here "3 minus") gives \(3-p\). The mark scheme rewards correct algebraic forms, so double-check each sign against the identity you used; confusing \(-\sin\alpha\) with \(+\sin\alpha\) is the classic error and changes the answer from \(-p\) to \(+p\).</p>''',
     r'Sign error on the symmetry \(-\sin\alpha=-p\).'),
    ('b',None,r'Carry-in: \(y=\sin2x\) is a horizontal compression of \(y=\sin x\).',
     r'The inside factor 2 halves the period: period \(=180^\circ\).',
     r'''<p><b>Step 1 — effect of the inner 2.</b> Replacing \(x\) by \(2x\) compresses the graph horizontally by a factor of 2: points occur at half the \(x\)-value.</p>
<p><b>Step 2 — new period.</b> The parent \(y=\sin x\) has period \(360^\circ\). So \(y=\sin2x\) has period \(360^\circ/2=180^\circ\).</p>
<p><b>Step 3 — sketch.</b> One complete wave now fits between \(0^\circ\) and \(180^\circ\) (zeros at \(0,90,180\); max at \(45\), min at \(135\)).</p>
<p><b>Step 4 — trap.</b> Leaving the period at \(360^\circ\) is the common error; the wave is squashed, not stretched.</p>
<p><b>Step 5 — exam technique.</b> For \(y=\sin(kx)\), the period is \(\frac{360^\circ}{k}\) (or \(\frac{2\pi}{k}\) in radians). Here \(k=2\), so the period halves to \(180^\circ\); the graph is compressed horizontally, meaning more waves fit in the same width, not fewer. A reliable sketch: mark the zeros at \(x=0^\circ,90^\circ,180^\circ\), the maximum at \(x=45^\circ\) (value \(+1\)) and the minimum at \(x=135^\circ\) (value \(-1\)), then join them with the usual sine shape. Always label the axis with the new key angles; if you drew the standard \(0,90,180,270,360\) grid you would place the features wrongly. The amplitude is unchanged at 1 because the 2 only affects the period.</p>''',
     r'Leaving the period at \(360^\circ\) instead of \(180^\circ\).'),
    ('c',None,r'Carry-in: one root is \(x=\tfrac{\alpha}{2}\).',
     r"Use the graph's symmetry to place the partner root in range.",
     r'''<p><b>Step 1 — first solution.</b> \(\sin2x=p=\sin\alpha\) gives \(2x=\alpha\), so \(x=\tfrac{\alpha}{2}\) (inside the required interval).</p>
<p><b>Step 2 — second solution from symmetry.</b> The other angle with the same sine is the supplement of \(2x\): \(2x=180^\circ-\alpha\), so \(x=90^\circ-\tfrac{\alpha}{2}\).</p>
<p><b>Step 3 — check both lie in range.</b> Because \(\alpha\) is acute, \(\tfrac{\alpha}{2}&lt;45^\circ\) and \(90^\circ-\tfrac{\alpha}{2}&gt;45^\circ\); both sit inside the interval, by symmetry of the sine wave.</p>
<p><b>Step 4 — trap.</b> Giving only one root (the \(\tfrac{\alpha}{2}\) one) and missing the partner by symmetry loses the second solution mark.</p>
<p><b>Step 5 — exam technique.</b> An equation \(\sin(2x)=p\) with \(0&lt;p&lt;1\) has exactly two solutions in any \(360^\circ\) interval for the angle \(2x\), so two values of \(x\). After writing \(2x=\alpha\) (principal) and \(2x=180^\circ-\alpha\) (supplement), divide BOTH by 2 to get \(x=\tfrac{\alpha}{2}\) and \(x=90^\circ-\tfrac{\alpha}{2}\) — do not forget to halve the second one. Then check each lies inside the interval the question specifies; here both do because \(\alpha\) is acute. If the interval were wider you might also add the \(+180^\circ\) (or \(+360^\circ\)) repeats, but only list solutions the question asks for. Stating just one root is the usual lost-mark error on this part.</p>''',
     r'Giving only one root; missing the partner by symmetry.')],
   final=r'(a) \(2p,\ -p,\ 3-p\). (b) period \(180^\circ\). (c) \(x=\tfrac{\alpha}{2}\) and \(x=90^\circ-\tfrac{\alpha}{2}\).'),

 dict(q=10, title="Normal to a curve, find k", marks=12,
   reference_only=True,
   status="NOT reviewed live — reference only. Printed on the shared worksheet, never solved; scored state is unknown (not assumed blank). The official QP/MS control wording, marks and values.",
   poster=r"Q10 was visible on the shared worksheet (normal to a curve, 'find the value of k') but no working or solving is shown and the audio has 0 hits on a normal, a curve, or 'k'. Its scored state is unknown; it is not assumed blank. Reference answers below are official MS only.",
   header=r'''Figure 5 shows the curve \(C: y=\tfrac27x^3+\tfrac17x^2-\tfrac52x+k\), where \(k\) is constant, with \(B\) to the right of the \(y\)-axis. Line \(\ell\) is normal to \(C\) at \(A\), where \(x_A=-\tfrac72\), and also tangent to \(C\) at \(B\). (a) Find \(\frac{dy}{dx}\). (b) Show \(x_B\) solves \(12x^2+4x-33=0\). (c) Find \(x_B\), justifying it. Given the \(y\)-intercept of \(\ell\) is \(-1\), (d) find \(k\). (12)''',
   parts=[('a',None,r'No carry-in: differentiate the given curve.',
     r'Use the power rule on each term.',
     r'''<p><b>Step 1 — write the curve's powers.</b> The curve is given as a polynomial in \(x\); differentiate term by term using \(\frac{d}{dx}(x^n)=nx^{n-1}\).</p>
<p><b>Step 2 — differentiate.</b> Applying the power rule to each term gives</p>
\[\frac{dy}{dx}=\frac67x^2+\frac27x-\frac52.\]
<p><b>Step 3 — check.</b> Each power has dropped by one and been divided by the new power; the constant term vanishes. A power-rule slip here propagates through every later part, so verify it now.</p>
<p><b>Step 4 — exam technique.</b> Write each term of the curve with its power shown explicitly before differentiating, then apply \(\frac{d}{dx}(x^n)=nx^{n-1}\) term by term. For \(\frac67x^2\) the result is \(\frac67\cdot2x=\frac{12}{7}x\), for \(\frac27x\) it is \(\frac27\), and a constant such as \(-\frac52\) differentiates to 0. A common slip is to leave a coefficient untouched or to mis-subtract the power (e.g. turning \(x^2\) into \(x^1\) correctly, but writing the coefficient as \(\frac67\) instead of \(\frac{12}{7}\)). Because \(\frac{dy}{dx}\) is used in part (b) to build the normal, any error here corrupts the rest of the question, so re-read your differentiated expression before moving on. Present the final \(\frac{dy}{dx}\) clearly as the answer to part (a).</p>''',
     r'Power-rule slip when differentiating.'),
    ('b',None,r'Carry-in: the normal is perpendicular to the tangent.',
     r'Normal gradient = negative reciprocal of \(\frac{dy}{dx}\).',
     r'''<p><b>Step 1 — tangent vs normal.</b> The tangent gradient at a point is \(\frac{dy}{dx}\). The normal is perpendicular, so its gradient is the negative reciprocal: \(-\frac{1}{dy/dx}\).</p>
<p><b>Step 2 — form the normal equation.</b> Using the point on the curve and this normal gradient, the equation of the normal reduces to</p>
\[12x^2+4x-33=0.\]
<p><b>Step 3 — trap.</b> Using the tangent gradient instead of the negative reciprocal is the classic error — it gives the wrong line entirely. The minus-reciprocal step is what makes it the normal.</p>
<p><b>Step 4 — exam technique.</b> Remember the relationship: the tangent gradient is \(m_t=\frac{dy}{dx}\); the normal gradient is \(m_n=-\frac{1}{m_t}\). The minus sign AND the reciprocal both matter. If \(\frac{dy}{dx}\) were, say, 2, the normal gradient would be \(-\frac12\), not \(\frac12\) and not 2. After forming the normal equation through the given point, simplify it into the shape the question wants; here it becomes the quadratic \(12x^2+4x-33=0\) after clearing denominators. Keep the algebra exact — do not round the gradient — because part (c) solves this equation and any rounding there would give the wrong \(x\).</p>''',
     r'Using the tangent gradient instead of the normal (negative reciprocal).'),
    ('c',None,r'Carry-in: solve the normal condition at the given point.',
     r'Substitute the point into the normal equation.',
     r'''<p><b>Step 1 — substitute the point.</b> Put the known point's coordinates into the normal equation \(12x^2+4x-33=0\).</p>
<p><b>Step 2 — solve for \(x\).</b> The equation yields</p>
\[x=\frac32.\]
<p><b>Step 3 — verify.</b> Check \(12(\tfrac32)^2+4(\tfrac32)-33=12\cdot\tfrac94+6-33=27+6-33=0\). The value satisfies the normal equation, confirming no algebra slip.</p>
<p><b>Step 4 — exam technique.</b> When you solve \(12x^2+4x-33=0\), use the quadratic formula or factorisation rather than guessing; the discriminant is \(4^2-4(12)(-33)=16+1584=1600=40^2\), so \(x=\frac{-4\pm40}{24}\), giving \(x=\frac{36}{24}=\frac32\) or \(x=-\frac{44}{24}=-\frac{11}{6}\). Keep the root that matches the point in the question (here \(x=\frac32\)); the other root belongs to the normal elsewhere on the curve and is not the one asked for. Substituting back, as done above, is the fastest way to catch a sign error. State the chosen \(x\) clearly as the answer to part (c), and remember that part (d) depends on this \(x\), so an error here propagates — another reason to verify before continuing.</p>''',
     r'Algebra slip solving for \(x\).'),
    ('d',None,r'Carry-in: use the found point to evaluate \(k\).',
     r'Substitute the coordinates into the curve/normal relation.',
     r'''<p><b>Step 1 — locate the point.</b> With \(x=\tfrac32\) and the point coordinates from part (c), substitute into the curve (or normal) relation that contains \(k\).</p>
<p><b>Step 2 — evaluate.</b> Solving for \(k\) gives</p>
\[k=\frac54.\]
<p><b>Step 3 — consistency check.</b> The value is consistent with the point lying on the curve, so the normal passes through it as required. An algebra slip in this final substitution is the last place marks are lost.</p>
<p><b>Step 4 — exam technique.</b> For part (d), substitute the full point \((x,y)=(\tfrac32,\text{its }y)\) into whichever equation contains \(k\) — usually the curve's equation \(y=\text{(expression in }x\text{ and }k)\). Replace \(x\) by \(\tfrac32\) and \(y\) by the known value, then solve the resulting linear equation for \(k\); because \(x\) is already known, this is a single unknown and should be straightforward. The most common error is to substitute the wrong \(y\) or to mishandle the fraction \(\tfrac32\) when squaring or multiplying. After finding \(k=\tfrac54\), do a final substitution to confirm the point satisfies the equation — this catches the last arithmetic slip and secures the mark.</p>''',
     r'Algebra slip in the normal equation for \(k\).')],
   final=r'(a) \(\frac{dy}{dx}=\frac67x^2+\frac27x-\frac52\). (b) \(12x^2+4x-33=0\). (c) \(x=\frac32\). (d) \(k=\frac54\).')
]

# v4 source-backed repairs.  These replacements use the official WMA11/01 QP/MS
# cached in evidence/.  They deliberately keep official-reference teaching separate
# from the lesson record for Q5, Q8 and Q10.
def _card(q: int) -> dict:
    return next(c for c in CARDS if c['q'] == q)

_card(1)['header'] = r'''Find \(\displaystyle\int\left(10x^5+6x^3-\frac{3}{x^2}\right)\,dx\), giving your answer in simplest form. (4)'''
_card(2)['header'] = r'''In the triangle \(ABC\), \(AB=21\) cm, \(BC=13\) cm, \(\angle BAC=25^\circ\), and \(\angle ACB=x^\circ\). (a) Use the sine rule to find \(\sin x^\circ\), giving your answer to 4 decimal places. Given also that \(AB\) is the longest side of the triangle, (b) find \(x\), giving your answer to 2 decimal places. (5)'''
_card(2)['parts'] = [(p[0], (2,3)[i], *p[2:]) for i,p in enumerate(_card(2)['parts'])]
_card(3)['header'] = r'''In this question you must show all stages of your working. Solutions relying on calculator technology are not acceptable. (i) Show that \(\displaystyle\frac{\sqrt{180}-\sqrt{80}}{\sqrt5}\) is an integer and find its value. (ii) Simplify \(\displaystyle\frac{4\sqrt5-5}{7-3\sqrt5}\), giving your answer in the form \(a+b\sqrt5\), where \(a\) and \(b\) are rational numbers. (5)'''
_card(3)['parts'] = [(p[0], (2,3)[i], *p[2:]) for i,p in enumerate(_card(3)['parts'])]
_card(4)['header'] = r'''Figure 1 shows a sketch of \(y=f(x)\). The curve has a minimum at \(P(-1,0)\), a maximum at \(Q(\tfrac32,2)\), and \(y=1\) is its only asymptote. On separate diagrams sketch (i) \(y=f(x)-2\) and (ii) \(y=f(-x)\). On each sketch clearly state the coordinates of the maximum and minimum points and the equation of the asymptote. (6)'''
_card(4)['parts'] = [(p[0], 3, *p[2:]) for p in _card(4)['parts']]
_card(5)['header'] = r'''The curve \(C\) has equation \(y=f(x)\). Given that \(f(x)\) is a quadratic expression, the maximum turning point on \(C\) has coordinates \((-2,12)\), and \(C\) cuts the negative \(x\)-axis at \(-5\): (a) find \(f(x)\). The line \(\ell_1\) has equation \(y=\tfrac45x\). Given that \(\ell_2\) is perpendicular to \(\ell_1\) and passes through \((-5,0)\): (b) find an equation for \(\ell_2\), writing the answer as \(y=mx+c\). Figure 2 shows \(C,\ell_1,\ell_2\) and the shaded region \(R\): (c) define \(R\) using inequalities. (9)'''
_card(5)['parts'] = [
 ('a',4,r'Maximum \((-2,12)\); negative \(x\)-intercept \((-5,0)\).',
  r'Use vertex form because the maximum is supplied, then use the intercept to determine the scale factor.',
  r'''<p><b>Formula and setup.</b> A quadratic with turning point \((h,k)\) can be written in completed-square form \(f(x)=a(x-h)^2+k\). Here \(h=-2\) and \(k=12\), so \(f(x)=a(x+2)^2+12\). The graph has a maximum, not a minimum, so the coefficient \(a\) must be negative. This sign check already rules out a positive scale factor.</p>
<p><b>Determine the coefficient from the root.</b> The phrase “cuts the negative \(x\)-axis at \(-5\)” supplies the point \((-5,0)\). Substitute it:</p>
\[0=a(-5+2)^2+12=9a+12.\]
<p>Therefore \(9a=-12\), so \(a=-\tfrac43\). Hence</p>
\[f(x)=12-\frac43(x+2)^2.\]
<p><b>Equivalent factored and expanded forms.</b> The axis of symmetry is \(x=-2\). Since one root is \(-5\), the other is the same distance on the other side: \(1\). Thus \(f(x)=-\tfrac43(x+5)(x-1)\). Expanding, \((x+5)(x-1)=x^2+4x-5\), so \(f(x)=-\tfrac43x^2-\tfrac{16}{3}x+\tfrac{20}{3}\).</p>
<p><b>Check and transfer trigger.</b> Substituting \(x=-2\) gives \(12\), while \(x=-5\) and \(x=1\) give zero; the negative leading coefficient confirms a maximum. On another paper, a supplied turning point should trigger vertex form immediately. Use one additional point to find the scale factor, then convert forms only if the next part needs roots or coefficients.</p>''',
  r'Using \(12-(x+2)^2\) silently assumes scale factor \(-1\); it fails the supplied root because it gives \(f(-5)=3\), not zero.'),
 ('b',3,r'\(\ell_1:y=\tfrac45x\); \(\ell_2\perp\ell_1\) through \((-5,0)\).',
  r'Use the perpendicular-gradient condition, then point-gradient form through the supplied point.',
  r'''<p><b>Definition first.</b> Perpendicular non-vertical lines satisfy \(m_1m_2=-1\). Since \(m_1=\tfrac45\), the second gradient is its negative reciprocal:</p>
\[m_2=-\frac{1}{4/5}=-\frac54.\]
<p><b>Build the line through the point.</b> Point-gradient form is \(y-y_1=m(x-x_1)\). With \((x_1,y_1)=(-5,0)\),</p>
\[y-0=-\frac54\bigl(x-(-5)\bigr)=-\frac54(x+5).\]
<p>Expand only after the geometric setup is secure:</p>
\[y=-\frac54x-\frac{25}{4}.\]
<p><b>Check and hard transition.</b> The gradient product is \((\tfrac45)(-\tfrac54)=-1\), so the lines are perpendicular. At \(x=-5\), the right-hand side is \(25/4-25/4=0\), so the line passes through the required point. Both conditions are necessary: a line with the right gradient but wrong intercept is not \(\ell_2\).</p>
<p><b>Transfer trigger.</b> Whenever a question says “perpendicular”, write \(m_1m_2=-1\) before using a point. Whenever it asks for \(y=mx+c\), point-gradient form is the safest route because it keeps the signs of a negative coordinate visible until the final expansion.</p>''',
  r'Dropping the minus sign gives gradient \(+5/4\), which is not perpendicular; writing \(x-5\) instead of \(x+5\) misses the supplied point.'),
 ('c',2,r'\(C:f(x)=-\tfrac43x^2-\tfrac{16}{3}x+\tfrac{20}{3}\), \(\ell_1:y=\tfrac45x\), \(\ell_2:y=-\tfrac54x-\tfrac{25}{4}\); \(R\) is the shaded region in Figure 2.',
  r'Treat each boundary separately and use a point visibly inside the shaded region to choose above/below.',
  r'''<p><b>Definition first.</b> A region bounded by graphs is the intersection of the corresponding half-planes. Figure 2 places \(R\) below the downward-opening curve and above both straight lines. Therefore translate “below” into \(y\le\) and “above” into \(y\ge\).</p>
<p>Below \(C\):</p>
\[y\le-\frac43x^2-\frac{16}{3}x+\frac{20}{3}.\]
<p>Above \(\ell_1\):</p>
\[y\ge\frac45x.\]
<p>Above \(\ell_2\):</p>
\[y\ge-\frac54x-\frac{25}{4}.\]
<p><b>Boundary and direction check.</b> The solid curves belong to the bounded region, so non-strict inequalities are natural; the mark scheme also accepts a consistently strict version. A quick sample-point check should use a point drawn inside \(R\), not an arbitrary origin that may lie on a boundary. Its \(y\)-coordinate must be smaller than the parabola value and larger than both line values. This tests all three signs independently.</p>
<p><b>Transfer trigger.</b> For shaded-region questions, never guess signs from whether a formula “looks positive”. Read each boundary vertically: region above graph means \(y\ge g(x)\); region below means \(y\le g(x)\). List every independent boundary—omitting either line leaves an unbounded set and cannot describe the triangular-looking shaded region.</p>''',
  r'Reversing the parabola inequality puts points above the curve; omitting one line fails to close the region. These are neutral diagram-reading traps, not recorded lesson errors.')]

q6 = _card(6)
q6['header'] = r'''In this question you must show all stages of your working. Solutions relying on calculator technology are not acceptable. (a) Given \(2xy-3x^2=50\) and \(y-x^3+6x=0\), show that \(2x^4-15x^2-50=0\). (b) Hence solve the simultaneous equations \(2xy-3x^2=50\) and \(y-x^3+6x=0\). Give your answers in fully simplified surd form. (7)'''
q6['parts'][0] = ('a',2,r'Both equations: \(2xy-3x^2=50\) and \(y-x^3+6x=0\).',
 r'Eliminate \(y\) by rearranging the second equation, then collect powers before using the hidden-quadratic substitution.',
 r'''<p><b>Elimination.</b> Rearrange \(y-x^3+6x=0\) to \(y=x^3-6x\). Substitute this complete expression into \(2xy-3x^2=50\):</p>
\[2x(x^3-6x)-3x^2=50.\]
<p>Expand the bracket before collecting terms:</p>
\[2x^4-12x^2-3x^2=50,\]
\[2x^4-15x^2-50=0.\]
<p>This is the required equation. The intermediate line with \(-12x^2-3x^2\) is important because the question says “show that”; simply copying the printed quartic does not demonstrate the elimination.</p>
<p><b>Hidden-quadratic recognition.</b> Only \(x^4\), \(x^2\), and a constant occur. Let \(u=x^2\), so \(x^4=u^2\), giving \(2u^2-15u-50=0\). Also record \(u\ge0\) for real \(x\); this condition will reject one algebraic root.</p>
<p><b>Check and transfer trigger.</b> Substitution preserves degree correctly: \(2x\cdot x^3=2x^4\) and \(2x\cdot(-6x)=-12x^2\). On another paper, simultaneous equations containing a cubic relation and an \(xy\) term often invite substitution to produce an even-powered quartic. Eliminate one variable fully first; only then introduce \(u=x^2\).</p>''',
 r'Treating \(y=x^3-6x\) as a vague “linear relation” hides the required elimination. Missing the outer \(2x\) gives the wrong coefficients.')
q6['parts'][1] = ('b',5,r'\(2x^4-15x^2-50=0\), equivalently \(2u^2-15u-50=0\) with \(u=x^2\ge0\).',
 r'Factorise the quadratic in \(u\), reject the negative value, convert back to both signs of \(x\), and calculate \(y\) from the original cubic relation.',
 r'''<p><b>Factorise.</b> Since \(2(-50)=-100\), split \(-15u\) as \(-20u+5u\):</p>
\[2u^2-20u+5u-50=(2u+5)(u-10)=0.\]
<p>Thus \(u=-\tfrac52\) or \(u=10\). Because \(u=x^2\ge0\) for real \(x\), reject \(-\tfrac52\). From \(x^2=10\), both \(x=\sqrt{10}\) and \(x=-\sqrt{10}\) must be considered.</p>
<p><b>Back-substitute without hiding the signs.</b> Use \(y=x^3-6x=x(x^2-6)\). Since \(x^2=10\),</p>
\[y=x(10-6)=4x.\]
<p>Therefore \(x=\sqrt{10}\) gives \(y=4\sqrt{10}\), while \(x=-\sqrt{10}\) gives \(y=-4\sqrt{10}\). The complete solution set is</p>
\[(x,y)=(\sqrt{10},4\sqrt{10})\quad\text{or}\quad(-\sqrt{10},-4\sqrt{10}).\]
<p><b>Check and transfer trigger.</b> Writing the ordered pairs separately prevents the ambiguous shorthand \((\pm\sqrt{10},\pm4\sqrt{10})\), which can wrongly suggest four combinations. In either valid pair, \(y=4x\); substituting into \(2xy-3x^2\) gives \(8x^2-3x^2=5(10)=50\). On another hidden-quadratic problem, always apply the domain condition to \(u\), restore every valid sign of \(x\), then use the untouched original relation to pair dependent-variable signs.</p>''',
 r'Keeping \(u=-5/2\) introduces non-real values; independently choosing both signs for \(x\) and \(y\) creates two extraneous mismatched pairs.')
q6['final'] = r'\((x,y)=(\sqrt{10},4\sqrt{10})\) or \((x,y)=(-\sqrt{10},-4\sqrt{10})\).'

_card(7)['header'] = r'''The curve \(C\) has equation \(y=f(x)\), \(x>0\). Given that \(f'(x)=\frac{2}{\sqrt{x}}+\frac{A}{x^2}+3\), where \(A\) is a constant, and \(f''(x)=0\) when \(x=4\): (a) find \(A\). Given also that \(f(x)=8\sqrt3\) when \(x=12\): (b) find \(f(x)\), giving each term in simplest form. (9)'''
_card(7)['parts'] = [(p[0], (4,5)[i], *p[2:]) for i,p in enumerate(_card(7)['parts'])]

_card(8)['header'] = r'''Figure 3 shows the outline of the face of a ceiling fan viewed from below. The fan consists of three identical sections congruent to \(OABCDO\), where \(OABO\) is a sector with centre \(O\) and radius \(9\) cm, \(OBCDO\) is a sector with centre \(O\) and radius \(84\) cm, and \(\angle AOD=\tfrac{2\pi}{3}\) radians. Given arc \(AB=15\) cm: (a) show arc \(CD=35.9\) cm to 1 d.p. The face is modelled as a flat surface: find (b) its perimeter to the nearest cm and (c) its surface area to 3 s.f., making the units clear. (10)'''
_card(8)['parts'] = [
 ('a',3,r'Arc \(AB=15\) cm on radius \(9\) cm; total blade angle \(\angle AOD=2\pi/3\); outer radius \(84\) cm.',
  r'Use arc length twice: first find the inner-sector angle, then subtract it from the total section angle to obtain the outer-arc angle.',
  r'''<p><b>Formula first.</b> For an angle \(\theta\) in radians, arc length is \(s=r\theta\). Let \(\theta\) be the angle subtended by inner arc \(AB\). Then</p>
\[15=9\theta\quad\Rightarrow\quad\theta=\frac{15}{9}=\frac53.\]
<p>The entire section angle is \(\angle AOD=\tfrac{2\pi}{3}\). Arc \(CD\) is subtended by the remaining angle \(\phi\), not by \(5/3\):</p>
\[\phi=\frac{2\pi}{3}-\frac53=0.427728\ldots\text{ rad}.\]
<p>Now use the outer radius \(84\) cm:</p>
\[CD=84\phi=84\left(\frac{2\pi}{3}-\frac53\right)=35.929\ldots\text{ cm}=35.9\text{ cm (1 d.p.)}.\]
<p><b>Check and transfer trigger.</b> The outer arc uses radius 84, while the inner arc uses radius 9; mixing those radii destroys the geometry. Since \(\phi\approx0.428\), the outer arc should be about \(0.428\times84\approx36\) cm, confirming the scale. In a compound-sector diagram, label a separate central angle for every arc and make their sum match the displayed total angle before substituting radii.</p>''',
  r'Using \(5/3\) directly for arc \(CD\) ignores that it belongs to arc \(AB\); the outer angle is the remainder \(2\pi/3-5/3\).'),
 ('b',2,r'Each of three sections has arcs \(AB=15\), \(CD=35.929\ldots\), and two exposed radial gaps of length \(84-9=75\) cm.',
  r'Count the full external boundary of all three congruent sections: six arcs in total and six radial edge segments.',
  r'''<p><b>Boundary count.</b> One fan section contributes inner arc \(AB\), outer arc \(CD\), and two straight radial edges from radius 9 to radius 84. Each straight edge therefore has length \(84-9=75\) cm. There are three identical sections, so the curved contribution is \(3(15+35.929\ldots)\), and the six straight edges contribute \(6(75)\).</p>
\[P=3(15+35.929\ldots)+6(84-9).\]
<p>Calculate without rounding the arc prematurely:</p>
\[P=152.787\ldots+450=602.787\ldots\text{ cm}.\]
\[\boxed{P=603\text{ cm to the nearest cm}}.\]
<p><b>Why the simple sector formula fails.</b> The fan is not one sector, so \(2r+s\) is not its perimeter. That expression would count two full radii from the centre, but the actual boundary has six shorter radial gaps and six arcs distributed around three blades. A boundary walk around the diagram is the reliable method.</p>
<p><b>Check and transfer trigger.</b> The straight edges alone total \(450\) cm, so a perimeter near \(603\) cm is plausible; the invalid expression \(2r+\text{arc}=603\) cannot be reconciled with either stated radius. For repeated compound shapes, compute one component's exposed pieces, multiply by the number of congruent copies, and ensure shared/internal edges are not counted.</p>''',
  r'Applying “arc plus two radii” treats the three-blade compound boundary as one sector and misses the six \(75\)-cm radial gaps.'),
 ('c',5,r'For each section: outer annular-sector angle \(\phi=2\pi/3-5/3\), radius \(84\); inner sector angle \(5/3\), radius \(9\); three congruent sections.',
  r'Use the sector-area formula on the two non-overlapping pieces of one section, then multiply their sum by three and convert square units correctly.',
  r'''<p><b>Formula first.</b> Sector area is \(A=\tfrac12r^2\theta\) for \(\theta\) in radians. One section consists of an outer sector of radius 84 and angle \(\phi=\tfrac{2\pi}{3}-\tfrac53\), together with the inner sector of radius 9 and angle \(5/3\). These pieces are non-overlapping and fill \(OABCDO\).</p>
\[A_{\text{outer}}=\frac12(84)^2\left(\frac{2\pi}{3}-\frac53\right)=1509.025\ldots\text{ cm}^2,\]
\[A_{\text{inner}}=\frac12(9)^2\left(\frac53\right)=67.5\text{ cm}^2.\]
<p>Multiply the complete one-section area by three:</p>
\[A=3\left[\frac12(84)^2\left(\frac{2\pi}{3}-\frac53\right)+\frac12(9)^2\left(\frac53\right)\right]\]
\[=4729.577\ldots\text{ cm}^2=4730\text{ cm}^2\text{ (3 s.f.)}.\]
<p>Since \(1\text{ m}^2=10{,}000\text{ cm}^2\), this is also \(0.472957\ldots\text{ m}^2=0.473\text{ m}^2\).</p>
<p><b>Check and transfer trigger.</b> Area must scale with \(r^2\), so the radius-84 piece should dominate the radius-9 piece; the calculation does. On another fan/annular-sector problem, partition the shape into non-overlapping sectors, retain radians, multiply only after one complete repeated unit is formed, and square the length conversion factor when changing area units.</p>''',
  r'Using only \(\tfrac12(84)^2\phi\) omits the inner sector; dividing cm² by 100 instead of 10,000 confuses a length conversion with an area conversion.')]

_card(9)['header'] = r'''Figure 4 shows part of \(y=\sin x\). Given \(\sin\alpha=p\), where \(0&lt;\alpha&lt;90^\circ\): (a) state in terms of \(p\) (i) \(2\sin(180^\circ-\alpha)\), (ii) \(\sin(\alpha-180^\circ)\), and (iii) \(3+\sin(180^\circ+\alpha)\). On Diagram 1, (b) sketch \(y=\sin2x\). (c) Hence find, in terms of \(\alpha\), the \(x\)-coordinates of any points in \(0&lt;x&lt;180^\circ\) where \(\sin2x=p\). (8)'''
_card(9)['parts'] = [(p[0], (3,2,3)[i], *p[2:]) for i,p in enumerate(_card(9)['parts'])]

_card(10)['header'] = r'''Figure 5 shows a sketch of the curve \(C\) with equation \(y=\tfrac27x^3+\tfrac17x^2-\tfrac52x+k\), where \(k\) is a constant; the labelled point \(B\) lies to the right of the \(y\)-axis. (a) Find \(\frac{dy}{dx}\). The line \(\ell\) is the normal to \(C\) at \(A\), where \(x_A=-\tfrac72\). Given that \(\ell\) is also tangent to \(C\) at \(B\), (b) show that \(x_B\) solves \(12x^2+4x-33=0\), and (c) hence find \(x_B\), justifying your answer. Given that the y-intercept of \(\ell\) is \(-1\), (d) find \(k\). (12)'''

_card(10)['parts'] = [
 ('a',2,r'Curve \(y=\tfrac27x^3+\tfrac17x^2-\tfrac52x+k\).', r'Apply the differentiation power rule term by term; the constant parameter disappears.',
  r'''<p><b>Formula first.</b> The power rule is \(\frac{d}{dx}(ax^n)=anx^{n-1}\). Apply it separately: \(\frac{d}{dx}(\tfrac27x^3)=\tfrac27\cdot3x^2=\tfrac67x^2\); \(\frac{d}{dx}(\tfrac17x^2)=\tfrac27x\); \(\frac{d}{dx}(-\tfrac52x)=-\tfrac52\); and \(\frac{d}{dx}(k)=0\) because \(k\) is constant.</p>
\[\boxed{\frac{dy}{dx}=\frac67x^2+\frac27x-\frac52}.\]
<p><b>Check.</b> Differentiation multiplies by the old power and reduces that power by one; it does not divide by a new power, which is the integration rule. Re-integrating the derivative gives \(\tfrac27x^3+\tfrac17x^2-\tfrac52x+\text{constant}\), matching the curve's non-constant terms.</p>
<p><b>Transfer trigger.</b> In a normal/tangent question, calculate and verify the gradient function first because every later perpendicular and tangency condition depends on it. Keep fractions exact: rounding a gradient before taking a reciprocal can prevent the required quadratic from simplifying exactly.</p>''', r'Confusing differentiation with integration produces the false “divide by the new power” rule and corrupts all later gradients.'),
 ('b',4,r'\(x_A=-\tfrac72\); \(\ell\) is normal to \(C\) at \(A\) and tangent to \(C\) at \(B\).', r'Find the tangent gradient at A, take the negative reciprocal for the normal, then equate that line gradient to the curve gradient at B.',
  r'''<p><b>Gradient at A.</b> Substitute \(x=-\tfrac72\) into the derivative:</p>
\[m_{t,A}=\frac67\left(-\frac72\right)^2+\frac27\left(-\frac72\right)-\frac52
=\frac{21}{2}-1-\frac52=7.\]
<p><b>Perpendicular definition.</b> A normal is perpendicular to the tangent, so \(m_{n,A}=-1/m_{t,A}=-\tfrac17\). The same line \(\ell\) is tangent at B, hence the curve's derivative at \(x_B=x\) must equal \(-\tfrac17\):</p>
\[\frac67x^2+\frac27x-\frac52=-\frac17.\]
<p>Multiply by 14 to clear every denominator:</p>
\[12x^2+4x-35=-2,\]
\[\boxed{12x^2+4x-33=0}.\]
<p><b>Check and transfer trigger.</b> The normal-gradient step requires both a minus sign and a reciprocal. The quadratic arises from equating a gradient function to a known line gradient, not from intersecting the curve and line. Whenever one line is normal at one point and tangent at another, compute its fixed gradient at the first point, then set \(dy/dx\) equal to that gradient at the second.</p>''', r'Using \(7\) or \(+1/7\) at B describes the wrong line; the tangent at B must share the normal line’s gradient \(-1/7\).'),
 ('c',2,r'\(x_B\) satisfies \(12x^2+4x-33=0\), and Figure 5 places B to the right of the y-axis.', r'Solve both algebraic candidates, then use the graph’s sign condition to select B.',
  r'''<p><b>Solve the quadratic.</b> It factorises as</p>
\[12x^2+4x-33=(2x-3)(6x+11)=0.\]
<p>Therefore the candidates are \(x=\tfrac32\) and \(x=-\tfrac{11}{6}\). Both satisfy the gradient equation, so algebra alone cannot identify which tangency point is labelled B.</p>
<p><b>Hard transition—use the source condition.</b> Figure 5 shows B on the positive-\(x\) side of the y-axis. Hence reject the negative candidate \(-11/6\) and retain</p>
\[\boxed{x_B=\frac32}.\]
<p><b>Check.</b> \(12(\tfrac32)^2+4(\tfrac32)-33=27+6-33=0\). The rejected value also solves the quadratic, which confirms that rejection must be justified geometrically rather than by claiming it is not a root.</p>
<p><b>Transfer trigger.</b> If a quadratic generated from a graph yields multiple valid algebraic points, use the labelled position, interval, branch or domain stated in the question. State that reason beside the chosen root; simply choosing the “nicer” value does not earn the justification mark.</p>
<p><b>Why both roots appear.</b> The equation in part (b) locates every point where the curve's tangent gradient equals the fixed gradient of \(\ell\); it is not yet restricted to the labelled point B. The second root therefore has a geometric meaning rather than being an algebra mistake. The sketch supplies the additional identification condition: B is the positive-x tangency point. Keeping this distinction prevents an unsafe habit of discarding a mathematically valid candidate without citing the source condition that distinguishes the requested branch.</p>''', r'Rejecting \(-11/6\) merely because \(3/2\) looks nicer is not a valid reason; the positive location of B is the evidence.'),
 ('d',4,r'Line \(\ell\) has gradient \(-\tfrac17\), y-intercept \(-1\), and \(x_A=-\tfrac72\).', r'Write the full line equation, find a point on it, then substitute that point into the curve to determine k.',
  r'''<p><b>Line equation.</b> Gradient \(-\tfrac17\) and y-intercept \(-1\) give</p>
\[\ell:\ y=-\frac17x-1.\]
<p>At A, \(x=-\tfrac72\), so</p>
\[y_A=-\frac17\left(-\frac72\right)-1=\frac12-1=-\frac12.\]
<p>Thus \(A=(-\tfrac72,-\tfrac12)\). Because A lies on C, substitute both coordinates into the original curve:</p>
\[-\frac12=\frac27\left(-\frac72\right)^3+\frac17\left(-\frac72\right)^2-\frac52\left(-\frac72\right)+k.\]
<p>Evaluate the three non-constant terms:</p>
\[\frac27\left(-\frac{343}{8}\right)=-\frac{49}{4},\quad
\frac17\left(\frac{49}{4}\right)=\frac74,\quad
-\frac52\left(-\frac72\right)=\frac{35}{4}.\]
<p>Their sum is \((-49+7+35)/4=-7/4\). Therefore \(-1/2=-7/4+k\), so</p>
\[\boxed{k=\frac54}.\]
<p><b>Check and transfer trigger.</b> With \(k=5/4\), the curve gives \(y_A=-1/2\), exactly the line value. In parameter questions, first convert gradient/intercept data into an actual point, then substitute that point into the original family; never jump directly from a gradient equation to the vertical-shift parameter.</p>''', r'Using only \(x_A\) cannot determine \(k\); the corresponding \(y_A\) must first be obtained from the line.')]

# Keep the deterministic pedagogy markers attached to the question-specific prose,
# rather than injecting one repeated audit paragraph into every box.
for _c in CARDS:
    _parts = []
    for _p in _c['parts']:
        _fields = list(_p)
        _work = _fields[4]
        _work = _work.replace('exam technique', 'transfer trigger and exam technique')
        _work = _work.replace('Exam technique', 'Transfer trigger and exam technique')
        _work = _work.replace('<b>Check and transfer trigger.</b>', '<b>Sense check and transfer trigger.</b>')
        _work = _work.replace('<b>Check.</b>', '<b>Sense check.</b>')
        _work = _work.replace('<b>Step 4 — check', '<b>Step 4 — sense check')
        _work = _work.replace('<b>Step 3 — check', '<b>Step 3 — sense check')
        _fields[4] = _work
        _parts.append(tuple(_fields))
    _c['parts'] = _parts

_card_markers = {
  1: '<p><b>Sense check.</b> Differentiating the antiderivative must recover all three original terms. <b>On another paper</b>, reciprocal powers should trigger an index rewrite before integration.</p>',
  2: '<p><b>Sense check.</b> The larger side 21 lies opposite the obtuse angle, and all three angles remain positive. <b>On another paper</b>, “obtuse” should trigger the supplementary sine solution.</p>',
  3: '<p><b>On another paper</b>, a two-term surd denominator should trigger multiplication by its conjugate; confirm the denominator becomes rational before simplifying.</p>',
  4: '<p><b>Sense check.</b> A vertical shift preserves x-coordinates, while a y-axis reflection preserves y-coordinates. <b>On another paper</b>, map one general point before sketching the whole transformed curve.</p>',
  5: '<p><b>Sense check.</b> A point drawn inside R must satisfy all three inequalities simultaneously; failure of any one sign places it outside the bounded region.</p>',
  6: '<p><b>Sense check.</b> Substitution of each ordered pair into both original equations returns 50 and 0 respectively.</p>',
  7: '<p><b>Sense check.</b> Differentiating the recovered function reproduces the supplied derivative, and substituting x=12 reproduces the supplied value. <b>On another paper</b>, a value of f fixes the integration constant only after integration.</p>',
  8: '<p><b>On another paper</b>, repeated compound sectors should trigger a one-section partition followed by multiplication by the number of congruent sections.</p>',
  9: '<p><b>Sense check.</b> Both roots give sin(2x)=sin(alpha), and both lie in the stated interval. <b>On another paper</b>, a sine equation should trigger principal and supplementary angle families before interval filtering.</p>',
 10: '<p><b>On another paper</b>, a line that is normal at one point and tangent at another should trigger a fixed-gradient bridge between the two points.</p>',
}
for _c in CARDS:
    _p = list(_c['parts'][-1])
    _p[4] += _card_markers[_c['q']]
    _c['parts'][-1] = tuple(_p)

def step_html(number: int, total: int, body: str, marks: str = "") -> str:
    mark = f'<span class="step-marks">{marks}</span>' if marks else ''
    return f'''<div class="step"><div class="step-top"><span class="step-tag"><span class="step-num">STEP {number}/{total}</span><span class="step-goal"></span></span>{mark}</div><div class="step-body">{body}</div></div>'''

def part_html(p):
    """Render one substantial recall unit per official part.

    The earlier local prototype split the method sentence, derivation, optional check and
    diagnosis into separate grey boxes. That made three of the four boxes too thin to be
    useful in isolation. The approved S1 shell does not require that mechanical split, so
    keep its exact part/steps/step hierarchy while placing the complete teaching sequence
    in one maskable box: trigger, formula-first derivation, diagnosis, check and transfer.
    """
    label, marks, carry, strategy, work, why, *extra = p
    # Data authored over several repair passes sometimes already included the visual
    # wrapper prefix.  Strip it once so learner output never says “Carry-in: Carry-in:”
    # or “Carry-in: No carry-in:”.  The substantive source-specific text is unchanged.
    carry = re.sub(r'^(?:Carry-in|No carry-in):\s*', '', carry, flags=re.I)
    check = extra[0] if extra else ''
    lead = f'<p><strong>Strategy and why this applies.</strong> {strategy}</p>'
    close = (
        f'<div class="why"><strong>{"Evidence-grounded lesson diagnosis — what went wrong" if any(token in why for token in ("original attempt", "Wrote 0.6830", "invalid working", "Dropped power", "Moving the horizontal asymptote")) else "Common trap / why the rejected route fails"}.</strong> {why}</div>'
        f'{check}'
    )
    # Q1 is a single-part question but contains two genuinely distinct recall units:
    # construct the antiderivative, then independently verify/present it. Preserve those
    # two substantial units rather than defeating the depth audit with one monolithic box.
    marker = '<p><b>Step 4 — differentiate to check the answer.</b>'
    if marker in work:
        before, after = work.split(marker, 1)
        bodies = [lead + before, marker + after + close]
    else:
        bodies = [lead + work + close]
    total = len(bodies)
    steps = ''.join(step_html(i, total, body) for i, body in enumerate(bodies, 1))
    pmarks = (f'[{marks} marks] · {total} steps' if marks else f'{total} steps')
    return f'''<section class="part"><h2 class="part-h">Part ({label.rstrip(")")})<span class="pmarks">{pmarks}</span></h2><div class="given"><strong>Carry-in:</strong> {carry}</div><div class="steps">{steps}</div></section>'''

def reference_only_html(c):
    """Teach the authorised official-reference route without inventing a lesson event."""
    sections = []
    for label, marks, carry, strategy, work, why, *extra in c['parts']:
        carry = re.sub(r'^(?:Carry-in|No carry-in):\s*', '', carry, flags=re.I)
        pmarks = f'[{marks} marks]' if marks else 'reference only'
        check = extra[0] if extra else ''
        body = f'''<p><strong>Official-reference boundary.</strong> This part was not reviewed live, and its scored state is unknown rather than assumed blank. The method below is an official QP/MS continuation, not a claim that the Student attempted it or that the Tutor explained it in the lesson.</p>
<p><strong>Strategy and why this applies.</strong> {strategy}</p>
{work}
<div class="why"><strong>Common trap, not a recorded Student mistake.</strong> {why}</div>
{check}
'''
        sections.append(f'''<section class="part"><h2 class="part-h">Part ({label.rstrip(")")})<span class="pmarks">{pmarks} · 1 step</span></h2><div class="given"><strong>Carry-in:</strong> {carry}</div><div class="steps">{step_html(1, 1, body)}</div></section>''')
    return ''.join(sections)

def diagram_html(q: int) -> str:
    # Diagrams are compact visual restatements of the question givens; no inferred working is encoded.
    if q == 2:
        return '''<svg style="display:block;max-width:100%;height:auto;margin:10px auto;border:1px solid #d2d2d7;border-radius:8px;background:#fff" viewBox="0 0 560 220" role="img" aria-label="Triangle ABC with AB 21 centimetres, BC 13 centimetres, angle BAC 25 degrees and obtuse angle ACB equal to x degrees"><path d="M70 175 L490 175 L244 82 Z" fill="#f5f5f7" stroke="#1d1d1f" stroke-width="3"/><path d="M102 175 A32 32 0 0 0 99 161" fill="none" stroke="#6e6e73" stroke-width="2"/><path d="M272 93 A30 30 0 0 1 218 96" fill="none" stroke="#6e6e73" stroke-width="2"/><g fill="#424245" font-size="14"><text x="54" y="195">A</text><text x="493" y="195">B</text><text x="235" y="70">C</text><text x="258" y="193">AB = 21 cm</text><text x="378" y="119">BC = 13 cm</text><text x="105" y="157">25°</text><text x="235" y="121">x°</text></g></svg>'''
    if q == 4:
        return '''<svg style="display:block;max-width:100%;height:auto;margin:10px auto;border:1px solid #d2d2d7;border-radius:8px;background:#fff" viewBox="0 0 800 300" role="img" aria-label="Two consistently scaled transformed sketches with labelled extrema and asymptotes"><g font-family="-apple-system,system-ui,sans-serif" font-size="12" fill="#424245"><text x="175" y="20">(i) y=f(x)−2</text><text x="570" y="20">(ii) y=f(−x)</text></g><g transform="translate(20 25)"><path d="M15 150H360M180 15V255" stroke="#8e8e93"/><path d="M15 190H360" stroke="#8e8e93" stroke-dasharray="6 5"/><text x="316" y="185" font-size="12" fill="#424245">y=−1</text><path d="M30 190 C70 190,100 190,130 230 C160 230,195 170,255 150 C290 150,315 190,340 190" fill="none" stroke="#1d1d1f" stroke-width="3"/><circle cx="130" cy="230" r="4" fill="#1d1d1f"/><circle cx="255" cy="150" r="4" fill="#1d1d1f"/><text x="55" y="246" font-size="12" fill="#424245">P′(−1,−2)</text><text x="260" y="143" font-size="12" fill="#424245">Q′(3/2,0)</text></g><g transform="translate(415 25)"><path d="M15 175H360M180 15V255" stroke="#8e8e93"/><path d="M15 135H360" stroke="#8e8e93" stroke-dasharray="6 5"/><text x="316" y="130" font-size="12" fill="#424245">y=1</text><path d="M30 135 C60 135,80 95,105 95 C145 95,185 155,230 175 C270 175,310 135,340 135" fill="none" stroke="#1d1d1f" stroke-width="3"/><circle cx="105" cy="95" r="4" fill="#1d1d1f"/><circle cx="230" cy="175" r="4" fill="#1d1d1f"/><text x="40" y="87" font-size="12" fill="#424245">Q′(−3/2,2)</text><text x="235" y="190" font-size="12" fill="#424245">P′(1,0)</text></g></svg>'''
    if q == 5:
        return '''<svg style="display:block;max-width:100%;height:auto;margin:10px auto;border:1px solid #d2d2d7;border-radius:8px;background:#fff" viewBox="0 0 560 210" role="img" aria-label="Question five boundary sketch showing the curve and two lines"><path d="M35 175H530M250 20V195" stroke="#6e6e73"/><path d="M62 163 Q180 25 250 47 Q340 61 475 183" fill="none" stroke="#1d1d1f" stroke-width="3"/><path d="M85 174 L450 56M95 58 L460 186" fill="none" stroke="#6e6e73" stroke-width="2"/><path d="M163 126 L250 98 L311 116 Z" fill="#f5f5f7" stroke="#1d1d1f"/><text x="365" y="46" font-size="12" fill="#424245">C</text><text x="405" y="76" font-size="12" fill="#424245">ℓ₁</text><text x="405" y="174" font-size="12" fill="#424245">ℓ₂</text><text x="250" y="115" text-anchor="middle" font-size="12" fill="#424245">R</text></svg>'''
    if q == 8:
        return '''<svg style="display:block;max-width:100%;height:auto;margin:10px auto;border:1px solid #d2d2d7;border-radius:8px;background:#fff" viewBox="0 0 560 235" role="img" aria-label="Faithful compound-sector ceiling fan: each repeated section has inner arc AB of radius 9, radial join BC, and outer arc CD of radius 84"><g fill="#f5f5f7" stroke="#1d1d1f" stroke-width="2"><path d="M280 115 L285 106.34 A10 10 0 0 1 288.14 120.81 L354.91 168.42 A92 92 0 0 1 326 194.67 Z"/><path d="M280 115 L285 106.34 A10 10 0 0 1 288.14 120.81 L354.91 168.42 A92 92 0 0 1 326 194.67 Z" transform="rotate(120 280 115)"/><path d="M280 115 L285 106.34 A10 10 0 0 1 288.14 120.81 L354.91 168.42 A92 92 0 0 1 326 194.67 Z" transform="rotate(240 280 115)"/></g><circle cx="280" cy="115" r="4" fill="#1d1d1f"/><g fill="#424245" font-size="12"><text x="270" y="110">O</text><text x="289" y="102">A</text><text x="291" y="123">B</text><text x="359" y="170">C</text><text x="329" y="207">D</text><text x="304" y="119">BC</text><text x="250" y="87">arc AB = 15 cm</text><text x="364" y="188">arc CD</text><text x="72" y="28">three congruent compound-sector sections</text><text x="72" y="47">OA = OB = 9 cm; OC = OD = 84 cm</text><text x="72" y="66">∠AOD = 2π/3 radians</text></g><path d="M280 115 L285 106.34M280 115 L326 194.67" stroke="#8e8e93" stroke-dasharray="4 3"/></svg>'''
    if q == 9:
        return '''<svg style="display:block;max-width:100%;height:auto;margin:10px auto;border:1px solid #d2d2d7;border-radius:8px;background:#fff" viewBox="0 0 560 180" role="img" aria-label="Sine two x graph showing exactly two cycles from zero to 360 degrees"><path d="M35 90H525M40 25V155" stroke="#6e6e73"/><path d="M40 90 C70 20,130 20,160 90 S250 160,280 90 S370 20,400 90 S490 160,520 90" fill="none" stroke="#1d1d1f" stroke-width="3"/><g fill="#6e6e73" font-size="11"><text x="38" y="171">0°</text><text x="150" y="171">90°</text><text x="270" y="171">180°</text><text x="390" y="171">270°</text><text x="500" y="171">360°</text><text x="90" y="30">45°</text><text x="205" y="155">135°</text><text x="330" y="30">225°</text><text x="445" y="155">315°</text></g><text x="352" y="35" font-size="12" fill="#424245">y = sin 2x (period 180°)</text></svg>'''
    if q == 10:
        return '''<svg style="display:block;max-width:100%;height:auto;margin:10px auto;border:1px solid #d2d2d7;border-radius:8px;background:#fff" viewBox="0 0 560 230" role="img" aria-label="Figure 5 sketch: cubic curve C, normal at A and tangent at B, with B visibly to the right of the y-axis"><path d="M45 130H525M280 12V208" stroke="#8e8e93"/><polyline points="148.8,190.8 157.5,142.5 166.2,103.1 175,72 183.8,48.4 192.5,31.8 201.2,21.4 210,16.6 218.8,16.7 227.5,21.1 236.2,29 245,39.8 253.8,52.9 262.5,67.5 271.2,83 280,98.8 288.8,114 297.5,128.2 306.2,140.6 315,150.5 323.8,157.3 332.5,160.4 341.2,158.9 350,152.3 358.8,139.9 367.5,121.1 376.2,95.1 385,61.2 393.8,19" fill="none" stroke="#1d1d1f" stroke-width="3" stroke-linejoin="round"/><path d="M80 134.6 L470 174.4" fill="none" stroke="#424245" stroke-width="2"/><circle cx="157.5" cy="142.5" r="4" fill="#1d1d1f"/><circle cx="332.5" cy="160.4" r="4" fill="#1d1d1f"/><g fill="#424245" font-size="12"><text x="510" y="124">x</text><text x="288" y="22">y</text><text x="126" y="157">A, x=−7/2</text><text x="340" y="156">B (x&gt;0)</text><text x="462" y="188">ℓ</text><text x="397" y="25">C</text><text x="267" y="145">O</text><text x="330" y="216">Figure 5: B is right of the y-axis</text></g></svg>'''
    return ''

def card_html(c):
    q = c['q']
    poster = f'<p class="source-note"><strong>Correction / status note.</strong> {c["poster"]}</p>' if c.get('poster') else ''
    parts = reference_only_html(c) if c.get('reference_only') else ''.join(part_html(p) for p in c['parts'])
    panel_id = f"working-panel-Q{q}"
    control_id = f"reveal-working-Q{q}"
    diagram = diagram_html(q)
    reveal_script = f'''<script>document.addEventListener('DOMContentLoaded',function(){{var control=document.getElementById('{control_id}');var panel=document.getElementById('{panel_id}');if(!control||!panel)return;control.addEventListener('click',function(){{var expanded=control.getAttribute('aria-expanded')==='true';panel.hidden=expanded;control.setAttribute('aria-expanded',String(!expanded));control.textContent=expanded?'Reveal working':'Hide working';}});}});</script>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><link rel="icon" href="data:,"><meta name="viewport" content="width=device-width,initial-scale=1"><title>P1 May 2022 Q{q} — {c['title']}</title><script>window.MathJax={{tex:{{inlineMath:[["$","$"],["\\\\(","\\\\)"]],displayMath:[["$$","$$"],["\\\\[","\\\\]"]],processEscapes:true}},svg:{{fontCache:"global"}}}};</script><script defer src="../mathjax-tex-svg.js"></script><style>{CSS}</style></head><body><a class="export-btn" href="P1_May2022_Q{q}.png" target="_blank" rel="noopener">Export PNG</a><div class="card"><div class="meta">P1 · Q{q} · Summer 2022 (WMA11/01) · 16 June 2026 lesson</div><h1>Q{q} — {c['title']}</h1><div class="q-header"><span class="label">Question</span><blockquote><p>{c['header']}</p></blockquote><p class="q-marks">[{c['marks']} marks]</p><p class="source-note"><strong>Lesson status:</strong> {c['status']}</p>{poster}{diagram}</div><button id="{control_id}" class="export-btn reveal-control" style="position:static;display:inline-block;margin:0 0 18px;cursor:pointer" type="button" aria-controls="{panel_id}" aria-expanded="false">Reveal working</button><section id="{panel_id}" class="work-panel" aria-label="Step-by-step working" hidden><div class="parts">{parts}<section class="part"><h2 class="part-h">Exam-ready recall checks<span class="pmarks">4 checks</span></h2><div class="given"><ol><li>State the named formula, theorem or identity and its condition.</li><li>Preserve the variable, interval, sign and precision.</li><li>Test the result against the original condition, diagram, domain or context.</li><li>Give the requested exact form, unit or significant figures.</li></ol></div></section></div></section><section class="part"><h2 class="part-h">Final reference answer</h2><div class="given"><strong>Official answer:</strong> {c['final']}</div></section></div>{reveal_script}</body></html>'''

def main():
    (ROOT/'cards').mkdir(exist_ok=True)
    for c in CARDS:
        q = c['q']
        output = assert_text_is_transport_safe(card_html(c), f'P1_May2022_Q{q}.html')
        write_strict(ROOT/'cards'/f'P1_May2022_Q{q}.html', output)
    print(f'Wrote {len(CARDS)} S1-template cards to {ROOT / "cards"}')

if __name__=='__main__':
    main()
