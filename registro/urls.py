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

urlpatterns = router.urls

urlpatterns += patterns('',
    url(r'^competidor/(?P<competidor_pk>\d+)/practica', views.PracticaArteMarcialViewSet.as_view({'get': 'detail',
                                                                                             'post': 'create'})),
    url(r'^competidor/(?P<competidor_pk>\d+)/entrena', views.EntrenaViewSet.as_view({'get': 'detail',
                                                                                     'post':'create'})),
)


#urlpatterns = format_suffix_patterns(urlpatterns)