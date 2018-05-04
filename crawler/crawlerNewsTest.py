#!/home/hadoop/anaconda3/bin/python
# -*- coding: utf-8 -*-
from crawler.crawler_utils import *

urls = ["http://new.qq.com/omn/20180504/20180504A00137.html",
        "https://news.qq.com/a/20180502/040440.htm",
        "http://new.qq.com/omn/20180503/20180503A05S0L.html"]

for url in urls:
    title, now_time, content, url = get_title_content(url)
    contents = title + "^" + now_time + "^" + content + "^" + url
    save_to_file(get_system_path() + get_now_date(), contents)
