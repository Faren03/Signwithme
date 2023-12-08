from flask import Flask, request, jsonify

app = Flask(__name__)
user_words = []  # List to store user-provided words

@app.route('/add_word', methods=['POST'])
def add_word():
    data = request.get_json()  # Get JSON data from the request
    word = data.get('word')  # Extract the word from the JSON data

    if word:
        user_words.append(word)  # Add the word to the list of user words
        return jsonify({'message': 'Word added successfully'})
    else:
        return jsonify({'error': 'Invalid request'})

@app.route('/get_user_words', methods=['GET'])
def get_user_words():
    return jsonify({'user_words': user_words})

if __name__ == '__main__':
    app.run(debug=True)
