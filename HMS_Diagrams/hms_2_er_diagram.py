import graphviz

dot = graphviz.Digraph("ER_Diagram", filename="diagram2_er", format="png")
dot.attr(rankdir="LR", fontsize="12", bgcolor="white", pad="0.5")
dot.attr("node", shape="plaintext")

def table(name, fields):
    label = f'''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" BGCOLOR="#E8F4FD">
    <TR><TD BGCOLOR="#2E86C1" ALIGN="CENTER"><FONT COLOR="white"><B>{name}</B></FONT></TD></TR>'''
    for f in fields:
        pk = "🔑 " if f.startswith("PK") else ("FK " if f.startswith("FK") else "• ")
        label += f'<TR><TD ALIGN="LEFT">{pk}{f.replace("PK ","").replace("FK ","")}</TD></TR>'
    label += "</TABLE>>"
    return label

dot.node("patient",          table("patient",          ["PK pid", "pname", "pemail", "ppassword", "pnic", "pdob", "ptel", "paddress"]))
dot.node("doctor",           table("doctor",           ["PK docid", "docname", "docemail", "docpassword", "FK specialties", "country", "city", "available", "consultation_fee", "rating"]))
dot.node("specialties",      table("specialties",      ["PK id", "sname"]))
dot.node("appointment",      table("appointment",      ["PK appoid", "FK pid", "FK scheduleid(docid)", "appodate", "status", "apponum"]))
dot.node("lab_result",       table("lab_result",       ["PK id", "FK pid", "FK docid", "test_name", "result", "notes", "created_at"]))
dot.node("webuser",          table("webuser",          ["PK email", "usertype (p/d/a)"]))
dot.node("admin",            table("admin",            ["PK aid", "aname", "aemail", "apassword"]))
dot.node("patient_health_info", table("patient_health_info", ["PK id", "FK pid (UNIQUE)", "blood_type", "allergies", "chronic_conditions", "current_medications", "emergency_contact"]))
dot.node("patient_documents",   table("patient_documents",   ["PK id", "FK pid", "original_name", "stored_name", "file_type", "uploaded_at"]))

dot.edge("patient",     "appointment",         label="1 books N", color="#2E86C1")
dot.edge("doctor",      "appointment",         label="1 handles N", color="#117A65")
dot.edge("doctor",      "specialties",         label="N has 1", color="#117A65")
dot.edge("patient",     "lab_result",          label="1 has N", color="#2E86C1")
dot.edge("doctor",      "lab_result",          label="1 adds N", color="#117A65")
dot.edge("patient",     "patient_health_info", label="1 has 1", color="#7D3C98")
dot.edge("patient",     "patient_documents",   label="1 uploads N", color="#7D3C98")
dot.edge("patient",     "webuser",             label="registered as", style="dashed")
dot.edge("doctor",      "webuser",             label="registered as", style="dashed")
dot.edge("admin",       "webuser",             label="registered as", style="dashed")

dot.render(cleanup=True)
print("✅ ER Diagram saved: diagram2_er.png")