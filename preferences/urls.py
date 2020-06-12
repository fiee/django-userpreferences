from django.urls import path
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    path('', views.index),
    path('change/<slug:app>/<slug:pref>/<new_value>/', views.change),
]
