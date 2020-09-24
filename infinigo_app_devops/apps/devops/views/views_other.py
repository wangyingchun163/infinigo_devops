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

from .views_user import *


#index
@check_login
@xframe_options_sameorigin
def index(request):
    username = request.session.get('username')
    userobj = User.objects.filter(username=username)
    if userobj:
        return render(request, 'devops/index.html', {"userinfo": userobj[0]})
    else:
        return HttpResponse('未登录，请先登录！')

#index
def favicon(request):
    return render(request, 'devops/media/favicon.ico')


#控制台接口
@check_login
@xframe_options_sameorigin
def dashboard(request):
    username = request.session.get('username')
    userobj = User.objects.filter(username=username)
    if userobj:
        return render(request, 'devops/dashboard.html', {"userinfo": userobj[0]})
    else:
        return HttpResponse('未登录，请先登录！')

#左侧栏导航点击接口
@check_login
@xframe_options_sameorigin
def html_page(request):
    new_url = ""
    for new_url in request.GET.getlist('new_url'):
        #return render(request, "{0}".format(new_url))
        return redirect("{0}".format(new_url))
        #return HttpResponse(new_url)
