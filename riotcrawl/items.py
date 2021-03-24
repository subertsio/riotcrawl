''' Post Items

Items represent the scraped Data
of our Spiders.
'''

import scrapy


class RiotPost(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    content = scrapy.Field()
    language = scrapy.Field()
    tagged = scrapy.Field()
    link = scrapy.Field()
    scraped_by = scrapy.Field()
