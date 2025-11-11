thonfrom scraper import CanadiantireScraper

class ProductExtractor:
    def __init__(self, base_url):
        self.scraper = CanadiantireScraper(base_url)

    def extract_product_data(self, product_url):
        return self.scraper.scrape_product(product_url)