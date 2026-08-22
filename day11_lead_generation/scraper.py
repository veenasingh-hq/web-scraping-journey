import os
import requests
import pandas as pd

from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://quotes.toscrape.com/"


def fetch_page(url):
    """Fetch HTML from a webpage."""

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        return response.text

    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return None


def parse_page(html, current_url):
    """Extract lead-style records from one page."""

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    records = []

    quotes = soup.select(".quote")

    for quote in quotes:

        # Name
        author_element = quote.select_one(
            ".author"
        )

        if author_element:
            name = author_element.get_text(
                strip=True
            )
        else:
            name = "N/A"

        # Category
        tags = [
            tag.get_text(strip=True)
            for tag in quote.select(".tag")
        ]

        category = ", ".join(tags)

        if not category:
            category = "N/A"

        # Demo location
        location = "Demo"

        # Source website
        website = current_url

        records.append({
            "name": name,
            "category": category,
            "location": location,
            "website": website
        })

    return records


def scrape_all_pages():
    """Scrape all pages automatically."""

    all_records = []

    current_url = BASE_URL

    page_number = 1

    while current_url:

        print(
            f"Scraping page {page_number}: "
            f"{current_url}"
        )

        html = fetch_page(
            current_url
        )

        if not html:
            print("Stopping scraper.")
            break

        records = parse_page(
            html,
            current_url
        )

        print(
            f"Records found: "
            f"{len(records)}"
        )

        all_records.extend(records)

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        next_link = soup.select_one(
            "li.next a"
        )

        if next_link:

            current_url = urljoin(
                current_url,
                next_link.get("href")
            )

            page_number += 1

        else:

            current_url = None

    return all_records


def clean_data(records):
    """Clean and deduplicate records."""

    df = pd.DataFrame(records)

    if df.empty:
        return df

    # Clean text
    df["name"] = (
        df["name"]
        .fillna("N/A")
        .astype(str)
        .str.strip()
    )

    df["category"] = (
        df["category"]
        .fillna("N/A")
        .astype(str)
        .str.strip()
    )

    df["location"] = (
        df["location"]
        .fillna("N/A")
        .astype(str)
        .str.strip()
    )

    df["website"] = (
        df["website"]
        .fillna("N/A")
        .astype(str)
        .str.strip()
    )

    # Remove duplicates
    before = len(df)

    df = df.drop_duplicates(
        subset=["name", "website"]
    )

    after = len(df)

    print(
        f"Duplicates removed: "
        f"{before - after}"
    )

    return df


def save_data(df):
    """Save data as CSV and Excel."""

    os.makedirs(
        "data",
        exist_ok=True
    )

    # CSV
    df.to_csv(
        "data/leads.csv",
        index=False,
        encoding="utf-8"
    )

    # Excel
    df.to_excel(
        "data/leads.xlsx",
        index=False
    )

    print(
        "\nCSV saved: data/leads.csv"
    )

    print(
        "Excel saved: data/leads.xlsx"
    )


def validate_data(df):
    """Display basic data validation information."""

    print("\n--- Data Validation ---")

    print(
        "Total records:",
        len(df)
    )

    print("\nMissing values:")

    print(
        df.isnull().sum()
    )

    print(
        "\nDuplicate records:",
        df.duplicated(
            subset=["name", "website"]
        ).sum()
    )


def main():

    print("=" * 60)
    print("DAY 11 - LEAD GENERATION SCRAPER")
    print("=" * 60)

    records = scrape_all_pages()

    print(
        f"\nRaw records collected: "
        f"{len(records)}"
    )

    df = clean_data(
        records
    )

    if df.empty:

        print(
            "No data collected."
        )

        return

    validate_data(
        df
    )

    save_data(
        df
    )

    print(
        "\nScraping completed successfully!"
    )


if __name__ == "__main__":
    main()