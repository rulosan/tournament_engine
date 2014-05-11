from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/registro/', include('registro.urls', namespace="registro")),
    url(r'^api/torneo/', include('torneo.urls', namespace="torneo")),
)

urlpatterns += patterns('',
    url(r'^webui/', include('webui.urls', namespace="webui")),
    url(r'^admin/', include(admin.site.urls)),
)
