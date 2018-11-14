# -*- coding: utf-8 -*-
import scrapy


class Result(scrapy.Item):
    # 数据列表
    stocks = scrapy.Field()
