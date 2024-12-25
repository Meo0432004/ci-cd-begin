import requests
from parsel import Selector


def test_extract_first_page():
    url = "http://quotes.toscrape.com"
    response = requests.get(url, timeout=10)
    selector = Selector(response.text)

    quotes = selector.css(".quote")
    assert len(quotes) > 0, "Không có trích dẫn nào được tìm thấy!"

    for quote in quotes:
        text = quote.css(".text::text").get()
        author = quote.css(".author::text").get()
        tags = quote.css(".tags .tag::text").getall()

        assert text, "Text không được rỗng!"
        assert author, "Author không được rỗng!"
        assert isinstance(tags, list), "Tags phải là danh sách!"
