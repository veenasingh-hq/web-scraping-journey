import logging

import pandas as pd
import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def get_data():
    """Fetch data from the public API."""

    try:
        response = requests.get(
            API_URL,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        logging.info(
            f"Received {len(data)} records"
        )

        return data

    except requests.exceptions.RequestException as error:
        logging.error(
            f"API request failed: {error}"
        )

        return []


def process_data(data):
    """Extract required fields from API response."""

    processed_data = []

    for item in data:

        processed_data.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "body": item.get("body")
        })

    return processed_data


def save_data(data):
    """Save processed data to CSV."""

    if not data:
        logging.warning(
            "No data to save."
        )
        return

    df = pd.DataFrame(data)

    df.drop_duplicates(
        subset=["id"],
        inplace=True
    )

    df.to_csv(
        "data.csv",
        index=False,
        encoding="utf-8"
    )

    logging.info(
        f"Saved {len(df)} records to data.csv"
    )


def main():

    logging.info(
        "Starting API data extraction..."
    )

    data = get_data()

    if not data:
        return

    processed_data = process_data(
        data
    )

    save_data(
        processed_data
    )

    logging.info(
        "API extraction completed!"
    )


if __name__ == "__main__":
    main()