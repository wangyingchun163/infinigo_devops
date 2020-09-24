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

from ..models.models_user import User

#注册接口
def register(request):
    if request.method == 'GET':
        return render(request, 'devops/user/register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('password')
        if not username:
            return HttpResponse('用户名不能为空')
        if not password:
            return HttpResponse('密码不能为空')
        if not repeat_password:
            return HttpResponse('确认密码不能为空')
        if username and password and repeat_password:
            if password == repeat_password:
                # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
                user_project = User.objects.filter(username=username).first()
                if user_project:
                    return HttpResponse('用户名已存在')
                else:
                    User.objects.create(username=username, password=password).save()
                    return redirect('/devops/login/')
            else:
                return HttpResponse('两次输入的密码不一致')

#验证登录状态
def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('/devops/login/')
    return inner

#登录接口
def login(request):
    if request.method == 'GET':
        return render(request, 'devops/user/login.html')
    if request.method == 'POST':
        # 这里判断，如果是name值为login的，则执行此段代码
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username, password=password).first()
            if user_obj:
                # return HttpResponse('登录成功')
                request.session['is_login'] = '1'
                request.session['username'] = username
                return redirect('/devops/index/')
            else:
                #return redirect('/devops/login/',{"error_info":"用户名或者密码错误！"})
                return render(request, 'devops/user/login.html',{"error_info":"用户名或者密码错误！"})

        elif 'register' in request.POST:
            return redirect('/devops/register/')
        else:
            return HttpResponse('你到底想干什么？')

# 退出登录接口
def logout(request):
    request.session.flush()
    return redirect('/devops/login/')

#登录成功时打开主页面接口
@check_login
def index(request):
    username = request.session.get('username')
    userobj = User.objects.filter(username=username)
    if userobj:
        return render(request, 'devops/index.html',{"userinfo":userobj[0]})
    else:
        return HttpResponse('未登录，请先登录！')
