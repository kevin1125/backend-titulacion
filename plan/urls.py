from django.urls import path
from plan.views import PlanListCreate, PlanRetrieveUpdateDelete  
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('planes', PlanListCreate.as_view(), name="Create-Plan-List"),
    path('plan/<int:pk>/', PlanRetrieveUpdateDelete.as_view(), name='plan-Details')
]