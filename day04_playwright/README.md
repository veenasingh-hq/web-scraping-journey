# Day 04 - JavaScript Quotes Scraper

A browser automation project built with Python and Playwright to scrape JavaScript-rendered content.

## 🌐 Website

https://quotes.toscrape.com/js/

This version of the Quotes to Scrape website uses JavaScript to render the quote content.

## 🎯 Project Goals

The scraper extracts:

* Quote
* Author
* Tags

It also automatically navigates through multiple pages.

## 🛠️ Technologies

* Python
* Playwright
* CSV

## 📁 Project Structure

```text
day04_playwright/
│
├── main.py
├── requirements.txt
├── README.md
├── quotes_dynamic.csv
└── page.png
```

## 📦 Installation

Install Playwright:

```bash
pip install playwright
```

Install the required browser binaries:

```bash
playwright install
```

Or install dependencies from the requirements file:

```bash
pip install -r requirements.txt
playwright install
```

## ▶️ How to Run

Run:

```bash
python main.py
```

The scraper opens the JavaScript-enabled website using Chromium and extracts the rendered quote data.

## 📊 Data Collected

| Field  | Description                    |
| ------ | ------------------------------ |
| quote  | Quote text                     |
| author | Author name                    |
| tags   | Tags associated with the quote |

## 🔄 Pagination

The scraper automatically detects and clicks the Next button.

```text
Page 1
   ↓
Page 2
   ↓
Page 3
   ↓
...
   ↓
Last Page
```

The scraper stops when a Next button is no longer available.

## ⏳ Waiting for Content

Because the website uses JavaScript, the scraper waits for the quote elements to become visible before extracting data.

This is different from a simple Requests + BeautifulSoup scraper.

## 📸 Screenshots

The scraper takes a screenshot of the page:

```text
page.png
```

If an error occurs during scraping, an additional screenshot is created:

```text
error.png
```

These screenshots can help with debugging automation problems.

## 🛡️ Error Handling

The main scraping workflow uses `try/except/finally`.

If an error occurs:

1. The error is printed.
2. An error screenshot is saved.
3. The browser is closed safely.

## 🧠 What I Learned

This project helped me understand:

* Static vs dynamic websites
* Browser automation
* Playwright
* Chromium automation
* Page navigation
* Locators
* CSS selectors
* Waiting for rendered content
* Extracting text from locators
* Pagination with browser automation
* Screenshots
* Basic error handling
* CSV export

## 🔍 BeautifulSoup vs Playwright

### BeautifulSoup

Best when the required data is already present in the HTML response.

```text
Request
   ↓
HTML
   ↓
BeautifulSoup
   ↓
Data
```

### Playwright

Useful when the page requires browser execution and JavaScript rendering.

```text
Browser
   ↓
Website
   ↓
JavaScript
   ↓
Rendered content
   ↓
Playwright
   ↓
Data
```

## 🚀 Future Improvements

Possible improvements include:

* Add structured logging
* Export to Excel
* Add retry logic
* Add configurable URLs
* Add command-line arguments
* Store data in a database
* Create reusable browser automation utilities
* Add automated tests

## 📌 Learning Project

This project is part of my Web Scraping Journey and is designed to build practical browser automation and data extraction skills for real-world projects and freelancing.
