环境准备
Python3.7/Mysql5.7/Pycharm/Node/Django3.0

基础步骤
创建Django项目/数据迁移/更换数据库为Mysql

创建Django项目
(venv) ➜ django-admin startproject infinigo_app_devops
(venv) ➜ pip install mysqlclient

配置settings.py文件，配置Mysql数据库引擎
执行数据库同步
python manage.py migrate

创建APP
(venv) ➜ python manage.py startapp myDjangoApp

Settings

models.py

views.py

APP级urls.py

项目级urls.py

步数据库
python manage.py makemigrations myDjangoApp
python manage.py migrate

测试接口
http://127.0.0.1:8000/api/add_book/?book_name=davieyang
HTTP/1.1 200 OK
Content-Length: 34
Content-Type: application/json
Date: Sun, 15 Dec 2019 09:11:12 GMT
Server: WSGIServer/0.2 CPython/3.7.4
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
{
    "error_num": 0,
    "msg": "success"
}


http://127.0.0.1:8000/api/add_book/?book_name=测试开发技术
HTTP/1.1 200 OK
Content-Length: 34
Content-Type: application/json
Date: Sun, 15 Dec 2019 09:11:44 GMT
Server: WSGIServer/0.2 CPython/3.7.4
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
{
    "error_num": 0,
    "msg": "success"
}




Vue部分
环境准备
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm install -g vue-cli


新建Vue工程
vue-init webpack frontend
安装 vue 依赖模块
cd frontend
cnpm install
cnpm install vue-resource
cnpm install element-ui

在frontend目录src下包含入口文件main.js，入口组件App.vue等。后缀为vue的文件是Vue.js框架定义的单文件组件，其中标签中的内容可以理解为是类html的页面结构内容。
在src/component文件夹下新建一个名为Home.vue的组件，通过调用之前在Django上写好的api，实现添加书籍和展示书籍信息的功能。在样式组件上我们使用了饿了么团队推出的element-ui，这是一套专门匹配Vue.js框架的功能样式组件。由于组件的编码涉及到了很多js、html、css的知识，并不是本文的重点，因此在此只贴出部分代码：

Home.vue文件代码
在src/router目录的index.js中，我们把新建的Home组件，配置到vue-router路由中
在src/main.js文件中，导入element-ui、vue-resource库
如果出现跨域问题，需要在Django层注入header，用Django的第三方包django-cors-headers来解决跨域问题：
pip install django-cors-headers

在前端工程frontend目录下，输入npm run dev启动node自带的服务器

在前端工程frontend目录下，输入npm run build，如果项目没有错误的话，就能够看到所有的组件、css、图片等都被webpack自动打包到dist目录下了

整合Django和Vue.js前端
目前已经分别完成了Django后端和Vue.js前端工程的创建和编写，但实际上它们是运行在各自的服务器上，和我们的要求是不一致的。因此我们须要把Django的TemplateView指向我们刚才生成的前端dist文件即可
找到project目录的urls.py，使用通用视图创建最简单的模板控制器，访问 『/』时直接返回 index.html
上一步使用了Django的模板系统，所以需要配置一下模板使Django知道从哪里找到index.html。在project目录的settings.py下
我们还需要配置一下静态文件的搜索路径。同样是project目录的settings.py下


Windows环境配置
Node.js
下载安装node.js， 官方下载地址https://nodejs.org/en/，下载符合自己操作系统版本的即可，安装也是傻瓜式安装。
安装完成后，在命令行输入node，如下展示则表示成功
C:\Users\Administrator>node -v
v8.17.0

配置cnpm并安装vue-cli
在命令行输入： npm install -g cnpm --registry=https://registry.npm.taobao.org (https://registry.npm.taobao.org/)
之后cnpm install -g vue-cli命令行展示如下内容，则表示成功

安装完成后，在命令行输入vue，如下所示，则表示成功

cnpm install element-ui
cnpm install coffeescript

# vue参考
很显然vue-admin-beautiful已经完全后来者居上了
开源地址：https://github.com/chuzhixin/vue-admin-beautiful/
演示地址：https://chu1204505056.gitee.io/vue-admin-beautiful/
pro演示地址：https://chu1204505056.gitee.io/vue-admin-beautiful-pro/