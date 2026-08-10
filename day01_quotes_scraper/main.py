import requests
from bs4 import BeautifulSoup
import csv


url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Website connected successfully!")

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Quote", "Author"])

        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)

            writer.writerow([text, author])

    print(f"{len(quotes)} quotes saved to quotes.csv")

else:
    print("Failed to access website")
    print("Status Code:", response.status_code)