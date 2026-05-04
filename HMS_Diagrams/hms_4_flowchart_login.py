#!/usr/bin/env python3
"""
HMS Login Flowchart
Canvas: 560 x 740 pt
"""
import os

SVG_W, SVG_H = 560, 740

LAVEN  = "#e8e8f5"
HDR_BG = "#d0d0ea"
BORDER = "#c0c0dc"
TEXT   = "#1a1a2e"
ARROW  = "#1a1a2e"
OK_BG  = "#e8f0e8"
ERR_BG = "#f0e8e8"

NW, NH, NR = 190, 36, 8
DW, DH     = 190, 52
SR         = 13

CX      = 215   # main column centre x
CX_ERR  = 445   # error column centre x


def box(cx, cy, label, fill=None, w=NW, h=NH):
    f = fill or LAVEN
    x, y = cx - w // 2, cy - h // 2
    svg  = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'rx="{NR}" fill="{f}" stroke="{BORDER}" stroke-width="1.1"/>')
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="11" fill="{TEXT}">{label}</text>')
    return svg


def diamond(cx, cy, lines):
    hw, hh = DW // 2, DH // 2
    pts = f"{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}"
    svg  = f'<polygon points="{pts}" fill="{HDR_BG}" stroke="{BORDER}" stroke-width="1.1"/>'
    for i, ln in enumerate(lines):
        dy = cy + (i - (len(lines) - 1) / 2) * 12
        svg += (f'<text x="{cx}" y="{dy:.0f}" text-anchor="middle" dominant-baseline="central" '
                f'font-family="Arial,sans-serif" font-size="10" fill="{TEXT}">{ln}</text>')
    return svg


def arr_v(x, y1, y2):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2-8}" '
            f'stroke="{ARROW}" stroke-width="1.3" marker-end="url(#arr)"/>')


def arr_h(x1, x2, y):
    dr = -8 if x2 > x1 else 8
    return (f'<line x1="{x1}" y1="{y}" x2="{x2+dr}" y2="{y}" '
            f'stroke="{ARROW}" stroke-width="1.3" marker-end="url(#arr)"/>')


def lbl(text, x, y):
    w = len(text) * 5.3 + 8
    return (f'<rect x="{x-w/2:.0f}" y="{y-8}" width="{w:.0f}" height="14" fill="white"/>'
            f'<text x="{x}" y="{y+1}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="9.5" fill="{TEXT}">{text}</text>')


def start_node(cx, cy):
    return f'<circle cx="{cx}" cy="{cy}" r="{SR}" fill="{TEXT}"/>'


def end_node(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="{SR+4}" fill="white" '
            f'stroke="{TEXT}" stroke-width="2"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{SR-3}" fill="{TEXT}"/>')


# ── Y positions ───────────────────────────────────────────────────────────────
Y_START      =  38
Y_OPEN       =  95
Y_ENTER      = 158
Y_SUBMIT     = 220
Y_CHECKUSER  = 300   # diamond centre
Y_GETTYPE    = 395
Y_CHECKPASS  = 485   # diamond centre
Y_SETSESSION = 578
Y_REDIRECT   = 650
Y_END        = 715

# Error boxes sit at the same y as the diamonds they branch from
Y_NOUSER     = Y_CHECKUSER
Y_WRONGPASS  = Y_CHECKPASS

# ── SVG scaffold ──────────────────────────────────────────────────────────────
parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'<defs><marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
    f'<polygon points="0 0,8 3,0 6" fill="{ARROW}"/></marker></defs>',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" '
    f'fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
]

# ── Arrows ────────────────────────────────────────────────────────────────────
# Main flow
parts.append(arr_v(CX, Y_START + SR, Y_OPEN - NH // 2))
parts.append(arr_v(CX, Y_OPEN + NH // 2, Y_ENTER - NH // 2))
parts.append(arr_v(CX, Y_ENTER + NH // 2, Y_SUBMIT - NH // 2))
parts.append(arr_v(CX, Y_SUBMIT + NH // 2, Y_CHECKUSER - DH // 2))

# checkuser → Yes (down)
parts.append(arr_v(CX, Y_CHECKUSER + DH // 2, Y_GETTYPE - NH // 2))
parts.append(lbl("Yes", CX + 22, (Y_CHECKUSER + DH // 2 + Y_GETTYPE - NH // 2) // 2))

# checkuser → No (right) → nouser
parts.append(arr_h(CX + DW // 2, CX_ERR, Y_CHECKUSER))
parts.append(lbl("No", (CX + DW // 2 + CX_ERR) // 2, Y_CHECKUSER - 12))

# gettype → checkpass
parts.append(arr_v(CX, Y_GETTYPE + NH // 2, Y_CHECKPASS - DH // 2))

# checkpass → Match (down)
parts.append(arr_v(CX, Y_CHECKPASS + DH // 2, Y_SETSESSION - NH // 2))
parts.append(lbl("Match", CX + 28, (Y_CHECKPASS + DH // 2 + Y_SETSESSION - NH // 2) // 2))

# checkpass → No Match (right)
parts.append(arr_h(CX + DW // 2, CX_ERR, Y_CHECKPASS))
parts.append(lbl("No Match", (CX + DW // 2 + CX_ERR) // 2, Y_CHECKPASS - 12))

# setsession → redirect → end
parts.append(arr_v(CX, Y_SETSESSION + NH // 2, Y_REDIRECT - NH // 2))
parts.append(arr_v(CX, Y_REDIRECT + NH // 2, Y_END - SR - 4))

# Wrong Password → retry back to Enter (dashed right-side path)
retry_rx = CX_ERR + NW // 2 + 30
parts.append(
    f'<path d="M {CX_ERR} {Y_WRONGPASS + NH//2} '
    f'L {CX_ERR} {Y_ENTER + 22} '
    f'L {CX + NW//2 + 4} {Y_ENTER + 22}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.2" '
    f'stroke-dasharray="5,3" marker-end="url(#arr)"/>'
)
parts.append(lbl("Retry", CX_ERR + 30, Y_ENTER + 12))

# No Account Found → End (right-side path down)
parts.append(
    f'<path d="M {CX_ERR} {Y_NOUSER + NH//2} '
    f'L {CX_ERR} {Y_END}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.2" marker-end="url(#arr)"/>'
)
parts.append(
    f'<line x1="{CX_ERR}" y1="{Y_END}" x2="{CX + SR + 6}" y2="{Y_END}" '
    f'stroke="{ARROW}" stroke-width="1.2"/>'
)

# ── Nodes ─────────────────────────────────────────────────────────────────────
parts.append(start_node(CX, Y_START))
parts.append(box(CX, Y_OPEN,       "Open Login Page"))
parts.append(box(CX, Y_ENTER,      "Enter Email &amp; Password"))
parts.append(box(CX, Y_SUBMIT,     "Submit Form"))
parts.append(diamond(CX, Y_CHECKUSER, ["Email in", "webuser table?"]))
parts.append(box(CX_ERR, Y_NOUSER,    "No Account Found",        ERR_BG))
parts.append(box(CX, Y_GETTYPE,    "Get usertype  (p / d / a)"))
parts.append(diamond(CX, Y_CHECKPASS, ["bcrypt.compare", "(password)?"]))
parts.append(box(CX_ERR, Y_WRONGPASS, "Show: Wrong Password",    ERR_BG))
parts.append(box(CX, Y_SETSESSION, "Set req.session.user",       OK_BG))
parts.append(box(CX, Y_REDIRECT,   "Redirect to Dashboard",      OK_BG))
parts.append(end_node(CX, Y_END))

parts.append('</svg>')

out_svg = 'diagram4_login_flowchart.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram4_login_flowchart.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram4_login_flowchart.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram4_login_flowchart.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram4_login_flowchart.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
