import json
import requests
from parsel import Selector


url = "http://quotes.toscrape.com"
response = requests.get(url, timeout=10)
selector = Selector(response.text)

quotes = selector.css(".quote")
data = []

for quote in quotes:
    text = quote.css(".text::text").get()
    author = quote.css(".author::text").get()
    tags = quote.css(".tags .tag::text").getall()

    data.append({"text": text, "author": author, "tags": tags})

# Lưu dữ liệu vào file JSON
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Dữ liệu đã được lưu vào file quotes.json.")
