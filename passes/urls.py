from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from passes import views

urlpatterns = [
    url(r'^pass-status/$', views.pass_status_list),
    url(r'^pass-status/(?P<pk>[0-9]+)/$', views.pass_status_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
