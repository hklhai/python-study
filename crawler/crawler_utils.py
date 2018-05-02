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


def get_url_content(driver, url):
    """
    睡眠2~4秒随机秒数，并获取url内容
    :param driver:  webdriver
    :param url:  爬取url
    :return: 返回BeautifulSoup后的html内容
    """
    driver.get(url)
    sleep_time = random.uniform(2, 4)
    time.sleep(sleep_time)
    web_element = driver.find_element("xpath", "/html")
    html = web_element.get_attribute("outerHTML")
    return BeautifulSoup(html, "html.parser")


def save_to_file(file_name, contents):
    """
    保存内容值本地文件
    :param file_name:  文件名称
    :param contents:  文件内容
    :return:
    """
    fh = open(file_name, 'w')
    fh.write(contents)
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
    linux_path = "/home/hadoop/news"
    windows_path = "E://news"
    path = windows_path if get_system() == "Windows" else linux_path
    return path
