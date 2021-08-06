# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python基础题
@File    ：P20.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/8/5 16:32
"""
# 矩形打印，输出十行十列 *
print('---------------打印矩形------------------')
for i in range(10):
    if i % 2 == 0:
        print("\033[0;30;42m* \033[0m" * 10)
    else:
        print('* ' * 10)

# 打印一个等边三角形
print('--------------打印三角形------------------')
for i in range(1, 11):
    print('* ' * i)
    i += 1

# 打印九九乘法表
print('--------------打印九九乘法表--------------')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end=' ')
    print()

print('-------------反向打印九九乘法表------------')
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end=' ')
    print()

print('-------------打印斐波那契数列--------------')
"""
斐波那契数列是，0,1,1,2,3,5... 
即前面两位数的和
"""


def fib():
    a = b = 1
    yield a
    yield b
    while b < 100:
        a, b = b, a + b
        yield b


for i in fib():
    print(i, end=' ')

print()

print('-------------百钱买百鸡--------------')
"""
一共有100块钱，需要买100只鸡
公鸡 == 3元 ==》33只
母鸡 == 1元 ==》100只
小鸡 == 0.5元 ==》 200只
问：100块钱买100只鸡，一共有多少种方案
"""
num = 0
count = 0       # 用来计算程序一共运行了多少次
for gj in range(0, 34):
    for mj in range(0, 101):
        for xj in range(0, 201):
            count += 1          # 计算程序一共运行了多少次
            if gj+mj+xj == 100 and gj*3+mj+xj*0.5 == 100:
                print(f'公鸡买{gj}只，母鸡买{mj}只，小鸡买{xj}只')
                num += 1
print(num)
print(f'程序一共运行了{count}次')       # 采用多层嵌套的方式特别影响性能，可以对代码进行优化改造，来提升代码的运行效率


# 对代码进行优化如下
print('-----------------代码优化---------------')
num1 = 0
count1 = 0       # 用来计算程序一共运行了多少次
for gj in range(0, 34):
    for mj in range(0, 101):
        xj = 100 - gj - mj
        count1 += 1          # 计算程序一共运行了多少次
        if gj*3+mj+xj*0.5 == 100:
            print(f'公鸡买{gj}只，母鸡买{mj}只，小鸡买{xj}只')
            num1 += 1
print(num1)
print(f'程序一共运行了{count1}次')


