#!/home/hadoop/anaconda3/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import platform


def get_user_agent():
    """"
    随机获取HTTP_User_Agent
    """
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    user_agent = random.choice(user_agents)
    return user_agent


def chrome_option():
    """
    设置 chrome option
    :return:  chrome option
    """
    global options
    options = webdriver.ChromeOptions()
    # 设置为无界面浏览器
    options.set_headless()
    options.add_argument(get_user_agent())
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
        print(url)
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
    content_style = soup.find_all(name="p", attrs={"style": "TEXT-INDENT: 2em"})
    content = soup.find_all(name="p")

    if len(content_text) > 0:
        content_list = content_text
    elif len(content_one) > 0:
        content_list = content_one
    elif len(content_style) > 0:
        content_list = content_style
    else:
        content_list = content

    s = ""
    for x in range(len(content_list) - 1):
        if x == len(content_list) - 1:
            # 尾部特殊处理
            tmp = content_list[x].contents[0].replace(u'\u3000', u'')
        else:
            if content_list[x].img is None:
                tmp = content_list[x].text.replace(u'\u3000', u'')
            else:
                continue
        s = s + tmp
    s = s.replace('\r', '').replace('\n', '').replace('\t', '')
    return soup.title.text, get_now_time(), s, url


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
