import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
html_path = ROOT / "zeiss_demo.html"
embed_path = ROOT / "slide-data-embed.js"

html = html_path.read_text(encoding="utf-8")
embed = embed_path.read_text(encoding="utf-8").strip()
helper = "function slideUrl(n){return SLIDE_DATA[n]}\n"

marker = "<script>\n"
if marker not in html:
    raise SystemExit("script marker missing")
if "const SLIDE_DATA=" not in html:
    html = html.replace(marker, "<script>\n" + embed + "\n" + helper + "\n", 1)

html = html.replace(
    ".zslide-cover .cover-bg{position:absolute;inset:0;background:url(slides/slide_002.png) center/cover}",
    ".zslide-cover .cover-bg{position:absolute;inset:0;background:center/cover no-repeat}",
)
html = html.replace(
    ".zslide-enjeux .enj-bg{position:absolute;inset:0;background:url(slides/slide_005.png) center/cover}",
    ".zslide-enjeux .enj-bg{position:absolute;inset:0;background:center/cover no-repeat}",
)

html = html.replace(
    '<div class="cover-bg"></div>',
    '<div class="cover-bg" style="background-image:url(${slideUrl(2)})"></div>',
    1,
)
html = html.replace(
    '<div class="enj-bg"></div>',
    '<div class="enj-bg" style="background-image:url(${slideUrl(5)})"></div>',
    1,
)

replacements = [
    (
        'src="slides/slide_\'+String(d.n).padStart(3,\'0\')+\'.png"',
        'src="\'+slideUrl(d.n)+\'"',
    ),
    (
        'src="slides/slide_\'+String(n).padStart(3,\'0\')+\'.png"',
        'src="\'+slideUrl(n)+\'"',
    ),
    (
        "'slides/slide_'+String(d.n).padStart(3,'0')+'.png'",
        "slideUrl(d.n)",
    ),
    (
        "'slides/slide_'+String(n).padStart(3,'0')+'.png'",
        "slideUrl(n)",
    ),
    ('src="slides/slide_006.png"', 'src="${slideUrl(6)}"'),
    ('src="slides/slide_012.png"', 'src="${slideUrl(12)}"'),
    ('src="slides/slide_020.png"', 'src="${slideUrl(20)}"'),
    ('src="slides/slide_035.png"', 'src="${slideUrl(35)}"'),
    ('src="slides/slide_002.png"', 'src="${slideUrl(2)}"'),
    (
        'src="slides/slide_${String(g.n).padStart(3,\'0\')}.png"',
        'src="${slideUrl(g.n)}"',
    ),
]
for old, new in replacements:
    html = html.replace(old, new)

if "slides/slide_" in html:
    remaining = sorted(set(re.findall(r"slides/slide_[^\"')]+", html)))
    if remaining:
        raise SystemExit("unresolved slide paths: " + ", ".join(remaining))

html_path.write_text(html, encoding="utf-8")
print("embedded", html_path, "size", html_path.stat().st_size)
