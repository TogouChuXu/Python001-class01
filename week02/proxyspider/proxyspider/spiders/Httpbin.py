# -*- coding: utf-8 -*-
import scrapy



class HttpbinSpider(scrapy.Spider):
    name = 'Httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)


