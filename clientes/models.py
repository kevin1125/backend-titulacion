from django.db import models

from productos.models import Producto

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length=100,primary_key=True)
    nombre_completo = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=100)
    nombre_producto = models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        db_table = 'Cliente' 