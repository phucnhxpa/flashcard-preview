#!/usr/bin/env python3
"""Render all cards with Chromium + deterministic local browser audit."""
from __future__ import annotations
import json, shutil
from pathlib import Path
from urllib.parse import unquote, urlparse
from playwright.sync_api import sync_playwright
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parent
CARDS = ["ESAT_warmup", "P3_Oct2025_Q2", "P3_Oct2025_Q3", "P3_Oct2025_Q4", "P3_Oct2025_Q5"]
MOBILE = ROOT / "_mobile_qa"

def relative_asset_check():
    import re
    failures=[]; checked=[]
    for html in [ROOT/"index.html", *[ROOT/f"{s}.html" for s in CARDS]]:
        text=html.read_text(encoding="utf-8")
        for val in re.findall(r'(?:href|src)="([^"]+)"', text):
            if val.startswith(("http:","https:","data:","#")): continue
            dest=(html.parent/unquote(urlparse(val).path)).resolve()
            checked.append({"from":html.name,"asset":val,"exists":dest.exists(),"inside_root":str(dest).startswith(str(ROOT.resolve()))})
            if not dest.exists() or not str(dest).startswith(str(ROOT.resolve())): failures.append(checked[-1])
    return checked, failures

def boxes(page, selector, width):
    return page.eval_on_selector_all(selector, """(els,w)=>els.map(e=>{const r=e.getBoundingClientRect(); return {selector:e.matches('.q-header')?'.q-header':e.className||e.tagName,left:r.left,right:r.right,top:r.top,bottom:r.bottom,overflow:r.left < -1 || r.right>w+1}})""", width)

def contact_sheet(paths, dest, cols=2):
    imgs=[Image.open(p).convert("RGB") for p in paths]
    thumbw=500; gap=16; labelh=28
    thumbs=[]
    for path,img in zip(paths,imgs):
        ratio=thumbw/img.width; h=max(1,int(img.height*ratio)); im=img.resize((thumbw,h))
        canvas=Image.new("RGB",(thumbw,h+labelh),"white"); canvas.paste(im,(0,labelh)); ImageDraw.Draw(canvas).text((8,7),path.stem,fill="#172033"); thumbs.append(canvas)
    rows=(len(thumbs)+cols-1)//cols; row_heights=[max(t.height for t in thumbs[i*cols:(i+1)*cols]) for i in range(rows)]
    out=Image.new("RGB",(cols*thumbw+(cols+1)*gap,sum(row_heights)+(rows+1)*gap),"#f3f5f8")
    y=gap
    for row in range(rows):
        x=gap
        for t in thumbs[row*cols:(row+1)*cols]: out.paste(t,(x,y)); x+=thumbw+gap
        y+=row_heights[row]+gap
    out.save(dest)

def main():
    MOBILE.mkdir(exist_ok=True)
    audit={"renderer":"Playwright Python + /usr/bin/chromium","mathjax_renderer":"tex-svg.js","desktop":{"viewport":{"width":1280,"height":900,"device_scale_factor":2}},"mobile":{"viewport":{"width":390,"height":844,"device_scale_factor":1}},"cards":{},"landing":{},"asset_resolution":{}}
    assets, failures=relative_asset_check(); audit["asset_resolution"]={"checked":assets,"failures":failures}
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path="/usr/bin/chromium",headless=True,args=["--no-sandbox","--disable-dev-shm-usage","--allow-file-access-from-files"])
        for slug in CARDS:
            per={}
            for label, viewport, screenshot in [("desktop",{"width":1280,"height":900},ROOT/f"{slug}.png"),("mobile",{"width":390,"height":844},MOBILE/f"{slug}.png")]:
                context=browser.new_context(viewport=viewport,device_scale_factor=2 if label=="desktop" else 1)
                page=context.new_page(); messages=[]; errors=[]
                page.on("console",lambda m,arr=messages: arr.append({"type":m.type,"text":m.text}) if m.type in ("error","warning") else None)
                page.on("pageerror",lambda e,arr=errors: arr.append(str(e)))
                page.goto((ROOT/f"{slug}.html").as_uri(),wait_until="networkidle")
                page.wait_for_function("window.MathJax && window.MathJax.startup && window.MathJax.startup.promise")
                page.evaluate("() => MathJax.startup.promise")
                page.wait_for_timeout(3000)
                page.add_style_tag(content=".export-btn{display:none!important}")
                width=viewport["width"]
                overflow=page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")
                math_count=page.locator("mjx-container").count()
                target=page.locator("#card"); target.screenshot(path=str(screenshot))
                selector_boxes=boxes(page,"mjx-container, svg, table, .q-header, .part, .carry-in, .why",width)
                per[label]={"console":messages,"page_errors":errors,"mathjax_containers":math_count,"horizontal_overflow":overflow,"overflow_boxes":[b for b in selector_boxes if b["overflow"]],"screenshot":screenshot.name,"screenshot_bytes":screenshot.stat().st_size}
                context.close()
            text=(ROOT/f"{slug}.html").read_text(encoding="utf-8")
            per["static"]={"part_count":text.count('class="part"'),"carry_in_count":text.count('class="carry-in"'),"visual_anchor_count":text.count('class="q-diagram"'),"literal_export_target":f'href="{slug}.png"' in text}
            audit["cards"][slug]=per
        context=browser.new_context(viewport={"width":1280,"height":900}); page=context.new_page(); landing_errors=[]; page.on("pageerror",lambda e:landing_errors.append(str(e))); page.goto((ROOT/"index.html").as_uri(),wait_until="networkidle"); page.wait_for_timeout(500)
        audit["landing"]["desktop"]={"tile_count":page.locator(".tile").count(),"images":page.locator(".tile img").count(),"horizontal_overflow":page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth"),"page_errors":landing_errors}; context.close()
        context=browser.new_context(viewport={"width":390,"height":844}); page=context.new_page(); page.goto((ROOT/"index.html").as_uri(),wait_until="networkidle"); page.wait_for_timeout(500)
        audit["landing"]["mobile"]={"tile_count":page.locator(".tile").count(),"images":page.locator(".tile img").count(),"horizontal_overflow":page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")}; context.close(); browser.close()
    contact_sheet([ROOT/f"{s}.png" for s in CARDS],ROOT/"contact_sheet_desktop.png")
    contact_sheet([MOBILE/f"{s}.png" for s in CARDS],ROOT/"contact_sheet_mobile.png")
    shutil.rmtree(MOBILE)
    (ROOT/"browser_audit.json").write_text(json.dumps(audit,indent=2),encoding="utf-8")
    print(json.dumps({"cards":len(CARDS),"asset_failures":len(failures),"browser_audit":"browser_audit.json"}))

if __name__=="__main__": main()
