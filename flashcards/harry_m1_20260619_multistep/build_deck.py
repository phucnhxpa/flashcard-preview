#!/usr/bin/env python3
"""Deterministic local builder for the 19 June 2026 Harry M1 (WME01/01 Jan 2023)
multi-step deck — current UI standard.

Source boundary: the independently release-audited PASS revision guide
(guide_v2/revision_guide.pdf, SHA-256
0edeb6db0a327900b6579a8c1b49b29a1d78f9fd83d6f399ce260ab17fd296a4). All wording,
marks and values are taken from that guide + its official MS appendix.

Standard features (controlled generator, strict-clean):
  * per-question standalone HTML cards
  * M1 dual-label scheme (tutor-packet <-> official WME01) on every card
  * status pills preserved (COMPLETED WITH PROMPTING / REVIEWED ONLY-DEFERRED /
    NOT DISCUSSED / LIVE SET-UP ONLY / ESAT-STYLE WARM-UP - NOT WME01)
  * exact official marks + parts (8/10/10/9/8/8/7/15; Q4 unsplit)
  * grey maskable "finalized work" boxes
  * REAL accessible reveal/hide control (button + aria-expanded/aria-controls)
  * MathJax v3 tex-svg (local mathjax-tex-svg.js)
  * literal static PNG export anchors (one PNG per card)
All authored strings are RAW literals: TeX backslashes stay literal. A strict
C0 guard refuses to write any control byte < 0x20 except LF (no restoration
shim). This is "warnings-as-errors" compile discipline.
"""
from __future__ import annotations
import shutil
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow

ROOT = Path(__file__).resolve().parent
SRC_MJ = Path("/root/agent-artifacts/workspace/revision_pipeline/lessons/2026-07-10_harry_p2_may2024/multistep_v2/mathjax-tex-svg.js")
GUIDE_HASH = "0edeb6db0a327900b6579a8c1b49b29a1d78f9fd83d6f399ce260ab17fd296a4"
BLUE, RED, GREEN, GREY, INK = "#2563eb", "#dc2626", "#15803d", "#94a3b8", "#172033"

CSS = r'''
:root{--ink:#111827;--muted:#5b6473;--paper:#fff;--canvas:#f3f5f8;--line:#d8dee8;--work:#e5e7eb;--accent:#0f4c81;--accent-pale:#e8f0f8;--trap:#9f1239;--source:#334155;--radius:12px;--green:#0b6b45;--amber:#865b00}*{box-sizing:border-box}html{background:var(--canvas)}body{margin:0;color:var(--ink);font:15px/1.53 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--canvas)}#card{max-width:1180px;margin:0 auto;padding:28px 28px 52px}.export-btn{position:fixed;top:16px;right:16px;z-index:100;background:#111827;color:#fff;text-decoration:none;padding:8px 16px;border-radius:8px;font-weight:700;font-size:12px;box-shadow:0 3px 10px #0003}.kicker{font-size:11px;font-weight:800;letter-spacing:.11em;text-transform:uppercase;color:var(--accent);margin-bottom:6px}.q-header{background:#fff;border:1px solid var(--line);border-left:6px solid var(--accent);border-radius:var(--radius);padding:22px 24px;margin:0 0 16px;box-shadow:0 1px 2px #1111}.q-header h1{font-size:25px;line-height:1.2;margin:0 0 9px}.q-header p{margin:8px 0}.meta{display:flex;flex-wrap:wrap;gap:7px;margin:13px 0 0}.badge{display:inline-block;border:1px solid #bdd8d4;background:var(--accent-pale);color:#0f4c81;border-radius:999px;padding:3px 9px;font-size:12px;font-weight:700}.badge.source{background:#eef2f7;border-color:#d7dee8;color:var(--source)}.badge.status{background:#eef7ee;border-color:#bfe0cb;color:#17633d}.badge.status.deferred{background:#fff8e9;border-color:#f0d797;color:#704b00}.badge.status.notdone{background:#fdeaea;border-color:#f3c2c2;color:#9a2c2c}.badge.status.setup{background:#eef1f8;border-color:#c8d2ec;color:#33458a}.notice{background:#fffbeb;border:1px solid #fcd34d;border-radius:9px;padding:10px 12px;margin:15px 0;color:#713f12}.global-toggle{position:sticky;top:0;z-index:50;background:#111827;color:#fff;border:none;border-radius:8px;padding:8px 14px;font-weight:700;font-size:12px;cursor:pointer;margin:0 0 14px;box-shadow:0 2px 8px #0003}.global-toggle:focus-visible{outline:3px solid #fbbf24;outline-offset:2px}.part{margin:18px 0;border:1px solid var(--line);border-radius:var(--radius);background:#fff;overflow:hidden}.part-title{display:flex;align-items:center;gap:9px;flex-wrap:wrap;padding:12px 16px;background:#f8fafc;border-bottom:1px solid var(--line);font-size:17px;font-weight:800}.marks{font-size:12px;color:#fff;background:#334155;border-radius:999px;padding:2px 8px}.carry-in{margin:13px 16px 0;border-left:4px solid #0f4c81;background:#edf4fb;padding:9px 11px;font-size:14px}.work{margin:13px 16px 16px;background:var(--work);border:1px solid #cbd5e1;border-radius:9px;padding:12px 14px;min-height:120px}.work[hidden]{display:none}.work p{margin:0 0 9px}.work p:last-child{margin-bottom:0}.work .formula{background:#fff;border:1px dashed #9fb3c8;border-radius:6px;padding:6px 9px;margin:6px 0}.work mjx-container{overflow-x:auto;overflow-y:hidden;max-width:100%}.mask-toggle{display:inline-block;margin:4px 16px 0;background:#334155;color:#fff;border:none;border-radius:7px;padding:6px 12px;font-weight:700;font-size:12px;cursor:pointer}.mask-toggle:focus-visible{outline:3px solid #fbbf24;outline-offset:2px}.answer{display:block;margin-top:8px;background:#e7f5ee;border:1px solid #bfe0cb;border-radius:7px;padding:7px 10px;font-weight:700;color:#17633d}.why{margin:12px 16px 14px;background:#fff;border-left:4px solid var(--trap);border-radius:0 8px 8px 0;padding:9px 12px;font-size:13px;color:#7a1530}.q-diagram{margin:12px 16px 0;text-align:center}.q-diagram img{max-width:420px;width:100%;height:auto;border:1px solid var(--line);border-radius:8px;background:#fff;padding:6px}.q-diagram figcaption{font-size:12px;color:var(--muted);margin-top:5px}.algebra-note{margin:12px 16px 0;background:#f1f5f9;border:1px dashed #cbd5e1;border-radius:8px;padding:8px 11px;font-size:13px;color:#475569}.footer{margin:16px 16px 14px;font-size:12px;color:var(--muted);border-top:1px solid var(--line);padding-top:9px}mjx-container{overflow-x:auto;overflow-y:hidden;max-width:100%}mjx-container>svg{max-width:100%;height:auto;display:block}mjx-container[display="true"]{display:block;max-width:100%;overflow-x:auto;overflow-y:hidden}@media(max-width:600px){.export-btn{position:static;display:block;width:calc(100% - 32px);margin:14px auto 0;text-align:center;top:auto;right:auto}.q-header h1{font-size:21px}.global-toggle{position:static;width:calc(100% - 32px);margin:0 auto 12px}}
'''

CARD_TOP = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__TITLE__ · Harry 19 Jun 2026</title><script>window.MathJax={tex:{inlineMath:[["\\(","\\)"]],displayMath:[["\\[","\\]"]]},svg:{fontCache:"global"}};</script><link rel="icon" href="data:,"><script defer src="mathjax-tex-svg.js"></script><style>__CSS__</style></head><body><a class="export-btn" href="__PNG__" target="_blank" rel="noopener">Export PNG</a><main id="card"><button class="global-toggle" type="button" id="global-toggle" aria-expanded="true" aria-controls="card">Mask all working</button>'''

CARD_BOTTOM = r'''<script>
(function(){
  function bind(btn){
    var id=btn.getAttribute("aria-controls");
    var work=document.getElementById(id);
    if(!work) return;
    btn.addEventListener("click",function(){
      var willHide=!work.hasAttribute("hidden");
      if(willHide){ work.setAttribute("hidden",""); btn.setAttribute("aria-expanded","false"); btn.textContent="Show working"; }
      else { work.removeAttribute("hidden"); btn.setAttribute("aria-expanded","true"); btn.textContent="Hide working"; }
    });
  }
  document.querySelectorAll(".mask-toggle").forEach(bind);
  var g=document.getElementById("global-toggle");
  if(g){ g.addEventListener("click",function(){
    var anyHidden=false, works=document.querySelectorAll(".work");
    works.forEach(function(w){ if(w.hasAttribute("hidden")) anyHidden=true; });
    var hide=!anyHidden;
    works.forEach(function(w){
      var b=document.querySelector('[aria-controls="'+w.id+'"]');
      if(hide){ w.setAttribute("hidden",""); if(b){b.setAttribute("aria-expanded","false"); b.textContent="Show working";} }
      else { w.removeAttribute("hidden"); if(b){b.setAttribute("aria-expanded","true"); b.textContent="Hide working";} }
    });
    g.setAttribute("aria-expanded", hide?"false":"true");
    g.textContent= hide ? "Reveal all working" : "Mask all working";
  }); }
})();
</script></main></body></html>'''

PRECISION = r'''<section class="part precision"><div class="part-title">Precision recall strip <span class="marks">closed-book check</span></div><div class="carry-in"><strong>Carry-in:</strong> retain the original condition, exact values, and command word before starting any algebra. Each grey box below is maskable — use the "Hide working" control to self-test, then "Show working" to check.</div><div class="work" data-maskable="true"><p class="strategy">Retrieve the symbolic route before substituting numbers.</p><p><strong>1. Read the command.</strong> "Show that" ends at the displayed result; "exact" forbids an early decimal; "magnitude" means a positive quantity (drop modulus bars); "find the acceleration" needs Newton's 2nd law along the resolving direction.</p><p><strong>2. Formula first.</strong> Write a named formula or identity symbolically, then substitute: momentum \(mv\), impulse \(mv-mu\), the SUVAT set, \(F=\mu R\) (and \(F\le\mu R\)), principle of moments (clockwise = anticlockwise about a pivot).</p><p><strong>3. Preserve the carry-in.</strong> Treat each displayed carry-in as known while the earlier grey working is covered. State the new equation created from it rather than referring vaguely to an earlier part.</p><p><strong>4. Final check.</strong> Check signs, domain or positivity, units where applicable, and requested rounding. Keep stored unrounded values (e.g. \(a=1.1838\ldots\)) until the final requested precision.</p><p><strong>Dual-label discipline.</strong> The card you worked from is the <em>tutor packet</em>; the official paper is <em>WME01/01 January 2023</em>. Both labels are shown so a packet number never stands alone.</p></div></section>'''

_status_class = {
    "COMPLETED WITH PROMPTING": "status",
    "REVIEWED ONLY / DEFERRED": "status deferred",
    "NOT DISCUSSED": "status notdone",
    "LIVE SET-UP ONLY": "status setup",
    "ESAT-STYLE WARM-UP — NOT WME01": "status deferred",
}

def header(title, prompt, total, status, source):
    cls = _status_class.get(status, "status")
    return (f'<section class="q-header"><div class="kicker">Harry &rarr; Student &middot; 19 June 2026</div>'
            f'<h1>{title}</h1><p>{prompt}</p>'
            f'<div class="meta"><span class="badge">{total} marks</span>'
            f'<span class="badge {cls}">{status}</span>'
            f'<span class="badge source">{source}</span></div></section>')

_work_id_counter = [0]
def part(label, marks, carry, work, why="", diagram="", ref_box=False):
    _work_id_counter[0] += 1
    wid = f"work-{_work_id_counter[0]}"
    visual = f'<figure class="q-diagram">{diagram}</figure>' if diagram else ""
    if not diagram:
        visual = '<div class="algebra-note">Algebra-only: no spatial, graphical, or statistical diagram is needed for this reasoning.</div>'
    why_html = f'<aside class="why">{why}</aside>' if why else ""
    mark_html = f'<span class="marks">{marks}</span>' if marks is not None else ""
    ref_cls = ' notice' if ref_box else ''
    toggle = (f'<button class="mask-toggle" type="button" aria-expanded="true" aria-controls="{wid}">Hide working</button>')
    return (f'<section class="part{ref_cls}"><div class="part-title">{label}{mark_html}</div>'
            f'<div class="carry-in"><strong>Carry-in / given:</strong> {carry}</div>{visual}'
            f'{toggle}<div class="work" id="{wid}" data-maskable="true">{work}</div>{why_html}</section>')

def fig(file, caption):
    return f'<img src="diagrams/{file}" alt="{caption}">'

def write_strict(path, text):
    """Strict-clean writer — the C0 guard promised by this module's docstring.

    Refuses to write ANY control byte < 0x20 except LF. There is deliberately
    NO control-character restoration shim: we never strip-and-rewrite, never
    decode-with-ignore, never silently swallow a stray control byte. A stray
    control byte is a hard build failure, not a silent pass (strict-clean).
    """
    for ch in text:
        code = ord(ch)
        if code < 0x20 and ch != "\n":
            raise ValueError(
                f"strict-clean C0 guard: refusing control byte U+{code:04X} in {path}"
            )
    path.write_text(text, encoding="utf-8")


def write_card(slug, title, body):
    top = CARD_TOP.replace("__TITLE__", title).replace("__PNG__", f"{slug}.png").replace("__CSS__", CSS)
    complete = top + body + PRECISION + CARD_BOTTOM
    write_strict(ROOT / f"{slug}.html", complete)
    return complete

# --------------------------------------------------------------------------
# Diagrams
# --------------------------------------------------------------------------
def diagrams():
    d = ROOT / "diagrams"; d.mkdir(exist_ok=True)
    # Collision: before / after velocity line.
    fig_, ax = plt.subplots(figsize=(6.2, 3.0), dpi=180); ax.set_xlim(0,10); ax.set_ylim(-1.4,1.8); ax.axis("off")
    ax.annotate("BEFORE",(0.2,1.6),weight="bold",color=BLUE)
    ax.text(1.0,0.9,r"$A:3m$",ha="center",weight="bold"); ax.text(1.0,0.55,r"$1.5$",ha="center")
    ax.annotate("",xy=(2.4,0.78),xytext=(0.4,0.78),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=2.2))
    ax.text(5.0,0.9,r"$B:m$",ha="center",weight="bold"); ax.text(5.0,0.55,r"$-1.5$",ha="center")
    ax.annotate("",xy=(3.6,0.78),xytext=(6.4,0.78),arrowprops=dict(arrowstyle="-|>",color=RED,lw=2.2))
    ax.annotate("AFTER",(0.2,-0.2),weight="bold",color=GREEN)
    ax.text(1.0,-0.5,r"$A:3m$",ha="center",weight="bold"); ax.text(1.0,-0.85,r"$x=0.5$",ha="center",color=GREEN)
    ax.annotate("",xy=(2.4,-0.62),xytext=(0.4,-0.62),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=2.2))
    ax.text(5.0,-0.5,r"$B:m$",ha="center",weight="bold"); ax.text(5.0,-0.85,r"$x+1=1.5$",ha="center",color=GREEN)
    ax.annotate("",xy=(6.4,-0.62),xytext=(3.6,-0.62),arrowprops=dict(arrowstyle="-|>",color=RED,lw=2.2))
    fig_.tight_layout(); fig_.savefig(d/"collision.png", bbox_inches="tight", facecolor="white"); plt.close(fig_)
    # Train speed-time trapezium.
    fig_, ax = plt.subplots(figsize=(5.4,3.0), dpi=180)
    xs=[0,40,40+180,40+180+80]; ys=[0,20,20,0]
    ax.plot(xs,ys,color=BLUE,lw=2.4); ax.fill_between(xs,ys,color=BLUE,alpha=.12)
    ax.plot([0,40+180+80],[0,0],color=INK,lw=1)
    ax.scatter(xs,ys,color=RED,zorder=3)
    for x,y,t in [(0,0,"0"),(40,20,"T"),(220,20,"T+180"),(300,0,"3T+180")]:
        ax.annotate(t,(x,y),xytext=(x,y+1.4),ha="center",fontsize=9,color=INK)
    ax.annotate("peak 20 m s⁻¹",(40+90,20),xytext=(40+90,20.6),ha="center",fontsize=9,color=GREEN)
    ax.set(xlim=(-8,310),ylim=(-3,25),xlabel="time (s)",ylabel="speed (m s⁻¹)"); ax.grid(alpha=.25)
    fig_.tight_layout(); fig_.savefig(d/"train.png", bbox_inches="tight", facecolor="white"); plt.close(fig_)
    # Moments: rod on supports C and D with loads.
    fig_, ax = plt.subplots(figsize=(6.4,2.8), dpi=180); ax.set_xlim(0,10); ax.set_ylim(-1.6,2.0); ax.axis("off")
    ax.plot([0.5,9.5],[0,0],color=INK,lw=4)  # rod
    ax.text(0.2,0.25,"rod 1.5 m",fontsize=9)
    # supports C (0.24 from left), D (0.36 from right)
    cx=0.5+ (0.24/1.5)*9.0; dx=9.5-(0.36/1.5)*9.0
    ax.text(cx,-0.5,"C",ha="center",weight="bold"); ax.text(dx,-0.5,"D",ha="center",weight="bold")
    ax.annotate("",xy=(cx,0),xytext=(cx,-1.2),arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=2))
    ax.annotate("",xy=(dx,0),xytext=(dx,-1.2),arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=2))
    # load 150N at 1.26 from C ; W at x from C
    lx=cx + (1.26/1.5)*9.0; ax.annotate("",xy=(lx,0),xytext=(lx,1.3),arrowprops=dict(arrowstyle="-|>",color=RED,lw=2)); ax.text(lx,1.5,"150 N",ha="center",color=RED,fontsize=9)
    wx=cx + (0.63/1.5)*9.0; ax.annotate("",xy=(wx,0),xytext=(wx,1.3),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=2)); ax.text(wx,1.5,"W",ha="center",color=BLUE,fontsize=9)
    ax.text(0.5,1.8,"tilt about C ⇒ R_D=0",fontsize=9,color=GREEN)
    fig_.tight_layout(); fig_.savefig(d/"moments.png", bbox_inches="tight", facecolor="white"); plt.close(fig_)
    # Inclined plane force diagram.
    fig_, ax = plt.subplots(figsize=(5.6,3.4), dpi=180); ax.set_xlim(-1,5); ax.set_ylim(-1,4); ax.axis("off")
    # plane
    ax.plot([-0.5,4.5],[-0.3,2.0],color=INK,lw=3)
    ax.text(4.1,2.1,r"$30^\circ$",fontsize=11)
    # block
    ax.add_patch(Rectangle((0.9,1.0),0.9,0.7,color="#dbeafe",ec=BLUE,lw=1.5))
    # weight
    ax.annotate("",xy=(1.35,-0.5),xytext=(1.35,1.0),arrowprops=dict(arrowstyle="-|>",color=RED,lw=2)); ax.text(1.5,-0.7,"2g",color=RED,fontsize=10)
    # normal
    n=0.9; ax.annotate("",xy=(1.35+0.5,1.35+0.3),xytext=(1.35,1.35),arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=2)); ax.text(2.0,1.7,"R",color=GREEN,fontsize=10)
    # applied 18N at 40 to plane
    ax.annotate("",xy=(1.35+1.3,1.35+1.1),xytext=(1.35,1.35),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=2.2)); ax.text(2.9,2.6,"18 N",color=BLUE,fontsize=10)
    ax.text(0.2,3.4,"Resolve ∥ and ⊥ to plane",fontsize=9,color=GREEN)
    fig_.tight_layout(); fig_.savefig(d/"incline.png", bbox_inches="tight", facecolor="white"); plt.close(fig_)
    # Vectors velocity.
    fig_, ax = plt.subplots(figsize=(4.6,3.4), dpi=180); ax.set_xlim(-1,4); ax.set_ylim(-1,4); ax.axis("off")
    ax.annotate("",xy=(3,2.5),xytext=(0.6,0.6),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=2.4)); ax.text(3.1,2.6,r"$\mathbf{v}$",color=BLUE,fontsize=11)
    ax.annotate("",xy=(3.4,0.6),xytext=(0.6,0.6),arrowprops=dict(arrowstyle="-",color=GREY,lw=1.5))
    ax.annotate("",xy=(0.6,2.9),xytext=(0.6,0.6),arrowprops=dict(arrowstyle="-",color=GREY,lw=1.5))
    ax.text(1.9,1.4,r"$\mathbf{i}$",color=GREY,fontsize=10); ax.text(0.1,1.9,r"$\mathbf{j}$",color=GREY,fontsize=10)
    ax.text(2.0,3.0,r"$|\mathbf{v}|=\sqrt{v_x^2+v_y^2}$",fontsize=9,color=GREEN)
    fig_.tight_layout(); fig_.savefig(d/"vectors.png", bbox_inches="tight", facecolor="white"); plt.close(fig_)
    # Boat two ropes.
    fig_, ax = plt.subplots(figsize=(5.6,3.2), dpi=180); ax.set_xlim(-1,6); ax.set_ylim(-0.5,4); ax.axis("off")
    ax.add_patch(Rectangle((2.2,1.4),1.4,1.0,color="#dbeafe",ec=BLUE,lw=1.5)); ax.text(2.9,1.9,"boat",ha="center",fontsize=9)
    ax.annotate("",xy=(2.9,1.4),xytext=(2.9,-0.2),arrowprops=dict(arrowstyle="-|>",color=RED,lw=2)); ax.text(3.05,-0.35,"W",color=RED,fontsize=10)
    ax.annotate("",xy=(1.2,3.2),xytext=(2.9,1.9),arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=2.2)); ax.text(0.7,3.3,"P",color=GREEN,fontsize=10)
    ax.annotate("",xy=(4.6,3.2),xytext=(3.5,1.9),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=2.2)); ax.text(4.7,3.3,"Q",color=BLUE,fontsize=10)
    ax.text(1.2,1.9,r"$\alpha$",fontsize=11); ax.text(4.4,1.9,r"$\alpha$",fontsize=11)
    fig_.tight_layout(); fig_.savefig(d/"boat.png", bbox_inches="tight", facecolor="white"); plt.close(fig_)
    # Lift two boxes.
    fig_, ax = plt.subplots(figsize=(4.4,3.6), dpi=180); ax.set_xlim(-1,4); ax.set_ylim(-0.5,4); ax.axis("off")
    ax.add_patch(Rectangle((1.0,1.6),1.6,0.9,color="#dbeafe",ec=BLUE,lw=1.5)); ax.text(1.8,2.0,"P",ha="center",fontsize=10)
    ax.add_patch(Rectangle((1.0,0.7),1.6,0.9,color="#ede9fe",ec="#7c3aed",lw=1.5)); ax.text(1.8,1.1,"Q",ha="center",fontsize=10)
    ax.annotate("",xy=(1.8,0.7),xytext=(1.8,-0.3),arrowprops=dict(arrowstyle="-|>",color=RED,lw=2)); ax.text(2.0,-0.4,"W",color=RED,fontsize=10)
    ax.annotate("",xy=(1.8,2.5),xytext=(1.8,4.0),arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=2)); ax.text(2.0,4.1,"T",color=GREEN,fontsize=10)
    fig_.tight_layout(); fig_.savefig(d/"lift.png", bbox_inches="tight", facecolor="white"); plt.close(fig_)

# --------------------------------------------------------------------------
# Cards
# --------------------------------------------------------------------------
def build():
    _work_id_counter[0] = 0
    ROOT.mkdir(parents=True, exist_ok=True); (ROOT/"diagrams").mkdir(exist_ok=True)
    if not SRC_MJ.exists():
        raise FileNotFoundError(f"missing {SRC_MJ}")
    shutil.copy2(SRC_MJ, ROOT/"mathjax-tex-svg.js")
    diagrams()

    # ---- ESAT warm-up (NOT WME01) ----
    esat = header("ESAT-style warm-up · inequality counting",
                  r"<strong>Problem (ESAT style, not WME01).</strong> How many different integers \(n\) are there such that the difference between \(2\sqrt{n}\) and \(7\) is less than \(1\)? (Options: 0, 2, 4, 6, 8.)",
                  5, "ESAT-STYLE WARM-UP — NOT WME01", "lesson warm-up (not part of WME01)")
    esat += part("Unfold the modulus chain", 3,
                 r"“Difference less than 1” means the size of the gap is under 1.",
                 r"<p class='strategy'>Write the gap as one modulus statement and unfold it on a number line; keep every term positive before squaring.</p>"
                 r"<p class='formula'><strong>Formula:</strong> \(\lvert 2\sqrt{n}-7\rvert<1\ \Rightarrow\ -1<2\sqrt{n}-7<1\).</p>"
                 r"<p><strong>Add 7:</strong> \(6<2\sqrt{n}<8\).</p>"
                 r"<p><strong>Divide by 2 (all positive):</strong> \(3<\sqrt{n}<4\).</p>"
                 r"<p><strong>Square:</strong> \(9<n<16\).</p>"
                 r"<div class='answer'>\(n\in\{10,11,12,13,14,15\}\): count \(=15-10+1=6\).</div>"
                 r"<p><strong>Sense check:</strong> strict bounds exclude 9 and 16; inclusive counting needs the “+1”.</p>",
                 r"<strong>Trap:</strong> squaring before isolating the root, or writing \(16-9=7\) and forgetting the +1. The endpoints 9 and 16 are excluded.")
    esat += "<p class='footer'>Source class: ESAT-style warm-up opening the lesson. It is <strong>not</strong> an M1 / WME01 question and must never be labelled as one.</p>"
    write_card("ESAT_warmup", "ESAT warm-up", esat)

    # ---- Packet Q1 / Official Q2: collision & impulse ----
    q2 = header("Packet Q1 / Official WME01 Q2 — direct collision and impulse",
                r"<strong>From the paper.</strong> Two particles collide directly along a line. Particle A has mass \(3m\) and particle B has mass \(m\); each approaches the other at \(1.5\ \mathrm{m\,s^{-1}}\). Find the speeds after impact, then the magnitude of the impulse on B.",
                8, "COMPLETED WITH PROMPTING", "official WME01/01 Jan 2023 (packet Q1)")
    q2 += part("Part (a) · speeds after impact", 5,
               r"Take A’s initial direction as positive; label post-collision speeds \(v_A=x\), \(v_B=x+1\).",
               r"<p class='strategy'>Apply conservation of linear momentum along the line of impact using signed velocities.</p>"
               r"<p class='formula'><strong>Formula:</strong> \(\sum mu=\sum mv\).</p>"
               r"<p>\((3m)(1.5)+m(-1.5)=3mx+m(x+1)\).</p>"
               r"<p>\(4.5-1.5=3x+x+1\ \Rightarrow\ 3=4x+1\ \Rightarrow\ x=\tfrac12\).</p>"
               r"<p>\(v_A=\tfrac12\ \mathrm{m\,s^{-1}}=0.5\ \mathrm{m\,s^{-1}}\), \(v_B=x+1=\tfrac32\ \mathrm{m\,s^{-1}}=1.5\ \mathrm{m\,s^{-1}}\).</p>"
               r"<div class='answer'>\(v_A=0.5\ \mathrm{m\,s^{-1}},\ v_B=1.5\ \mathrm{m\,s^{-1}}\).</div>"
               r"<p><strong>Sense check:</strong> both speeds are positive, consistent with the chosen direction.</p>",
               r"<strong>Trap:</strong> dropping B’s negative initial sign; two unlabelled numbers do not say which is A and which is B — label them. (Earlier-guide claim of a live slip to \(x=2.75,\ v_B=3.75\) is removed: the recording shows only the correct values.)",
               fig("collision.png", "Before/after velocity line; A positive, B negative before impact."))
    q2 += part("Part (b) · magnitude of impulse on B", 3,
               r"Carry-in: \(v_B=1.5\ \mathrm{m\,s^{-1}}\) after, \(u_B=-1.5\ \mathrm{m\,s^{-1}}\) before.",
               r"<p class='strategy'>Impulse on B is B’s change of momentum; “magnitude” means a positive quantity.</p>"
               r"<p class='formula'><strong>Formula:</strong> \(I_B=m(v_B-u_B)\).</p>"
               r"<p>\(I_B=m\!\left(\tfrac32-(-1.5)\right)=m\!\left(\tfrac32+\tfrac32\right)=3m\ \mathrm{N\,s}\).</p>"
               r"<div class='answer'>\(\lvert I_B\rvert=3m\ \mathrm{N\,s}\).</div>"
               r"<p><strong>Sense check:</strong> magnitude is positive; the modulus bars are dropped in the final answer.</p>",
               r"<strong>Trap:</strong> taking impulse on the wrong particle, or leaving the modulus bars / a sign. The question asks for the impulse <em>on B</em>.")
    q2 += "<p class='footer'>Source class: COMPLETED WITH PROMPTING. Tutor-packet Q1 = official WME01 Q2. No false slip narrative retained.</p>"
    write_card("M1_WME01_Q2", "M1 WME01 Q2 — collision & impulse", q2)

    # ---- Packet Q2 / Official Q1: train speed-time ----
    q1 = header("Packet Q2 / Official WME01 Q1 — train speed–time graph",
                r"<strong>From the paper.</strong> A train accelerates from rest to \(20\ \mathrm{m\,s^{-1}}\), runs at that speed for \(180\ \mathrm{s}\), then decelerates to rest. The magnitude of the acceleration is twice the magnitude of the deceleration; total distance is \(4.8\ \mathrm{km}\). Sketch the graph, find \(T\), and find the initial acceleration.",
                10, "COMPLETED WITH PROMPTING", "official WME01/01 Jan 2023 (packet Q2)")
    q1 += part("Part (a) · the sketch", 3,
               r"Acceleration phase lasts \(T\); because \(|a|=2|d|\), the deceleration phase lasts \(2T\).",
               r"<p class='strategy'>Place the peak at \(20\ \mathrm{m\,s^{-1}}\); read base markers from the two ramp durations.</p>"
               r"<p>Base markers: \(T,\ T+180,\ 3T+180\).</p>"
               r"<div class='answer'>Trapezium peaking at \(20\ \mathrm{m\,s^{-1}}\) with base \(0\to 3T+180\).</div>"
               r"<p><strong>Sense check:</strong> the constant phase runs to \(T+180\), not to \(180\) from the origin.</p>",
               r"<strong>Trap:</strong> assuming both ramp times are equal. The acceleration is twice the deceleration, so the deceleration phase is twice as long.")
    q1 += part("Part (b) · find T", 5,
               r"Carry-in: total distance \(=4800\ \mathrm{m}\) (convert \(4.8\ \mathrm{km}\) first).",
               r"<p class='strategy'>Area of the trapezium = distance; use \(A=\tfrac12(a+b)h\).</p>"
               r"<p class='formula'><strong>Formula:</strong> \(A=\tfrac12(a+b)h\), parallel sides \(a=180,\ b=3T+180\), height \(h=20\).</p>"
               r"<p>\(4800=\tfrac12\big(180+(3T+180)\big)(20)=(3T+360)(10)\).</p>"
               r"<p>\(480=3T+360\ \Rightarrow\ 3T=120\ \Rightarrow\ T=40\ \mathrm{s}\).</p>"
               r"<div class='answer'>\(T=40\ \mathrm{s}\).</div>"
               r"<p><strong>Sense check:</strong> \(3(40)+180=300\ \mathrm{s}\) total time; area is positive.</p>",
               r"<strong>Trap:</strong> using the gradient instead of the area; equating km directly to a metre-based area without converting \(4.8\ \mathrm{km}=4800\ \mathrm{m}\). (Peak label is \(20\ \mathrm{m\,s^{-1}}\); do not cite a mis-drawn value such as “30”.)",
               fig("train.png", "Speed–time trapezium; base markers T, T+180, 3T+180."))
    q1 += part("Part (c) · initial acceleration", 2,
               r"Carry-in: peak speed \(20\ \mathrm{m\,s^{-1}}\), acceleration phase lasts \(T=40\ \mathrm{s}\).",
               r"<p class='strategy'>Gradient of the first segment = acceleration.</p>"
               r"<p class='formula'><strong>Formula:</strong> \(a=\dfrac{\Delta v}{\Delta t}\).</p>"
               r"<p>\(a=\dfrac{20}{T}=\dfrac{20}{40}=0.5\ \mathrm{m\,s^{-2}}\).</p>"
               r"<div class='answer'>\(a=0.5\ \mathrm{m\,s^{-2}}\).</div>"
               r"<p><strong>Sense check:</strong> positive, since the train speeds up from rest.</p>",
               r"<strong>Trap:</strong> reading the gradient off the wrong segment (e.g. the deceleration phase).")
    q1 += "<p class='footer'>Source class: COMPLETED WITH PROMPTING. Tutor-packet Q2 = official WME01 Q1.</p>"
    write_card("M1_WME01_Q1", "M1 WME01 Q1 — train speed–time", q1)

    # ---- Packet Q5 / Official Q4: moments & tilting ----
    q4 = header("Packet Q5 / Official WME01 Q4 — moments and tilting",
                r"<strong>From the paper.</strong> A non-uniform branch of length \(1.5\ \mathrm{m}\) rests on two supports C and D, placed \(0.24\ \mathrm{m}\) and \(0.36\ \mathrm{m}\) from its ends. The weight \(W\) acts at a distance \(x\) from C. Two tilting cases (loads \(150\ \mathrm{N}\) and \(225\ \mathrm{N}\)) give two equations; find \(W\) and \(x\).",
                8, "COMPLETED WITH PROMPTING", "official WME01/01 Jan 2023 (packet Q5)")
    q4 += ("<p class='notice'><strong>Official marks: 8 — both values, not split by the paper.</strong> "
           "The two scenarios below share that single 8-mark allocation; no subpart split is invented.</p>")
    q4 += part("Scenario 1 — moments about C", None,
               r"On the point of tilting about C \(\Rightarrow R_D=0\); the \(150\ \mathrm{N}\) load is \(1.5-0.24=1.26\ \mathrm{m}\) from C.",
               r"<p class='strategy'>Equate clockwise and anticlockwise moments about C; a zero reaction (or a force through the pivot) contributes no moment.</p>"
               r"<p class='formula'><strong>Formula:</strong> clockwise moments = anticlockwise moments about C.</p>"
               r"<p>\(Wx=150(1.5-0.24)=150(1.26)=189\).</p>"
               r"<div class='answer'>Equation (A): \(Wx=189\).</div>"
               r"<p><strong>Sense check:</strong> only \(W\) (at \(x\)) and the \(150\ \mathrm{N}\) load produce moments about C.</p>",
               r"<strong>Trap:</strong> sign errors from one long signed sum — put clockwise on one side, anticlockwise on the other. (Earlier-guide claim of “moments about B” is removed: the recording shows D was used.)",
               fig("moments.png", "Rod on supports C and D; tilt about C means R_D=0."))
    q4 += part("Scenario 2 — moments about D, then solve", None,
               r"Carry-in: equation (A) \(Wx=189\); tilt about D \(\Rightarrow R_C=0\); the \(225\ \mathrm{N}\) load is \(0.36\ \mathrm{m}\) from D.",
               r"<p class='strategy'>Take moments about D for equation (B), then divide (A) by (B) to cancel \(W\).</p>"
               r"<p>\(225(0.36)=(1.5-0.36-0.24-x)W\ \Rightarrow\ 81=(0.9-x)W\).</p>"
               r"<p>\(\dfrac{Wx}{W(0.9-x)}=\dfrac{189}{81}=\dfrac{7}{3}\ \Rightarrow\ \dfrac{x}{0.9-x}=\dfrac{7}{3}\).</p>"
               r"<p>\(3x=7(0.9-x)\ \Rightarrow\ 10x=6.3\ \Rightarrow\ x=0.63\ \mathrm{m}\).</p>"
               r"<p>Back-substitute: \(W=\dfrac{189}{0.63}=300\ \mathrm{N}\).</p>"
               r"<div class='answer'>\(x=0.63\ \mathrm{m},\ W=300\ \mathrm{N}\).</div>"
               r"<p><strong>Sense check:</strong> \(0.9-0.63=0.27\); \(300(0.27)=81\) matches.</p>",
               r"<strong>Trap:</strong> substitution when division cancels \(W\) more cleanly; starting the back-substitution from a wrong \(W\). Box and label equations (A) and (B) before combining.")
    q4 += "<p class='footer'>Source class: COMPLETED WITH PROMPTING. Tutor-packet Q5 = official WME01 Q4. The 8 marks are not split between the two values.</p>"
    write_card("M1_WME01_Q4", "M1 WME01 Q4 — moments & tilting", q4)

    # ---- Packet Q3 / Official Q3: vectors (REVIEWED ONLY / DEFERRED) ----
    q3 = header("Packet Q3 / Official WME01 Q3 — constant-acceleration vectors",
                r"<strong>From the paper.</strong> A particle moves with constant acceleration; its position is \(\mathbf{r}(t)\). (a) Find the speed at \(t=2\). (b) Find the angle the velocity makes with \(\mathbf{i}\) at \(t=2\). (c) Find \(T\) for which the direction is \(2\mathbf{i}-3\mathbf{j}\).",
                10, "REVIEWED ONLY / DEFERRED", "official WME01/01 Jan 2023 (packet Q3)")
    q3 += ("<p class='notice'><strong>Status boundary: REVIEWED ONLY / DEFERRED.</strong> The Student’s vector work was “pretty good” in the earlier test, so this question was deliberately skipped and left for a later day. No subpart was re-worked live; the values below are <strong>OFFICIAL MS REFERENCE ONLY</strong>.</p>")
    q3 += part("Part (a) · speed at t = 2  [MS reference]", None,
               r"Standard method: \(\mathbf{v}(t)=\dfrac{d\mathbf{r}}{dt}\); speed \(=\lvert\mathbf{v}\rvert\).",
               r"<p class='strategy'>Differentiate position to get velocity; speed is the magnitude of the velocity vector.</p>"
               r"<p class='formula'><strong>Formula:</strong> speed \(=\sqrt{v_x^2+v_y^2}\).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: speed at \(t=2\) is \(\sqrt{45}=3\sqrt5\approx6.7\ \mathrm{m\,s^{-1}}\).</p>"
               r"<div class='answer'>\(3\sqrt5\approx6.7\ \mathrm{m\,s^{-1}}\).</div>",
               r"<strong>Trap:</strong> forgetting that speed uses <em>both</em> components (not just one).",
               fig("vectors.png", "Velocity vector with components along i and j."))
    q3 += part("Part (b) · angle with i at t = 2  [MS reference]", None,
               r"Carry-in: the velocity components at \(t=2\) from part (a).",
               r"<p class='strategy'>The direction angle uses \(\tan^{-1}(v_y/v_x)\), quadrant-correct.</p>"
               r"<p class='formula'><strong>Formula:</strong> \(\theta=\tan^{-1}\!\big(\tfrac{v_y}{v_x}\big)\) (reference to \(\mathbf{i}\)).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: angle \(=27^\circ\) (or \(333^\circ\) per the stated convention).</p>"
               r"<div class='answer'>\(27^\circ\) (or \(333^\circ\)).</div>",
               r"<strong>Trap:</strong> measuring the angle from \(\mathbf{j}\) instead of \(\mathbf{i}\); dropping the quadrant statement.")
    q3 += part("Part (c) · T for direction 2i − 3j  [MS reference]", None,
               r"Carry-in: the velocity expression \(\mathbf{v}(t)\) from the paper.",
               r"<p class='strategy'>Set the velocity direction equal to \(2\mathbf{i}-3\mathbf{j}\) (i.e. \(v_y/v_x=-3/2\)) and solve for \(T\).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: \(T=3.2\).</p>"
               r"<div class='answer'>\(T=3.2\).</div>"
               r"<p><strong>Sense check:</strong> keep the exact ratio until the final value.</p>",
               r"<strong>Trap:</strong> rounding before solving for \(T\).")
    q3 += "<p class='footer'>Source class: REVIEWED ONLY / DEFERRED. Tutor-packet Q3 = official WME01 Q3. All values are official-MS reference; none was produced live.</p>"
    write_card("M1_WME01_Q3", "M1 WME01 Q3 — vectors", q3)

    # ---- Packet Q4 / Official Q5: vehicle SUVAT (REVIEWED ONLY / DEFERRED) ----
    q5 = header("Packet Q4 / Official WME01 Q5 — vehicle SUVAT (P–Q–R)",
                r"<strong>From the paper.</strong> A vehicle moves with constant acceleration between points P, Q and R. (a) Show \(x=3u\). (b) Find \(u\). (c) Find the distance travelled in the first \(14\ \mathrm{s}\).",
                9, "REVIEWED ONLY / DEFERRED", "official WME01/01 Jan 2023 (packet Q4)")
    q5 += ("<p class='notice'><strong>Status boundary: REVIEWED ONLY / DEFERRED.</strong> The Student’s SUVAT work was “okay too”, so this question was left for later. No subpart was re-worked live; the values below are <strong>OFFICIAL MS REFERENCE ONLY</strong>.</p>")
    q5 += part("Part (a) · show x = 3u  [MS reference]", None,
               r"Standard method: use the given positions/speeds to establish the relation.",
               r"<p class='strategy'>Manipulate the given expressions to reach the displayed result; “show that” ends at \(x=3u\).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: the model establishes \(x=3u\).</p>"
               r"<div class='answer'>\(x=3u\) (shown).</div>",
               r"<strong>Trap:</strong> over-solving past the given “show that” result.")
    q5 += part("Part (b) · find u  [MS reference]", None,
               r"Carry-in: the relation \(x=3u\) and the paper’s geometry/times.",
               r"<p class='strategy'>Solve the derived model for the initial speed \(u\).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: \(u=9\ \mathrm{m\,s^{-1}}\).</p>"
               r"<div class='answer'>\(u=9\ \mathrm{m\,s^{-1}}\).</div>",
               r"<strong>Trap:</strong> a sign or algebra slip in the set-up.")
    q5 += part("Part (c) · distance in first 14 s  [MS reference]", None,
               r"Carry-in: the speed–time description from the paper.",
               r"<p class='strategy'>Distance = area under the speed–time graph over the stated interval.</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: distance in first \(14\ \mathrm{s}=201\ \mathrm{m}\).</p>"
               r"<div class='answer'>\(201\ \mathrm{m}\).</div>"
               r"<p><strong>Sense check:</strong> match the stated time bound exactly (\(0\to14\ \mathrm{s}\)).</p>",
               r"<strong>Trap:</strong> using the wrong time bound for the area.")
    q5 += "<p class='footer'>Source class: REVIEWED ONLY / DEFERRED. Tutor-packet Q4 = official WME01 Q5. All values are official-MS reference; none was produced live.</p>"
    write_card("M1_WME01_Q5", "M1 WME01 Q5 — vehicle SUVAT", q5)

    # ---- Packet Q6 / Official Q6: boat two ropes (NOT DISCUSSED) ----
    q6 = header("Packet Q6 / Official WME01 Q6 — boat pulled by two ropes",
                r"<strong>From the paper.</strong> A boat is in equilibrium, pulled by two ropes each at angle \(\alpha\) to the line of motion, with tensions \(P\) and another tension. Find the rope angle \(\alpha\) and the tension \(P\).",
                8, "NOT DISCUSSED", "official WME01/01 Jan 2023 (packet Q6)")
    q6 += ("<p class='notice'><strong>Status boundary: NOT DISCUSSED.</strong> Packet Q6 (official Q6) was not opened in the lesson. It appears here only so the paper inventory is complete; the values below are <strong>OFFICIAL MS REFERENCE ONLY</strong>.</p>")
    q6 += part("Part · rope angle and tension  [MS reference]", None,
               r"Standard method: resolve both rope tensions into components; net force = 0.",
               r"<p class='strategy'>Each rope contributes a component along the line of motion; equate the sum to the resisting force.</p>"
               r"<p class='formula'><strong>Formula:</strong> equilibrium \(\Rightarrow\sum F_x=0,\ \sum F_y=0\).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: rope angle \(\alpha\approx31.9^\circ\); tension \(P\approx609\ \mathrm{N}\) (mark scheme accepts \(610\ \mathrm{N}\) or better).</p>"
               r"<div class='answer'>\(\alpha\approx31.9^\circ,\ P\approx609\ \mathrm{N}\).</div>"
               r"<p><strong>Sense check:</strong> the two ropes are not assumed symmetric unless the paper says so.</p>",
               r"<strong>Trap:</strong> assuming both ropes symmetric without checking; rounding too early.",
               fig("boat.png", "Boat in equilibrium under two rope tensions and its weight."))
    q6 += "<p class='footer'>Source class: NOT DISCUSSED. Tutor-packet Q6 = official WME01 Q6. Value is official-MS reference; not produced live.</p>"
    write_card("M1_WME01_Q6", "M1 WME01 Q6 — boat two ropes", q6)

    # ---- Packet Q7 / Official Q7: lift and two boxes (NOT DISCUSSED) ----
    q7 = header("Packet Q7 / Official WME01 Q7 — lift and two boxes",
                r"<strong>From the paper.</strong> A lift carries two boxes P and Q. (a) Find the combined mass of P and Q. (b) Find the mass of P.",
                7, "NOT DISCUSSED", "official WME01/01 Jan 2023 (packet Q7)")
    q7 += ("<p class='notice'><strong>Status boundary: NOT DISCUSSED.</strong> Packet Q7 (official Q7) was not opened in the lesson. The values below are <strong>OFFICIAL MS REFERENCE ONLY</strong>.</p>")
    q7 += part("Part (a) · combined mass  [MS reference]", None,
               r"Standard method: the combined mass follows from the total weight / contact forces.",
               r"<p class='strategy'>Combined mass = mass of both boxes P and Q.</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: combined mass of P and Q \(=5m\).</p>"
               r"<div class='answer'>\(5m\).</div>",
               r"<strong>Trap:</strong> forgetting one of the two boxes.")
    q7 += part("Part (b) · mass of P  [MS reference]", None,
               r"Carry-in: combined mass \(=5m\); solve the contact-force equations for P’s mass.",
               r"<p class='strategy'>Separate the contact forces on P from those on Q.</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: mass of P \(=2m\).</p>"
               r"<div class='answer'>\(2m\).</div>"
               r"<p><strong>Sense check:</strong> P and Q are distinct masses.</p>",
               r"<strong>Trap:</strong> confusing P and Q.",
               fig("lift.png", "Lift carrying boxes P (upper) and Q (lower) under tension T and weight W."))
    q7 += "<p class='footer'>Source class: NOT DISCUSSED. Tutor-packet Q7 = official WME01 Q7. Values are official-MS reference; not produced live.</p>"
    write_card("M1_WME01_Q7", "M1 WME01 Q7 — lift & boxes", q7)

    # ---- Packet Q8 / Official Q8: parcel on rough incline (LIVE SET-UP ONLY) ----
    q8 = header("Packet Q8 / Official WME01 Q8 — parcel on a rough inclined plane",
                r"<strong>From the paper.</strong> A parcel P of mass \(2\ \mathrm{kg}\) lies on a rough plane inclined at \(30^\circ\). A force of \(18\ \mathrm{N}\) acts on P at \(40^\circ\) to the plane; \(\mu=0.3\). (a) Find the acceleration. (b) Find the speed at B. (c) Decide whether P then remains at rest.",
                15, "LIVE SET-UP ONLY", "official WME01/01 Jan 2023 (packet Q8)")
    q8 += ("<p class='notice'><strong>Status boundary: LIVE SET-UP ONLY.</strong> The lesson reached the force diagram and the two governing equations (1) and (2) but did not finish the arithmetic. Every numerical value below the live set-up is <strong>OFFICIAL MS REFERENCE ONLY</strong> (purple boxes).</p>")
    q8 += part("Live set-up — force diagram &amp; governing equations", None,
               r"Weight \(2g\) vertical; normal reaction \(R\); friction \(F_R\) along the plane; \(18\ \mathrm{N}\) resolved as \(18\cos40^\circ\) up the plane and \(18\sin40^\circ\) away from the plane; weight resolves as \(2g\sin30^\circ\) down and \(2g\cos30^\circ\) into the plane.",
               r"<p class='strategy'>Resolve parallel and perpendicular to the plane; apply Newton’s 2nd law along the plane.</p>"
               r"<p class='formula'><strong>Parallel (Newton 2):</strong> \(18\cos40^\circ - F_R - 2g\sin30^\circ = 2a\). &nbsp; <strong>Friction:</strong> \(F_R=\mu R=0.3R\).</p>"
               r"<p><strong>Corrected perpendicular equation:</strong> \(R+18\sin40^\circ = 2g\cos30^\circ\) (the board line was wrong — use this corrected form).</p>"
               r"<p><strong>Sense check:</strong> resolving direction is <em>perpendicular to the plane</em>, not “vertically”.</p>",
               r"<strong>Tutor remark that needs correction:</strong> “friction only exists because of the applied pull, so it can never exceed the applied component” is <em>not</em> a valid general rule. The direction of acceleration comes from the net resolved force along the plane, not from that claim. (Here the net force does happen to be up the slope — but only because equation (1) says so.)",
               fig("incline.png", "Force diagram on the 30° plane; resolve parallel and perpendicular."))
    q8 += part("Part (a) · acceleration  [MS reference for the arithmetic]", 8,
               r"Carry-in: live equations (1) \(18\cos40^\circ-F_R-2g\sin30^\circ=2a\) and (2) \(F_R=0.3R\); corrected \(R+18\sin40^\circ=2g\cos30^\circ\); \(g=9.8\).",
               r"<p class='strategy'>Find \(R\) from the perpendicular equation, then \(F_R\), then substitute into (1) and divide by 2.</p>"
               r"<p>\(R=2g\cos30^\circ-18\sin40^\circ=19.6(0.86603)-18(0.64279)\approx5.4039\ \mathrm{N}\).</p>"
               r"<p>\(F_R=0.3R\approx1.6212\ \mathrm{N}\).</p>"
               r"<p>\(2a=18\cos40^\circ-F_R-2g\sin30^\circ=13.7888-1.6212-9.8\approx2.3676\).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: \(a\approx1.1838\ \mathrm{m\,s^{-2}}\Rightarrow a\approx1.18\ \mathrm{m\,s^{-2}}\) (or \(\approx1.2\)).</p>"
               r"<div class='answer'>\(a\approx1.18\ \mathrm{m\,s^{-2}}\).</div>"
               r"<p><strong>Sense check:</strong> keep the unrounded \(1.1838\ldots\) for onward substitution.</p>",
               r"<strong>Trap:</strong> using the uncorrected board perpendicular line; confusing “balanced vertically” with balanced perpendicular to the plane.")
    q8 += part("Part (b) · speed at B  [MS reference]", 3,
               r"Carry-in: \(u=2\ \mathrm{m\,s^{-1}}\), \(s=5\ \mathrm{m}\), \(a=1.1838\ldots\ \mathrm{m\,s^{-2}}\).",
               r"<p class='strategy'>Use the SUVAT energy-free relation \(v^2=u^2+2as\).</p>"
               r"<p class='formula'><strong>Formula:</strong> \(v^2=u^2+2as\).</p>"
               r"<p>\(v^2=2^2+2(1.1838)(5)\approx15.838\).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: \(v\approx3.98\ \mathrm{m\,s^{-1}}\) (or \(\approx4.0\)).</p>"
               r"<div class='answer'>\(v\approx3.98\ \mathrm{m\,s^{-1}}\).</div>"
               r"<p><strong>Sense check:</strong> speed is positive; use the unrounded \(a\).</p>",
               r"<strong>Trap:</strong> substituting a rounded \(a\) too early.")
    q8 += part("Part (c) · does P remain at rest?  [MS reference]", 4,
               r"Carry-in: with the \(18\ \mathrm{N}\) force removed, at rest \(R=2g\cos30^\circ\approx16.974\ \mathrm{N}\); weight component down the plane \(=2g\sin30^\circ=9.8\ \mathrm{N}\).",
               r"<p class='strategy'>Compare the down-plane weight component with the maximum available friction \(\mu R\).</p>"
               r"<p class='formula'><strong>Formula:</strong> max friction \(=\mu R=0.3(16.974)\approx5.09\ \mathrm{N}\).</p>"
               r"<p>OFFICIAL MS REFERENCE ONLY: \(9.8\ \mathrm{N} > 5.09\ \mathrm{N}\), so friction cannot hold the parcel.</p>"
               r"<div class='answer'>P does <strong>not</strong> remain at rest.</div>"
               r"<p><strong>Sense check:</strong> the down-plane component exceeds the limiting friction.</p>",
               r"<strong>Trap:</strong> asserting “it remains at rest” without comparing the two forces; the friction rule does not decide this.")
    q8 += "<p class='footer'>Source class: LIVE SET-UP ONLY. Tutor-packet Q8 = official WME01 Q8. The live lesson reached only the diagram + equations (1),(2); all numerics are official-MS reference.</p>"
    write_card("M1_WME01_Q8", "M1 WME01 Q8 — rough inclined plane", q8)

    tiles = [
        ("ESAT_warmup", "ESAT warm-up", "ESAT-STYLE WARM-UP — NOT WME01", "Inequality counting"),
        ("M1_WME01_Q2", "Packet Q1 / WME01 Q2", "COMPLETED WITH PROMPTING", "Collision & impulse"),
        ("M1_WME01_Q1", "Packet Q2 / WME01 Q1", "COMPLETED WITH PROMPTING", "Train speed–time graph"),
        ("M1_WME01_Q4", "Packet Q5 / WME01 Q4", "COMPLETED WITH PROMPTING", "Moments & tilting"),
        ("M1_WME01_Q3", "Packet Q3 / WME01 Q3", "REVIEWED ONLY / DEFERRED", "Vectors"),
        ("M1_WME01_Q5", "Packet Q4 / WME01 Q5", "REVIEWED ONLY / DEFERRED", "Vehicle SUVAT"),
        ("M1_WME01_Q6", "Packet Q6 / WME01 Q6", "NOT DISCUSSED", "Boat, two ropes"),
        ("M1_WME01_Q7", "Packet Q7 / WME01 Q7", "NOT DISCUSSED", "Lift & two boxes"),
        ("M1_WME01_Q8", "Packet Q8 / WME01 Q8", "LIVE SET-UP ONLY", "Rough inclined plane"),
    ]
    tile_html = "".join(
        f'<a class="tile" href="{s}.html"><img src="{s}.png" alt="Preview of {t}"><div>'
        f'<span class="pill">{status}</span><h2>{t}</h2><p>{desc}</p></div></a>' for s, t, status, desc in tiles)
    landing = (f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Harry M1 Jan 2023 · multi-step v2</title><style>:root{{--ink:#111827;--muted:#64748b;--paper:#fff;--canvas:#f3f5f8;--accent:#0f4c81;--line:#d8dee8;--green:#0b6b45;--amber:#865b00;--red:#9a2c2c}}*{{box-sizing:border-box}}body{{margin:0;background:var(--canvas);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--ink)}}main{{max-width:1120px;margin:auto;padding:44px 24px}}.eyebrow{{color:var(--accent);font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}}h1{{font-size:clamp(28px,5vw,44px);letter-spacing:-.04em;line-height:1.05;margin:8px 0 12px}}.lead{{max-width:780px;color:var(--muted)}}.notice{{margin:24px 0;padding:13px 15px;border-left:4px solid var(--accent);background:#e8f0f8;border-radius:8px}}.pill{{display:inline-block;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:#0f4c81;background:#e8f0f8;border:1px solid #bdd8d4;border-radius:999px;padding:2px 8px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px;margin-top:10px}}.tile{{background:var(--paper);border:1px solid var(--line);border-radius:13px;overflow:hidden;color:inherit;text-decoration:none;box-shadow:0 1px 2px #1111;transition:transform .15s,box-shadow .15s}}.tile:hover{{transform:translateY(-2px);box-shadow:0 7px 18px #1112}}.tile img{{width:100%;height:190px;object-fit:cover;object-position:top;border-bottom:1px solid var(--line);display:block}}.tile div{{padding:14px 16px}}.tile h2{{font-size:19px;margin:6px 0 4px}}.tile p{{margin:0;color:var(--muted)}}footer{{margin-top:28px;padding-top:14px;border-top:1px solid var(--line);font-size:12px;color:var(--muted)}}button{{font:inherit}}@media(max-width:600px){{main{{padding:28px 15px}}.tile img{{height:150px}}}}</style></head><body><main><div class="eyebrow">Harry &rarr; Student &middot; 19 June 2026</div><h1>Mechanics M1 (WME01/01 Jan 2023)<br>multi-step deck</h1><p class="lead">Nine source-bounded, maskable working cards rebuilt to the current multi-step format. Each opens a per-question standalone page with the dual label (tutor packet &harr; official WME01), exact marks/parts, a grey maskable “finalized work” box with a real reveal/hide control, and a literal PNG export. The official QP/MS controls wording, marks and values; lesson status is shown on every card.</p><div class="notice"><strong>Coverage:</strong> 1 ESAT warm-up (not WME01) + 8 WME01 questions. Guide provenance SHA-256 <code>{GUIDE_HASH}</code>. Publication status: local only — not published, uploaded, or indexed.</div><div class="grid">{tile_html}</div><footer>Independent-release audit PASS on guide_v2/revision_guide.pdf. Deck is local-only.</footer></main></body></html>''')
    write_strict(ROOT / "index.html", landing)
    print(f"Wrote {9} cards + diagrams + landing to {ROOT}")


if __name__ == "__main__":
    build()
