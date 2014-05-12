# -*- coding: utf-8 -*-

from django.db import models
from datetime import date

# Create your models here.

class Competidor(models.Model):
    HOMBRE = 'M'
    MUJER = 'F'
    SEXO = (
        (HOMBRE, 'masculino'),
        (MUJER, 'femenino'),
    )

    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    apodo = models.CharField(max_length=50, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default=HOMBRE)
    email = models.EmailField(max_length=100)

    def __unicode__(self):
        return "{nombre} {apellido_paterno} {apeqllido_materno}".format(**self.__dict__)

    def get_edad(self):
        tmp_edad = date.today() - self.fecha_nacimiento
        days = tmp_edad.days / 365
        return days

    class Meta:
        pass


class Academia(models.Model):
    nombre = models.CharField(max_length=150)


class ArteMarcial(models.Model):
    nombre = models.CharField(max_length=150)


class PracticaArteMarcial(models.Model):
    competidor = models.ForeignKey(Competidor)
    arte_marcial = models.ForeignKey(ArteMarcial)
    anhos_experiencia = models.PositiveSmallIntegerField()
    meses_experiencia = models.PositiveSmallIntegerField()
    academia = models.ForeignKey(Academia)
    actual = models.BooleanField(null=None)


class Participacion(models.Model):
    JUVENIL = 'JU'
    ADULTO = 'AD'
    SENIOR = 'SE'

    PRINCIPIANTE = 'PI'
    MEDIO = 'ME'
    AVANZADO = 'AV'

    CATEGORIAS = (
        (JUVENIL, 'Juvenil'),
        (ADULTO, 'Adulto'),
        (SENIOR, 'Senior'),
    )

    NIVEL = (
        (PRINCIPIANTE, 'Principiante'),
        (MEDIO, 'Medio'),
        (AVANZADO, 'Avanzado'),
    )

    torneo = models.ForeignKey('torneo.Torneo')
    competidor = models.ForeignKey(Competidor)
    fecha_registro = models.DateTimeField()
    edad = models.IntegerField()
    categoria = models.CharField(max_length=2, choices=CATEGORIAS, default=ADULTO)
    nivel = models.CharField(max_length=2, choices=NIVEL, default=PRINCIPIANTE)
    si_pago = models.BooleanField()
    peso = models.DecimalField(max_digits=3, decimal_places=3)
