# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..item.MovieItem import MovieItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['diaomie.com']
    start_urls = ['http://www.diaomie.com/']

    rules = (
        Rule(LinkExtractor(allow=(r'.*tv-list-id.*'))),
        Rule(LinkExtractor(allow=(r'.*tv-type-id.*'))),
        Rule(LinkExtractor(allow=(r'.*tv-detail-id.*')), callback='parse_item'),
    )

    def parse_item(self, response):
        i = MovieItem()
        i['name'] = response.css('.detail-title h2::text').extract()
        i['actor'] = ','.join(response.css('.detail-info dl')[0].css('a::text').extract())
        i['type'] = response.css('.detail-info dl')[2].css('a::text').extract()
        i['country'] = response.css('.detail-info dl')[3].css('a::text').extract()
        i['label'] = ','.join(response.css('.detail-info dl')[4].css('a::text').extract())
        i['director'] = response.css('.detail-info dl')[5].css('a::text').extract()
        yield i
