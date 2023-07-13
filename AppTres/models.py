from django.db import models

# Create your models here.

class Area(models.Model):
    nombre = models.CharField(max_length=30)
    zona = models.CharField(max_length=30)
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    tipo_auto= models.CharField(max_length=40)
    
class Proovedor(models.Model):
    marca = models.CharField(max_length=30)
    producto = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entrgado = models.BooleanField()
    
    