# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from torneo import models
from torneo import serializers
from registro.models import Participacion
from registro.serializers import PostParticipacionSerializer


class TorneoViewSet(viewsets.ViewSet):
    def create(self, request, format=None):
        serializer = serializers.TorneoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk, format=None):
        queryset = models.Torneo.objects.all()
        torneo = get_object_or_404(queryset, pk=pk)
        serializer = serializers.TorneoSerializer(torneo)
        print serializer.data
        return Response(serializer.data)


class LocacionViewSet(viewsets.ViewSet):

    def create(self, request, format=None):
        serializer = serializers.LocacionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk, format=None):
        queryset = models.Locacion.objects.all()
        locacion = get_object_or_404(queryset, pk=pk)
        serializer = serializers.LocacionSerializer(locacion)
        return Response(serializer.data)


class TorneoParticipacion (viewsets.ViewSet):

    def detail(self, request, torneo_id, format=None):
        participaciones = Participacion.objects.filter(torneo__id=torneo_id)
        serializer = PostParticipacionSerializer(participaciones, many=True)
        return Response(serializer.data)
