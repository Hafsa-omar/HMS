import graphviz

dot = graphviz.Digraph("Use_Case", filename="diagram3_usecase", format="png")
dot.attr(rankdir="LR", bgcolor="white", fontsize="12", pad="0.6")

# Actors
dot.attr("node", shape="plaintext", fontsize="13")
dot.node("Patient", label='''<<TABLE BORDER="0"><TR><TD>🧑</TD></TR><TR><TD><B>Patient</B></TD></TR></TABLE>>''')
dot.node("Doctor",  label='''<<TABLE BORDER="0"><TR><TD>👨‍⚕️</TD></TR><TR><TD><B>Doctor</B></TD></TR></TABLE>>''')
dot.node("Admin",   label='''<<TABLE BORDER="0"><TR><TD>🔧</TD></TR><TR><TD><B>Admin</B></TD></TR></TABLE>>''')

# Use cases - ellipses
dot.attr("node", shape="ellipse", style="filled", fillcolor="#D6EAF8", fontsize="11", width="2.2")

patient_cases = ["Register / Login", "View Dashboard", "Book Appointment",
                 "View My Bookings", "Cancel Appointment", "View Lab Results",
                 "View Health Record", "Upload Document", "Update Profile",
                 "Chat with AI Bot"]

doctor_cases  = ["Doctor Login", "View Appointments", "View My Patients",
                 "Add Lab Result", "Update Profile"]

admin_cases   = ["Admin Login", "Manage Doctors", "Manage Patients",
                 "View All Appointments", "View System Stats"]

for uc in patient_cases: dot.node(uc, fillcolor="#D6EAF8")
for uc in doctor_cases:  dot.node(uc, fillcolor="#D5F5E3")
for uc in admin_cases:   dot.node(uc, fillcolor="#FAD7A0")

# System boundary
with dot.subgraph(name="cluster_system") as s:
    s.attr(label="Hospital Management System", style="rounded", bgcolor="#F8F9FA", fontsize="14", penwidth="2")
    for uc in patient_cases + doctor_cases + admin_cases:
        s.node(uc)

# Edges
dot.attr("edge", arrowhead="none")
for uc in patient_cases: dot.edge("Patient", uc, color="#2E86C1")
for uc in doctor_cases:  dot.edge("Doctor",  uc, color="#117A65")
for uc in admin_cases:   dot.edge("Admin",   uc, color="#E67E22")

dot.render(cleanup=True)
print("✅ Use Case Diagram saved: diagram3_usecase.png")