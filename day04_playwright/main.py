import csv
from playwright.sync_api import sync_playwright


BASE_URL = "https://quotes.toscrape.com/js/"


def create_browser(playwright):
    """Create and return a Chromium browser."""

    browser = playwright.chromium.launch(
        headless=True
    )

    return browser


def scrape_page(page):
    """Extract quotes from the current page."""

    data = []

    # Wait for JavaScript-rendered quotes
    page.locator(".quote").first.wait_for(
        state="visible"
    )

    quotes = page.locator(".quote")

    print("Quotes found:", quotes.count())

    for i in range(quotes.count()):

        quote = quotes.nth(i)

        text = quote.locator(
            ".text"
        ).inner_text()

        author = quote.locator(
            ".author"
        ).inner_text()

        tags = quote.locator(
            ".tags .tag"
        )

        tag_list = []

        for j in range(tags.count()):
            tag_list.append(
                tags.nth(j).inner_text()
            )

        data.append({
            "quote": text,
            "author": author,
            "tags": ", ".join(tag_list)
        })

    return data


def save_data(data):
    """Save scraped data to CSV."""

    with open(
        "quotes_dynamic.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "quote",
                "author",
                "tags"
            ]
        )

        writer.writeheader()
        writer.writerows(data)

    print(
        f"Saved {len(data)} quotes to quotes_dynamic.csv"
    )


def main():

    all_data = []

    with sync_playwright() as playwright:

        browser = create_browser(
            playwright
        )

        page = browser.new_page()

        try:

            page.goto(
                BASE_URL,
                wait_until="domcontentloaded",
                timeout=30000
            )

            page.screenshot(
                path="page.png",
                full_page=True
            )

            page_number = 1

            while True:

                print(
                    f"\nScraping Page {page_number}"
                )

                page_data = scrape_page(page)

                all_data.extend(page_data)

                # Find Next button
                next_button = page.locator(
                    ".next a"
                )

                if next_button.count() == 0:
                    print(
                        "No more pages."
                    )
                    break

                next_button.click()

                # Wait for new page content
                page.locator(
                    ".quote"
                ).first.wait_for(
                    state="visible"
                )

                page_number += 1

        except Exception as error:

            print(
                f"Scraping error: {error}"
            )

            page.screenshot(
                path="error.png",
                full_page=True
            )

        finally:

            browser.close()

    save_data(all_data)


if __name__ == "__main__":
    main()


    