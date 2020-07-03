# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from homework1.items import Homework1Item


class NewmaoyanSpider(scrapy.Spider):
    name = 'newmaoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=2']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=2&offset='
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Homework1Item()
        move_infos = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for info in move_infos:
            item['title'] = info.xpath('./div[1]/span/text()').extract_first().strip()
            item['kind'] = info.xpath('./div[2]/text()').extract()[1].strip()
            item['time'] = info.xpath('./div[4]/text()').extract()[1].strip()
            print(item)
            yield item
