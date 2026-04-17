// HMS Chatbot

document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('chatInput');
    if (input) input.addEventListener('keypress', e => { if (e.key === 'Enter') handleChat(); });
});

// ── UI ────────────────────────────────────────────────────────────────────────
function toggleChat() {
    const chat = document.getElementById('chatWindow');
    chat.style.display =
        (chat.style.display === 'none' || chat.style.display === '') ? 'flex' : 'none';
}

function handleChat() {
    const input   = document.getElementById('chatInput');
    const message = input.value.trim();
    if (!message) return;
    input.value = '';
    sendMessage(message);
}

function appendMessage(text, type) {
    const body = document.getElementById('chatBody');
    const div  = document.createElement('div');
    div.className = `msg ${type}-msg`;
    div.innerHTML = text.replace(/\n/g, '<br>');
    body.appendChild(div);
    body.scrollTop = body.scrollHeight;
}

function showTyping() {
    const body = document.getElementById('chatBody');
    const div  = document.createElement('div');
    div.className = 'msg bot-msg';
    div.id = 'typing-indicator';
    div.innerHTML = '<span style="opacity:0.6">⏳ Thinking...</span>';
    body.appendChild(div);
    body.scrollTop = body.scrollHeight;
}

function removeTyping() {
    const el = document.getElementById('typing-indicator');
    if (el) el.remove();
}

// ── Send message to chatbot backend ──────────────────────────────────────────
async function sendMessage(userMessage) {
    appendMessage(userMessage, 'user');
    showTyping();

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await res.json();
        removeTyping();

        const reply = data.reply || 'Sorry, I could not get a response.';
        appendMessage(reply, 'bot');

    } catch(e) {
        removeTyping();
        appendMessage('Sorry, something went wrong. Please try again.', 'bot');
    }
}
