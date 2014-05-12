# -*- coding: utf-8 -*-

__author__ = 'rulo'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from torneo import views


router = SimpleRouter()
router.register('torneo', views.TorneoViewSet, base_name='torneo')
router.register('locacion', views.LocacionViewSet, base_name='locacion')
urlpatterns = router.urls
