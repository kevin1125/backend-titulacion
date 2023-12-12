from django.urls import path
from crear_pago.views import Crear_PagoListCreate, Crear_PagoRetrieveUpdateDelete
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('crear_pagos', Crear_PagoListCreate.as_view(), name="Create-Crear_Pago-List"),
    path('crear_pago/<int:pk>/', Crear_PagoRetrieveUpdateDelete.as_view(), name='Crear_Pago-Details')
]