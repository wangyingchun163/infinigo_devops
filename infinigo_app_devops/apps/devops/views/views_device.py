from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from functools import wraps
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
import hashlib

# Create your views here.
from django.conf import settings    # 获取 settings.py 里边配置的信息
import os

from ..models.models_device import Device ,User
from .views_user import *

# 密码hash存储


#打开设备列表页面
@check_login
@xframe_options_sameorigin
def device(request):
    username = request.session.get('username')
    userobj = User.objects.filter(username=username)
    if userobj:
        if request.method == 'GET':
            data = Device.objects.all()
            content = {'data': data}
            return render(request, 'devops/device/device.html', content)
            #return render(request, 'devops/device/device.html', {"userinfo": userobj[0]})
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

    #关联表获取对象，方便为插入赋值
    # leader_id = User.objects.get(username = leader)
    # print(leader_id.username)

    device_obj = Device()
    device_obj.name = name
    device_obj.local_ip = local_ip
    device_obj.public_ip = public_ip
    device_obj.ssh_port = ssh_port
    device_obj.environment = environment
    device_obj.address = address
    device_obj.user = user
    h = hashlib.sha256()
    device_obj.password = h.update(bytes(password, encoding='utf-8'))
    device_obj.password = h.hexdigest()
    device_obj.t_image = t_image
    device_obj.leader_id = leader_id
    # 存访问路径到数据库
    device_obj.t_image = os.path.join("/static/media/", t_image.name)
    device_obj.save()

    return redirect('/devops/device')

# 修改设备页面
@check_login
@xframe_options_sameorigin
def get_device_by_id(request,device_id):
    device = Device.objects.filter(id=device_id)
    content = {'data': device}
    print("content is {}".format(content))
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
    print("{},{},{}".format(id,name,password))

    t_image = request.FILES['t_image']
    leader = request.POST['leader']
    fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
    with open(fname, 'wb') as pic:
        for c in t_image.chunks():
            pic.write(c)

    #关联表获取对象，方便为插入赋值
    leader_id = User.objects.get(username = leader)
    print(leader_id.username)
    t_image = os.path.join("/static/media/", t_image.name)
    Device.objects.filter(id=id).update(name=name, local_ip=local_ip, public_ip=public_ip,
                                        ssh_port=ssh_port, user=user, password=password,
                                        environment=environment, address=address,
                                        t_image=t_image, leader=leader_id)
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
