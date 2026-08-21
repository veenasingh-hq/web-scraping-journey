import requests
import pandas as pd

from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"


def fetch_page(url):
    """Fetch webpage HTML."""

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


def clean_price(price):
    """Convert price from £51.77 to 51.77."""

    try:

        return float(
            price.replace("£", "").strip()
        )

    except (AttributeError, ValueError):

        return None


def parse_products(html, current_url):
    """Extract products from one page."""

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    products = []

    books = soup.select(
        "article.product_pod"
    )

    for book in books:

        # -------------------------
        # TITLE
        # -------------------------

        title_element = book.select_one(
            "h3 a"
        )

        if title_element:

            title = title_element.get(
                "title",
                "N/A"
            ).strip()

        else:

            title = "N/A"


        # -------------------------
        # PRICE
        # -------------------------

        price_element = book.select_one(
            ".price_color"
        )

        if price_element:

            raw_price = price_element.get_text(
                strip=True
            )

            price = clean_price(
                raw_price
            )

        else:

            price = None


        # -------------------------
        # RATING
        # -------------------------

        rating_element = book.select_one(
            "p.star-rating"
        )

        if rating_element:

            classes = rating_element.get(
                "class",
                []
            )

            if len(classes) > 1:

                rating = classes[-1]

            else:

                rating = "N/A"

        else:

            rating = "N/A"


        # -------------------------
        # AVAILABILITY
        # -------------------------

        availability_element = (
            book.select_one(
                ".availability"
            )
        )

        if availability_element:

            availability = (
                availability_element
                .get_text(
                    " ",
                    strip=True
                )
            )

        else:

            availability = "N/A"


        # -------------------------
        # PRODUCT URL
        # -------------------------

        link_element = book.select_one(
            "h3 a"
        )

        if link_element:

            relative_url = link_element.get(
                "href"
            )

            product_url = urljoin(
                current_url,
                relative_url
            )

        else:

            product_url = None


        # -------------------------
        # STORE PRODUCT
        # -------------------------

        products.append({

            "title": title,

            "price": price,

            "rating": rating,

            "availability": availability,

            "product_url": product_url

        })

    return products


def clean_data(products):
    """Clean and validate scraped data."""

    cleaned_products = []

    seen_urls = set()

    for product in products:

        product_url = product.get(
            "product_url"
        )

        # Duplicate check
        if product_url in seen_urls:

            continue

        if product_url:

            seen_urls.add(
                product_url
            )

        # Title validation
        if not product.get("title"):

            product["title"] = "N/A"

        # Rating validation
        if not product.get("rating"):

            product["rating"] = "N/A"

        # Availability validation
        if not product.get(
            "availability"
        ):

            product["availability"] = "N/A"

        cleaned_products.append(
            product
        )

    return cleaned_products


def scrape_all_products():
    """Scrape all product pages."""

    all_products = []

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

            print(
                "Stopping scraper because "
                "the request failed."
            )

            break

        products = parse_products(
            html,
            current_url
        )

        print(
            f"Products found: "
            f"{len(products)}"
        )

        all_products.extend(
            products
        )

        # Parse next page
        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        next_link = soup.select_one(
            "li.next a"
        )

        if next_link:

            relative_next_url = (
                next_link.get("href")
            )

            current_url = urljoin(
                current_url,
                relative_next_url
            )

            page_number += 1

        else:

            current_url = None

    return all_products


def save_data(products):
    """Save products to CSV and JSON."""

    df = pd.DataFrame(products)

    # Create data directory if needed
    import os

    os.makedirs(
        "data",
        exist_ok=True
    )

    # -------------------------
    # VALIDATION
    # -------------------------

    print("\n--- Data Validation ---")

    print(
        "Total records:",
        len(df)
    )

    print(
        "\nMissing values:"
    )

    print(
        df.isnull().sum()
    )

    print(
        "\nDuplicate records:",
        df.duplicated().sum()
    )

    # -------------------------
    # CSV
    # -------------------------

    df.to_csv(
        "data/products.csv",
        index=False
    )

    # -------------------------
    # JSON
    # -------------------------

    df.to_json(
        "data/products.json",
        orient="records",
        indent=4
    )

    print(
        "\nCSV saved:"
        " data/products.csv"
    )

    print(
        "JSON saved:"
        " data/products.json"
    )


def main():

    print("=" * 60)
    print("E-COMMERCE PRODUCT SCRAPER")
    print("=" * 60)

    products = scrape_all_products()

    print(
        f"\nRaw products collected: "
        f"{len(products)}"
    )

    products = clean_data(
        products
    )

    print(
        f"Clean products: "
        f"{len(products)}"
    )

    save_data(
        products
    )

    print(
        "\nScraping completed successfully!"
    )


if __name__ == "__main__":

    main()