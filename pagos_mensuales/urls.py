from django.urls import path
from .views import PagosMensualesListCreate, PagosMensualesRetrieveUpdateDelete


urlpatterns = [
    path('pagosmensuales', PagosMensualesListCreate.as_view(), name="Create-PagosMensuales-List"),
    path('pagomensual/<int:pk>/', PagosMensualesRetrieveUpdateDelete.as_view(), name='pagosmensuales-Details')
]