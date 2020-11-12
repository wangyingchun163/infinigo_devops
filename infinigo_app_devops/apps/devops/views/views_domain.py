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

from ..models.models_domain import Domain
from ..models.models_user import User
from .views_user import *

@check_login
@xframe_options_sameorigin
def domain(request):
    username = request.session.get('username')
    userobj = User.objects.filter(username=username)
    if userobj:
        if request.method == 'GET':
            data = Domain.objects.all()
            print(data)
            content={'data': data }
            return render(request, 'devops/domain/domain.html', content)
        else:
            return HttpResponse('only get!')

# 列出所有业务 -- 暂未使用的接口
@check_login
@xframe_options_sameorigin
def all_domain(request):
    data = domain.objects.all()
    content={'data': data}
    return render(request, 'devops/domain/domain.html', content)

# 添加业务页面
@check_login
@xframe_options_sameorigin
def add_domain(request):
    leader_list = User.objects.all()
    content = {'leader_list': leader_list}
    return render(request, 'devops/domain/add_domain.html' , content)

# 添加业务提交保存
@check_login
@xframe_options_sameorigin
def add_domain_commit(request):
    domain = request.POST['domain']
    ip = request.POST['ip']
    cname = request.POST['cname']
    remark = request.POST['remark']

    domain_obj = Domain()
    domain_obj.domain = domain
    domain_obj.ip = ip
    domain_obj.cname = cname
    domain_obj.remark = remark

    domain_obj.save()
    return redirect('/devops/domain')

# 修改业务页面
@check_login
@xframe_options_sameorigin
def get_domain_by_id(request,domain_id):
    domain = Domain.objects.filter(id=domain_id)
    #leader_id = Domain.objects.filter(id=domain_id).values("leader").first()['leader']
    #leader_name = User.objects.filter(id=leader_id).values("username").first()
    #print(leader_name)
    #leader_all = User.objects.all()
    #content = {'data': domain , "leader_name": leader_name ,"leader_all":leader_all}
    content = {'data': domain}
    return  render(request,'devops/domain/update_domain.html',content)

# 修改业务保存
@check_login
@xframe_options_sameorigin
def update_domain(request):
    id = request.POST['id']
    domain = request.POST['domain']
    ip = request.POST['ip']
    cname = request.POST['cname']
    remark = request.POST['remark']

    Domain.objects.filter(id=id).update(domain=domain,ip=ip,cname=cname,remark=remark)
    return redirect('/devops/domain')

#查询业务
@check_login
@xframe_options_sameorigin
def search_domain(request):
    domain = request.GET['domain']
    domain_obj = Domain.objects.filter(domain__icontains=domain)
    content={'data':domain_obj}
    return render(request,'devops/domain/domain.html', content)

#删除业务
@check_login
@xframe_options_sameorigin
def delete_domain(request,domain_id):
    Domain.objects.filter(id=domain_id).delete()
    return redirect('/devops/domain')

