import graphviz

dot = graphviz.Digraph("Login_Flow", filename="diagram4_login_flowchart", format="png")
dot.attr(rankdir="TB", bgcolor="white", fontsize="12", pad="0.4")
dot.attr("node", fontsize="11")

# Nodes
dot.node("start",      "Start",                     shape="oval",    style="filled", fillcolor="#2E86C1", fontcolor="white")
dot.node("open",       "Open Login Page",            shape="box",     style="filled", fillcolor="#D6EAF8")
dot.node("enter",      "Enter Email & Password",     shape="box",     style="filled", fillcolor="#D6EAF8")
dot.node("submit",     "Submit Form",                shape="box",     style="filled", fillcolor="#D6EAF8")
dot.node("checkuser",  "Email in webuser table?",    shape="diamond", style="filled", fillcolor="#FCF3CF")
dot.node("gettype",    "Get usertype (p / d / a)",   shape="box",     style="filled", fillcolor="#D6EAF8")
dot.node("checkpass",  "bcrypt.compare(password)?",  shape="diamond", style="filled", fillcolor="#FCF3CF")
dot.node("setsession", "Set req.session.user",       shape="box",     style="filled", fillcolor="#D5F5E3")
dot.node("redirect",   "Redirect to Dashboard",      shape="box",     style="filled", fillcolor="#D5F5E3")
dot.node("wrongpass",  "Show: Wrong Password",       shape="box",     style="filled", fillcolor="#FADBD8")
dot.node("nouser",     "Show: No Account Found",     shape="box",     style="filled", fillcolor="#FADBD8")
dot.node("end",        "End",                        shape="oval",    style="filled", fillcolor="#2E86C1", fontcolor="white")

# Edges
dot.edge("start",      "open")
dot.edge("open",       "enter")
dot.edge("enter",      "submit")
dot.edge("submit",     "checkuser")
dot.edge("checkuser",  "gettype",    label="Yes", color="#117A65")
dot.edge("checkuser",  "nouser",     label="No",  color="#E74C3C")
dot.edge("gettype",    "checkpass")
dot.edge("checkpass",  "setsession", label="Match", color="#117A65")
dot.edge("checkpass",  "wrongpass",  label="No Match", color="#E74C3C")
dot.edge("setsession", "redirect")
dot.edge("redirect",   "end")
dot.edge("wrongpass",  "enter",      label="Retry", style="dashed", color="#E74C3C")
dot.edge("nouser",     "end")

dot.render(cleanup=True)
print("✅ Login Flowchart saved: diagram4_login_flowchart.png")