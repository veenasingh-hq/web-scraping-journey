import logging
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# -----------------------------
# Logging Configuration
# -----------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# -----------------------------
# Get Page
# -----------------------------

def get_page(url):
    """Fetch a webpage and return BeautifulSoup object."""

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        logging.info(f"Successfully fetched: {url}")

        return BeautifulSoup(
            response.text,
            "html.parser"
        )

    except requests.exceptions.RequestException as error:
        logging.error(f"Request failed: {error}")
        return None


# -----------------------------
# Parse Books
# -----------------------------

def parse_books(soup, current_url):
    """Extract book information from a page."""

    data = []

    books = soup.select("article.product_pod")

    for book in books:

        # Title
        title_element = book.select_one("h3 a")

        title = title_element.get("title", "").strip()

        # Price
        price_element = book.select_one("p.price_color")

        price = price_element.get_text(strip=True)

        price = price.replace("£", "")

        try:
            price = float(price)
        except ValueError:
            price = None

        # Rating
        rating_element = book.select_one(
            "p.star-rating"
        )

        rating_classes = rating_element.get(
            "class",
            []
        )

        rating = (
            rating_classes[1]
            if len(rating_classes) > 1
            else None
        )

        # Availability
        availability_element = book.select_one(
            "p.instock"
        )

        availability = (
            availability_element.get_text(
                " ",
                strip=True
            )
            if availability_element
            else None
        )

        # Product URL
        product_url = title_element.get("href")

        product_url = urljoin(
            current_url,
            product_url
        )

        # Store data
        data.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "url": product_url
        })

    logging.info(
        f"Books found on page: {len(data)}"
    )

    return data


# -----------------------------
# Save Data
# -----------------------------

def save_to_csv(data):
    """Clean data and save it to CSV."""

    if not data:
        logging.warning("No data to save.")
        return

    df = pd.DataFrame(data)

    # Remove duplicate books
    df.drop_duplicates(
        subset=["url"],
        inplace=True
    )

    # Clean text columns
    df["title"] = (
        df["title"]
        .fillna("")
        .str.strip()
    )

    df["availability"] = (
        df["availability"]
        .fillna("")
        .str.strip()
    )

    df["rating"] = (
        df["rating"]
        .fillna("Unknown")
        .str.strip()
    )

    # Remove missing URLs
    df = df[
        df["url"].notna()
        & (df["url"] != "")
    ]

    # Save CSV
    df.to_csv(
        "books.csv",
        index=False,
        encoding="utf-8"
    )

    logging.info(
        f"Saved {len(df)} books to books.csv"
    )


# -----------------------------
# Main Scraper
# -----------------------------

def main():

    url = BASE_URL

    all_books = []

    while url:

        soup = get_page(url)

        if soup is None:
            break

        # Extract books
        books = parse_books(
            soup,
            url
        )

        all_books.extend(books)

        # Find next page
        next_button = soup.select_one(
            "li.next a"
        )

        if next_button:

            next_url = next_button.get(
                "href"
            )

            url = urljoin(
                url,
                next_url
            )

        else:

            url = None

    # Save everything
    save_to_csv(all_books)

    logging.info(
        "Scraping completed successfully!"
    )


# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    main()