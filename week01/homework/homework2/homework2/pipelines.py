# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Homework2Pipeline:
    def process_item(self, item, spider):
        title = item["title"]
        type = item["type"]
        time = item["time"]
        output = f'|{title}|\t{type}|\t{time}|\n\n'
        print(output)
        with open('./maoyan.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
            article.close()
        return item
