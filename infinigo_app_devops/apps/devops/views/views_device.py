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

import hashlib
from ..models.models_device import Device
from .views_user import *

#打开设备列表页面
@check_login
@xframe_options_sameorigin
def device(request):
    username = request.session.get('username')
    userobj = User.objects.get(username=username)

    if userobj:
        # username = userobj.username
        data = Device.objects.all()
        content = {'data': data}
        return render(request, 'devops/device/device.html', content)
    else:
        return HttpResponse('only get!')

# 列出所有设备 -- 暂未使用的接口
@check_login
@xframe_options_sameorigin
def all_device(request):
    data = Device.objects.all()
    content={'data': data}
    return render(request, 'devops/device/device.html', content)

# 添加设备页面
@check_login
@xframe_options_sameorigin
def add_device(request):
    leader_list = User.objects.all()
    content = {'leader_list': leader_list}
    return render(request, 'devops/device/add_device.html', content)

# 添加设备提交保存
@check_login
@xframe_options_sameorigin
def add_device_commit(request):
    name = request.POST['name']
    local_ip = request.POST['local_ip']
    public_ip = request.POST['public_ip']
    environment = request.POST['environment']
    address = request.POST['address']
    ssh_port = request.POST['ssh_port']
    user = request.POST['user']
    password = request.POST['password']
    t_image = request.FILES['t_image']
    leader_id = request.POST['leader']

    fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
    with open(fname, 'wb') as pic:
        for c in t_image.chunks():
            pic.write(c)

    h = hashlib.sha256()
    device_password = h.update(bytes(password, encoding='utf-8'))
    device_password = h.hexdigest()
    device_t_image = t_image
    device_t_image = os.path.join("/static/media/", t_image.name)

    leader_objects = User.objects.get(id=leader_id).id
    Device.objects.create(leader_id=leader_objects,
                            name=name,
                            local_ip=local_ip,
                            public_ip=public_ip,
                            environment=environment,
                            address=address,
                            ssh_port=ssh_port,
                            user=user,
                            password=device_password,
                            t_image=device_t_image)
    return redirect('/devops/device')

# 修改设备页面
@check_login
@xframe_options_sameorigin
def get_device_by_id(request,device_id):
    device = Device.objects.filter(id=device_id)
    leader_all = User.objects.all()
    content = {'data': device , "leader_all":leader_all}
    return render(request,'devops/device/update_device.html',content)

# 修改设备保存
@check_login
@xframe_options_sameorigin
def update_device(request):
    id = request.POST['id']
    name = request.POST['name']
    local_ip = request.POST['local_ip']
    public_ip = request.POST['public_ip']
    ssh_port = request.POST['ssh_port']
    environment = request.POST['environment']
    address = request.POST['address']
    user = request.POST['user']
    passwordstr = request.POST['password']
    h = hashlib.sha256()
    h.update(bytes(passwordstr, encoding='utf-8'))
    password = h.hexdigest()

    t_image = request.FILES['t_image']
    leader = request.POST['leader']
    fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
    with open(fname, 'wb') as pic:
        for c in t_image.chunks():
            pic.write(c)

    t_image = os.path.join("/static/media/", t_image.name)
    Device.objects.filter(id=id).update(name=name, local_ip=local_ip, public_ip=public_ip,
                                        ssh_port=ssh_port, user=user, password=password,
                                        environment=environment, address=address,
                                        t_image=t_image, leader=leader)
    return redirect('/devops/device')

#查询设备
@check_login
@xframe_options_sameorigin
def search_device(request):
    name = request.GET['name']
    device = Device.objects.filter(name__icontains=name)
    content={'data':device}
    return render(request,'devops/device/device.html', content)

#删除设备
@check_login
@xframe_options_sameorigin
def delete_device(request,device_id):
    Device.objects.filter(id=device_id).delete()
    return redirect('/devops/device')
