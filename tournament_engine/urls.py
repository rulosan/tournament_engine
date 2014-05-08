from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'registro/', include('registro.urls', namespace="registro")),
    url(r'torneo/', include('torneo.url', namespace="torneo")),
    url(r'^admin/', include(admin.site.urls)),
)
