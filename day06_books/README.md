# Day 06 - Scrapy Books Crawler

A web crawling project built with Python and Scrapy.

This project introduces the Scrapy framework for structured crawling, pagination, item management, data extraction, and CSV export.

## 🌐 Website

https://books.toscrape.com/

Books to Scrape is a practice website designed for learning web scraping.

## 🎯 Project Goals

The crawler extracts:

- Book title
- Price
- Rating
- Availability
- Product URL

It automatically follows pagination and collects all available books.

## 🛠️ Technologies Used

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

