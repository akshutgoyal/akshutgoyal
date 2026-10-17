#!/usr/bin/env python3
"""Generate the neofetch-style profile banner (dark + light variants).

Modelled on github.com/Andrew6rant/Andrew6rant, which renders its profile
head as a single self-contained SVG: an ASCII-art portrait drawn in
monospace text on the left, a neofetch key/value block on the right, both
syntax-highlighted with GitHub's own theme colours.

Matching his technique means the portrait is *text*, not an embedded raster
image -- so there is no base64 payload, the file stays ~6 KB, and the
portrait recolours with the theme instead of being a fixed photo.

Two things this particular source photo needs that the reference banner's
does not, because his is a face against a plain dark wall:

  1. GrabCut, to lift the cat off a busy tiled background. Without it the
     grout lines and wall stains render as noise and swamp the subject.
  2. A short 10-level ramp. A long ramp (60+ glyphs) resolves to
     high-frequency mush at 38x25 cells; ten levels read as shapes.

Deps: pillow, numpy, opencv-python
Run:  python3 tools/gen_banner.py
Out:  banner-dark.svg, banner-light.svg
"""

import sys
import urllib.request
from io import BytesIO
from pathlib import Path

try:
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("needs pillow, numpy and opencv-python:\n"
             "  pip install pillow numpy opencv-python")

# ---------------------------------------------------------------- geometry
W, H = 985, 530
RADIUS = 15
FONT_SIZE = 16
ROW_STEP = 20
CHAR_W = 9.6              # monospace advance, worst case

ART_X0 = 15
ART_X1 = 390              # left column must stay clear of this
INFO_X = 390
INFO_COLS = 60
VALUE_COL = 25

ART_COLS, ART_ROWS = 38, 25
ART_TOP = 30

# ---------------------------------------------------------------- avatar
AVATAR_URL = "https://avatars.githubusercontent.com/u/291477182?s=460&v=4"
GRABCUT_RECT = (30, 20, 400, 400)   # x, y, w, h around the subject
GRABCUT_ITERS = 6
CLAHE_CLIP = 3.0
BLACK, WHITE = 70, 150              # tonal window mapped across the ramp

# Lightest ink to densest. Deliberately short -- see module docstring.
RAMP = " .:-=+*#%@"

# --------------------------------------------------------------- content
INFO = [
    ("H1", "akshut@goyal"),
    ("KV", ". Location", "Delhi, India"),
    ("KV", ". Education", "B.Tech @ DTU"),
    ("KV", ". OS", "Arch Linux, Android"),
    ("KV", ". Coding since", "2022"),
    ("SP",),
    ("KV", ". Focus", "Local-first software, Linux tooling"),
    ("KV", ". Languages.Code", "Python, TypeScript, C, Solidity"),
    ("KV", ". Languages.Markup", "HTML, CSS, JSON, YAML"),
    ("KV", ". Languages.Real", "English, Hindi"),
    ("SP",),
    ("KV", ". Desktop", "GTK4/libadwaita, Qt/PySide6"),
    ("KV", ". Backend", "Bun, FastAPI, SQLite, Laravel"),
    ("KV", ". Blockchain", "Solidity, ethers.js, OpenZeppelin"),
    ("KV", ". On-device ML", "PyTorch, YOLOv8, ONNX, TFLite"),
    ("KV", ". Automation", "Playwright, GitHub Actions"),
    ("SP",),
    ("H2", "Contact"),
    ("KV", ". Email", "akshutgoyal@gmail.com"),
    ("KV", ". GitHub", "akshutgoyal"),
    ("KV", ". LinkedIn", "akshut"),
    ("KV", ". Portfolio", "akshutgoyal.github.io"),
    ("SP",),
    ("H2", "Currently"),
    ("KV", ". Building", "The Aethel suite (16 tools)"),
]

# --------------------------------------------------------------- theming
# Colour values mirror the reference banner's dark/light palettes.
THEMES = {
    "dark": {
        "bg": "#161b22",
        "fg": "#c9d1d9",
        "key": "#ffa657",
        "value": "#a5d6ff",
        "cc": "#616e7f",
    },
    "light": {
        "bg": "#f6f8fa",
        "fg": "#24292f",
        "key": "#953800",
        "value": "#0a3069",
        "cc": "#c2cfde",
    },
}


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def subject_image() -> Image.Image:
    """Fetch the avatar and isolate the subject on a flat white field."""
    req = urllib.request.Request(
        AVATAR_URL, headers={"User-Agent": "akshutgoyal-profile-banner"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()

    bgr = cv2.imdecode(np.frombuffer(raw, np.uint8), cv2.IMREAD_COLOR)
    mask = np.zeros(bgr.shape[:2], np.uint8)
    bgd = np.zeros((1, 65), np.float64)
    fgd = np.zeros((1, 65), np.float64)
    cv2.grabCut(
        bgr, mask, GRABCUT_RECT, bgd, fgd, GRABCUT_ITERS, cv2.GC_INIT_WITH_RECT
    )
    m = np.where(
        (mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0
    ).astype(np.uint8)
    k = np.ones((7, 7), np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, k)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, k)

    grey = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    grey = cv2.createCLAHE(clipLimit=CLAHE_CLIP, tileGridSize=(8, 8)).apply(grey)

    ys, xs = np.where(m > 0)
    h, w = m.shape
    x0, x1 = max(0, xs.min()), min(w, xs.max())
    y0, y1 = max(0, ys.min()), min(h, ys.max())
    sub_g = grey[y0:y1, x0:x1].astype(np.float32)
    sub_m = m[y0:y1, x0:x1].astype(np.float32) / 255.0

    # Flat white background maps to the space character at the end of the ramp.
    flat = sub_g * sub_m + 255.0 * (1.0 - sub_m)
    return Image.fromarray(flat.astype(np.uint8))


def ascii_portrait() -> list[str]:
    img = subject_image()

    # A cell is 9.6 x 20 px, so the character grid is far taller than wide.
    # Crop the source to that ratio first or the portrait comes out stretched.
    target = (ART_COLS * CHAR_W) / (ART_ROWS * ROW_STEP)
    w, h = img.size
    if w / h > target:
        nw = h * target
        img = img.crop(((w - nw) / 2, 0, (w - nw) / 2 + nw, h))
    else:
        nh = w / target
        img = img.crop((0, (h - nh) / 2, w, (h - nh) / 2 + nh))

    img = img.resize((ART_COLS, ART_ROWS), Image.LANCZOS)
    px = img.load()

    rows = []
    for y in range(ART_ROWS):
        row = []
        for x in range(ART_COLS):
            lum = max(0.0, min(1.0, (px[x, y] - BLACK) / (WHITE - BLACK)))
            # Dark pixels become dense glyphs, so on the dark card the subject
            # reads as the lit region -- how ASCII art behaves on a terminal.
            row.append(RAMP[min(len(RAMP) - 1, int((1.0 - lum) * len(RAMP)))])
        rows.append("".join(row))
    return rows


def build(theme_name: str, art: list[str]) -> str:
    c = THEMES[theme_name]

    # Art rows are centred against the 25-row info column.
    pad = (len(INFO) - len(art)) // 2
    art_svg = []
    for i, row in enumerate(art):
        y = ART_TOP + (i + pad) * ROW_STEP
        art_svg.append(f'<tspan x="{ART_X0}" y="{y}">{esc(row)}</tspan>')

    info_svg = []
    for i, row in enumerate(INFO):
        y = ART_TOP + i * ROW_STEP
        kind = row[0]

        if kind == "SP":
            info_svg.append(f'<tspan x="{INFO_X}" y="{y}" class="cc">. </tspan>')
        elif kind in ("H1", "H2"):
            label = row[1] if kind == "H1" else f"- {row[1]}"
            info_svg.append(
                f'<tspan x="{INFO_X}" y="{y}">{esc(label)} '
                f'{"─" * (INFO_COLS - len(label) - 1)}</tspan>'
            )
        else:
            _, key, value = row
            fill = max(1, VALUE_COL - len(f". {key}:") - 1)
            info_svg.append(
                f'<tspan x="{INFO_X}" y="{y}" class="cc">. </tspan>'
                f'<tspan class="key">{esc(key)}</tspan>'
                f'<tspan class="cc">:{"." * fill} </tspan>'
                f'<tspan class="value">{esc(value)}</tspan>'
            )

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"
     font-family="ConsolasFallback,Consolas,monospace" font-size="{FONT_SIZE}">
<style>
@font-face {{
  src: local('Consolas'), local('Consolas Bold');
  font-family: 'ConsolasFallback';
  font-display: swap;
  size-adjust: 109%;
}}
.key   {{fill: {c['key']};}}
.value {{fill: {c['value']};}}
.cc    {{fill: {c['cc']};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="{W}" height="{H}" fill="{c['bg']}" rx="{RADIUS}"/>
<text x="{ART_X0}" y="{ART_TOP}" fill="{c['fg']}">
{chr(10).join(art_svg)}
</text>
<text x="{INFO_X}" y="{ART_TOP}" fill="{c['fg']}">
{chr(10).join(info_svg)}
</text>
</svg>
"""


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    art = ascii_portrait()
    for name in ("dark", "light"):
        out = root / f"banner-{name}.svg"
        out.write_text(build(name, art), encoding="utf-8")
        print(f"wrote {out.relative_to(root)}  ({out.stat().st_size / 1024:.1f} KB)")
    print()
    print("\n".join(art))


if __name__ == "__main__":
    main()
