from django.urls import path
from .views import ClienteListCreate, ClienteRetrieveUpdateDelete
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('docs/', include_docs_urls(title = 'Backend Api')),
    path('clientes', ClienteListCreate.as_view(), name="Create-Cliente-List"),
    path('cliente/<int:pk>/', ClienteRetrieveUpdateDelete.as_view(), name='cliente-Details')
]