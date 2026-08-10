# Day 01 - Quotes Web Scraper

A beginner-friendly web scraping project built with Python.

## Technologies

* Python
* Requests
* BeautifulSoup
* CSV

## What This Project Does

This scraper extracts:

* Quote
* Author

from the practice website:

https://quotes.toscrape.com/

The extracted data is saved into a CSV file.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the scraper:

```bash
python main.py
```

## Output

The scraper creates:

```text
quotes.csv
```

containing the extracted quotes and authors.

## Learning Goals

This project helped me understand:

* HTTP requests
* HTML parsing
* BeautifulSoup
* Finding HTML elements
* Extracting text
* Saving scraped data into CSV
