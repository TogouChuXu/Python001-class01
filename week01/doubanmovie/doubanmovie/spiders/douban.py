# -*- coding: utf-8 -*-
import scrapy
from doubanmovie.items import DoubanmovieItem
from bs4 import BeautifulSoup as bs


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for i in range(0,10):
            url = f'https://movie.douban.com/top250?start={i*25}&filter='
            yield scrapy.Request(url, self.parse)

    # 解释每一个页面的所有电影条目
    def parse(self, response):
        # 使用 BeautifulSoup 解析网页内容
        bs_info = bs(response.text, 'html.parser')  # html 解析方式
        # Python 中使用for in 形式的循环,Python使用缩进来做语句块分隔
        title_list = bs_info.find_all('div', attrs={'class': 'hd'})
        for i in title_list:
            item = DoubanmovieItem()
            item["title"] = i.find('a').find('span', ).text
            item["link"] = i.find('a').get('href')
            yield scrapy.Request(url=item["link"], meta={'item': item}, callback=self.parse2)

    # 解析每一个具体电影的内容，获取电影简介
    def parse2(self, response):
        soup = bs(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item = response.meta["item"]
        item["content"] = content
        yield item

