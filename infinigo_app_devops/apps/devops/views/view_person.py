#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           : view_person.py
@Time           : 2020/11/13/11/2020 16:42
@Site           : 
@Software       : PyCharm
@project        : infinigo_devops
@description    : PyCharm  infinigo_devops  view_person.py
@Author         : eddie
@Email          : eddie.wang@infinigo.cn
@ide            : PyCharm
"""

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from functools import wraps
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.
from django.conf import settings    # 获取 settings.py 里边配置的信息
import os

# from ..models.models_region import Province, Person, City
#
# def person(request):
#     person1 = Person.objects.select_related().all()
#     print(person1)
