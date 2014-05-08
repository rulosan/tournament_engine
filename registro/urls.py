
from django.conf.urls import patterns, url

from registro import views

urlpatterns = patterns('',


	# Url para ver el menu principal
	url (r'^$', 'registro.views.index' , name='index'),

	# Url para logearse como usuario
	url(r'^acceder/', 'registro.views.acceder', name='acceder'),

	# Url para hacer el registro del usuario nuevo
	url(r'^registro/' , views.CompetidorCreate.as_view() , name='registro'),

	# Url para ver el perfil del usuario
	url(r'^(?P<user_id>\d+)/perfil/$', 'registro.views.perfil' , name='perfil'),
)