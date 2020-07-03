import requests
import random
import lxml.etree
import pandas as pd
from bs4 import BeautifulSoup as bs
from time import sleep


# 获取电影的详情页,并将内容解析出来保存
def get_film_detail(response):
    #  xml化处理
    selector = lxml.etree.HTML(response.text)

    # 获取解析内容
    film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')  # 电影名称
    print(f'电影名称: {film_name}')

    plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')  # 上映时间
    print(f'上映时间: {plan_date}')

    rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')  # 评分
    print(f'评分: {rating}')

    mylist = [film_name, plan_date, rating]

    df = pd.DataFrame(data=mylist)
    df.to_csv("./movie.csv", mode='a', encoding='utf-8', index=False, header=False)


# 根据不同的url获取当前页面的电影名和电影链接
def get_url_name(url, header):
    response = requests.get(url, headers=header)
    # 使用 BeautifulSoup 解析网页内容
    bs_info = bs(response.text, 'html.parser')  # html 解析方式

    # Python 中使用for in 形式的循环,Python使用缩进来做语句块分隔
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a'):
            # 获取电影链接
            print(atag.get('href'))
            detail_url = atag.get('href')
            detail_response = requests.get(detail_url, headers=header)
            get_film_detail(detail_response)
            # 获取电影名字
            print(atag.find('span', ).text)



def main1():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    ]

    # 构建Request Header
    header = {'user-agent': random.choice(user_agents)}

    for num in range(0, 9):
        url = 'https://movie.douban.com/top250?start=' + str(num * 25) + '&filter='
        get_url_name(url, header)
        sleep(5)

def main2():
    output = "hello world"
    with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
        article.write(output)
        article.close()



# 主函数调用
if __name__ == '__main__':
    main2()















