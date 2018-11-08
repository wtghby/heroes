# -*- coding: utf-8 -*-
import scrapy

class Stock(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    increase = scrapy.Field()
    deal = scrapy.Field()
    buy = scrapy.Field()
