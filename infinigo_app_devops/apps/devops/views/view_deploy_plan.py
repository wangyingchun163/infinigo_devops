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

from ..models.models_deployPlan import DeployPlan
from ..models.models_user import User
from ..models.models_business import Business
from ..models.models_device import Device
from .views_user import check_login
# # from .views_business import *
# # from .views_device import *

@check_login
@xframe_options_sameorigin
def deploy(request):
    username = request.session.get('username')
    userobj = User.objects.get(username=username)

    if userobj:
        # username = userobj.username
        if request.method == 'GET':
            data = DeployPlan.objects.all()
            content = {'data': data}
            return render(request, 'devops/deploy/deploy.html', content)
        else:
            return HttpResponse('only get!')

# 列出所有业务 -- 暂未使用的接口
@check_login
@xframe_options_sameorigin
def all_deploy(request):
    data = deploy.objects.all()
    content = {'data': data}
    return render(request, 'devops/deploy/deploy.html', content)

# 添加业务页面
@check_login
@xframe_options_sameorigin
def add_deploy(request):
    # leader_list = User.objects.all()
    # device_list = Device.objects.all()
    # business_list = Business.objects.all()
    # content = {'leader_list': leader_list, 'device_list': device_list, 'business_list': business_list}
    # return render(request, 'devops/deploy/add_deploy.html', content)

    leader_list = User.objects.filter(username__isnull=False).distinct().order_by('username')
    device_list = Device.objects.filter(local_ip__isnull=False).distinct().order_by('local_ip')
    business_list = Business.objects.filter(business__isnull=False).distinct().order_by('business')
    project_list = Business.objects.filter(project__isnull=False).distinct().order_by('project')
    application_list = Business.objects.filter(application__isnull=False).distinct().order_by('application')
    content = {'leader_list': leader_list, 'device_list': device_list, 'business_list': business_list, 'project_list': project_list, 'application_list': application_list}

    # print("==="*100)
    # print("leader_list is {}".format(leader_list))
    # print("device_list is {}".format(device_list))
    # print("business_list is {}".format(business_list))
    # print("project_list is {}".format(project_list))
    # print("application_list is {}".format(application_list))
    # print("===" * 100)
    print(content)
    return render(request, 'devops/deploy/add_deploy.html', content)

# 添加业务提交保存
@check_login
@xframe_options_sameorigin
def add_deploy_commit(request):
    print(request.POST)
    business = request.POST['business']
    project = request.POST['project']
    application = request.POST['application']
    main_version = request.POST.get('main_version')
    second_version = request.POST.get('second_version')
    third_version = request.POST.get('third_version')
    git_url = request.POST.get('git_url')
    git_version = request.POST.get('git_version')
    device = request.POST['device']
    leader = request.POST['leader']

    business_objects = Business.objects.get(id=business)
    project_objects = Business.objects.get(id=project)
    application_objects = Business.objects.get(id=application)
    leader_objects = User.objects.get(id=leader)
    device_objects = Device.objects.get(id=device)
    DeployPlan.objects.create(business=business_objects,
                            project=project_objects,
                            application=application_objects,
                            main_version=main_version,
                            second_version=second_version,
                            third_version=third_version,
                            git_url=git_url,
                            git_version=git_version,
                            device=device_objects,
                            leader=leader_objects)
    return redirect('/devops/deploy')

# 修改业务页面
@check_login
@xframe_options_sameorigin
def get_business_by_id(request,business_id):
    business = Business.objects.filter(id=business_id)
    leader_all = User.objects.all()
    content = {'data': business , "leader_all":leader_all}
    # content = {'data': business}
    print(content)
    return render(request,'devops/business/update_business.html', content)

# 修改业务保存
@check_login
@xframe_options_sameorigin
def update_business(request):
    id = request.POST['id']
    business = request.POST['business']
    project = request.POST['project']
    application = request.POST['application']
    deploy_dir = request.POST['deploy_dir']
    log_dir = request.POST['log_dir']
    local_ip = request.POST['local_ip']
    port = request.POST['port']
    leader = request.POST['leader']
    Business.objects.filter(id=id).update(business=business, project=project, application=application,
                                          deploy_dir=deploy_dir, log_dir=log_dir, local_ip=local_ip, port=port, leader=leader)
    return redirect('/devops/business')

#查询业务
@check_login
@xframe_options_sameorigin
def search_business(request):
    project = request.GET['project']
    project_obj = Business.objects.filter(project__icontains=project)
    content={'data':project_obj}
    return render(request,'devops/business/business.html', content)

#删除业务
@check_login
@xframe_options_sameorigin
def delete_business(request,business_id):
    Business.objects.filter(id=business_id).delete()
    return redirect('/devops/business')
