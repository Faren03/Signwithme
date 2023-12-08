pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Send a GET request to the Lifeprint dictionary page
url = "https://www.lifeprint.com/dictionary.htm"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the elements containing the words
    word_elements = soup.find_all("td", class_="WordListTable")

    # Extract the words
    words = [word.text.strip() for word in word_elements]

    # Print the extracted words
    print(words)
else:
    print("Failed to fetch the page")
