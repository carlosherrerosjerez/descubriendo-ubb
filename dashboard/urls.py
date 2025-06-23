from django.urls import path
from .views import resumen_visitas

urlpatterns = [
    path('', resumen_visitas, name='dashboard'),
]
