# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：monistor.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/28 14:07
"""
import psutil
import time

# print('CPU使用率， 内存使用率， C盘使用率')
delay =3

# while True:
    # time.sleep(delay)
    # print()
    # print(psutil.cpu_percent())
    # print(psutil.virtual_memory().percent)
    # print(psutil.disk_usage("C:\\").percent)
# CPU的完整信息
print(psutil.cpu_times())