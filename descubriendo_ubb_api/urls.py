from django.contrib import admin
from django.urls import path, include
from visitas.views import registrar_visita, health
from usuarios.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('api/visitas/', registrar_visita),
    path('dashboard/', include('dashboard.urls')),
    path('login/', login_view, name='login'),
]
