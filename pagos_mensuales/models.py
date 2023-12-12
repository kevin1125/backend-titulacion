from django.db import models
from caja.models import Caja
from clientes.models import Cliente
from crear_pago.models import Crear_Pago
from plan.models import Plan


opciones_estado = [
    ('opcion1','Cancelado'),
    ('opcion2','Por pagar'),
]

# Create your models here.
class PagosMensuales(models.Model):
    pagos_mensuales = models.DecimalField(max_digits=20, decimal_places=2)
    vencimiento = models.DateField()
    estado = models.CharField(max_length=20,choices=opciones_estado, default='opcion2')
    total_cobrar = models.DecimalField(max_digits=20, decimal_places=2)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    crear_pago = models.ForeignKey(Crear_Pago, null=True, blank=True, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, null=True, blank=True, on_delete=models.CASCADE)
    caja = models.ForeignKey(Caja, null=True, blank=True, on_delete=models.CASCADE)

    
    

    
    class Meta:
        db_table = 'PagosMensuales'


    def __str__(self):
        return self.estado