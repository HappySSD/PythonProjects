# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql


class SpiderPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(user='root', password='320209', database='test', charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('insert into movie (name) values ("%s")', item['name'])
        return item
