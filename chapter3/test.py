# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/14 14:06
"""
# 浏览器的类型
# 浏览器的启动参数（无头模式、最大化、尺寸化）
# 浏览器的属性（显示尺寸、隐式等待、页面加载、js执行时间）
from selenium.webdriver import *
from typing import Type, Union
import time


class BrowserTypeError(Exception):

    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f'unsupported browser type: {self._type}'


class BROWSER:
    # driver地址
    CHROME_DRIVER_PATH = '../driver/chromedriver.exe'
    EDGE_DRIVER_PATH = '../driver/edge_driver.exe'
    FIREFOX_DRIVER_PATH = '../driver/gecko_driver.exe'
    IE_DRIVER_PATH = '../driver/IEDriverServer.exe'
    OPERA_DRIVER_PATH = '../driver/opera_driver.exe'

    WINDOWS_SIZE = (1024, 768)  # 定义浏览器的尺寸

    IMP_TIME = 30  # 定义隐式等待时间

    PAGE_LOAD_TIME = 20  # 定义页面加载时间

    SCRIPT_TIME_OUT = 20  # js执行等待时间

    HEADLESS = True  # 定义浏览器的无头模式为true，以上定义都可以通过继承父类重写来进行修改

    def __init__(self, browser_type: Type[Union[Firefox, Chrome, Ie, Edge, Opera]] = Chrome,
                 option_type: Type[Union[FirefoxOptions, ChromeOptions, IeOptions]] = ChromeOptions,
                 driver_path: str = CHROME_DRIVER_PATH):
        if not issubclass(browser_type, (Firefox, Chrome, Ie, Edge, Opera)):
            raise BrowserTypeError(browser_type)
        if not issubclass(option_type, (FirefoxOptions, ChromeOptions, IeOptions)):
            raise BrowserTypeError(option_type)
        if not isinstance(driver_path, str):
            raise TypeError
        self._path = driver_path
        self._browser = browser_type
        self._option = option_type

    @property
    def options(self):
        """
        浏览器特定的操作，在子类中实现
        :return:
        """
        return

    @property
    def browser(self):
        """
        启动浏览器，返回浏览器实例
        :return:
        """
        return


class CHROME(BROWSER):
    OPTION_MARK = True      # 定义option的标签，如果为true则使用options启动

    METHOD_MARK = True      # 定义browser的标签，如果为true则使用，否则不适用

    HEADLESS = False  # 重写父类属性

    IMP_TIME = 30

    PAGE_LOAD_TIME = 30

    SCRIPT_TIME_OUT = 30

    WINDOWS_SIZE = (1920, 900)

    START_MAX = '--start-maximized'

    EXP = {
        'excludeSwitches': ['enable-automation'],
        # 'mobileEmulation': {'deviceName': 'iPhone 6'}
    }

    @property
    def options(self):
        if self.OPTION_MARK:
            chrome_option = self._option()
            chrome_option.add_argument(self.START_MAX)
            for k, v in self.EXP.items():  # 把EXP定义的字典类型转化为键值对
                chrome_option.add_experimental_option(k, v)  # add_experimental_option()
            chrome_option.headless = self.HEADLESS
            return chrome_option
        return None

    @property
    def browser(self):
        if self.options:
            chrome = self._browser(self._path, options=self.options)
        else:
            chrome = self._browser(self._path)
        if self.METHOD_MARK:
            chrome.implicitly_wait(self.IMP_TIME)  # 设置隐式等待时间
            chrome.set_script_timeout(self.SCRIPT_TIME_OUT)  # 设置js执行等待时间
            chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)  # 设置页面加载等待时间
            # chrome.set_window_size(*self.WINDOWS_SIZE)            # 浏览器启动的时候已经设置了最大化启动，所以这一步注释掉
        return chrome


# # 启动Chrome浏览器
# with CHROME().browser as _chrome:
#     _chrome.get(r'https://jira.souche-inc.com/login.jsp')
#     time.sleep(3)


class IE(BROWSER):
    CLEAN_SESSION = True

    IMP_TIME = 40

    def __init__(self):
        super(IE, self).__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path=super().IE_DRIVER_PATH
        )

    @property
    def options(self):
        ie_option = self._option()
        ie_option.ensure_clean_session = self.CLEAN_SESSION
        return ie_option

    @property
    def browser(self):
        ie = self._browser(self._path, options=self.options)
        ie.implicitly_wait(self.IMP_TIME)
        ie.set_page_load_timeout(self.PAGE_LOAD_TIME)
        ie.set_script_timeout(self.SCRIPT_TIME_OUT)
        ie.maximize_window()
        return ie


# # 启动IE浏览器
# with IE().browser as _ie:
#     _ie.get(r'https://jira.souche-inc.com/login.jsp')
#     time.sleep(3)
