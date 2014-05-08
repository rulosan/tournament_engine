from django.shortcuts import render
from django.http import HttpResponse
import json


def index(request):
    return HttpResponse(json.dumps({'message':'Bienvenido al tournament_engine'}))