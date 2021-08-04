# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：wh.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/8/3 14:33
"""
# 维宏准备
# v = '0b1111011'
# print(int(v, 2))
#
# list1 = [1, 2, 3, 4, 9]
# list1.pop()
# print(list1)
#
# tuple1 = (1, 2, 3, 4, 9)
# print(dir(tuple1))
# print(tuple1)
# print(tuple1.__len__())
# print(tuple1.__contains__(1))
# l = str([1, 2, 3])
# print(l,type(l))
# print(l[0])
# l1 = [1, 2, 3]
# for i, element in enumerate(l1):
#     print(i, element)
from functools import reduce
import pandas as pd

# print('{} {}'.format('hello', 'world'))
# x = set('runoob')
# y = set('google')
# print(x)
# print(y)
#
# # reduce\map\filter\eval\enumerate\hash\hex\oct\bin\int\zip\
# # hash()函数返回对象的哈希值
# print(hash('hello'))
#
# # 进制之间互相转化
# # 十进制转化为二进制
# print(bin(10))
#
# # 十进制转化为八进制
# print(oct(10))
#
# # 十进制转化为十六进制
# print(hex(10))
#
# # 二进制、八进制、十六进制转化为十进制
# print(int('0b1010', 2))
# print(int('0o12', 8))
# print(int('0xa', 16))
#
# # reduce()函数，先对集合中的元素1和2进行作用，然后得到的结果在和后面的元素进行操作
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
# print(reduce(lambda x, y:x.join(y), ['d', 'a', 'i', 's', 'y']))
# name = ['d', 'a', 'i', 's', 'y']
# print('?|'.join(name))

# map()函数，参数序列的每个元素都调用function函数，返回组成的列表
print(tuple(map(lambda x, y: x+y, [1, 2, 3, 4, 5], [2, 4, 6, 8, 10])))

li = ['1', '2', '3']
series = pd.Series(li, ['a', 'b', 'c'])
# series=list(series.map(lambda x:int(x)))
# print(series)
print(series)

a = '我是一个列表111'
print(list(filter(str.isdigit, a)))


