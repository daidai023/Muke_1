# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：po_demo2.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/21 11:39
"""

from chapter3.test import *
from selenium.webdriver.common.keys import Keys


class Page:
    url = None  # 项目访问的url
    locators = {}  # 定位器
    browser = CHROME  # 浏览器

    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            self.driver = self.browser().browser

    def __getattr__(self, loc):
        if loc not in self.locators.keys():
            raise Exception
        by, val = self.locators[loc]
        return self.driver.find_element(by, val)


# 定义通用页面
class CommonLoginPage(Page):
    url = r'http://zentao:XMR0mWcyXKJ@127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html'
    locators = {
        'username': ('id', 'account'),
        'password': ('name', 'password'),
        'loginBtn': ('id', 'submit')
    }

    def get(self):
        """
        定义打开浏览器
        :return:
        """
        self.driver.get(self.url)

    def login(self, username: str = 'admin', password: str = 'Aa123456'):
        self.username.send_keys(username)   # 直接调用属性，因为属性不存在，所以直接调用__getattr__方法，执行return self.driver.find_element(by,val)
        self.password.send_keys(password)
        self.loginBtn.click()


# 定义业务页面
class MainPage(CommonLoginPage):
    # 通过update方法更新locators定位器
    CommonLoginPage.locators.update({
        'searchInput': ('xpath', '//*[@id="searchInput"]'),
        'searchGo': ('id', 'searchGo'),
        'user_name': ('xpath', '//*[@id="userNav"]/li/a/span[1]'),
        'bug_label': ('xpath', '//*[@id="mainMenu"]/div[1]/div[2]/span[1]')
    })

    def search_bug(self, bug_id: str = '1'):
        self.searchInput.send_keys(bug_id)  # 跟上面的login()定义一致，因为属性不存在，所以直接调用__getattr__()方法
        self.searchGo.click()


class TestMain:

    def test_login(self):
        page = MainPage()       # 实例化页面
        page.get()
        page.login()
        assert page.user_name.text == 'admin'
        print('test_login is ok!')
        page.driver.quit()

    def test_search(self):
        page = MainPage()
        page.get()
        page.login()
        page.search_bug()
        assert page.bug_label.text == '1'
        print('test_search is ok!')
        page.driver.quit()


# 执行测试
obj = TestMain()
obj.test_login()
obj.test_search()


