import graphviz

dot = graphviz.Digraph("DFD", filename="diagram6_dfd", format="png")
dot.attr(rankdir="LR", bgcolor="white", fontsize="12", pad="0.5")

# External entities (rectangles)
dot.attr("node", shape="box", style="filled", fillcolor="#D6EAF8", fontsize="12", width="1.5")
dot.node("P", "Patient")
dot.node("D", "Doctor")
dot.node("A", "Admin")

# Processes (circles)
dot.attr("node", shape="ellipse", style="filled", fillcolor="#D5F5E3", fontsize="11", width="2")
dot.node("P1", "1.0\nAuthentication")
dot.node("P2", "2.0\nAppointment\nManagement")
dot.node("P3", "3.0\nLab Result\nManagement")
dot.node("P4", "4.0\nHealth Record\nManagement")
dot.node("P5", "5.0\nAI Chatbot")
dot.node("P6", "6.0\nAdmin\nManagement")

# Data stores (open rectangles)
dot.attr("node", shape="none", fontsize="11")
dot.node("DS1", label='''<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" BGCOLOR="#FAD7A0">
    <TR><TD WIDTH="20"><B>D1</B></TD><TD> patient / doctor / admin </TD></TR></TABLE>>''')
dot.node("DS2", label='''<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" BGCOLOR="#FAD7A0">
    <TR><TD WIDTH="20"><B>D2</B></TD><TD> appointment </TD></TR></TABLE>>''')
dot.node("DS3", label='''<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" BGCOLOR="#FAD7A0">
    <TR><TD WIDTH="20"><B>D3</B></TD><TD> lab_result </TD></TR></TABLE>>''')
dot.node("DS4", label='''<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" BGCOLOR="#FAD7A0">
    <TR><TD WIDTH="20"><B>D4</B></TD><TD> patient_health_info\n patient_documents </TD></TR></TABLE>>''')

# Flows
dot.edge("P",  "P1", label="credentials")
dot.edge("D",  "P1", label="credentials")
dot.edge("A",  "P1", label="credentials")
dot.edge("P1", "DS1", label="read/write")

dot.edge("P",  "P2", label="book / cancel")
dot.edge("D",  "P2", label="update status")
dot.edge("P2", "DS2", label="read/write")
dot.edge("DS2","P",   label="appointment list")
dot.edge("DS2","D",   label="patient schedule")

dot.edge("D",  "P3", label="add result")
dot.edge("P3", "DS3", label="write result")
dot.edge("DS3","P",   label="view results")

dot.edge("P",  "P4", label="upload / update\nhealth info")
dot.edge("P4", "DS4", label="read/write")
dot.edge("DS4","P",   label="health record")

dot.edge("P",  "P5", label="chat message")
dot.edge("P5", "DS2", label="query appointments", style="dashed")
dot.edge("P5", "DS3", label="query results",      style="dashed")
dot.edge("P5", "P",   label="AI reply")

dot.edge("A",  "P6", label="manage system")
dot.edge("P6", "DS1", label="read/write doctors\n& patients")

dot.render(cleanup=True)
print("✅ DFD saved: diagram6_dfd.png")