# -*- coding: utf-8 -*-
import scrapy


class Department(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 买入金额
    rise = scrapy.Field()
    # 卖出金额
    fall = scrapy.Field()
    # 买卖净额
    total = scrapy.Field()
