import scrapy


class BookSpiderSpider(scrapy.Spider):
    name = "book-spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
