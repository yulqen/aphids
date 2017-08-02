from django.conf.urls import url
from passes import views

urlpatterns = [
    url(r'^passes/$', views.pass_status_list),
    url(r'^passes/(?P<pk>[0-9]+)/$', views.pass_status_detail),
]
