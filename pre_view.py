# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：pre_view.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/16 10:32
"""

# print(chr(0b100111001011000))
# print(ord('乘'))
#
# print('十六进制', 0x1EAF)
# f1 = True
#
# print(f1+1)
#
# num_a = int(input('请输入第一个整数：'))
# num_b = int(input('请输入第二个整数'))
#
# print(str(num_a) + '大于等于' + str(num_b) if num_a >= num_b else str(num_a) + '小于' + str(num_b))
#
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(str(i) + '*' + str(j) + '=' + str(i*j), end='\t')
#     print()
#
# lst = [i*i for i in range(1, 10)]
# print(lst)

# # 字典的创建方式
# Student = dict(name='jack', age=20)
# print(Student)
#
# print(Student.get('name'))  # get的参数是key
# print(Student.get('jack', 11))
#
# del Student['name']
# print(Student)
#
# Student.clear()
# print(Student)

# keys = Student.keys()
# print(list(keys))
# values = Student.values()
# print(list(values))
#
# items = Student.items()
# # print(list(items))
#
# items = ['F', 'G', 'H']
# prices = [98, 76, 99, 100, 0]
# d = {item: price for item, price in zip(items, prices)}
# print(d)
#
#
# t = ('python', 'world', 98)
# print(type(t))
#
# t2 = 'python', 'world', 98
# print(t2, type(t2))
#
#
# t2 = ('python',)    # 元组中只有一个元素的时候需要添加， 否则是个字符串
# print(t2, type(t2))

#
# l1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# # 传一个字典
# l1.update({'a': 2, 'ad': 55})
#
# # 传关键字
# l1.update(a=44, b=33)
#
# # 传列表
# l1.update([('a', '00'), ('b', 99)])
#
# # 传zip函数
# l1.update(zip(['a', 'b'], [11, 22]))
#
# print(l1)

# capitalize()和title()的区别
# str1 = 'student Python'
# print(str1.swapcase())      # 把所有的大写变成小写，把所有的小写变成大写
#
# print(str1.capitalize())    # 把字符串的第一个字符变成大写，其余字符变成小写
# print(str1.title())         # 把每个单词的第一个字符变成大写，其余字符变成小写

# def func(*args):
#     print(args)
#
#
# func(10, 100)
#
#
# def func1(**args):
#     print(args)
#
#
# func1(a=10, b=100)
#
#
# def func2(a, b, *, c, d):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)
#     print('d=', d)
#
#
# func2(10, 20, c=30, d=40)

# lst = [
#     {'rating':[9.7, 2062397], 'id':'1', 'type':['犯罪', '剧情'], 'title':'肖申克的救赎', 'actors': ['Tim', 'Mogen']},
#     {'rating':[9.6, 2062396], 'id':'2', 'type':['爱情', '剧情'], 'title':'霸王别姬', 'actors': ['张国荣', '张丰毅']},
#     {'rating':[9.7, 2062337], 'id':'3', 'type':['喜剧', '剧情'], 'title':'阿甘正传', 'actors': ['Tom', 'Robin']}
# ]
# name = input('请输入需要查询的演员名称：')
# for item in lst:
#     actor_list = item['actors']
#     if name in actor_list:
#         print(f'{name}出演了{item["title"]}这部电影')

# import traceback
#
# try:
#     print(1 / 0)
# except:
#     traceback.print_exc()

# class Animal(object):
#     def eat(self):
#         print('动物会吃')
#
#
# class Dog(Animal):
#     def eat(self):
#         print('狗吃骨头。。。。')
#
#
# class Cat(Animal):
#     def eat(self):
#         print('猫吃鱼')
#
#
# class Person(object):
#     def eat(self):
#         print('任吃')
#
#
# def fun(a):
#     a.eat()
#
#
# fun(Dog())
# fun(Cat())
# fun(Animal())
# fun(Person())


# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class C(A, B):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # 特殊属性
# x = C('jack', 20)
# print(x.__dict__)       # 输出实例对象的属性字典
# print(C.__dict__)       # 输出类对象的属性和方法字典
# print(x.__class__)
# print(C.__bases__)      # C类的父类类型的元素
# print(C.__base__)
# print(C.__mro__)            # 输出类的层次结构
# print(A.__subclasses__())   # 输出A类的子类列表

# from selenium.webdriver import *
# import time
#
# Chrome().get(url='https://jira.souche-inc.com/login.jsp')
# time.sleep(1)
# Chrome().quit()

"""
个数可变的位置形参
个数可变的关键字形参
"""


# def func(*loc: tuple):
#     print(loc)
#
#
# func((10,))
# func((10, 100))
# func((10, 100, 1000))

# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome('./driver/chromedriver.exe')
#
#
# def func(loc: tuple):
#     return driver.find_element(*loc)
#
#
# driver.get(r'https://www.baidu.com/')
# input_box = ('id', 'kw')
# print(func(input_box))
# func(input_box).send_keys('我是百度输入框')
# time.sleep(2)
#
# driver.quit()

# __getatr__()的使用
class Test():
    def test1(self):
        pass

    def __getattr__(self, item):
        return 1


print(Test().a)
