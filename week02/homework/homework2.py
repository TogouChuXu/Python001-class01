import os
import json
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from time import sleep


# 使用webdriver 自动打开浏览器进行登录
# browser = webdriver.Chrome()
# try:
#     browser.get("https://shimo.im/")
#     sleep(1)
#
#     # 模拟点击切换iframe
#     bm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
#     sleep(1)
#     bm1.click()
#
#     # 模拟点击登录
#     browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('1007300048@qq.com')
#     browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('123456789')
#     browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
#
#     # 获取cookie
#     cookies = browser.get_cookies()
#     print(cookies)
#     sleep(3)
#
# except Exception as e:
#     print(e)
#
# finally:
#     browser.close()

# 完整的使用requests模拟请求登录石墨
ua = UserAgent(verify_ssl=False)

headers1 = {
    'user-agent': ua.random,
}
headers2 = {
    'authority': 'shimo.im',
    'origin': 'https://shimo.im',
    'referer': 'https://shimo.im/login',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ua.random,
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
}

wel_url = 'https://shimo.im/login'
login_url = "https://shimo.im/lizard-api/auth/password/login"

form_data = {
    'mobile': '+86XXXXXXXXXXX',
    'password': '*********'
}

with requests.Session() as s:
    s.get(wel_url, headers=headers1)
    print(s.cookies)
    response = s.post(login_url, data=form_data, headers=headers2, cookies=s.cookies)
    print(response.status_code)












