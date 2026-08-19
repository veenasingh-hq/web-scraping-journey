class BookPipeline:

    def __init__(self):

        self.seen_urls = set()

    def process_item(self, item, spider):

        # -------------------------
        # DUPLICATE CHECK
        # -------------------------

        product_url = item.get(
            "product_url"
        )

        if product_url:

            if product_url in self.seen_urls:

                spider.logger.warning(
                    f"Duplicate skipped: {product_url}"
                )

                return item

            self.seen_urls.add(
                product_url
            )

        # -------------------------
        # TITLE CLEANING
        # -------------------------

        if item.get("title"):

            item["title"] = (
                item["title"].strip()
            )

        else:

            item["title"] = "N/A"

            spider.logger.warning(
                "Missing book title"
            )

        # -------------------------
        # AVAILABILITY CLEANING
        # -------------------------

        if item.get("availability"):

            item["availability"] = (
                item["availability"].strip()
            )

        else:

            item["availability"] = "N/A"

        # -------------------------
        # PRICE VALIDATION
        # -------------------------

        price = item.get("price")

        if price is not None:

            if not isinstance(
                price,
                (int, float)
            ):

                spider.logger.warning(
                    f"Invalid price: {price}"
                )

                item["price"] = None

        else:

            spider.logger.warning(
                f"Price missing: "
                f"{item.get('title')}"
            )

        # -------------------------
        # PRODUCT URL VALIDATION
        # -------------------------

        if not product_url:

            spider.logger.warning(
                f"Product URL missing: "
                f"{item.get('title')}"
            )

        return item