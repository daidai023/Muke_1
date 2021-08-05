# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：perform_1.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/8/4 15:47
"""
import cProfile


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    cProfile.run('fib(30)')
