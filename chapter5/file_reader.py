# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：file_reader.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/30 10:00
"""
from os.path import exists
from yaml import safe_load, safe_load_all


class File:

    def __init__(self, file_path: str):
        if not exists(file_path):
            raise FileNotFoundError
        self._file_path = file_path
        self._data = None


class YamlReader(File):

    def __init__(self, yaml_path: str, multi: bool = False):        # multi定义是否是多节读取，对应yaml文件里面可以使用---进行分节
        super(YamlReader, self).__init__(yaml_path)
        self._multi = multi

    @property
    def data(self):
        if not self._data:
            with open(self._file_path, 'r') as fp:
                if self._multi:
                    self._data = list(safe_load_all(fp))
                else:
                    self._data = list(safe_load(fp))

        return self._data


obj = YamlReader(r'D:\03APPInstaller\Python\Muke_1\chapter5\demo.yaml',multi=True)
print(obj.data)



