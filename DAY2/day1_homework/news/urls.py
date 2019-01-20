from django.conf.urls import url
from . import views

urlpatterns=[

    # 访问路径为空
    url(r'^$', views.index),

]