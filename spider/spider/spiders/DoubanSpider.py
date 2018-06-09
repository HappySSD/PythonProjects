from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import MovieItem


class DdoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/chart']

    rules = (
        Rule(LinkExtractor(allow=(r'.*type_name.*'))),
        Rule(LinkExtractor(allow=(r'.*/subject/\d+.*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        item = MovieItem()
        item['name'] = response.css("#content span::text")[0].extract()
        return item