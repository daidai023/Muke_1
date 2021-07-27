# !/usr/bin/env python
# -*- coding: UTF-8 -*-

from os.path import join, dirname
import unittest
from chapter4.case import tests
from HTMLTestRunner import HTMLTestRunner

CASE_PATH = join(dirname(__file__), './chapter4/case')

suit = unittest.TestSuite()
loader = unittest.defaultTestLoader

for test in tests:
    test_suit = loader.discover(start_dir=CASE_PATH, pattern=test)

    suit.addTest(test_suit)

# with open('./report.txt', 'w') as f:
#     runner = unittest.TextTestRunner(f, verbosity=2)
#

#     runner.run(suit)


with open('./report.html', 'wb') as f:
# f = open('./report.html', 'w')
    runner = HTMLTestRunner(stream=f, title='测试报告',verbosity=2)
    runner.run(suit)
