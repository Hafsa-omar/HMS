#!/usr/bin/env python3
"""
HMS Activity Diagram — Appointment Booking Workflow
2-swimlane layout: Patient | HMS System
Canvas: 595 x 880 pt
"""
import os

SVG_W, SVG_H = 595, 880

LAVEN  = "#e8e8f5"
HDR_BG = "#d0d0ea"
BORDER = "#c0c0dc"
TEXT   = "#1a1a2e"
ARROW  = "#1a1a2e"

NW, NH, NR = 175, 40, 8
SR   = 13
LH   = 44
MID  = SVG_W // 2          # 297 – vertical divider
PAT_CX = 148               # Patient swimlane centre
SYS_CX = 446               # System swimlane centre


# ── Helpers ──────────────────────────────────────────────────────────────────

def act_box(cx, cy, label):
    x, y = cx - NW//2, cy - NH//2
    svg  = (f'<rect x="{x}" y="{y}" width="{NW}" height="{NH}" '
            f'rx="{NR}" ry="{NR}" fill="{LAVEN}" stroke="{BORDER}" stroke-width="1.1"/>')
    lines = label.split('\n')
    if len(lines) == 1:
        svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
                f'font-family="Arial,sans-serif" font-size="11" fill="{TEXT}">{label}</text>')
    else:
        for i, line in enumerate(lines):
            dy = cy - 7 + i * 14
            svg += (f'<text x="{cx}" y="{dy}" text-anchor="middle" dominant-baseline="central" '
                    f'font-family="Arial,sans-serif" font-size="10" fill="{TEXT}">{line}</text>')
    return svg


def diamond(cx, cy, label):
    hw, hh = 58, 26
    pts = f"{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}"
    svg  = f'<polygon points="{pts}" fill="{HDR_BG}" stroke="{BORDER}" stroke-width="1.1"/>'
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="9.5" fill="{TEXT}">{label}</text>')
    return svg


def start_node(cx, cy):
    return f'<circle cx="{cx}" cy="{cy}" r="{SR}" fill="{TEXT}"/>'


def end_node(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="{SR+4}" fill="white" '
            f'stroke="{TEXT}" stroke-width="2"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{SR-3}" fill="{TEXT}"/>')


def v_arrow(cx, y1, y2, dashed=False):
    dash = ' stroke-dasharray="5,3"' if dashed else ''
    return (f'<line x1="{cx}" y1="{y1}" x2="{cx}" y2="{y2-8}" '
            f'stroke="{ARROW}" stroke-width="1.3"{dash} marker-end="url(#arr)"/>')


def h_arrow(x1, x2, y, dashed=False):
    dash = ' stroke-dasharray="5,3"' if dashed else ''
    dr = -1 if x2 < x1 else 1
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - dr*8}" y2="{y}" '
            f'stroke="{ARROW}" stroke-width="1.3"{dash} marker-end="url(#arr)"/>')


def lbl(text, x, y):
    w = len(text)*5.4 + 8
    return (f'<rect x="{x - w/2:.0f}" y="{y-8}" width="{w:.0f}" height="15" fill="white"/>'
            f'<text x="{x:.0f}" y="{y+1:.0f}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="9.5" fill="{TEXT}">{text}</text>')


# ── Y positions ───────────────────────────────────────────────────────────────
Y_START  =  55
Y_P1     = 115   # Patient: Open App & Navigate
Y_P2     = 175   # Patient: Enter Login Credentials
# Interaction 1: login request / response
Y_I1     = 230   # horizontal arrow y (request goes right)
Y_S1     = 240   # System: Authenticate User & Create Session
Y_P3     = 310   # Patient: View Dashboard
Y_P4     = 370   # Patient: Select Specialty & Doctor
# Interaction 2: doctor list
Y_I2     = 420
Y_S2     = 430   # System: Query & Return Doctor List
Y_P5     = 500   # Patient: Choose Date & Confirm
# Interaction 3: book request
Y_I3     = 555
Y_S3     = 565   # System: Process & Save Booking
Y_D1     = 630   # Decision: Slot available?
Y_P6     = 700   # Patient: Booking Confirmed
Y_ERR    = 700   # System: Return Error (same row, right side)
Y_END    = 780

# ── SVG scaffold ──────────────────────────────────────────────────────────────
parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'<defs><marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
    f'<polygon points="0 0,8 3,0 6" fill="{ARROW}"/></marker></defs>',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
    # Swimlane divider
    f'<line x1="{MID}" y1="28" x2="{MID}" y2="{SVG_H-10}" stroke="{BORDER}" stroke-width="1" stroke-dasharray="6,3"/>',
    # Swimlane headers
    f'<rect x="0.5" y="0.5" width="{MID-1}" height="28" fill="{HDR_BG}"/>',
    f'<rect x="{MID}" y="0.5" width="{SVG_W-MID-1}" height="28" fill="{HDR_BG}"/>',
    f'<text x="{PAT_CX}" y="15" text-anchor="middle" dominant-baseline="central" '
    f'font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{TEXT}">Patient</text>',
    f'<text x="{SYS_CX}" y="15" text-anchor="middle" dominant-baseline="central" '
    f'font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{TEXT}">HMS System</text>',
]

# ── Arrows ─────────────────────────────────────────────────────────────────────
# Patient vertical flow
parts.append(v_arrow(PAT_CX, Y_START + SR,   Y_P1  - NH//2))
parts.append(v_arrow(PAT_CX, Y_P1   + NH//2, Y_P2  - NH//2))
parts.append(v_arrow(PAT_CX, Y_P2   + NH//2, Y_I1  - 7))
# Interaction 1: login request →
parts.append(h_arrow(PAT_CX + NW//2, SYS_CX - NW//2, Y_I1 - 7))
parts.append(lbl("Login Request", MID, Y_I1 - 18))
# System processes login
parts.append(v_arrow(SYS_CX, Y_I1 + 7,  Y_S1 - NH//2))
# Response ← (dashed)
parts.append(h_arrow(SYS_CX - NW//2, PAT_CX + NW//2, Y_I1 + 7, dashed=True))
parts.append(lbl("Session Cookie", MID, Y_I1 + 18))
# Continue patient flow
parts.append(v_arrow(PAT_CX, Y_I1 + 30,  Y_P3 - NH//2))
parts.append(v_arrow(PAT_CX, Y_P3 + NH//2, Y_P4 - NH//2))
parts.append(v_arrow(PAT_CX, Y_P4 + NH//2, Y_I2 - 7))
# Interaction 2: doctor query →
parts.append(h_arrow(PAT_CX + NW//2, SYS_CX - NW//2, Y_I2 - 7))
parts.append(lbl("GET /api/doctors", MID, Y_I2 - 18))
parts.append(v_arrow(SYS_CX, Y_I2 + 7, Y_S2 - NH//2))
# Response ← (dashed)
parts.append(h_arrow(SYS_CX - NW//2, PAT_CX + NW//2, Y_I2 + 7, dashed=True))
parts.append(lbl("JSON doctor list", MID, Y_I2 + 18))
# Continue patient flow
parts.append(v_arrow(PAT_CX, Y_I2 + 30,  Y_P5 - NH//2))
parts.append(v_arrow(PAT_CX, Y_P5 + NH//2, Y_I3 - 7))
# Interaction 3: book request →
parts.append(h_arrow(PAT_CX + NW//2, SYS_CX - NW//2, Y_I3 - 7))
parts.append(lbl("POST /api/book", MID, Y_I3 - 18))
parts.append(v_arrow(SYS_CX, Y_I3 + 7, Y_S3 - NH//2))
parts.append(v_arrow(SYS_CX, Y_S3 + NH//2, Y_D1 - 26))
# Decision: Yes → system side
parts.append(v_arrow(SYS_CX, Y_D1 - 26, Y_D1 - 26))  # stub
# Yes branch → back to patient
parts.append(h_arrow(SYS_CX - 60, PAT_CX + NW//2, Y_D1, dashed=True))
parts.append(lbl("[Yes] Confirmed", MID - 20, Y_D1 - 12))
parts.append(v_arrow(PAT_CX, Y_D1 + 10, Y_P6 - NH//2))
parts.append(v_arrow(PAT_CX, Y_P6 + NH//2, Y_END - SR - 4))
# No branch → error box
parts.append(v_arrow(SYS_CX, Y_D1 + 26, Y_ERR - NH//2))
parts.append(lbl("[No] Slot taken", SYS_CX + 72, Y_D1 + 15))

# ── Nodes & boxes ─────────────────────────────────────────────────────────────
parts.append(start_node(PAT_CX, Y_START))
parts.append(act_box(PAT_CX, Y_P1, "Open App &amp; Navigate"))
parts.append(act_box(PAT_CX, Y_P2, "Enter Login Credentials"))
parts.append(act_box(SYS_CX, Y_S1, "Authenticate User\n&amp; Create Session"))
parts.append(act_box(PAT_CX, Y_P3, "View Dashboard"))
parts.append(act_box(PAT_CX, Y_P4, "Select Specialty &amp; Doctor"))
parts.append(act_box(SYS_CX, Y_S2, "Query &amp; Return\nDoctor List"))
parts.append(act_box(PAT_CX, Y_P5, "Choose Date &amp; Confirm"))
parts.append(act_box(SYS_CX, Y_S3, "Process &amp; Save Booking"))
parts.append(diamond(SYS_CX, Y_D1, "Slot available?"))
parts.append(act_box(PAT_CX, Y_P6, "Booking Confirmed"))
parts.append(act_box(SYS_CX, Y_ERR, "Return Error Message"))
parts.append(end_node(PAT_CX, Y_END))

parts.append('</svg>')

out_svg = 'diagram10_activity.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram10_activity.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram10_activity.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram10_activity.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram10_activity.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
