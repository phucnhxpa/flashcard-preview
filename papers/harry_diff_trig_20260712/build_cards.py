#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the source-grounded multi-step cards for the Harry 12 Jul 2026
differentiation & trig lesson (P3 June 2024 past paper + segment-1 warm-up drill).

Content is taken verbatim/derived from the FINAL PASSED guide
(guide/harry_2026-07-12_differentiation_trig_revision_guide.tex) and
analysis/gemini_video_evidence.md. On-screen question wording is reproduced from the
gemini ledger. No official WMA13 June-2024 question-paper PDF or mark scheme was in the
source set, so per-part MARKS are NOT shown (they were not captured on the board) and no
tutor solution is invented beyond what the lesson/guide evidence supports.

.why boxes quote only mistakes Phuc actually made on the recording; where no personal
mistake is evidenced a labelled "Common trap" is used instead.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------- shell
HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<script>
window.MathJax = {
  tex: { inlineMath: [['\\(','\\)']], displayMath: [['\\[','\\]']] },
  svg: { fontCache: 'global' }
};
</script>
<script src="mathjax-tex-svg.js" id="MathJax-script" async></script>
<style>
  :root { --green:#1b4d2c; --red:#961414; --ink:#1c1c1c; --grey:#f2f2f2; }
  * { box-sizing:border-box; }
  body { font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Arial,sans-serif;
         color:var(--ink); margin:0; background:#e9ecef; line-height:1.5; }
  .wrap { max-width:940px; margin:0 auto; padding:28px 22px 60px; }
  .export-btn { position:fixed; top:16px; right:16px; z-index:100; background:#000; color:#fff;
         border:none; padding:8px 16px; border-radius:8px; font-weight:600; font-size:12px;
         font-family:inherit; cursor:pointer; }
  .meta { font-size:12px; color:#555; letter-spacing:.02em; text-transform:uppercase; margin-bottom:6px; }
  .subject-tag { display:inline-block; background:var(--green); color:#fff; font-size:11px; font-weight:700;
         padding:3px 9px; border-radius:5px; letter-spacing:.03em; margin-bottom:10px; }
  .subject-tag.board { background:#8a5a00; }
  h1 { font-size:22px; margin:2px 0 4px; color:var(--green); }
  .q-header { background:#fff; border:1px solid #d8dde2; border-left:5px solid var(--green);
         border-radius:8px; padding:16px 18px; margin:12px 0 18px; }
  .q-header .marks { float:right; font-weight:700; color:var(--green); }
  .q-source { font-size:12px; color:#666; margin-top:8px; border-top:1px dashed #ccc; padding-top:8px; }
  .status-banner { background:#fff4e0; border:1px solid #e0b060; border-radius:8px; padding:12px 16px;
         margin:14px 0; font-size:14px; }
  .status-banner b { color:#8a5a00; }
  .part { margin:22px 0 8px; }
  .part-head { background:var(--green); color:#fff; border-radius:7px 7px 0 0; padding:9px 14px;
         font-weight:700; font-size:15px; display:flex; justify-content:space-between; align-items:center; }
  .part-head .pm { font-size:12px; font-weight:600; opacity:.92; }
  .carry-in { background:#eef4ff; border:1px solid #b9cdf0; border-top:none; padding:10px 14px;
         font-size:13.5px; }
  .carry-in .lab { font-weight:700; color:#1f5fa8; text-transform:uppercase; font-size:11px;
         letter-spacing:.04em; margin-right:6px; }
  .work { background:var(--grey); border:1px solid #d3d7db; border-top:none; border-radius:0 0 7px 7px;
         padding:8px 14px 14px; position:relative; transition:filter .15s; }
  .work.masked { filter:blur(7px); }
  .mask-toggle { float:right; font-size:11px; color:#666; cursor:pointer; border:1px solid #c4c8cc;
         background:#fff; border-radius:4px; padding:2px 8px; margin:6px 0 0; user-select:none; }
  .step { margin:12px 0; padding-left:12px; border-left:2px solid #cfd4d8; }
  .step-label { font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.05em;
         color:var(--green); margin-bottom:2px; }
  .step-label.chk { color:#7a5b00; }
  .why { background:#fff0f0; border:1px solid #e3b3b3; border-left:4px solid var(--red);
         border-radius:6px; padding:10px 14px; margin:10px 0; font-size:13.5px; }
  .why .lab { font-weight:700; color:var(--red); }
  .trap { background:#fbf6e8; border:1px solid #d9c98a; border-left:4px solid #b08900;
         border-radius:6px; padding:10px 14px; margin:10px 0; font-size:13.5px; }
  .trap .lab { font-weight:700; color:#8a5a00; }
  .good { background:#eef7f0; border:1px solid #b6d8c1; border-left:4px solid var(--green);
         border-radius:6px; padding:10px 14px; margin:10px 0; font-size:13.5px; }
  .good .lab { font-weight:700; color:var(--green); }
  .answer { background:#e8f3ec; border:1px solid #9cc6ab; border-radius:6px; padding:8px 13px;
         margin:10px 0 2px; font-weight:600; }
  .q-diagram { text-align:center; margin:12px 0; }
  .q-diagram img { max-width:380px; width:100%; height:auto; border-radius:6px; margin:8px auto;
         display:block; box-shadow:0 1px 3px rgba(0,0,0,0.08); }
  .q-diagram .cap { font-size:12px; color:#555; margin-top:2px; }
  .drill { width:100%; border-collapse:collapse; font-size:13.5px; margin:6px 0; }
  .drill th, .drill td { border:1px solid #d3d7db; padding:5px 9px; text-align:left; }
  .drill th { background:#eef4ee; color:var(--green); }
  .foot { margin-top:30px; font-size:11.5px; color:#777; border-top:1px solid #ccc; padding-top:10px; }
  mjx-container[display="true"] svg { max-width:100%!important; height:auto!important; }
</style>
</head>
<body>
<button class="export-btn" onclick="exportPNG()">Export PNG</button>
<div class="wrap">
<script>
  function exportPNG() {
    var png = location.pathname.split('/').pop().replace(/\.html$/, '.png');
    window.open(png, '_blank');
  }
  function toggleMask(el) {
    var box = el.parentElement;
    box.classList.toggle('masked');
    el.textContent = box.classList.contains('masked') ? 'Show working' : 'Hide working';
  }
</script>
"""

FOOT = """
</div>
</body>
</html>
"""

META = '<div class="meta">Harry &rarr; Phuc &bull; 12 July 2026 tutorial</div>'


# --------------------------------------------------------------- html helpers
def tag(txt, cls=""):
    return f'<span class="subject-tag {cls}">{txt}</span>'


def qheader(intro, parts_line="", source=""):
    src = f'<div class="q-source">{source}</div>' if source else ""
    body = intro + (f" {parts_line}" if parts_line else "")
    return f'<div class="q-header">{body}{src}</div>'


def banner(html):
    return f'<div class="status-banner">{html}</div>'


def diagram(img, cap):
    return (f'<div class="q-diagram"><img src="{img}" alt="diagram">'
            f'<div class="cap">{cap}</div></div>')


def step(label, body, chk=False):
    cl = "step-label chk" if chk else "step-label"
    return f'<div class="step"><div class="{cl}">{label}</div>{body}</div>'


def answer(html):
    return f'<div class="answer">{html}</div>'


def work(steps):
    inner = "".join(steps)
    return ('<div class="work"><span class="mask-toggle" '
            'onclick="toggleMask(this)">Hide working</span>' + inner + "</div>")


def part(head, inner, pm="", carry=""):
    pm_html = f'<span class="pm">{pm}</span>' if pm else ""
    carry_html = ""
    if carry:
        carry_html = (f'<div class="carry-in"><div><span class="lab">Carry-in</span>'
                      f'{carry}</div></div>')
    return (f'<div class="part"><div class="part-head"><span>{head}</span>{pm_html}</div>'
            f'{carry_html}{inner}</div>')


def why(lab, body):
    return f'<div class="why"><span class="lab">{lab}</span> {body}</div>'


def trap(body, lab="Common trap:"):
    return f'<div class="trap"><span class="lab">{lab}</span> {body}</div>'


def good(lab, body):
    return f'<div class="good"><span class="lab">{lab}</span> {body}</div>'


def foot(html):
    return f'<div class="foot">{html}</div>'


def build(slug, title, body_inner):
    html = HEAD.replace("__TITLE__", title) + body_inner + FOOT
    path = os.path.join(OUT, slug + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {slug}.html  ({len(html)//1024} KB)")


NOMARKS = ("Source: Pearson Edexcel IAL Pure Mathematics P3 (WMA13/01), <b>June 2024</b> paper, "
           "as displayed on-screen by the tutor and reproduced from the lesson recording "
           "(<code>analysis/gemini_video_evidence.md</code>) and the final revision guide. "
           "No official question-paper PDF or mark scheme was in the source set, so per-part "
           "marks are not shown.")


# ===========================================================================
# CARD 1 — Warm-up recall drill (segment 1): derivatives + identities
# ===========================================================================
def card_warmup():
    slug = "Warmup_derivatives_identities"
    title = "Warm-up — exponential/log & trig derivatives + identity recall"

    header = qheader(
        "<b>Warm-up recall drill (lesson segment 1).</b> Harry opened by writing two "
        "differentiation rules on the board, then ran a rapid fluency set and quizzed the "
        "reciprocal-trig derivatives and the standard identities cold "
        "(<i>&ldquo;it's really important that you have all of that memorised&rdquo;</i>). "
        "The double-angle work here is the toolkit that Q4 of the paper depends on.",
        source=("Source: tutorial recording, segment 1 "
                "(<code>analysis/gemini_video_evidence.md</code>, guide &sect;3&ndash;&sect;5). "
                "This is a formula-recall drill, not an exam question &mdash; no marks apply."))

    # -- Part A: the two rules + numerical set
    rulesA = work([
        step("Rule &middot; where is the variable?",
             r"If the variable is in the <b>power</b> (not the base), the power rule does "
             r"not apply. Differentiating leaves \(a^{x}\) unchanged and brings down \(\ln a\):"
             r"\[ \frac{d}{dx}\bigl(a^{x}\bigr)=a^{x}\ln a, \qquad "
             r"\frac{d}{dx}\bigl(a^{kx}\bigr)=k\,a^{kx}\ln a. \]"),
        step("Rule &middot; natural log of a function",
             r"<i>&ldquo;Differentiate the argument, and that goes on the top.&rdquo;</i> "
             r"\[ \frac{d}{dx}\bigl(\ln f(x)\bigr)=\frac{f'(x)}{f(x)}\quad (f(x)>0), "
             r"\qquad \frac{d}{dx}(e^{x})=e^{x},\quad \frac{d}{dx}(e^{kx})=k\,e^{kx}. \]"),
        step("Drill &middot; the board set (all answered by Phuc)",
             r"""<table class="drill">
<tr><th>Differentiate</th><th>Answer</th><th>Why</th></tr>
<tr><td>\(3^{x}\)</td><td>\(3^{x}\ln 3\)</td><td>\(a^{x}\) rule</td></tr>
<tr><td>\(x^{3}\)</td><td>\(3x^{2}\)</td><td>power rule &mdash; contrast with \(a^x\)</td></tr>
<tr><td>\(\ln 3x\)</td><td>\(\dfrac{3}{3x}=\dfrac1x\)</td><td>\(f'=3\) on top; the \(3\) cancels</td></tr>
<tr><td>\(\ln(x^{2}+3x+5)\)</td><td>\(\dfrac{2x+3}{x^{2}+3x+5}\)</td><td>\(\tfrac{f'}{f}\) rule</td></tr>
<tr><td>\(3^{2x}\)</td><td>\(2\cdot 3^{2x}\ln 3\)</td><td>\(a^{kx}\) rule, \(k=2\)</td></tr>
<tr><td>\(2^{3x}\)</td><td>\(3\cdot 2^{3x}\ln 2\)</td><td>\(a^{kx}\) rule, \(k=3\)</td></tr>
<tr><td>\(5\ln x\)</td><td>\(\dfrac{5}{x}\)</td><td>constant \(\times\tfrac1x\)</td></tr>
<tr><td>\(5\ln 2x\)</td><td>\(\dfrac{5}{x}\)</td><td>\(5\cdot\tfrac{2}{2x}=\tfrac5x\)</td></tr>
<tr><td>\(9^{t}\)</td><td>\(9^{t}\ln 9=2\cdot 9^{t}\ln 3\)</td><td>\(\ln 9=2\ln 3\)</td></tr>
<tr><td>\(3e^{2x}\)</td><td>\(6e^{2x}\)</td><td>\(3\cdot 2\cdot e^{2x}\)</td></tr>
<tr><td>\(e^{-x}\)</td><td>\(-e^{-x}\)</td><td>\(e^{kx}\) rule, \(k=-1\)</td></tr>
</table>"""),
        step("Sense check", r"For \(\ln(kx)\) the answer is always \(\tfrac{k}{kx}=\tfrac1x\): "
             r"the constant inside the log cancels, so \(\ln 3x\) and \(\ln 6x\) both give "
             r"\(\tfrac1x\).", chk=True),
    ])
    partA = part("Part A &middot; Exponential / log derivatives", rulesA,
                 pm="rules + fluency set")
    whyA = why("Phuc's slips (recorded):",
               r"Phuc's first attempt at \(\tfrac{d}{dx}(a^{x})\) was \(x\,a^{x-1}\) &mdash; the "
               r"<b>power rule misapplied</b>. Harry's fix: check <b>where the variable is</b> "
               r"(base &rarr; power rule; power &rarr; \(a^{x}\ln a\)). Phuc also wrote "
               r"\(\tfrac{1}{3x}\) for \(\tfrac{d}{dx}(\ln 3x)\) (missing the \(f'=3\) on top) "
               r"and \(5\cdot\tfrac{10}{2x}\) for \(\tfrac{d}{dx}(5\ln 2x)\).")

    # -- Part B: trig derivative table
    tableB = work([
        step("Fill the six derivatives",
             r"""<table class="drill">
<tr><th>\(y\)</th><th>\(\dfrac{dy}{dx}\)</th><th>Sign / memory hook</th></tr>
<tr><td>\(\sin x\)</td><td>\(+\cos x\)</td><td>pattern position 1: \(+\)</td></tr>
<tr><td>\(\cos x\)</td><td>\(-\sin x\)</td><td>pattern position 2: \(-\)</td></tr>
<tr><td>\(\tan x\)</td><td>\(+\sec^{2}x\)</td><td>links to \(1+\tan^2x=\sec^2x\)</td></tr>
<tr><td>\(\operatorname{cosec} x\)</td><td>\(-\operatorname{cosec} x\cot x\)</td><td>pattern position 4: \(-\)</td></tr>
<tr><td>\(\sec x\)</td><td>\(+\sec x\tan x\)</td><td>mirror of the \(\operatorname{cosec}\) derivative</td></tr>
<tr><td>\(\cot x\)</td><td>\(-\operatorname{cosec}^{2}x\)</td><td>links to \(1+\cot^2x=\operatorname{cosec}^2x\)</td></tr>
</table>"""),
        step("Harry's sign pattern",
             r"Written in the order \(\sin,\cos,\tan,\ \operatorname{cosec},\sec,\cot\), the "
             r"derivative signs run \[+\ \ -\ \ +\ \ -\ \ +\ \ -.\]"),
        step("Derivative &harr; identity link",
             r"\(\tfrac{d}{dx}(\tan x)=\sec^2x\) should remind you of \(1+\tan^2x=\sec^2x\); "
             r"likewise \(\tfrac{d}{dx}(\cot x)=-\operatorname{cosec}^2x\) pairs with "
             r"\(1+\cot^2x=\operatorname{cosec}^2x\).", chk=True),
    ])
    partB = part("Part B &middot; Reciprocal-trig derivative table", tableB,
                 pm="6 derivatives + pattern")
    whyB = why("Phuc's slip (recorded):",
               r"Phuc wrote \(\cos x\) for \(\tfrac{d}{dx}(\sin x)\) but <b>omitted the sign</b>, "
               r"and wrote &ldquo;\(\pm\)&rdquo; for \(\tfrac{d}{dx}(\cos x)\): "
               r"<i>&ldquo;I usually confuse about the plus minus, I don't remember which "
               r"one.&rdquo;</i> The \(+\,-\,+\,-\,+\,-\) pattern is Harry's remedy.")

    # -- Part C: identity recall + cos 2A
    idsC = work([
        step("Reciprocal identities",
             r"\[ \tan A=\frac{\sin A}{\cos A},\quad \operatorname{cosec} A=\frac{1}{\sin A},"
             r"\quad \sec A=\frac{1}{\cos A},\quad \cot A=\frac{1}{\tan A}. \]"
             r"Harry's hook: <i>&ldquo;cosec is one over sine &hellip; the third letter&rdquo;</i> "
             r"&mdash; the third letter of co<b>s</b>ec matches \(\sin\), of <b>se</b>c matches \(\cos\)."),
        step("Pythagorean identities",
             r"\[ \sin^{2}A+\cos^{2}A=1,\quad 1+\tan^{2}A=\sec^{2}A,\quad "
             r"1+\cot^{2}A=\operatorname{cosec}^{2}A. \]"),
        step("Double-angle identities",
             r"\[ \sin 2A=2\sin A\cos A, \]"
             r"\[ \cos 2A=\cos^{2}A-\sin^{2}A=1-2\sin^{2}A=2\cos^{2}A-1. \]"),
        step("How the three \\(\\cos 2A\\) forms connect (understanding only)",
             r"Start from \(\cos 2A=\cos^2A-\sin^2A\) (cosine first). Replace "
             r"\(\cos^2A=1-\sin^2A\Rightarrow 1-2\sin^2A\); replace "
             r"\(\sin^2A=1-\cos^2A\Rightarrow 2\cos^2A-1\)."),
        step("Sense check",
             r"<i>&ldquo;Memorise these three forms rather than deriving them during the "
             r"exam&rdquo;</i> &mdash; deriving costs time; this is prime flashcard material.", chk=True),
    ])
    partC = part("Part C &middot; Trig identity recall", idsC,
                 pm="reciprocal + Pythagorean + double-angle")
    whyC = why("Phuc's slips (recorded):",
               r"For \(1+\tan^2A\) Phuc answered \(\cot^2A\); Harry corrected it to \(\sec^2A\). "
               r"For \(\cos 2A\) he first reached for \(\sin(A+B)\), then wrote it in the wrong "
               r"order as \(\sin^2A-\cos^2A\) and \(\cos^2A-2\sin^2A\). <b>Order matters:</b> "
               r"it is \(\cos^2A-\sin^2A\), cosine first.")

    body = (META + tag("P3 warm-up &mdash; segment 1") +
            "<h1>Warm-up &middot; exp/log &amp; trig derivatives + identity recall</h1>" +
            header +
            banner("<b>Status:</b> recall drill, fully completed on the board (all items "
                   "Solved). Algebra-only fluency work &mdash; no diagram needed. The "
                   "double-angle identities in Part&nbsp;C feed straight into paper Q4.") +
            partA + whyA + partB + whyB + partC + whyC +
            foot("Segment-1 warm-up. Every row/derivative/identity above was set by Harry and "
                 "answered by Phuc on the shared board; wording and the recorded slips trace to "
                 "<code>analysis/gemini_video_evidence.md</code> and guide &sect;3&ndash;&sect;5."))
    build(slug, title, body)


# ===========================================================================
# CARD 2 — Q1 modulus function
# ===========================================================================
def card_q1():
    slug = "P3_Jun2024_Q1"
    title = "P3 June 2024 Q1 — modulus function: vertex, inequality, transformation"

    header = qheader(
        "<b>Question 1.</b> Figure&nbsp;1 shows a sketch of the graph with equation "
        "\\(y=f(x)\\) where \\(f(x)=2|x-5|+10\\). The point \\(P\\), shown in Figure&nbsp;1, "
        "is the vertex of the graph.",
        parts_line=("<b>(a)</b> State the coordinates of \\(P\\). &nbsp; "
                    "<b>(b)</b> Use algebra to solve \\(2|x-5|+10>6x\\) "
                    "(solutions relying on calculator technology are not acceptable). &nbsp; "
                    "<b>(c)</b> Find the point to which \\(P\\) is mapped when the graph "
                    "\\(y=f(x)\\) is transformed to the graph \\(y=3f(x-2)\\)."),
        source=NOMARKS)

    dia = diagram("q1_modulus.png",
                  r"The V-graph \(y=2|x-5|+10\): left branch \(y=-2x+20\), right branch "
                  r"\(y=2x\), vertex \(P=(5,10)\). \(f(x)>6x\) on the left branch, up to "
                  r"\(A\) where \(6x=-2x+20\Rightarrow x=\tfrac52\).")

    # (a)
    a = work([
        step("Strategy", r"Split the modulus into its two branches, then read off / substitute "
             r"to get the vertex."),
        step("Working &middot; piecewise form",
             r"\[ f(x)=\begin{cases} 2x, & x\ge 5\ (\text{since } 2(x-5)+10=2x),\\ "
             r"-2x+20, & x<5\ (\text{since } -2(x-5)+10=-2x+20). \end{cases} \]"),
        step("Substitute the vertex \\(x=5\\)",
             r"\[ f(5)=2|5-5|+10=2|0|+10=10 \;\Rightarrow\; P=(5,10). \]"),
        step("Result", answer(r"\( P=(5,\,10) \)")),
        step("Shortcut Harry gave",
             r"The vertex of \(y=a|x-h|+k\) is \((h,k)\), so \(f(x)=2|x-5|+10\) has vertex "
             r"\((5,10)\) directly.", chk=True),
    ])
    partA = part("Part (a) &middot; Coordinates of \\(P\\)", a, pm="Solved")
    goodA = good("Phuc did this well (recorded):",
                 r"Phuc derived the piecewise function and marked \(x=5\) at the vertex, then "
                 r"substituted \(x=5\) into \(f(x)=2|x-5|+10\) to get \(f(5)=10\) &mdash; correct.")

    # (b)
    b = work([
        step("Strategy",
             r"Think graphically first to pick the right branch, then solve by algebra "
             r"(the calculator is not allowed here). Sketch \(y=6x\): it is steeper than the "
             r"right branch \(y=2x\), so \(f(x)>6x\) only on the <b>left</b> branch."),
        step("Working &middot; intersect the left branch with \\(y=6x\\)",
             r"\[ 6x=-2x+20 \;\Rightarrow\; 8x=20 \;\Rightarrow\; x=\frac{20}{8}=\frac52. \]"),
        step("Read off the region",
             r"To the left of this intersection the V-graph is above \(y=6x\); to the right it "
             r"drops below. Hence the solution set."),
        step("Result", answer(r"\( x<\dfrac52 \)")),
        step("Sense check",
             r"At \(x=0\): \(f(0)=20>0=6x\) ✓ (inside); at \(x=3\): \(f(3)=14<18=6x\) ✗ "
             r"(outside). Boundary \(x=\tfrac52\) is where they are equal.", chk=True),
    ])
    partB = part("Part (b) &middot; Solve \\(2|x-5|+10>6x\\) by algebra", b,
                 pm="Solved", carry=r"From (a): vertex \(P=(5,10)\); right branch \(y=2x\), "
                 r"left branch \(y=-2x+20\).")
    whyB = why("Phuc's slips (recorded):",
               r"Phuc made an earlier numerical error and also solved an <b>unnecessary second "
               r"case</b> (the right branch). Harry's point: a quick sketch of \(y=6x\) against "
               r"the V shows only the left branch can exceed \(6x\), so only "
               r"\(6x=-2x+20\) needs solving.")

    # (c)
    c = work([
        step("Strategy",
             r"Apply the two transformations in \(y=3f(x-2)\) to the vertex only: the "
             r"\((x-2)\) shifts right, the outer factor \(3\) stretches vertically."),
        step("Working &middot; horizontal shift",
             r"\(x-2\) replaces \(x\): the graph moves <b>right</b> by \(2\), so the "
             r"\(x\)-coordinate \(5\to 5+2=7\)."),
        step("Working &middot; vertical stretch",
             r"The factor \(3\) multiplies \(y\): the \(y\)-coordinate \(10\to 3\times 10=30\)."),
        step("Result", answer(r"\( P'=(7,\,30) \)")),
        step("Sense check",
             r"Order is independent here: the horizontal translation acts on \(x\), the "
             r"vertical stretch on \(y\), so \((5,10)\to(7,30)\).", chk=True),
    ])
    partC = part("Part (c) &middot; Image of \\(P\\) under \\(y=3f(x-2)\\)", c,
                 pm="Solved", carry=r"From (a): \(P=(5,10)\).")
    goodC = good("Phuc did this (recorded):",
                 r"This was a part Phuc had previously left blank; with the transformation rules "
                 r"\((x-2)\Rightarrow\) right \(2\) and \(3f\Rightarrow\) \(y\)-stretch \(3\), "
                 r"he reached \((7,30)\).")

    tip = trap(r"if you cannot do an early part (e.g. finding \(P\)), <b>invent</b> a plausible "
               r"value and carry it forward &mdash; you can still earn full method marks on the "
               r"later part. Harry stressed this twice in the lesson.",
               lab="Exam tip Harry stressed:")

    body = (META + tag("P3 WMA13/01 &mdash; June 2024 &mdash; Q1") +
            "<h1>Q1 &middot; Modulus \\(f(x)=2|x-5|+10\\): vertex, inequality, transformation</h1>" +
            header + dia +
            banner("<b>Status:</b> fully worked in the lesson &mdash; \\(P=(5,10)\\), "
                   "\\(x&lt;\\tfrac52\\), image \\((7,30)\\).") +
            partA + goodA + partB + whyB + partC + goodC + tip +
            foot("Q1 fully worked in the lesson. On-screen wording reproduced from "
                 "<code>analysis/gemini_video_evidence.md</code> (01:02&ndash;13:13, segment&nbsp;2); "
                 "solution matches guide &sect;6.1. Marks per part were not shown on the board."))
    build(slug, title, body)


# ===========================================================================
# CARD 3 — Q2 algebraic division + integration
# ===========================================================================
def card_q2():
    slug = "P3_Jun2024_Q2"
    title = "P3 June 2024 Q2 — algebraic division then a definite integral"

    header = qheader(
        "<b>Question 2.</b> \\(g(x)=\\dfrac{2x^{2}-5x+8}{x-2}\\).",
        parts_line=("<b>(a)</b> Write \\(g(x)\\) in the form \\(Ax+B+\\dfrac{C}{x-2}\\), where "
                    "\\(A\\), \\(B\\) and \\(C\\) are integers to be found. &nbsp; "
                    "<b>(b)</b> Show that \\(\\displaystyle\\int_{4}^{8} g(x)\\,dx=\\alpha+\\beta\\ln 3\\), "
                    "where \\(\\alpha\\) and \\(\\beta\\) are integers to be found."),
        source=NOMARKS)

    # (a) two methods
    a = work([
        step("Strategy", r"Two equivalent routes. <b>Method 1</b> polynomial long division "
             r"(Harry's preferred, for speed); <b>Method 2</b> the identity / substitution "
             r"method as a cross-check."),
        step("Method 1 &middot; long division",
             r"Divide \(2x^{2}-5x+8\) by \(x-2\):"
             r"\[ 2x^{2}\div x=2x;\quad 2x(x-2)=2x^{2}-4x;\quad (-5x)-(-4x)=-x. \]"
             r"\[ -x\div x=-1;\quad -1(x-2)=-x+2;\quad 8-2=6\ (\text{remainder}). \]"
             r"\[ g(x)=2x-1+\frac{6}{x-2}. \]"),
        step("Method 2 &middot; identity / substitution",
             r"Multiply up: \(2x^{2}-5x+8\equiv(Ax+B)(x-2)+C\). Then"
             r"\[ x=2:\ 8-10+8=C\Rightarrow C=6; \]"
             r"\[ x=0:\ 8=-2B+6\Rightarrow B=-1;\qquad x=1:\ 5=-(A-1)+6\Rightarrow A=2. \]"),
        step("Result", answer(r"\( g(x)=2x-1+\dfrac{6}{x-2},\qquad A=2,\ B=-1,\ C=6. \)")),
        step("Sense check",
             r"Both methods agree. Quick check at \(x=3\): LHS \(\tfrac{18-15+8}{1}=11\); RHS "
             r"\(6-1+6=11\) ✓.", chk=True),
    ])
    partA = part("Part (a) &middot; Write \\(g(x)=Ax+B+\\dfrac{C}{x-2}\\)  (two methods)", a,
                 pm="Solved")
    whyA = why("Phuc's slips (recorded):",
               r"In the division Phuc computed \((-5x)-(-4x)\) as \(-9x\) instead of \(-x\). "
               r"Harry's rule: <b>always bracket the term you subtract</b> &mdash; "
               r"\((-5x)-(-4x)=-5x+4x=-x\). Phuc also mis-wrote the answer as "
               r"\(\tfrac{(x-2)(2x-1)+6}{x-2}\); the remainder \(6\) alone sits over \((x-2)\).")

    # (b)
    b = work([
        step("Strategy",
             r"Integrate the part-(a) form term by term. The key fact from the warm-up: "
             r"\(\int\tfrac{k}{x-2}\,dx=k\ln|x-2|\), because "
             r"\(\tfrac{d}{dx}\bigl(6\ln|x-2|\bigr)=\tfrac{6}{x-2}\)."),
        step("Formula &middot; antiderivative",
             r"\[ \int\!\Bigl(2x-1+\tfrac{6}{x-2}\Bigr)dx=x^{2}-x+6\ln|x-2|+C. \]"),
        step("Substitute the limits \\(4\\) and \\(8\\)",
             r"\[ \Bigl[x^{2}-x+6\ln|x-2|\Bigr]_{4}^{8} "
             r"=\bigl(64-8+6\ln 6\bigr)-\bigl(16-4+6\ln 2\bigr). \]"),
        step("Working &middot; simplify with the log law",
             r"\[ =(56-12)+6(\ln 6-\ln 2)=44+6\ln\tfrac{6}{2}=44+6\ln 3. \]"
             r"(The modulus signs drop because \(6,2>0\).)"),
        step("Result", answer(r"\( \displaystyle\int_{4}^{8} g(x)\,dx=44+6\ln 3, "
                              r"\qquad \alpha=44,\ \beta=6. \)")),
        step("Sense check",
             r"\(\ln 6-\ln 2=\ln\tfrac62=\ln 3\) is the quotient log law; the polynomial part "
             r"\(x^2-x\) contributes \(56-12=44\).", chk=True),
    ])
    partB = part("Part (b) &middot; Show \\(\\int_{4}^{8} g(x)\\,dx=\\alpha+\\beta\\ln 3\\)", b,
                 pm="Solved",
                 carry=r"From (a): \(g(x)=2x-1+\dfrac{6}{x-2}\), so "
                 r"\(\int g\,dx=x^{2}-x+6\ln|x-2|\).")
    whyB = why("Phuc's slip (recorded):",
               r"Phuc paused on \(\int\tfrac{6}{x-2}\,dx\) &mdash; recognising it as a "
               r"\(\ln\)-type integral \(6\ln|x-2|\) was the sticking point; and he used square "
               r"brackets \(\bigl[\ \bigr]_{4}^{8}\) for the definite-integral evaluation, which "
               r"is the correct notation.")

    body = (META + tag("P3 WMA13/01 &mdash; June 2024 &mdash; Q2") +
            "<h1>Q2 &middot; Algebraic division of \\(\\tfrac{2x^{2}-5x+8}{x-2}\\), then integrate</h1>" +
            header +
            banner("<b>Status:</b> fully worked in the lesson &mdash; \\(A=2,\\ B=-1,\\ C=6\\); "
                   "\\(\\int_{4}^{8} g\\,dx=44+6\\ln 3\\). "
                   "<b>Algebra-only</b> question &mdash; no diagram needed.") +
            partA + whyA + partB + whyB +
            foot("Q2 fully worked across segments&nbsp;2&ndash;3. Wording reproduced from "
                 "<code>analysis/gemini_video_evidence.md</code> (14:04&hellip;, segment&nbsp;2 and "
                 "04:46&ndash;12:44, segment&nbsp;3); solution matches guide &sect;6.2. "
                 "The exact \\(\\alpha+\\beta\\ln 3\\) target wording is the board form; per-part "
                 "marks were not shown."))
    build(slug, title, body)


# ===========================================================================
# CARD 4 — Q3 log-log graph (DISCUSSED ONLY)
# ===========================================================================
def card_q3():
    slug = "P3_Jun2024_Q3"
    title = "P3 June 2024 Q3 — log-log graph sketch (discussed only)"

    header = qheader(
        "<b>Question 3.</b> <b>(a)</b> Sketch the graph of \\(\\log_{10} y\\) against "
        "\\(\\log_{10} x\\). Show on your sketch the coordinates of the points of intersection "
        "of the graph with the axes.",
        source=NOMARKS)

    dia = diagram("q3_loglog.png",
                  r"A \(\log\)-\(\log\) linear relationship plots as a straight line; the "
                  r"intercepts are labelled as coordinate pairs \((0,6)\) and \((2,0)\) on the "
                  r"\(\log_{10}y\) vs \(\log_{10}x\) axes.")

    a = work([
        step("What was reviewed (not fully re-worked)",
             r"Harry reviewed Phuc's existing sketch rather than re-deriving it: he called it "
             r"<i>&ldquo;pretty much fine&rdquo;</i> and confirmed the graph was otherwise "
             r"correct. The two teaching points below are what Harry added."),
        step("Point 1 &middot; label intercepts as coordinate pairs",
             r"Write the axis intercepts as \((x,y)\) pairs &mdash; e.g. \((0,6)\) and "
             r"\((2,0)\) &mdash; not as bare numbers on the axes."),
        step("Point 2 &middot; &lsquo;sketch&rsquo; vs &lsquo;plot&rsquo;",
             r"A <b>sketch</b> needs correct shape plus key points only; a <b>plot</b> demands "
             r"an accurate scale. This question says <i>sketch</i>, so shape + labelled "
             r"intercepts suffice."),
        step("Note on the working shown",
             r"The lesson evidence records the review and the two points above, and the "
             r"intercepts \((0,6)\), \((2,0)\); it does not record a full tutor re-derivation of "
             r"the underlying model, so none is reconstructed here.", chk=True),
    ])
    partA = part("Part (a) &middot; Sketch \\(\\log_{10}y\\) vs \\(\\log_{10}x\\)", a,
                 pm="Discussed only")

    trapA = trap(r"a \(\log\)-\(\log\) graph of a power law \(y=ax^{n}\) is a straight line "
                 r"\(\log_{10}y=\log_{10}a+n\log_{10}x\); its intercepts give \(\log_{10}a\) and "
                 r"\(-\tfrac{\log_{10}a}{n}\). Reading intercepts as unlabelled numbers, or "
                 r"drawing a curve instead of a line, loses the marks.",
                 lab="Common trap (general):")

    body = (META + tag("P3 WMA13/01 &mdash; June 2024 &mdash; Q3", "board") +
            "<h1>Q3 &middot; Sketch \\(\\log_{10}y\\) against \\(\\log_{10}x\\)</h1>" +
            header + dia +
            banner("<b>Status: discussed only (not fully re-worked).</b> Harry reviewed Phuc's "
                   "sketch (&ldquo;pretty much fine&rdquo;) and added two points on notation and "
                   "&lsquo;sketch vs plot&rsquo;. No full tutor solution was worked, so none is "
                   "invented; only the evidenced review and the intercepts \\((0,6)\\), "
                   "\\((2,0)\\) are shown.") +
            partA + trapA +
            foot("Q3 is <b>discussed only</b> (guide &sect;6.3; "
                 "<code>analysis/gemini_video_evidence.md</code> 12:44&ndash;13:36, segment&nbsp;3). "
                 "The diagram is a compact teaching reconstruction of the two evidenced "
                 "intercepts on \\(\\log\\)-\\(\\log\\) axes; no derivation beyond the recording "
                 "is asserted."))
    build(slug, title, body)


# ===========================================================================
# CARD 5 — Q4 double angle, R-formula, trig equation
# ===========================================================================
def card_q4():
    slug = "P3_Jun2024_Q4"
    title = "P3 June 2024 Q4 — double angle, R-form, and a trig equation"

    header = qheader(
        "<b>Question 4.</b> \\(f(x)=8\\sin x\\cos x+4\\cos^{2}x-3\\).",
        parts_line=("<b>(a)</b> Write \\(f(x)\\) in the form \\(a\\sin 2x+b\\cos 2x+c\\), where "
                    "\\(a\\), \\(b\\) and \\(c\\) are integers to be found. &nbsp; "
                    "<b>(b)</b> Use the answer to part (a) to write \\(f(x)\\) in the form "
                    "\\(R\\sin(2x+\\alpha)+c\\), where \\(R>0\\) and \\(0<\\alpha<\\tfrac{\\pi}{2}\\); "
                    "give the exact value of \\(R\\) and the value of \\(\\alpha\\) in radians to "
                    "3&nbsp;s.f. &nbsp; <b>(c)(i)</b> Hence state the maximum value of \\(f(x)\\); "
                    "<b>(ii)</b> find the second smallest positive value of \\(x\\) at which the "
                    "maximum occurs (answer to 3&nbsp;s.f.)."),
        source=NOMARKS)

    dia1 = diagram("q4_triangle.png",
                   r"Right triangle for the \(R\)-form: \(R\cos\alpha=4\), \(R\sin\alpha=2\), so "
                   r"\(\tan\alpha=\tfrac12\), \(\alpha=\arctan\tfrac12\approx0.464\) rad, "
                   r"\(R=\sqrt{4^2+2^2}=2\sqrt5\).")

    # (a)
    a = work([
        step("Strategy",
             r"Convert each term to a double-angle form using \(\sin 2x=2\sin x\cos x\) and "
             r"\(\cos 2x=2\cos^2x-1\). <i>&ldquo;You really need to know those trig identities "
             r"to answer that kind of question.&rdquo;</i>"),
        step("Formula &middot; the \\(8\\sin x\\cos x\\) term",
             r"\[ 8\sin x\cos x=4\,(2\sin x\cos x)=4\sin 2x. \]"),
        step("Formula &middot; the \\(4\\cos^{2}x\\) term",
             r"From \(\cos 2x=2\cos^2x-1\Rightarrow 2\cos^2x=\cos 2x+1\), so"
             r"\[ 4\cos^{2}x=2(\cos 2x+1)=2\cos 2x+2. \]"),
        step("Working &middot; combine",
             r"\[ f(x)=4\sin 2x+(2\cos 2x+2)-3=4\sin 2x+2\cos 2x-1. \]"),
        step("Result", answer(r"\( f(x)=4\sin 2x+2\cos 2x-1,\qquad a=4,\ b=2,\ c=-1. \)")),
        step("Sense check",
             r"Check \(x=0\): original \(f(0)=0+4-3=1\); new form \(0+2-1=1\) ✓.", chk=True),
    ])
    partA = part("Part (a) &middot; Write as \\(a\\sin 2x+b\\cos 2x+c\\)", a, pm="Solved")
    whyA = why("Phuc's slips (recorded):",
               r"Phuc first wrote \(\sin 2x\) with an \(A\) rather than \(x\), reached for the "
               r"wrong \(\cos 2x\) forms, <b>over-complicated</b> \(8\sin x\cos x\), and got "
               r"stuck relating \(4\cos^2x\) to \(\cos 2x\). Harry's route: pull the \(4\) out of "
               r"\(8\sin x\cos x\) to see \(4\sin 2x\), and rearrange \(\cos 2x=2\cos^2x-1\) for "
               r"\(4\cos^2x\).")

    # (b)
    b = work([
        step("Strategy",
             r"Only the \(a\sin 2x+b\cos 2x\) part is written in \(R\)-form; the constant "
             r"\(c=-1\) carries straight over. Expand and match coefficients."),
        step("Formula &middot; compound-angle expansion",
             r"\[ R\sin(2x+\alpha)=R\sin 2x\cos\alpha+R\cos 2x\sin\alpha. \]"),
        step("Substitute &middot; match \\(4\\sin 2x+2\\cos 2x\\)",
             r"\[ R\cos\alpha=4,\qquad R\sin\alpha=2. \]"),
        step("Working &middot; \\(\\alpha\\) by dividing",
             r"\[ \tan\alpha=\frac{R\sin\alpha}{R\cos\alpha}=\frac{2}{4}=\frac12 "
             r"\;\Rightarrow\; \alpha=\arctan\tfrac12\approx0.464\ \text{rad (3 s.f.)}. \]"),
        step("Working &middot; \\(R\\) exactly, by squaring and adding",
             r"\[ R^{2}=(R\cos\alpha)^2+(R\sin\alpha)^2=4^{2}+2^{2}=20 "
             r"\;\Rightarrow\; R=\sqrt{20}=2\sqrt5\ (\text{exact}). \]"),
        step("Result", answer(r"\( f(x)=2\sqrt5\,\sin(2x+\alpha)-1,\quad R=2\sqrt5,\ "
                              r"\alpha=\arctan\tfrac12\approx0.464\ \text{rad}. \)")),
        step("Sense check",
             r"\(0<\alpha<\tfrac\pi2\) ✓ (both \(R\cos\alpha,\,R\sin\alpha>0\)); the rounded "
             r"\(0.464\) is a 3-s.f. approximation, not an exact value.", chk=True),
    ])
    partB = part("Part (b) &middot; Write as \\(R\\sin(2x+\\alpha)+c\\)", b, pm="Solved",
                 carry=r"From (a): \(f(x)=4\sin 2x+2\cos 2x-1\), so match \(R\sin(2x+\alpha)\) "
                 r"to \(4\sin 2x+2\cos 2x\) and carry \(c=-1\).")
    whyB = why("Phuc's slip (recorded):",
               r"Phuc wrote \(R=4.472\). <b>Harry:</b> <i>&ldquo;This would be wrong because we "
               r"want the <u>exact</u> value of \(R\), not a decimal. Exact, no decimals "
               r"allowed&rdquo;</i> \(\Rightarrow R=2\sqrt5\). Also check the question: \(\alpha\) "
               r"is wanted in <b>radians, to 3&nbsp;s.f.</b>")

    # (c)(i)
    ci = work([
        step("Strategy", r"\(\sin(\cdot)\) has maximum \(1\); substitute into the \(R\)-form."),
        step("Substitute the maximum of sine",
             r"\[ f_{\max}=2\sqrt5\,(1)-1=2\sqrt5-1\ (\text{exact}). \]"),
        step("Result", answer(r"\( f_{\max}=2\sqrt5-1 \)")),
    ])
    partCi = part("Part (c)(i) &middot; Maximum value of \\(f(x)\\)", ci, pm="Solved",
                  carry=r"From (b): \(f(x)=2\sqrt5\,\sin(2x+\alpha)-1\).")
    goodCi = good("Phuc did this well (recorded):",
                  r"Phuc correctly took \(\sin=1\) to give the maximum \(2\sqrt5-1\).")

    # (c)(ii)
    cii = work([
        step("Strategy",
             r"The maximum occurs when \(\sin(2x+\alpha)=1\). Write down all solutions for the "
             r"<b>whole angle</b> \(2x+\alpha\) first, then rearrange for \(x\)."),
        step("Formula &middot; where \\(\\sin=1\\)",
             r"\[ 2x+\alpha=\frac{\pi}{2},\ \frac{5\pi}{2},\ \frac{9\pi}{2},\dots "
             r"\quad(\text{steps of }2\pi). \]"),
        step("Working &middot; smallest positive \\(x\\)",
             r"\[ 2x+0.464=\frac{\pi}{2}\Rightarrow x=\frac{\pi/2-0.464}{2}\approx0.553. \]"),
        step("Working &middot; second smallest positive \\(x\\)",
             r"\[ 2x+0.464=\frac{5\pi}{2}\Rightarrow x=\frac{5\pi/2-0.464}{2}\approx3.69\ "
             r"(3\text{ s.f.}). \]"),
        step("Result", answer(r"\( x\approx3.69\ (3\text{ s.f.}) \)")),
        step("Sense check",
             r"The two maxima on the graph are at \(x\approx0.553\) then \(x\approx3.69\); the "
             r"second is the required answer. \(3.694\to3.69\) to 3 s.f.", chk=True),
    ])
    partCii = part("Part (c)(ii) &middot; Second smallest positive \\(x\\) at the maximum", cii,
                   pm="Solved",
                   carry=r"From (b): maximum when \(\sin(2x+\alpha)=1\), \(\alpha\approx0.464\).")
    dia2 = diagram("q4_sine.png",
                   r"\(\sin(2x+\alpha)\) reaches \(1\) at \(2x+\alpha=\tfrac\pi2,\tfrac{5\pi}2\); "
                   r"solving the whole angle first gives \(x\approx0.553\) (smallest) then "
                   r"\(x\approx3.69\) (second smallest).")
    whyCii = why("The headline mistake of the lesson (recorded):",
                 r"Phuc found the first \(x\) and then added \(2\pi\) to <b>that \(x\)</b>. "
                 r"<b>Harry:</b> <i>&ldquo;ones are two pi apart, but these ones, when you've "
                 r"rearranged, are not two pi apart&rdquo;</i> &mdash; the \(2\pi\) periodicity "
                 r"belongs to the angle \(2x+\alpha\), <b>before</b> you divide by 2. "
                 r"<b>Rule:</b> list all whole-angle solutions first, then rearrange for \(x\). "
                 r"Also \(3\) s.f. \(\ne\) 3 d.p. (\(3.694\to3.69\)).")

    body = (META + tag("P3 WMA13/01 &mdash; June 2024 &mdash; Q4") +
            "<h1>Q4 &middot; Double angle &rarr; \\(R\\sin(2x+\\alpha)\\) &rarr; max &amp; smallest \\(x\\)</h1>" +
            header + dia1 +
            banner("<b>Status:</b> fully worked in the lesson &mdash; \\(a=4,b=2,c=-1\\); "
                   "\\(R=2\\sqrt5,\\ \\alpha=\\arctan\\tfrac12\\approx0.464\\); "
                   "\\(f_{\\max}=2\\sqrt5-1\\); second smallest \\(x\\approx3.69\\). "
                   "<b>This is the payoff for the identity drill.</b>") +
            partA + whyA + partB + whyB + partCi + goodCi + partCii + dia2 + whyCii +
            foot("Q4 fully worked across segments&nbsp;3&ndash;4. On-screen wording reproduced "
                 "from <code>analysis/gemini_video_evidence.md</code> (Q4a/b/c(i)/c(ii)); solution "
                 "matches guide &sect;6.4. \\(\\alpha\\) shown as \\(\\arctan\\tfrac12\\approx0.464\\) "
                 "rad and \\(R\\) kept exact as \\(2\\sqrt5\\); per-part marks were not shown."))
    build(slug, title, body)


if __name__ == "__main__":
    card_warmup()
    card_q1()
    card_q2()
    card_q3()
    card_q4()
    print("cards done")
