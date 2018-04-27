# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
from crawler.crawlerNews import *

url = "http://history.news.qq.com/"

user_agent = '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

driver = webdriver.Chrome(chrome_options=chrome_option())
get_url_content(url)
soup = get_soup()
if url[0] in ["历史"]:
    itemList = soup.select(".newTopicL")
    for e in itemList:
        print(e.a["href"])
