from flask import Flask, request, jsonify

app = Flask(__name__)
user_words = [] 
@app.route('/add_word', methods=['POST'])
def add_word():
    data = request.get_json()  
    word = data.get('word')

    if word:
        user_words.append(word) 
        return jsonify({'message': 'Word added successfully'})
    else:
        return jsonify({'error': 'Invalid request'})

@app.route('/get_user_words', methods=['GET'])
def get_user_words():
    return jsonify({'user_words': user_words})

if __name__ == '__main__':
    app.run(debug=True)
