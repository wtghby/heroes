# -*- coding: UTF-8 -*-
import time

import pymysql
import uuid


class Mysql:
    def __init__(self):
        self.date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    def connect(self):
        self.connect = pymysql.connect("localhost", "root", "123456", "heroes")

    def version(self):
        cursor = self.connect.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()

        print("Database version : %s " % data)
        self.connect.close()

    def insert(self, item):
        # 插入股票数据
        uid = self.insert_stock(item)
        # 插入营业部数据
        for department in item['rise_departments']:
            # 买入营业部
            self.insert_department(item['code'], department, 0, item['date'], uid)
        for department in item['fall_departments']:
            # 卖出营业部
            self.insert_department(item['code'], department, 1, item['date'], uid)

    def insert_stock(self, stock):
        uid = uuid.uuid1()
        print(uid)
        sql = """insert into tb_stock(id,name,price,increase,deal,buy,rise,fall,reason,code,ddate) values (
        '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            uid, stock['name'], stock['price'], stock['increase'], stock['deal'], stock['buy'],
            stock['rise'], stock['fall'], stock['reason'], stock['code'], stock['date'])

        cursor = self.connect.cursor()
        try:
            cursor.execute(sql)
            self.connect.commit()
            return uid
        except:
            self.connect.rollback()

    def insert_department(self, code, department, type, date, uid):
        if department['name'] is None:
            return
        sql = """insert into tb_department(name,rise,fall,total,code,ddate,type,stock_id) values ('%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            department['name'], department['rise'], department['fall'], department['total'], code,
            date, type, uid)

        cursor = self.connect.cursor()
        try:
            cursor.execute(sql)
            self.connect.commit()
        except:
            self.connect.rollback()

    def close(self):
        self.connect.close()
