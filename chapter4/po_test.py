# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：po_test.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/23 16:05
"""
import unittest
from chapter3.po_demo2 import MainPage
from time import sleep


class A(unittest.TestCase):

    def setUp(self) -> None:
        self.page = MainPage()
        self.page.get()
        self.page.login()

    def test_a(self):
        # self.page = MainPage()
        # self.page.get()
        # self.page.login()
        self.page.search_bug()
        assert self.page.bug_label.text == '1'

    def tearDown(self) -> None:
        self.page.driver.quit()
