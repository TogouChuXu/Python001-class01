import os
import json
import requests
import pytesseract
from fake_useragent import UserAgent
from selenium import webdriver
from PIL import Image
from time import sleep
from urllib.parse import urlparse


# 使用webdriver 自动打开浏览器进行登录
# browser = webdriver.Chrome()
# try:
#     # browser.get("https://www.douban.com")
#     # sleep(1)
#     #
#     # # 模拟点击切换iframe
#     # browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[0])
#     # bm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
#     # sleep(1)
#     # bm1.click()
#     #
#     # # 模拟点击登录
#     # browser.find_element_by_xpath('//*[@id="username"]').send_keys('1007300048@qq.com')
#     # browser.find_element_by_xpath('//*[@id="password"]').send_keys('123456789')
#     # browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
#     #
#     # # 获取cookie
#     # cookies = browser.get_cookies()
#     # print(cookies)
#     # sleep(3)
#
#     # 模拟浏览器登录获取短评信息
#     browser.get("https://movie.douban.com/subject/1292052/")
#     browser.find_element_by_xpath('//*[@id="hot-comments"]/a').click()
#     sleep(10)
#     print(browser.page_source)
#
# except Exception as e:
#     print(e)
#
# finally:
#     browser.close()

# # 完整的使用requests模拟请求登录豆瓣
# ua = UserAgent(verify_ssl=False)
# headers = {
#     'User-Agent': ua.random,
#     'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
# }
#
# s = requests.Session()
# login_url = "https://accounts.douban.com/j/mobile/login/basic"
# form_data = {
#     "ck": "",
#     "name": "1007300048@qq.com",
#     "password": "123456",
#     "remember": 'false',
#     "ticket": ""
# }
# # 提交登录信息
# response = s.post(login_url, data=form_data, headers=headers)
# print(response.text)

# #  使用Python库模拟不同的浏览器代理
# ua = UserAgent(verify_ssl=False)
#
# # 模拟使用Chrome浏览器
# print("谷歌浏览器： " + ua.chrome)
#
# # 模拟随机浏览器
# print("随机浏览器： " + ua.random)
#
# # 使用requests 发起 GET请求
# r = requests.get("https://github.com")
# print(r.status_code)
# print(r.encoding)
# print(r.headers["content-type"])
# # 使用requests 发起 POST 请求
# s = requests.post("http://httpbin.org/post", data={'key': 'value'})
# print(s.json())
# # 在同一个session实例发出的所有请求之间保持 cookie
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
# r = s.get("http://httpbin.org/cookies")
# print(r.text)
# # 会话可以使用上下文管理器
# with requests.Session() as s:
#     s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")

# 文件下载
# 小文件下载
# r = requests.get('https://www.python.org/static/community_logos/python-logo-master-v3-TM.png')
# with open("python_logo.png", "wb") as f:
#     f.write(r.content)
#     f.close()
#
# # 大文件下载 流式分块下载
# r = requests.get('http://python.xxx.yyy.pdf', stream=True)
# with open("python.pdf", "wb") as f:
#     for chunk in r.iter_content(chunk_size=1024):
#         if chunk:
#             f.write(chunk)
#     f.close()

# 验证码识别
# 打开图片并显示
# im = Image.open('cap.jpg')
# im.show()
#
#
# # 灰度处理
# gray = im.convert('L')
# gray.save('c_gray2.jpg')
# im.close()
# # # 二值化
# threshold = 100
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# out = gray.point(table, '1')
# out.save('c_th.jpg')
#
# th = Image.open('c_th.jpg')
# print(pytesseract.image_to_string(th, lang="chi_sim+eng"))


# 获取代理ip库
s = requests.get('https://ip.jiangxianli.com/api/proxy_ips/', data={'page': 2})
print(s.text)
ip_dict = json.loads(s.text)["data"]["data"]
ip_list = []
for row in ip_dict:
    ip_proxy = row['protocol']+"//"+row['ip']
    ip_list.append(ip_proxy)
print(ip_list)








