# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：typing_union.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/14 14:30
"""
from typing import List, Union


def func(a: int, string: str) -> List[str or int]:
    list1 = []
    list1.append(a)
    list1.append(string)
    print(list1)


func(88, ['999'])


def get_next_id(id: int) -> Union[int, None]:
    if not isinstance(id, int):
        return
    if id > 1:
        return id
    return None


print(get_next_id('999'))
print(get_next_id(999))
