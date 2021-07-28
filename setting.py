# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：setting.py.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/27 14:33
"""
# 项目地址
# 项目包和文件夹的路径
# 浏览器对象属性
# 测试套件
from os.path import dirname, join

# -----------------项目地址------------------
# 项目一地址
PROJECT_ZENTAO_URL = 'http://zentao:XMR0mWcyXKJ@127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html'

# 项目二地址
PROJECT_QQ_URL = ''

# -------------项目包配置---------------
# 项目根目录
BASE_PATH = dirname(__file__)

# 浏览器驱动文件地址
CHROME_DRIVER_PATH = join(BASE_PATH, 'driver/chrome_driver.exe')
IE_DRIVER_PATH = join(BASE_PATH, 'driver/IEDriverServer.exe')
EDGE_DRIVER_PATH = join(BASE_PATH, 'driver/edge_driver.exe')
FIREFOX_DRIVER_PATH = join(BASE_PATH, 'driver/gecko_driver.exe')
OPERA_DRIVER_PATH = join(BASE_PATH, 'driver/opera_driver.exe')

# 模块1路径
CHAPTER_1_PATH = join(BASE_PATH, 'chapter3')

# 模块2路径
CHAPTER_2_PATH = join(BASE_PATH, 'chapter4')

# 模块3路径
CHAPTER_3_PATH = join(BASE_PATH, 'chapter5')

# 测试套件
# 流程1测试套件
SUIT_MODULE_1 = ['module_1_test.py', 'module_2_test.py']

# 流程2测试套件
SUIT_MODULE_2 = ['test_1_smoke.py', 'test_2_smoke.py']

# 流程3测试套件
SUIT_MODULE_3 = ['test_module_1.py', 'test_module_2.py']

# 主测试套件
SUIT = ['test_module_1.py', 'test_module_2.py', 'test_module_3.py']

