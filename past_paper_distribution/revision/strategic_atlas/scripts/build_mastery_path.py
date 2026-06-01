#!/usr/bin/env python3
"""
Build the Strategic Atlas MASTERY PATH layer.

A step-by-step, foundation -> A* curriculum that sequences every technique
(move) and every past-paper question into ordered problem sets, with
browser-local progress tracking.

Inputs  (reconstructed from the deployed site + reports):
  /tmp/atlas_moves.json   per-move: slug,name,domain,family,freq,macro,units,qlinks,usewhen
  /tmp/atlas_marks.json   {UNIT|Session|qnum: marks}
  ../../reports/<UNIT>_distribution.json   spec-topic mark-share

Outputs (into  strategic_atlas/path/ ):
  index.html        hub (7 units, overall progress)
  <unit>.html       per-unit mastery path  (P1..P4, FP1..FP3)

Deterministic, no LLM, no network. Run from the strategic_atlas dir.
"""
import json, os, re, html as ih
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ATLAS = os.path.dirname(HERE)                      # strategic_atlas/
OUT = os.path.join(ATLAS, "path")
REPORTS = os.path.normpath(os.path.join(ATLAS, "..", "..", "reports"))
os.makedirs(OUT, exist_ok=True)

UNITS = ["P1", "P2", "P3", "P4", "FP1", "FP2", "FP3"]
UNIT_NAME = {"P1":"Pure 1","P2":"Pure 2","P3":"Pure 3","P4":"Pure 4",
             "FP1":"Further Pure 1","FP2":"Further Pure 2","FP3":"Further Pure 3"}
EXAM_ISO = {"P1":"2026-05-07","P2":"2026-05-12","P3":"2026-05-28","P4":"2026-06-02",
            "FP1":"2026-05-21","FP2":"2026-06-05","FP3":"2026-06-09"}
EXAM_HUMAN = {"P1":"7 May 2026","P2":"12 May 2026","P3":"28 May 2026","P4":"2 Jun 2026",
              "FP1":"21 May 2026","FP2":"5 Jun 2026","FP3":"9 Jun 2026"}

DOMAIN_COLOR = {
    "Integration":"#FFA726","Sequences & Series":"#26A69A","Algebra & Functions":"#5B6BFA",
    "Trigonometry":"#E91E63","Coordinate Geometry":"#42A5F5","Proof":"#789262",
    "Complex Numbers":"#5C6BC0","Differentiation":"#FF6B35","Differential Equations":"#66BB6A",
    "Binomial Expansion":"#EC407A","Matrices":"#8D6E63","Vectors":"#7E57C2","Polar Coordinates":"#AB47BC",
}
def dcolor(d): return DOMAIN_COLOR.get(d, "#6E6E73")

# tier visuals
T_CORE, T_BUILD, T_STAR = "core", "build", "star"
TIER_DOT = {T_CORE:"#34C759", T_BUILD:"#007AFF", T_STAR:"#AF52DE"}
TIER_LABEL = {T_CORE:"Core", T_BUILD:"Build", T_STAR:"A★"}

moves = json.load(open("/tmp/atlas_moves.json"))
marks = json.load(open("/tmp/atlas_marks.json"))

def esc(t): return ih.unescape(str(t)).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def attr(t): return esc(t).replace('"',"&quot;")

# domain page slugs (existing atlas pages)
DOMAIN_SLUG = {
    "Algebra & Functions":"algebra","Trigonometry":"trig","Integration":"calculus_int",
    "Differentiation":"calculus_diff","Coordinate Geometry":"coordinate_geom",
    "Sequences & Series":"sequences_series","Complex Numbers":"complex",
    "Differential Equations":"ode","Vectors":"vectors","Binomial Expansion":"binomial",
    "Proof":"proof","Matrices":"matrices","Polar Coordinates":"polar",
}

def move_tier(freq):
    if freq >= 3: return T_CORE
    if freq == 2: return T_BUILD
    return T_STAR

def qlabel(qlink):
    base = os.path.basename(qlink)
    m = re.match(r'q-(.+)-Q([0-9A-Za-z]+)\.html$', base)
    if not m: return base, None, None
    sess, qn = m.group(1), m.group(2)
    return f"{sess.replace('_',' ')} Q{qn}", sess, qn

def qmarks(unit, sess, qn):
    if sess is None: return 0
    try: k = f"{unit}|{sess}|{int(re.sub(r'[^0-9].*','',qn))}"
    except Exception: k = f"{unit}|{sess}|{qn}"
    return marks.get(k, 0)

def qid(qlink):
    # canonical id stable across pages: UNIT/chN/q-...html
    return re.sub(r'^(\.\./)+', '', qlink)

# ---------------- shared CSS / chrome ----------------
CSS = """
:root{--bg:#FFFFFF;--fg:#1D1D1F;--muted:#6E6E73;--muted-2:#86868B;--line:#E5E5EA;
--line-soft:#F0F0F2;--pill-bg:#F5F5F7;--shadow:0 4px 24px rgba(0,0,0,.05);--shadow-strong:0 8px 32px rgba(0,0,0,.08);}
*{box-sizing:border-box;}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'SF Pro Display','Segoe UI',sans-serif;
background:var(--bg);color:var(--fg);line-height:1.55;-webkit-font-smoothing:antialiased;}
a{color:inherit;text-decoration:none;}
.container{max-width:1180px;margin:0 auto;padding:22px 28px 90px;}
.topbar{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.86);backdrop-filter:saturate(180%) blur(18px);
-webkit-backdrop-filter:saturate(180%) blur(18px);border-bottom:1px solid var(--line-soft);}
.topbar .inner{max-width:1180px;margin:0 auto;padding:11px 28px;display:flex;align-items:center;gap:18px;flex-wrap:wrap;}
.topbar .brand{font-weight:700;font-size:16px;letter-spacing:-.01em;white-space:nowrap;}
.topbar nav{display:flex;gap:4px;flex-wrap:wrap;}
.topbar nav a{font-size:13px;color:var(--muted);padding:5px 11px;border-radius:8px;transition:.14s;}
.topbar nav a:hover{color:var(--fg);background:var(--pill-bg);}
.topbar nav a.active{color:var(--fg);background:var(--pill-bg);font-weight:600;}
.topbar .spacer{flex:1;}
.topbar .stats{font-size:11.5px;color:var(--muted-2);white-space:nowrap;}
.topbar .stats b{color:var(--fg);font-weight:600;}
header.hero{padding:30px 28px 8px;}
header.hero .container{padding:0;max-width:1180px;}
header.hero .breadcrumb{font-size:12.5px;color:var(--muted-2);margin-bottom:10px;}
header.hero h1{font-size:32px;font-weight:700;margin:0 0 6px;letter-spacing:-.02em;}
header.hero p{color:var(--muted);margin:0;font-size:15px;max-width:760px;line-height:1.55;}
/* progress */
.bar{height:7px;border-radius:99px;background:var(--line);overflow:hidden;}
.bar>i{display:block;height:100%;background:#34C759;border-radius:99px;transition:width .25s;width:0;}
.bigprog{display:flex;align-items:center;gap:16px;margin:20px 0 6px;}
.bigprog .bar{flex:1;height:10px;}
.bigprog .pc{font-size:15px;font-weight:700;white-space:nowrap;font-variant-numeric:tabular-nums;}
/* hub unit cards */
.units{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:14px;margin-top:8px;}
.unit-card{border:1px solid var(--line);border-radius:16px;padding:18px 20px;display:block;transition:.16s;position:relative;overflow:hidden;background:var(--bg);}
.unit-card:hover{transform:translateY(-2px);box-shadow:var(--shadow-strong);border-color:rgba(0,0,0,.16);}
.unit-card .ub{position:absolute;top:0;left:0;right:0;height:4px;}
.unit-card .uh{display:flex;align-items:baseline;justify-content:space-between;gap:10px;}
.unit-card h3{margin:0;font-size:19px;font-weight:700;letter-spacing:-.01em;}
.unit-card .un{font-size:12.5px;color:var(--muted-2);}
.unit-card .exam{font-size:12px;font-weight:600;padding:3px 9px;border-radius:99px;background:var(--pill-bg);color:var(--muted);white-space:nowrap;}
.unit-card .exam.soon{background:#FFEDEA;color:#C0341D;}
.unit-card .exam.past{opacity:.55;}
.unit-card .meta{display:flex;gap:14px;font-size:12.5px;color:var(--muted);margin:12px 0 12px;flex-wrap:wrap;}
.unit-card .meta b{color:var(--fg);font-weight:600;}
.unit-card .pcrow{display:flex;align-items:center;gap:10px;}
.unit-card .pcrow .pc{font-size:12.5px;font-weight:700;font-variant-numeric:tabular-nums;color:var(--muted);min-width:34px;text-align:right;}
/* spec weighting */
.sec-title{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted-2);font-weight:600;margin:34px 2px 12px;}
.weight-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px;}
.weight{border:1px solid var(--line);border-radius:11px;padding:11px 13px;background:var(--bg);}
.weight .wt{font-size:13px;font-weight:600;line-height:1.35;margin-bottom:6px;}
.weight .wm{display:flex;align-items:center;gap:8px;font-size:11.5px;color:var(--muted-2);}
.weight .wbar{flex:1;height:5px;border-radius:99px;background:var(--line);overflow:hidden;}
.weight .wbar>i{display:block;height:100%;background:#FFA726;}
/* steps */
.step{border:1px solid var(--line);border-radius:16px;margin:14px 0;overflow:hidden;background:var(--bg);}
.step>summary{list-style:none;cursor:pointer;padding:16px 20px;display:flex;align-items:center;gap:14px;}
.step>summary::-webkit-details-marker{display:none;}
.step .sn{flex:none;width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;
font-size:14px;font-weight:700;color:#fff;}
.step .stitle{flex:1;min-width:0;}
.step .stitle h3{margin:0;font-size:16.5px;font-weight:700;letter-spacing:-.01em;display:flex;align-items:center;gap:9px;}
.step .stitle .sub{font-size:12px;color:var(--muted-2);margin-top:2px;}
.step .scount{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap;}
.step .sbarwrap{flex:none;width:120px;}
.step .chev{flex:none;color:var(--muted-2);transition:.18s;font-size:13px;}
.step[open] .chev{transform:rotate(90deg);}
.step .body{padding:4px 20px 20px;border-top:1px solid var(--line-soft);}
.lbl{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted-2);font-weight:600;margin:18px 0 9px;}
/* technique chips */
.tier-row{margin-bottom:6px;}
.tier-tag{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:700;color:var(--muted);margin:8px 0 6px;}
.tier-tag .d{width:9px;height:9px;border-radius:50%;}
.tech{display:flex;flex-wrap:wrap;gap:6px;}
.tech a{font-size:12px;padding:5px 11px;border-radius:99px;background:var(--pill-bg);color:var(--fg);
border:1px solid transparent;transition:.13s;line-height:1.3;}
.tech a:hover{background:#fff;border-color:var(--line);transform:translateY(-1px);}
.tech a .td{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:6px;vertical-align:middle;}
details.more>summary{font-size:12px;color:#5B6BFA;cursor:pointer;margin-top:8px;list-style:none;}
details.more>summary::-webkit-details-marker{display:none;}
/* problem checklist */
.plist{display:flex;flex-direction:column;gap:2px;margin-top:4px;}
.q{display:flex;align-items:center;gap:12px;padding:9px 11px;border-radius:10px;transition:.12s;cursor:pointer;}
.q:hover{background:var(--pill-bg);}
.q.done{opacity:.5;}
.q input{appearance:none;-webkit-appearance:none;flex:none;width:20px;height:20px;border:2px solid var(--line);
border-radius:7px;cursor:pointer;position:relative;transition:.12s;margin:0;}
.q input:hover{border-color:#34C759;}
.q input:checked{background:#34C759;border-color:#34C759;}
.q input:checked::after{content:"";position:absolute;left:6px;top:2px;width:5px;height:10px;
border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg);}
.q .qd{flex:none;width:9px;height:9px;border-radius:50%;}
.q .qn{flex:1;min-width:0;font-size:13.5px;font-weight:600;}
.q .qn a:hover{color:#5B6BFA;}
.q.done .qn{text-decoration:line-through;}
.q .qmk{font-size:11.5px;color:var(--muted-2);white-space:nowrap;}
.q .qtech{font-size:11px;color:var(--muted-2);background:var(--pill-bg);border-radius:99px;padding:2px 9px;white-space:nowrap;cursor:help;}
.q .open{font-size:11.5px;color:#5B6BFA;white-space:nowrap;}
.steptools{display:flex;gap:10px;margin-top:12px;}
.steptools button{font-size:11.5px;padding:5px 12px;border:1px solid var(--line);border-radius:99px;background:var(--bg);
color:var(--muted);cursor:pointer;font-family:inherit;transition:.13s;}
.steptools button:hover{border-color:rgba(0,0,0,.25);color:var(--fg);}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--muted);margin:14px 0 0;}
.legend span{display:inline-flex;align-items:center;gap:6px;}
.legend .d{width:9px;height:9px;border-radius:50%;}
footer{color:var(--muted);font-size:13px;padding:46px 24px;text-align:center;border-top:1px solid var(--line);margin-top:64px;}
.callout{background:#FAFAFC;border:1px solid var(--line-soft);border-radius:13px;padding:15px 18px;font-size:13.5px;color:var(--muted);line-height:1.6;margin-top:16px;}
.callout b{color:var(--fg);}
mjx-container{font-size:.97em!important;}
"""

MATHJAX = """<script>window.MathJax={tex:{inlineMath:[['$','$'],['\\\\(','\\\\)']]},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>"""

def topbar():
    # every path page lives in path/ -> atlas root is one level up
    items = [("Big Picture", "../index.html#bigpicture", False),
             ("Domains", "../index.html#domains", False),
             ("All Moves", "../all.html", False),
             ("Mastery Path", "index.html", True)]
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' class="active"' if a else '', t)
        for t, h, a in items)
    return ('<div class="topbar"><div class="inner">'
            '<a class="brand" href="../index.html">Strategic Atlas</a>'
            '<nav>' + nav + '</nav><div class="spacer"></div>'
            '<div class="stats"><b>Mastery Path</b> · foundation → A★</div>'
            '</div></div>')

# ---------------- shared client JS ----------------
UNIT_JS = """
(function(){var KEY='sa_mastery_v1';
function load(){try{return JSON.parse(localStorage.getItem(KEY))||{}}catch(e){return {}}}
function save(o){try{localStorage.setItem(KEY,JSON.stringify(o))}catch(e){}}
var done=load();
function pct(n,d){return d?Math.round(100*n/d):0;}
var boxes=[].slice.call(document.querySelectorAll('input[data-qid]'));
boxes.forEach(function(b){
 if(done[b.dataset.qid]){b.checked=true;b.closest('.q').classList.add('done');}
 b.addEventListener('change',function(){
  if(b.checked){done[b.dataset.qid]=1;b.closest('.q').classList.add('done');}
  else{delete done[b.dataset.qid];b.closest('.q').classList.remove('done');}
  save(done);recompute();});});
// click anywhere on a row (except a link or the box itself) toggles it
document.querySelectorAll('.q').forEach(function(row){row.addEventListener('click',function(e){
 if(e.target.tagName==='A'||e.target.tagName==='INPUT')return;
 var b=row.querySelector('input[data-qid]');b.checked=!b.checked;b.dispatchEvent(new Event('change'));});});
function recompute(){
 document.querySelectorAll('details.step').forEach(function(s){
  var qs=s.querySelectorAll('input[data-qid]');var n=0;
  qs.forEach(function(b){if(b.checked)n++;});
  var bar=s.querySelector('.sbar');if(bar)bar.style.width=pct(n,qs.length)+'%';
  var c=s.querySelector('.scount');if(c)c.textContent=n+' / '+qs.length+' done';});
 var all=document.querySelectorAll('input[data-qid]');var dn=0;
 all.forEach(function(b){if(b.checked)dn++;});
 var ub=document.getElementById('unitBar');if(ub)ub.style.width=pct(dn,all.length)+'%';
 var up=document.getElementById('unitPc');if(up)up.textContent=pct(dn,all.length)+'% · '+dn+' / '+all.length;}
recompute();
document.querySelectorAll('[data-markall]').forEach(function(btn){btn.addEventListener('click',function(e){
 e.preventDefault();var s=btn.closest('details.step');
 s.querySelectorAll('input[data-qid]').forEach(function(b){if(!b.checked){b.checked=true;b.dispatchEvent(new Event('change'));}});});});
document.querySelectorAll('[data-clearall]').forEach(function(btn){btn.addEventListener('click',function(e){
 e.preventDefault();var s=btn.closest('details.step');
 s.querySelectorAll('input[data-qid]').forEach(function(b){if(b.checked){b.checked=false;b.dispatchEvent(new Event('change'));}});});});
var today=new Date();
document.querySelectorAll('[data-exam]').forEach(function(el){
 var d=new Date(el.dataset.exam+'T09:00:00');var days=Math.ceil((d-today)/86400000);
 if(days<0){el.classList.add('past');el.textContent='exam '+el.dataset.human;}
 else if(days===0){el.classList.add('soon');el.textContent='exam today';}
 else{if(days<=10)el.classList.add('soon');el.textContent=days+' days · '+el.dataset.human;}});
})();
"""

HUB_JS = """
(function(){var KEY='sa_mastery_v1';var done={};try{done=JSON.parse(localStorage.getItem(KEY))||{}}catch(e){}
var U=window.UNITQIDS||{};var tot=0,dn=0;
Object.keys(U).forEach(function(u){var ids=U[u];var n=0;ids.forEach(function(id){if(done[id])n++;});
 tot+=ids.length;dn+=n;var p=ids.length?Math.round(100*n/ids.length):0;
 var bar=document.getElementById('bar-'+u);if(bar)bar.style.width=p+'%';
 var pc=document.getElementById('pc-'+u);if(pc)pc.textContent=p+'%';});
var p=tot?Math.round(100*dn/tot):0;
var ob=document.getElementById('overallBar');if(ob)ob.style.width=p+'%';
var op=document.getElementById('overallPc');if(op)op.textContent=p+'% · '+dn+' / '+tot+' questions mastered';
var today=new Date();
document.querySelectorAll('[data-exam]').forEach(function(el){
 var d=new Date(el.dataset.exam+'T09:00:00');var days=Math.ceil((d-today)/86400000);
 if(days<0){el.classList.add('past');el.textContent=el.dataset.human;}
 else if(days===0){el.classList.add('soon');el.textContent='exam today';}
 else{if(days<=10)el.classList.add('soon');el.textContent=days+'d · '+el.dataset.human;}});
})();
"""

def page_head(title):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{esc(title)}</title><style>{CSS}</style>{MATHJAX}</head><body>')

# ---------------- per-unit computation ----------------
def build_unit_model(U):
    um = [m for m in moves if U in m["units"]]
    # question -> moves (restricted to this unit's papers)
    q2m = defaultdict(list)
    for m in um:
        for ql in m["qlinks"]:
            if f"/{U}/" in ql:
                q2m[ql].append(m)
    # difficulty score per question
    qscore = {}
    for ql, ms in q2m.items():
        lab, sess, qn = qlabel(ql)
        mk = qmarks(U, sess, qn)
        qscore[ql] = mk + 1.5 * len(ms)
    scores = sorted(qscore.values())
    def tier_of_q(ql):
        s = qscore[ql]
        if not scores: return T_CORE
        rank = sum(1 for x in scores if x < s) / len(scores)
        if rank <= 0.45: return T_CORE
        if rank <= 0.78: return T_BUILD
        return T_STAR
    # assign each question to a dominant domain
    qdom = {}
    for ql, ms in q2m.items():
        cnt = Counter(m["domain"] for m in ms)
        top = max(cnt.items(), key=lambda kv: (kv[1], -min(mm["freq"] for mm in ms if mm["domain"]==kv[0])))
        qdom[ql] = top[0]
    # build per-domain buckets
    domains = {}
    for d in set(m["domain"] for m in um):
        dms = [m for m in um if m["domain"] == d]
        dqs = [ql for ql, dom in qdom.items() if dom == d]
        dqs.sort(key=lambda ql: (qscore[ql], qlabel(ql)[0]))
        domains[d] = {"moves": dms, "questions": dqs}
    order = sorted(domains, key=lambda d: (-len(domains[d]["questions"]), -len(domains[d]["moves"]), d))
    return dict(unit=U, um=um, q2m=q2m, qscore=qscore, qdom=qdom,
                tier_of_q=tier_of_q, domains=domains, order=order)

def render_tech(dms):
    """technique chips grouped by freq tier; collapses long lists."""
    buckets = {T_CORE:[], T_BUILD:[], T_STAR:[]}
    for m in sorted(dms, key=lambda x:(-x["freq"], x["name"])):
        buckets[move_tier(m["freq"])].append(m)
    out = []
    for t in (T_CORE, T_BUILD, T_STAR):
        b = buckets[t]
        if not b: continue
        out.append(f'<div class="tier-tag"><span class="d" style="background:{TIER_DOT[t]}"></span>'
                   f'{TIER_LABEL[t]} · {len(b)}</div>')
        chips = []
        for m in b:
            tip = attr(m["usewhen"]) if m["usewhen"] else attr(m["name"])
            chips.append(f'<a href="../move/{m["slug"]}.html" title="{tip}">'
                         f'<span class="td" style="background:{TIER_DOT[t]}"></span>{esc(m["name"])}</a>')
        if len(chips) > 14:
            shown = "".join(chips[:14])
            hidden = "".join(chips[14:])
            out.append(f'<div class="tech">{shown}</div>'
                       f'<details class="more"><summary>+ {len(chips)-14} more</summary>'
                       f'<div class="tech" style="margin-top:8px">{hidden}</div></details>')
        else:
            out.append(f'<div class="tech">{"".join(chips)}</div>')
    return "".join(out)

def render_questions(M, dqs):
    rows = []
    for ql in dqs:
        lab, sess, qn = qlabel(ql)
        mk = qmarks(M["unit"], sess, qn)
        t = M["tier_of_q"](ql)
        ntech = len(M["q2m"][ql])
        names = " · ".join(sorted(set(mm["name"] for mm in M["q2m"][ql])))
        mkstr = f"{mk}m" if mk else "—"
        rows.append(
            f'<div class="q"><input type="checkbox" data-qid="{attr(qid(ql))}">'
            f'<span class="qd" style="background:{TIER_DOT[t]}" title="{TIER_LABEL[t]} difficulty"></span>'
            f'<span class="qn"><a href="{attr(ql)}">{esc(lab)}</a></span>'
            f'<span class="qmk">{mkstr}</span>'
            f'<span class="qtech" title="{attr(names)}">{ntech} technique{"s" if ntech!=1 else ""}</span>'
            f'<a class="open" href="{attr(ql)}">solve →</a></div>')
    return "".join(rows)

def render_unit_page(U):
    M = build_unit_model(U)
    nq = sum(len(M["domains"][d]["questions"]) for d in M["order"])
    ntech = len(M["um"])
    # spec weighting from report
    try:
        dist = json.load(open(os.path.join(REPORTS, f"{U}_distribution.json")))
        topics = sorted(dist["topics"], key=lambda t:-t["marks_share"])[:6]
    except Exception:
        topics = []
    weight = ""
    if topics:
        cards = []
        for t in topics:
            cards.append(
                f'<div class="weight"><div class="wt">{t["id"]} · {esc(t["topic"])}</div>'
                f'<div class="wm"><span class="wbar"><i style="width:{min(100,t["marks_share"]*4):.0f}%"></i></span>'
                f'{t["marks_share"]:.1f}% marks · {t["freq_pct"]:.0f}% of papers</div></div>')
        weight = ('<div class="sec-title">Where the marks are — examiner weighting (top 6 spec topics)</div>'
                  f'<div class="weight-grid">{"".join(cards)}</div>')
    # steps
    steps = []
    for i, d in enumerate(M["order"], 1):
        bucket = M["domains"][d]
        col = dcolor(d)
        nqd = len(bucket["questions"])
        nmd = len(bucket["moves"])
        slug = DOMAIN_SLUG.get(d)
        domlink = (f'<a href="../{slug}.html" class="open" style="margin-left:auto">'
                   f'open in atlas →</a>') if slug else ""
        body = (f'<div class="lbl">Techniques to master — work top (Core) to bottom (A★)</div>'
                f'{render_tech(bucket["moves"])}'
                f'<div class="lbl">Problem set — {nqd} past-paper question{"s" if nqd!=1 else ""}, easiest first</div>'
                f'<div class="plist" data-step="{i}">{render_questions(M, bucket["questions"])}</div>'
                f'<div class="steptools"><button data-markall>Mark all done</button>'
                f'<button data-clearall>Clear</button></div>')
        steps.append(
            f'<details class="step"{" open" if i==1 else ""}>'
            f'<summary>'
            f'<span class="sn" style="background:{col}">{i}</span>'
            f'<span class="stitle"><h3><span class="qd" style="background:{col}"></span>{esc(d)}</h3>'
            f'<span class="sub">{nmd} techniques · {nqd} questions{("" )}</span></span>'
            f'<span class="sbarwrap"><div class="bar"><i class="sbar"></i></div></span>'
            f'<span class="scount">0 / {nqd} done</span>'
            f'<span class="chev">▸</span>'
            f'</summary><div class="body" data-step="{i}">{body}{domlink}</div></details>')
    legend = ('<div class="legend">'
              f'<span><span class="d" style="background:{TIER_DOT[T_CORE]}"></span>Core technique / easier question</span>'
              f'<span><span class="d" style="background:{TIER_DOT[T_BUILD]}"></span>Build</span>'
              f'<span><span class="d" style="background:{TIER_DOT[T_STAR]}"></span>A★ clincher / hardest</span>'
              '</div>')
    html_out = (
        page_head(f"{U} Mastery Path — Strategic Atlas") + topbar() +
        '<header class="hero"><div class="container">'
        f'<div class="breadcrumb"><a href="index.html">Mastery Path</a> / <strong>{U} · {esc(UNIT_NAME[U])}</strong></div>'
        f'<h1>{U} — {esc(UNIT_NAME[U])}</h1>'
        f'<p>Work through the steps in order. Each step: master the techniques (Core → A★), '
        f'then tick off its past-paper questions (easiest first). Finish every step and you have '
        f'covered every technique and every question this unit has ever asked.</p>'
        f'<div style="margin-top:14px"><span class="exam" data-exam="{EXAM_ISO[U]}" data-human="{EXAM_HUMAN[U]}">{EXAM_HUMAN[U]}</span></div>'
        f'<div class="bigprog"><div class="bar"><i id="unitBar"></i></div>'
        f'<span class="pc" id="unitPc">0% · 0 / {nq}</span></div>'
        f'{legend}'
        '</div></header><div class="container">' +
        weight +
        f'<div class="sec-title">The path — {len(M["order"])} steps · {ntech} techniques · {nq} questions</div>' +
        "".join(steps) +
        '<div class="callout"><b>How the order works.</b> Steps run high-yield → niche '
        '(the topic asked most often comes first). Inside each step, techniques are tiered '
        '<b>Core</b> (appears in 3+ questions), <b>Build</b> (2), <b>A★</b> (a one-off that '
        'separates an A from an A★); questions are sorted easiest → hardest by marks and the '
        'number of techniques they fuse. Progress is saved in this browser only.</div>'
        '</div>'
        f'<footer>Strategic Atlas · Mastery Path · {U} {esc(UNIT_NAME[U])} · Edexcel IAL</footer>'
        f'<script>{UNIT_JS}</script></body></html>')
    return html_out, M, nq, ntech

# ---------------- build all ----------------
unit_models = {}
unit_qids = {}
summary = {}
for U in UNITS:
    html_out, M, nq, ntech = render_unit_page(U)
    open(os.path.join(OUT, f"{U}.html"), "w").write(html_out)
    unit_models[U] = M
    qids = []
    for d in M["order"]:
        qids += [qid(q) for q in M["domains"][d]["questions"]]
    unit_qids[U] = qids
    summary[U] = dict(steps=len(M["order"]), tech=ntech, q=nq)

# ---------------- hub ----------------
def render_hub():
    order = sorted(UNITS, key=lambda u: EXAM_ISO[u])  # soonest exam first
    cards = []
    for U in order:
        col = dcolor(unit_models[U]["order"][0]) if unit_models[U]["order"] else "#5B6BFA"
        s = summary[U]
        cards.append(
            f'<a class="unit-card" href="{U}.html">'
            f'<div class="ub" style="background:{col}"></div>'
            f'<div class="uh"><div><h3>{U}</h3><div class="un">{esc(UNIT_NAME[U])}</div></div>'
            f'<span class="exam" data-exam="{EXAM_ISO[U]}" data-human="{EXAM_HUMAN[U]}">{EXAM_HUMAN[U]}</span></div>'
            f'<div class="meta"><span><b>{s["steps"]}</b> steps</span>'
            f'<span><b>{s["tech"]}</b> techniques</span><span><b>{s["q"]}</b> questions</span></div>'
            f'<div class="pcrow"><div class="bar" style="flex:1"><i id="bar-{U}"></i></div>'
            f'<span class="pc" id="pc-{U}">0%</span></div></a>')
    qjs = "window.UNITQIDS=" + json.dumps(unit_qids) + ";"
    total_q = sum(len(v) for v in unit_qids.values())
    total_t = len(set(m["slug"] for m in moves))  # distinct techniques (a move can span units)
    return (
        page_head("Mastery Path — Strategic Atlas") + topbar() +
        '<header class="hero"><div class="container">'
        '<div class="breadcrumb"><a href="../index.html">← Strategic Atlas</a></div>'
        '<h1>Mastery Path</h1>'
        '<p>A step-by-step route through <b>every technique and every past-paper question</b> in '
        'Edexcel IAL Pure &amp; Further Pure — sequenced foundation → A★. Pick a unit, work the '
        'steps in order, tick off each problem as you crack it. Your progress is saved on this '
        'device.</p>'
        '<div class="bigprog"><div class="bar"><i id="overallBar"></i></div>'
        '<span class="pc" id="overallPc">0%</span></div>'
        '</div></header><div class="container">'
        f'<div class="sec-title">Units — ordered by exam date · {len(UNITS)} units · {total_t} techniques · {total_q} questions</div>'
        f'<div class="units">{"".join(cards)}</div>'
        '<div class="callout"><b>How to use it.</b> Each unit is split into ordered <b>steps</b> '
        '(one per topic area, most-examined first). A step gives you the <b>techniques to master</b> '
        '— tiered Core → Build → A★ — then a <b>problem set</b> of the real past-paper questions that '
        'test them, easiest first. Tick a question once you can do it unaided. The bars fill as you go; '
        'reach 100% on every unit and there is no past-paper move you have not drilled.</div>'
        '</div>'
        '<footer>Strategic Atlas · Mastery Path · Edexcel IAL Maths / Further Maths · Pure + Further Pure</footer>'
        f'<script>{qjs}</script><script>{HUB_JS}</script></body></html>')

open(os.path.join(OUT, "index.html"), "w").write(render_hub())

# ---------------- coverage audit ----------------
print("=== MASTERY PATH BUILD ===")
all_assigned_moves = set()
all_assigned_q = set()
for U in UNITS:
    M = unit_models[U]
    mv = set(m["slug"] for m in M["um"])
    qs = set()
    for d in M["order"]:
        for m in M["domains"][d]["moves"]: all_assigned_moves.add(m["slug"])
        for q in M["domains"][d]["questions"]: qs.add(qid(q)); all_assigned_q.add(qid(q))
    # every unit move in exactly one step?
    step_moves = [m["slug"] for d in M["order"] for m in M["domains"][d]["moves"]]
    dup = [x for x,c in Counter(step_moves).items() if c>1]
    print(f"{U}: {summary[U]['steps']} steps · {summary[U]['tech']} techniques · "
          f"{summary[U]['q']} questions · dup_moves={len(dup)}")
print("---")
print("distinct moves covered:", len(all_assigned_moves), "/ 1630")
print("distinct questions covered:", len(all_assigned_q))
print("pages written:", len(UNITS)+1, "->", OUT)
