from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/parse-file', methods=['POST'])
def parse_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        try:
            # Read the file using pandas
            df = pd.read_csv(file)
            # Assuming the CSV file has a 'text' column, you can categorize words here
            # For simplicity, we'll just split and categorize the words based on their length
            df['category'] = df['text'].apply(lambda x: 'short' if len(x) < 5 else 'long')

            # Return the categorized data as JSON
            return jsonify(df.to_dict(orient='records'))

        except Exception as e:
            return jsonify({'error': f'Error processing the file: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
