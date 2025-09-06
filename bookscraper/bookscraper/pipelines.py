import sqlite3
import os
from scrapy.exceptions import DropItem
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'books.db')

class BookscraperPipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()
        
    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        has_title = item.get('title')
        has_price = item.get('price')

        if not has_title or not has_price:
            raise DropItem("Book is missing a title or price!")

        sql_command = "INSERT INTO books (title, price, rating, availability, product_url, image_url, category) VALUES (?, ?, ?, ?, ?, ?, ?)"
        
        data_to_insert = (
            item.get('title'),
            item.get('price'),
            item.get('rating'),
            item.get('availability'),
            item.get('product_url'),
            item.get('image_url')[0] if item.get('image_url') else None,
            item.get('category')
        )
        
        try:
            self.cursor.execute(sql_command, data_to_insert)
            self.connection.commit()
        except sqlite3.IntegrityError:
            spider.logger.warning(f"This book is already in the database: {item.get('product_url')}")

        return item