# -*- coding: utf-8 -*-
__author__ = 'rulo'

from django.conf.urls import patterns, url
from webui import views

urlpatterns = patterns('',
    url(r'^index/$', views.index , name='index'),
)
