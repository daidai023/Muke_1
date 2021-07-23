# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：assert_test.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/22 14:24
"""

import unittest


class A(unittest.TestCase):

    def test_a(self):
        assert (_len :=self.test_a.__name__.__len__()) == 4, \
            print(f'test_a方法名称的长度是{_len},不是4！')             # 如果assert失败则输出print里面的内容

    def test_b(self):
        try:
            self.assertEqual((_len := self.test_b.__name__.__len__()), 4)
        except AssertionError:
            print(f'test_a方法名称的长度是{_len},不是4！')
            raise AssertionError
