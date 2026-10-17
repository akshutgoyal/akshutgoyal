#!/usr/bin/env python3
"""Generate the neofetch-style profile banner (dark + light variants).

Inspired by github.com/Andrew6rant/Andrew6rant, which renders its profile
head as a self-contained SVG rather than a README of markdown widgets.

The left column is the GitHub avatar, downsampled to a 64x64 pixel grid and
embedded as a base64 PNG. It has to be embedded rather than linked: an SVG
rendered via <img> (which is how GitHub shows it) cannot load external
resources, so a remote href would silently render as nothing.

Deps: pillow  (pip install pillow)
Run:  python3 tools/gen_banner.py
Out:  banner-dark.svg, banner-light.svg
"""

import base64
import sys
import urllib.request
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image, ImageEnhance
except ImportError:
    sys.exit("needs pillow:  pip install pillow")

# ---------------------------------------------------------------- geometry
W, H = 985, 530
RADIUS = 15

FONT_STACK = "Consolas,Menlo,DejaVu Sans Mono,monospace"
FONT_SIZE = 16
ROW_STEP = 20

ART_X0, ART_X1 = 15, 390  # left column bounds
INFO_X = 390              # right column origin
INFO_COLS = 60            # characters that fit, with headroom for wider fonts
VALUE_COL = 25            # column where values start

# ---------------------------------------------------------------- avatar
AVATAR_URL = "https://avatars.githubusercontent.com/u/291477182?s=460&v=4"
AVATAR_PX = 64            # pixel grid of the portrait
IMG_SIZE = 360            # on-canvas size
IMG_RADIUS = 16
CONTRAST = 1.30           # the source photo is flat and hazy
SATURATION = 1.35

# --------------------------------------------------------------- content
# Every value below is drawn from the profile README / public repos.
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
        "cc": "#6e7781",
    },
}


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def avatar_data_uri() -> tuple[str, int]:
    """Fetch the avatar, pixelate it, return (data URI, PNG byte count)."""
    req = urllib.request.Request(
        AVATAR_URL, headers={"User-Agent": "akshutgoyal-profile-banner"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()

    img = Image.open(BytesIO(raw)).convert("RGB")
    img = img.resize((AVATAR_PX, AVATAR_PX), Image.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(CONTRAST)
    img = ImageEnhance.Color(img).enhance(SATURATION)

    buf = BytesIO()
    img.save(buf, format="PNG", optimize=True)
    png = buf.getvalue()
    return "data:image/png;base64," + base64.b64encode(png).decode(), len(png)


def build(theme_name: str, uri: str) -> str:
    c = THEMES[theme_name]

    ix = (ART_X0 + ART_X1) // 2 - IMG_SIZE // 2
    iy = (H - IMG_SIZE) // 2

    # ---- right column: neofetch-style key/value listing ----
    info_svg = []
    for i, row in enumerate(INFO):
        y = 30 + i * ROW_STEP
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
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{W}" height="{H}" font-family="{FONT_STACK}" font-size="{FONT_SIZE}">
<style>
.key   {{fill: {c['key']};}}
.value {{fill: {c['value']};}}
.cc    {{fill: {c['cc']};}}
text, tspan {{white-space: pre;}}
.av {{image-rendering: pixelated; image-rendering: crisp-edges;}}
</style>
<defs>
  <clipPath id="avclip">
    <rect x="{ix}" y="{iy}" width="{IMG_SIZE}" height="{IMG_SIZE}" rx="{IMG_RADIUS}"/>
  </clipPath>
</defs>
<rect width="{W}" height="{H}" fill="{c['bg']}" rx="{RADIUS}"/>
<image class="av" x="{ix}" y="{iy}" width="{IMG_SIZE}" height="{IMG_SIZE}"
       href="{uri}" xlink:href="{uri}" clip-path="url(#avclip)" preserveAspectRatio="none"/>
<text x="{INFO_X}" y="30" fill="{c['fg']}">
{chr(10).join(info_svg)}
</text>
</svg>
"""


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    uri, png_bytes = avatar_data_uri()
    print(f"avatar: {AVATAR_PX}x{AVATAR_PX} png, {png_bytes / 1024:.1f} KB")
    for name in ("dark", "light"):
        out = root / f"banner-{name}.svg"
        out.write_text(build(name, uri), encoding="utf-8")
        print(f"wrote {out.relative_to(root)}  ({out.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
