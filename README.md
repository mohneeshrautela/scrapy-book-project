# Mini Product Crawler: Book Scraper Project

This is a Scrapy project designed to scrape book information from [books.toscrape.com]

## What it does:
* Goes to all the book categories on the site.
* Clicks the "next" page button to get all the books.
* Grabs the title, price, rating, etc. for each book.
* Saves everything into a SQLite database file.
* Also saves the data to books_data.csv and books_data.json.
* Downloads all the book cover images into the images folder.

## How to Install & Run

### Installation

1.  **Set up the project folder**
    Clone or download this project to your local machine.

2.  **Install the required packages**
    Install Scrapy and Pillow using pip.
    ```bash
    pip install Scrapy Pillow
    ```
### Running the Spider

Run the commands from the project's root folder.

1. **Set up the database**
    Create the database and its table.
    ```bash
    # Navigate into the correct folder first
    cd bookscraper
    
    # Now run the setup script
    python database_setup.py
    ```
2.  **Run the spider**
    To start the scraping process, run the below mentioned command.
    ```bash
    scrapy crawl bookspider
    ```
    The spider will start, and the scraped data will be saved automatically to the database, CSV/JSON files, and the images folder.

## How to Change Category/Start URL

1. **Navigate to and open**: `bookscraper/bookscraper/spiders/bookspider.py`.

2. **Edit the `start_urls` list**

3. **Change the URL**: Replace the homepage URL with the URL of the specific category you want to scrape.


