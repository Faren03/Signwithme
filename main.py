# main.py
from word_extractor import extract_words

def main():
    url = "https://www.lifeprint.com/dictionary.htm"
    words = extract_words(url)
    print(words)

if __name__ == "__main__":
    main()
