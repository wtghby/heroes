# -*- coding: utf-8 -*-
import scrapy


class Stock(scrapy.Item):
    # 代码
    code = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 涨幅
    increase = scrapy.Field()
    # 成交额
    deal = scrapy.Field()
    # 买入净额
    buy = scrapy.Field()
    # 上榜原因
    reason = scrapy.Field()
    # 买入金额
    rise = scrapy.Field()
    # 卖出金额
    fall = scrapy.Field()
    # 买入前5营业部
    rise_departments = scrapy.Field()
    # 卖出前5营业部
    fall_departments = scrapy.Field()
