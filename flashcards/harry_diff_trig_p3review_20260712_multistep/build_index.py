#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Landing page for the Harry 12 Jul 2026 differentiation & trig multi-step deck
(multistep_v2, current UI standard).

Cards + preview images use relative same-directory paths. No live/publish links.
Q3 is DISCUSSED ONLY and labelled as such so the landing cannot contradict the card.
Reader-only provenance (no SHA-256 / manifest / source_register wording — Pitfall 18).
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# (slug, title, desc, badge_text, badge_class)
CARDS = [
    ("Warmup_derivatives_identities",
     "Warm-up &middot; Derivatives &amp; identity recall",
     "Exponential/log derivatives, reciprocal-trig derivatives, and reciprocal / "
     "Pythagorean / double-angle identities &mdash; the toolkit Q4 depends on.",
     "Recall drill &mdash; all solved on the board", "ok"),
    ("P3_Jun2024_Q1",
     "Q1 &middot; Modulus function \\(2|x-5|+10\\)",
     "Vertex of a V-graph, an algebraic modulus inequality, and the image of a point "
     "under \\(y=3f(x-2)\\).",
     "Fully worked &mdash; \\(P=(5,10)\\), \\(x&lt;\\tfrac52\\), \\((7,30)\\)", "ok"),
    ("P3_Jun2024_Q2",
     "Q2 &middot; Algebraic division then integration",
     "Divide \\(\\tfrac{2x^{2}-5x+8}{x-2}\\) to \\(Ax+B+\\tfrac{C}{x-2}\\), then a "
     "definite integral giving \\(\\alpha+\\beta\\ln 3\\).",
     "Fully worked &mdash; \\(A{=}2,B{=}{-}1,C{=}6\\); \\(44+6\\ln3\\)", "ok"),
    ("P3_Jun2024_Q3",
     "Q3 &middot; Sketch \\(\\log_{10}y\\) vs \\(\\log_{10}x\\)",
     "Harry reviewed Phuc's existing sketch (&ldquo;pretty much fine&rdquo;) and added "
     "two points: label intercepts as coordinate pairs, and &lsquo;sketch&rsquo; vs "
     "&lsquo;plot&rsquo;. Not re-derived.",
     "Discussed only &mdash; not re-worked", "note"),
    ("P3_Jun2024_Q4",
     "Q4 &middot; Double angle &rarr; \\(R\\)-form &rarr; max",
     "Rewrite \\(f(x)=8\\sin x\\cos x+4\\cos^{2}x-3\\) as \\(a\\sin2x+b\\cos2x+c\\), "
     "then \\(R\\sin(2x+\\alpha)+c\\), then max value and second smallest \\(x\\).",
     "Fully worked &mdash; \\(R=2\\sqrt5\\), max \\(2\\sqrt5-1\\), \\(x\\approx3.69\\)", "ok"),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Differentiation &amp; Trig &mdash; Multi-step flashcards</title>
<script>
window.MathJax = { tex: { inlineMath: [['\\\\(','\\\\)']] }, svg: { fontCache: 'global' } };
</script>
<script src="mathjax-tex-svg.js" async></script>
<style>
  body { font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Arial,sans-serif;
         margin:0; background:#e9ecef; color:#1c1c1c; }
  .wrap { max-width:1040px; margin:0 auto; padding:34px 22px 60px; }
  h1 { color:#1b4d2c; font-size:26px; margin:0 0 4px; }
  .sub { color:#555; font-size:14px; margin-bottom:6px; }
  .prov { background:#fff; border:1px solid #d8dde2; border-left:5px solid #1b4d2c; border-radius:8px;
          padding:14px 18px; margin:16px 0 24px; font-size:13.5px; line-height:1.55; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:18px; }
  .card { background:#fff; border:1px solid #d3d7db; border-radius:10px; overflow:hidden;
          text-decoration:none; color:inherit; display:flex; flex-direction:column;
          box-shadow:0 1px 3px rgba(0,0,0,.07); transition:box-shadow .15s, transform .15s; }
  .card:hover { box-shadow:0 6px 18px rgba(0,0,0,.14); transform:translateY(-2px); }
  .thumb { height:190px; background:#f6f7f8 center top/cover no-repeat; border-bottom:1px solid #e2e5e8; }
  .body { padding:13px 15px 16px; }
  .body h2 { font-size:16px; margin:0 0 4px; color:#1b4d2c; }
  .body p { font-size:13px; color:#444; margin:0 0 10px; }
  .badge { display:inline-block; font-size:11px; font-weight:700; padding:3px 9px; border-radius:5px; }
  .badge.ok { background:#e8f3ec; color:#1b4d2c; border:1px solid #9cc6ab; }
  .badge.note { background:#fff4e0; color:#8a5a00; border:1px solid #e0b060; }
  .foot { margin-top:30px; font-size:12px; color:#777; border-top:1px solid #ccc; padding-top:12px; }
  @media (max-width:600px){ .wrap{padding-top:20px} h1{font-size:22px} }
</style>
</head>
<body>
<div class="wrap">
<h1>Differentiation &amp; Trigonometry &mdash; Multi-step flashcards</h1>
<p class="sub">Harry &rarr; Phuc &nbsp;|&nbsp; 12 July 2026 lesson &nbsp;|&nbsp; Edexcel IAL P3 (WMA13/01), June 2024 paper</p>
<div class="prov">
  Source-grounded deck built from the final passed revision guide, the lesson recording /
  Gemini video ledger, and the official P3 specification. Question wording is reproduced from
  the paper <b>as displayed on-screen by the tutor</b> (no official question-paper PDF or mark
  scheme was in the source set, so per-part marks are not shown). Every <b>.why</b> box quotes a
  mistake Phuc actually made on the recording; non-evidenced warnings use a labelled
  &ldquo;Common trap&rdquo;. Grey work boxes are maskable via an accessible reveal control; MathJax v3 (tex-svg, self-contained).
  Q3 is <b>discussed only</b> and is not given an invented full solution.
</div>
<div class="grid">
"""

FOOT = """</div>
<div class="foot">
  Harry (Get Me That Grade) &rarr; Phuc &nbsp;|&nbsp; 12 July 2026 &nbsp;|&nbsp;
  Source-grounded revision deck &bull; local-only rebuild to current UI standard &bull; not published.
</div>
</div>
</body>
</html>
"""


def main():
    html = HEAD
    for slug, title, desc, badge_txt, badge_cls in CARDS:
        html += f"""  <a class="card" href="{slug}.html">
    <div class="thumb" style="background-image:url('{slug}.png')"></div>
    <div class="body">
      <h2>{title}</h2>
      <p>{desc}</p>
      <span class="badge {badge_cls}">{badge_txt}</span>
    </div>
  </a>
"""
    html += FOOT
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote index.html", f"({len(html)//1024} KB)")


if __name__ == "__main__":
    main()
