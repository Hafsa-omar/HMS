#!/usr/bin/env python3
"""
HMS Full System Sequence Diagram
Shows the complete interaction between all actors and system components.
Canvas: 860 x 720 pt
"""
import os

SVG_W, SVG_H = 860, 720

LAVEN  = "#e8e8f5"
HDR_BG = "#d0d0ea"
BORDER = "#c0c0dc"
TEXT   = "#1a1a2e"
ARROW  = "#1a1a2e"

BOX_W, BOX_H = 110, 36
FS_ACT = 10
FS_MSG = 9.5
ACT_Y  = 40
LIFE_TOP = ACT_Y + BOX_H
LIFE_BOT = SVG_H - 30
ACT_W  = 80
ACT_H  = 28

ACTORS = [
    ("Patient",          100),
    ("Browser",          235),
    ("Express Server",   390),
    ("MySQL DB",         560),
    ("File System",      720),
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

def msg(x1, x2, y, label, dashed=False, color=ARROW):
    dash = ' stroke-dasharray="5,3"' if dashed else ''
    dr = -1 if x2 < x1 else 1
    svg  = (f'<line x1="{x1}" y1="{y}" x2="{x2 - dr*8}" y2="{y}" '
            f'stroke="{color}" stroke-width="1.2"{dash} marker-end="url(#arr)"/>')
    mx = (x1 + x2) // 2
    w  = len(label) * 5 + 10
    svg += (f'<rect x="{mx - w//2}" y="{y-11}" width="{w}" height="14" fill="white"/>')
    svg += (f'<text x="{mx}" y="{y-4}" text-anchor="middle" '
            f'font-family="Arial,sans-serif" font-size="{FS_MSG}" fill="{TEXT}">{label}</text>')
    return svg

def note(x, y, text):
    lines = text.split('\n')
    w = max(len(l) for l in lines) * 5.5 + 14
    h = len(lines) * 14 + 8
    svg = (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h:.0f}" '
           f'fill="#fffff0" stroke="#b0b080" stroke-width="0.8" rx="3"/>')
    for i, line in enumerate(lines):
        svg += (f'<text x="{x+7}" y="{y + 12 + i*14}" '
                f'font-family="Arial,sans-serif" font-size="9" fill="{TEXT}">{line}</text>')
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

# Activations
parts.append(activation(CX["Browser"],        80,  680))
parts.append(activation(CX["Express Server"], 120, 640))
parts.append(activation(CX["MySQL DB"],       160, 580))

# ── Messages ─────────────────────────────────────────────────────────────────
Y = 100
messages = [
    # (from, to, label, dashed)
    ("Patient",        "Browser",       "Open browser / navigate to /",      False),
    ("Browser",        "Express Server","GET /",                              False),
    ("Express Server", "Browser",       "200 index.html",                    True),
    ("Patient",        "Browser",       "Fill login form & submit",          False),
    ("Browser",        "Express Server","POST /auth/login",                  False),
    ("Express Server", "MySQL DB",      "SELECT FROM webuser + patient",     False),
    ("MySQL DB",       "Express Server","User record + bcrypt hash",         True),
    ("Express Server", "Browser",       "302 redirect /dashboard  (session cookie)", True),
    ("Patient",        "Browser",       "Click Book Appointment",            False),
    ("Browser",        "Express Server","GET /api/doctors?specialty=X",      False),
    ("Express Server", "MySQL DB",      "SELECT doctor JOIN specialties",    False),
    ("MySQL DB",       "Express Server","Doctor list rows",                  True),
    ("Express Server", "Browser",       "200 JSON doctor list",              True),
    ("Patient",        "Browser",       "Select doctor & date → submit",     False),
    ("Browser",        "Express Server","POST /api/book",                    False),
    ("Express Server", "MySQL DB",      "INSERT INTO appointment",           False),
    ("MySQL DB",       "Express Server","insertId",                          True),
    ("Express Server", "Browser",       "200 { success: true }",            True),
    ("Patient",        "Browser",       "Upload document",                   False),
    ("Browser",        "Express Server","POST /api/documents/upload (multipart)", False),
    ("Express Server", "File System",   "Write file to uploads/",            False),
    ("File System",    "Express Server","File stored OK",                    True),
    ("Express Server", "MySQL DB",      "INSERT INTO patient_documents",     False),
    ("MySQL DB",       "Express Server","OK",                                True),
    ("Express Server", "Browser",       "200 { success: true, id }",        True),
]

step_h = (LIFE_BOT - LIFE_TOP - 20) / len(messages)
for i, (frm, to, label, dashed) in enumerate(messages):
    y = LIFE_TOP + 10 + int(i * step_h)
    parts.append(msg(CX[frm], CX[to], y, label, dashed))

parts.append('</svg>')

out_svg = 'diagram7_sequence_full.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram7_sequence_full.png',
                     output_width=SVG_W*2, output_height=SVG_H*2)
    print("Saved: diagram7_sequence_full.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(f'inkscape "{out_svg}" --export-filename="diagram7_sequence_full.png" --export-dpi=180 2>nul')
    if rc == 0:
        print("Saved: diagram7_sequence_full.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
