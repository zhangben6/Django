from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^01-add-author/$', views.add_author),
    url(r'^01-add-publisher/$',views.add_punlisher),
    url(r'^01-add-book/$',views.add_book),
    url(r'^02-query/$',views.query),
    url(r'^03-queryall/$',views.queryall),
    url(r'^04-filter/$',views.filter_views),
    url(r'^05-update/(\d+)/$',views.update),
    #不带分组的聚合查询
    url(r'06-aggregate/$',views.aggregate),
    # 带分组的聚合查询
    url(r'07-annotate/$',views.annotate),
    url(r'^08-update/$',views.update08),
    # 删除03-queryall中的实体类
    url(r'^09-delete/(\d+)/$',views.delete),

]

# ORM关系映射的相关路由(数据处理)
urlpatterns +=[
    url(r'^10-oto/$',views.oto_views),
    url(r'^11-otm/$',views.otm_views),
    url(r'^12-mtm/$',views.mtm_views),
]