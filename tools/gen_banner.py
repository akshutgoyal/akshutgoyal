#!/usr/bin/env python3
"""Generate the neofetch-style profile banner (dark + light variants).

Modelled on github.com/Andrew6rant/Andrew6rant, which renders its profile
head as a single self-contained SVG: an ASCII-art portrait drawn in
monospace text on the left, a neofetch key/value block on the right, both
syntax-highlighted with GitHub's own theme colours.

Matching his technique means the portrait is *text*, not an embedded raster
image -- so there is no base64 payload, the file stays ~6 KB, and the
portrait recolours with the theme instead of being a fixed photo.

His photo is a face against a plain dark wall. This one is a dark cat lying on
a light tiled floor, which turns out to need a different treatment. Five things
that were not obvious going in:

  1. GrabCut, to lift the cat off that busy tiled background. Without it the
     grout lines and wall stains render as noise and swamp the subject.
  2. The mask used as a gate, not merely a cut-out. Tone alone cannot hold
     this silhouette: the cat's chest and the top of its head are as light as
     the wall behind them, so keying off brightness alone leaves holes through
     the body. The mask decides which cells are cat; tone only chooses glyph.
  3. A tonal window measured from the subject rather than guessed. This cat's
     median sits near 91 and its lit fur reaches 238, so the 70..150 window
     that looked reasonable erased about three quarters of it.
  4. Glyphs chosen by MEASURED coverage, not by their order in the ramp. A
     ramp like " .:-=+*#%@" assumes each glyph prints a little more than the
     last, and at these sizes that is simply false: ':' and '-' measure 0.049
     and 0.051, '+' and '*' both measure 0.157, and '#' prints denser than
     '@'. Sorting by measurement is what stops the portrait going flat.
  5. The background drawn as a faint glyph field rather than left empty. The
     cat is DARKER than its background and the card is dark, so no single
     mapping works: natural order sinks the cat into the card, and inverted
     order flips its own shading so its dark head becomes the brightest thing
     in the frame. Giving the background a fixed sparse glyph and ordering the
     cat's tones naturally above it sidesteps both -- the card then reads the
     way the photo does, a pale form against a quiet field.

Framing matters as much as any of those. Shot whole, the cat's head occupies
only ~37% of the frame and the face never resolves, so SUBJECT_REGION crops to
the head and chest -- which is also the framing the reference uses.

Two other candidate treatments were tried and rejected. Keeping the photo's own
background tones as a faint texture makes the tiled wall compete with the cat.
A finer grid -- 8px, 77x48 -- sounds better but reads worse: the glyphs become
comparable in size to the cat's features, so its fur turns to high-frequency
static. ART_FONT stays at the info column's 16px, as in the reference.

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
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:
    sys.exit("needs pillow, numpy and opencv-python:\n"
             "  pip install pillow numpy opencv-python")

# ---------------------------------------------------------------- geometry
W, H = 985, 530
RADIUS = 15
FONT_SIZE = 16            # type size of the info column
ROW_STEP = 20             # and its line height
ADVANCE = 0.6             # monospace advance as a fraction of the font size

ART_X0 = 15
ART_BOX_W = 370           # left column must stay clear of INFO_X
ART_TOP = 30
ART_BOX_H = 480
ART_FONT = 16             # portrait type size -- same as the info column
ART_ROW_STEP = 20

INFO_X = 390
INFO_COLS = 60
VALUE_COL = 25

# ---------------------------------------------------------------- avatar
AVATAR_URL = "https://avatars.githubusercontent.com/u/291477182?s=460&v=4"
GRABCUT_RECT = (30, 20, 400, 400)   # x, y, w, h around the subject
GRABCUT_ITERS = 6
CLAHE_CLIP = 3.0
UNSHARP = (3, 140, 2)               # radius, percent, threshold
SUBJECT_REGION = (0.18, 0.0, 0.74, 0.58)   # x0, y0, x1, y1 of the subject
GATE = 0.45                         # cell coverage below this is background
BG_GLYPH = "."                      # fixed faint glyph for the background
MIN_INK = 0.10                      # floor, so cat cells always beat the field

# Candidate glyphs. Their order here only has to be roughly light-to-heavy:
# selection sorts by MEASURED coverage (see glyph_coverage), which is what
# keeps the portrait from collapsing onto a few glyphs that happen to share a
# density. Space is not a candidate -- the background is drawn explicitly.
RAMP = " .:;~vco%@#"

# A mono face to measure glyph coverage with. The SVG itself still asks the
# browser for Consolas/monospace; this only needs the same metrics, so any
# DejaVu or Liberation mono will do.
MONO_CANDIDATES = (
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",
    "/Library/Fonts/DejaVu Sans Mono.ttf",
)

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


def art_grid() -> tuple[int, int]:
    """Cells the portrait box holds at the configured type size."""
    return int(ART_BOX_W // (ART_FONT * ADVANCE)), int(ART_BOX_H // ART_ROW_STEP)


def glyph_coverage() -> list[tuple[str, float]]:
    """The ramp sorted by how much ink each glyph actually prints.

    Coverage is measured by drawing the glyph at the size it will really be
    rendered at, not assumed from its position in the ramp.
    """
    size = max(1, round(ART_FONT))
    cw, ch = max(2, int(ART_FONT * ADVANCE)), max(2, int(ART_ROW_STEP))

    path = next((p for p in MONO_CANDIDATES if Path(p).exists()), None)
    if path is None:
        # No font to measure with: fall back to the ramp's own order and
        # pretend it is evenly spaced.
        n = max(1, len(RAMP) - 1)
        return sorted(((c, i / n) for i, c in enumerate(RAMP)), key=lambda kv: kv[1])

    font = ImageFont.truetype(path, size)
    measured = []
    for ch in RAMP:
        tile = Image.new("L", (cw, ch), 0)
        ImageDraw.Draw(tile).text((0, 0), ch, fill=255, font=font)
        measured.append((ch, float(np.asarray(tile).mean()) / 255.0))
    return sorted(measured, key=lambda kv: kv[1])


def subject() -> tuple[np.ndarray, np.ndarray]:
    """Fetch the avatar; return the greyscale and mask of the framed subject.

    The mask matters as much as the greyscale. It is what lets the portrait
    hold a solid silhouette even where the cat's own fur is as light as the
    background behind it.
    """
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
    # Sharpen before the grid averages everything away, so the ear edges, the
    # closed eye and the paw stay put instead of smearing.
    grey = np.asarray(
        Image.fromarray(grey).filter(ImageFilter.UnsharpMask(*UNSHARP))
    )

    ys, xs = np.where(m > 0)
    h, w = m.shape
    bx0, bx1 = max(0, xs.min()), min(w, xs.max())
    by0, by1 = max(0, ys.min()), min(h, ys.max())

    # Frame the portrait. Shot whole, the cat's head is only ~37% of the frame,
    # which leaves too few cells to read a face, so SUBJECT_REGION crops to the
    # head and chest instead.
    rx0, ry0, rx1, ry1 = SUBJECT_REGION
    x0 = int(bx0 + (bx1 - bx0) * rx0)
    x1 = int(bx0 + (bx1 - bx0) * rx1)
    y0 = int(by0 + (by1 - by0) * ry0)
    y1 = int(by0 + (by1 - by0) * ry1)
    return grey[y0:y1, x0:x1], m[y0:y1, x0:x1]


def ascii_portrait(dense_is_light: bool) -> list[str]:
    """Render the portrait.

    `dense_is_light` says what a dense glyph looks like on the card the
    portrait is going onto. On the dark card the glyphs ARE the light, so the
    cat's pale fur takes the dense ones and it looks like itself. On the light
    card dense glyphs are dark ink, and drawing the same grid there would turn
    the cat into a photographic negative -- its pale fur would come out dark.
    So the polarity follows the card.
    """
    cols, rows = art_grid()
    grey, mask = subject()

    # A cell is (ART_FONT * ADVANCE) wide by ART_ROW_STEP tall, so the grid is
    # far taller than wide. Crop to that ratio first or it comes out stretched.
    target = (cols * ART_FONT * ADVANCE) / (rows * ART_ROW_STEP)
    h, w = grey.shape
    if w / h > target:
        nw = int(h * target)
        sx = (w - nw) // 2
        box = (slice(None), slice(sx, sx + nw))
    else:
        nh = int(w / target)
        sy = (h - nh) // 2
        box = (slice(sy, sy + nh), slice(None))

    # Area-average both planes down to the character grid.
    g = cv2.resize(grey[box], (cols, rows), interpolation=cv2.INTER_AREA)
    cov = cv2.resize(mask[box], (cols, rows),
                     interpolation=cv2.INTER_AREA).astype(np.float32) / 255.0

    # Map the subject's own tonal range across the ramp rather than a guessed
    # window. This cat's median sits near 91 and its lit fur reaches 238, so a
    # fixed 70..150 window erased three quarters of it.
    fg = grey[mask > 0]
    black, white = (float(np.percentile(fg, p)) for p in (2, 98))

    # Glyphs are chosen by measured ink, and the wanted ink is normalised onto
    # the range glyphs can actually reach: the densest one prints barely a
    # third of its cell, so asking for full ink and taking the nearest glyph
    # squashes every dark cell onto the same glyph.
    #
    # The subject is floored so that no cell of it ever prints fainter than the
    # background field, which is what keeps its outline intact where its fur is
    # as pale as the wall behind it.
    usable = [(c, v) for c, v in glyph_coverage() if c != " "]
    hi = usable[-1][1]

    # On the dark card, dense glyphs read as light, so the cat's pale fur must
    # take them. On the light card dense glyphs read as dark, so the mapping
    # flips. Either way the fur that is pale in the photo comes out pale.
    def ink(lum: float) -> float:
        return lum if dense_is_light else 1.0 - lum

    art = []
    for y in range(rows):
        row = []
        for x in range(cols):
            if cov[y, x] < GATE:
                row.append(BG_GLYPH)     # the mask, not tone, says background
                continue
            lum = max(0.0, min(1.0, (g[y, x] - black) / (white - black)))
            want = MIN_INK + ink(lum) * (hi - MIN_INK)
            row.append(min(usable, key=lambda kv: abs(kv[1] - want))[0])
        art.append("".join(row))
    return art


def build(theme_name: str, art: list[str]) -> str:
    c = THEMES[theme_name]

    # Art rows are centred against the 25-row info column.
    pad = max(0, (len(INFO) - len(art)) // 2)
    art_svg = []
    for i, row in enumerate(art):
        y = ART_TOP + (i + pad) * ART_ROW_STEP
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
#art   {{font-size: {ART_FONT}px;}}
</style>
<rect width="{W}" height="{H}" fill="{c['bg']}" rx="{RADIUS}"/>
<text id="art" x="{ART_X0}" y="{ART_TOP}" fill="{c['fg']}">
{chr(10).join(art_svg)}
</text>
<text x="{INFO_X}" y="{ART_TOP}" fill="{c['fg']}">
{chr(10).join(info_svg)}
</text>
</svg>
"""


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    cols, rows = art_grid()
    # Dense glyphs are light on the dark card and dark on the light card, so
    # each theme gets its portrait drawn with the matching polarity.
    arts = {"dark": ascii_portrait(dense_is_light=True),
            "light": ascii_portrait(dense_is_light=False)}
    for name, art in arts.items():
        out = root / f"banner-{name}.svg"
        out.write_text(build(name, art), encoding="utf-8")
        print(f"wrote {out.relative_to(root)}  ({out.stat().st_size / 1024:.1f} KB)")
    print(f"portrait: {cols}x{rows} cells at {ART_FONT}px / {ART_ROW_STEP}px rows")
    print()
    print("\n".join(arts["dark"]))


if __name__ == "__main__":
    main()
