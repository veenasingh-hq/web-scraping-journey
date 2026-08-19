import scrapy

from day06_books.items import BookItem


class BooksSpider(scrapy.Spider):

    name = "books"

    allowed_domains = [
        "books.toscrape.com"
    ]

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):

        self.logger.info(
            f"Scraping page: {response.url}"
        )

        books = response.css(
            "article.product_pod"
        )

        self.logger.info(
            f"Books found: {len(books)}"
        )

        for book in books:

            item = BookItem()

            # -------------------------
            # TITLE
            # -------------------------

            title = book.css(
                "h3 a::attr(title)"
            ).get()

            if title:
                title = title.strip()
            else:
                title = "N/A"

                self.logger.warning(
                    f"Missing title: {response.url}"
                )

            item["title"] = title

            # -------------------------
            # PRICE
            # -------------------------

            price = book.css(
                ".price_color::text"
            ).get()

            if price:

                price = price.replace(
                    "£", ""
                ).strip()

                try:
                    price = float(price)

                except ValueError:

                    self.logger.warning(
                        f"Invalid price: {price}"
                    )

                    price = None

            else:

                self.logger.warning(
                    f"Missing price: {response.url}"
                )

                price = None

            item["price"] = price

            # -------------------------
            # RATING
            # -------------------------

            rating_classes = book.css(
                "p.star-rating::attr(class)"
            ).get()

            if rating_classes:

                rating_parts = (
                    rating_classes.split()
                )

                if len(rating_parts) > 1:
                    rating = rating_parts[1]
                else:
                    rating = "N/A"

            else:

                self.logger.warning(
                    f"Missing rating: {response.url}"
                )

                rating = "N/A"

            item["rating"] = rating

            # -------------------------
            # AVAILABILITY
            # -------------------------

            availability = book.css(
                ".availability::text"
            ).getall()

            availability = " ".join(
                text.strip()
                for text in availability
                if text.strip()
            )

            if not availability:
                availability = "N/A"

            item["availability"] = availability

            # -------------------------
            # PRODUCT URL
            # -------------------------

            relative_url = book.css(
                "h3 a::attr(href)"
            ).get()

            if relative_url:

                product_url = response.urljoin(
                    relative_url
                )

            else:

                self.logger.warning(
                    f"Missing product URL: {response.url}"
                )

                product_url = None

            item["product_url"] = product_url

            # Send item to pipeline
            yield item

        # -------------------------
        # PAGINATION
        # -------------------------

        next_page = response.css(
            "li.next a::attr(href)"
        ).get()

        if next_page:

            self.logger.info(
                f"Following next page: {next_page}"
            )

            yield response.follow(
                next_page,
                callback=self.parse
            )

        else:

            self.logger.info(
                "No next page. Crawling completed."
            )