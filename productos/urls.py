from django.urls import path
from .views import ProductoListCreate, ProductoRetrieveUpdateDelete


urlpatterns = [
    path('productos', ProductoListCreate.as_view(), name="Create-Producto-List"),
    path('producto/<int:pk>/', ProductoRetrieveUpdateDelete.as_view(), name='producto-Details')
]