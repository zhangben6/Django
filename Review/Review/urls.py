"""Review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

#urlpatterns列表的作用为 用于描述路由-视图的映射,里面包含若干个url()从而来具体描述路由-视图的映射关系
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 带参数的url处理
    url(r'^demo1/(\d{3})/$',views.demo1),

    #应用fuxi 下的url处理,今日笔记代码都在此
    url(r'^fuxi/',include('fuxi.urls')),


    # 分布式路由管理系统 -- 部署在index应用中,包括 index(首页) login(登录页) register(注册页)
    url(r'^',include('index.urls'))
]
