# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import platform

user_agent = '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'


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
    :return: 返回BeautifulSoup后的html内容
    """
    driver = webdriver.Chrome(chrome_options=chrome_option())
    try:
        driver.get(url)
        sleep_time = random.uniform(2, 4)
        time.sleep(sleep_time)
        web_element = driver.find_element("xpath", "/html")
        html = web_element.get_attribute("outerHTML")
    except Exception as e:
        print(e)
    finally:
        if driver is not None:
            driver.quit()
    return BeautifulSoup(html, "html.parser")


def save_to_file(file_name, contents):
    """
    保存内容值本地文件
    :param file_name:  文件名称
    :param contents:  文件内容
    """
    try:
        fh = open(file_name, 'a')
        fh.write(contents + "\n")
    except Exception as e:
        print(e)
    finally:
        fh.close()


def get_system():
    """
    获取当前系统
    :return:  Windows\Linux\Other System
    """
    sys_str = platform.system()
    if sys_str == "Windows":
        return "Windows"
    elif sys_str == "Linux":
        return "Linux"
    else:
        return "Other System"


def get_system_path():
    """
    获取爬虫持久化路径
    :return: 当前系统路径
    """
    linux_path = "/home/hadoop/news/"
    windows_path = "E://news//"
    path = windows_path if get_system() == "Windows" else linux_path
    return path


def get_title_content(url):
    """
    获取url连接 内容信息
    :param url:  待获取url
    :return: 标题，爬取时间，新闻内容，url
    """
    soup = get_url_content(url)
    content_text = soup.find_all(name="p", attrs={"class": "text"})
    content_one = soup.find_all(name="p", attrs={"class": "one-p"})
    content_list = (content_text if (len(content_text) > 0) else content_one)
    s = ""
    for x in range(len(content_list) - 1):
        if x == len(content_list) - 1:
            # 尾部特殊处理
            tmp = content_list[x].contents[0].replace(u'\u3000', u'')
        else:
            if content_list[x].img is None:
                # 处理加粗标记的内容
                if len(content_list[x].contents) >= 2:
                    tmp = content_list[x].contents[2]
                elif content_list[x].string is None:
                    continue
                else:
                    tmp = content_list[x].string.replace(u'\u3000', u'')
            else:
                continue
        s = s + tmp

    return soup.h1.string, get_now_time(), s, url


def get_now_time():
    """
    返回形如2018-05-03 09:33:00的日期
    :return: 返回当前时间
    """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def get_now_date():
    """
    返回形如2018-05-03的日期
    :return: 返回当前时间
    """
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))
