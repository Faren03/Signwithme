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

function translateToASL() {
  if (!translationApplied) {
    const messageList = document.getElementById('message-list');
    const messages = messageList.getElementsByTagName('li');

    for (let i = 0; i < messages.length; i++) {
      const messageText = messages[i].textContent.split(': ')[1];
      const aslResult = translateToASLText(messageText);
      messages[i].innerHTML = `<span class="user">${currentUser}:</span> ${aslResult}`;
    }

    // Set translation flag to true
    translationApplied = true;
  }
}

function translateToASLText(text) {
  const asl_dictionary = {
    "hello": "👋",
    "world": "🌎",
    "how": "🤔",
    "are": "👍",
    "you": "👋",
  };

  const words = text.toLowerCase().split(' ');
  let aslTranslation = '';

  for (const word of words) {
    if (asl_dictionary[word]) {
      aslTranslation += asl_dictionary[word] + ' ';
    } else {
      aslTranslation += word + ' ';
    }
  }

  return aslTranslation.trim();
}

function checkForASL() {
  const messageBox = document.getElementById('message-box');
  const inputText = messageBox.value.trim().toLowerCase();

  if (inputText in asl_dictionary) {
    messageBox.value = asl_dictionary[inputText];
  }
}
