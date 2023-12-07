from django.db import models

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length=100,primary_key=True)
    nombre_completo = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=100)