# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getSoup():
    """
    获取Soup
    :return: soup对象
    """
    global webElement, html, soup
    webElement = driver.find_element("xpath", "/html")
    html = webElement.get_attribute("outerHTML")
    return BeautifulSoup(html, "html.parser")


categoryUrls = []

options = webdriver.ChromeOptions()
options.set_headless()
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://news.qq.com/")
# time.sleep(2)
soup = getSoup()
urlList = soup.find(id="channelNavPart").find_all("li")
for url in urlList:
    print(url.string + " " + url.a["href"])
    categoryUrls.append((url.string, url.a["href"]))


for url in categoryUrls:
    driver.get(url[1])
    soup = getSoup()
    itemList = soup.select(".Q-tpWrap")
    for ele in itemList:
        print(ele.a["href"])


# Refresh
# driver.refresh()
driver.close()
