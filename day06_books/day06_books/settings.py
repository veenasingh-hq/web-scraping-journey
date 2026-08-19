BOT_NAME = "day06_books"

SPIDER_MODULES = ["day06_books.spiders"]

NEWSPIDER_MODULE = "day06_books.spiders"


# -------------------------
# ROBOTS
# -------------------------

ROBOTSTXT_OBEY = True


# -------------------------
# REQUEST SETTINGS
# -------------------------

DOWNLOAD_TIMEOUT = 20

DOWNLOAD_DELAY = 1

CONCURRENT_REQUESTS_PER_DOMAIN = 4

USER_AGENT = "day06-books-learning-scraper"


# -------------------------
# RETRY
# -------------------------

RETRY_ENABLED = True

RETRY_TIMES = 2


# -------------------------
# AUTOTHROTTLE
# -------------------------

AUTOTHROTTLE_ENABLED = True

AUTOTHROTTLE_START_DELAY = 1

AUTOTHROTTLE_MAX_DELAY = 10

AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0


# -------------------------
# PIPELINE
# -------------------------

ITEM_PIPELINES = {
    "day06_books.pipelines.BookPipeline": 300,
}


# -------------------------
# ENCODING
# -------------------------

FEED_EXPORT_ENCODING = "utf-8"