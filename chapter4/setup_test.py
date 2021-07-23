# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：setup_test.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/23 11:10
"""
import unittest
from chapter3.po_demo import Search
import time


class TestA(unittest.TestCase, Search):

    @classmethod
    def setUpClass(cls) -> None:
        ...

    def setUp(self) -> None:
        self.get()
        self.login()

    def test_search(self):
        # self.get()
        # self.login()
        self.search_bug()
        assert self.element(self.bug_label).text == '1'

    def test_logout(self):
        # self.get()
        # self.login()
        self.logout()
        time.sleep(1)
        assert self.driver.current_url == r'http://zentao:XMR0mWcyXKJ@127.0.0.1/zentao/user-login.html'


class B(unittest.TestCase, Search):

    @classmethod
    def setUpClass(cls) -> None:
        cls.cls_get()
        cls.cls_login()
        time.sleep(2)

    def setUp(self) -> None:
        ...

    def test_search(self):
        # self.get()
        time.sleep(2)
        self.login()
        self.search_bug()
        assert self.element(self.bug_label).text == '1'

    def test_logout(self):
        # self.get()
        # self.login()
        self.logout()
        time.sleep(1)
        assert self.driver.current_url == r'http://zentao:XMR0mWcyXKJ@127.0.0.1/zentao/user-login.html'

    def tearDown(self) -> None:
        self.driver.refresh()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()