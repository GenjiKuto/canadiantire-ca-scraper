thonfrom scraper import CanadiantireScraper

class CategoryExtractor:
    def __init__(self, base_url):
        self.scraper = CanadiantireScraper(base_url)

    def extract_category_data(self, category_url):
        return self.scraper.scrape_category(category_url)