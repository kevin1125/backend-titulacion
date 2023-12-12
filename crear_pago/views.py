from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Crear_Pago
from .serializer import Crear_PagoSerializer

# Create your views here.
class Crear_PagoListCreate(generics.ListCreateAPIView):
    queryset = Crear_Pago.objects.all()
    serializer_class = Crear_PagoSerializer


class Crear_PagoRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crear_Pago.objects.all()
    serializer_class = Crear_PagoSerializer