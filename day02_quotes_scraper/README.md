# Day 02 - Quotes Scraper v2

A multi-page web scraper built with Python, Requests, and BeautifulSoup.

This project is an improved version of the Day 1 Quotes Scraper. Instead of scraping only the first page, this scraper automatically navigates through all available pages and collects structured quote data.

## 🌐 Website

https://quotes.toscrape.com/

Quotes to Scrape is a practice website designed for learning web scraping.

## 🎯 Project Goals

The scraper extracts:

* Quote
* Author
* Author profile URL
* Tags

It automatically follows the pagination until the last page.

## 🛠️ Technologies Used

* Python
* Requests
* BeautifulSoup
* CSV

## 📁 Project Structure

```text
day02_quotes_scraper/
│
├── main.py
├── quotes.csv
├── requirements.txt
└── README.md
```

## 📦 Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

Or install them directly:

```bash
pip install requests beautifulsoup4
```

## ▶️ How to Run

Run the scraper from the project directory:

```bash
python main.py
```

The program will automatically scrape the pages and save the extracted data into:

```text
quotes.csv
```

## 📊 Data Collected

The CSV file contains four columns:

| Column     | Description                    |
| ---------- | ------------------------------ |
| quote      | The quote text                 |
| author     | Name of the author             |
| author_url | Author's profile URL           |
| tags       | Tags associated with the quote |

## 🔄 Pagination

The scraper automatically detects the **Next** button.

The process works like this:

```text
Page 1
   ↓
Page 2
   ↓
Page 3
   ↓
Page 4
   ↓
...
   ↓
Last Page
   ↓
Stop
```

This allows the scraper to collect data from multiple pages without manually entering each URL.

## 🛡️ Error Handling

The scraper uses:

```python
response.raise_for_status()
```

and a `try/except` block to handle request-related errors.

A timeout is also used:

```python
timeout=10
```

This prevents the program from waiting indefinitely for a response.

## 🌐 User-Agent

The scraper sends a User-Agent header with the request:

```python
headers = {
    "User-Agent": "Mozilla/5.0"
}
```

This makes the HTTP request resemble a normal browser request.

## 🔗 URL Handling

Some URLs on the website are relative URLs, such as:

```text
/page/2/
```

The project uses `urljoin()` to convert relative URLs into complete URLs.

Example:

```text
/page/2/
```

becomes:

```text
https://quotes.toscrape.com/page/2/
```

## 💾 Output

The final data is stored in:

```text
quotes.csv
```

Example:

```text
quote,author,author_url,tags
"The world as we have created it...",Albert Einstein,https://quotes.toscrape.com/author/Albert-Einstein/,change,deep-thoughts
```

## 🧠 What I Learned

Through this project, I learned:

* CSS selectors with BeautifulSoup
* `select()` and `select_one()`
* Extracting attributes from HTML
* Pagination
* `while` loops for automated scraping
* Relative and absolute URLs
* `urljoin()`
* HTTP error handling
* Request timeouts
* User-Agent headers
* Exporting scraped data to CSV
* Structuring a web scraping project

## 🚀 Future Improvements

Possible improvements for the next version:

* Add logging
* Add command-line arguments
* Scrape author details
* Store data in JSON
* Store data in a database
* Add duplicate detection
* Add retry logic
* Build a reusable scraper class

## 📌 Learning Project

This project was created as part of my **Web Scraping Journey** to develop practical web scraping and data extraction skills.
