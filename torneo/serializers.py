# -*- coding: utf-8 -*-
__author__ = 'rulo'

from torneo import models
from rest_framework import serializers


class TorneoSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Torneo
        fields = ('id',
                  'nombre',
                  'descripcion',
                  'fecha_realizacion',
                  'url_imagen')

class LocacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Locacion
        fields = ('id',
                  'calle',
                  'numero',
                  'numero_interior',
                  'municipio',
                  'estado')