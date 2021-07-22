# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：po_demo.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/19 14:11
"""
from chapter3.test import *
from selenium.webdriver.common.keys import Keys


class Page:
    url = None

    driver = None

    def element(self, loc: tuple):
        """
        定位元素的方法
        :return:
        """
        return self.driver.find_element(*loc)

    def elements(self, loc: tuple):
        """
        定位元素组的方法
        :param loc:
        :return:
        """
        return self.driver.find_elements(*loc)


class CommonLoginPage(Page):
    url = r'http://zentao:XMR0mWcyXKJ@127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html'
    driver = CHROME().browser           # 直接调用test定义的浏览器类型
    username = ('id', 'account')
    password = ('name', 'password')
    loginBtn = ('id', 'submit')

    def get(self):
        """
        打开浏览器
        :return:
        """
        self.driver.get(self.url)

    def login(self, username: str='admin', password: str='Aa123456'):
        self.element(self.username).send_keys(username)
        self.element(self.password).send_keys(password)
        self.element(self.loginBtn).click()


class Search(CommonLoginPage):
    searchInput = ('xpath', '//*[@id="searchInput"]')
    searchGo = ('id', 'searchGo')

    # 断言的元素
    user_name = ('xpath', '//*[@id="userNav"]/li/a/span[1]')
    bug_label = ('xpath', '//*[@id="mainMenu"]/div[1]/div[2]/span[1]')

    # 退出的元素
    log_out = ('xpath', '//*[@id="userNav"]/li/ul/li[13]/a')

    def search_bug(self, bug_id: str='1'):
        self.element(self.searchInput).send_keys(bug_id)
        self.element(self.searchGo).click()

    def logout(self):
        self.element(self.user_name).click()
        self.element(self.log_out).click()


class TestSearch(Search):
    """
    测试登录和验证bug功能
    """
    def test_login(self):
        self.get()
        self.login()
        time.sleep(1)
        assert self.element(self.user_name).text == 'admin'
        print('test_login is ok!')

    def test_search(self):
        self.search_bug()
        assert self.element(self.bug_label).text == '1'
        print('tes_search is ok!')
        self.driver.quit()


# obj = TestSearch()
# obj.test_login()
# obj.test_search()





