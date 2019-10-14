from django.db import models

# Create your models here.
from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=75)



class Ciudad(models.Model):
    nombre = models.CharField(max_length=75)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)


class Local(models.Model):
    nombre = models.CharField(max_length=200)
    dirección = models.CharField(max_length=300)
    tipo = models.CharField(max_length=15)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)


class Review(models.Model):
    dirección = models.CharField(max_length=300)
    mes = models.IntegerField
    año = models.IntegerField
    local = models.ManyToManyField(Local)

