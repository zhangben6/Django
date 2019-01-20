from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),

    url(r'^01-template/$',views.template_01),

    url(r'^static/$',views.static_views),




]