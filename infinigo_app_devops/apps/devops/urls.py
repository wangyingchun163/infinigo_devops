from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from .views import views_business , views_device , views_user ,views_domain ,views_supplier ,views_other
app_name = 'devops'
urlpatterns = [
    # 根路径则跳转到登录页
    path('', views_user.login),  # login

    #用户管理
    path('login/', views_user.login),  # login
    path('register/', views_user.register),  # register
    path('logout/', views_user.logout),  # 退出登录

    #首页
    path('index/', views_other.index),  # index首页
    path('dashboard/', views_other.dashboard),  # dashboard
    path('index/html_page', views_other.html_page),    # 嵌套页面打开

    #设备管理
    path('device/', views_device.device),  # device

    path('add_device/', views_device.add_device),  # device
    path('add_device_commit/', views_device.add_device_commit),  # device

    #path('all_device',views_device.all_device), # list device

    path('get_device/<int:device_id>/', views_device.get_device_by_id),   # 根据 id 查找设备的 dao 操作
    path('update_device/', views_device.update_device),  # 修改设备的 dao 操作

    path('search_device/',views_device.search_device),  # 搜索设备的 dao 操作

    path('delete_device/<int:device_id>',views_device.delete_device),  # 删除设备的 dao 操作

    #业务&项目&应用管理
    path('business/', views_business.business),  # device

    path('add_business/', views_business.add_business),  # device
    path('add_business_commit/', views_business.add_business_commit),  # device

    path('get_business/<int:business_id>/', views_business.get_business_by_id),   # 根据 id 查找设备的 dao 操作
    path('update_business/', views_business.update_business),  # 修改设备的 dao 操作

    path('search_business/',views_business.search_business),  # 搜索设备的 dao 操作

    path('delete_business/<int:business_id>',views_business.delete_business),  # 删除设备的 dao 操作

    # 域名管理
    path('domain/', views_domain.domain),  # device

    path('add_domain/', views_domain.add_domain),  # device
    path('add_domain_commit/', views_domain.add_domain_commit),  # device

    path('get_domain/<int:domain_id>/', views_domain.get_domain_by_id),  # 根据 id 查找设备的 dao 操作
    path('update_domain/', views_domain.update_domain),  # 修改设备的 dao 操作

    path('search_domain/', views_domain.search_domain),  # 搜索设备的 dao 操作

    path('delete_domain/<int:domain_id>', views_domain.delete_domain),  # 删除设备的 dao 操作

    # 供应商管理
    path('supplier/', views_supplier.supplier),  # 供应商

    path('add_domain/', views_supplier.add_supplier),  # device

]