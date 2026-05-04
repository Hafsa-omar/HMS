#!/usr/bin/env python3
"""
HMS Login Sequence Diagram
Canvas: 680 x 580 pt
"""
import os

SVG_W, SVG_H = 680, 580

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
    ("Patient",        90),
    ("Browser",       230),
    ("Express /auth", 400),
    ("MySQL DB",      570),
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
    w  = len(label) * 5.1 + 10
    svg += f'<rect x="{mx - w//2}" y="{y-11}" width="{w:.0f}" height="14" fill="white"/>'
    svg += (f'<text x="{mx}" y="{y-4}" text-anchor="middle" '
            f'font-family="Arial,sans-serif" font-size="{FS_MSG}" fill="{TEXT}">{label}</text>')
    return svg

def alt_box(y1, y2, label):
    return (
        f'<rect x="10" y="{y1}" width="{SVG_W-20}" height="{y2-y1}" '
        f'fill="none" stroke="{BORDER}" stroke-width="0.8" stroke-dasharray="4,2"/>'
        f'<rect x="10" y="{y1}" width="45" height="15" fill="{HDR_BG}"/>'
        f'<text x="15" y="{y1+11}" font-family="Arial,sans-serif" font-size="9" '
        f'fill="{TEXT}">{label}</text>'
    )

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

parts.append(activation(CX["Browser"],       90, 530))
parts.append(activation(CX["Express /auth"], 130, 490))
parts.append(activation(CX["MySQL DB"],      165, 430))

steps = [
    (CX["Patient"],        CX["Browser"],       100, "Enter email & password",       False),
    (CX["Browser"],        CX["Express /auth"], 135, "POST /auth/login",             False),
    (CX["Express /auth"],  CX["MySQL DB"],      170, "SELECT * FROM webuser WHERE email=?", False),
    (CX["MySQL DB"],       CX["Express /auth"], 210, "usertype row",                 True),
    (CX["Express /auth"],  CX["MySQL DB"],      250, "SELECT * FROM patient WHERE pemail=?", False),
    (CX["MySQL DB"],       CX["Express /auth"], 285, "patient row (hashed password)", True),
    # alt block start ~310
    (CX["Express /auth"],  CX["Express /auth"], 330, "bcrypt.compare(password, hash)", False),
    # success path
    (CX["Express /auth"],  CX["Browser"],       385, "302 redirect /dashboard + Set-Cookie", True),
    (CX["Browser"],        CX["Patient"],       420, "Dashboard page loaded",        True),
    # alt failure
    (CX["Express /auth"],  CX["Browser"],       470, "alert('Wrong password') + redirect /login", True),
]

# alt frame for the bcrypt decision
parts.append(alt_box(305, 490, "alt"))
parts.append(
    f'<text x="15" y="400" font-family="Arial,sans-serif" font-size="9" '
    f'fill="#666">[password match]</text>'
)
parts.append(
    f'<line x1="10" y1="445" x2="{SVG_W-10}" y2="445" '
    f'stroke="{BORDER}" stroke-width="0.6" stroke-dasharray="4,2"/>'
)
parts.append(
    f'<text x="15" y="459" font-family="Arial,sans-serif" font-size="9" '
    f'fill="#666">[password mismatch]</text>'
)

for x1, x2, y, label, dashed in steps:
    if x1 == x2:
        # self-message (loop arrow)
        parts.append(
            f'<path d="M {x1+5} {y} Q {x1+40} {y} {x1+40} {y+18} Q {x1+40} {y+35} {x1+5} {y+35}" '
            f'fill="none" stroke="{ARROW}" stroke-width="1.2" marker-end="url(#arr)"/>'
        )
        w = len(label)*5.1+10
        parts.append(
            f'<rect x="{x1+42}" y="{y+9}" width="{w:.0f}" height="14" fill="white"/>'
            f'<text x="{x1+47}" y="{y+19}" font-family="Arial,sans-serif" '
            f'font-size="{FS_MSG}" fill="{TEXT}">{label}</text>'
        )
    else:
        parts.append(msg(x1, x2, y, label, dashed))

parts.append('</svg>')

out_svg = 'diagram8_sequence_login.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram8_sequence_login.png',
                     output_width=SVG_W*2, output_height=SVG_H*2)
    print("Saved: diagram8_sequence_login.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(f'inkscape "{out_svg}" --export-filename="diagram8_sequence_login.png" --export-dpi=180 2>nul')
    if rc == 0:
        print("Saved: diagram8_sequence_login.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
