from rest_framework import serializers
from .models import PagosMensuales

class PagosMensualesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagosMensuales
        fields = ('vencimiento', 'estado','total_cobrar')  # Utiliza una tupla, no una cadena