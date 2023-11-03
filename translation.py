from flask import Flask, request, jsonify
from asl_translator import ASLTranslator

app = Flask(__name__)
translator = ASLTranslator()

@app.route('/translate', methods=['POST'])
def translate_to_asl():
    try:
        data = request.get_json()
        if 'text' in data:
            text = data['text']
            asl_translation = translator.translate(text, from_lang='en')
            return jsonify({'asl_translation': asl_translation})
        else:
            return jsonify({'error': 'Missing "text" field in request data'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

