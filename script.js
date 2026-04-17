/* --- 1. Doctor Loading Logic --- */
// Fetches data from your MySQL 'doctor' and 'specialties' tables
async function loadDoctors() {
    const listDiv = document.getElementById('doctor-list');
    if (!listDiv) return; // Only runs if the element exists on the page

    try {
        const response = await fetch('http://localhost:3000/api/doctors');
        const doctors = await response.json();
        
        listDiv.innerHTML = ''; // Clear loading message

        doctors.forEach(doc => {
            const card = document.createElement('div');
            card.className = 'doctor-card';
            // Matches your SQL column names: docname and sname (from the join)
            card.innerHTML = `
                <h3>Dr. ${doc.docname}</h3>
                <p>Specialization: ${doc.sname || 'General'}</p>
                <button class="btn-blue" onclick="location.href='book.html?doc=${doc.docid}'" style="padding: 10px; font-size: 0.8rem;">Book Now</button>
            `;
            listDiv.appendChild(card);
        });
    } catch (error) {
        console.error('Error fetching doctors:', error);
        listDiv.innerHTML = '<p style="color:red;">Unable to load doctors. Is the server running?</p>';
    }
}

/* --- 2. Dynamic Specialty Dropdown --- */
// Pulls the 56 specialties you inserted into MySQL
function loadSpecialties() {
    const select = document.getElementById('specialtySelect');
    if (!select) return;

    fetch('http://localhost:3000/api/specialties')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                let option = document.createElement('option');
                option.value = item.id; // From your 'id' column
                option.text = item.sname; // From your 'sname' column
                select.appendChild(option);
            });
        })
        .catch(err => console.error('Error loading specialties:', err));
}

/* --- 3. Global AI Chatbot Logic --- */
function toggleChat() {
    const win = document.getElementById('chatWindow');
    if (win) {
        win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
    }
}

function handleChat() {
    const input = document.getElementById('chatInput');
    const body = document.getElementById('chatBody');
    if (!input || !body) return;

    const text = input.value.toLowerCase().trim();
    if (!text) return;

    // Add User Message bubble
    body.innerHTML += `<div class="msg user-msg">${input.value}</div>`;
    input.value = "";
    body.scrollTop = body.scrollHeight;

    // Simple AI Routing Logic
    setTimeout(() => {
        let response = "I'm not sure I understand. Try asking for 'register' or 'appointment'.";
        
        if (text.includes("register") || text.includes("sign up") || text.includes("account")) {
            response = "Sure! I'm taking you to the registration page now...";
            setTimeout(() => location.href = 'register.html', 2000);
        } else if (text.includes("appointment") || text.includes("doctor") || text.includes("book")) {
            response = "I'll help you make an appointment. Please log in or register first!";
            setTimeout(() => location.href = 'login.html', 2000);
        } else if (text.includes("hello") || text.includes("hi") || text.includes("hey")) {
            response = "Hello! I am the HMS AI Assistant. Do you want to book an appointment or register?";
        }

        body.innerHTML += `<div class="msg bot-msg">${response}</div>`;
        body.scrollTop = body.scrollHeight; // Auto-scroll
    }, 800);
}

/* --- 4. Initialization --- */
window.onload = function() {
    loadDoctors();
    loadSpecialties();
    
    // Allow 'Enter' key to send chat messages
    const chatInput = document.getElementById('chatInput');
    if (chatInput) {
        chatInput.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                handleChat();
            }
        });
    }
};