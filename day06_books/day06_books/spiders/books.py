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

        books = response.css(
            "article.product_pod"
        )

        self.logger.info(
            f"Books found: {len(books)}"
        )

        for book in books:

            item = BookItem()

            # -------------------------
            # Title
            # -------------------------

            item["title"] = book.css(
                "h3 a::attr(title)"
            ).get()

            # -------------------------
            # Price
            # -------------------------

            price = book.css(
                ".price_color::text"
            ).get()

            if price:

                price = price.replace(
                    "£",
                    ""
                ).strip()

                try:
                    price = float(price)

                except ValueError:
                    price = None

            item["price"] = price

            # -------------------------
            # Rating
            # -------------------------

            rating_classes = book.css(
                "p.star-rating::attr(class)"
            ).get()

            if rating_classes:

                rating_parts = (
                    rating_classes.split()
                )

                if len(rating_parts) > 1:

                    item["rating"] = (
                        rating_parts[1]
                    )

                else:

                    item["rating"] = None

            else:

                item["rating"] = None

            # -------------------------
            # Availability
            # -------------------------

            availability = book.css(
                ".availability::text"
            ).getall()

            item["availability"] = " ".join(
                text.strip()
                for text in availability
                if text.strip()
            )

            # -------------------------
            # Product URL
            # -------------------------

            relative_url = book.css(
                "h3 a::attr(href)"
            ).get()

            item["product_url"] = (
                response.urljoin(
                    relative_url
                )
            )

            yield item

        # -------------------------
        # Pagination
        # -------------------------

        next_page = response.css(
            "li.next a::attr(href)"
        ).get()

        if next_page:

            yield response.follow(
                next_page,
                callback=self.parse
            )