# -*- coding: utf-8 -*-

from crawler.crawler_utils import *

categoryUrls = []

driver = webdriver.Chrome(chrome_options=chrome_option())
soup = get_url_content(driver, "http://news.qq.com/")
urlList = soup.find(id="channelNavPart").find_all("li")
for url in urlList:
    # 主要列表列表
    # print(url.string + " " + url.a["href"])
    categoryUrls.append((url.string, url.a["href"]))

urlSet = set()

for url in categoryUrls:
    soup = driver.get(url[1])
    if url[0] in ["首页", "国际", "社会", "军事"]:
        itemList = soup.select(".Q-tpWrap")
        for ele in itemList:
            urlSet.add(ele.a["href"])
    # elif url[0] in ["历史"]:
    #     itemList = soup.select(".newTopicL")[0].find_all("li")
    #     for ele in itemList:
    #         urlSet.add(ele.a["href"])
    # elif url[0] in ["文化"]:
    #     itemList = soup.select(".Q-pList")
    #     for ele in itemList:
    #         urlSet.add(ele.a["href"])
    # elif url[0] in ["公益"]:
    #     itemList = soup.select(".Q-tpWrap")
    #     for ele in itemList:
    #         urlSet.add("http://gongyi.qq.com/" + ele.a["href"])
print("=====================")

# 遍历url获取网页内容
for url in urlSet:
    get_url_content(url)
    soup = get_soup()
    div = soup.find_all("div", class_="LEFT")
    print(div.h1)

# Refresh
# driver.refresh()
driver.close()
