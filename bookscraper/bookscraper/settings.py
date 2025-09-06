# Scrapy settings for bookscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "bookscraper"

SPIDER_MODULES = ["bookscraper.spiders"]
NEWSPIDER_MODULE = "bookscraper.spiders"

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

ITEM_PIPELINES = {
   "bookscraper.pipelines.BookscraperPipeline": 300,
   "scrapy.pipelines.images.ImagesPipeline": 1, 
}

IMAGES_STORE = 'images'

IMAGES_URLS_FIELD = 'image_url'

FEEDS = {
    'books_data.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': None,
        'indent': 4,
    },
    'books_data.csv': {
        'format': 'csv',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': ['title', 'price', 'rating', 'availability', 'category', 'product_url'],
    },
}
