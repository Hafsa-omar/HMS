#!/usr/bin/env python3
"""
HMS Entity-Relationship Diagram
Pure SVG — same colour palette as all other HMS diagrams
Canvas: 980 x 760 pt
"""
import os

SVG_W, SVG_H = 980, 760

LAVEN   = "#e8e8f5"
NODE_BG = "#f5f5fc"
HDR_BG  = "#d0d0ea"
BORDER  = "#c0c0dc"
NODE_BD = "#9595c0"
TEXT    = "#1a1a2e"
ARROW   = "#1a1a2e"

TW   = 195    # table width
RH   = 17     # row height
PAD  = 4      # top/bottom padding inside section
HDR  = 28     # header height
FS_H = 11     # header font size
FS_R = 9.5    # row font size


def tbl_height(fields):
    return HDR + len(fields) * RH + PAD * 2


def table(x, y, name, fields):
    h   = tbl_height(fields)
    cx  = x + TW // 2
    out = []
    out.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{h}" '
               f'rx="5" ry="5" fill="{NODE_BG}" stroke="{NODE_BD}" stroke-width="1.3"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{HDR}" '
               f'rx="5" ry="5" fill="{HDR_BG}"/>')
    out.append(f'<rect x="{x}" y="{y+HDR-4}" width="{TW}" height="4" fill="{HDR_BG}"/>')
    out.append(f'<text x="{cx}" y="{y+HDR//2+1}" text-anchor="middle" '
               f'dominant-baseline="central" font-family="Arial,sans-serif" '
               f'font-size="{FS_H}" font-weight="bold" fill="{TEXT}">{name}</text>')
    for i, (prefix, field) in enumerate(fields):
        ry = y + HDR + PAD + i * RH + RH // 2
        colour = "#5050a0" if prefix == "PK" else ("#7070b0" if prefix == "FK" else TEXT)
        tag = "PK " if prefix == "PK" else ("FK " if prefix == "FK" else "     ")
        out.append(f'<text x="{x+7}" y="{ry}" dominant-baseline="central" '
                   f'font-family="Arial,sans-serif" font-size="{FS_R}" fill="{colour}">'
                   f'{tag}{field}</text>')
        if i < len(fields) - 1:
            gy = y + HDR + PAD + (i + 1) * RH
            out.append(f'<line x1="{x+1}" y1="{gy}" x2="{x+TW-1}" y2="{gy}" '
                       f'stroke="{BORDER}" stroke-width="0.5"/>')
    return '\n'.join(out), h


def rel_line(x1, y1, x2, y2, label="", dashed=False):
    dash = ' stroke-dasharray="5,3"' if dashed else ''
    out  = (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{ARROW}" stroke-width="1.1"{dash}/>')
    if label:
        mx, my = (x1+x2)//2, (y1+y2)//2 - 8
        w = len(label)*4.8 + 8
        out += (f'<rect x="{mx-w/2:.0f}" y="{my-7}" width="{w:.0f}" height="13" fill="white"/>'
                f'<text x="{mx}" y="{my}" text-anchor="middle" dominant-baseline="central" '
                f'font-family="Arial,sans-serif" font-size="9" fill="{TEXT}">{label}</text>')
    return out


# ── Table positions ───────────────────────────────────────────────────────────
#  Col 1 x=20  Col 2 x=240  Col 3 x=460  Col 4 x=685  Col 5 x=770 (not used)
C1, C2, C3, C4 = 20, 235, 455, 730

TABLES = {
    "patient": (C1, 25, "patient", [
        ("PK", "pid"),
        ("", "pname"),
        ("", "pemail"),
        ("", "ppassword"),
        ("", "pnic"),
        ("", "pdob"),
        ("", "ptel"),
        ("", "paddress"),
    ]),
    "doctor": (C2, 25, "doctor", [
        ("PK", "docid"),
        ("", "docname"),
        ("", "docemail"),
        ("", "docpassword"),
        ("FK", "specialties"),
        ("", "country"),
        ("", "city"),
        ("", "available"),
        ("", "consultation_fee"),
        ("", "rating"),
    ]),
    "specialties": (C3, 25, "specialties", [
        ("PK", "id"),
        ("", "sname"),
    ]),
    "webuser": (C4, 25, "webuser", [
        ("PK", "email"),
        ("", "usertype  (p / d / a)"),
    ]),
    "admin": (C4, 135, "admin", [
        ("PK", "aid"),
        ("", "aname"),
        ("", "aemail"),
        ("", "apassword"),
    ]),
    "appointment": (C1, 310, "appointment", [
        ("PK", "appoid"),
        ("FK", "pid"),
        ("FK", "scheduleid  (docid)"),
        ("", "appodate"),
        ("", "status"),
        ("", "apponum"),
    ]),
    "lab_result": (C2, 310, "lab_result", [
        ("PK", "id"),
        ("FK", "pid"),
        ("FK", "docid"),
        ("", "test_name"),
        ("", "result"),
        ("", "notes"),
        ("", "created_at"),
    ]),
    "patient_health_info": (C1, 560, "patient_health_info", [
        ("PK", "id"),
        ("FK", "pid  (UNIQUE)"),
        ("", "blood_type"),
        ("", "allergies"),
        ("", "chronic_conditions"),
        ("", "current_medications"),
        ("", "emergency_contact"),
    ]),
    "patient_documents": (C2, 560, "patient_documents", [
        ("PK", "id"),
        ("FK", "pid"),
        ("", "original_name"),
        ("", "stored_name"),
        ("", "file_type"),
        ("", "uploaded_at"),
    ]),
}

# ── Build SVG ─────────────────────────────────────────────────────────────────
parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" '
    f'fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
]

# Compute box info
INFO = {}
for key, (x, y, name, fields) in TABLES.items():
    h = tbl_height(fields)
    INFO[key] = {
        'x': x, 'y': y, 'h': h,
        'cx':    x + TW // 2,
        'top':   y,
        'bot':   y + h,
        'mid_y': y + h // 2,
        'left':  x,
        'right': x + TW,
    }


def cx(k):    return INFO[k]['cx']
def top(k):   return INFO[k]['top']
def bot(k):   return INFO[k]['bot']
def mid(k):   return INFO[k]['mid_y']
def lx(k):    return INFO[k]['left']
def rx(k):    return INFO[k]['right']


# ── Relationship lines (drawn before tables) ──────────────────────────────────

# patient 1 ── N appointment  (vertical, col 1)
parts.append(rel_line(cx("patient"), bot("patient"), cx("appointment"), top("appointment"),
                      "1 books N"))

# doctor 1 ── N appointment  (diagonal/L from doctor down-left to appointment right)
mid_y_appo = mid("appointment")
parts.append(rel_line(cx("doctor"), bot("doctor"),
                      cx("doctor"), mid_y_appo))
parts.append(rel_line(cx("doctor"), mid_y_appo,
                      rx("appointment"), mid_y_appo, "1 handles N"))

# doctor N ── 1 specialties (horizontal)
parts.append(rel_line(rx("doctor"), mid("doctor"),
                      lx("specialties"), mid("doctor"), "N has 1"))

# patient ── lab_result (L-shaped)
mid_yr = INFO["lab_result"]["y"] - 15
parts.append(rel_line(cx("patient"), bot("patient"),
                      cx("patient"), mid_yr))
parts.append(rel_line(cx("patient"), mid_yr,
                      lx("lab_result"), mid_yr, "1 has N"))
parts.append(rel_line(lx("lab_result"), mid_yr,
                      lx("lab_result"), top("lab_result")))

# doctor 1 ── N lab_result (vertical col 2)
parts.append(rel_line(cx("doctor"), bot("doctor"), cx("lab_result"), top("lab_result"),
                      "1 adds N"))

# patient 1 ── 1 patient_health_info (vertical col 1)
parts.append(rel_line(cx("patient_health_info") - 12, bot("appointment"),
                      cx("patient_health_info") - 12, top("patient_health_info"), "1 has 1"))

# patient 1 ── N patient_documents (vertical col 2)
parts.append(rel_line(cx("patient_documents"), bot("lab_result"),
                      cx("patient_documents"), top("patient_documents"), "1 uploads N"))

# patient registered as webuser (dashed, L-path)
parts.append(rel_line(rx("patient"), mid("patient"),
                      lx("webuser"), mid("patient"), "registered as", dashed=True))
# Extend to webuser y
parts.append(rel_line(lx("webuser"), mid("patient"),
                      lx("webuser"), top("webuser"), dashed=True))

# doctor registered as webuser
parts.append(rel_line(rx("doctor"), mid("doctor"),
                      lx("webuser") + 10, mid("doctor"), "", dashed=True))
parts.append(rel_line(lx("webuser") + 10, mid("doctor"),
                      lx("webuser") + 10, top("webuser"), "", dashed=True))

# admin registered as webuser (vertical)
parts.append(rel_line(cx("admin"), top("admin"),
                      cx("admin"), bot("webuser"), "registered as", dashed=True))

# ── Table boxes (drawn on top of lines) ──────────────────────────────────────
for key, (x, y, name, fields) in TABLES.items():
    svg, _ = table(x, y, name, fields)
    parts.append(svg)

parts.append('</svg>')

out_svg = 'diagram2_er.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram2_er.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram2_er.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram2_er.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram2_er.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
