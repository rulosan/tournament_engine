from django.shortcuts import render

from django.views.generic.edit import CreateView

from registro import models
# Create your views here.


class CompetidorCreate (CreateView):
	model = models.Competidor
	fields = [
		'nombre',
		'apellido_paterno',
		'apellido_materno',
		'fecha_nacimiento',
		'apodo',
		'sexo',
		'email',
	]


def index (request):
	return render(request,'registro/index.html')

def acceder (request):
	return render(request,'registro/acceder.html')

def registro (request):
	return render(request,'registro/registro.html')

def perfil (request, user_id):
	return render(request,'registro/perfil.html')