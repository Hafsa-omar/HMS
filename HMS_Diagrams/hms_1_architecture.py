from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MySQL
from diagrams.onprem.compute import Server as Storage
from diagrams.programming.language import NodeJS

graph_attr = {"fontsize": "18", "bgcolor": "white", "pad": "0.5", "splines": "ortho"}

with Diagram("HMS - System Architecture", filename="diagram1_architecture", show=False,
             direction="LR", graph_attr=graph_attr):

    with Cluster("Users"):
        patient = User("Patient")
        doctor  = User("Doctor")
        admin   = User("Admin")

    with Cluster("Frontend (HTML/CSS/JS)"):
        dashboard  = Server("Dashboard")
        book       = Server("Book Appointment")
        healthrec  = Server("Health Record")
        docpanel   = Server("Doctor Panel")
        adminpanel = Server("Admin Panel")
        chatui     = Server("AI Chatbot")

    with Cluster("Backend (Node.js / Express)"):
        auth    = NodeJS("Auth Routes")
        pat_r   = NodeJS("Patient Routes")
        doc_r   = NodeJS("Doctor Routes")
        adm_r   = NodeJS("Admin Routes")
        chat_r  = NodeJS("Chatbot Routes")
        multer  = Storage("Multer\n(File Upload)")

    with Cluster("Database (MySQL)"):
        db      = MySQL("MySQL")
        uploads = Storage("uploads/")

    patient >> [dashboard, book, healthrec, chatui]
    doctor  >> docpanel
    admin   >> adminpanel

    dashboard   >> [auth, pat_r]
    book        >> pat_r
    healthrec   >> Edge(label="upload") >> multer
    healthrec   >> pat_r
    chatui      >> chat_r
    docpanel    >> doc_r
    adminpanel  >> adm_r

    [auth, pat_r, doc_r, adm_r, chat_r] >> db
    multer >> db
    multer >> uploads