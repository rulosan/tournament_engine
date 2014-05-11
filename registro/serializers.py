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
        fields = ('competidor',
                  'arte_marcial',
                  'anhos_experiencia',
                  'meses_experiencia')

class DetailPracticaArteMarcialSerializer(serializers.ModelSerializer):
    arte_marcial = ArteMarcialSerializer(read_only=True)
    class Meta:
        model = models.PracticaArteMarcial
        fields = ('arte_marcial',
                  'anhos_experiencia',
                  'meses_experiencia')