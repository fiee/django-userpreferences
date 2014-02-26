from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('preferences.views',
    url(r'^$', 'index'),
    url(r'^media/(.*)$','media'),
    url(r'^change/(?P<app>[a-z_\-]*)/(?P<pref>[a-z_\-]*)/(?P<new_value>.*)/$','change'),
)
