"""About app urls file"""

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.about, name='about'),
]