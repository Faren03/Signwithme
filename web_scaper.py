# web_scraper.py
import requests
from bs4 import BeautifulSoup

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
