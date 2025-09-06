import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'books.db')

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    rating TEXT,
    availability TEXT,
    product_url TEXT UNIQUE,
    image_url TEXT,
    category TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
cursor.execute(create_table_query)
connection.commit()
connection.close()

print(f"Database created successfully at: {DB_PATH}")