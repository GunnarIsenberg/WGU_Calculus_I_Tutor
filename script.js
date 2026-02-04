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