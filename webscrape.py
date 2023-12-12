import json
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=python+tutorial&gl=us"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.2816.203 Safari/537.36"}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')

search_results = []
#select all elements which has class g
for el in soup.select("div.g"):
    title = el.select_one("h3").get_text()
    # Check if the anchor element exists before trying to access its attributes
    link_element = el.select_one("a")
    link = link_element["href"] if link_element else None
    description = el.select_one(".VwiC3b").get_text()

    search_results.append({
        "title": title,
        "link": link,
        "description": description,
    })

# Print the results in JSON format
print(json.dumps(search_results, indent=2))

