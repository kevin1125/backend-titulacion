from django.urls import path
from .views import ClienteListCreate, ClienteRetrieveUpdateDelete


urlpatterns = [
    path('clientes', ClienteListCreate.as_view(), name="Create-Cliente-List"),
    path('cliente/<int:pk>/', ClienteRetrieveUpdateDelete.as_view(), name='cliente-Details')
]