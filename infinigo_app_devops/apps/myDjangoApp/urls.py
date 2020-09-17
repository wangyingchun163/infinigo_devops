#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           : urls.py
@Time           : 2020/9/16/09/2020 17:21
@Site           : 
@Software       : PyCharm
@project        : infinigo_devops
@description    : PyCharm  infinigo_devops  urls.py
@Author         : eddie
@Email          : eddie.wang@infinigo.cn
@ide            : PyCharm
"""

from django.conf.urls import url, include
from .views import add_book, show_books

urlpatterns = [
    url('add_book/', add_book),
    url('show_books/', show_books),
]