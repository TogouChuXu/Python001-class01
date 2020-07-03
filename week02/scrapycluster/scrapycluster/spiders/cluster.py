# -*- coding: utf-8 -*-
import scrapy
import json
from scrapycluster.items import ScrapyclusterItem


class ClusterSpider(scrapy.Spider):
    name = 'cluster'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(json.loads(response.text)['origin'])
        item = ScrapyclusterItem()
        item["ip"] = json.loads(response.text)['origin']
        yield item
