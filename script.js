const sendBtn = document.getElementById('send-btn');
const userInput = document.getElementById('user-input');
const messageBox = document.getElementById('messages');

async function sendMessage() {
    const text = userInput.value;
    if (!text) return;

    // 1. Add User Message to UI
    appendMessage(text, 'user');
    userInput.value = '';

    // 2. Call your FastAPI Endpoint
    try {
        const response = await fetch('http://127.0.0.1:8000/sendmsg', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_text: text }) // Matches your Pydantic model
        });

        const data = await response.json();
        
        // 3. Add AI Response to UI
        appendMessage(data.reply, 'ai');
    } catch (error) {
        appendMessage("Error connecting to server.", 'ai');
    }
}

function appendMessage(content, sender) {
    const div = document.createElement('div');
    div.className = `msg ${sender}`;
    div.innerText = content;
    messageBox.appendChild(div);
    messageBox.scrollTop = messageBox.scrollHeight; // Auto-scroll
}

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => { if(e.key === 'Enter') sendMessage(); });

// Helper to get cookie by name
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

async function sendMessage() {
    const text = userInput.value;
    const userId = getCookie('user_id'); // Get the ID we set in the backend

    if (!text || !userId) return;

    appendMessage(text, 'user');
    userInput.value = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/sendmsg', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                user_text: text,
                user_id: userId // Send this to link messages to the account
            })
        });

        const data = await response.json();
        appendMessage(data.reply, 'ai');
    } catch (error) {
        appendMessage("Connection error. Try logging in again.", 'ai');
    }
}

function appendMessage(content, sender) {
    const div = document.createElement('div');
    const userId = getCookie('user_id');
    
    // Determine label
    let labelText = "Tutor";
    if (sender === 'user') {
        labelText = userId.startsWith('guest_') ? "Guest" : "Student";
    }

    div.className = `msg ${sender}`;
    div.innerHTML = `
        <span class="msg-label">${labelText}</span>
        <div class="msg-text">${content}</div>
    `;
    
    messageBox.appendChild(div);
    messageBox.scrollTop = messageBox.scrollHeight;
}