import scrapy

from bookscraper.items import BookscraperItem

class BookspiderSpider(scrapy.Spider):

    name = "bookspider"
    
    allowed_domains = ["books.toscrape.com"]
    
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):

        category_links = response.css('div.side_categories ul li ul li a::attr(href)').getall()
        
        for single_category_link in category_links:

            full_category_url = response.urljoin(single_category_link)
            
            yield scrapy.Request(full_category_url, callback=self.parse_category_page)

    def parse_category_page(self, response):

        book_page_links = response.css('article.product_pod h3 a::attr(href)').getall()
        
        for single_book_link in book_page_links:

            full_book_url = response.urljoin(single_book_link)
            
            yield scrapy.Request(full_book_url, callback=self.parse_book_page)
            
        next_page_link = response.css('li.next a::attr(href)').get()
        
        if next_page_link is not None:

            full_next_page_url = response.urljoin(next_page_link)
            
            yield scrapy.Request(full_next_page_url, callback=self.parse_category_page)

    def parse_book_page(self, response):

        book_item = BookscraperItem()

        book_item['title'] = response.css('h1::text').get()
        
        price_string = response.css('p.price_color::text').get()

        if price_string:
            book_item['price'] = price_string.replace('£', '')
        
        rating_text = response.css('p.star-rating::attr(class)').get()
        if rating_text:

            book_item['rating'] = rating_text.split(' ')[1]
        
        availability_text = response.css('p.availability::text').getall()

        if availability_text:
            book_item['availability'] = "".join(availability_text).strip()
            

        relative_image_url = response.css('div.item.active img::attr(src)').get()
        if relative_image_url:

            book_item['image_url'] = [response.urljoin(relative_image_url)]
            
        category = response.css('ul.breadcrumb li:nth-last-child(2) a::text').get()
        book_item['category'] = category

        book_item['product_url'] = response.url

        yield book_item