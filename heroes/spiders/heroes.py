# -*- coding: utf-8 -*-
import scrapy
from heroes.items import Stock
from heroes.items import Department
from heroes.items import Result
from urllib import parse as urlparse


class heroes(scrapy.Spider):
    name = "heroes"
    start_urls = ["http://data.10jqka.com.cn/market/longhu"]
    allowed_domains = ['data.10jqka.com.cn']

    def parse(self, response):
        # -----------获取当日龙虎榜列表--------------------------
        # 获取所有table节点
        datas = response.xpath('//div[@class="twrap"]/table/tbody/child::*')
        i = 1
        stocks = []
        for data in datas:
            item = Stock.Stock()
            item['code'] = data.xpath(self.get_path(i, 2)).extract_first()
            item['name'] = data.xpath(self.get_path(i, 3)).extract_first()
            item['price'] = data.xpath(self.get_path(i, 4)).extract_first()
            item['increase'] = data.xpath(self.get_path(i, 5)).extract_first()
            item['deal'] = data.xpath(self.get_path(i, 6)).extract_first()
            item['buy'] = data.xpath(self.get_path(i, 7)).extract_first()
            stocks.append(item)
            i += 1
            # print(item['code'])
            # print(item['name'])
            # print(item['price'])
            # print(item['increase'])
            # print(item['deal'])
            # print(item['buy'])
        # -----------获取当日龙虎榜列表--------------------------
        # print(stocks)
        details = response.xpath('//div[@class="rightcol fr"]//@stockcode').extract()
        # 类型名称：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][1]/p/text()').extract_first()
        # 成交额：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"]/div[@class="cell-cont cjmx"]/p[@style="padding: 7px 0;"]/text()').extract_first()
        # 合计买入：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"]/div[@class="cell-cont cjmx"]/p[@style="padding: 7px 0;"]/span[@class="c-rise"]/text()').extract_first()
        # 合计卖出：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"]/div[@class="cell-cont cjmx"]/p[@style="padding: 7px 0;"]/span[@class="c-fall"][1]/text()').extract_first()
        # 净额：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"]/div[@class="cell-cont cjmx"]/p[@style="padding: 7px 0;"]/span[@class="c-fall"][2]/text()').extract_first()

        # 营业部名称：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"]/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"]/tbody/tr/td[@class="tl rel"]//@title').extract_first()
        # 买入额：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"]/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"]/tbody/tr/td[@class="c-rise tr rel"][1]/text()').extract_first()
        # 卖出额：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"]/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"]/tbody/tr/td[@class="c-fall tr rel"]/text()').extract_first()
        # 买卖净额：xpath('//div[@class="rightcol fr"]/div[@class="stockcont"]/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"]/tbody/tr/td[@class="c-rise tr rel"][2]/text()').extract_first()
        j = 1
        for detail in details:
            stock_code = detail
            item = self.get_item_by_code(stocks, stock_code)
            detail_title = response.xpath(
                '//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(j) + ']/p/text()').extract_first()
            total_deal = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                j) + ']/div[@class="cell-cont cjmx"]/p[@style="padding: 7px 0;"]/text()').extract_first()
            total_rise = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                j) + ']/div[@class="cell-cont cjmx"]/p[@style="padding: 7px 0;"]/span[1]/text()').extract_first()
            total_sell = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                j) + ']/div[@class="cell-cont cjmx"]/p[@style="padding: 7px 0;"]/span[2]/text()').extract_first()
            total_amount = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                j) + ']/div[@class="cell-cont cjmx"]/p[@style="padding: 7px 0;"]/span[3]/text()').extract_first()

            item['reason'] = detail_title
            item['rise'] = total_rise
            item['fall'] = total_sell

            # 买入营业部前5
            k = 1
            red_departments = []
            # red_departments_rise = [5]
            # red_departments_fall = [5]
            # red_departments_total = [5]

            while k < 6:
                department = Department.Department()
                red_department = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                    j) + ']/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"][1]/tbody/tr[' + str(
                    k) + ']/td[@class="tl rel"]//@title').extract_first()
                department['name'] = red_department
                # red_departments.append(red_department)
                red_department_rise = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                    j) + ']/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"][1]/tbody/tr[' + str(
                    k) + ']/td[2]/text()').extract_first()
                department['rise'] = red_department_rise
                # red_departments_rise.append(red_department_rise)
                red_department_fall = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                    j) + ']/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"][1]/tbody/tr[' + str(
                    k) + ']/td[3]/text()').extract_first()
                department['fall'] = red_department_fall
                # red_departments_fall.append(red_department_fall)
                red_department_total = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                    j) + ']/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"][1]/tbody/tr[' + str(
                    k) + ']/td[4]/text()').extract_first()
                department['total'] = red_department_total
                # red_departments_total.append(red_department_total)
                # print(red_departments[k])
                red_departments.append(department)
                k += 1

            # 卖出营业部钱5
            k = 1
            green_departments = []
            # green_departments_rise = [5]
            # green_departments_fall = [5]
            # green_departments_total = [5]
            while k < 6:
                department = Department.Department()
                green_department = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                    j) + ']/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"][2]/tbody/tr[' + str(
                    k) + ']/td[@class="tl rel"]//@title').extract_first()
                department['name'] = green_department
                # green_departments.append(green_department)
                green_department_rise = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                    j) + ']/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"][2]/tbody/tr[' + str(
                    k) + ']/td[2]/text()').extract_first()
                department['rise'] = green_department_rise
                # green_departments_rise.append(green_department_rise)
                green_department_fall = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                    j) + ']/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"][2]/tbody/tr[' + str(
                    k) + ']/td[3]/text()').extract_first()
                department['fall'] = green_department_fall
                # green_departments_fall.append(green_department_fall)
                green_department_total = response.xpath('//div[@class="rightcol fr"]/div[@class="stockcont"][' + str(
                    j) + ']/div[@class="cell-cont cjmx"]/table[@class="m-table m-table-nosort mt10"][2]/tbody/tr[' + str(
                    k) + ']/td[4]/text()').extract_first()
                department['total'] = green_department_total
                # green_departments_total.append(green_department_total)
                # print(green_departments[k])
                green_departments.append(department)
                k += 1

            j += 1

            item['rise_departments'] = red_departments
            item['fall_departments'] = green_departments
            # print(detali_title)
        result = Result.Result()
        result.stocks = stocks
        # print(result.stocks)
        # self.print_by_code(stocks,'002408')

    # ------当日龙虎榜解析
    def get_path(self, row, col):
        if col == 3:
            return '//div[@class="twrap"]/table/tbody//tr[' + str(row) + ']/td[' + str(col) + ']/a/text()'
        return '//div[@class="twrap"]/table/tbody//tr[' + str(row) + ']/td[' + str(col) + ']/text()'

    def get_item_by_code(self, stocks, code):
        for stock in stocks:
            if stock['code'] == code:
                return stock

    def print_by_code(self, stocks, code):
        for stock in stocks:
            # print(stock['code'])
            if stock['code'] == code:
                print(stock)
