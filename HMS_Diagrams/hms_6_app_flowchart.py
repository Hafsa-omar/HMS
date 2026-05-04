#!/usr/bin/env python3
"""
HMS Application Navigation Flowchart
Shows the page-routing logic after login by user role.
Canvas: 700 x 780 pt
"""
import os

SVG_W, SVG_H = 700, 780

LAVEN  = "#e8e8f5"
HDR_BG = "#d0d0ea"
BORDER = "#c0c0dc"
TEXT   = "#1a1a2e"
ARROW  = "#1a1a2e"

NW, NH, NR = 170, 38, 8
DW, DH     = 170, 50   # diamond
SR         = 13

def box(cx, cy, label, w=NW, h=NH):
    x, y = cx - w//2, cy - h//2
    svg  = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'rx="{NR}" ry="{NR}" fill="{LAVEN}" stroke="{BORDER}" stroke-width="1.1"/>')
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="11" fill="{TEXT}">{label}</text>')
    return svg

def diamond(cx, cy, label):
    hw, hh = DW//2, DH//2
    pts = f"{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}"
    svg  = f'<polygon points="{pts}" fill="{HDR_BG}" stroke="{BORDER}" stroke-width="1.1"/>'
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="10" fill="{TEXT}">{label}</text>')
    return svg

def arrow_v(x, y1, y2):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2-8}" '
            f'stroke="{ARROW}" stroke-width="1.3" marker-end="url(#arr)"/>')

def arrow_h(x1, x2, y):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2-8 if x2>x1 else x2+8}" y2="{y}" '
            f'stroke="{ARROW}" stroke-width="1.3" marker-end="url(#arr)"/>')

def lbl(text, x, y):
    w = len(text)*5.2+8
    return (f'<rect x="{x-w/2:.0f}" y="{y-8}" width="{w:.0f}" height="15" fill="white"/>'
            f'<text x="{x}" y="{y+1}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="9.5" fill="{TEXT}">{text}</text>')

def start_node(cx, cy):
    return f'<circle cx="{cx}" cy="{cy}" r="{SR}" fill="{TEXT}"/>'

def end_node(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="{SR+4}" fill="white" stroke="{TEXT}" stroke-width="2"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{SR-3}" fill="{TEXT}"/>')

CX = 350   # centre x

Y_START  =  35
Y_LAND   =  95   # Landing page
Y_LOGIN  = 175   # Login page
Y_ROLE   = 265   # Role decision diamond
Y_PAT    = 360   # Patient dashboard
Y_DOC    = 360   # Doctor dashboard
Y_ADM    = 360   # Admin dashboard
CX_PAT   = 140
CX_DOC   = 350
CX_ADM   = 560

parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'<defs><marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
    f'<polygon points="0 0,8 3,0 6" fill="{ARROW}"/></marker></defs>',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" '
    f'fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
]

# ── Arrows ────────────────────────────────────────────────────────────────────
# Start → Landing
parts.append(arrow_v(CX, Y_START+SR, Y_LAND-NH//2))
# Landing → Login
parts.append(arrow_v(CX, Y_LAND+NH//2, Y_LOGIN-NH//2))
# Login → Role diamond
parts.append(arrow_v(CX, Y_LOGIN+NH//2, Y_ROLE-DH//2))
parts.append(lbl("Authenticated", CX+48, (Y_LOGIN+NH//2+Y_ROLE-DH//2)//2))

# Role → Patient (left diagonal)
parts.append(f'<line x1="{CX-DW//2}" y1="{Y_ROLE}" x2="{CX_PAT+NW//2+5}" y2="{Y_PAT-NH//2}" '
             f'stroke="{ARROW}" stroke-width="1.3" marker-end="url(#arr)"/>')
parts.append(lbl("Patient", (CX-DW//2+CX_PAT)//2, (Y_ROLE+Y_PAT)//2 - 12))

# Role → Doctor (straight down)
parts.append(arrow_v(CX_DOC, Y_ROLE+DH//2, Y_DOC-NH//2))
parts.append(lbl("Doctor", CX_DOC+42, (Y_ROLE+DH//2+Y_DOC-NH//2)//2))

# Role → Admin (right diagonal)
parts.append(f'<line x1="{CX+DW//2}" y1="{Y_ROLE}" x2="{CX_ADM-NW//2-5}" y2="{Y_ADM-NH//2}" '
             f'stroke="{ARROW}" stroke-width="1.3" marker-end="url(#arr)"/>')
parts.append(lbl("Admin", (CX+DW//2+CX_ADM)//2, (Y_ROLE+Y_ADM)//2 - 12))

# Patient sub-pages
Y_P1 = Y_PAT + 75
patient_pages = ["Book Appointment", "My Bookings", "Lab Results", "Health Record", "Settings"]
for i, pg in enumerate(patient_pages):
    parts.append(arrow_v(CX_PAT, Y_PAT+NH//2 + i*62, Y_PAT+NH//2 + i*62 + 62-NH-10))
    parts.append(box(CX_PAT, Y_PAT+NH//2 + i*62 + 31 + NH//2, pg, w=160))

# Doctor sub-pages
Y_D1 = Y_DOC + 75
doctor_pages = ["My Appointments", "My Patients", "Add Lab Result", "Settings"]
for i, pg in enumerate(doctor_pages):
    parts.append(arrow_v(CX_DOC, Y_DOC+NH//2 + i*62, Y_DOC+NH//2 + i*62 + 62-NH-10))
    parts.append(box(CX_DOC, Y_DOC+NH//2 + i*62 + 31 + NH//2, pg, w=160))

# Admin sub-pages
Y_A1 = Y_ADM + 75
admin_pages = ["All Patients", "All Doctors", "All Appointments"]
for i, pg in enumerate(admin_pages):
    parts.append(arrow_v(CX_ADM, Y_ADM+NH//2 + i*62, Y_ADM+NH//2 + i*62 + 62-NH-10))
    parts.append(box(CX_ADM, Y_ADM+NH//2 + i*62 + 31 + NH//2, pg, w=160))

# ── Nodes & Boxes ──────────────────────────────────────────────────────────────
parts.append(start_node(CX, Y_START))
parts.append(box(CX, Y_LAND, "Landing Page (index.html)"))
parts.append(box(CX, Y_LOGIN, "Login / Register"))
parts.append(diamond(CX, Y_ROLE, "User Role?"))
parts.append(box(CX_PAT, Y_PAT, "Patient Dashboard"))
parts.append(box(CX_DOC, Y_DOC, "Doctor Dashboard"))
parts.append(box(CX_ADM, Y_ADM, "Admin Dashboard"))

parts.append('</svg>')

out_svg = 'diagram6_app_flowchart.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram6_app_flowchart.png',
                     output_width=SVG_W*2, output_height=SVG_H*2)
    print("Saved: diagram6_app_flowchart.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(f'inkscape "{out_svg}" --export-filename="diagram6_app_flowchart.png" --export-dpi=180 2>nul')
    if rc == 0:
        print("Saved: diagram6_app_flowchart.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
