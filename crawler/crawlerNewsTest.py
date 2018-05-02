# -*- coding: utf-8 -*-
from crawler.crawler_utils import *

user_agent = '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

driver = webdriver.Chrome(chrome_options=chrome_option())
soup = get_url_content(driver, "https://news.qq.com/a/20180502/001638.htm")
print(soup.h1.string)
content_list = soup.find_all(name="p", attrs={"class": "text"})
s = ""
for x in range(len(content_list)):
    if x >= len(content_list) - 1:
        tmp = content_list[x].contents[0].replace(u'\u3000', u'')
    else:
        tmp = content_list[x].string.replace(u'\u3000', u'')
    s = s + tmp

print(s)
