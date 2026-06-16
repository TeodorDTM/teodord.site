// ===== CONFIG =====
// Setează pe true dacă rulezi serverul Python (python server.py)
// Setează pe false pentru mod demo (fără server)
const USE_SERVER = true;
const SERVER_URL = '';

// ===== SESIUNE =====
const SESSION_ID = 'session_' + Math.random().toString(36).slice(2, 10);

// ===== STATE LOCAL (backup când nu e server) =====
const localState = {
  step: 'AWAIT_CHAPTER',
  chapter: null,
  waitingForBot: false,
};

const CHAPTERS = {
  '1': 'Matrici',
  '2': 'Generarea matricelor',
  '3': 'Subprograme',
  '4': 'Siruri de caractere',
  '5': 'Struct',
  '6': 'Recursivitate',
  '7': "Mesajul de final al clasei a X-a",
};

// ===== INIT =====
window.addEventListener('DOMContentLoaded', async () => {
  const input = document.getElementById('userInput');
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendMessage();
  });

  if (USE_SERVER) {
    await loadWelcomeFromServer();
  } else {
    showLocalWelcome();
  }
});

// ===== WELCOME (SERVER) =====
async function loadWelcomeFromServer() {
  try {
    const res = await fetch(`${SERVER_URL}/api/welcome`);
    if (!res.ok) throw new Error('Server unavailable');
    const data = await res.json();

    for (let i = 0; i < data.messages.length; i++) {
      await delay(400 + i * 650);
      addBotMessage(data.messages[i].text);
    }
  } catch (e) {
    console.warn('Server indisponibil, folosim mod local:', e.message);
    showLocalWelcome();
  }
}

// ===== WELCOME (LOCAL FALLBACK) =====
function showLocalWelcome() {
  const chList = Object.entries(CHAPTERS).map(([n, t]) =>
    `<div style="padding:2px 0">📘 <strong>${n}</strong> — ${t}</div>`
  ).join('');

  setTimeout(() => addBotMessage('👋 Bună! Sunt <strong>EduBot</strong>, asistentul tău educațional interactiv.'), 400);
  setTimeout(() => addBotMessage('Tastează un număr de la <strong>1 la 7</strong> pentru a selecta capitolul pe care vrei să îl parcurgi.'), 1050);
  setTimeout(() => addBotMessage(`<div style="margin-top:6px">${chList}</div>`), 1800);
}

// ===== SEND MESSAGE =====
async function sendMessage() {
  if (localState.waitingForBot) return;
  const input = document.getElementById('userInput');
  const text = input.value.trim();
  if (!text) return;

  input.value = '';
  addUserMessage(text);

  if (USE_SERVER) {
    await sendToServer(text);
  } else {
    await handleLocalMessage(text);
  }
}

// ===== SERVER COMMUNICATION =====
async function sendToServer(text) {
  localState.waitingForBot = true;
  const typingId = showTypingIndicator();

  try {
    const res = await fetch(`${SERVER_URL}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: SESSION_ID, message: text }),
    });

    removeTypingIndicator(typingId);

    if (!res.ok) throw new Error('Server error');
    const data = await res.json();

    // Afișăm mesajele cu delay între ele
    for (let i = 0; i < (data.messages || []).length; i++) {
      await delay(i === 0 ? 0 : 500);
      addBotMessage(data.messages[i].text);
    }

    // Afișăm butoanele dacă există
    if (data.buttons && data.buttons.length > 0) {
      await delay(300);
      addChoiceButtonsFromServer(data.buttons, data.chapter);
    }

    // Actualizăm sidebar
    if (data.step === 'AWAIT_CHOICE' || data.step === 'DONE') {
      const chNum = extractChapterFromButtons(data.buttons);
      if (chNum) highlightChapter(chNum);
    }

  } catch (e) {
    console.error('Eroare server:', e);
    removeTypingIndicator(typingId);
    addBotMessage('⚠️ <em>Serverul nu răspunde. Asigură-te că ai pornit <code>python server.py</code>.</em>');
    // Fallback la logic local
    await handleLocalMessage(text);
  } finally {
    localState.waitingForBot = false;
  }
}

function extractChapterFromButtons(buttons) {
  if (!buttons || !buttons.length) return null;
  const href = buttons[0].href || '';
  const match = href.match(/capitol=(\d)/);
  return match ? match[1] : null;
}

// ===== SERVER BUTTONS =====
function addChoiceButtonsFromServer(buttons, chapter) {
  const area = document.getElementById('messagesArea');

  const row = document.createElement('div');
  row.className = 'msg-row bot';
  row.id = 'choice-row';

  const avatar = document.createElement('div');
  avatar.className = 'bot-avatar';
  avatar.textContent = 'EB';

  const btnsDiv = document.createElement('div');
  btnsDiv.className = 'choice-buttons';

  buttons.forEach(btn => {
    if (btn.href === 'change_chapter') {
      // Buton special: nu navigheaza, trimite comanda la server
      const b = document.createElement('button');
      b.className = 'choice-btn';
      b.innerHTML = btn.text;
      b.addEventListener('click', () => {
        disableChoiceButtons();
        addUserMessage('🔀 Alege alt capitol');
        sendToServer('change_chapter');
      });
      btnsDiv.appendChild(b);
    } else {
      const a = document.createElement('a');
      a.className = 'choice-btn';
      a.href = `${btn.href}`;
      a.innerHTML = btn.text;
      a.addEventListener('click', () => disableChoiceButtons());
      btnsDiv.appendChild(a);
    }
  });

  row.appendChild(avatar);
  row.appendChild(btnsDiv);
  area.appendChild(row);
  scrollToBottom();
}

// ===== LOCAL FALLBACK LOGIC =====
async function handleLocalMessage(text) {
  if (localState.step === 'AWAIT_CHAPTER') {
    await handleLocalChapter(text);
  } else if (localState.step === 'AWAIT_CHOICE') {
    await delay(600);
    addBotMessage('Te rog apasă unul dintre butoanele de mai sus — <strong>📖 Teorie</strong> sau <strong>✏️ Probleme</strong>.');
  }
}

async function handleLocalChapter(text) {
  const num = text.trim();
  const typingId = showTypingIndicator();
  await delay(800);
  removeTypingIndicator(typingId);

  if (!['1','2','3','4','5'].includes(num)) {
    addBotMessage('⚠️ Te rog tastează un număr valid între <strong>1 și 5</strong>.');
    return;
  }

  localState.chapter = num;
  localState.step = 'AWAIT_CHOICE';
  highlightChapter(num);

  addBotMessage(`✅ Ai selectat <strong>Capitol ${num} — ${CHAPTERS[num]}</strong>.`);
  await delay(500);
  addBotMessage('Ce vrei să faci în cadrul acestui capitol?');
  await delay(400);
  addChoiceButtonsLocal(num);
}

function addChoiceButtonsLocal(num) {
  const area = document.getElementById('messagesArea');

  const row = document.createElement('div');
  row.className = 'msg-row bot';
  row.id = 'choice-row';

  const avatar = document.createElement('div');
  avatar.className = 'bot-avatar';
  avatar.textContent = 'EB';

  const btnsDiv = document.createElement('div');
  btnsDiv.className = 'choice-buttons';

  const teorie = document.createElement('a');
  teorie.className = 'choice-btn';
  teorie.href = `teorie.html?capitol=${num}`;
  teorie.innerHTML = '📖 Teorie';
  teorie.addEventListener('click', () => disableChoiceButtons());

  const probleme = document.createElement('a');
  probleme.className = 'choice-btn';
  probleme.href = `probleme.html?capitol=${num}`;
  probleme.innerHTML = '✏️ Probleme';
  probleme.addEventListener('click', () => disableChoiceButtons());

  btnsDiv.appendChild(teorie);
  btnsDiv.appendChild(probleme);
  row.appendChild(avatar);
  row.appendChild(btnsDiv);
  area.appendChild(row);
  scrollToBottom();
}

// ===== TYPING INDICATOR =====
let typingCounter = 0;
function showTypingIndicator() {
  const id = 'typing-' + (++typingCounter);
  const area = document.getElementById('messagesArea');

  const row = document.createElement('div');
  row.className = 'msg-row bot';
  row.id = id;

  const avatar = document.createElement('div');
  avatar.className = 'bot-avatar';
  avatar.textContent = 'EB';

  const bubble = document.createElement('div');
  bubble.className = 'msg-bubble';
  bubble.innerHTML = `<div class="typing-indicator"><span></span><span></span><span></span></div>`;

  row.appendChild(avatar);
  row.appendChild(bubble);
  area.appendChild(row);
  scrollToBottom();
  return id;
}

function removeTypingIndicator(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

// ===== DISABLE CHOICE BUTTONS =====
function disableChoiceButtons() {
  const row = document.getElementById('choice-row');
  if (row) {
    row.querySelectorAll('.choice-btn').forEach(b => b.classList.add('disabled'));
  }
}

// ===== ADD BOT MESSAGE =====
function addBotMessage(html) {
  const area = document.getElementById('messagesArea');

  const row = document.createElement('div');
  row.className = 'msg-row bot';

  const avatar = document.createElement('div');
  avatar.className = 'bot-avatar';
  avatar.textContent = 'EB';

  const bubble = document.createElement('div');
  bubble.className = 'msg-bubble';
  bubble.innerHTML = html;

  row.appendChild(avatar);
  row.appendChild(bubble);
  area.appendChild(row);
  scrollToBottom();
}

// ===== ADD USER MESSAGE =====
function addUserMessage(text) {
  const area = document.getElementById('messagesArea');

  const row = document.createElement('div');
  row.className = 'msg-row user';

  const bubble = document.createElement('div');
  bubble.className = 'msg-bubble';
  bubble.textContent = text;

  row.appendChild(bubble);
  area.appendChild(row);
  scrollToBottom();
}

// ===== HIGHLIGHT SIDEBAR =====
function highlightChapter(num) {
  document.querySelectorAll('.chapter-item').forEach(el => el.classList.remove('active'));
  const el = document.getElementById(`ch${num}`);
  if (el) el.classList.add('active');
}

// ===== RESET CHAT =====
async function resetChat() {
  localState.step = 'AWAIT_CHAPTER';
  localState.chapter = null;
  localState.waitingForBot = false;
  document.querySelectorAll('.chapter-item').forEach(el => el.classList.remove('active'));
  document.getElementById('messagesArea').innerHTML = '';

  addSystemMessage('Chat resetat');

  if (USE_SERVER) {
    try {
      const res = await fetch(`${SERVER_URL}/api/reset`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: SESSION_ID }),
      });
      const data = await res.json();
      setTimeout(() => addBotMessage(data.messages[0].text), 300);
    } catch {
      setTimeout(() => addBotMessage('🔄 Chat resetat! Tastează un număr de la <strong>1 la 5</strong>.'), 300);
    }
  } else {
    setTimeout(() => addBotMessage('🔄 Chat resetat! Tastează un număr de la <strong>1 la 5</strong>.'), 300);
  }
}

// ===== SYSTEM MESSAGE =====
function addSystemMessage(text) {
  const area = document.getElementById('messagesArea');
  const div = document.createElement('div');
  div.className = 'system-msg';
  div.textContent = `— ${text} —`;
  area.appendChild(div);
}

// ===== UTILS =====
function scrollToBottom() {
  const area = document.getElementById('messagesArea');
  setTimeout(() => { area.scrollTop = area.scrollHeight; }, 50);
}

function delay(ms) {
  return new Promise(res => setTimeout(res, ms));
}