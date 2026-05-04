#!/usr/bin/env python3
"""
HMS Deployment Architecture Diagram
3-tier layout: Client | Application Server | Data Tier
Canvas: 820 x 510 pt
"""
import os

SVG_W, SVG_H = 820, 510

LAVEN   = "#e8e8f5"
NODE_BG = "#f5f5fc"
HDR_BG  = "#d0d0ea"
BORDER  = "#c0c0dc"
NODE_BD = "#9595c0"
TEXT    = "#1a1a2e"
ARROW   = "#1a1a2e"

NODE_HDR = 40    # node header height
COMP_H   = 34    # component box height
FS_COMP  = 10.5  # component font size
FS_NODE  = 11.5  # node title font size
FS_ST    = 9.5   # stereotype font size
COMP_OFF = 72    # offset from node top_y to first component centre


def node_box(x, y, w, h, title, stereo):
    """Node container with darker header."""
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
    """Component box (lavender, same style as all other diagrams)."""
    x, y = cx - w // 2, cy - COMP_H // 2
    svg  = (f'<rect x="{x}" y="{y}" width="{w}" height="{COMP_H}" '
            f'rx="5" ry="5" fill="{LAVEN}" stroke="{BORDER}" stroke-width="1.0"/>')
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="{FS_COMP}" fill="{TEXT}">{label}</text>')
    return svg


def conn_line(x1, y1, x2, y2, bidir=True):
    """Connection line, optionally bidirectional."""
    ms = ' marker-start="url(#arr_rev)"' if bidir else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{ARROW}" stroke-width="1.6"{ms} marker-end="url(#arr_fwd)"/>')


def conn_label(x1, y1, x2, y2, label):
    """Label (with white bg) placed above the midpoint of a connection line."""
    mx = (x1 + x2) // 2
    my = (y1 + y2) // 2 - 9
    w  = len(label) * 5.3 + 10
    return (
        f'<rect x="{mx - w/2:.0f}" y="{my-9}" width="{w:.0f}" height="15" fill="white"/>'
        f'<text x="{mx}" y="{my}" text-anchor="middle" dominant-baseline="central" '
        f'font-family="Arial,sans-serif" font-size="9.5" fill="{TEXT}">{label}</text>'
    )


# ── Node geometry ─────────────────────────────────────────────────────────────
BX, BY, BW, BH = 15,  75, 172, 215   # Client Browser
AX, AY, AW, AH = 215, 42, 335, 375   # Application Server
DX, DY, DW, DH = 585, 75, 210, 190   # Database Server
FX, FY, FW, FH = 585, 310, 210, 155  # File System

B_CX = BX + BW // 2   # 101
A_CX = AX + AW // 2   # 382
D_CX = DX + DW // 2   # 690
F_CX = FX + FW // 2   # 690

def comp_y(node_top, idx, spacing=48):
    return node_top + COMP_OFF + idx * spacing

# ── Connection y positions ────────────────────────────────────────────────────
CONN_BD = BY + 88    # Browser ↔ App Server
CONN_AD = DY + 75    # App Server ↔ DB Server
CONN_AF = FY + 55    # App Server → File System

# ── SVG ───────────────────────────────────────────────────────────────────────
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

# ── Tier background bands (dashed outlines) ───────────────────────────────────
TIER_TOP, TIER_BOT = 28, SVG_H - 28
for bx, bw, tier_label in [(5, 205, "Client Tier"),
                             (210, 370, "Application Tier"),
                             (580, 235, "Data Tier")]:
    parts.append(
        f'<rect x="{bx}" y="{TIER_TOP}" width="{bw}" height="{TIER_BOT-TIER_TOP}" '
        f'rx="5" fill="#f7f7fd" stroke="{BORDER}" stroke-width="0.7" stroke-dasharray="5,3"/>'
    )
    parts.append(
        f'<text x="{bx + bw//2}" y="{TIER_BOT - 8}" text-anchor="middle" '
        f'font-family="Arial,sans-serif" font-size="9.5" font-style="italic" '
        f'fill="#8080a0">{tier_label}</text>'
    )

# ── Connection lines (drawn before nodes) ─────────────────────────────────────
parts.append(conn_line(BX + BW, CONN_BD, AX, CONN_BD, bidir=True))
parts.append(conn_line(AX + AW, CONN_AD, DX, CONN_AD, bidir=True))
parts.append(conn_line(AX + AW, CONN_AF, FX, CONN_AF, bidir=False))

# ── Node containers ───────────────────────────────────────────────────────────
parts.append(node_box(BX, BY, BW, BH, "Client Browser",       "«device»"))
parts.append(node_box(AX, AY, AW, AH, "Application Server",   "«server»"))
parts.append(node_box(DX, DY, DW, DH, "Database Server",      "«server»"))
parts.append(node_box(FX, FY, FW, FH, "File System",          "«storage»"))

# ── Components: Client Browser ────────────────────────────────────────────────
for i, lbl in enumerate(["Web Browser",
                          "HTML / CSS / JS",
                          "Session Cookie"]):
    parts.append(comp_box(B_CX, comp_y(BY, i, 47), 140, lbl))

# ── Components: Application Server ───────────────────────────────────────────
for i, lbl in enumerate(["Express.js Framework",
                          "Session Manager (express-session)",
                          "bcrypt Authentication",
                          "REST API  (/api/  /auth/)",
                          "multer  File Handler",
                          "Rule-based Chatbot"]):
    parts.append(comp_box(A_CX, comp_y(AY, i, 50), 260, lbl))

# ── Components: Database Server ───────────────────────────────────────────────
for i, lbl in enumerate(["MySQL 8.0",
                          "HMS Database",
                          "Port  :3306"]):
    parts.append(comp_box(D_CX, comp_y(DY, i, 44), 170, lbl))

# ── Components: File System ───────────────────────────────────────────────────
for i, lbl in enumerate(["uploads/  folder",
                          "Patient Documents"]):
    parts.append(comp_box(F_CX, comp_y(FY, i, 50), 170, lbl))

# ── Connection labels (drawn last — on top of nodes) ─────────────────────────
parts.append(conn_label(BX + BW, CONN_BD, AX, CONN_BD, "HTTP/HTTPS  :3000"))
parts.append(conn_label(AX + AW, CONN_AD, DX, CONN_AD, "MySQL Protocol  :3306"))
parts.append(conn_label(AX + AW, CONN_AF, FX, CONN_AF, "Local File  I/O"))

parts.append('</svg>')

out_svg = 'diagram13_deployment.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram13_deployment.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram13_deployment.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram13_deployment.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram13_deployment.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
