from django.db import models

# Create your models here.
class Sobrevivente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_infectado = models.BooleanField()

# class Inventario(models.Model):
#      id nome quantidade pontos_unitario