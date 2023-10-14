from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (you can replace this with your data)
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

# Define a route for your API endpoint
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
