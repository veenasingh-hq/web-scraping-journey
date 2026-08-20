import time
import requests


URL = "https://quotes.toscrape.com/"


def fetch_page(url, headers=None):
    """
    Fetch a webpage with timeout and error handling.
    """

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response

    except requests.Timeout:
        print("Request timed out.")

    except requests.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.RequestException as error:
        print(f"Request failed: {error}")

    return None


def basic_request():
    """
    Make a basic HTTP request.
    """

    print("\n--- Basic Request ---")

    response = fetch_page(URL)

    if response:

        print("Status Code:", response.status_code)
        print("URL:", response.url)
        print("Content Length:", len(response.text))


def request_with_headers():
    """
    Make a request with a User-Agent header.
    """

    print("\n--- Request With Headers ---")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = fetch_page(
        URL,
        headers=headers
    )

    if response:

        print("Status Code:", response.status_code)
        print("Content Length:", len(response.text))

        print("\nSelected Response Headers:")

        print(
            "Content-Type:",
            response.headers.get("Content-Type")
        )

        print(
            "Content-Length:",
            response.headers.get("Content-Length")
        )


def session_request():
    """
    Create a requests session and inspect cookies.
    """

    print("\n--- Session Request ---")

    session = requests.Session()

    session.headers.update({
        "User-Agent": "Mozilla/5.0"
    })

    try:

        response = session.get(
            URL,
            timeout=10
        )

        response.raise_for_status()

        print(
            "Status Code:",
            response.status_code
        )

        print(
            "Session Cookies:",
            session.cookies
        )

        print(
            "Response Cookies:",
            response.cookies
        )

    except requests.Timeout:

        print("Session request timed out.")

    except requests.HTTPError as error:

        print(f"HTTP error: {error}")

    except requests.RequestException as error:

        print(f"Request failed: {error}")

    finally:

        session.close()


def compare_requests():
    """
    Compare a request without headers
    and a request with headers.
    """

    print("\n--- Comparing Requests ---")

    # Request A
    response_a = requests.get(
        URL,
        timeout=10
    )

    # Small delay between requests
    time.sleep(1)

    # Request B
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response_b = requests.get(
        URL,
        headers=headers,
        timeout=10
    )

    print("\nRequest A")
    print("Status:", response_a.status_code)
    print(
        "Length:",
        len(response_a.text)
    )

    print("\nRequest B")
    print("Status:", response_b.status_code)
    print(
        "Length:",
        len(response_b.text)
    )


def main():

    print("=" * 50)
    print("DAY 8 - REQUEST HANDLING")
    print("=" * 50)

    basic_request()

    request_with_headers()

    session_request()

    compare_requests()

    print("\nDay 8 request handling completed.")


if __name__ == "__main__":
    main()