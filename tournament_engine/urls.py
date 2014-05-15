# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/registro/', include('registro.urls', namespace="registro")),
    url(r'^api/proceso/', include('torneo.urls', namespace="proceso")),
)

urlpatterns += patterns('',
    url(r'^webui/', include('webui.urls', namespace="webui")),
    url(r'^admin/', include(admin.site.urls)),
)
