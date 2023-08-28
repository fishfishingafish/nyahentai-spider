import scrapy
from scrapy import Field


class NyaspiderItem(scrapy.Item):
    pages = scrapy.Field()
    title = scrapy.Field()
    
    file_urls = scrapy.Field()
    files = scrapy.Field()
    
    pass
