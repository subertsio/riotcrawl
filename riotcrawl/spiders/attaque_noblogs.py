import scrapy


class AttaqueNoblogsSpider(scrapy.Spider):
    name = 'attaque_noblogs'
    allowed_domains = ['attaque.noblogs.org']
    start_urls = ['http://attaque.noblogs.org/']

    def parse(self, response):
        pass
