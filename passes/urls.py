from django.conf.urls import url
from passes import views

urlpatterns = [
    url(r'^passes/pass-status/$', views.pass_status_list),
    url(r'^passes/pass-status/(?P<pk>[0-9]+)/$', views.pass_status_detail),
]
