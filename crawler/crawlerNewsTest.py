# -*- coding: utf-8 -*-
from crawler.crawler_utils import *

user_agent = '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

driver = webdriver.Chrome(chrome_options=chrome_option())
soup = get_url_content(driver, "http://new.qq.com/omn/20180502/20180502A0T57K.html")
print(soup.h1.string)
content_text = soup.find_all(name="p", attrs={"class": "text"})
content_one = soup.find_all(name="p", attrs={"class": "one-p"})
content_list = (content_text if (len(content_text) > 0) else content_one)
s = ""
for x in range(len(content_list)):
    if x >= len(content_list) - 1:
        tmp = content_list[x].contents[0].replace(u'\u3000', u'')
    else:
        if content_list[x].img is None:
            tmp = content_list[x].string.replace(u'\u3000', u'')
        else:
            continue
        s = s + tmp

print(s)
