#!/usr/bin/env python3
"""Clean local-only downstream rebuild from the frozen final 26 June P4 guide.
This script deliberately has no input path to legacy/downstream artifacts.
"""
from __future__ import annotations
import hashlib, html, json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LESSON = ROOT.parent
GUIDE = LESSON / "guide_v2" / "revision_guide.pdf"
GUIDE_TEXT = LESSON / "guide_v2" / "revision_guide_text.md"
REGISTER = LESSON / "guide_v2" / "source_register.md"
EXPECTED_GUIDE_SHA = "34ce9ab8dc45d124f39f7d3ecb951bae3c92f607be5f998615628e118457a56a"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def tex(s: str) -> str:
    # Card expressions are authored as raw Python strings; normalize escaped TeX
    # commands once so the browser receives real TeX, not visible `tfrac` text.
    s = s.replace(chr(92) + chr(92), chr(92))
    return r"\(" + s + r"\)"

def answer_html(s: str) -> str:
    """Render embedded TeX fragments while preserving explanatory prose as HTML."""
    s = s.replace(chr(92) + chr(92), chr(92))
    chunks = re.split(r"(\\\(.*?\\\))", s)
    return ''.join(tex(chunk[2:-2]) if chunk.startswith(r"\(") else html.escape(chunk) for chunk in chunks)

if sha(GUIDE) != EXPECTED_GUIDE_SHA:
    raise SystemExit("Frozen final guide hash mismatch; refusing to create derivatives.")

# A fresh local MathJax asset is staged by the caller from a public package source.
mathjax = ROOT / "assets" / "mathjax" / "tex-svg.js"
if not mathjax.is_file():
    raise SystemExit("Missing fresh local MathJax tex-svg asset.")

for p in (ROOT / "cards", ROOT / "assets" / "diagrams", ROOT / "recall_pdf_renders"):
    p.mkdir(parents=True, exist_ok=True)

CSS = r"""
:root { --ink:#17212b; --muted:#52606d; --paper:#fff; --wash:#f3f5f7; --accent:#0c6675; --accent2:#a1452e; --line:#ced6dc; --status:#eaf4f5; }
* { box-sizing:border-box; } body { margin:0; background:#e8edf0; color:var(--ink); font:17px/1.55 Arial, Helvetica, sans-serif; }
main { width:min(1160px, calc(100% - 32px)); margin:24px auto; background:var(--paper); padding:44px 54px 56px; border:1px solid #dfe5e8; }
h1 { font-size:32px; line-height:1.16; margin:0 0 7px; } h2 { font-size:23px; margin:34px 0 12px; border-bottom:2px solid var(--accent); padding-bottom:6px; } h3 { font-size:19px; margin:0 0 8px; } p { margin:10px 0; } .eyebrow { color:var(--accent); font-weight:700; letter-spacing:.06em; text-transform:uppercase; font-size:13px; }
mjx-container { display:block !important; width:100% !important; max-width:100%; overflow-x:auto; overflow-y:hidden; vertical-align:middle; } mjx-container > svg { max-width:100% !important; height:auto !important; } mjx-assistive-mml { max-width:1px !important; overflow:hidden !important; } .nav { display:flex; flex-wrap:wrap; gap:10px; margin:18px 0 24px; }.btn { background:var(--accent); color:#fff; border:0; border-radius:7px; padding:10px 14px; font:inherit; font-weight:700; text-decoration:none; display:inline-block; cursor:pointer; }.btn.secondary { background:#3f4d59; }.reveal-control { margin:0 0 2px; }.work-panel[hidden] { display:none; }.status { border-left:6px solid var(--accent); padding:14px 16px; background:var(--status); margin:18px 0; font-weight:600; }.marks { display:inline-block; background:#f7e8df; color:#71331f; border-radius:20px; padding:3px 10px; margin-left:8px; font-size:14px; font-weight:bold; }.work { background:#eef1f3; border:1px solid #d4dade; border-radius:8px; padding:17px 19px; margin:16px 0; break-inside:avoid; }.step { font-weight:700; color:var(--accent); }.answer { background:#e4f0e9; border-left:6px solid #287248; padding:14px 17px; margin:18px 0; font-weight:700; }.boundary { background:#fff5e8; border-left:6px solid #b66b1c; padding:13px 16px; margin:18px 0; }.visual { border:1px solid var(--line); border-radius:8px; padding:12px; background:#fff; margin:20px 0; text-align:center; }.visual svg { max-width:100%; height:auto; }.small { color:var(--muted); font-size:14px; }.deck { display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:16px; }.tile { border:1px solid var(--line); border-radius:10px; padding:17px; background:#fff; }.tile h2 { font-size:19px; margin:0 0 9px; border:none; padding:0; }.tile .status { font-size:14px; padding:10px; margin:12px 0; }.legend { border:1px solid var(--line); background:#f9fbfc; padding:16px; border-radius:8px; }.checklist li { margin:7px 0; } table { border-collapse:collapse; width:100%; margin:14px 0; } th,td { border:1px solid var(--line); padding:9px; vertical-align:top; } th { background:#edf3f5; text-align:left; }
@media print { body{background:#fff;} main{width:100%; margin:0; padding:16mm;} .nav{display:none;} }
"""

cards = [
{
"slug":"01_q1_binomial", "title":"P4 Q1 - negative-index binomial", "marks":"5 + 1 + 1 marks", "status":"Lesson hints/start only. The full expansion and answers below are official mark-scheme reference; they were not completed in the lesson.",
"stem":"For the October 2025 P4 question, find the first four terms in ascending powers of x of (2 + 5x)^(-2); state the values of x for which the expansion is valid; then find a, b and c such that (4/(2+5x))^2 is approximately a + bx + cx^2.",
"steps":[("Normalise",r"(2+5x)^{-2}=2^{-2}(1+\\tfrac52x)^{-2}=\\tfrac14(1+\\tfrac52x)^{-2}."),("Use the general binomial series",r"(1+u)^{-2}=1-2u+3u^2-4u^3+\\cdots,\\quad u=\\tfrac52x."),("Expand",r"(2+5x)^{-2}=\\tfrac14-\\tfrac54x+\\tfrac{75}{16}x^2-\\tfrac{125}{8}x^3+\\cdots."),("State validity",r"|u|<1\\Rightarrow |\\tfrac52x|<1\\Rightarrow |x|<\\tfrac25."),("Scale for part (c)",r"(\\tfrac4{2+5x})^2=16(2+5x)^{-2}\\approx4-20x+75x^2.")],
"answer":r"First four terms: \\(\\frac14-\\frac54x+\\frac{75}{16}x^2-\\frac{125}{8}x^3\\). Valid for \\(|x|<\\frac25\\). Hence \\(a=4, b=-20, c=75\\).",
"visual":"""<svg viewBox=\"0 0 700 180\" role=\"img\" aria-label=\"Normalisation flow for the binomial expansion\"><defs><marker id=\"a\" markerWidth=\"8\" markerHeight=\"8\" refX=\"7\" refY=\"4\" orient=\"auto\"><path d=\"M0,0 L8,4 L0,8Z\" fill=\"#0c6675\"/></marker></defs><rect x=\"20\" y=\"55\" width=\"180\" height=\"65\" rx=\"8\" fill=\"#edf3f5\" stroke=\"#0c6675\"/><text x=\"110\" y=\"94\" text-anchor=\"middle\" font-size=\"21\">(2 + 5x)⁻²</text><path d=\"M205 88H290\" stroke=\"#0c6675\" stroke-width=\"3\" marker-end=\"url(#a)\"/><rect x=\"300\" y=\"55\" width=\"190\" height=\"65\" rx=\"8\" fill=\"#edf3f5\" stroke=\"#0c6675\"/><text x=\"395\" y=\"94\" text-anchor=\"middle\" font-size=\"19\">¼(1 + 5x/2)⁻²</text><path d=\"M495 88H580\" stroke=\"#0c6675\" stroke-width=\"3\" marker-end=\"url(#a)\"/><rect x=\"590\" y=\"55\" width=\"95\" height=\"65\" rx=\"8\" fill=\"#e4f0e9\" stroke=\"#287248\"/><text x=\"637\" y=\"94\" text-anchor=\"middle\" font-size=\"18\">series</text></svg>"""
},
{
"slug":"02_q2_volume", "title":"P4 Q2 - volume of revolution", "marks":"Marks not stated in the final guide", "status":"Self-assessed gap. The official result below is reference-only: this question was not taught in the lesson.",
"stem":"The final guide identifies P4 Q2 as: y = (5/3)√(x−1), for 2 ≤ x ≤ 8, rotated through 2π about the x-axis. Find the volume of revolution.",
"steps":[("Choose the required P4 formula",r"V=\\pi\\int_a^b y^2\\,dx."),("Substitute the curve",r"y^2=\\tfrac{25}{9}(x-1),\\quad V=\\pi\\int_2^8\\tfrac{25}{9}(x-1)\\,dx."),("Integrate",r"V=\\tfrac{25\\pi}{9}\\left[\\tfrac12(x-1)^2\\right]_2^8=\\tfrac{25\\pi}{18}(49-1).")],
"answer":r"\\(V=\\frac{200\\pi}{3}\\) cubic units. The final guide distinguishes \\(\\pi\\int y^2dx\\) (required P4 form) from \\(\\pi\\int x^2dy\\), which is not required for P4.",
"visual":"""<svg viewBox=\"0 0 700 230\" role=\"img\" aria-label=\"Curve and rotation about x-axis\"><line x1=\"70\" y1=\"170\" x2=\"640\" y2=\"170\" stroke=\"#17212b\" stroke-width=\"3\"/><text x=\"648\" y=\"176\" font-size=\"18\">x</text><path d=\"M150 145 Q300 118 540 35\" fill=\"none\" stroke=\"#0c6675\" stroke-width=\"5\"/><path d=\"M150 170 L150 145 M540 170 L540 35\" stroke=\"#a1452e\" stroke-dasharray=\"7 6\" stroke-width=\"2\"/><path d=\"M250 185 C300 210 430 210 480 185\" fill=\"none\" stroke=\"#a1452e\" stroke-width=\"3\"/><text x=\"240\" y=\"110\" font-size=\"19\">y = (5/3)√(x−1)</text><text x=\"139\" y=\"198\" font-size=\"17\">2</text><text x=\"533\" y=\"198\" font-size=\"17\">8</text><text x=\"300\" y=\"220\" font-size=\"16\" fill=\"#a1452e\">rotate about x-axis</text></svg>"""
},
{
"slug":"03_q4_implicit", "title":"P4 Q4 - implicit differentiation", "marks":"5 + 5 marks", "status":"Part (a) was corrected and completed live. Part (b) reached the two-equation setup and was deferred; its solution below is official mark-scheme reference, not a completed lesson solution.",
"stem":"The curve C has equation 4x^2 + y^2 − 2xy = 24x. (a) Find dy/dx in terms of x and y. (b) P(a,b) lies on C, has gradient 2, with a>0 and b>0. Find a and b.",
"steps":[("Differentiate (a)",r"8x+2y\\frac{dy}{dx}-2(x\\frac{dy}{dx}+y)=24."),("Collect dy/dx",r"(2y-2x)\\frac{dy}{dx}=24-8x+2y\\Rightarrow\\frac{dy}{dx}=\\frac{12-4x+y}{y-x}."),("Use the gradient at P",r"2=\\frac{12-4a+b}{b-a}\\Rightarrow 2a+b=12\\Rightarrow b=12-2a."),("Use P on C",r"4a^2+b^2-2ab=24a."),("Solve and filter",r"a^2-8a+12=0\\Rightarrow(a-2)(a-6)=0;\\quad (a,b)=(2,8),(6,0);\\quad b>0\\Rightarrow(2,8).")],
"answer":r"\\(\\frac{dy}{dx}=\\frac{12-4x+y}{y-x}\\), and \\(P=(2,8)\\).",
"visual":"""<svg viewBox=\"0 0 700 210\" role=\"img\" aria-label=\"Two-equation relationship map for P4 Q4\"><rect x=\"25\" y=\"45\" width=\"260\" height=\"110\" rx=\"10\" fill=\"#edf3f5\" stroke=\"#0c6675\" stroke-width=\"2\"/><text x=\"155\" y=\"82\" text-anchor=\"middle\" font-size=\"20\">gradient = 2</text><text x=\"155\" y=\"117\" text-anchor=\"middle\" font-size=\"20\">2a + b = 12</text><rect x=\"415\" y=\"45\" width=\"260\" height=\"110\" rx=\"10\" fill=\"#edf3f5\" stroke=\"#0c6675\" stroke-width=\"2\"/><text x=\"545\" y=\"82\" text-anchor=\"middle\" font-size=\"20\">P lies on C</text><text x=\"545\" y=\"117\" text-anchor=\"middle\" font-size=\"18\">4a²+b²−2ab=24a</text><path d=\"M290 100H405\" stroke=\"#a1452e\" stroke-width=\"4\"/><text x=\"350\" y=\"38\" text-anchor=\"middle\" font-size=\"17\" fill=\"#a1452e\">solve together</text><text x=\"350\" y=\"190\" text-anchor=\"middle\" font-size=\"22\" font-weight=\"bold\">P = (2, 8)</text></svg>"""
},
{
"slug":"04_q5_vectors", "title":"P4 Q5 - intersecting vector lines", "marks":"6 marks total", "status":"Lesson-covered setup and method. λ=−9 and μ=−3 were supplied in the lesson; the arithmetic for β and P below is official mark-scheme reference, not completed live.",
"stem":"The lines l₁: r=(2,−1,3)+λ(1,4,2) and l₂: r=(−1,β,6)+μ(2,−1,7) intersect at P. Find (i) β and (ii) the coordinates of P.",
"steps":[("Equate components",r"2+\\lambda=-1+2\\mu;\\quad -1+4\\lambda=\\beta-\\mu;\\quad 3+2\\lambda=6+7\\mu."),("Solve the outer components",r"\\lambda=-9,\\quad\\mu=-3."),("Find β",r"\\beta=-1+4\\lambda+\\mu=-1+4(-9)-3=-40."),("Find P",r"P=(2+\\lambda,-1+4\\lambda,3+2\\lambda)=(-7,-37,-15)."),("Cross-check",r"(-1,\\beta,6)+\\mu(2,-1,7)=(-7,-37,-15).")],
"answer":r"\\(\\beta=-40\\) and \\(P=(-7,-37,-15)\\). A row of coordinates or an accepted vector form represents the same point.",
"visual":"""<svg viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Vector component equations meeting at a common point\"><line x1=\"80\" y1=\"160\" x2=\"330\" y2=\"75\" stroke=\"#0c6675\" stroke-width=\"6\"/><line x1=\"620\" y1=\"160\" x2=\"330\" y2=\"75\" stroke=\"#a1452e\" stroke-width=\"6\"/><circle cx=\"330\" cy=\"75\" r=\"11\" fill=\"#287248\"/><text x=\"330\" y=\"48\" text-anchor=\"middle\" font-size=\"21\" font-weight=\"bold\">P = (−7, −37, −15)</text><text x=\"135\" y=\"115\" font-size=\"20\" fill=\"#0c6675\">l₁, λ = −9</text><text x=\"475\" y=\"115\" font-size=\"20\" fill=\"#a1452e\">l₂, μ = −3</text><text x=\"350\" y=\"200\" text-anchor=\"middle\" font-size=\"19\">equate x, y and z components</text></svg>"""
},
{
"slug":"05_q6_trig_sub", "title":"P4 Q6 - trigonometric substitution", "marks":"7 marks", "status":"Lesson-covered through substitution, transformed limits and the power split. The final integration/evaluation is official mark-scheme reference, not completed aloud in the lesson.",
"stem":"Using u=3+cos θ, show that ∫₀^(π/2) [sin 2θ / √(3+cos θ)] dθ = a√3+b, where a and b are constants. Show all working; the question says solutions relying entirely on calculator technology are not acceptable.",
"steps":[("Use the identity and substitution",r"\\sin2\\theta=2\\sin\\theta\\cos\\theta,\\quad du=-\\sin\\theta\\,d\\theta,\\quad \\cos\\theta=u-3."),("Transform limits",r"\\theta:0\\to\\pi/2\\quad\\mapsto\\quad u:4\\to3."),("Transform the integral",r"-2\\int_4^3\\frac{u-3}{\\sqrt u}du=-2\\int_4^3(u^{1/2}-3u^{-1/2})du."),("Integrate",r"-2\\left[\\tfrac23u^{3/2}-6u^{1/2}\\right]_4^3."),("Evaluate",r"8\\sqrt3-\\tfrac{40}{3}.")],
"answer":r"\\(a=8\\), \\(b=-\\frac{40}{3}\\), so the integral is \\(8\\sqrt3-\\frac{40}{3}\\).",
"visual":"""<svg viewBox=\"0 0 700 205\" role=\"img\" aria-label=\"Substitution maps theta limits to u limits\"><line x1=\"110\" y1=\"125\" x2=\"580\" y2=\"125\" stroke=\"#17212b\" stroke-width=\"3\"/><circle cx=\"150\" cy=\"125\" r=\"9\" fill=\"#0c6675\"/><circle cx=\"535\" cy=\"125\" r=\"9\" fill=\"#a1452e\"/><text x=\"150\" y=\"161\" text-anchor=\"middle\" font-size=\"20\">θ=0 → u=4</text><text x=\"535\" y=\"161\" text-anchor=\"middle\" font-size=\"20\">θ=π/2 → u=3</text><path d=\"M150 75 C250 25 430 25 535 75\" fill=\"none\" stroke=\"#0c6675\" stroke-width=\"3\"/><text x=\"345\" y=\"48\" text-anchor=\"middle\" font-size=\"21\">u = 3 + cos θ</text><text x=\"345\" y=\"195\" text-anchor=\"middle\" font-size=\"17\" fill=\"#a1452e\">limits reverse: 4 to 3</text></svg>"""
},
{
"slug":"06_prior_p3_review", "title":"Prior P3 review - range and inverse domain", "marks":"Not a P4 paper question; marks not established", "status":"Prior P3 correction reviewed on 26 June. It is explicitly not an October 2025 P4 question. The full inverse algebra was prior work/reference, not re-derived live.",
"stem":"For g(x)=(3+5x)/(x+2), with x>−2, state the range of g and the domain of g⁻¹. Use an algebraic form that exposes the asymptotes.",
"steps":[("Divide",r"g(x)=5-\\frac7{x+2}."),("Use the given domain",r"x>-2\\Rightarrow x+2>0\\Rightarrow -\\frac7{x+2}<0."),("State the range",r"g(x)=5-\\frac7{x+2}<5,\\quad\\text{so }y<5."),("Transfer range to inverse domain",r"\\operatorname{Dom}(g^{-1})=\\operatorname{Range}(g),\\quad\text{therefore }x<5.")],
"answer":r"\\(g(x)=5-\\frac7{x+2}\\); range \\(y<5\\); domain of \\(g^{-1}\\) is \\(x<5\\).",
"visual":"""<svg viewBox=\"0 0 700 230\" role=\"img\" aria-label=\"Rational curve with asymptotes x equals negative two and y equals five\"><line x1=\"80\" y1=\"170\" x2=\"650\" y2=\"170\" stroke=\"#17212b\" stroke-width=\"2\"/><line x1=\"230\" y1=\"25\" x2=\"230\" y2=\"205\" stroke=\"#a1452e\" stroke-width=\"3\" stroke-dasharray=\"8 6\"/><line x1=\"90\" y1=\"85\" x2=\"650\" y2=\"85\" stroke=\"#a1452e\" stroke-width=\"3\" stroke-dasharray=\"8 6\"/><path d=\"M245 190 Q290 125 400 101 Q520 89 640 87\" fill=\"none\" stroke=\"#0c6675\" stroke-width=\"5\"/><text x=\"237\" y=\"220\" font-size=\"17\">x=−2</text><text x=\"100\" y=\"77\" font-size=\"17\">y=5</text><text x=\"440\" y=\"142\" font-size=\"20\">x&gt;−2 branch</text></svg>"""
},
{
"slug":"07_q8_ode", "title":"P4 Q8 - separable differential equation", "marks":"Marks not stated in the final guide", "status":"Self-assessed gap. The solution below is official mark-scheme reference only: Q8 was not taught in the lesson.",
"stem":"The final guide identifies P4 Q8 as dV/dt=12te^(−t), with V(0)=6. Solve for V in terms of t, then decide whether the vessel capacity 20 is reached.",
"steps":[("Integrate",r"V=\\int12te^{-t}dt=-12(t+1)e^{-t}+C."),("Use the initial value",r"6=V(0)=-12+C\\Rightarrow C=18."),("Write the model",r"V=18-12te^{-t}-12e^{-t}."),("Compare with capacity",r"V=18-12(t+1)e^{-t}<18<20\\quad(t\\ge0).")],
"answer":r"\\(V=18-12te^{-t}-12e^{-t}\\). The vessel never reaches capacity 20; it stays below 18 for \\(t\\ge0\\).",
"visual":"""<svg viewBox=\"0 0 700 230\" role=\"img\" aria-label=\"Volume curve rising toward eighteen below a capacity line at twenty\"><line x1=\"70\" y1=\"185\" x2=\"650\" y2=\"185\" stroke=\"#17212b\" stroke-width=\"3\"/><line x1=\"70\" y1=\"42\" x2=\"70\" y2=\"200\" stroke=\"#17212b\" stroke-width=\"3\"/><line x1=\"70\" y1=\"55\" x2=\"650\" y2=\"55\" stroke=\"#a1452e\" stroke-width=\"3\" stroke-dasharray=\"10 7\"/><line x1=\"70\" y1=\"78\" x2=\"650\" y2=\"78\" stroke=\"#0c6675\" stroke-width=\"2\" stroke-dasharray=\"7 6\"/><path d=\"M75 165 C110 130 140 105 185 91 C280 70 430 78 640 78\" fill=\"none\" stroke=\"#287248\" stroke-width=\"5\"/><text x=\"540\" y=\"47\" font-size=\"18\" fill=\"#a1452e\">capacity 20</text><text x=\"560\" y=\"72\" font-size=\"18\" fill=\"#0c6675\">limit 18</text><text x=\"35\" y=\"48\" font-size=\"18\">V</text><text x=\"654\" y=\"193\" font-size=\"18\">t</text></svg>"""
}
]

answer_text = {
    "01_q1_binomial": "First four terms: 1/4 − 5x/4 + 75x²/16 − 125x³/8. Valid for |x|<2/5. Hence a=4, b=−20, c=75.",
    "02_q2_volume": "V = 200π/3 cubic units. The required P4 form is π∫y²dx; π∫x²dy is not required for P4.",
    "03_q4_implicit": "dy/dx = (12−4x+y)/(y−x), and P=(2,8).",
    "04_q5_vectors": "β=−40 and P=(−7,−37,−15). A row of coordinates or an accepted vector form represents the same point.",
    "05_q6_trig_sub": "a=8 and b=−40/3, so the integral is 8√3−40/3.",
    "06_prior_p3_review": "g(x)=5−7/(x+2); range y<5; domain of g⁻¹ is x<5.",
    "07_q8_ode": "V=18−12te^(−t)−12e^(−t). The vessel never reaches capacity 20; it stays below 18 for t≥0.",
}
for card in cards:
    card["answer_text"] = answer_text[card["slug"]]

# Recall source is deliberately reader-safe: no internal paths, hashes, source identifiers, or surnames.
recall_md = """# 26 June P4 recall sheet

## How to use this sheet

Recall the method before opening the answer. Labels distinguish what was reached in the lesson from official-reference completion and self-assessed gaps.

## Method prompts

### P4 Q1 - negative-index binomial [lesson hints; official reference completion]
- Put the expression into the form `constant × (1+u)^n` before expanding.
- For `(2+5x)^−2`, what are the first four terms and what condition must `u` satisfy?
- **Answer:** `1/4 − 5x/4 + 75x²/16 − 125x³/8 + …`, valid for `|x|<2/5`.
- After multiplying by 16, `(4/(2+5x))² ≈ 4 − 20x + 75x²`.

### P4 Q2 - volume of revolution [self-assessed gap; reference only]
- For rotation about the x-axis, use `V=π∫y² dx`.
- For `y=(5/3)√(x−1), 2≤x≤8`, evaluate `π∫₂⁸(25/9)(x−1)dx`.
- **Answer:** `200π/3` cubic units.
- Scope reminder: `π∫y²dx` is required P4 content; `π∫x²dy` is not required for P4.

### P4 Q4 - implicit differentiation [part (a) reached; part (b) reference completion]
- Differentiate `4x²+y²−2xy=24x`, keeping the full product-rule bracket.
- **Answer:** `dy/dx=(12−4x+y)/(y−x)`.
- At `P(a,b)` with gradient 2, use **both** the derivative and the fact that P is on the curve: `2a+b=12`, `4a²+b²−2ab=24a`.
- **Official reference answer:** `P=(2,8)`; reject `(6,0)` because `b>0`.

### P4 Q5 - vector-line intersection [setup reached; reference completion]
- Equate each x-, y- and z-component of the two line equations.
- The lesson reached `λ=−9`, `μ=−3`.
- **Official reference:** `β=−40`, `P=(−7,−37,−15)`.

### P4 Q6 - trigonometric substitution [through power split; reference completion]
- Use `sin 2θ=2sinθcosθ`, `u=3+cosθ`, `du=−sinθ dθ`, and `cosθ=u−3`.
- Transform limits in order: `θ:0→π/2` becomes `u:4→3`.
- Reached form: `−2∫₄³(u^(1/2)−3u^(−1/2))du`.
- **Official reference:** `8√3−40/3`, so `a=8`, `b=−40/3`.

### Prior P3 review - range and inverse domain [not a P4 paper question]
- Rewrite `(3+5x)/(x+2)` as `5−7/(x+2)`.
- With `x>−2`, the range is `y<5`; therefore the inverse domain is `x<5`.

### P4 Q8 - separable differential equation [self-assessed gap; reference only]
- Integrate `dV/dt=12te^(−t)` and apply `V(0)=6`.
- **Answer:** `V=18−12te^(−t)−12e^(−t)`.
- For `t≥0`, `V<18<20`, so capacity 20 is never reached.

## Status key

- **Reached:** the furthest point actually worked live.
- **Reference completion:** official result retained for checking, not completed aloud.
- **Self-assessed gap:** named as a gap but not taught in the lesson.
- **Prior P3 review:** revisited material, not an October 2025 P4 question.
"""
write(ROOT / "harry_p4_recall.md", recall_md)

def recall_to_html(md: str) -> str:
    out, in_list = [], False
    for raw in md.splitlines():
        line = html.escape(raw).replace('**', '').replace('`', '')
        if raw.startswith('- '):
            if not in_list:
                out.append('<ul>'); in_list = True
            out.append(f'<li>{line[2:]}</li>')
            continue
        if in_list:
            out.append('</ul>'); in_list = False
        if not raw.strip():
            continue
        if raw.startswith('# '): out.append(f'<h1>{line[2:]}</h1>')
        elif raw.startswith('## '): out.append(f'<h2>{line[3:]}</h2>')
        elif raw.startswith('### '): out.append(f'<h3>{line[4:]}</h3>')
        else: out.append(f'<p>{line}</p>')
    if in_list: out.append('</ul>')
    return ''.join(out)

recall_body = recall_to_html(recall_md)
recall_css = CSS.replace("mjx-container { display:block !important; width:100% !important; max-width:100%; overflow-x:auto; overflow-y:hidden; vertical-align:middle; } mjx-container > svg { max-width:100% !important; height:auto !important; } mjx-assistive-mml { max-width:1px !important; overflow:hidden !important; } ", "")
recall_html = f"""<!doctype html><html><head><meta charset="utf-8"><title>26 June P4 recall sheet</title><style>{recall_css} section{{margin:0 0 14px}} h1{{color:#0c6675}} @page{{size:A4;margin:14mm}} @media print {{ h3{{break-after:avoid}} ul{{break-inside:avoid}} main{{font-size:15px;line-height:1.42}} li{{line-height:1.34}} h3{{font-size:18px}} }}</style></head><body><main>{recall_body}</main></body></html>"""
write(ROOT / "harry_p4_recall.html", recall_html)

config = """<script>window.MathJax={tex:{inlineMath:[['\\\\(','\\\\)'],['$','$']]},svg:{fontCache:'local'}};</script><script defer src=\"../assets/mathjax/tex-svg.js\"></script>"""
for card in cards:
    parts = []
    for i, (heading, expression) in enumerate(card["steps"], 1):
        parts.append(f'<div class="work"><div class="step">Step {i} - {html.escape(heading)}</div><p>{tex(expression)}</p></div>')
    panel_id = f"working-panel-{card['slug']}"
    control_id = f"reveal-working-{card['slug']}"
    reveal_script = f"""<script>document.addEventListener('DOMContentLoaded',function(){{const control=document.getElementById('{control_id}');const panel=document.getElementById('{panel_id}');if(!control||!panel)return;control.addEventListener('click',function(){{const expanded=control.getAttribute('aria-expanded')==='true';panel.hidden=expanded;control.setAttribute('aria-expanded',String(!expanded));control.textContent=expanded?'Reveal working':'Hide working';}});}});</script>"""
    card_html = f"""<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><link rel=\"icon\" href=\"data:,\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>{html.escape(card['title'])}</title><style>{CSS}</style>{config}</head><body><main><div class=\"eyebrow\">26 June study deck · standalone recall</div><h1>{html.escape(card['title'])}<span class=\"marks\">{html.escape(card['marks'])}</span></h1><div class=\"nav\"><a class=\"btn secondary\" href=\"../index.html\">Back to deck</a><a class=\"btn\" href=\"{html.escape(card['slug'])}.png\" download>Download this card as PNG</a></div><div class=\"status\"><strong>STATUS:</strong> {html.escape(card['status'])}</div><h2>Standalone question</h2><p>{html.escape(card['stem'])}</p><div class=\"visual\">{card['visual']}<div class=\"small\">Concept visual - supports the stated method; it does not add a different question or solution.</div></div><h2>Multi-step working</h2><button id=\"{control_id}\" class=\"btn reveal-control\" type=\"button\" aria-controls=\"{panel_id}\" aria-expanded=\"false\">Reveal working</button><section id=\"{panel_id}\" class=\"work-panel\" aria-label=\"Step-by-step working\" hidden>{''.join(parts)}</section><div class=\"answer\"><strong>Recall answer:</strong> {html.escape(card['answer_text'])}</div><div class=\"boundary\"><strong>Study boundary:</strong> Use the status above when reviewing. The card is self-contained, while the status records whether a final result was reached live or is official-reference completion.</div></main>{reveal_script}</body></html>"""
    write(ROOT / "cards" / f"{card['slug']}.html", card_html)

landing_tiles=[]
for c in cards:
    landing_tiles.append(f"<article class=\"tile\"><h2>{html.escape(c['title'])}</h2><span class=\"marks\">{html.escape(c['marks'])}</span><div class=\"status\">{html.escape(c['status'])}</div><a class=\"btn\" href=\"cards/{html.escape(c['slug'])}.html\">Open multi-step card</a><a class=\"btn secondary\" href=\"cards/{html.escape(c['slug'])}.png\" download>PNG</a></article>")
index_html=f"""<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><link rel=\"icon\" href=\"data:,\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>26 June P4 multi-step deck</title><style>{CSS}</style></head><body><main><div class=\"eyebrow\">Local-only learner artifact · 26 June P4</div><h1>Seven standalone multi-step recall cards</h1><p>Work from the question, then reveal the grey method boxes. Every card contains a local status label so that official-reference completion is never presented as work completed aloud.</p><div class=\"legend\"><strong>Study order:</strong> P4 Q4 → Q5 → Q6 → Q1 → Q2 → Q8; use the Prior P3 review card separately. No question that was not discussed is represented as covered.</div><div class=\"nav\"><a class=\"btn\" href=\"harry_p4_recall.md\">Open recall Markdown</a><a class=\"btn secondary\" href=\"harry_p4_recall.pdf\">Open recall PDF</a></div><div class=\"deck\">{''.join(landing_tiles)}</div><p class=\"small\">This local deck is not published. It is bound in the local manifest to the frozen final guide and includes no raw candidate pool, model metadata, personal surnames, recording identifiers or internal-source paths.</p></main></body></html>"""
write(ROOT / "index.html", index_html)

manifest={
 "build":"clean downstream replacement", "publication":"not published; local-only", "authoritative_inputs":{
  "final_guide_pdf":{"relative_path":"guide_v2/revision_guide.pdf","sha256":sha(GUIDE),"expected_sha256":EXPECTED_GUIDE_SHA},
  "guide_text_mirror":{"relative_path":"guide_v2/revision_guide_text.md","sha256":sha(GUIDE_TEXT)},
  "source_register":{"relative_path":"guide_v2/source_register.md","sha256":sha(REGISTER)}},
 "derivatives":{"recall_markdown":"harry_p4_recall.md","recall_pdf":"harry_p4_recall.pdf","landing":"index.html","multi_step_cards":[f"cards/{x['slug']}.html" for x in cards],"pngs":[f"cards/{x['slug']}.png" for x in cards]},
 "coverage":{"total_targets":7,"p4_question_targets":["Q1","Q2","Q4","Q5","Q6","Q8"],"separate_prior_p3_review":1},
 "content_boundary":"Only the frozen final guide, its accessible mirror, and its source register were used; quarantined legacy output was not an input.",
 "qa":"Run qa_clean_downstream.py after PDF and PNG rendering; that report records final file hashes and scan results."
}
write(ROOT / "build_manifest.json", json.dumps(manifest,indent=2)+"\n")
print("Generated clean source artifacts from frozen final guide:", len(cards), "cards")
