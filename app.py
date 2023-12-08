
from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/fetch_words')
def fetch_words():
    url = 'https://www.lifeprint.com/dictionary.htm'  # Replace with your desired URL
    html_content = fetch_page(url)
    if html_content:
        words = parse_words(html_content)
        return jsonify({'words': words})
    else:
        return jsonify({'words': []})

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def parse_words(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        word_elements = soup.find_all("td", class_="WordListTable")
        words = [word.text.strip() for word in word_elements]
        return words
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True)
