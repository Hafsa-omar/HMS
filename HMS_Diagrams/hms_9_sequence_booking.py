#!/usr/bin/env python3
"""
HMS Appointment Booking Sequence Diagram
Canvas: 720 x 600 pt
"""
import os

SVG_W, SVG_H = 720, 600

LAVEN  = "#e8e8f5"
HDR_BG = "#d0d0ea"
BORDER = "#c0c0dc"
TEXT   = "#1a1a2e"
ARROW  = "#1a1a2e"

BOX_W, BOX_H = 110, 36
FS_ACT = 10.5
FS_MSG = 9.5
ACT_Y  = 40
LIFE_TOP = ACT_Y + BOX_H
LIFE_BOT = SVG_H - 30

ACTORS = [
    ("Patient",           85),
    ("Browser",          225),
    ("Express /api",     400),
    ("MySQL DB",         570),
    ("File System",      685),
]
# Trim to 4 actors (no file system needed for booking)
ACTORS = [
    ("Patient",          85),
    ("Browser",         230),
    ("Express /api",    410),
    ("MySQL DB",        590),
]

def actor_box(cx, label):
    x = cx - BOX_W//2
    svg  = (f'<rect x="{x}" y="{ACT_Y}" width="{BOX_W}" height="{BOX_H}" '
            f'rx="5" ry="5" fill="{HDR_BG}" stroke="{BORDER}" stroke-width="1.1"/>')
    svg += (f'<text x="{cx}" y="{ACT_Y + BOX_H//2 + 1}" text-anchor="middle" '
            f'dominant-baseline="central" font-family="Arial,sans-serif" '
            f'font-size="{FS_ACT}" font-weight="bold" fill="{TEXT}">{label}</text>')
    return svg

def lifeline(cx):
    return (f'<line x1="{cx}" y1="{LIFE_TOP}" x2="{cx}" y2="{LIFE_BOT}" '
            f'stroke="{BORDER}" stroke-width="1" stroke-dasharray="5,3"/>')

def activation(cx, y1, y2):
    return (f'<rect x="{cx-5}" y="{y1}" width="10" height="{y2-y1}" '
            f'fill="{LAVEN}" stroke="{BORDER}" stroke-width="0.8"/>')

def msg(x1, x2, y, label, dashed=False):
    dr = -1 if x2 < x1 else 1
    dash = ' stroke-dasharray="5,3"' if dashed else ''
    svg  = (f'<line x1="{x1}" y1="{y}" x2="{x2 - dr*8}" y2="{y}" '
            f'stroke="{ARROW}" stroke-width="1.3"{dash} marker-end="url(#arr)"/>')
    mx = (x1 + x2) // 2
    w  = len(label) * 5 + 10
    svg += f'<rect x="{mx - w//2}" y="{y-11}" width="{w:.0f}" height="14" fill="white"/>'
    svg += (f'<text x="{mx}" y="{y-4}" text-anchor="middle" '
            f'font-family="Arial,sans-serif" font-size="{FS_MSG}" fill="{TEXT}">{label}</text>')
    return svg

CX = {name: cx for name, cx in ACTORS}

parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'<defs><marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
    f'<polygon points="0 0,8 3,0 6" fill="{ARROW}"/></marker></defs>',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" '
    f'fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
]

for name, cx in ACTORS:
    parts.append(actor_box(cx, name))
    parts.append(lifeline(cx))

parts.append(activation(CX["Browser"],      90, 560))
parts.append(activation(CX["Express /api"], 130, 520))
parts.append(activation(CX["MySQL DB"],     165, 480))

steps = [
    (CX["Patient"],       CX["Browser"],      100, "Click 'Book Appointment'",                False),
    (CX["Browser"],       CX["Express /api"], 135, "GET /api/specialties",                    False),
    (CX["Express /api"],  CX["MySQL DB"],     170, "SELECT * FROM specialties",               False),
    (CX["MySQL DB"],      CX["Express /api"], 205, "specialty list",                          True),
    (CX["Express /api"],  CX["Browser"],      240, "200 JSON specialties",                    True),
    (CX["Patient"],       CX["Browser"],      275, "Select specialty, country, city",         False),
    (CX["Browser"],       CX["Express /api"], 310, "GET /api/doctors/specialty/:id?country=X", False),
    (CX["Express /api"],  CX["MySQL DB"],     345, "SELECT doctor WHERE specialties=? AND country=?", False),
    (CX["MySQL DB"],      CX["Express /api"], 380, "filtered doctor rows",                    True),
    (CX["Express /api"],  CX["Browser"],      415, "200 JSON doctor list",                    True),
    (CX["Patient"],       CX["Browser"],      450, "Select doctor &amp; date → Confirm",      False),
    (CX["Browser"],       CX["Express /api"], 482, "POST /api/book  { docid, appodate }",     False),
    (CX["Express /api"],  CX["MySQL DB"],     514, "INSERT INTO appointment (pid,scheduleid,appodate)", False),
    (CX["MySQL DB"],      CX["Express /api"], 546, "insertId",                                True),
    (CX["Express /api"],  CX["Browser"],      568, "200 { success:true, appointmentId }",     True),
]

for x1, x2, y, label, dashed in steps:
    if y < LIFE_BOT - 5:
        parts.append(msg(x1, x2, y, label, dashed))

parts.append('</svg>')

out_svg = 'diagram9_sequence_booking.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram9_sequence_booking.png',
                     output_width=SVG_W*2, output_height=SVG_H*2)
    print("Saved: diagram9_sequence_booking.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(f'inkscape "{out_svg}" --export-filename="diagram9_sequence_booking.png" --export-dpi=180 2>nul')
    if rc == 0:
        print("Saved: diagram9_sequence_booking.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
