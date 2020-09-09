from django.db import models

# Create your models here.

class TasaMaximaConvencional(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    valor = models.FloatField()
    fecha = models.DateField()
    hasta = models.DateField()
    tipo = models.IntegerField()