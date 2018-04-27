# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random


def get_soup():
    """
    获取Soup
    :return: soup对象
    """
    global webElement, html, soup
    webElement = driver.find_element("xpath", "/html")
    html = webElement.get_attribute("outerHTML")
    return BeautifulSoup(html, "html.parser")


def chrome_option():
    """
    设置 chrome option
    :return:  chrome option
    """
    global options
    options = webdriver.ChromeOptions()
    # 设置为无界面浏览器
    options.set_headless()
    options.add_argument(user_agent)
    return options


def get_url_content(url):
    """
     睡眠2~4秒随机秒数，并获取url内容
    :param url:  爬取url
    :return:
    """
    driver.get(url)
    sleep_time = random.uniform(2, 4)
    time.sleep(sleep_time)


categoryUrls = []
user_agent = '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

driver = webdriver.Chrome(chrome_options=chrome_option())
get_url_content("http://news.qq.com/")
soup = get_soup()
urlList = soup.find(id="channelNavPart").find_all("li")
for url in urlList:
    # 主要列表列表
    # print(url.string + " " + url.a["href"])
    categoryUrls.append((url.string, url.a["href"]))

for url in categoryUrls:
    print(url[0])
    driver.get(url[1])
    soup = get_soup()
    if url[0] in ["首页", "国际", "社会", "军事"]:
        itemList = soup.select(".Q-tpWrap")
        for ele in itemList:
            print(ele.a["href"])
    # elif url[0] in ["评论"]:
    #     itemList = soup.select(".comtopic")
    #     for e in itemList:
    #         print(e.a["href"])
    elif url[0] in ["历史"]:
        itemList = soup.select(".newTopicL")[0].find_all("li")
        for e in itemList:
            print(e.a["href"])
    elif url[0] in ["文化"]:
        itemList = soup.select(".Q-pList")
        for e in itemList:
            print(e.a["href"])
    elif url[0] in ["公益"]:
        itemList = soup.select(".Q-tpWrap")
        for e in itemList:
            print("http://gongyi.qq.com/" + e.a["href"])
    elif url[0] in ["旅游"]:
        itemList = soup.select(".bd")
        for e in itemList:
            print("http://ly.qq.com/" + e.a["href"])

print("=====================")

# Refresh
# driver.refresh()
driver.close()
