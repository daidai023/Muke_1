# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：test_module_1.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/23 17:02
"""
import unittest
from unittest import skip, skipIf, skipUnless


@skip
# skip直接跳过当前测试类
class A(unittest.TestCase):

    def test_a1(self):
        self.assertEqual(1, 4)

    def test_a2(self):
        ...


@skipIf(1 == 2, '')
# 当条件满足的时候跳过，有两个参数，表达式和reason
class B(unittest.TestCase):

    def test_b1(self):
        ...

    @skipUnless(3 > 2, '')
    # 当条件不满足的时候跳过，有两个参数，表达式和reason
    def test_b2(self):
        ...
