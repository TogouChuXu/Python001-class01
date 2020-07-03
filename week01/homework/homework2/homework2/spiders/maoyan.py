# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from time import sleep
from homework2.items import Homework2Item


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=2']  # 首次需要请求的页面

    def start_requests(self):
        # for num in range(0, 1):
        url = 'https://maoyan.com/films?showType=2&offset=' + str(0 * 30)
        yield scrapy.Request(url, self.parse)

    # 获取电影链接信息
    def parse(self, response):
        print("打印测试")
        item = Homework2Item()
        movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        for movie in movies:
            print(movie)
            link = movie.xpath('./a/@href')
            url = "https://maoyan.com" + link.extract_first()
            print("电影链接： " + url)
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)

    # 获取电影详情页信息
    def parse2(self, response):
        item = response.meta["item"]
        detail = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        title = detail.xpath('./h1[@class="name"]/text()').extract_first()
        items = detail.xpath('./ul/li[1]/a[@class="text-link"]/text()').extract()
        types = ""
        for row in items:
            types += row
        time = detail.xpath('./ul/li[3]/text()').extract_first()
        item['title'] = title
        item['type'] = types
        item['time'] = time
        yield item



