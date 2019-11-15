from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
]