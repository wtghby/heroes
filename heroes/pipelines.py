# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from heroes.db.mysql import Mysql


class HeroesPipeline(object):
    def __init__(self):
        self.mysql = Mysql()

    def open_spider(self, spider):
        self.mysql.connect()

    def process_item(self, item, spider):
        self.mysql.insert(item)
        return item

    def close_spider(self, spider):
        self.mysql.close()
