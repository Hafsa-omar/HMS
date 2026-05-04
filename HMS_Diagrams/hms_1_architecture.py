#!/usr/bin/env python3
"""
HMS System Architecture Diagram
4-tier layout: Users | Frontend | Backend | Database
Canvas: 860 x 520 pt
"""
import os

SVG_W, SVG_H = 860, 520

LAVEN   = "#e8e8f5"
NODE_BG = "#f5f5fc"
HDR_BG  = "#d0d0ea"
BORDER  = "#c0c0dc"
NODE_BD = "#9595c0"
TEXT    = "#1a1a2e"
ARROW   = "#1a1a2e"

NODE_HDR = 40
COMP_H   = 34
FS_COMP  = 10.5
FS_NODE  = 11.5
FS_ST    = 9.5
COMP_OFF = 72


def node_box(x, y, w, h, title, stereo):
    svg  = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'rx="6" ry="6" fill="{NODE_BG}" stroke="{NODE_BD}" stroke-width="1.4"/>')
    svg += (f'<rect x="{x}" y="{y}" width="{w}" height="{NODE_HDR}" '
            f'rx="6" ry="6" fill="{HDR_BG}"/>')
    svg += (f'<rect x="{x}" y="{y+NODE_HDR-5}" width="{w}" height="5" fill="{HDR_BG}"/>')
    svg += (f'<text x="{x+w//2}" y="{y+12}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="{FS_ST}" font-style="italic" '
            f'fill="{TEXT}">{stereo}</text>')
    svg += (f'<text x="{x+w//2}" y="{y+28}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="{FS_NODE}" font-weight="bold" '
            f'fill="{TEXT}">{title}</text>')
    return svg


def comp_box(cx, cy, w, label):
    x, y = cx - w // 2, cy - COMP_H // 2
    svg  = (f'<rect x="{x}" y="{y}" width="{w}" height="{COMP_H}" '
            f'rx="5" ry="5" fill="{LAVEN}" stroke="{BORDER}" stroke-width="1.0"/>')
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="{FS_COMP}" fill="{TEXT}">{label}</text>')
    return svg


def conn_line(x1, y1, x2, y2, bidir=True):
    ms = ' marker-start="url(#arr_rev)"' if bidir else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{ARROW}" stroke-width="1.6"{ms} marker-end="url(#arr_fwd)"/>')


def conn_label(x1, y1, x2, y2, label):
    mx = (x1 + x2) // 2
    my = (y1 + y2) // 2 - 9
    w  = len(label) * 5.3 + 10
    return (
        f'<rect x="{mx - w/2:.0f}" y="{my-9}" width="{w:.0f}" height="15" fill="white"/>'
        f'<text x="{mx}" y="{my}" text-anchor="middle" dominant-baseline="central" '
        f'font-family="Arial,sans-serif" font-size="9.5" fill="{TEXT}">{label}</text>'
    )


# ── Node geometry ─────────────────────────────────────────────────────────────
UX, UY, UW, UH = 14,  70, 148, 215   # Users
FX, FY, FW, FH = 182, 42, 195, 385   # Frontend
BX, BY, BW, BH = 397, 42, 270, 435   # Backend
DX, DY, DW, DH = 687, 70, 162, 280   # Database

U_CX = UX + UW // 2
F_CX = FX + FW // 2
B_CX = BX + BW // 2
D_CX = DX + DW // 2

def comp_y(node_top, idx, spacing=48):
    return node_top + COMP_OFF + idx * spacing

CONN_UF = UY + 90
CONN_FB = FY + 110
CONN_BD = DY + 95

# ── SVG ───────────────────────────────────────────────────────────────────────
TIER_TOP, TIER_BOT = 28, SVG_H - 28

parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'''<defs>
  <marker id="arr_fwd" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
    <polygon points="0 0,8 3,0 6" fill="{ARROW}"/>
  </marker>
  <marker id="arr_rev" markerWidth="8" markerHeight="6" refX="1" refY="3" orient="auto">
    <polygon points="8 0,0 3,8 6" fill="{ARROW}"/>
  </marker>
</defs>''',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" '
    f'fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
]

# Tier background bands
for bx, bw, tier_label in [(5,  172, "Users Tier"),
                             (177, 210, "Frontend Tier"),
                             (392, 285, "Backend Tier"),
                             (677, 178, "Database Tier")]:
    parts.append(
        f'<rect x="{bx}" y="{TIER_TOP}" width="{bw}" height="{TIER_BOT-TIER_TOP}" '
        f'rx="5" fill="#f7f7fd" stroke="{BORDER}" stroke-width="0.7" stroke-dasharray="5,3"/>'
    )
    parts.append(
        f'<text x="{bx + bw//2}" y="{TIER_BOT - 8}" text-anchor="middle" '
        f'font-family="Arial,sans-serif" font-size="9.5" font-style="italic" '
        f'fill="#8080a0">{tier_label}</text>'
    )

# Connection lines
parts.append(conn_line(UX + UW, CONN_UF, FX, CONN_UF, bidir=False))
parts.append(conn_line(FX + FW, CONN_FB, BX, CONN_FB, bidir=True))
parts.append(conn_line(BX + BW, CONN_BD, DX, CONN_BD, bidir=True))

# Node containers
parts.append(node_box(UX, UY, UW, UH, "Users",     "«actors»"))
parts.append(node_box(FX, FY, FW, FH, "Frontend",  "«browser»"))
parts.append(node_box(BX, BY, BW, BH, "Backend",   "«server»"))
parts.append(node_box(DX, DY, DW, DH, "Database",  "«storage»"))

# Users
for i, lbl in enumerate(["Patient", "Doctor", "Admin"]):
    parts.append(comp_box(U_CX, comp_y(UY, i, 50), 118, lbl))

# Frontend
for i, lbl in enumerate(["Dashboard / Book",
                          "Health Record",
                          "Doctor Panel",
                          "Admin Panel",
                          "AI Chatbot UI"]):
    parts.append(comp_box(F_CX, comp_y(FY, i, 58), 162, lbl))

# Backend
for i, lbl in enumerate(["Express.js Router",
                          "Auth Routes  (/auth/)",
                          "Patient Routes  (/api/)",
                          "Doctor Routes  (/api/doctor/)",
                          "Admin Routes  (/api/admin/)",
                          "Rule-based Chatbot",
                          "multer  File Handler",
                          "Session  (express-session)"]):
    parts.append(comp_box(B_CX, comp_y(BY, i, 48), 230, lbl))

# Database
for i, lbl in enumerate(["MySQL 8.0  :3306",
                          "HMS Database",
                          "uploads/  folder",
                          "Patient Documents"]):
    parts.append(comp_box(D_CX, comp_y(DY, i, 52), 135, lbl))

# Connection labels
parts.append(conn_label(UX + UW, CONN_UF, FX, CONN_UF, "HTTP"))
parts.append(conn_label(FX + FW, CONN_FB, BX, CONN_FB, "REST API"))
parts.append(conn_label(BX + BW, CONN_BD, DX, CONN_BD, "MySQL  :3306"))

parts.append('</svg>')

out_svg = 'diagram1_architecture.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram1_architecture.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram1_architecture.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram1_architecture.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram1_architecture.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
