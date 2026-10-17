#!/usr/bin/env python3
"""Generate the neofetch-style profile banner (dark + light variants).

Inspired by github.com/Andrew6rant/Andrew6rant, which renders its profile
head as a self-contained SVG rather than a README of markdown widgets.

Two deliberate departures from the original:
  * The left column is the name in block letters rather than an ASCII face.
  * Those letters are drawn as <rect>s, not text. U+2588 FULL BLOCK renders
    at wildly different widths across monospace fonts, which shreds the
    glyphs; rectangles look identical everywhere.

Run:  python3 tools/gen_banner.py
Out:  banner-dark.svg, banner-light.svg
"""

from pathlib import Path

# ---------------------------------------------------------------- geometry
W, H = 985, 530
RADIUS = 15

FONT_STACK = "Consolas,Menlo,DejaVu Sans Mono,monospace"
FONT_SIZE = 16
CHAR_W = FONT_SIZE * 0.6  # worst-case monospace advance width
ROW_STEP = 20

ART_X0, ART_X1 = 15, 390  # left column bounds
INFO_X = 390              # right column origin
INFO_COLS = 60            # characters that fit, with headroom for wider fonts
VALUE_COL = 25            # column where values start

CELL_W, CELL_H = 10, 20   # block-letter cell size
GLYPH_COLS, GLYPH_ROWS = 5, 5
GAP_CELLS = 1             # blank cells between glyphs
WORD_GAP = 14             # vertical gap between the two words

# ------------------------------------------------------------- block font
FONT = {
    "A": ["01110", "10001", "11111", "10001", "10001"],
    "G": ["01111", "10000", "10011", "10001", "01111"],
    "H": ["10001", "10001", "11111", "10001", "10001"],
    "K": ["10001", "10010", "11100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "11111"],
    "O": ["01110", "10001", "10001", "10001", "01110"],
    "S": ["01111", "10000", "01110", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "01110"],
    "Y": ["10001", "10001", "00100", "00100", "00100"],
}


def word_cells(word: str) -> int:
    return len(word) * GLYPH_COLS + (len(word) - 1) * GAP_CELLS


def word_rects(word: str, y0: int, centre_x: float) -> str:
    """Draw `word` as filled rectangles, horizontally centred on centre_x."""
    x0 = centre_x - word_cells(word) * CELL_W / 2
    out = []
    for gi, ch in enumerate(word):
        glyph = FONT[ch]
        gx = gi * (GLYPH_COLS + GAP_CELLS)
        for ry, row in enumerate(glyph):
            for cx, bit in enumerate(row):
                if bit != "1":
                    continue
                x = x0 + (gx + cx) * CELL_W
                y = y0 + ry * CELL_H
                out.append(
                    f'<rect x="{x:.1f}" y="{y:.1f}" '
                    f'width="{CELL_W - 1.5:.1f}" height="{CELL_H - 1.5:.1f}"/>'
                )
    return "\n".join(out)


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

TAGLINES = ["local-first · systems · blockchain", "one engine, several surfaces"]

# --------------------------------------------------------------- theming
THEMES = {
    "dark": {
        "bg": "#161b22",
        "fg": "#c9d1d9",
        "key": "#ffa657",
        "value": "#a5d6ff",
        "cc": "#616e7f",
        "g1": "#58a6ff",
        "g2": "#bc8cff",
    },
    "light": {
        "bg": "#f6f8fa",
        "fg": "#24292f",
        "key": "#953800",
        "value": "#0a3069",
        "cc": "#6e7781",
        "g1": "#0969da",
        "g2": "#8250df",
    },
}


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(theme_name: str) -> str:
    c = THEMES[theme_name]
    centre_x = (ART_X0 + ART_X1) / 2

    # ---- left column: block-letter name over two taglines ----
    art_h = GLYPH_ROWS * CELL_H * 2 + WORD_GAP
    tag_h = len(TAGLINES) * 22
    total_h = art_h + 40 + tag_h
    top = (H - total_h) / 2

    art_svg = word_rects("AKSHUT", top, centre_x)
    art_svg += "\n" + word_rects(
        "GOYAL", top + GLYPH_ROWS * CELL_H + WORD_GAP, centre_x
    )

    tag_top = top + art_h + 40
    tag_svg = [
        f'<tspan x="{centre_x - len(t) * CHAR_W / 2:.0f}" '
        f'y="{tag_top + 16 + i * 22:.0f}">{esc(t)}</tspan>'
        for i, t in enumerate(TAGLINES)
    ]

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
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"
     font-family="{FONT_STACK}" font-size="{FONT_SIZE}">
<style>
.key   {{fill: {c['key']};}}
.value {{fill: {c['value']};}}
.cc    {{fill: {c['cc']};}}
text, tspan {{white-space: pre;}}
</style>
<defs>
  <linearGradient id="art" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{c['g1']}"/>
    <stop offset="100%" stop-color="{c['g2']}"/>
  </linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="{c['bg']}" rx="{RADIUS}"/>
<g fill="url(#art)">
{art_svg}
</g>
<text x="{ART_X0}" y="30" class="cc">
{chr(10).join(tag_svg)}
</text>
<text x="{INFO_X}" y="30" fill="{c['fg']}">
{chr(10).join(info_svg)}
</text>
</svg>
"""


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    for name in ("dark", "light"):
        out = root / f"banner-{name}.svg"
        out.write_text(build(name), encoding="utf-8")
        print(f"wrote {out.relative_to(root)}")


if __name__ == "__main__":
    main()
