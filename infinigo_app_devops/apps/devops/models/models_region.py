#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           : models_region.py
@Time           : 2020/11/13/11/2020 11:53
@Site           : 
@Software       : PyCharm
@project        : infinigo_devops
@description    : PyCharm  infinigo_devops  models_region.py
@Author         : eddie
@Email          : eddie.wang@infinigo.cn
@ide            : PyCharm
"""

from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return '[name={}]'.format(self.name)

class City(models.Model):
    name = models.CharField(max_length=5)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '[name={}, province={}]'.format(self.name, self.province)

class Person(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    visitation = models.ForeignKey(City, related_name="visitor", on_delete=models.DO_NOTHING)
    hometown = models.ForeignKey(City, related_name="birth", on_delete=models.DO_NOTHING)
    living = models.ForeignKey(City, related_name="citizen", on_delete=models.DO_NOTHING)

    def __str__(self):
        return '[firstname={}, lastname={}, visitation={}, hometown={}, living={}]'.format(
            self.firstname, self.lastname, self.visitation, self.hometown, self.living)