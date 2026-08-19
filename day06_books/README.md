
# Day 07 - Scraper Reliability & Error Handling

This project upgrades the Day 06 Scrapy Books Crawler with reliability, validation, logging, retries, throttling, and duplicate handling.

## 🌐 Website

https://books.toscrape.com/

Books to Scrape is a practice website designed for learning web scraping.

## 🎯 Day 07 Goals

The scraper focuses on:

- HTTP error awareness
- Request timeouts
- Retry configuration
- Request delays
- AutoThrottle
- Logging
- Missing data handling
- Duplicate detection
- Data validation
- Scrapy pipelines

## 🛠️ Technologies

- Python
- Scrapy
- CSS Selectors
- CSV

## 📁 Project Structure

```text
day06_books/
│
├── scrapy.cfg
├── README.md
├── books.csv
│
└── day06_books/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    │
    └── spiders/
        ├── __init__.py
        └── books.py
