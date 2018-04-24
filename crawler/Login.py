# -*- coding: utf-8 -*-

import os
import datetime
import time

##################################################

##### Wish login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options)  # Get local session of firefox

driver.get("http://news.qq.com/")
time.sleep(2)

## Email Login
# driver.find_element_by_xpath("//*[@id=\"signup-form\"]/div[6]").click()
## Input email & password
driver.find_element_by_xpath("//*[@id=\"_accountName\"]").send_keys("")
driver.find_element_by_xpath("//*[@id=\"_passwordName\"]").send_keys("")

## Click login
driver.find_element_by_xpath("//*[@id=\"_loginBtn\"]").click()
time.sleep(2)

###### Refresh
## driver.refresh()
driver.close()
