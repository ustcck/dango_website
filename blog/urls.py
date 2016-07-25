from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^time/$', views.time),
    url(r'^foo/(\d{4})/(\w+)/$', views.foo),
    url(r'^bar/(?P<id>\d{4})/(?P<name>\w+)/$', views.bar),

    url(r'^student_list/$', views.student_list),

]
