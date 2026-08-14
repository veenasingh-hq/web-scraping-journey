import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

# Starting URL
url = "https://quotes.toscrape.com/"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

# CSV file
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "quote",
        "author",
        "author_url",
        "tags"
    ])

    # Pagination loop
    while url:

        print(f"Scraping: {url}")

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print("Request Error:", e)
            break

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.select("div.quote")

        for quote in quotes:

            text = quote.select_one(
                "span.text"
            ).get_text(strip=True)

            author = quote.select_one(
                "small.author"
            ).get_text(strip=True)

            author_url = quote.select_one(
                "span a"
            )["href"]

            author_url = urljoin(
                url,
                author_url
            )

            tags = [
                tag.get_text(strip=True)
                for tag in quote.select("a.tag")
            ]

            writer.writerow([
                text,
                author,
                author_url,
                ", ".join(tags)
            ])

        # Next page
        next_button = soup.select_one(
            "li.next a"
        )

        if next_button:
            next_url = next_button.get("href")

            url = urljoin(
                url,
                next_url
            )
        else:
            url = None

print("Scraping completed!")