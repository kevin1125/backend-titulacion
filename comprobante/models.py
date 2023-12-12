from pagos_mensuales.models import PagosMensuales
from django.db import models


# Create your models here.
class Comprobante(models.Model):
    pagos_mensuales = models.ForeignKey(PagosMensuales,null=True,blank=True,on_delete=models.CASCADE)

class Meta:
        db_table = 'Comprobante' 