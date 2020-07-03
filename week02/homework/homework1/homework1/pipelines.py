# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from homework1.pymysql_client import PymysqlClient


class Homework1Pipeline:

    def __init__(self):
        user = 'user'
        host = '127.0.0.1'
        password = '******'
        database = 'scrapydb'
        self.db = PymysqlClient(host, user, password, database)

    def close_spider(self, spider):
        if self.db is not None:
            self.db.close()

    # 保存到本地文件当中
    def process_item(self, item, spider):
        strsql = "INSERT INTO maoyan(name,type,stime)  VALUES(%s,%s,%s)"
        try:
            print(tuple(item.values()))
            self.db.execute(strsql, tuple(item.values()))
        except Exception as e:
            self.db.close()
            print(e)
        return item
