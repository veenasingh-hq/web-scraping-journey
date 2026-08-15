# Day 03 - Books Web Scraper

A professional-style multi-page web scraper built with Python, Requests, BeautifulSoup, and Pandas.

This project improves upon the previous Quotes Scraper projects by introducing data cleaning, duplicate removal, pagination, logging, error handling, and structured code using functions.

## 🌐 Website

https://books.toscrape.com/

Books to Scrape is a practice website designed for learning web scraping.

## 🎯 Project Goals

The scraper collects:

* Book title
* Price
* Rating
* Availability
* Product URL

It automatically navigates through all available pages.

## 🛠️ Technologies

* Python
* Requests
* BeautifulSoup
* Pandas
* CSV

## 📁 Project Structure

```text
day03_books_scraper/
│
├── main.py
├── books.csv
├── requirements.txt
└── README.md
```

## 📦 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run:

```bash
python main.py
```

The scraper will automatically:

1. Request the website
2. Parse the HTML
3. Extract book information
4. Clean the data
5. Remove duplicate books
6. Follow pagination
7. Save the final dataset

## 📊 Data Fields

| Field        | Description          |
| ------------ | -------------------- |
| title        | Book title           |
| price        | Numerical book price |
| rating       | Star rating          |
| availability | Stock availability   |
| url          | Product URL          |

## 🧹 Data Cleaning

The scraper converts prices such as:

```text
£51.77
```

into:

```text
51.77
```

It also:

* Removes unnecessary whitespace
* Handles missing values
* Removes duplicate URLs
* Converts prices into numeric values

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

No page URLs need to be entered manually.

## 🛡️ Error Handling

The project uses:

```python
response.raise_for_status()
```

along with exception handling for request failures.

A timeout is also configured to prevent requests from waiting indefinitely.

## 📝 Logging

Basic logging is used to track:

* Successfully fetched pages
* Number of books found
* Request errors
* CSV export status
* Scraping completion

## 🧠 What I Learned

This project helped me understand:

* Web scraping with Requests
* HTML parsing with BeautifulSoup
* CSS selectors
* Data cleaning
* Missing-value handling
* Duplicate removal
* Pandas DataFrames
* CSV export
* Pagination
* URL handling
* Functions and modular code
* Logging
* Basic error handling

## 🚀 Future Improvements

Possible improvements include:

* Exporting to Excel
* Adding retry logic
* Using a database
* Adding command-line arguments
* Creating a reusable scraper class
* Adding automated tests
* Scraping individual author information

## 📌 Learning Project

This project is part of my Web Scraping Journey and is designed to develop practical skills for real-world data extraction and freelancing projects.
