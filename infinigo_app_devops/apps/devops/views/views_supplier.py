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

from ..models.models_supplier import Supplier
from .views_user import *

@check_login
@xframe_options_sameorigin
def supplier(request):
    username = request.session.get('username')
    userobj = User.objects.filter(username=username)
    if userobj:
        if request.method == 'GET':
            data = Supplier.objects.all()
            content = {'data': data}
            return render(request, 'devops/supplier/supplier.html', content)
        else:
            return HttpResponse('only get!')

# 列出所有业务 -- 暂未使用的接口
@check_login
@xframe_options_sameorigin
def all_supplier(request):
    data = supplier.objects.all()
    content={'data': data}
    return render(request, 'devops/supplier/supplier.html', content)

# 添加业务页面
@check_login
@xframe_options_sameorigin
def add_supplier(request):
    leader_id_list = User.objects.all()
    content = {'leader_id_list': leader_id_list}
    return render(request, 'devops/supplier/add_supplier.html', content)

# 添加业务提交保存
@check_login
@xframe_options_sameorigin
def add_supplier_commit(request):
    company = request.POST['company']
    address = request.POST['address']
    idc_address = request.POST['idc_address']
    contact = request.POST['contact']
    contact_phone = request.POST['contact_phone']
    assistant = request.POST['assistant']
    assistant_phone = request.POST['assistant_phone']
    #print("{}{}{}{}{}{}{}".format(company,address,idc_address,contact,contact_phone,assistant,assistant_phone))

    supplier_obj = Supplier()
    supplier_obj.company = company
    supplier_obj.address = address
    supplier_obj.idc_address = idc_address
    supplier_obj.contact = contact
    supplier_obj.contact_phone = contact_phone
    supplier_obj.assistant = assistant
    supplier_obj.assistant_phone = assistant_phone
    print("{}{}{}{}{}{}{}".format(supplier_obj.company,supplier_obj.address,supplier_obj.idc_address,supplier_obj.contact,
                                  supplier_obj.contact_phone,supplier_obj.assistant,supplier_obj.assistant_phone))

    supplier_obj.save()
    return redirect('/devops/supplier')

# 修改业务页面
@check_login
@xframe_options_sameorigin
def get_supplier_by_id(request,supplier_id):
    supplier = Supplier.objects.filter(id=supplier_id)
    #leader_id = supplier.objects.filter(id=supplier_id).values("leader_id").first()['leader_id']
    #leader_id_name = User.objects.filter(id=leader_id).values("username").first()
    #print(leader_id_name)
    #leader_id_all = User.objects.all()
    #content = {'data': supplier , "leader_id_name": leader_id_name ,"leader_id_all":leader_id_all}
    content = {'data': supplier}
    return render(request,'devops/supplier/update_supplier.html',content)

# 修改业务保存
@check_login
@xframe_options_sameorigin
def update_supplier(request):
    id = request.POST['id']
    company = request.POST['company']
    address = request.POST['address']
    idc_address = request.POST['idc_address']
    contact = request.POST['contact']
    contact_phone = request.POST['contact_phone']
    assistant = request.POST['assistant']
    assistant_phone = request.POST['assistant_phone']

    Supplier.objects.filter(id=id).update(company=company,address=address,idc_address=idc_address,
                                          contact=contact,contact_phone=contact_phone,assistant=assistant,assistant_phone=assistant_phone)
    return redirect('/devops/supplier')

#查询业务
@check_login
@xframe_options_sameorigin
def search_supplier(request):
    company = request.GET['company']
    supplier_obj = Supplier.objects.filter(company__icontains=company)
    content={'data':supplier_obj}
    return render(request,'devops/supplier/supplier.html', content)

#删除业务
@check_login
@xframe_options_sameorigin
def delete_supplier(request,supplier_id):
    Supplier.objects.filter(id=supplier_id).delete()
    return redirect('/devops/supplier')

