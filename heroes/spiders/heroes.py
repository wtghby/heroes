# -*- coding: utf-8 -*-
import scrapy
from heroes.items import Stock
from urllib import parse as urlparse


class heroes(scrapy.Spider):
    name = "heroes"
    start_urls = ["http://data.10jqka.com.cn/market/longhu"]
    allowed_domains = ['data.10jqka.com.cn']

    def parse(self, response):
        # 获取所有table节点
        datas = response.xpath('//div[@class="twrap"]/table/tbody/child::*')
        i = 1
        for data in datas:
            item = Stock.Stock()
            item['code'] = data.xpath(self.get_path(i, 2)).extract_first()
            item['name'] = data.xpath(self.get_path(i, 3)).extract_first()
            item['price'] = data.xpath(self.get_path(i, 4)).extract_first()
            item['increase'] = data.xpath(self.get_path(i, 5)).extract_first()
            item['deal'] = data.xpath(self.get_path(i, 6)).extract_first()
            item['buy'] = data.xpath(self.get_path(i, 7)).extract_first()
            i += 1
            print(item['code'])
            print(item['name'])
            print(item['price'])
            print(item['increase'])
            print(item['deal'])
            print(item['buy'])

    def get_path(self, row, col):
        if col == 3:
            return '//div[@class="twrap"]/table/tbody//tr[' + str(row) + ']/td[' + str(col) + ']/a/text()'
        return '//div[@class="twrap"]/table/tbody//tr[' + str(row) + ']/td[' + str(col) + ']/text()'
