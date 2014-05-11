from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from registro import models
from registro import serializers

"""
 def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
"""


###########################
# Vistas del Competidor
###########################

class CompetidorViewSet (viewsets.ViewSet):

    def list(self, request, format=None):
        queryset = models.Competidor.objects.all()
        serializer = serializers.CompetidorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, format=None):
        queryset = models.Competidor.objects.all()
        competidor = get_object_or_404(queryset,pk=pk)
        serializer = models.CompetidorSerializer(competidor)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = serializers.CompetidorSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###########################
# Vistas del Academia
###########################

class AcademiaViewSet (viewsets.ViewSet):

    def list(self, request, format=None):
        queryset = models.Academia.objects.all()
        serializer = serializers.AcademiaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, format=None):
        queryset = models.Academia.objects.all()
        academia = get_object_or_404(queryset, pk=pk)
        serializer = serializers.AcademiaSerializer(academia)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = serializers.AcademiaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


#################################################################################
# Vistas de las Artes Marciales
#################################################################################

class ArteMarcialViewSet (viewsets.ViewSet):

    def list(self, request, format=None):
        queryset = models.ArteMarcial.objects.all()
        serializer = serializers.ArteMarcialSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        s = serializers.ArteMarcialSerializer(data=request.DATA)
        if s.is_valid():
            s.save()
            return Response(s.data , status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, format=None):
        queryset = models.ArteMarcial.objects.all()
        arteMarcial = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ArteMarcialSerializer(arteMarcial)
        return Response(serializer.data)


#################################################################################
# Vistas del Practica Arte Marcial
#################################################################################

class PracticaArteMarcialViewSet(viewsets.ViewSet):

    def create (self, request, competidor_pk, format=None):
        # TODO : probar este metodo para ver como se le agrega el competidor_pk
        ser = serializers.PracticaArteMarcialSerializer(data=request.DATA)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def detail(self, request, competidor_pk, format=None):
        queryset = models.PracticaArteMarcial.objects.filter(competidor__id=competidor_pk)
        serializer = serializers.DetailPracticaArteMarcialSerializer(queryset, many=True)
        return Response(serializer.data)



class EntrenaViewSet(viewsets.ViewSet):

    def create(self, request, competidor_pk, format=None):
        pass

    def detail(self, request, competidor_pk, format=None):
        pass
