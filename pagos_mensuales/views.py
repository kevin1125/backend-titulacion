from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import  PagosMensuales
from .serializer import  PagosMensualesSerializer

# Create your views here.
class PagosMensualesListCreate(generics.ListCreateAPIView):
    queryset = PagosMensuales.objects.all()
    serializer_class = PagosMensualesSerializer


class PagosMensualesRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PagosMensuales.objects.all()
    serializer_class = PagosMensualesSerializer