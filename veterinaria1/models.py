from django.db import models

# Create your models here.
class Veterinaria (models.Model):
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    encargado=models.CharField(max_length=40)
    capacidad=models.IntegerField
    ocupacion=models.IntegerField
    
class Cliente (models.Model):
    clientenro=models.IntegerField
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    
class Animal (models.Model):
    nombre=models.CharField(max_length=40)
    especie=models.CharField(max_length=40)
    raza=models.CharField(max_length=40)
    antecedentes=models.CharField(max_length=500)
