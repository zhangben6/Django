"""day1_homework URL Configuration

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


# 适用于 version 2.0
# import index.views as index_views



urlpatterns = [

    url(r'^admin/', admin.site.urls),

    #当访问路径是localhost:8000/index/xxxx 的时候,要将地址交给music的urls进一步做处理
    url(r'^index/',include('index.urls')),

    # 当访问路径是localhost:8000/music/xxxx 的时候
    url(r'^music/',include('music.urls')),

    # 访问路径 localhost:8000/news/xxxx
    url(r'^news/',include('news.urls')),

    # 访问路径 localhost:8000/sport/xxxx
    url(r'^sport/',include('sport.urls')),



# ---------------------------------------------------

    # version 2.0
    # 通过主路由配置文件直接进入到应用中的视图函数处理(跨过应用中的路由)
    # localhost:8000/login
    #url(r'^login/$',index_views.login),

    #localhost:8000/register
    #url(r'^register/$',index_views.register),

    # localhost:8000/  交给index包中views.py中的index()视图函数处理
    #url(r'^$',index_views.index),

# ------------------------------------------------------

    # 分布式路由管理系统   最终版本 version 3.0
    # 当访问路径不是 admin/xxx , music/xxx ...  一律要交给index应用中的路由系统去处理
    url(r'^',include('index.urls')),

]
