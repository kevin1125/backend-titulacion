from django.contrib.auth.models import User
from django.db import models
from pagos_mensuales.models import PagosMensuales



# Create your models here.
class Estado_Cuenta(models.Model):
      pagos_mensuales = models.ForeignKey(PagosMensuales,null=True,blank=True,on_delete=models.CASCADE)

class Meta:
        db_table = 'Estado_Cuenta' 