# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class HeroesPipeline(object):
    def process_item(self, item, spider):
        dic = dict(item)
        r = json.dumps(dic,ensure_ascii=False)
        with open('data.txt', 'a') as f:
            f.write(r)
        print("HeroesPipelineHeroesPipelineHeroesPipelineHeroesPipelineHeroesPipeline")
        return item
