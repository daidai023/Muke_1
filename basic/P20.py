# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
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

print('=====方式一:使用yield实现=====')


def fib():
    a = b = 1
    yield a
    yield b
    while b < 100:
        a, b = b, a + b
        yield b


for i in fib():
    print(i, end=' ')

print('=====方式二:=====')
num = int(input('请输入你要显示的斐波那契数列的个数：'))
n1 = 0
n2 = 1
count =
if num <= 0:
    print('请输入一个正整数：')
elif num == 1:
    print(f'斐波那契数列为{n1}')
elif num == 2:
    print(f'斐波那契数列为{n1} {n2}')
else:




