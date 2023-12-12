from rest_framework import serializers
from .models import Crear_Pago

class Crear_PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crear_Pago
        fields = ('fecha_inicio', 'total_pagar')  # Utiliza una tupla, no una cadena
