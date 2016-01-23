from django.conf.urls import url

from .core import views

urlpatterns = [
    url(r'^(?P<name>[a-z0-9-]+/[a-z0-9-]+)$', views.repository_detail),
    url(r'^(?P<pk>\d+)$', views.repository_detail),
]
