#!/usr/bin/env python3
"""
HMS Appointment Booking Flowchart
Canvas: 520 x 800 pt
"""
import os

SVG_W, SVG_H = 520, 800

LAVEN  = "#e8e8f5"
HDR_BG = "#d0d0ea"
BORDER = "#c0c0dc"
TEXT   = "#1a1a2e"
ARROW  = "#1a1a2e"
OK_BG  = "#e8f0e8"
ERR_BG = "#f0e8e8"

NW, NH, NR = 200, 36, 8
DW, DH     = 200, 52
SR         = 13

CX      = 200   # main column centre x
CX_ERR  = 415   # redirect-to-login branch x


def box(cx, cy, label, fill=None, w=NW, h=NH):
    f = fill or LAVEN
    x, y = cx - w // 2, cy - h // 2
    svg  = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'rx="{NR}" fill="{f}" stroke="{BORDER}" stroke-width="1.1"/>')
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="10.5" fill="{TEXT}">{label}</text>')
    return svg


def box2(cx, cy, line1, line2, fill=None):
    f = fill or LAVEN
    x, y = cx - NW // 2, cy - NH
    svg  = (f'<rect x="{x}" y="{y}" width="{NW}" height="{NH*2-4}" '
            f'rx="{NR}" fill="{f}" stroke="{BORDER}" stroke-width="1.1"/>')
    svg += (f'<text x="{cx}" y="{cy - 7}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="10" fill="{TEXT}">{line1}</text>')
    svg += (f'<text x="{cx}" y="{cy + 9}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="9.5" fill="{TEXT}">{line2}</text>')
    return svg


def diamond(cx, cy, label):
    hw, hh = DW // 2, DH // 2
    pts = f"{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}"
    svg  = f'<polygon points="{pts}" fill="{HDR_BG}" stroke="{BORDER}" stroke-width="1.1"/>'
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="10" fill="{TEXT}">{label}</text>')
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
Y_START    =  38
Y_LOGIN    = 102   # diamond: Patient Logged In?
Y_GOLOGIN  = 102   # error branch (same row)
Y_OPENBOOK = 195
Y_PICKSPEC = 258
Y_LOADDOCS = 320
Y_PICKDOC  = 382
Y_PICKDATE = 444
Y_CONFIRM  = 506
Y_DBINSERT = 575
Y_SUCCESS  = 640
Y_VIEWBOOK = 700
Y_END      = 762

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
parts.append(arr_v(CX, Y_START + SR, Y_LOGIN - DH // 2))

# login diamond → Yes (down)
parts.append(arr_v(CX, Y_LOGIN + DH // 2, Y_OPENBOOK - NH // 2))
parts.append(lbl("Yes", CX + 24, (Y_LOGIN + DH // 2 + Y_OPENBOOK - NH // 2) // 2))

# login diamond → No (right) → Redirect to Login
parts.append(arr_h(CX + DW // 2, CX_ERR, Y_LOGIN))
parts.append(lbl("No", (CX + DW // 2 + CX_ERR) // 2, Y_LOGIN - 12))

# Redirect to Login → End (down along right edge)
parts.append(
    f'<path d="M {CX_ERR} {Y_GOLOGIN + NH//2} L {CX_ERR} {Y_END}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.2" marker-end="url(#arr)"/>'
)
parts.append(
    f'<line x1="{CX_ERR}" y1="{Y_END}" x2="{CX + SR + 6}" y2="{Y_END}" '
    f'stroke="{ARROW}" stroke-width="1.2"/>'
)

# Main booking flow
parts.append(arr_v(CX, Y_OPENBOOK + NH // 2, Y_PICKSPEC - NH // 2))
parts.append(arr_v(CX, Y_PICKSPEC + NH // 2, Y_LOADDOCS - NH // 2))
parts.append(arr_v(CX, Y_LOADDOCS + NH // 2, Y_PICKDOC  - NH // 2))
parts.append(arr_v(CX, Y_PICKDOC  + NH // 2, Y_PICKDATE - NH // 2))
parts.append(arr_v(CX, Y_PICKDATE + NH // 2, Y_CONFIRM  - NH // 2))
parts.append(arr_v(CX, Y_CONFIRM  + NH // 2, Y_DBINSERT - NH + 4))
parts.append(arr_v(CX, Y_DBINSERT + NH + 4,  Y_SUCCESS  - NH // 2))
parts.append(arr_v(CX, Y_SUCCESS  + NH // 2, Y_VIEWBOOK - NH // 2))
parts.append(arr_v(CX, Y_VIEWBOOK + NH // 2, Y_END - SR - 4))

# ── Nodes ─────────────────────────────────────────────────────────────────────
parts.append(start_node(CX, Y_START))
parts.append(diamond(CX, Y_LOGIN, "Patient Logged In?"))
parts.append(box(CX_ERR, Y_GOLOGIN, "Redirect to Login", ERR_BG))
parts.append(box(CX, Y_OPENBOOK, "Open Book Appointment Page"))
parts.append(box(CX, Y_PICKSPEC, "Select Specialty"))
parts.append(box(CX, Y_LOADDOCS, "Fetch Doctors by Specialty"))
parts.append(box(CX, Y_PICKDOC,  "Select Doctor"))
parts.append(box(CX, Y_PICKDATE, "Select Appointment Date"))
parts.append(box(CX, Y_CONFIRM,  "Click Confirm Booking"))
parts.append(box2(CX, Y_DBINSERT,
                  "INSERT INTO appointment",
                  "(pid, docid, date, status=BOOKED)"))
parts.append(box(CX, Y_SUCCESS,  "Booking Confirmed", OK_BG))
parts.append(box(CX, Y_VIEWBOOK, "View in My Bookings"))
parts.append(end_node(CX, Y_END))

parts.append('</svg>')

out_svg = 'diagram5_booking_flowchart.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram5_booking_flowchart.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram5_booking_flowchart.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram5_booking_flowchart.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram5_booking_flowchart.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
