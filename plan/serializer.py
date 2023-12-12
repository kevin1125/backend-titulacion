from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ( 'meses_diferidos',)  # Utiliza una tupla, no una cadena
