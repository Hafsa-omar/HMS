#!/usr/bin/env python3
"""
HMS State Machine Diagram — Appointment Lifecycle
Canvas: 595 x 730 pt
"""
import os, math

SVG_W, SVG_H = 595, 730

LAVEN  = "#e8e8f5"
BORDER = "#c0c0dc"
TEXT   = "#1a1a2e"
ARROW  = "#1a1a2e"

NW, NH, NR = 160, 44, 8   # state box dims
SR = 13                    # start/end circle radius


# ── Helpers ──────────────────────────────────────────────────────────────────

def state_box(cx, cy, label):
    x, y = cx - NW // 2, cy - NH // 2
    svg  = (f'<rect x="{x}" y="{y}" width="{NW}" height="{NH}" '
            f'rx="{NR}" ry="{NR}" fill="{LAVEN}" stroke="{BORDER}" stroke-width="1.1"/>')
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="12" fill="{TEXT}">{label}</text>')
    return svg


def start_node(cx, cy):
    return f'<circle cx="{cx}" cy="{cy}" r="{SR}" fill="{TEXT}"/>'


def end_node(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="{SR + 4}" fill="white" '
            f'stroke="{TEXT}" stroke-width="2"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{SR - 3}" fill="{TEXT}"/>')


def arrow(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    dist   = math.hypot(dx, dy)
    ux, uy = dx / dist, dy / dist
    ex, ey = x2 - ux * 10, y2 - uy * 10
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" '
            f'stroke="{ARROW}" stroke-width="1.3" marker-end="url(#arr)"/>')


def lbl(text, x, y):
    """Label with white background so it stays readable over arrow lines."""
    w = len(text) * 5.4 + 10
    return (
        f'<rect x="{x - w/2:.0f}" y="{y - 8}" width="{w:.0f}" height="15" fill="white"/>'
        f'<text x="{x:.0f}" y="{y + 1:.0f}" text-anchor="middle" '
        f'dominant-baseline="central" font-family="Arial,sans-serif" '
        f'font-size="10" fill="{TEXT}">{text}</text>'
    )


# ── State centres ─────────────────────────────────────────────────────────────
CX_MAIN = 120    # left column: Confirmed, Completed, Lab Result Added
CX_CANC = 475    # right column: Cancelled
CX_MID  = 297    # centre: ●, Booked, ⬤

Y_START  =  45
Y_BOOKED = 130
Y_CONF   = 270
Y_COMP   = 410
Y_LAB    = 548
Y_END    = 660

# ── SVG scaffold ──────────────────────────────────────────────────────────────
parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'<defs>'
    f'<marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
    f'<polygon points="0 0,8 3,0 6" fill="{ARROW}"/></marker>'
    f'</defs>',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" '
    f'fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
    # Subtitle
    f'<text x="{SVG_W//2}" y="18" text-anchor="middle" '
    f'font-family="Arial,sans-serif" font-size="11" font-style="italic" '
    f'fill="{TEXT}">«Appointment Lifecycle»</text>',
]

# ── Transition arrows (drawn first, behind state boxes) ───────────────────────

# 1. Start → Booked
parts.append(arrow(CX_MID, Y_START + SR, CX_MID, Y_BOOKED - NH // 2))

# 2. Booked → Confirmed  (diagonal left-down)
parts.append(arrow(CX_MID, Y_BOOKED + NH // 2, CX_MAIN, Y_CONF - NH // 2))

# 3. Booked → Cancelled  (diagonal right-down)
parts.append(arrow(CX_MID, Y_BOOKED + NH // 2, CX_CANC, Y_CONF - NH // 2))

# 4. Confirmed → Cancelled  (horizontal right)
parts.append(arrow(CX_MAIN + NW // 2, Y_CONF, CX_CANC - NW // 2, Y_CONF))

# 5. Confirmed → Completed  (vertical down)
parts.append(arrow(CX_MAIN, Y_CONF + NH // 2, CX_MAIN, Y_COMP - NH // 2))

# 6. Completed → Lab Result Added  (vertical down)
parts.append(arrow(CX_MAIN, Y_COMP + NH // 2, CX_MAIN, Y_LAB - NH // 2))

# 7. Lab Result Added → End  (diagonal right-down)
parts.append(arrow(CX_MAIN, Y_LAB + NH // 2, CX_MID, Y_END - SR - 4))

# 8. Cancelled → End  (diagonal left-down)
parts.append(arrow(CX_CANC, Y_CONF + NH // 2, CX_MID, Y_END - SR - 4))

# ── Transition labels (with white background) ─────────────────────────────────

# 1. Start → Booked  (vertical, right side)
parts.append(lbl("Patient confirms booking", CX_MID + 75, (Y_START + Y_BOOKED) // 2 + 4))

# 2. Booked → Confirmed  (diagonal, label near midpoint)
parts.append(lbl("Appointment scheduled",
                  (CX_MID + CX_MAIN) // 2 - 18,
                  (Y_BOOKED + NH // 2 + Y_CONF - NH // 2) // 2 - 8))

# 3. Booked → Cancelled  (diagonal)
parts.append(lbl("Patient cancels",
                  (CX_MID + CX_CANC) // 2 + 20,
                  (Y_BOOKED + NH // 2 + Y_CONF - NH // 2) // 2 - 8))

# 4. Confirmed → Cancelled  (horizontal)
parts.append(lbl("Cancellation request", (CX_MAIN + NW // 2 + CX_CANC - NW // 2) // 2, Y_CONF - 12))

# 5. Confirmed → Completed  (vertical, right side)
parts.append(lbl("Patient attends", CX_MAIN + 68, (Y_CONF + Y_COMP) // 2))

# 6. Completed → Lab Result Added  (vertical, right side)
parts.append(lbl("Doctor adds result", CX_MAIN + 72, (Y_COMP + Y_LAB) // 2))

# 7. Lab Result Added → End  (diagonal)
parts.append(lbl("Results available",
                  (CX_MAIN + CX_MID) // 2 - 10,
                  (Y_LAB + NH // 2 + Y_END - SR - 4) // 2 + 4))

# ── State boxes (on top of arrows) ───────────────────────────────────────────
parts.append(start_node(CX_MID, Y_START))
parts.append(state_box(CX_MID,  Y_BOOKED, "Booked"))
parts.append(state_box(CX_MAIN, Y_CONF,   "Confirmed"))
parts.append(state_box(CX_CANC, Y_CONF,   "Cancelled"))
parts.append(state_box(CX_MAIN, Y_COMP,   "Completed"))
parts.append(state_box(CX_MAIN, Y_LAB,    "Lab Result Added"))
parts.append(end_node(CX_MID, Y_END))

parts.append('</svg>')

out_svg = 'diagram12_state_machine.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram12_state_machine.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram12_state_machine.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram12_state_machine.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram12_state_machine.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
