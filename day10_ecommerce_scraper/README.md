# 🚀 E-commerce Product Scraper

A client-style web scraping project that extracts structured product data from Books to Scrape.

## 🌐 Target Website

https://books.toscrape.com/

Books to Scrape is a practice website designed for learning web scraping.

## 🎯 Project Goal

The goal of this project is to collect product information from all available pages and deliver clean, structured data in CSV and JSON formats.

## 📊 Data Fields

The scraper extracts:

* Product title
* Price
* Rating
* Availability
* Product URL

## ✨ Features

* HTTP requests using Requests
* HTML parsing using BeautifulSoup
* Automatic pagination
* Product extraction
* Price cleaning
* Relative URL normalization
* Missing-data handling
* Duplicate detection
* Data validation
* CSV export
* JSON export
* Basic error handling
* User-Agent header

## 🛠️ Technologies

* Python
* Requests
* BeautifulSoup
* Pandas

## 📁 Project Structure

```text
day10_ecommerce_scraper/
│
├── scraper.py
│
├── data/
│   ├── products.csv
│   └── products.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Clone the repository and install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run:

```bash
python scraper.py
```

The scraper automatically:

1. Opens the first page
2. Extracts product information
3. Cleans the data
4. Finds the next page
5. Continues until the last page
6. Removes duplicate product URLs
7. Validates the collected data
8. Saves the results

## 📦 Output

The scraper generates:

```text
data/products.csv
data/products.json
```

### CSV

The CSV contains:

```text
title
price
rating
availability
product_url
```

### JSON

The JSON contains the same product information in structured JSON format.

## 🧹 Data Cleaning

Prices such as:

```text
£51.77
```

are converted into:

```text
51.77
```

Product URLs are converted from relative URLs into absolute URLs.

Missing values are handled gracefully instead of causing the scraper to crash.

## 🔍 Data Validation

Before saving the data, the scraper checks:

* Total number of records
* Missing values
* Duplicate records

Example:

```python
df.isnull().sum()
```

and:

```python
df.duplicated().sum()
```

## 🔄 Pagination

The scraper automatically follows the next-page link:

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

No manual page URLs are required.

## ⚠️ Error Handling

The scraper uses:

```python
response.raise_for_status()
```

and catches request-related exceptions.

If a request fails, the scraper stops safely instead of silently producing incorrect data.

## 💼 Client-Style Deliverable

A typical client request could be:

> "Collect all publicly available products from the website and provide the data in a structured format."

This project demonstrates the workflow:

```text
Website
   ↓
HTTP Request
   ↓
HTML
   ↓
BeautifulSoup
   ↓
Product Extraction
   ↓
Data Cleaning
   ↓
Validation
   ↓
CSV + JSON
```

## ⚖️ Responsible Scraping

This project uses a dedicated practice website.

For real client projects:

* Check whether automated access is permitted.
* Prefer an official/public API when available.
* Respect applicable terms and access rules.
* Use reasonable request rates.
* Do not attempt to bypass authentication, CAPTCHA, or other access controls.
* Collect only the data required for the project.

## 🚧 Limitations

This project is designed as a learning and portfolio project.

For production use, additional features could include:

* Structured logging
* Configurable request delays
* Retry strategies
* Database storage
* Automated tests
* Monitoring
* Scheduled scraping
* Better duplicate handling

## 🧠 What I Learned

* Building a client-style scraper
* Separating scraper functions
* HTML parsing
* Pagination
* Data cleaning
* URL normalization
* Data validation
* Duplicate detection
* CSV and JSON exports
* Basic error handling
* Responsible web scraping

## 🚀 Future Improvements

Possible improvements include:

* Add Scrapy version
* Add database storage
* Add automated tests
* Add configuration files
* Add logging
* Build a scheduled data pipeline
* Deploy the scraper as a service

---

### 📌 Learning Project

Part of my Web Scraping Journey — focused on building practical, reliable, and client-ready scraping projects.
