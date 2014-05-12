# -*- coding: utf-8 -*-
__author__ = 'rulo'

from registro import models
from rest_framework import serializers


class CompetidorSerializer (serializers.ModelSerializer):
    edad = serializers.CharField(source='get_edad', read_only=True)

    class Meta:
        model = models.Competidor
        fields = ('id',
                  'nombre',
                  'apellido_paterno',
                  'apellido_materno',
                  'fecha_nacimiento',
                  'edad',
                  'apodo',
                  'sexo',
                  'email')
        lookup_field = 'apodo'


class AcademiaSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Academia
        fields = ('id', 'nombre')


class ArteMarcialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArteMarcial
        fields = ('id', 'nombre')


class PracticaArteMarcialSerializer (serializers.ModelSerializer):

    class Meta:
        model = models.PracticaArteMarcial
        fields = ('arte_marcial',
                  'competidor',
                  'anhos_experiencia',
                  'meses_experiencia',
                  'academia',
                  'actual')

class DetailPracticaArteMarcialSerializer(serializers.ModelSerializer):
    arte_marcial = ArteMarcialSerializer(read_only=True)
    academia = AcademiaSerializer(read_only=True)
    class Meta:
        model = models.PracticaArteMarcial
        fields = ('arte_marcial',
                  'anhos_experiencia',
                  'meses_experiencia',
                  'academia',
                  'actual')


class PreParticipacionSerializer(serializers.ModelSerializer):
    """
        Sirve para tratar los datos cuando el usuario
        se preregistra, lo separo porque hay datos en
        la participacion que no puede llenar el Competidor
        y tienen que ser llenados por el staff del sistema
    """
    def save_object(self, obj, **kwargs):
        #incluir los campos que se tienen que generar desde el backend
        # fecha_registro, edad, categoria, si_pago = FAlse
        print obj
        super(PreParticipacionSerializer, self).save_object(obj, **kwargs)

    class Meta:
        model = models.Participacion
        fields = ('torneo',
                  'competidor',
                  'nivel',
                  'peso')
        read_only_fields = ('si_pago',
                            'edad',
                            'fecha_registro',
                            'categoria')
