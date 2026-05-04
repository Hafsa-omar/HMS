#!/usr/bin/env python3
"""
HMS Use Case Diagram
Pure SVG — same colour palette as all other HMS diagrams
Canvas: 900 x 680 pt
"""
import os

SVG_W, SVG_H = 900, 680

LAVEN   = "#e8e8f5"
NODE_BG = "#f5f5fc"
HDR_BG  = "#d0d0ea"
BORDER  = "#c0c0dc"
NODE_BD = "#9595c0"
TEXT    = "#1a1a2e"
ARROW   = "#1a1a2e"

UC_W, UC_H, UC_R = 185, 34, 17   # use-case rounded rect
ACT_W, ACT_H     = 70,  28       # actor box
FS_UC  = 10
FS_ACT = 11
FS_HDR = 12


def actor_box(cx, cy, label):
    x, y = cx - ACT_W // 2, cy - ACT_H // 2
    svg  = (f'<rect x="{x}" y="{y}" width="{ACT_W}" height="{ACT_H}" '
            f'rx="6" fill="{HDR_BG}" stroke="{NODE_BD}" stroke-width="1.2"/>')
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="{FS_ACT}" font-weight="bold" '
            f'fill="{TEXT}">{label}</text>')
    return svg


def usecase(cx, cy, label, fill=None):
    f = fill or LAVEN
    x, y = cx - UC_W // 2, cy - UC_H // 2
    svg  = (f'<rect x="{x}" y="{y}" width="{UC_W}" height="{UC_H}" '
            f'rx="{UC_R}" fill="{f}" stroke="{BORDER}" stroke-width="1.0"/>')
    svg += (f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="{FS_UC}" fill="{TEXT}">{label}</text>')
    return svg


def conn(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{ARROW}" stroke-width="1.0"/>')


# ── Layout ────────────────────────────────────────────────────────────────────
# Left: actors stacked vertically
# Right: system boundary box with use cases in 3 role-coloured groups

ACTOR_X  = 68   # actor centre x
SYS_X    = 138  # system boundary left edge
SYS_W    = 748
SYS_Y    = 28
SYS_H    = SVG_H - 40

UC_COL1  = 260  # patient use cases centre x
UC_COL2  = 510  # doctor use cases centre x
UC_COL3  = 760  # admin use cases centre x

PAT_FILL = "#e8e8f5"   # LAVEN
DOC_FILL = "#e8f5ea"   # light green
ADM_FILL = "#f5f0e8"   # light amber

patient_cases = [
    "Register / Login",
    "View Dashboard",
    "Book Appointment",
    "View My Bookings",
    "Cancel Appointment",
    "View Lab Results",
    "View Health Record",
    "Upload Document",
    "Update Profile",
    "Chat with AI Bot",
]

doctor_cases = [
    "Doctor Login",
    "View Appointments",
    "View My Patients",
    "Add Lab Result",
    "Update Profile",
]

admin_cases = [
    "Admin Login",
    "Manage Doctors",
    "Manage Patients",
    "View All Appointments",
    "View System Stats",
]

UC_GAP = 46   # vertical spacing between use cases

def uc_positions(cases, cx, y_start):
    return [(cx, y_start + i * UC_GAP) for i in range(len(cases))]

PAT_Y0  = 68
DOC_Y0  = 68
ADM_Y0  = 68

pat_pos = uc_positions(patient_cases, UC_COL1, PAT_Y0)
doc_pos = uc_positions(doctor_cases,  UC_COL2, DOC_Y0)
adm_pos = uc_positions(admin_cases,   UC_COL3, ADM_Y0)

# Actor y positions: centre of their role's use-case block
def mid_y(positions):
    return (positions[0][1] + positions[-1][1]) // 2

ACT_PAT_Y = mid_y(pat_pos)
ACT_DOC_Y = mid_y(doc_pos)
ACT_ADM_Y = mid_y(adm_pos)

# ── SVG scaffold ──────────────────────────────────────────────────────────────
parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" '
    f'fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
]

# System boundary
parts.append(
    f'<rect x="{SYS_X}" y="{SYS_Y}" width="{SYS_W}" height="{SYS_H}" '
    f'rx="8" fill="{NODE_BG}" stroke="{NODE_BD}" stroke-width="1.6"/>'
)
parts.append(
    f'<text x="{SYS_X + SYS_W//2}" y="{SYS_Y + SYS_H - 10}" '
    f'text-anchor="middle" font-family="Arial,sans-serif" font-size="{FS_HDR}" '
    f'font-style="italic" fill="#8080a0">Hospital Management System</text>'
)

# Column group headers inside boundary
for col_x, col_label, fill in [
        (UC_COL1, "Patient", PAT_FILL),
        (UC_COL2, "Doctor",  DOC_FILL),
        (UC_COL3, "Admin",   ADM_FILL)]:
    parts.append(
        f'<rect x="{col_x - UC_W//2 - 6}" y="{SYS_Y + 6}" '
        f'width="{UC_W + 12}" height="{SYS_H - 22}" '
        f'rx="6" fill="{fill}" stroke="{BORDER}" stroke-width="0.6" '
        f'fill-opacity="0.45"/>'
    )
    parts.append(
        f'<text x="{col_x}" y="{SYS_Y + 18}" text-anchor="middle" '
        f'font-family="Arial,sans-serif" font-size="10" font-weight="bold" '
        f'fill="{TEXT}">{col_label} Use Cases</text>'
    )

# Connection lines (actor → each use case)
for (cx_uc, cy_uc) in pat_pos:
    parts.append(conn(ACTOR_X + ACT_W//2, ACT_PAT_Y, cx_uc - UC_W//2, cy_uc))
for (cx_uc, cy_uc) in doc_pos:
    parts.append(conn(ACTOR_X + ACT_W//2, ACT_DOC_Y, cx_uc - UC_W//2, cy_uc))
for (cx_uc, cy_uc) in adm_pos:
    parts.append(conn(ACTOR_X + ACT_W//2, ACT_ADM_Y, cx_uc - UC_W//2, cy_uc))

# Use case boxes
for (cx_uc, cy_uc), label in zip(pat_pos, patient_cases):
    parts.append(usecase(cx_uc, cy_uc, label, PAT_FILL))
for (cx_uc, cy_uc), label in zip(doc_pos, doctor_cases):
    parts.append(usecase(cx_uc, cy_uc, label, DOC_FILL))
for (cx_uc, cy_uc), label in zip(adm_pos, admin_cases):
    parts.append(usecase(cx_uc, cy_uc, label, ADM_FILL))

# Actor boxes (drawn last so they appear on top of connection lines)
parts.append(actor_box(ACTOR_X, ACT_PAT_Y, "Patient"))
parts.append(actor_box(ACTOR_X, ACT_DOC_Y, "Doctor"))
parts.append(actor_box(ACTOR_X, ACT_ADM_Y, "Admin"))

parts.append('</svg>')

out_svg = 'diagram3_usecase.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram3_usecase.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram3_usecase.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram3_usecase.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram3_usecase.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
