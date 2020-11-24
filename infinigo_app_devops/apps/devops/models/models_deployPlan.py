#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           : models_deployPlan.py
@Time           : 2020/11/13/11/2020 11:39
@Site           : 
@Software       : PyCharm
@project        : infinigo_devops
@description    : PyCharm  infinigo_devops  models_deployPlan.py
@Author         : eddie
@Email          : eddie.wang@infinigo.cn
@ide            : PyCharm
"""

from django.db import models
from .models_user import User
from .models_business import Business
from .models_device import Device

# Create your models here.

class DeployPlan(models.Model):
    # id = models.AutoField(primary_key=True)  #id
    # business = models.CharField(max_length=32)  # 业务线
    # project = models.CharField(max_length=32)   # 项目名
    # application = models.CharField(max_length=32)  # 应用名
    # main_version = models.CharField(max_length=3)  # 主版本号
    # second_version = models.CharField(max_length=3)  # 二级版本号
    # third_version = models.CharField(max_length=3)  # 三级版本号
    # git_version = models.CharField(max_length=32)  # Git版本号
    # deploy_time = models.CharField(max_length=8)  # 部署时间
    # deploy_ip = models.CharField(max_length=15)  # 部署的目标机器
    # UAT_status = models.CharField(max_length=1)  # UAT环境发布状态
    # PREIDC_status = models.CharField(max_length=1)  # PREIDC环境发布状态
    # IDC_status = models.CharField(max_length=1)  # IDC环境发布状态
    # exec_status = models.CharField(max_length=1)  # 当前正在发布锁
    # leader_id = models.CharField(max_length=50)  # 操作员

    id = models.AutoField(primary_key=True)  #id
    business = models.ForeignKey(Business, related_name="Business_business", on_delete=models.DO_NOTHING)  # 业务线
    project = models.ForeignKey(Business, related_name="Business_project", on_delete=models.DO_NOTHING)  # 业务线
    application = models.ForeignKey(Business, related_name="Business_application", on_delete=models.DO_NOTHING)  # 业务线
    main_version = models.IntegerField(max_length=3)  # 主版本号
    second_version = models.IntegerField(max_length=3)  # 二级版本号
    third_version = models.IntegerField(max_length=3)  # 三级版本号
    git_url = models.CharField(max_length=32)  # Git版本号
    git_version = models.CharField(max_length=32)  # Git版本号
    deploy_time = models.DateTimeField(max_length=8)  # 部署时间
    device = models.ForeignKey(Device, related_name="Device_device", on_delete=models.DO_NOTHING)  # 部署的目标机器
    UAT_status = models.IntegerField(max_length=1)  # UAT环境发布状态
    PREIDC_status = models.IntegerField(max_length=1)  # PREIDC环境发布状态
    IDC_status = models.IntegerField(max_length=1)  # IDC环境发布状态
    exec_status = models.IntegerField(max_length=1)  # 当前正在发布锁
    leader = models.ForeignKey(User, related_name="User_leader", on_delete=models.DO_NOTHING)  # 操作员

    def __str__(self):
        return '[id={}, business={}, project={}, application={}, main_version={}, second_version={}, third_version={}, git_url={},\
               git_version={}, deploy_time={}, device={}, UAT_status={}, PREIDC_status={}, IDC_status={}, exec_status={}, \
               leader={}]'.format(self.id, self.business, self.project, self.application, self.main_version, self.second_version,
                                  self.third_version, self.git_url, self.git_version, self.deploy_time, self.device, self.UAT_status,
                                  self.PREIDC_status, self.IDC_status, self.exec_status, self.leader)