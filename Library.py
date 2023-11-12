// Define a simple SignLanguageLibrary object
var SignLanguageLibrary = {
  // Define a dictionary mapping words to sign language representations
  signDictionary: {
    'hello': '👋',
    'world': '🌍',
    'goodbye': '👋🏽😊',
    // Add more words and their sign language representations as needed
  },

  // Function to convert text to sign language
  convertTextToSignLanguage: function (text) {
    // Split the input text into words
    var words = text.toLowerCase().split(' ');

    // Map each word to its sign language representation
    var signLanguageRepresentation = words.map(function (word) {
      // Use the signDictionary or default to the original word if not found
      return SignLanguageLibrary.signDictionary[word] || word;
    });

    // Join the sign language representations into a single string
    return signLanguageRepresentation.join(' ');
  }
};

// Example usage
var userInput = 'hello world';
var signLanguageOutput = SignLanguageLibrary.convertTextToSignLanguage(userInput);
console.log(signLanguageOutput);  // Output: 👋 🌍
