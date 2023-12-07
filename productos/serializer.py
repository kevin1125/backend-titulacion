from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre_producto', 'cantidad','precio')  # Utiliza una tupla, no una cadena
