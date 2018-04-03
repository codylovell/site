"""Projects app urls file"""

from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^projects/$', views.projects, name='projects'),
  url(r'^projects/(?P<pk>\d+)/project_detail/$', views.project_detail, name='project_detail'),
]