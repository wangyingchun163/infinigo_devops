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

from ..models.models_business import Business
from .views_user import *

@check_login
@xframe_options_sameorigin
def business(request):
    username = request.session.get('username')
    userobj = User.objects.get(username=username)

    if userobj:
        # username = userobj.username
        if request.method == 'GET':
            data = Business.objects.all()

            # print("*" * 100)
            # print(data)
            # print("*" * 100)
            content = {'data': data}
            return render(request, 'devops/business/business.html', content)
        else:
            return HttpResponse('only get!')

# 列出所有业务 -- 暂未使用的接口
@check_login
@xframe_options_sameorigin
def all_business(request):
    data = Business.objects.all()
    content = {'data': data}
    return render(request, 'devops/business/business.html', content)

# 添加业务页面
@check_login
@xframe_options_sameorigin
def add_business(request):
    leader_list = User.objects.all()
    content = {'leader_list': leader_list}
    return render(request, 'devops/business/add_business.html', content)

# 添加业务提交保存
@check_login
@xframe_options_sameorigin
def add_business_commit(request):
    business = request.POST['business']
    project = request.POST['project']
    application = request.POST['application']
    leader = request.POST['leader']
    deploy_dir = request.POST['deploy_dir']
    log_dir = request.POST['log_dir']
    local_ip = request.POST['local_ip']
    port = request.POST['port']

    leader_objects = User.objects.get(id=leader)
    print('leader_objects is {}'.format(leader_objects))
    Business.objects.create(leader=leader_objects,
                            business=business,
                            project=project,
                            application=application,
                            deploy_dir=deploy_dir,
                            log_dir=log_dir,
                            local_ip=local_ip,
                            port=port)
    return redirect('/devops/business')

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
