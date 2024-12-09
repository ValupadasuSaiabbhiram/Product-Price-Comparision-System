import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0 Safari/537.36"
        }

    def get_page_content(self, query):
        search_url = self.base_url.format(query=query.replace(" ", "+"))
        response = requests.get(search_url, headers=self.headers)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

class AmazonScraper(Scraper):
    def __init__(self):
        super().__init__("https://www.amazon.in/s?k={query}")

    def parse_page(self, content):
        soup = BeautifulSoup(content, "html.parser")
        products = []
        for item in soup.select(".s-main-slot .s-result-item"):
            name = item.select_one("span.a-text-normal")
            price = item.select_one("span.a-price-whole")
            link = item.select_one("a.a-link-normal")
            if name and price and link:
                products.append({
                    "name": name.text.strip(),
                    "price": float(price.text.replace(",", "").strip()),
                    "link": "https://www.amazon.in" + link['href']
                })
        return products
