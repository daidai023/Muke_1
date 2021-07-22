# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：naked_code.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/14 17:33
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'D:/chromedriver.exe')

# driver.get(r'https://jira.souche-inc.com/login.jsp')    # jira访问地址
driver.get('http://zentao:XMR0mWcyXKJ@127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html')      # 禅道访问地址
# driver.switch_to.alert.send_keys('admin')
# time.sleep(1)
# driver.switch_to.alert.dismiss()

time.sleep(1)
# driver.find_element_by_id('login-form-username').send_keys('chenxiaojuan')
driver.find_element_by_id('account').send_keys('admin')
time.sleep(1)
# driver.find_element_by_name('os_password').send_keys('cxj20210628')
driver.find_element_by_name('password').send_keys('Aa123456')
time.sleep(1)
# driver.find_element_by_id('login-form-submit').click()
driver.find_element_by_id('submit').click()
time.sleep(1)

# 获取登录成功的账号信息
# account_info = driver.find_element_by_xpath('//*[@id="header-details-user-fullname"]/span/span/img')
account_info = driver.find_element_by_xpath('//*[@id="userNav"]/li/a/span[1]')

# if '陈小娟' in account_info.get_attribute('alt'):
#     print('登录成功')
# else:
#     print('登录失败')

if account_info.text == 'admin':
    print('登录成功')
else:
    print('登录失败')

# # 检索bug
# # input_box = driver.find_element_by_id('quickSearchInput')
# # input_box.send_keys('ISP-1699')
# input_box = driver.find_element_by_xpath('//*[@id="searchInput"]')
# input_box.send_keys('1')
# time.sleep(0.5)
# # input_box.send_keys(Keys.ENTER)
# search_go = driver.find_element_by_id('searchGo')
# search_go.click()
# time.sleep(1)
#
# # bug_id = driver.find_element_by_xpath('//*[@id="key-val"]').text
# bug_id = driver.find_element_by_xpath('//*[@id="mainMenu"]/div[1]/div[2]/span[1]').text
# if bug_id == '1':
#     print('检索成功')
# else:
#     print('检索失败')

# 退出系统
account_info.click()
driver.find_element_by_xpath('//*[@id="userNav"]/li/ul/li[13]/a').click()
time.sleep(2)

driver.quit()
