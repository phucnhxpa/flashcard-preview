#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Landing page for the P3 Oct 2025 + ESAT multi-step deck.
Preview images and links use relative same-directory paths."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))

CARDS = [
    ("ESAT_warmup", "ESAT warm-up", "Sphere surface area = 10 closed cylinders",
     "Board-read (Miro) &mdash; not official WMA13", "board"),
    ("P3_Oct2025_Q1", "Q1 &middot; Functions f and g", "Range, inverse, composite functions",
     "Discussed only &mdash; not worked in lesson", "note"),
    ("P3_Oct2025_Q2", "Q2 &middot; Roots, IVT, iteration", "Sign change + continuity; cube-root rearrangement",
     "(a) reviewed &middot; (b) completed w/ prompting &middot; (c) deferred", "note"),
    ("P3_Oct2025_Q3", "Q3 &middot; Logs and exponential rate", "Log-linear graph, V=ab^t, dV/dt = 50",
     "Fully worked &mdash; T = 13", "ok"),
    ("P3_Oct2025_Q4", "Q4 &middot; R-form and minimum", "R sin(2x-&alpha;), min g(x), smallest x",
     "Fully worked &mdash; R=2&radic;3, &alpha;=&pi;/3", "ok"),
    ("P3_Oct2025_Q5", "Q5 &middot; Squirrels model", "Quotient rule, show e^{0.2T}=A, maximum",
     "Fully worked &mdash; max 459", "ok"),
]

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>P3 Oct 2025 + ESAT — Multi-step flashcards</title>
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
  .badge.board { background:#8a5a00; color:#fff; }
  .badge.note { background:#fff4e0; color:#8a5a00; border:1px solid #e0b060; }
  .badge.ok { background:#e8f3ec; color:#1b4d2c; border:1px solid #9cc6ab; }
  .foot { margin-top:30px; font-size:12px; color:#777; border-top:1px solid #ccc; padding-top:12px; }
</style>
</head>
<body>
<div class="wrap">
  <h1>P3 October 2025 &amp; ESAT &mdash; Multi-step flashcards</h1>
  <div class="sub">Pearson Edexcel IAL Pure Mathematics P3 (WMA13/01, 21 Oct 2025) + ESAT surface-area warm-up</div>
  <div class="sub">Built from the Harry &rarr; Phuc tutorial, 11 July 2026 &bull; Loom 1&nbsp;h&nbsp;08&nbsp;m</div>
  <div class="prov">
    <b>How to use:</b> each card shows the exact exam question and marks, then a grey
    <i>maskable</i> working box you can hide and re-solve. <b>Why-boxes</b> quote only mistakes
    Phuc actually made on the recording (or a labelled &ldquo;common trap&rdquo; where none was
    recorded). Grounded solely in the lesson recording, the official paper and the study log;
    internal evidence conflicts (ESAT option labels, Q2(b) completion status, Q4 coefficients,
    Q5 denominator / &ldquo;459 vs 959&rdquo;) are flagged in-card. The ESAT starter is
    <b>board-read from the Miro board</b>, not an official WMA13 question.
  </div>
  <div class="grid">
"""

for slug, title, desc, badge_txt, badge_cls in CARDS:
    html += f"""    <a class="card" href="{slug}.html">
      <div class="thumb" style="background-image:url('{slug}.png')"></div>
      <div class="body">
        <h2>{title}</h2>
        <p>{desc}</p>
        <span class="badge {badge_cls}">{badge_txt}</span>
      </div>
    </a>
"""

html += """  </div>
  <div class="foot">
    Source-grounded revision deck &bull; no content invented. Q1 and Q2(c) are shown with their
    evidenced &ldquo;not worked / deferred&rdquo; status and are not given a fabricated tutor
    solution. Review and publishing are handled separately by the parent process.
  </div>
</div>
</body>
</html>
"""

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("wrote index.html", f"({len(html)//1024} KB)")
