let currentUser = 'User';
let translationApplied = false;

function sendMessage() {
  const messageBox = document.getElementById('message-box');
  const message = messageBox.value.trim();

  if (message !== '') {
    sendMessageToBackend(message); // Send the message to the backend
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

function sendMessageToBackend(message) {
  // Use Fetch API to send the message to the backend
  fetch('/send-message', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: message }),
  })
    .then(response => {
      // Handle the response from the backend if needed
    })
    .catch(error => console.error('Error:', error));
}

// Event listener for the send button
document.getElementById('send-button').addEventListener('click', sendMessage);

// You can add more functionality or event listeners as needed

