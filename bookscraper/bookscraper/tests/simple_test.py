from scrapy.http import HtmlResponse
from bookscraper.spiders.bookspider import BookspiderSpider

html_string = """
<html>
<body>
    <h1>A Light in the Attic</h1>
    <p class="price_color">£51.77</p>
    <p class="star-rating Three">some text here</p>
</body>
</html>
"""

my_spider = BookspiderSpider()

fake_url = "http://some-fake-url.com"
fake_response = HtmlResponse(url=fake_url, body=html_string, encoding='utf-8')

scraped_item = next(my_spider.parse_book_page(fake_response))

print(scraped_item)

if scraped_item['title'] == 'A Light in the Attic':
    print("Title is correct.")
else:
    print("Title is wrong!")

if scraped_item['price'] == '51.77':
    print("Price is correct.")
else:
    print("Price is wrong!")

if scraped_item['rating'] == 'Three':
    print("Rating is correct.")
else:
    print("Rating is wrong!")
