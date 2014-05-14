# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from registro import views
from rest_framework.routers import SimpleRouter

#urlpatterns = patterns('',
#    url(r'^competidor/$', views.CompetidorList.as_view()),
#    url(r'^competidor/(?P<pk>\d+)$', views.CompetidorDetail.as_view()),
#)

router = SimpleRouter()
router.register(r'academia', views.AcademiaViewSet, base_name='academia')
router.register(r'competidor', views.CompetidorViewSet, base_name='competidor')
router.register(r'artemarcial', views.ArteMarcialViewSet, base_name='artemarcial')
router.register(r'participacion', views.PreParticipacionViewSet, base_name='participacion')

urlpatterns = router.urls

urlpatterns += patterns('',
    url(r'^competidor/(?P<competidor_pk>\d+)/practica', views.PracticaArteMarcialViewSet.as_view({'get': 'detail',
                                                                                                  'post': 'create'})),
    url(r'^apodo/(?P<apodo>\w+)/available', views.ApodoViewSet.as_view({'get': 'retrieve'})),
)


#urlpatterns = format_suffix_patterns(urlpatterns)