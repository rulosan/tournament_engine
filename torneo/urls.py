__author__ = 'rulo'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^index', 'torneo.views.index', name="torneo-index"),
)
