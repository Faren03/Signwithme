# word_extractor.py
from web_scraper import fetch_page, parse_words

def extract_words(url):
    html_content = fetch_page(url)
    words = parse_words(html_content)
    return words
