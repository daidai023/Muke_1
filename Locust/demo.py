# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Crown项目，使用pytest实现自动化
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：Daisy
@Date    ：2021/7/27 17:03
"""
from locust import HttpUser, TaskSet, task


class TestIndex(TaskSet):
    @task
    def get_index(self):
        self.client.get("/")
        print("here")


class WebSite(HttpUser):
    task_set = TestIndex
    min_wait = 1000
    max_wait = 2000
