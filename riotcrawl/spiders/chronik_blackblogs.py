'''
Scraper for 
https://chronik.blackblogs.org
'''

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from riotcrawl.items import RiotPost


class ChronikBlackblogsSpider(CrawlSpider):
    ''' Spider for:
            < https://chronik.blackblogs.org >

    Basically we try to scrape all posts.

    Attributes
    ----------
    name : str
        Name of the Spider.
    allowed_domains : str
        Spider can scrape from these domains.
    start_urls : str
        Start Domain for Spider.
    rules : ...
        Rules how Spider scrapes/crawls.
    '''
    name = 'chronik_blackblogs'
    allowed_domains = ['chronik.blackblogs.org']
    start_urls = ['https://chronik.blackblogs.org/']
    rules = [
        Rule(
            LinkExtractor(
                restrict_css=(
                    'div.hentry',
                    'div.navigation-links',
                    ), 
                deny=(
                    r'/?tag=*', 
                    r'/?author=*',
                    r'/?paged=*'
                    r'/?cat=6',
                    r'/?cat=7*',
                    r'/?cat=15*',
                    r'/?cat=9*',
                    r'/?cat=16*',
                    r'/?cat=385*',
                    ),
                ), 
            callback='parse_posts', 
            follow=True,
        ),
    ]

    def parse_posts(self, response):
        ''' Parsing all Posts into 
            our RiotPost Item

        This method recieves the Response
        of the Spider and processes it.
        
        Notes
        -----
        See items.py for the posts
        and pipelines.py for how 
        data will processed after.

        Parameters
        ----------
        response : :obj: Response
            The Response of the Spiders
            Request.

        Returns
        -------
        posts : scrapy :obj: Item
            The Responses get processed
            represented by posts.
            Posts will be sent to the
            Pipelines.
        '''
        posts = RiotPost()
        posts['title'] = response.xpath('//h1[@class="post-title entry-title"]/a/text()').get()
        posts['date'] = response.xpath('//div[@class="entry-content"]/p/text()').get()
        posts['location'] = response.xpath('//div[@class="entry-content"]/p/strong/text()').get()
        posts['content'] = response.xpath('//blockquote/p/text()').getall()
        posts['language'] = response.xpath('//span[@class="category"]/a/text()').get()
        posts['tagged'] = response.xpath('//span[@class="post_tag"]/a/text()').get()
        posts['link'] = response.url
        posts['scraped_by'] = self.name
        return posts

