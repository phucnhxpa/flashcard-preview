#!/usr/bin/env python3
"""Deterministic browser render + audit for the M1 multistep_v2 deck.

Renders every card to a literal static PNG (desktop + mobile) with Playwright +
system Chromium, captures console/page errors, overflow and MathJax metrics, and
writes browser_audit.json. Also writes desktop/mobile contact sheets.
"""
from __future__ import annotations
import asyncio, functools, json, threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent
CARDS = ["ESAT_warmup", "M1_WME01_Q2", "M1_WME01_Q1", "M1_WME01_Q4",
         "M1_WME01_Q3", "M1_WME01_Q5", "M1_WME01_Q6", "M1_WME01_Q7", "M1_WME01_Q8"]

async def render_and_audit():
    audits = []
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    server = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT)))
    thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(executable_path="/usr/bin/chromium",
                                               headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
            for viewport, suffix in [({"width":1280,"height":900}, "desktop"), ({"width":390,"height":900}, "mobile")]:
                for slug in CARDS:
                    page = await browser.new_page(viewport=viewport)
                    console = []; errors = []
                    page.on("console", lambda m, c=console: c.append(f"{m.type}: {m.text}") if m.type == "error" else None)
                    page.on("pageerror", lambda e, c=errors: c.append(str(e)))
                    await page.goto(f"{base}/{slug}.html", wait_until="networkidle")
                    await page.wait_for_function("window.MathJax && window.MathJax.startup && window.MathJax.startup.promise")
                    await page.evaluate("window.MathJax.startup.promise")
                    await page.wait_for_timeout(700)
                    metrics = await page.evaluate("""() => ({
                        scrollWidth: document.documentElement.scrollWidth,
                        clientWidth: document.documentElement.clientWidth,
                        math: document.querySelectorAll('mjx-container').length,
                        parts: document.querySelectorAll('.part-title').length,
                        carry: document.querySelectorAll('.carry-in').length,
                        work: document.querySelectorAll('.work').length,
                        toggles: document.querySelectorAll('.mask-toggle').length,
                        ariaExpanded: [...document.querySelectorAll('.mask-toggle')].filter(b=>b.getAttribute('aria-expanded')==='true').length,
                        exportHref: document.querySelector('.export-btn') ? document.querySelector('.export-btn').getAttribute('href') : null,
                        overflows: [...document.querySelectorAll('mjx-container, svg, table, .part, .q-header, .work')].filter(e=>{const r=e.getBoundingClientRect();return r.right>innerWidth+1||r.left<-1;}).length
                    })""")
                    target = ROOT / f"{slug}.png" if suffix == "desktop" else ROOT / f"mobile_{slug}.png"
                    await page.screenshot(path=str(target), full_page=True)
                    audits.append({"card": slug, "viewport": suffix, "metrics": metrics,
                                   "console_errors": console, "page_errors": errors})
                    await page.close()
                # landing
                page = await browser.new_page(viewport=viewport)
                console = []; errors = []
                page.on("console", lambda m, c=console: c.append(f"{m.type}: {m.text}") if m.type == "error" else None)
                page.on("pageerror", lambda e, c=errors: c.append(str(e)))
                await page.goto(f"{base}/index.html", wait_until="networkidle")
                await page.wait_for_timeout(400)
                lm = await page.evaluate("""() => ({
                    tiles: document.querySelectorAll('.tile').length,
                    images: [...document.images].map(i=>({src:i.getAttribute('src'),complete:i.complete,width:i.naturalWidth})),
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth
                })""")
                await page.screenshot(path=str(ROOT / f"{suffix}_landing.png"), full_page=True)
                audits.append({"card": "landing", "viewport": suffix, "metrics": lm,
                               "console_errors": console, "page_errors": errors})
                await page.close()
            await browser.close()
    finally:
        server.shutdown(); server.server_close(); thread.join()
    (ROOT / "browser_audit.json").write_text(json.dumps(audits, indent=2) + "\n")

    # Contact sheets (montage via PIL).
    try:
        from PIL import Image
        make_contact_sheet([ROOT / f"{s}.png" for s in CARDS], ROOT / "contact_sheet_desktop.png", "desktop")
        make_contact_sheet([ROOT / f"mobile_{s}.png" for s in CARDS], ROOT / "contact_sheet_mobile.png", "mobile")
    except Exception as e:
        print("contact sheet skipped:", e)

def make_contact_sheet(paths, out, tag):
    from PIL import Image
    valid = [p for p in paths if p.exists()]
    if not valid:
        return
    thumbs = []
    tw = 360
    for p in valid:
        im = Image.open(p); ratio = tw / im.width; thumbs.append(im.resize((tw, int(im.height * ratio))))
    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    pad = 8
    maxh = max(t.height for t in thumbs)
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * pad, rows * (maxh + pad) + pad), "white")
    for i, t in enumerate(thumbs):
        r, c = divmod(i, cols)
        x = pad + c * (tw + pad); y = pad + r * (maxh + pad)
        sheet.paste(t, (x, y))
    sheet.save(out)
    print(f"wrote {out} ({len(valid)} tiles)")

if __name__ == "__main__":
    asyncio.run(render_and_audit())
