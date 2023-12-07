from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('cedula', 'nombre_completo','email','direccion')  # Utiliza una tupla, no una cadena
