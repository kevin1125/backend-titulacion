from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100,primary_key=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=50, decimal_places=2)
    # meses_diferidos_plan = models.ForeignKey(max_length=100)
    
    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        db_table = 'Producto' 