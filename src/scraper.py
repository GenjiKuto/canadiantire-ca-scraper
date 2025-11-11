thonimport requests
from bs4 import BeautifulSoup
import json
import time

class CanadiantireScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_soup(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        return BeautifulSoup(response.content, 'html.parser')

    def scrape_product(self, product_url):
        soup = self.get_soup(product_url)
        title = soup.find('h1', {'class': 'product-title'}).text.strip()
        price = soup.find('span', {'class': 'price'}).text.strip()
        description = soup.find('div', {'class': 'product-description'}).text.strip()
        rating = soup.find('span', {'class': 'average-rating'}).text.strip()
        availability = soup.find('span', {'class': 'availability'}).text.strip()
        image_urls = [img['src'] for img in soup.find_all('img', {'class': 'product-image'})]

        return {
            'title': title,
            'description': description,
            'price': price,
            'availability': availability,
            'rating': rating,
            'image_urls': image_urls
        }

    def scrape_category(self, category_url):
        soup = self.get_soup(category_url)
        products = soup.find_all('a', {'class': 'product-link'})
        product_urls = [product['href'] for product in products]

        product_data = []
        for url in product_urls:
            product_data.append(self.scrape_product(url))
            time.sleep(1)

        return product_data

    def scrape(self, start_url):
        return self.scrape_category(start_url)