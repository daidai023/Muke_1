# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：demo1.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/29 10:42
"""
import random
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client.get('/hello')
        self.client.get('/world')

    @task(3)
    def view_item(self):
        item_id = random.randint(1, 10000)
        self.client.get(f'/item?id={item_id}', name='/item')

    def on_start(self):
        self.client.post('/login', {"username:": "BiqiLiu", "password": "anM5sm"})
