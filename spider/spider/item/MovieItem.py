import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    actor = scrapy.Field()
    type = scrapy.Field()
    country = scrapy.Field()
    label = scrapy.Field()
    director = scrapy.Field()
