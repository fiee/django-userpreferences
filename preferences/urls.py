from __future__ import absolute_import
from django.conf.urls import url
from django.contrib import admin
from preferences import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index),
    url(r'^media/(.*)$', views.media),
    url(r'^change/(?P<app>[a-z_\-]*)/(?P<pref>[a-z_\-]*)/(?P<new_value>.*)/$', views.change),
]
