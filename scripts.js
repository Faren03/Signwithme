let currentUser = 'User';
let translationApplied = false;

function sendMessage() {
  const messageBox = document.getElementById('message-box');
  const message = messageBox.value.trim();

  if (message !== '') {
    const messageList = document.getElementById('message-list');
    const li = document.createElement('li');
    li.className = 'message';
    li.innerHTML = `<span class="user">${currentUser}:</span> ${message}`;
    messageList.appendChild(li);

    // Clear the input box
    messageBox.value = '';

    // Reset translation flag
    translationApplied = false;
  }
}

function switchUser() {
  currentUser = currentUser === 'User' ? 'Another User' : 'User';
}

function checkForASL() {
  const messageBox = document.getElementById('message-box');
  const inputText = messageBox.value.trim().toLowerCase();
}

