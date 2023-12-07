from django.shortcuts import render
from rest_framework import generics
from .models import Cliente
from .serializer import ClienteSerializer

# Create your views here.
class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer