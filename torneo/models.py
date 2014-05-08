from django.db import models

# Create your models here.


class Torneo(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    fecha_realizacion = models.DateTimeField()
    url_imagen = models.URLField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        pass


class Locacion(models.Model):
    calle = models.CharField(max_length=200)
    numero = models.IntegerField()
    numero_interior = models.IntegerField(null=True)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __unicode__(self):
        return " {calle} , {numero}, {municipio}".format(**self.__dict__)

    class Meta:
        pass

class Combate ( models.Model ):
    KO = 'KO'
    TKO = 'TKO'
    SUMISION = 'SUB'
    DESICION = 'DEC'
    EMPATE = 'EMP'
    NO_SE_PRESENTO = 'NP'
    EN_CURSO = 'EC'
    NO_REALIZADO = 'NR'

    TIPOS_VICTORIA = (
        (KO, 'KO'),
        (TKO, 'TKO'),
        (SUMISION, 'Sumision'),
        (DESICION, 'Desicion'),
        (EMPATE, 'Empate') ,
        (NO_SE_PRESENTO,'No se presento'),
        (EN_CURSO, 'En curso'),
        (NO_REALIZADO, 'No realizado'),
    )

    torneo = models.ForeignKey(Torneo)
    combate_anterior_1 = models.ForeignKey('torneo.Combate', null=True, related_name='ant_1')
    combate_anterior_2 = models.ForeignKey('torneo.Combate', null=True, related_name='ant_2')
    competidor_azul = models.ForeignKey('registro.Competidor', related_name='azul')
    competidor_rojo = models.ForeignKey('registro.Competidor', related_name='rojo')
    competidor_ganador = models.ForeignKey('registro.Competidor', related_name='ganador')
    fecha_realizacion = models.DateTimeField()
    victoria = models.CharField(max_length=3, choices=TIPOS_VICTORIA, default=EN_CURSO)

    class Meta:
        pass