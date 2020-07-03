import requests
import random
from bs4 import BeautifulSoup as bs
from time import sleep


# 获取电影的详情页,并将内容解析出来保存
def get_film_detail(response):
    # 使用BeautifulSoup获取电影详情信息
    detail_info = bs(response.text, 'html.parser').find('div', attrs={'class': 'movie-brief-container'})  # html 解析方式
    title = detail_info.find('h1',).text.strip()
    print("电影名称： "+title)
    dli = detail_info.find_all('li')
    types = ""
    for type in dli[0].find_all('a'):
        types += type.get_text()
    print("电影类型： " + types)
    time = dli[2].get_text()
    print("上映时间： " + time)
    # 组合文件一行类型
    output = f'{title},{types},{time}\n\n'
    print("写入的文件信息: " + output)
    # 写入爬取的电影内容到文件中
    with open('./homework1.csv', mode='a+', encoding='utf-8') as line:
        line.write(output)
        line.close()


# 根据不同的url获取当前页面的电影名和电影链接
def get_url_name(url, header):
    response = requests.get(url, headers=header)
    # 使用 BeautifulSoup 解析网页内容
    bs_info = bs(response.text, 'html.parser')  # html 解析方式

    # Python 中使用for in 形式的循环,Python使用缩进来做语句块分隔
    for tags in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'}):
        detail_url = tags.find('a',).get('href')
        # 获取电影链接
        print(detail_url)
        detail_response = requests.get("https://maoyan.com"+detail_url, headers=header)
        get_film_detail(detail_response)


def main1():
    user_agents = [
        'Chrome/83.0.4103.106 Mobile Safari/537.36'
    ]

    # 构建Request Header
    header = {'user-agent': random.choice(user_agents)}

    # 开始遍历并且进行
    for num in range(0, 1):
        url = 'https://maoyan.com/films?showType=2&offset=' + str(num * 30)
        get_url_name(url, header)
        sleep(5)


# 主函数调用
if __name__ == '__main__':
    main1()















