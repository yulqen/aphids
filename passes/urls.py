from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from passes import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^pass-status/$', views.PassStatusList.as_view(), name='pass-status-list'),
    url(r'^pass-status/(?P<pk>[0-9]+)/$', views.PassStatusDetail.as_view()),
    url(r'^person/$', views.PersonList.as_view(), name='person-list'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^application-status/$', views.ApplicationStatusList.as_view(), name='application-status-list'),
    url(r'^application-status/(?P<pk>[0-9]+)/$', views.ApplicationStatusDetail.as_view()),
    url(r'^proof-id-type/$', views.ProofIdTypeList.as_view(), name='proof-id-type-list'),
    url(r'^proof-id-type/(?P<pk>[0-9]+)/$', views.ProofIdTypeDetail.as_view()),
    url(r'^pass-type/$', views.PassTypeList.as_view(), name='pass-type-list'),
    url(r'^pass-type/(?P<pk>[0-9]+)/$', views.PassTypeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
