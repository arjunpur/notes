#!/usr/bin/env python3
"""Render raster teaching diagrams for the clustered-spiking course.

The figures are deliberately PNG-first and avoid external vector source files
while keeping mathematical labels exact enough for lecture notes.
"""

from __future__ import annotations

import math
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"

W, H = 2400, 1500

INK = "#1f2933"
MUTED = "#5b6773"
GRID = "#d7dee6"
PANEL = "#f6f8fb"
BLUE = "#2866b1"
BLUE2 = "#79a8d8"
GREEN = "#2f7d5b"
GREEN2 = "#9bd3b5"
RED = "#b84a4a"
RED2 = "#e3a0a0"
GOLD = "#b07a1f"
GOLD2 = "#f2d58b"
PURPLE = "#6654a3"
PURPLE2 = "#beb5eb"
TEAL = "#2a7886"
TEAL2 = "#9bd6dd"
ORANGE = "#c56b2c"
ORANGE2 = "#f1b583"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            pass
    return ImageFont.load_default()


F_TITLE = font(62, True)
F_SUB = font(36)
F_LABEL = font(34, True)
F_TEXT = font(30)
F_SMALL = font(24)
F_TINY = font(20)


def canvas(title: str, subtitle: str | None = None) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, H], fill="#ffffff")
    d.text((90, 58), title, font=F_TITLE, fill=INK)
    if subtitle:
        d.text((92, 132), subtitle, font=F_SUB, fill=MUTED)
    return im, d


def save(im: Image.Image, name: str) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    im.save(FIG / f"{name}.png", optimize=True)


def text_center(d: ImageDraw.ImageDraw, box, text: str, fnt=F_TEXT, fill=INK, spacing=8) -> None:
    x0, y0, x1, y1 = box
    lines = text.split("\n")
    heights = []
    widths = []
    for line in lines:
        b = d.textbbox((0, 0), line, font=fnt)
        widths.append(b[2] - b[0])
        heights.append(b[3] - b[1])
    total_h = sum(heights) + spacing * (len(lines) - 1)
    y = y0 + (y1 - y0 - total_h) / 2
    for line, ww, hh in zip(lines, widths, heights):
        d.text((x0 + (x1 - x0 - ww) / 2, y), line, font=fnt, fill=fill)
        y += hh + spacing


def rounded(d: ImageDraw.ImageDraw, box, fill=PANEL, outline=GRID, width=3, r=28) -> None:
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def arrow(d: ImageDraw.ImageDraw, p0, p1, fill=INK, width=6, head=22) -> None:
    x0, y0 = p0
    x1, y1 = p1
    d.line([p0, p1], fill=fill, width=width)
    ang = math.atan2(y1 - y0, x1 - x0)
    a1 = ang + math.pi * 0.82
    a2 = ang - math.pi * 0.82
    pts = [
        (x1, y1),
        (x1 + head * math.cos(a1), y1 + head * math.sin(a1)),
        (x1 + head * math.cos(a2), y1 + head * math.sin(a2)),
    ]
    d.polygon(pts, fill=fill)


def axes(d, box, xlabel="", ylabel="", x_ticks=None, y_ticks=None):
    x0, y0, x1, y1 = box
    d.line([(x0, y1), (x1, y1)], fill=INK, width=4)
    d.line([(x0, y1), (x0, y0)], fill=INK, width=4)
    for i in range(6):
        x = x0 + i * (x1 - x0) / 5
        d.line([(x, y0), (x, y1)], fill=GRID, width=1)
    for i in range(5):
        y = y0 + i * (y1 - y0) / 4
        d.line([(x0, y), (x1, y)], fill=GRID, width=1)
    if xlabel:
        text_center(d, (x0, y1 + 28, x1, y1 + 82), xlabel, F_SMALL, MUTED)
    if ylabel:
        d.text((x0 - 96, y0 + 10), ylabel, font=F_SMALL, fill=MUTED)


def plot_line(d, box, xs, ys, color=BLUE, width=8):
    x0, y0, x1, y1 = box
    pts = [(x0 + x * (x1 - x0), y1 - y * (y1 - y0)) for x, y in zip(xs, ys)]
    d.line(pts, fill=color, width=width, joint="curve")
    return pts


def label_box(d, box, title, body, color=BLUE):
    rounded(d, box, fill="#ffffff", outline=color, width=4, r=24)
    x0, y0, x1, y1 = box
    inner_w = max(20, x1 - x0 - 56)
    title_font = F_LABEL
    title_lines = wrap_for_width(d, title, title_font, inner_w)
    y = y0 + 22
    for line in title_lines:
        d.text((x0 + 28, y), line, font=title_font, fill=color)
        y += line_height(d, line, title_font) + 5
    body_font = F_SMALL
    body_lines = []
    for raw in body.split("\n"):
        body_lines.extend(wrap_for_width(d, raw, body_font, inner_w))
    y += 10
    max_y = y1 - 22
    for line in body_lines:
        if y + line_height(d, line, body_font) > max_y:
            break
        d.text((x0 + 28, y), line, font=body_font, fill=INK)
        y += line_height(d, line, body_font) + 8


def line_height(d: ImageDraw.ImageDraw, text: str, fnt) -> int:
    b = d.textbbox((0, 0), text or "Ag", font=fnt)
    return b[3] - b[1]


def wrap_for_width(d: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    if not text:
        return [""]
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if d.textbbox((0, 0), trial, font=fnt)[2] <= width:
            current = trial
            continue
        if current:
            lines.append(current)
        if d.textbbox((0, 0), word, font=fnt)[2] <= width:
            current = word
        else:
            chunks = textwrap.wrap(word, width=max(4, int(width / max(8, fnt.size * 0.55))))
            lines.extend(chunks[:-1])
            current = chunks[-1] if chunks else ""
    if current:
        lines.append(current)
    return lines


def fig01_jacobian():
    im, d = canvas("Jacobian spectrum controls local stability", "Linearize near x*:  dx/dt = J(x*) (x - x*)")
    panels = [(90, 225, 720, 1190), (885, 225, 1465, 1190), (1640, 225, 2220, 1190)]
    titles = ["Eigenvalues", "Stable fixed point", "Unstable direction"]
    for box, title in zip(panels, titles):
        rounded(d, box)
        d.text((box[0] + 34, box[1] + 28), title, font=F_LABEL, fill=INK)
    # complex plane
    x0, y0, x1, y1 = (160, 405, 650, 980)
    axes(d, (x0, y0, x1, y1), "Re(lambda)", "Im")
    d.line([(x0 + 245, y0), (x0 + 245, y1)], fill=RED, width=5)
    d.text((x0 + 196, y1 + 94), "0", font=F_SMALL, fill=RED)
    for px, py, col in [(135, 150, GREEN), (165, 360, GREEN), (330, 260, RED), (395, 130, RED)]:
        d.ellipse([x0 + px - 14, y0 + py - 14, x0 + px + 14, y0 + py + 14], fill=col)
    d.text((185, 1040), "Left half-plane:\nperturbations decay", font=F_SMALL, fill=GREEN)
    d.text((435, 1040), "Right half-plane:\none mode grows", font=F_SMALL, fill=RED)
    # stable spiral
    cx, cy = 1175, 735
    for r in [270, 210, 155, 105, 65]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline="#c8d8ea", width=2)
    pts = []
    for k in range(300):
        t = k / 18
        r = 330 * math.exp(-0.011 * k)
        pts.append((cx + r * math.cos(t), cy + 0.65 * r * math.sin(t)))
    d.line(pts, fill=BLUE, width=8, joint="curve")
    d.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill=GREEN)
    d.text((990, 1040), "all Re(lambda) < 0\nreturn to x*", font=F_SMALL, fill=GREEN)
    # unstable
    cx, cy = 1930, 735
    d.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill=RED)
    for ang in [-0.8, -0.35, 0.2, 0.7]:
        for sign in [-1, 1]:
            p0 = (cx + sign * 50 * math.cos(ang), cy + sign * 35 * math.sin(ang))
            p1 = (cx + sign * 245 * math.cos(ang), cy + sign * 170 * math.sin(ang))
            arrow(d, p0, p1, fill=RED, width=5, head=20)
    for yy in [555, 650, 820, 910]:
        arrow(d, (1700, yy), (1865, yy + (735 - yy) * 0.35), fill=BLUE2, width=4, head=16)
        arrow(d, (2160, yy), (1995, yy + (735 - yy) * 0.35), fill=BLUE2, width=4, head=16)
    d.text((1775, 1040), "positive Lyapunov-like\nlocal growth", font=F_SMALL, fill=RED)
    label_box(d, (410, 1240, 1990, 1410), "Use later", "A cluster-level perturbation that decays suggests an attractor basin; exponential growth suggests chaotic mesoscale flow.", PURPLE)
    save(im, "ch01-jacobian-eigenvalues")


def fig01_landscape():
    im, d = canvas("Multistable attractor landscape", "Basins, basin boundaries, small perturbations, and finite-size switching")
    rounded(d, (95, 220, 2305, 1225))
    # colored basins
    d.ellipse([160, 375, 1040, 1130], fill="#e8f1fb", outline=BLUE2, width=4)
    d.ellipse([790, 320, 1635, 1135], fill="#ebf6ee", outline=GREEN2, width=4)
    d.ellipse([1410, 375, 2225, 1130], fill="#fff2de", outline=GOLD2, width=4)
    d.line([(780, 350), (875, 520), (850, 690), (935, 850), (895, 1105)], fill="#7e8792", width=7)
    d.line([(1490, 350), (1430, 530), (1510, 710), (1445, 900), (1495, 1105)], fill="#7e8792", width=7)
    centers = [(575, 765, BLUE, "state A\nclusters {1,4}"), (1215, 760, GREEN, "state B\nclusters {2,3,5}"), (1810, 765, GOLD, "state C\ncluster {6}")]
    for cx, cy, col, txt in centers:
        d.ellipse([cx - 48, cy - 48, cx + 48, cy + 48], fill=col)
        text_center(d, (cx - 210, cy + 76, cx + 210, cy + 170), txt, F_SMALL, INK)
        for ang in [0, 0.75, 1.6, 2.6, 3.7, 4.8]:
            p0 = (cx + 260 * math.cos(ang), cy + 180 * math.sin(ang))
            p1 = (cx + 80 * math.cos(ang), cy + 55 * math.sin(ang))
            arrow(d, p0, p1, fill=col, width=4, head=17)
    arrow(d, (540, 590), (645, 565), fill=BLUE, width=6)
    d.text((405, 520), "small perturbation:\nreturns", font=F_SMALL, fill=BLUE)
    arrow(d, (1290, 610), (1510, 570), fill=RED, width=7)
    d.text((1305, 495), "large perturbation:\ncrosses boundary", font=F_SMALL, fill=RED)
    for x in [730, 810, 875, 1400, 1475]:
        d.arc([x - 48, 285, x + 48, 381], 30, 330, fill=RED2, width=4)
    label_box(d, (365, 1265, 2025, 1422), "Finite N", "Population noise repeatedly nudges the coarse state. If the basin barrier is shallow, these nudges can produce metastable switching.", RED)
    save(im, "ch01-attractor-landscape")


def fig02_spike_filtering():
    im, d = canvas("From spikes to mesoscopic activity", "Point events -> synaptic filter -> neuron trace -> cluster average")
    boxes = [(100, 260, 650, 1160), (710, 260, 1210, 1160), (1270, 260, 1770, 1160), (1830, 260, 2300, 1160)]
    for box in boxes:
        rounded(d, box)
    labels = ["1. spike train s_i(t)", "2. filter epsilon(t)", "3. filtered trace r_i(t)", "4. cluster mean R_a(t)"]
    for box, label in zip(boxes, labels):
        d.text((box[0] + 32, box[1] + 28), label, font=F_LABEL, fill=INK)
    # spike train
    x0, y0, x1, y1 = 155, 475, 595, 900
    axes(d, (x0, y0, x1, y1), "time", "")
    spikes = [0.1, 0.18, 0.38, 0.58, 0.64, 0.83]
    for s in spikes:
        x = x0 + s * (x1 - x0)
        d.line([(x, y1), (x, y0 + 45)], fill=INK, width=8)
    d.text((190, 975), "sum of delta events", font=F_SMALL, fill=MUTED)
    # filter
    x0, y0, x1, y1 = 775, 500, 1145, 900
    axes(d, (x0, y0, x1, y1), "lag", "")
    xs = [i / 100 for i in range(101)]
    ys = [math.exp(-5 * x) for x in xs]
    plot_line(d, (x0, y0, x1, y1), xs, ys, GREEN, 8)
    d.text((810, 975), "decay time tau_s", font=F_SMALL, fill=MUTED)
    # filtered trace
    x0, y0, x1, y1 = 1335, 500, 1705, 900
    axes(d, (x0, y0, x1, y1), "time", "")
    xs = [i / 300 for i in range(301)]
    ys = []
    for t in xs:
        y = sum(math.exp(-(t - s) * 9) for s in spikes if t >= s)
        ys.append(min(1.0, y / 1.75))
    plot_line(d, (x0, y0, x1, y1), xs, ys, BLUE, 8)
    d.text((1355, 975), "continuous current trace", font=F_SMALL, fill=MUTED)
    # cluster mean
    x0, y0, x1, y1 = 1895, 500, 2245, 900
    axes(d, (x0, y0, x1, y1), "time", "")
    xs = [i / 300 for i in range(301)]
    ys = [0.45 + 0.16 * math.sin(2 * math.pi * (2.1 * x + 0.1)) + 0.08 * math.sin(2 * math.pi * 6.2 * x) for x in xs]
    ys = [(y - 0.18) / 0.62 for y in ys]
    plot_line(d, (x0, y0, x1, y1), xs, ys, PURPLE, 8)
    d.text((1905, 975), "mesoscopic state variable", font=F_SMALL, fill=MUTED)
    for p0, p1 in [((650, 710), (710, 710)), ((1210, 710), (1270, 710)), ((1770, 710), (1830, 710))]:
        arrow(d, p0, p1, fill=ORANGE, width=7, head=24)
    text_center(d, (460, 1215, 1960, 1405), "The state used for cluster-level dynamics is not a raw spike. It is a filtered and averaged activity trace.", F_TEXT, INK)
    save(im, "ch02-spike-filtering")


def fig02_noise_scaling():
    im, d = canvas("Finite-size noise shrinks as 1/sqrt(N_E)", "The xi coordinate measures sampling noise: xi = 1/sqrt(N_E)")
    box = (250, 255, 1570, 1160)
    rounded(d, (90, 220, 2310, 1245))
    axes(d, box, "cluster size N_E", "fluctuation amplitude")
    Ns = [50, 100, 200, 400, 800, 1600, 3200]
    vals = [1 / math.sqrt(n / 50) for n in Ns]
    maxv = max(vals)
    xs = [(math.log(n) - math.log(50)) / (math.log(3200) - math.log(50)) for n in Ns]
    ys = [v / maxv for v in vals]
    pts = plot_line(d, box, xs, ys, BLUE, 8)
    for (x, y), n in zip(pts, Ns):
        d.ellipse([x - 14, y - 14, x + 14, y + 14], fill=BLUE)
        d.text((x - 32, box[3] + 96), str(n), font=F_TINY, fill=MUTED)
    d.text((790, 425), "slope: -1/2", font=F_LABEL, fill=BLUE)
    label_box(d, (1680, 300, 2220, 575), "Finite-size switching", "As N_E grows, noise-driven basin escapes become rare.", RED)
    label_box(d, (1680, 645, 2220, 935), "Chaos test", "If switching survives as xi -> 0, finite-size noise is not the full explanation.", PURPLE)
    arrow(d, (1890, 1035), (2050, 1035), fill=GREEN, width=8)
    d.text((1665, 1075), "move right: larger clusters, smaller xi", font=F_SMALL, fill=GREEN)
    save(im, "ch02-noise-scaling")


def fig03_lif():
    im, d = canvas("Leaky integrate-and-fire voltage trace", "A continuous membrane voltage generates discrete spike events")
    rounded(d, (90, 220, 2310, 1245))
    box = (210, 350, 2220, 1040)
    axes(d, box, "time", "voltage V(t)")
    x0, y0, x1, y1 = box
    def yv(v): return y1 - v * (y1 - y0)
    thr, reset, rest = 0.82, 0.23, 0.12
    d.line([(x0, yv(thr)), (x1, yv(thr))], fill=RED, width=5)
    d.line([(x0, yv(reset)), (x1, yv(reset))], fill=BLUE2, width=4)
    d.line([(x0, yv(rest)), (x1, yv(rest))], fill=GRID, width=3)
    d.text((x0 + 20, yv(thr) - 48), "threshold V_theta", font=F_SMALL, fill=RED)
    d.text((x0 + 20, yv(reset) + 12), "reset V_r", font=F_SMALL, fill=BLUE)
    pts = []
    t = 0.0
    starts = [0.0, 0.29, 0.56, 0.79]
    for start in starts:
        local = [start + i * 0.002 for i in range(110)]
        for tt in local:
            phase = (tt - start) / 0.22
            v = reset + (thr - reset) * (1 - math.exp(-3.2 * phase)) + 0.025 * math.sin(44 * tt)
            if v >= thr and tt < start + 0.22:
                pts.append((x0 + tt * (x1 - x0), yv(thr)))
                px = x0 + tt * (x1 - x0)
                d.line([(px, yv(thr)), (px, yv(1.0))], fill=RED, width=8)
                d.line([(px, yv(thr)), (px + 18, yv(reset))], fill=BLUE, width=5)
                d.text((px - 35, yv(1.0) - 48), "spike", font=F_TINY, fill=RED)
                break
            pts.append((x0 + tt * (x1 - x0), yv(v)))
        if start != starts[-1]:
            pts.append((x0 + (start + 0.24) * (x1 - x0), yv(reset)))
    d.line(pts, fill=INK, width=8, joint="curve")
    label_box(d, (330, 1090, 1010, 1400), "Key mechanism", "Leak pulls V toward rest; input current raises V; threshold emits an event; reset erases recent voltage.", GREEN)
    label_box(d, (1220, 1090, 2070, 1400), "For mean field", "Many stochastic LIF neurons give a smooth population firing rate, but individual spikes remain event times.", PURPLE)
    save(im, "ch03-lif-threshold-reset")


def fig03_transfer():
    im, d = canvas("Input current to firing-rate transfer", "Noise and adaptation change the gain curve")
    rounded(d, (90, 220, 2310, 1245))
    box = (250, 330, 1570, 1080)
    axes(d, box, "mean input current", "expected firing rate")
    xs = [i / 300 for i in range(301)]
    hard = [0 if x < 0.43 else min(1, 2.1 * (x - 0.43)) for x in xs]
    noisy = [1 / (1 + math.exp(-12 * (x - 0.43))) * 0.93 for x in xs]
    adapt = [0.82 / (1 + math.exp(-10 * (x - 0.48))) * (1 - 0.23 * x) for x in xs]
    plot_line(d, box, xs, hard, RED, 7)
    plot_line(d, box, xs, noisy, BLUE, 8)
    plot_line(d, box, xs, adapt, GREEN, 8)
    d.text((1210, 475), "noisy LIF", font=F_SMALL, fill=BLUE)
    d.text((1130, 640), "adapted/GIF", font=F_SMALL, fill=GREEN)
    d.text((790, 900), "hard threshold", font=F_SMALL, fill=RED)
    label_box(d, (1690, 320, 2240, 555), "Population map", "Firing rate = average over neurons, noise, and trials.", BLUE)
    label_box(d, (1690, 635, 2240, 875), "Why nonlinear?", "The recurrent network feeds this curve back into itself.", PURPLE)
    label_box(d, (1690, 955, 2240, 1190), "Next step", "Mean field replaces many inputs by mean and variance.", GREEN)
    save(im, "ch03-transfer-function")


def fig04_balance():
    im, d = canvas("Balanced excitation and inhibition", "Large opposing currents leave a small residual drive")
    rounded(d, (90, 220, 2310, 1245))
    for i, (box, title) in enumerate([((210, 330, 2180, 650), "large components"), ((210, 760, 2180, 1095), "small residual near threshold")]):
        axes(d, box, "time", "" if i else "current")
        d.text((box[0] + 20, box[1] - 62), title, font=F_LABEL, fill=INK)
    xs = [i / 500 for i in range(501)]
    E = [0.65 + 0.12 * math.sin(2 * math.pi * 2.2 * x) + 0.06 * math.sin(2 * math.pi * 8.1 * x) for x in xs]
    I = [0.35 - 0.12 * math.sin(2 * math.pi * 2.2 * x + 0.1) - 0.055 * math.sin(2 * math.pi * 8.1 * x + 0.4) for x in xs]
    plot_line(d, (210, 330, 2180, 650), xs, E, GREEN, 8)
    plot_line(d, (210, 330, 2180, 650), xs, I, RED, 8)
    residual = [0.5 + 0.22 * ((e + i) - 1.0) for e, i in zip(E, I)]
    plot_line(d, (210, 760, 2180, 1095), xs, residual, BLUE, 8)
    d.line([(210, 928), (2180, 928)], fill=GOLD, width=4)
    d.text((1790, 390), "E current", font=F_SMALL, fill=GREEN)
    d.text((1780, 565), "I current (opposes E)", font=F_SMALL, fill=RED)
    d.text((1600, 800), "E + I + external", font=F_SMALL, fill=BLUE)
    label_box(d, (330, 1135, 2080, 1415), "Balanced-state intuition", "Strong excitation and inhibition can cancel in the mean. Irregular spiking is then controlled by the residual fluctuations and correlations, not by the large raw currents alone.", PURPLE)
    save(im, "ch04-balance-cancellation")


def fig04_sparse():
    im, d = canvas("Sparse fixed-in-degree connectivity", "Exactly K selected sources control mean input; identities create quenched disorder")
    rounded(d, (90, 220, 2310, 1245))
    post = (1900, 735)
    d.ellipse([post[0] - 120, post[1] - 120, post[0] + 120, post[1] + 120], fill="#f9fafb", outline=INK, width=6)
    text_center(d, (post[0] - 115, post[1] - 60, post[0] + 115, post[1] + 60), "target\ncluster", F_LABEL, INK)
    sources = []
    for i in range(14):
        y = 360 + i * 65
        x = 345 + (i % 2) * 120
        typ = "E" if i < 8 else "I"
        col = GREEN if typ == "E" else RED
        sources.append((x, y, typ, col, i in {0, 2, 4, 6, 8, 10, 12}))
    for x, y, typ, col, selected in sources:
        d.ellipse([x - 42, y - 42, x + 42, y + 42], fill=col if selected else "#ffffff", outline=col, width=5)
        text_center(d, (x - 35, y - 28, x + 35, y + 28), typ, F_LABEL, "#ffffff" if selected else col)
        if selected:
            arrow(d, (x + 48, y), (post[0] - 125, post[1] + 0.38 * (y - post[1])), fill=col, width=5, head=18)
        else:
            d.line([(x + 48, y), (post[0] - 125, post[1] + 0.38 * (y - post[1]))], fill="#cfd6dd", width=2)
    label_box(d, (750, 330, 1420, 555), "Fixed in-degree", "Each postsynaptic cluster receives K inputs, not a random count.", BLUE)
    label_box(d, (750, 630, 1420, 855), "Split by type", "K_E = fK excitatory\nK_I = (1-f)K inhibitory", GREEN)
    label_box(d, (750, 930, 1420, 1155), "Quenched identities", "The selected source IDs stay fixed across time.", PURPLE)
    save(im, "ch04-sparse-fixed-indegree")


def fig05_matrix():
    im, d = canvas("Clustered EE connectivity matrix", "Diagonal blocks potentiate assemblies; off-diagonal blocks depress competition")
    rounded(d, (90, 220, 2310, 1245))
    x0, y0, size = 330, 320, 780
    n = 5
    cell = size / n
    for i in range(n):
        for j in range(n):
            if i == j:
                fill = "#2768b7"
            else:
                shade = 210 + ((i + j) % 2) * 20
                fill = (shade, 225, 240)
            d.rectangle([x0 + j * cell, y0 + i * cell, x0 + (j + 1) * cell, y0 + (i + 1) * cell], fill=fill, outline="white", width=5)
            if i == j:
                text_center(d, (x0 + j * cell, y0 + i * cell, x0 + (j + 1) * cell, y0 + (i + 1) * cell), "Jhat\nEE", F_SMALL, "white")
    d.text((x0, y0 - 55), "presynaptic cluster b", font=F_SMALL, fill=MUTED)
    d.text((x0 - 215, y0 + 330), "postsynaptic\ncluster a", font=F_SMALL, fill=MUTED)
    d.text((x0 + 365, y0 + size + 30), "off diagonal: Jcheck_ab^EE", font=F_SMALL, fill=BLUE)
    # network sketch
    centers = [(1600 + 280 * math.cos(2 * math.pi * k / 5), 700 + 240 * math.sin(2 * math.pi * k / 5)) for k in range(5)]
    for idx, (cx, cy) in enumerate(centers, 1):
        d.ellipse([cx - 74, cy - 74, cx + 74, cy + 74], fill="#eaf2fb", outline=BLUE, width=5)
        text_center(d, (cx - 70, cy - 38, cx + 70, cy + 38), f"C{idx}", F_LABEL, BLUE)
    for i, a in enumerate(centers):
        for j, b in enumerate(centers):
            if i < j:
                d.line([a, b], fill="#cfd6dd", width=3)
    for cx, cy in centers:
        d.arc([cx - 105, cy - 105, cx + 105, cy + 105], 210, 510, fill=GREEN, width=8)
    label_box(d, (1285, 1045, 2180, 1210), "Coarse variables", "Block structure lets active clusters behave like dynamical units while neurons still spike.", GREEN)
    save(im, "ch05-clustered-connectivity-matrix")


def fig05_landscape():
    im, d = canvas("Metastable active-cluster patterns", "Noise-driven hops among coarse states in an E-clustered attractor network")
    rounded(d, (90, 220, 2310, 1245))
    basins = [(520, 690, BLUE, "{1,4}"), (1120, 610, GREEN, "{2,3,5}"), (1720, 720, GOLD, "{6}"), (1460, 1010, PURPLE, "{1,2}")]
    for cx, cy, col, lab in basins:
        d.ellipse([cx - 260, cy - 165, cx + 260, cy + 165], fill="#ffffff", outline=col, width=7)
        d.ellipse([cx - 36, cy - 36, cx + 36, cy + 36], fill=col)
        text_center(d, (cx - 180, cy + 55, cx + 180, cy + 135), lab, F_LABEL, col)
        for ang in [0.5, 2.1, 3.6, 5.2]:
            arrow(d, (cx + 210 * math.cos(ang), cy + 125 * math.sin(ang)), (cx + 60 * math.cos(ang), cy + 35 * math.sin(ang)), fill=col, width=4, head=17)
    for p0, p1 in [((760, 620), (895, 585)), ((1375, 650), (1510, 675)), ((1590, 895), (1515, 950))]:
        arrow(d, p0, p1, fill=RED, width=8, head=26)
    d.text((835, 505), "finite-size\nkick", font=F_SMALL, fill=RED)
    d.text((1415, 560), "cross saddle", font=F_SMALL, fill=RED)
    label_box(d, (380, 1255, 2020, 1420), "Thermodynamic check", "If these hops disappear as cluster size grows, the switching was finite-size metastability rather than deterministic chaos.", PURPLE)
    save(im, "ch05-active-inactive-landscape")


def fig06_phase():
    im, d = canvas("SCS random rate transition", "Leak dominates below g_c; recurrent amplification creates stretching and folding above g_c")
    panels = [(150, 300, 1100, 1165), (1300, 300, 2250, 1165)]
    titles = ["g < g_c: stable fixed point", "g > g_c: bounded chaos"]
    for box, title in zip(panels, titles):
        rounded(d, box)
        d.text((box[0] + 40, box[1] + 35), title, font=F_LABEL, fill=INK)
        axes(d, (box[0] + 110, box[1] + 155, box[2] - 90, box[3] - 115), "rate unit 1", "rate unit 2")
    # contraction vector field
    box = (260, 455, 1010, 1050)
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    for ix in range(6):
        for iy in range(5):
            x = box[0] + 70 + ix * 120
            y = box[1] + 70 + iy * 105
            arrow(d, (x, y), (x + 0.18 * (cx - x), y + 0.18 * (cy - y)), fill="#b9c4d0", width=3, head=12)
    for phase, col in [(0, BLUE), (1.2, GREEN), (2.4, PURPLE)]:
        pts = []
        for k in range(180):
            t = k / 18 + phase
            r = 330 * math.exp(-0.017 * k)
            pts.append((cx + r * math.cos(t), cy + 0.7 * r * math.sin(t)))
        d.line(pts, fill=col, width=6)
    d.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill=GREEN)
    # chaotic folded path
    box = (1410, 455, 2160, 1050)
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    for ix in range(6):
        for iy in range(5):
            x = box[0] + 70 + ix * 120
            y = box[1] + 70 + iy * 105
            ang = math.sin(ix * 1.7 + iy) * 1.7
            arrow(d, (x, y), (x + 45 * math.cos(ang), y + 32 * math.sin(ang)), fill="#c6ccd3", width=3, head=12)
    pts = []
    for k in range(520):
        t = k / 25
        x = cx + 290 * math.sin(1.7 * t) + 70 * math.sin(5.1 * t)
        y = cy + 215 * math.sin(2.3 * t + 0.9)
        pts.append((x, y))
    d.line(pts, fill=RED, width=6, joint="curve")
    label_box(d, (350, 1230, 2060, 1420), "Mathematical point", "The high-dimensional SCS transition is a competition between stabilizing leak and random recurrent gain, not a finite-size noise effect.", ORANGE)
    save(im, "ch06-random-rate-phase-portrait")


def fig06_autocorr():
    im, d = canvas("Autocorrelation through the SCS transition", "Smooth chaotic rate correlations broaden near and above critical gain")
    rounded(d, (90, 220, 2310, 1245))
    box = (265, 330, 1660, 1100)
    axes(d, box, "lag tau", "C(tau)/C(0)")
    xs = [i / 500 for i in range(501)]
    sub = [math.exp(-10 * x) for x in xs]
    crit = [math.exp(-3.1 * x) for x in xs]
    chaos = [math.exp(-1.6 * x * x) * (0.96 - 0.06 * math.sin(7 * x)) for x in xs]
    plot_line(d, box, xs, sub, BLUE, 7)
    plot_line(d, box, xs, crit, GOLD, 8)
    plot_line(d, box, xs, chaos, RED, 8)
    d.text((565, 610), "subcritical", font=F_SMALL, fill=BLUE)
    d.text((840, 745), "near critical", font=F_SMALL, fill=GOLD)
    d.text((1170, 505), "chaotic smooth shoulder", font=F_SMALL, fill=RED)
    label_box(d, (1750, 340, 2240, 585), "Finite-size noise", "adds a sharp zero-lag kink", BLUE)
    label_box(d, (1750, 675, 2240, 930), "Chaotic rate", "has zero slope at tau = 0", RED)
    d.arc([1780, 1000, 2210, 1195], 180, 350, fill=PURPLE, width=8)
    d.text((1805, 1205), "diagnostic: shape near zero lag", font=F_SMALL, fill=PURPLE)
    save(im, "ch06-scs-autocorrelation-transition")


def fig07_quenched():
    im, d = canvas("Quenched versus annealed disorder", "Fixed recurrent geometry is different from time-redrawn noise")
    panels = [(120, 275, 1130, 1210), (1270, 275, 2280, 1210)]
    for box, title in zip(panels, ["Quenched: sampled once", "Annealed: redrawn over time"]):
        rounded(d, box)
        d.text((box[0] + 38, box[1] + 36), title, font=F_LABEL, fill=INK)
    # matrices
    for origin, changing in [((210, 420), False), ((1360, 420), True)]:
        x0, y0 = origin
        cell = 58
        for i in range(5):
            for j in range(5):
                val = (i * 3 + j * 5) % 4
                col = [BLUE2, GREEN2, GOLD2, RED2][val] if not changing else [BLUE2, GREEN2, GOLD2, RED2][(val + i) % 4]
                d.rectangle([x0 + j * cell, y0 + i * cell, x0 + (j + 1) * cell, y0 + (i + 1) * cell], fill=col, outline="white", width=3)
        d.text((x0, y0 + 320), "J_ab fixed" if not changing else "J_ab(t) changes", font=F_SMALL, fill=MUTED)
    # trajectories
    for base, color in [((620, 570), BLUE), ((1770, 570), RED)]:
        cx, cy = base
        for q in range(4):
            pts = []
            for k in range(160):
                t = k / 30
                pts.append((cx + 220 * math.sin(t + q * 0.2) * math.exp(-0.002 * k), cy + 140 * math.sin(1.7 * t + q) * math.exp(-0.002 * k)))
            d.line(pts, fill=color if q == 0 else "#9aa6b2", width=5 if q == 0 else 3)
    label_box(d, (215, 920, 1045, 1145), "Deterministic sensitivity", "Same frozen matrix shapes every trajectory; perturbations can diverge in that fixed vector field.", PURPLE)
    label_box(d, (1365, 920, 2195, 1145), "Input-like variability", "Redrawing weights mimics variance but erases the fixed geometry needed for Lyapunov growth.", ORANGE)
    save(im, "ch07-quenched-vs-annealed-disorder")


def fig07_dmft():
    im, d = canvas("Dynamic mean-field self-consistency", "Replace many random inputs by one representative stochastic process")
    rounded(d, (90, 220, 2310, 1245))
    nodes = {
        "net": (230, 560, 730, 825, "High-dimensional\nrandom network", BLUE),
        "unit": (930, 360, 1510, 630, "Representative unit\nmu + eta0 + zeta(t)", GREEN),
        "stats": (1660, 560, 2160, 825, "Output statistics\nm, C_r(tau)", GOLD),
        "closure": (930, 940, 1510, 1190, "Input closure\nVar eta0 = g^2 m^2\nCov zeta = g^2 C_r", PURPLE),
    }
    for x0, y0, x1, y1, txt, col in nodes.values():
        rounded(d, (x0, y0, x1, y1), fill="#ffffff", outline=col, width=6, r=34)
        text_center(d, (x0 + 20, y0 + 20, x1 - 20, y1 - 20), txt, F_TEXT, INK)
    arrow(d, (730, 660), (930, 500), fill=INK, width=7)
    arrow(d, (1510, 500), (1660, 660), fill=INK, width=7)
    arrow(d, (1910, 825), (1510, 1065), fill=INK, width=7)
    arrow(d, (930, 1065), (480, 825), fill=INK, width=7)
    d.text((760, 420), "average over random couplings", font=F_SMALL, fill=MUTED)
    d.text((1575, 430), "simulate one process", font=F_SMALL, fill=MUTED)
    d.text((1600, 1005), "self-consistency", font=F_SMALL, fill=MUTED)
    d.text((520, 1010), "feed back assumptions", font=F_SMALL, fill=MUTED)
    save(im, "ch07-dmft-self-consistency-loop")


def fig08_paired():
    im, d = canvas("Paired excitatory/inhibitory clusters", "A cluster pair is a mesoscale E-I unit with structured internal couplings")
    rounded(d, (90, 220, 2310, 1245))
    centers = [(670, 720, "pair a"), (1730, 720, "pair b")]
    for cx, cy, lab in centers:
        rounded(d, (cx - 310, cy - 280, cx + 310, cy + 280), fill="#ffffff", outline=GRID, width=5, r=34)
        d.text((cx - 90, cy - 250), lab, font=F_LABEL, fill=INK)
        d.ellipse([cx - 185, cy - 80, cx - 55, cy + 50], fill=GREEN, outline=INK, width=4)
        d.ellipse([cx + 55, cy - 80, cx + 185, cy + 50], fill=RED, outline=INK, width=4)
        text_center(d, (cx - 185, cy - 80, cx - 55, cy + 50), "E", F_LABEL, "white")
        text_center(d, (cx + 55, cy - 80, cx + 185, cy + 50), "I", F_LABEL, "white")
        arrow(d, (cx - 55, cy - 25), (cx + 55, cy - 25), fill=GREEN, width=7)
        arrow(d, (cx + 55, cy + 25), (cx - 55, cy + 25), fill=RED, width=7)
        d.text((cx - 212, cy + 90), "J_E+ boosts EE", font=F_SMALL, fill=GREEN)
        d.text((cx - 212, cy + 130), "J_I+ boosts EI/IE/II", font=F_SMALL, fill=RED)
    for yy, col, txt in [(560, GREEN, "depressed EE between pairs"), (830, RED, "depressed inhibitory cross-structure")]:
        d.line([(980, yy), (1420, yy)], fill=col, width=5)
        d.line([(980, yy + 34), (1420, yy + 34)], fill=col, width=2)
        d.text((1010, yy - 45), txt, font=F_SMALL, fill=col)
    label_box(d, (520, 1045, 1880, 1225), "Mesoscale variable", "Pair activity is the chaotic degree of freedom. Strong local E-I recurrence makes each pair an effective rate unit.", PURPLE)
    save(im, "ch08-paired-ei-clusters")


def fig08_amplification():
    im, d = canvas("Inhibitory structure amplifies quenched variance", "Variance weights squared couplings, so strong I projections can dominate")
    rounded(d, (90, 220, 2310, 1245))
    box = (250, 350, 1400, 1080)
    axes(d, box, "architecture", "quenched input variance")
    categories = [("E-only\nhomogeneous I", [0.55, 0.12, 0.18]), ("paired E/I\nclustered I", [0.35, 0.72, 0.15])]
    colors = [GREEN, RED, BLUE2]
    labels = ["E heterogeneity", "I heterogeneity", "finite-size"]
    x_positions = [0.28, 0.72]
    for xp, (name, vals) in zip(x_positions, categories):
        base = 0
        for val, col in zip(vals, colors):
            x = box[0] + xp * (box[2] - box[0])
            y0 = box[3] - base * (box[3] - box[1])
            y1 = box[3] - (base + val) * (box[3] - box[1]) * 0.75
            top, bottom = sorted((y0, y1))
            d.rectangle([x - 110, top, x + 110, bottom], fill=col, outline="white", width=4)
            base += val
        text_center(d, (x - 170, box[3] + 35, x + 170, box[3] + 125), name, F_SMALL, INK)
    for i, (lab, col) in enumerate(zip(labels, colors)):
        d.rectangle([1540, 410 + i * 75, 1600, 460 + i * 75], fill=col)
        d.text((1625, 410 + i * 75), lab, font=F_SMALL, fill=INK)
    label_box(d, (1530, 720, 2220, 990), "Core mechanism", "If |J_I| is large, small frozen differences in inhibitory cluster wiring contribute a large squared-coupling variance.", RED)
    d.text((1540, 1060), "Prediction: chaos can persist as finite-size noise shrinks.", font=F_SMALL, fill=PURPLE)
    save(im, "ch08-quenched-amplification")


def fig09_xi_kappa():
    im, d = canvas("Diagnostic plane: finite-size noise versus quenched heterogeneity", "Move toward xi = 0 to test whether switching survives the infinite-size limit")
    rounded(d, (90, 220, 2310, 1245))
    box = (320, 350, 1730, 1090)
    axes(d, box, "xi = 1/sqrt(N_E)  (finite-size amplitude)", "kappa  (quenched variability)")
    x0, y0, x1, y1 = box
    d.rectangle([x0, y0, (x0+x1)/2, (y0+y1)/2], fill="#f2fbf6")
    d.rectangle([(x0+x1)/2, y0, x1, (y0+y1)/2], fill="#fff3e6")
    d.rectangle([x0, (y0+y1)/2, (x0+x1)/2, y1], fill="#eef4fc")
    d.rectangle([(x0+x1)/2, (y0+y1)/2, x1, y1], fill="#f9eef2")
    axes(d, box, "xi = 1/sqrt(N_E)  (finite-size amplitude)", "kappa  (quenched variability)")
    text_center(d, (x0+40, y0+70, (x0+x1)/2-30, (y0+y1)/2-30), "mesoscopic\nchaos candidate", F_LABEL, GREEN)
    text_center(d, ((x0+x1)/2+40, y0+70, x1-40, (y0+y1)/2-30), "mixed effects:\nnoise + disorder", F_LABEL, ORANGE)
    text_center(d, (x0+40, (y0+y1)/2+80, (x0+x1)/2-40, y1-40), "asynchronous\nor fixed point", F_LABEL, BLUE)
    text_center(d, ((x0+x1)/2+45, (y0+y1)/2+80, x1-40, y1-40), "finite-size\nmetastability", F_LABEL, RED)
    arrow(d, (1630, 1165), (520, 1165), fill=PURPLE, width=8)
    d.text((800, 1210), "increase cluster size: xi -> 0", font=F_SMALL, fill=PURPLE)
    label_box(d, (1840, 390, 2240, 720), "Question", "Does switching remain when sampling noise vanishes?", PURPLE)
    label_box(d, (1840, 810, 2240, 1065), "Answer", "Only persistent switching near xi=0 supports chaos.", GREEN)
    save(im, "ch09-xi-kappa-plane")


def fig09_perturb():
    im, d = canvas("Perturbation recovery versus chaotic divergence", "Small-pulse behavior distinguishes basin stability from positive Lyapunov growth")
    rounded(d, (90, 220, 2310, 1245))
    box = (260, 330, 1600, 1090)
    axes(d, box, "time after perturbation", "trajectory distance d(t)")
    xs = [i / 300 for i in range(301)]
    stable = [0.85 * math.exp(-5.5 * x) + 0.03 for x in xs]
    chaos = [min(0.95, 0.05 * math.exp(4.3 * x)) for x in xs]
    large = [0.74 * math.exp(-1.2 * x) + 0.18 * math.exp(-18 * (x - 0.25) ** 2) for x in xs]
    plot_line(d, box, xs, stable, BLUE, 8)
    plot_line(d, box, xs, chaos, RED, 8)
    plot_line(d, box, xs, large, GOLD, 8)
    d.text((610, 580), "stable basin:\ndecay", font=F_SMALL, fill=BLUE)
    d.text((1010, 500), "chaotic flow:\nexp growth", font=F_SMALL, fill=RED)
    d.text((790, 900), "large pulse can\nswitch basins", font=F_SMALL, fill=GOLD)
    label_box(d, (1720, 360, 2220, 620), "Use infinitesimal pulses", "Large basin jumps are not Lyapunov growth.", RED)
    label_box(d, (1720, 735, 2220, 1000), "Expected result", "Attractor: recovery\nChaos: divergence until saturation", PURPLE)
    save(im, "ch09-perturbation-divergence")


def fig09_autocorr():
    im, d = canvas("Zero-lag autocorrelation shape", "Kink suggests finite-size noise; smooth shoulder suggests deterministic chaotic rate")
    rounded(d, (90, 220, 2310, 1245))
    box = (290, 330, 1660, 1090)
    axes(d, box, "lag tau", "autocorrelation")
    xs = [i / 500 for i in range(501)]
    # map x in [0,1] to tau in [-1,1]
    noise = [math.exp(-abs(2*x - 1) / 0.23) for x in xs]
    chaos = [math.exp(-((2*x - 1) / 0.55) ** 2) for x in xs]
    mix = [0.45 * n + 0.55 * c for n, c in zip(noise, chaos)]
    plot_line(d, box, xs, noise, BLUE, 7)
    plot_line(d, box, xs, chaos, RED, 8)
    plot_line(d, box, xs, mix, PURPLE, 7)
    mid = (box[0] + box[2]) / 2
    d.line([(mid, box[1]), (mid, box[3])], fill=GRID, width=3)
    d.text((mid - 30, box[3] + 90), "0", font=F_SMALL, fill=MUTED)
    d.text((1150, 540), "smooth chaotic", font=F_SMALL, fill=RED)
    d.text((980, 735), "mixture", font=F_SMALL, fill=PURPLE)
    d.text((760, 900), "finite-size cusp", font=F_SMALL, fill=BLUE)
    label_box(d, (1745, 390, 2240, 690), "Practical test", "Zoom near tau=0 after changing N_E.", GREEN)
    label_box(d, (1745, 790, 2240, 1055), "Interpretation", "The cusp should shrink with xi; smooth chaos should persist.", PURPLE)
    save(im, "ch09-autocorrelation-kink")


def fig09_regimes():
    im, d = canvas("A/B/C scaling regimes", "Separate finite-size variance, quenched variance, and many-unit DMFT availability")
    rounded(d, (90, 220, 2310, 1245))
    box = (240, 360, 1680, 1040)
    axes(d, box, "regime", "relative contribution")
    regimes = [("A\nsmall clusters", [0.75, 0.25, 0.1]), ("B\nfew large clusters", [0.12, 0.78, 0.25]), ("C\nmany large clusters", [0.08, 0.72, 0.9])]
    colors = [BLUE, RED, GREEN]
    labels = ["finite-size variance", "quenched variance", "DMFT units"]
    group_w = 330
    for gi, (name, vals) in enumerate(regimes):
        gx = box[0] + 230 + gi * 420
        for bi, (val, col) in enumerate(zip(vals, colors)):
            x = gx + (bi - 1) * 82
            y = box[3] - val * (box[3] - box[1]) * 0.85
            d.rectangle([x - 30, y, x + 30, box[3]], fill=col)
        text_center(d, (gx - 160, box[3] + 35, gx + 160, box[3] + 140), name, F_SMALL, INK)
    for i, (lab, col) in enumerate(zip(labels, colors)):
        d.rectangle([1800, 410 + i * 80, 1860, 460 + i * 80], fill=col)
        d.text((1885, 410 + i * 80), lab, font=F_SMALL, fill=INK)
    label_box(d, (1780, 770, 2240, 1055), "Clean chaos target", "Regime C: finite-size noise small, quenched disorder present, many cluster units.", PURPLE)
    save(im, "ch09-regimes-abc-variance")


def fig10_phase():
    im, d = canvas("Research phase diagram", "Classify dynamics by cluster strength and heterogeneity")
    rounded(d, (90, 220, 2310, 1245))
    box = (280, 340, 1700, 1095)
    x0, y0, x1, y1 = box
    d.polygon([(x0, y1), (x0, y0+150), (x0+430, y0+320), (x0+545, y1)], fill="#eef4fc")
    d.polygon([(x0+430, y0+320), (x0+890, y0+170), (x1, y0+220), (x1, y1), (x0+545, y1)], fill="#fff1df")
    d.polygon([(x0+890, y0+170), (x1, y0+80), (x1, y0+535), (x0+1090, y0+520)], fill="#f7eaf0")
    d.polygon([(x0+1090, y0+520), (x1, y0+535), (x1, y1), (x0+545, y1)], fill="#edf8f1")
    axes(d, box, "cluster strength J_E+ or s", "heterogeneity kappa or g_het")
    text_center(d, (x0+100, y0+570, x0+500, y0+760), "asynchronous\nirregular", F_LABEL, BLUE)
    text_center(d, (x0+620, y0+450, x0+1000, y0+650), "attractor /\nmetastable", F_LABEL, ORANGE)
    text_center(d, (x0+1050, y0+180, x1-70, y0+380), "transient\nchaos", F_LABEL, RED)
    text_center(d, (x0+980, y0+760, x1-70, y0+960), "mesoscopic\nchaos", F_LABEL, GREEN)
    label_box(d, (1810, 420, 2240, 690), "Measure", "lifetimes, Lyapunov exponents, autocorrelations", PURPLE)
    label_box(d, (1810, 800, 2240, 1045), "Goal", "map regime boundaries, not just mean rates", GREEN)
    save(im, "ch10-phase-diagram-dashboard")


def fig10_observable():
    im, d = canvas("Observable dashboard for simulations", "Classify phases using a bundle of statistics")
    rounded(d, (90, 220, 2310, 1245))
    panels = [(160, 320, 1080, 720), (1320, 320, 2240, 720), (160, 815, 1080, 1215), (1320, 815, 2240, 1215)]
    titles = ["autocorrelation time", "cluster lifetime distribution", "active-cluster count", "summary instability metrics"]
    for box, title in zip(panels, titles):
        rounded(d, box, fill="#ffffff")
        d.text((box[0] + 28, box[1] + 24), title, font=F_LABEL, fill=INK)
    # autocorr
    box = (250, 430, 1000, 660)
    axes(d, box, "lag", "C")
    xs = [i / 200 for i in range(201)]
    plot_line(d, box, xs, [math.exp(-3*x) for x in xs], BLUE, 6)
    plot_line(d, box, xs, [math.exp(-1.2*x*x) for x in xs], RED, 6)
    d.text((740, 515), "HWHM", font=F_TINY, fill=PURPLE)
    # histogram
    x0, y0, x1, y1 = (1400, 450, 2160, 660)
    axes(d, (x0, y0, x1, y1), "lifetime", "count")
    vals = [0.3, 0.55, 0.75, 0.65, 0.42, 0.22, 0.12]
    for i, v in enumerate(vals):
        x = x0 + 50 + i * 95
        d.rectangle([x, y1 - v * 180, x + 58, y1], fill=GOLD)
    # distribution
    x0, y0, x1, y1 = (250, 930, 1000, 1150)
    axes(d, (x0, y0, x1, y1), "active clusters", "prob")
    vals = [0.05, 0.16, 0.31, 0.25, 0.14, 0.06]
    for i, v in enumerate(vals):
        x = x0 + 60 + i * 105
        d.rectangle([x, y1 - v * 520, x + 58, y1], fill=GREEN)
        text_center(d, (x-5, y1+10, x+65, y1+45), str(i+1), F_TINY, MUTED)
    # summary bars
    x0, y0 = 1420, 940
    metrics = [("Fano", 0.55, BLUE), ("Dim.", 0.72, GREEN), ("Lyap.", 0.82, RED), ("HWHM", 0.45, PURPLE)]
    for i, (lab, val, col) in enumerate(metrics):
        y = y0 + i * 56
        d.text((x0, y), lab, font=F_SMALL, fill=INK)
        d.rectangle([x0 + 130, y + 7, x0 + 670, y + 34], fill="#e6ebf0")
        d.rectangle([x0 + 130, y + 7, x0 + 130 + 540 * val, y + 34], fill=col)
    save(im, "ch10-observable-dashboard")


def main():
    for fn in [
        fig01_jacobian, fig01_landscape,
        fig02_spike_filtering, fig02_noise_scaling,
        fig03_lif, fig03_transfer,
        fig04_balance, fig04_sparse,
        fig05_matrix, fig05_landscape,
        fig06_phase, fig06_autocorr,
        fig07_quenched, fig07_dmft,
        fig08_paired, fig08_amplification,
        fig09_xi_kappa, fig09_perturb, fig09_autocorr, fig09_regimes,
        fig10_phase, fig10_observable,
    ]:
        fn()


if __name__ == "__main__":
    main()
