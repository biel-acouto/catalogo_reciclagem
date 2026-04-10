from django.contrib import admin
from django.urls import path
from catalogo import views  # Importamos a nossa view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Rota para a página inicial
]
