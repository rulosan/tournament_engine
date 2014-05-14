# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from registro import models
from torneo.models import  Torneo
from registro import serializers
from datetime import datetime

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
        competidor = get_object_or_404(queryset, pk=pk)
        serializer = serializers.CompetidorSerializer(competidor)
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
        data = request.DATA
        data['competidor'] = competidor_pk
        ser = serializers.PracticaArteMarcialSerializer(data=data)
        if ser.is_valid():
            dd = ser.data
            lookup = {
                'academia__id': dd['academia'],
                'competidor__id': dd['competidor'],
                'arte_marcial__id': dd['arte_marcial']
            }
            count = models.PracticaArteMarcial.objects.filter(**lookup).count()
            if count == 0:
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Ya tienes esa arte marcial con esa academia'},
                                status=status.HTTP_403_FORBIDDEN)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def detail(self, request, competidor_pk, format=None):
        queryset = models.PracticaArteMarcial.objects.filter(competidor__id=competidor_pk)
        serializer = serializers.DetailPracticaArteMarcialSerializer(queryset, many=True)
        return Response(serializer.data)


#################################################################################
#  Apodos
#################################################################################

class ApodoViewSet(viewsets.ViewSet):
    """
        Sirve para cheacar si ya existe un apodo en el momento
        que se estan registrando
    """
    def retrieve(self, request, apodo, format=None):
        count = models.Competidor.objects.filter(apodo__exact=apodo).count()
        if count == 0:
            return Response({'available': True}, status=status.HTTP_200_OK)
        return Response({'available': False}, status=status.HTTP_403_FORBIDDEN)

#################################################################################
#  PArticiopaciones
#################################################################################

class PreParticipacionViewSet(viewsets.ViewSet):
    """
        Cuando el usuario se registra, pero solo
        puede llenar ciertos datos, ya que los demas
        datos tiene que ser confirmados por el staff
    """

    def create(self, request, format=None):
        serializer = serializers.PreParticipacionSerializer(data=request.DATA)
        if serializer.is_valid():
            data = serializer.data
            torneo = data['torneo']
            competidor = data['competidor']
            count_part = models.Participacion.objects.filter(torneo__id=torneo,
                                                             competidor__id=competidor).count()
            if count_part == 0:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'message': 'Ya existe una participacion en este torneo'},
                            status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostParticipacionViewSet(viewsets.ViewSet):
    """
        TODO: esta vista solo tiene que ser consultada
        por un usuario administrador o de staff del torneo
        ya que puede modificar los estados de la participacion
        si_pago , nivel, peso que son los definitivos
    """
    def create(self, request, format=None):
        pass