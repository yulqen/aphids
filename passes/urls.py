from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from passes import views

urlpatterns = [
    url(r'^pass-status/$', views.PassStatusList.as_view()),
    url(r'^pass-status/(?P<pk>[0-9]+)/$', views.PassStatusDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
