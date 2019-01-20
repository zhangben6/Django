from django.conf.urls import url
from . import views

urlpatterns=[
    # 访问路径 localhost:8000/
    url(r'^$',views.index),

    # 访问路径 localhost:8000/login
    url(r'^login/$',views.login),

    #匹配 register/
    url(r'^register/$',views.register),

]