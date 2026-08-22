# 🚀 Day 11 — Lead Generation Scraper

A client-style lead generation scraping project that demonstrates how publicly accessible web data can be collected, cleaned, deduplicated, and exported into CSV and Excel formats.

## 🌐 Practice Website

https://quotes.toscrape.com/

This project uses a scraping-friendly practice website to simulate a lead-generation workflow.

The extracted quote-author information is transformed into a demo lead-style dataset.

## 🎯 Project Goal

The workflow is:

```text
Public Web Data
      ↓
   Scraper
      ↓
Data Extraction
      ↓
 Data Cleaning
      ↓
Deduplication
      ↓
CSV + Excel
```

## 📊 Data Fields

The project generates the following fields:

* Name
* Category
* Location
* Website

Because this is a demo project, `Location` and the business context are simulated rather than representing real businesses.

## ✨ Features

* HTTP requests using Requests
* BeautifulSoup HTML parsing
* Automatic pagination
* Structured data extraction
* Data cleaning
* Missing-value handling
* Duplicate detection
* Data validation
* CSV export
* Excel export
* Basic error handling
* User-Agent header

## 🛠️ Technologies

* Python
* Requests
* BeautifulSoup
* Pandas
* OpenPyXL

## 📁 Project Structure

```text
day11_lead_generation/
│
├── scraper.py
├── data/
│   ├── leads.csv
│   └── leads.xlsx
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run:

```bash
python scraper.py
```

The scraper will:

1. Request the webpage
2. Extract records
3. Follow pagination
4. Clean the data
5. Remove duplicates
6. Validate the dataset
7. Export CSV
8. Export Excel

## 📦 Output

The scraper creates:

```text
data/leads.csv
data/leads.xlsx
```

### CSV

The CSV contains:

```text
name
category
location
website
```

### Excel

The Excel file contains the same structured data in `.xlsx` format.

## 🔄 Pagination

The scraper automatically follows the next-page link.

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

No page numbers need to be manually entered.

## 🧹 Data Cleaning

Text fields are stripped of unnecessary whitespace.

Missing values are replaced with:

```text
N/A
```

This prevents missing data from causing unexpected failures later in the workflow.

## 🔁 Deduplication

Duplicate records are removed using:

```python
df.drop_duplicates(
    subset=["name", "website"]
)
```

Using a combination of fields is useful because a single field may not always uniquely identify a record.

## 🔍 Data Validation

Before exporting, the scraper checks:

* Total records
* Missing values
* Duplicate records

Example:

```python
df.isnull().sum()
```

and:

```python
df.duplicated(
    subset=["name", "website"]
).sum()
```

## 💼 Real Client Workflow

For an actual lead-generation project, the requirements should be clarified before scraping.

### Source

Which website or authorized data source should be used?

### Location

Which city, country, or region?

### Category

Which type of businesses?

### Fields

For example:

* Business name
* Category
* Website
* Public business address
* Public business phone

### Output

Possible formats:

* CSV
* Excel
* JSON
* Database

### Frequency

* One-time extraction
* Weekly
* Daily
* Scheduled updates

## ⚖️ Responsible Data Collection

This project uses a dedicated practice website.

For real client work:

* Verify that automated access is permitted.
* Prefer an official or authorized API when available.
* Respect applicable terms and access rules.
* Collect only the fields required for the project.
* Avoid collecting private or restricted personal information.
* Do not bypass authentication, CAPTCHA, or other access controls.
* Use reasonable request rates.

## 🧠 What I Learned

* Lead-generation workflow
* Structured schema design
* HTML parsing
* Pagination
* Data cleaning
* Deduplication
* Data validation
* CSV export
* Excel export
* Error handling
* Client requirement analysis

## 🚀 Future Improvements

Possible improvements:

* Add database storage
* Add logging
* Add configurable request delays
* Add automated tests
* Add email/domain validation
* Add scheduled scraping
* Build a reusable scraping framework
* Connect authorized APIs

## 📌 Learning Project

Part of my Web Scraping Journey, focused on developing practical scraping, data-processing, and client-delivery skills.
