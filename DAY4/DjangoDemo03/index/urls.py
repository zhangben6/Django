from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^01-add-author/$',views.add_author),
    url(r'^01-add-publisher/$',views.add_publisher),
    url(r'^01-add-book/$',views.add_book),
    url(r'^02-query/$',views.query),
    url(r'^03-queryall/$',views.queryall),
    url(r'^04-filter/$',views.filter_views),
    url(r'^05-update/(\d+)/$',views.update),



    ###########################################
    # django第四天笔记
    ############################################
    url(r'^06-aggregate/$',views.aggregate),
    # 带分组的查询 annotate
    url(r'07-annotate/$',views.annotate),
    # 修改实体类中的属性
    url(r'08-update/$',views.update08),
    # 删除03-query的实体类
    url(r'^09-delete/(\d+)/$',views.delete09),


]

# 关系映射相关的路由设置
urlpatterns +=[
    url(r'^10-oto/$',views.oto_views),
    url(r'^11-dtd/$',views.dtd_views),
    url(r'^11-otm/$',views.otm_views),
    url(r'^12-mtm/$',views.mtm_views),
]