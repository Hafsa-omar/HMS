#!/usr/bin/env python3
"""
HMS Class Diagram — 7 classes, inheritance + associations
Canvas: 800 x 880 pt
"""
import os

SVG_W, SVG_H = 800, 880

LAVEN  = "#e8e8f5"
HDR_BG = "#d0d0ea"
BORDER = "#c0c0dc"
TEXT   = "#1a1a2e"
ARROW  = "#1a1a2e"

CW    = 158   # class box width
LH    = 15    # line height per attribute / method line
PY    = 5     # vertical padding inside each section
HDR_H = 25    # header section height
FS    = 10    # font size for attributes / methods
FNS   = 11.5  # font size for class name


def sh(n):
    """Height of an attribute or method section with n lines."""
    return n * LH + 2 * PY


def class_box(x, y, name, attrs, methods):
    ha  = sh(len(attrs))
    hm  = sh(len(methods))
    h   = HDR_H + ha + hm
    cx  = x + CW // 2
    out = []

    # Outer border (whole box)
    out.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{h}" '
               f'rx="4" ry="4" fill="{LAVEN}" stroke="{BORDER}" stroke-width="1.1"/>')

    # Header background
    out.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{HDR_H}" '
               f'rx="4" ry="4" fill="{HDR_BG}"/>')
    # Square off bottom corners of header fill
    out.append(f'<rect x="{x}" y="{y+HDR_H-4}" width="{CW}" height="4" fill="{HDR_BG}"/>')

    # Horizontal dividers
    out.append(f'<line x1="{x}" y1="{y+HDR_H}" x2="{x+CW}" y2="{y+HDR_H}" '
               f'stroke="{BORDER}" stroke-width="1.1"/>')
    out.append(f'<line x1="{x}" y1="{y+HDR_H+ha}" x2="{x+CW}" y2="{y+HDR_H+ha}" '
               f'stroke="{BORDER}" stroke-width="1.1"/>')

    # Class name (bold, centred in header)
    out.append(f'<text x="{cx}" y="{y + HDR_H//2 + 1}" text-anchor="middle" '
               f'dominant-baseline="central" font-family="Arial,sans-serif" '
               f'font-size="{FNS}" font-weight="bold" fill="{TEXT}">{name}</text>')

    # Attributes
    ay = y + HDR_H + PY + LH // 2 + 1
    for a in attrs:
        out.append(f'<text x="{x+6}" y="{ay}" dominant-baseline="central" '
                   f'font-family="Arial,sans-serif" font-size="{FS}" fill="{TEXT}">{a}</text>')
        ay += LH

    # Methods
    my = y + HDR_H + ha + PY + LH // 2 + 1
    for m in methods:
        out.append(f'<text x="{x+6}" y="{my}" dominant-baseline="central" '
                   f'font-family="Arial,sans-serif" font-size="{FS}" fill="{TEXT}">{m}</text>')
        my += LH

    return '\n'.join(out)


def mult(x, y, label):
    """Small multiplicity label."""
    return (f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Arial,sans-serif" font-size="9.5" fill="{TEXT}">{label}</text>')


# ── Class definitions ────────────────────────────────────────────────────────
CLASSES = [
    ('User', 321, 20,
     ['- userId : INT', '- name : VARCHAR', '- email : VARCHAR',
      '- password : VARCHAR', '- role : ENUM', '- phone : VARCHAR'],
     ['+ login()', '+ logout()', '+ register()']),

    ('Patient', 30, 260,
     ['- patientId : INT', '- dateOfBirth : DATE',
      '- bloodType : VARCHAR', '- country : VARCHAR'],
     ['+ bookAppointment()', '+ viewLabResults()', '+ updateProfile()']),

    ('Doctor', 321, 260,
     ['- doctorId : INT', '- specialty : VARCHAR',
      '- hospital : VARCHAR', '- fee : DECIMAL'],
     ['+ viewAppointments()', '+ addLabResult()', '+ viewPatients()']),

    ('Admin', 600, 260,
     ['- adminId : INT'],
     ['+ manageUsers()', '+ viewReports()']),

    ('Appointment', 175, 490,
     ['- appointmentId : INT', '- patientId : INT', '- doctorId : INT',
      '- date : DATE', '- status : ENUM', '- specialty : VARCHAR'],
     ['+ create()', '+ cancel()']),

    ('LabResult', 460, 490,
     ['- resultId : INT', '- patientId : INT', '- doctorId : INT',
      '- testName : VARCHAR', '- result : TEXT', '- date : DATE'],
     ['+ create()', '+ view()']),

    ('HealthRecord', 30, 705,
     ['- recordId : INT', '- patientId : INT',
      '- bloodType : VARCHAR', '- allergies : TEXT'],
     ['+ update()', '+ view()']),
]

# Pre-compute box heights and key coordinates
def box_height(attrs, methods):
    return HDR_H + sh(len(attrs)) + sh(len(methods))

INFO = {}
for (name, x, y, attrs, methods) in CLASSES:
    h = box_height(attrs, methods)
    INFO[name] = {
        'x': x, 'y': y, 'h': h,
        'cx':   x + CW // 2,
        'top':  y,
        'bot':  y + h,
        'mid_y': y + h // 2,
        'left':  x,
        'right': x + CW,
    }

# Shortcuts
def cx(n):    return INFO[n]['cx']
def top(n):   return INFO[n]['top']
def bot(n):   return INFO[n]['bot']
def mid_y(n): return INFO[n]['mid_y']
def lx(n):    return INFO[n]['left']
def rx(n):    return INFO[n]['right']

# ── SVG scaffold ─────────────────────────────────────────────────────────────
parts = [
    f'<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">',
    f'''<defs>
  <marker id="inh" markerWidth="14" markerHeight="10" refX="13" refY="5" orient="auto">
    <polygon points="1 1, 13 5, 1 9" fill="white" stroke="{ARROW}" stroke-width="1.2"/>
  </marker>
</defs>''',
    f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
    f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" '
    f'fill="none" stroke="{BORDER}" stroke-width="1.2"/>',
]

# ── Relationships (drawn first so class boxes appear on top) ─────────────────

Y_INH = 237   # y of horizontal bar linking children to User

# Inheritance: Patient → User (L-shaped via Y_INH)
parts.append(
    f'<path d="M {cx("Patient")} {top("Patient")} '
    f'L {cx("Patient")} {Y_INH} L {cx("User")} {Y_INH} L {cx("User")} {bot("User")}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.2" marker-end="url(#inh)"/>'
)

# Inheritance: Doctor → User (direct vertical)
parts.append(
    f'<path d="M {cx("Doctor")} {top("Doctor")} L {cx("Doctor")} {bot("User")}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.2" marker-end="url(#inh)"/>'
)

# Inheritance: Admin → User (L-shaped via Y_INH)
parts.append(
    f'<path d="M {cx("Admin")} {top("Admin")} '
    f'L {cx("Admin")} {Y_INH} L {cx("User")} {Y_INH} L {cx("User")} {bot("User")}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.2" marker-end="url(#inh)"/>'
)

# Association: Patient 1 --- * Appointment  (diagonal)
Y_ASSOC1 = 462
parts.append(
    f'<path d="M {cx("Patient")} {bot("Patient")} '
    f'L {cx("Patient")} {Y_ASSOC1} L {cx("Appointment")} {Y_ASSOC1} '
    f'L {cx("Appointment")} {top("Appointment")}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.1"/>'
)
parts.append(mult(cx("Patient") + 10, bot("Patient") + 12, "1"))
parts.append(mult(cx("Appointment") - 12, top("Appointment") - 10, "*"))

# Association: Doctor 1 --- * Appointment  (L-shaped)
Y_ASSOC2 = 472
parts.append(
    f'<path d="M {cx("Doctor")} {bot("Doctor")} '
    f'L {cx("Doctor")} {Y_ASSOC2} L {cx("Appointment")} {Y_ASSOC2} '
    f'L {cx("Appointment")} {top("Appointment")}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.1"/>'
)
parts.append(mult(cx("Doctor") - 12, bot("Doctor") + 12, "1"))
parts.append(mult(cx("Appointment") + 14, top("Appointment") - 10, "*"))

# Association: Appointment 1 --- * LabResult  (horizontal)
parts.append(
    f'<line x1="{rx("Appointment")}" y1="{mid_y("Appointment")}" '
    f'x2="{lx("LabResult")}" y2="{mid_y("LabResult")}" '
    f'stroke="{ARROW}" stroke-width="1.1"/>'
)
parts.append(mult(rx("Appointment") + 12, mid_y("Appointment") - 8, "1"))
parts.append(mult(lx("LabResult") - 12, mid_y("LabResult") - 8, "*"))

# Association: Doctor 1 --- * LabResult  (L-shaped via right side of Doctor)
parts.append(
    f'<path d="M {rx("Doctor")} {mid_y("Doctor")} '
    f'L {cx("LabResult")} {mid_y("Doctor")} '
    f'L {cx("LabResult")} {top("LabResult")}" '
    f'fill="none" stroke="{ARROW}" stroke-width="1.1"/>'
)
parts.append(mult(rx("Doctor") + 12, mid_y("Doctor") - 8, "1"))
parts.append(mult(cx("LabResult") + 14, top("LabResult") - 10, "*"))

# Association: Patient 1 --- 1 HealthRecord  (vertical, left of Appointment)
parts.append(
    f'<line x1="{cx("Patient")}" y1="{bot("Patient")}" '
    f'x2="{cx("Patient")}" y2="{top("HealthRecord")}" '
    f'stroke="{ARROW}" stroke-width="1.1"/>'
)
parts.append(mult(cx("Patient") - 14, bot("Patient") + 14, "1"))
parts.append(mult(cx("Patient") - 14, top("HealthRecord") - 10, "1"))

# ── Class boxes (on top of relationship lines) ───────────────────────────────
for (name, x, y, attrs, methods) in CLASSES:
    parts.append(class_box(x, y, name, attrs, methods))

parts.append('</svg>')

out_svg = 'diagram11_class.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f"Saved: {out_svg}")

converted = False
try:
    import cairosvg
    cairosvg.svg2png(url=os.path.abspath(out_svg),
                     write_to='diagram11_class.png',
                     output_width=SVG_W * 2, output_height=SVG_H * 2)
    print("Saved: diagram11_class.png  (via cairosvg)")
    converted = True
except Exception:
    pass

if not converted:
    rc = os.system(
        f'inkscape "{out_svg}" --export-filename="diagram11_class.png"'
        f' --export-dpi=180 2>nul'
    )
    if rc == 0:
        print("Saved: diagram11_class.png  (via Inkscape)")
        converted = True

if not converted:
    print("SVG saved — open in browser or insert into Word directly.")
